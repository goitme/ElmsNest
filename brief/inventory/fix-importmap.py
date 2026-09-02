#!/usr/bin/env python3
"""Kalles loads its modules through an <script type="importmap"> whose entries mirror.py's src/href regex never saw,
so every entry still points at elmsnest.com and the module graph dies offline (custom elements never defined,
reveal-on-scroll cards stay at opacity 0). This fetches each remote importmap entry into <dir>/a/ and rewrites the map.
Usage: python3 brief/inventory/fix-importmap.py <mirror_dir> [...]"""
import re,os,sys,json,hashlib,subprocess
for out in sys.argv[1:]:
    f=os.path.join(out,'index.html')
    if not os.path.exists(f): continue
    html=open(f,encoding='utf-8').read()
    m=re.search(r'(<script type="importmap">)(.*?)(</script>)',html,re.S)
    if not m: print(out,'no importmap'); continue
    try: im=json.loads(m.group(2))
    except Exception as e: print(out,'importmap json error',e); continue
    n=0
    for k,u in list(im.get('imports',{}).items()):
        if u.startswith('a/') or u.startswith('/a/'): continue
        full='https:'+u if u.startswith('//') else u
        if not full.startswith('http'): continue
        name='a/'+hashlib.md5(full.encode()).hexdigest()+'.js'; p=os.path.join(out,name)
        if not os.path.exists(p) or os.path.getsize(p)==0:
            r=subprocess.run(['curl','-sSL','--max-time','40','-o',p,full],capture_output=True)
            if r.returncode!=0 or not os.path.exists(p) or os.path.getsize(p)==0: print(out,'FAILED',full); continue
        im['imports'][k]=name; n+=1
    html=html[:m.start(2)]+'\n'+json.dumps(im,indent=2)+'\n'+html[m.end(2):]
    open(f,'w',encoding='utf-8').write(html); print(out,'rewrote',n,'importmap entries')
