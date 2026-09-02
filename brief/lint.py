#!/usr/bin/env python3
"""Lint ElmsNest v2 theme files. Usage: python3 brief/lint.py [theme_dir]
Checks every sections/elmsnest-v2-*.liquid + snippets/elmsnest-v2-*.liquid, every templates/*.json +
templates/customers/*.json + sections/*-group.json under theme_dir (settings <-> schema per section type,
using the verbatim Kalles dumps in brief/inventory/theme-src/sections/ for non-env2 sections), and that
no file anywhere under theme_dir contains the sequence of three double quotes (GraphQL block string)."""
import re,json,glob,os,sys
root=sys.argv[1] if len(sys.argv)>1 else '/home/user/ElmsNest/theme'
bad=0
def err(f,msg):
    global bad; bad+=1; print(f"  !! {f}: {msg}")
schemas={}
for f in sorted(glob.glob(root+'/sections/elmsnest-v2-*.liquid')+glob.glob(root+'/snippets/elmsnest-v2-*.liquid')):
    s=open(f,encoding='utf-8').read(); name=os.path.basename(f)
    if '"""' in s: err(name,'contains """ (breaks GraphQL block string upload)')
    for tag in ('if','unless','for','case','capture','comment','schema','stylesheet','javascript','style','form','paginate'):
        o=len(re.findall(r'\{%-?\s*'+tag+r'(?![a-z_])',s)); c=len(re.findall(r'\{%-?\s*end'+tag+r'\s*-?%\}',s))
        if o!=c: err(name,f'unbalanced {tag}: {o} open / {c} end')
    for blk in ('stylesheet','javascript'):
        for m in re.finditer(r'\{%-?\s*'+blk+r'\s*-?%\}(.*?)\{%-?\s*end'+blk+r'\s*-?%\}',s,re.S):
            if re.search(r'\{\{|\{%',m.group(1)): err(name,f'Liquid tags inside {{% {blk} %}} block (not rendered there)')
    if '/sections/' in f:
        m=re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}',s,re.S)
        if not m: err(name,'no {% schema %}')
        else:
            try:
                j=json.loads(m.group(1)); schemas[name.replace('.liquid','')]=j
                ids=[x.get('id') for x in j.get('settings',[]) if x.get('id')]
                if len(ids)!=len(set(ids)): err(name,'duplicate setting ids')
                if not j.get('presets'): err(name,'no presets (section will not appear in the theme editor)')
            except Exception as e: err(name,f'schema JSON invalid: {e}')
        if not re.search(r'id="env2-',s): err(name,'no id="env2-…" anchor on the section root')
        if 'scroll-margin-top' not in s: err(name,'no scroll-margin-top for the sticky header')
        css=re.search(r'\{%-?\s*stylesheet\s*-?%\}(.*?)\{%-?\s*endstylesheet',s,re.S)
        if css:
            sel=re.findall(r'(?m)^\s*([.#][A-Za-z0-9_-]+)',css.group(1))
            leak=[x for x in sel if not x.startswith('.env2-')]
            if leak: err(name,f'unprefixed selectors in stylesheet: {sorted(set(leak))[:6]}')
        if re.search(r'\{\{\s*block\.',s) and 'block.shopify_attributes' not in s: err(name,'blocks used but no block.shopify_attributes')
        if re.search(r'#2b2118|#f7f0e6',s,re.I): print(f"  .. {name}: contains v1 brown/cream hex — check it is not a surface")
# ---- no file under theme/ may contain the GraphQL block-string terminator ----
for f in sorted(glob.glob(root+'/**/*',recursive=True)):
    if os.path.isfile(f) and '"""' in open(f,encoding='utf-8',errors='replace').read():
        err(os.path.relpath(f,root),'contains three double quotes (breaks GraphQL block string upload)')
# ---- template JSON ↔ section schema (env2 sections from theme/, Kalles sections from the theme-src dumps) ----
SRC=os.path.join(os.path.dirname(os.path.abspath(__file__)),'inventory','theme-src','sections')
def load_schema(t):
    if t in schemas: return schemas[t]
    p=os.path.join(SRC,t+'.liquid')
    if not os.path.exists(p): return None
    m=re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}',open(p,encoding='utf-8').read(),re.S)
    if not m: return None
    txt=re.sub(r'/\*.*?\*/','',m.group(1),flags=re.S)      # Kalles schemas carry /* commented-out */ settings
    txt=re.sub(r',(\s*[\]}])',r'\1',txt)                    # ...and trailing commas
    try: schemas[t]=json.loads(txt)
    except Exception as e: err(t+'.liquid',f'dumped schema JSON invalid: {e}'); schemas[t]=None
    return schemas[t]
def strip_header(txt):
    return re.sub(r'^\s*/\*.*?\*/\s*','',txt,count=1,flags=re.S)
def check_template(path):
    name=os.path.relpath(path,root)
    try: d=json.loads(strip_header(open(path,encoding='utf-8').read()))
    except Exception as e: err(name,f'invalid JSON: {e}'); return
    secs=d.get('sections',{})
    for sid,sec in secs.items():
        t=sec.get('type'); sch=load_schema(t)
        if sch is None: print(f'  .. {name}: section "{sid}" type {t}: no schema dumped in theme-src — settings not checked'); continue
        ok_ids={x.get('id') for x in sch.get('settings',[])}
        for k in sec.get('settings',{}):
            if k not in ok_ids: err(name,f'{sid}.settings.{k} not in {t} schema')
        btypes={b.get('type'):b for b in sch.get('blocks',[])}
        open_blocks=any(b.get('type') in ('@theme','@app') for b in sch.get('blocks',[]))
        for bid,b in sec.get('blocks',{}).items():
            bt=b.get('type')
            if bt not in btypes or bt.startswith('_') or bt.startswith('shopify://'):
                if open_blocks or bt.startswith('_') or bt.startswith('shopify://'): continue   # theme blocks (blocks/_*.liquid) / app blocks: schema lives elsewhere
                err(name,f'{sid} block {bid} type {bt} not in {t} schema'); continue
            bok={x.get('id') for x in btypes[bt].get('settings',[])}
            if not bok: print(f'  .. {name}: {sid}.{bid} block type {bt} has no settings in the dumped {t} schema — settings not checked'); continue
            for k in b.get('settings',{}):
                if k not in bok: err(name,f'{sid}.{bid}.settings.{k} not in block {bt} schema')
        if sec.get('blocks') and not set(sec.get('block_order',[]))<=set(sec['blocks']): err(name,f'{sid} block_order names a block that does not exist')   # static (content_for) blocks are absent from block_order by design
    if set(d.get('order',[]))!=set(secs): err(name,'order/sections mismatch')
for tj in sorted(glob.glob(root+'/templates/*.json')+glob.glob(root+'/templates/customers/*.json')+glob.glob(root+'/sections/*-group.json')):
    check_template(tj)
print('LINT', 'FAIL' if bad else 'OK', f'({bad} issues)')
sys.exit(1 if bad else 0)
