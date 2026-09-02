#!/usr/bin/env python3
"""Extract per-template facts from the mirrored inventory pages → brief/inventory/INVENTORY-FACTS.md"""
import re,glob,os,html
rows=[]
for d in sorted(glob.glob('/home/user/ElmsNest/brief/inventory/*/')):
    f=d+'index.html'
    if not os.path.exists(f): continue
    k=os.path.basename(d.rstrip('/'))
    s=open(f,encoding='utf-8',errors='ignore').read()
    body=re.search(r'<body[^>]*class="([^"]*)"',s); body=body.group(1) if body else '?'
    title=re.search(r'<title>(.*?)</title>',s,re.S); title=re.sub(r'\s+',' ',html.unescape(title.group(1))).strip() if title else '?'
    secs=re.findall(r'<(?:div|section|header|footer)[^>]*id="(shopify-section-[^"]+)"[^>]*class="([^"]*)"',s)
    secs2=[(i.replace('shopify-section-',''),' '.join(x for x in c.split() if x not in('shopify-section',))) for i,c in secs]
    h1=re.findall(r'<h1[^>]*>(.*?)</h1>',s,re.S); h1=[re.sub(r'<[^>]+>','',x).strip()[:80] for x in h1]
    liquid_err=s.count('Liquid error')
    env2=('env2-base' in s, 'fonts.googleapis.com/css2?family=Frank' in s or 'Frank+Ruhl' in s)
    wa='elmsnest-whatsapp' in s or 'wa.me' in s
    cards=len(re.findall(r'hdt-card-product(?:\s|")',s))
    forms=len(re.findall(r'<form[^>]*action="/cart/add"',s))
    rows.append((k,title,body,liquid_err,env2,wa,cards,forms,h1,secs2))
out=['# Inventory facts — dev theme 154726400174, mirrored '+__import__('datetime').date.today().isoformat(),'']
for k,title,body,le,env2,wa,cards,forms,h1,secs in rows:
    out.append(f'## {k}')
    out.append(f'- title: {title}')
    out.append(f'- body class: `{body}` · Liquid errors: {le} · env2 base loaded: {env2[0]} · FRL font loaded: {env2[1]} · whatsapp float: {wa} · product cards: {cards} · add-to-cart forms: {forms}')
    out.append(f'- h1: {h1}')
    out.append('- sections (id · classes):')
    for i,c in secs: out.append(f'  - `{i}` · {c}')
    out.append('')
open('/home/user/ElmsNest/brief/inventory/INVENTORY-FACTS.md','w',encoding='utf-8').write('\n'.join(out))
print('\n'.join(out))
