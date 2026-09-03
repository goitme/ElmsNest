#!/usr/bin/env python3
"""Lint ElmsNest v2 theme files. Usage: python3 brief/lint.py [theme_dir]
Checks every sections/elmsnest-v2-*.liquid + snippets/elmsnest-v2-*.liquid (which includes the PDP set,
sections/elmsnest-v2-pdp-* and snippets/elmsnest-v2-pdp-*, and the COLLECTION set,
sections/elmsnest-v2-coll-* and snippets/elmsnest-v2-coll-*, all globbed explicitly below), every
templates/*.json + templates/customers/*.json + sections/*-group.json under theme_dir (settings <->
schema per section type, using the verbatim Kalles dumps in brief/inventory/theme-src/sections/ for
non-env2 sections), that templates/product.elmsnest.json matches the PDP section schemas (WINNING-SPEC
§8.1: the PDP template file is product.elmsnest.json, NOT product.json), that templates/collection.json
matches the collection section schemas (collection WINNING-SPEC §5.1 — one file serves all five URLs),
and that no file anywhere under theme_dir contains the sequence of three double quotes (GraphQL block
string).

The strict rules (applied to elmsnest-v2-pdp-*, elmsnest-v2-coll-* and the two ground snippets only, so
nothing already shipped on the homepage can regress):
no "בוואטסאפ" outside the photo-cta snippet while settings.whatsapp_number is empty (BRIEF §3, do-not
§6.9) · no compare-at / sale UI (§6.5) · no <bdi> split across a slash pair (§6.17) · logical CSS
properties only (an RTL app flips physical ones) · no raw product.images[0] (the never-use ledger lives
in elmsnest-v2-pdp-image, §3.5) · radius 0 except pills (§6.14)."""
import re,json,glob,os,sys
root=sys.argv[1] if len(sys.argv)>1 else '/home/user/ElmsNest/theme'
bad=0
def err(f,msg):
    global bad; bad+=1; print(f"  !! {f}: {msg}")
schemas={}
env2_files=sorted(set(
    glob.glob(root+'/sections/elmsnest-v2-*.liquid')+glob.glob(root+'/snippets/elmsnest-v2-*.liquid')+
    glob.glob(root+'/sections/elmsnest-v2-pdp-*.liquid')+glob.glob(root+'/snippets/elmsnest-v2-pdp-*.liquid')+
    glob.glob(root+'/sections/elmsnest-v2-coll-*.liquid')+glob.glob(root+'/snippets/elmsnest-v2-coll-*.liquid')))
pdp_sections=sorted(os.path.basename(f)[:-7] for f in glob.glob(root+'/sections/elmsnest-v2-pdp-*.liquid'))
coll_sections=sorted(os.path.basename(f)[:-7] for f in glob.glob(root+'/sections/elmsnest-v2-coll-*.liquid'))
for f in env2_files:
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
                nm=j.get('name','')
                if len(nm)>25: err(name,f'schema name {nm!r} is {len(nm)} chars — the limit is 25')
                # Shopify caps a setting label at 70 characters and rejects the whole file otherwise
                def _labels(items,where):
                    for it in items or []:
                        lb=it.get('label')
                        if isinstance(lb,str) and len(lb)>70:
                            err(name,f'{where} setting {it.get("id")} label is {len(lb)} chars — Shopify caps a label at 70')
                _labels(j.get('settings'),'section')
                for _b in j.get('blocks',[]) or []:
                    _labels(_b.get('settings'),'block '+str(_b.get('type')))
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
# ---- strict rules (elmsnest-v2-pdp-*, elmsnest-v2-coll-*, the grounds): applied nowhere else, so the
#      shipped homepage cannot regress ----
PHYS=re.compile(r'(?<![-\w])(margin|padding|border)-(left|right)\s*:|(?<![-\w])(left|right)\s*:\s*[-0-9a-z]|text-align\s*:\s*(left|right)')
PDPSET=('elmsnest-v2-pdp-','elmsnest-v2-ground-product','elmsnest-v2-coll-','elmsnest-v2-ground-collection')
for f in [x for x in env2_files if os.path.basename(x).startswith(PDPSET)]:
    s=open(f,encoding='utf-8').read(); name=os.path.basename(f)
    body=re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}','',s,flags=re.S)
    if 'בוואטסאפ' in body and name!='elmsnest-v2-pdp-photo-cta.liquid':
        err(name,'contains "בוואטסאפ" — settings.whatsapp_number is empty; the only file allowed to name that channel is elmsnest-v2-pdp-photo-cta.liquid (BRIEF §3)')
    for token in ('compare_at_price','compare_at','hidden_badges','on_sale','מבצע'):
        if token in body: err(name,f'sale UI token "{token}" — there are no sales: no badge, no strikethrough, no compare-at (§6.5)')
    if re.search(r'</bdi>\s*/\s*<bdi>',body): err(name,'<bdi> split across a slash pair — use ONE <bdi>6W/12W</bdi> (§6.17)')
    for blk in re.findall(r'\{%-?\s*stylesheet\s*-?%\}(.*?)\{%-?\s*endstylesheet',body,re.S)+re.findall(r'<style[^>]*>(.*?)</style>',body,re.S):
        css=re.sub(r'/\*.*?\*/','',blk,flags=re.S)
        m=PHYS.search(css)
        if m: err(name,f'physical CSS property "{m.group(0).strip()}" — logical properties only, an RTL app flips physical ones (§3.3)')
        for r in set(re.findall(r'border-radius\s*:\s*([^;}]+)',css)):
            if r.strip() not in ('0','0px','999px','50%','inherit','var(--env2-radius,0)'):
                err(name,f'border-radius:{r.strip()} — radius 0 everywhere except pills (999px) (§6.14)')
    # Ruby Liquid closes an output tag at the FIRST '}' (VariableIncompleteEnd = /\}\}?/), so a
    # {placeholder} inside {{ ... }} is a Shopify parse error even though python-liquid accepts it.
    for m in re.finditer(r'\{\{',s):
        j=s.find('}',m.end())
        if j>=0 and s[j:j+2]!='}}':
            err(name,f'output tag closes on a single "}}" at line {s.count(chr(10),0,m.start())+1} — a {{placeholder}} inside {{{{ … }}}} is a Shopify Liquid parse error; substitute inside an assign tag')
            break
    if re.search(r'product\.images\[\s*0\s*\]',body):
        err(name,'raw product.images[0] — resolve every slot through elmsnest-v2-pdp-image so a never-use index 0 can never render (§3.5)')
    small=[x for x in re.findall(r'font-size\s*:\s*([0-9.]+)px',body) if float(x)<11.5]
    if small: print(f"  .. {name}: font-size below 11.5px {sorted(set(small))} — captions have a 13px floor, labels 11.5px (§3.2)")

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
PDP_ORDER=["pdp_stage","pdp_fit","pdp_night","pdp_ledger","pdp_facts","pdp_terms","pdp_ask","pdp_related"]
# collection WINNING-SPEC §5.1 — one templates/collection.json serves all five URLs; the sections branch
# on collection.handle through their own unit_mode defaults, never through a template suffix.
COLL_ORDER=["coll_scene","coll_ruler","coll_bands","coll_span","coll_ledger","coll_terms","coll_goodnight"]
def check_pdp_template():
    path=os.path.join(root,'templates','product.elmsnest.json')
    if not os.path.exists(path):
        err('templates/product.elmsnest.json','missing — the PDP template file is product.elmsnest.json, never product.json (WINNING-SPEC §8.1)'); return
    if os.path.exists(os.path.join(root,'templates','product.json')):
        err('templates/product.json','must not exist — all 27 products carry templateSuffix "elmsnest" and templateSuffix is shared with the LIVE theme (§8.1)')
    try: d=json.loads(strip_header(open(path,encoding='utf-8').read()))
    except Exception: return          # check_template already reported the JSON error
    secs=d.get('sections',{}); order=d.get('order',[])
    used=[t for t in (v.get('type') for v in secs.values()) if t and t.startswith('elmsnest-v2-pdp-')]
    for t in used:
        if not os.path.exists(os.path.join(root,'sections',t+'.liquid')):
            err('templates/product.elmsnest.json',f'section type {t} has no sections/{t}.liquid — Shopify rejects the template on upsert')
    if len(pdp_sections)>=8:          # the build has landed: the template must be the §5 list, in order
        if order!=PDP_ORDER:
            err('templates/product.elmsnest.json',f'order is {order} — WINNING-SPEC §5 wants {PDP_ORDER}')
        for sid,want in zip(PDP_ORDER,['elmsnest-v2-pdp-'+x.split('_',1)[1] for x in PDP_ORDER]):
            if secs.get(sid,{}).get('type')!=want:
                err('templates/product.elmsnest.json',f'section "{sid}" should be type {want}')
    elif used:
        print(f'  .. templates/product.elmsnest.json: {len(pdp_sections)}/8 PDP sections built — order/type check deferred')
    else:
        print('  .. templates/product.elmsnest.json: still the v1 template (no elmsnest-v2-pdp-* section) — nothing to check yet')

def check_collection_template():
    path=os.path.join(root,'templates','collection.json')
    if not os.path.exists(path):
        err('templates/collection.json','missing — one file serves all five collection URLs (§5.1)'); return
    if glob.glob(root+'/templates/collection.*.json'):
        err('templates/collection.json','a collection.<suffix>.json exists — §5.1: no per-collection template suffix is in use, one file serves all five URLs')
    try: d=json.loads(strip_header(open(path,encoding='utf-8').read()))
    except Exception: return          # check_template already reported the JSON error
    secs=d.get('sections',{}); order=d.get('order',[])
    used=[t for t in (v.get('type') for v in secs.values()) if t and t.startswith('elmsnest-v2-coll-')]
    for t in used:
        if not os.path.exists(os.path.join(root,'sections',t+'.liquid')):
            err('templates/collection.json',f'section type {t} has no sections/{t}.liquid — Shopify rejects the template on upsert')
    if len(coll_sections)>=7:         # the build has landed: the template must be the §5.1 list, in order
        if order!=COLL_ORDER:
            err('templates/collection.json',f'order is {order} — collection WINNING-SPEC §5.1 wants {COLL_ORDER}')
        for sid in COLL_ORDER:
            want='elmsnest-v2-coll-'+sid.split('_',1)[1]
            if secs.get(sid,{}).get('type')!=want:
                err('templates/collection.json',f'section "{sid}" should be type {want}')
        for sid,sec in secs.items():
            t=sec.get('type') or ''
            if t in ('main-collection','main-heading','top-list-collections') or t.startswith('collections_list'):
                err('templates/collection.json',f'section "{sid}" type {t} is retired by §5.4 — remove it from the template (the file stays on the theme)')
    elif used:
        print(f'  .. templates/collection.json: {len(coll_sections)}/7 collection sections built — order/type check deferred')
    else:
        print('  .. templates/collection.json: still the Kalles template (no elmsnest-v2-coll-* section) — nothing to check yet')

for tj in sorted(glob.glob(root+'/templates/*.json')+glob.glob(root+'/templates/customers/*.json')+glob.glob(root+'/sections/*-group.json')):
    check_template(tj)
check_pdp_template()
check_collection_template()
print('LINT', 'FAIL' if bad else 'OK', f'({bad} issues)')
sys.exit(1 if bad else 0)
