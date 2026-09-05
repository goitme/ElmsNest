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
import time
# 2026-09-05: Shopify's bot shield answers a burst of ~250 asset fetches with HTTP 429 "Verifying your connection..."
# for every request that follows, page or asset, for some minutes. So: a short pause between fetches, and on a 429
# (or a 9 KB "Verifying your connection" body) wait and retry instead of writing the challenge page as the mirror.
PAUSE=float(os.environ.get("ENV2_MIRROR_PAUSE","0.15"))
def fetch(args,text=True):
    for attempt in range(6):
        r=subprocess.run(["curl","-sSL","--max-time","60","-w","\n__HTTP__%{http_code}"]+args,capture_output=True,text=text)
        body,_,code=r.stdout.rpartition("\n__HTTP__") if text else (r.stdout,None,"")
        if text and (code.strip()=="429" or "Verifying your connection" in body[:4000]):
            wait=20*(attempt+1); print(f"mirror: 429 from the store, waiting {wait}s (attempt {attempt+1}/6)",file=sys.stderr); time.sleep(wait); continue
        time.sleep(PAUSE); return body if text else r
    raise SystemExit("mirror: still 429 after six attempts — the store is throttling this box; try later")
html=fetch(["-c",out+"/cj.txt","-b",out+"/cj.txt",url])
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
    # shared asset cache across mirrors: the same Kalles CSS/JS/fonts are fetched by every page, and the store's bot
    # shield counts requests, not pages. Cache hits cost the store nothing. ENV2_MIRROR_CACHE=0 disables it.
    CACHE=os.environ.get("ENV2_MIRROR_CACHE","/home/user/ElmsNest/brief/.mirror-cache")
    cp=os.path.join(CACHE,os.path.basename(name)) if CACHE!="0" else None
    if cp and os.path.exists(cp) and os.path.getsize(cp)>0 and not os.path.exists(p):
        import shutil; shutil.copyfile(cp,p)
    if not os.path.exists(p):
        r=subprocess.run(["curl","-sSL","--max-time","40","-o",p,"-w","%{http_code}",full],capture_output=True,text=True)
        if r.stdout.strip()=="429":
            print("mirror: 429 on an asset, waiting 20s",file=sys.stderr); time.sleep(20)
            r=subprocess.run(["curl","-sSL","--max-time","40","-o",p,"-w","%{http_code}",full],capture_output=True,text=True)
        time.sleep(PAUSE)
        if r.returncode!=0 or not os.path.exists(p) or os.path.getsize(p)==0: continue
        if cp and r.stdout.strip()=="200":
            os.makedirs(CACHE,exist_ok=True); import shutil; shutil.copyfile(p,cp)
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
# Kalles importmap: its entries are JSON, not src/href — fetch them too or the module graph dies offline
import json as _json
_im=re.search(r'(<script type="importmap">)(.*?)(</script>)',html,re.S)
if _im:
    try:
        _m=_json.loads(_im.group(2)); _n=0
        for _k,_u in list(_m.get('imports',{}).items()):
            _full='https:'+_u if _u.startswith('//') else _u
            if not _full.startswith('http'): continue
            _name="a/"+hashlib.md5(_full.encode()).hexdigest()+".js"; _p=out+"/"+_name
            if not os.path.exists(_p):
                _r=subprocess.run(["curl","-sSL","--max-time","40","-o",_p,_full],capture_output=True)
                if _r.returncode!=0 or not os.path.exists(_p) or os.path.getsize(_p)==0: continue
            _m['imports'][_k]=_name; _n+=1
        html=html[:_im.start(2)]+'\n'+_json.dumps(_m,indent=2)+'\n'+html[_im.end(2):]
    except Exception as _e: print('importmap:',_e)
for u,name in sorted(mapping.items(),key=lambda kv:-len(kv[0])):
    html=html.replace('"'+u+'"','"'+name+'"').replace('('+u+')','('+name+')').replace("('"+u+"')","('"+name+"')").replace(u+' ',name+' ')
open(out+"/index.html","w",encoding="utf-8").write(html)
print(f"mirrored {len(mapping)}/{len(sel)} assets → {out}/index.html ({len(html)//1024} KB)")
