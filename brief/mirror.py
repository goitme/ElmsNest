#!/usr/bin/env python3
"""Mirror a Shopify page for offline screenshots.
Usage: python3 brief/mirror.py <url> <out_dir>
Fetches the page with curl (which works through the sandbox proxy; Chromium does not),
downloads every css/js/img/font asset it references, rewrites the HTML to local paths,
and writes <out_dir>/index.html. Then: node brief/shot.js <out_dir>/index.html <prefix>."""
import re,os,subprocess,hashlib,sys
from urllib.parse import urljoin
url,out=sys.argv[1],sys.argv[2]
os.makedirs(out+"/a",exist_ok=True)
html=subprocess.run(["curl","-sSL","--max-time","60","-c",out+"/cj.txt","-b",out+"/cj.txt",url],capture_output=True,text=True).stdout
urls=set()
for m in re.finditer(r'(?:src|href)="([^"]+)"',html): urls.add(m.group(1))
for m in re.finditer(r'srcset="([^"]+)"',html):
    for part in m.group(1).split(','):
        u=part.strip().split(' ')[0]
        if u: urls.add(u)
for m in re.finditer(r'url\((["\']?)([^)"\']+)\1\)',html): urls.add(m.group(2))
def keep(u):
    if u.startswith(('data:','#','mailto:','tel:','javascript:')): return False
    return bool(re.search(r'\.(css|js|png|jpe?g|webp|svg|gif|woff2?|ico)(\?|$)',u))
mapping={}
sel=[u for u in urls if keep(u)]
for u in sel:
    full=u if u.startswith("http") else ("https:"+u if u.startswith("//") else urljoin(url,u))
    ext=re.search(r'\.(css|js|png|jpe?g|webp|svg|gif|woff2?|ico)',full).group(0)
    name="a/"+hashlib.md5(full.encode()).hexdigest()+ext
    p=out+"/"+name
    if not os.path.exists(p):
        r=subprocess.run(["curl","-sSL","--max-time","40","-o",p,full],capture_output=True)
        if r.returncode!=0 or not os.path.exists(p) or os.path.getsize(p)==0: continue
    mapping[u]=name
# google fonts css → also fetch the woff2 it references
for u,name in list(mapping.items()):
    if 'fonts.googleapis.com' in u and name.endswith('.css'):
        css=open(out+"/"+name,encoding='utf-8',errors='ignore').read()
        for fu in set(re.findall(r'url\((https://fonts\.gstatic\.com[^)]+)\)',css)):
            fn="a/"+hashlib.md5(fu.encode()).hexdigest()+".woff2"
            if not os.path.exists(out+"/"+fn): subprocess.run(["curl","-sS","-o",out+"/"+fn,fu])
            css=css.replace(fu,fn)
        open(out+"/"+name,"w",encoding='utf-8').write(css)
for u,name in sorted(mapping.items(),key=lambda kv:-len(kv[0])):
    html=html.replace('"'+u+'"','"'+name+'"').replace('('+u+')','('+name+')').replace("('"+u+"')","('"+name+"')").replace(u+' ',name+' ')
open(out+"/index.html","w",encoding="utf-8").write(html)
print(f"mirrored {len(mapping)}/{len(sel)} assets → {out}/index.html ({len(html)//1024} KB)")
