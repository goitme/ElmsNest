#!/usr/bin/env python3
# Renders sections/elmsnest-s-pdp-print.liquid for the three archetypes with python-liquid and the REAL
# snippets (elmsnest-s-place, elmsnest-v2-bdi-range), then wraps each render in a harness page that carries
# the env2 tokens, the real fonts (file://) and the night ground. Assets resolve to file:// paths in theme/assets.
import os, re, json, html
from liquid import Environment, FileSystemLoader

ROOT = '/home/user/ElmsNest'
THEME = ROOT + '/theme'
OUT = ROOT + '/brief/side-pages/pdp3/build/print'
FONTS = ROOT + '/brief/assets/fonts'

env = Environment(loader=FileSystemLoader(THEME + '/snippets/', ext='.liquid'))

def asset_img_url(name, size=None, *a, **k):
    return 'file://' + THEME + '/assets/' + str(name)  # the local file is the real asset; the requested width is dropped so file:// resolves
def image_url(img, width=None, *a, **k):
    return 'file://' + THEME + '/assets/' + str(img)
def asset_url(name, *a, **k):
    return 'file://' + THEME + '/assets/' + str(name)
env.filters['asset_img_url'] = asset_img_url
env.filters['image_url'] = image_url
env.filters['asset_url'] = asset_url

src = open(THEME + '/sections/elmsnest-s-pdp-print.liquid', encoding='utf-8').read()
body = re.sub(r'\{%\s*schema\s*%\}.*?\{%\s*endschema\s*%\}', '', src, flags=re.S)
tpl = env.from_string(body)

# schema defaults -> section.settings (every string is a setting with the spec's default)
schema = json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}', src, re.S).group(1))
settings = {s['id']: s.get('default', '') if s.get('default') is not None else '' for s in schema['settings'] if s.get('id')}

ARCH = {
 'A': dict(handle='stainless-steel-solar-path-light-ip65', title='פנס שביל סולארי מנירוסטה IP65',
           coll='תאורת-שביל-סולארית', desc='<ul><li>עמידות IP65</li><li>תאורה סולארית</li></ul>',
           note='solar path light, IP65, solar pair, place word שביל'),
 'B': dict(handle='waterproof-led-wall-light-ip65-6w-12w', title='מנורת קיר LED אטומה IP65',
           coll='solar-wall-lights', desc='<ul><li>עמידות IP65</li><li>חיבור לחשמל 220V</li></ul>',
           note='mains wall light, IP65, plain pair, place word קיר'),
 'C': dict(handle='dual-head-garden-light-10w-ip65', title='פרוז׳קטור סולארי לגינה IP67',
           coll='ספוטים-ופרוז-קטורים-סולאריים', desc='<ul><li>עמידות IP67</li><li>תאורה סולארית</li></ul>',
           note='solar floodlight, IP67, place word גינה'),
}

def product(a):
    return {'handle': a['handle'], 'title': a['title'], 'description': a['desc'],
            'collections': [{'handle': a['coll']}],
            'metafields': {'custom': {'power_source': ''}}}

def face(fam, path, weight):
    return ("@font-face{font-family:'%s';src:url('file://%s/%s') format('woff2');"
            "font-weight:%s;font-style:normal;font-display:block}" % (fam, FONTS, path, weight))

FONTCSS = "".join([
  face('Frank Ruhl Libre','FrankRuhlLibre-hebrew-400.woff2',400),
  face('Frank Ruhl Libre','FrankRuhlLibre-latin-400.woff2',400),
  face('Frank Ruhl Libre','FrankRuhlLibre-hebrew-700.woff2',700),
  face('Frank Ruhl Libre','FrankRuhlLibre-latin-700.woff2',700),
  face('Heebo','Heebo-hebrew-400.woff2',400),
  face('Heebo','Heebo-latin-400.woff2',400),
  face('Heebo','Heebo-hebrew-300.woff2',300),
  face('Heebo','Heebo-latin-300.woff2',300),
])

# the env2 tokens + section helpers, copied from snippets/elmsnest-v2-core.liquid
CORE = """
:root{--env2-sky-2:#0f1a2f;--env2-sky-3:#070b15;--env2-sky-4:#020306;
 --env2-ink:#f4eee3;--env2-ink-2:#c9c4b8;--env2-mute:#8f95a3;--env2-gold:#e9b96e;--env2-glow:#ffd394;
 --env2-hair:rgba(244,238,227,.12);--env2-gut:clamp(20px,4vw,64px);--env2-w:1240px;
 --env2-serif:"Frank Ruhl Libre","Noto Serif Hebrew",serif;--env2-sans:"Heebo","Assistant",system-ui,sans-serif}
html{background:#020306}
body{margin:0;background-color:#020306;color:#f4eee3;
 background-image:linear-gradient(180deg,#0f1a2f 0%,#070b15 45%,#020306 100%);
 background-repeat:no-repeat;background-size:100% 100%;min-height:100vh}
.env2-section{position:relative;background:transparent;color:var(--env2-ink);font-family:var(--env2-sans);font-weight:300;font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:clip;direction:rtl;text-align:start}
.env2-section img{display:block;max-width:100%}
.env2-section bdi{unicode-bidi:isolate}
.env2-wrap{width:min(var(--env2-w),100% - 2*var(--env2-gut));margin-inline:auto}
"""

for k, a in ARCH.items():
    ctx = {'product': product(a), 'section': {'id': 'harness-' + k, 'settings': settings}}
    out = tpl.render(**ctx)
    page = ("<!doctype html><html lang=\"he\" dir=\"rtl\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>ens_pdp_print — %s</title><style>%s%s</style></head><body>"
            "<div id=\"ens-harness\">%s</div></body></html>" % (k, FONTCSS, CORE, out))
    open(os.path.join(OUT, 'archetype-%s.html' % k), 'w', encoding='utf-8').write(page)
    print(k, a['note'], '->', 'archetype-%s.html' % k, len(out), 'bytes of section html')
