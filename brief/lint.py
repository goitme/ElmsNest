#!/usr/bin/env python3
"""Lint ElmsNest v2 theme files. Usage: python3 brief/lint.py [theme_dir]
Checks every sections/*.liquid + snippets/*.liquid + templates/index.json under theme_dir."""
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
# index.json ↔ schema
ij=root+'/templates/index.json'
if os.path.exists(ij):
    try:
        d=json.load(open(ij,encoding='utf-8'))
        for sid,sec in d['sections'].items():
            t=sec['type']; sch=schemas.get(t)
            if not sch: err('index.json',f'section "{sid}" type {t} has no file'); continue
            ok_ids={x.get('id') for x in sch.get('settings',[])}
            for k in sec.get('settings',{}):
                if k not in ok_ids: err('index.json',f'{sid}.settings.{k} not in {t} schema')
            btypes={b['type']:b for b in sch.get('blocks',[])}
            for bid,b in sec.get('blocks',{}).items():
                if b['type'] not in btypes: err('index.json',f'{sid} block {bid} type {b["type"]} not in {t} schema'); continue
                bok={x.get('id') for x in btypes[b['type']].get('settings',[])}
                for k in b.get('settings',{}):
                    if k not in bok: err('index.json',f'{sid}.{bid}.settings.{k} not in block {b["type"]} schema')
            if sec.get('blocks') and set(sec.get('block_order',[]))!=set(sec['blocks']): err('index.json',f'{sid} block_order mismatch')
        if set(d['order'])!=set(d['sections']): err('index.json','order/sections mismatch')
    except Exception as e: err('index.json',f'invalid: {e}')
print('LINT', 'FAIL' if bad else 'OK', f'({bad} issues)')
sys.exit(1 if bad else 0)
