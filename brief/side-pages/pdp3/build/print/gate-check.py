#!/usr/bin/env python3
# The closed gate must print NOTHING: no root, no <style>, no whitespace-only wrapper.
import re, json, importlib.util, sys
spec = importlib.util.spec_from_file_location('r', '/home/user/ElmsNest/brief/side-pages/pdp3/build/print/render.py')
# render.py writes files on import; run its pieces instead
from liquid import Environment, FileSystemLoader
THEME='/home/user/ElmsNest/theme'
env=Environment(loader=FileSystemLoader(THEME+'/snippets/', ext='.liquid'))
env.filters['asset_img_url']=lambda n,s=None,*a,**k:'x'
env.filters['image_url']=lambda i,width=None,*a,**k:'x'
src=open(THEME+'/sections/elmsnest-s-pdp-print.liquid',encoding='utf-8').read()
tpl=env.from_string(re.sub(r'\{%\s*schema\s*%\}.*?\{%\s*endschema\s*%\}','',src,flags=re.S))
sch=json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}',src,re.S).group(1))
st={s['id']: (s.get('default') or '') for s in sch['settings'] if s.get('id')}
def P(h,c): return {'handle':h,'title':h,'description':'','collections':([{'handle':c}] if c else []),
                    'metafields':{'custom':{'power_source':''}}}
cases=[('sale-only product (no place collection)',P('some-product','sale')),
       ('lighted-birch-branches-20-led (decor collection)',P('lighted-birch-branches-20-led','גרילנדות-ותאורה-דקורטיבית')),
       ('rechargeable-telescopic-camping-lantern (spot collection)',P('rechargeable-telescopic-camping-lantern','ספוטים-ופרוז-קטורים-סולאריים')),
       ('no product at all',None)]
bad=0
for name,p in cases:
    out=tpl.render(product=p, section={'id':'gate','settings':st})
    ok = out.strip()==''
    print(('PASS' if ok else 'FAIL'), name, '->', repr(out[:80]))
    if not ok: bad=1
sys.exit(bad)
