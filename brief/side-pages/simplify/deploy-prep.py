#!/usr/bin/env python3
"""Prepare the SIMPLIFY deploy: one GraphQL themeFilesUpsert mutation per file, in DEPLOY.md order, written to
<out>/NN-<name>.graphql so each can be pasted verbatim into the Shopify mutation tool. Refuses any file containing
the block-string terminator. Prints the ordered list with local sizes and md5 (to compare with Shopify's checksumMd5)."""
import os,sys,hashlib,json,re
ROOT='/home/user/ElmsNest/theme'; OUT=sys.argv[1] if len(sys.argv)>1 else '/home/user/ElmsNest/brief/side-pages/simplify/deploy'
THEME='gid://shopify/OnlineStoreTheme/154726400174'
ORDER=[
 # 1 snippets
 'snippets/elmsnest-s-skin.liquid','snippets/elmsnest-s-place.liquid','snippets/elmsnest-s-contact.liquid','snippets/elmsnest-s-terms.liquid',
 'snippets/elmsnest-s-pdp-kicker.liquid','snippets/elmsnest-s-pdp-unit.liquid','snippets/elmsnest-s-pdp-terms-line.liquid','snippets/elmsnest-s-pdp-notfor.liquid',
 # 2 sections
 'sections/elmsnest-s-collections.liquid','sections/elmsnest-s-products.liquid','sections/elmsnest-s-fit.liquid','sections/elmsnest-s-terms.liquid',
 'sections/elmsnest-s-coll-header.liquid','sections/elmsnest-s-guide-strip.liquid','sections/elmsnest-s-pdp-facts.liquid','sections/elmsnest-v2-hero.liquid',
 # 3 layout / settings / footer
 'layout/theme.liquid','config/settings_data.json','sections/footer-group.json','sections/header-group.json',
 # 4 templates
 'templates/index.json','templates/collection.json','templates/product.elmsnest.json',
]
os.makedirs(OUT,exist_ok=True)
for f in os.listdir(OUT):
    if f.endswith('.graphql'): os.remove(os.path.join(OUT,f))
rows=[]
for i,rel in enumerate(ORDER,1):
    p=os.path.join(ROOT,rel); body=open(p,encoding='utf-8').read()
    if '"""' in body: raise SystemExit(f'{rel}: contains \"\"\" — cannot be sent as a block string')
    if rel.endswith('.json'):
        json.loads(re.sub(r'^\s*/\*.*?\*/','',body,flags=re.S))  # must parse after the header
    q=('mutation { themeFilesUpsert(themeId: "%s", files: [{filename: "%s", body: {type: TEXT, value: """\n%s\n"""}}]) '
       '{ upsertedThemeFiles { filename size checksumMd5 } userErrors { filename code message } } }')%(THEME,rel,body)
    name='%02d-%s.graphql'%(i,rel.replace('/','__'))
    open(os.path.join(OUT,name),'w',encoding='utf-8').write(q)
    rows.append((i,rel,len(body.encode('utf-8')),hashlib.md5(body.encode('utf-8')).hexdigest()))
print(f"{'#':>2}  {'file':44} {'bytes':>7}  md5")
for i,rel,n,h in rows: print(f"{i:>2}  {rel:44} {n:>7}  {h}")
print(f"\n{len(rows)} mutation files written to {OUT}")
