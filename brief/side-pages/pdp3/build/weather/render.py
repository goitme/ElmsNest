#!/usr/bin/env python3
"""Render sections/elmsnest-s-pdp-weather.liquid for the three archetypes and inline the result
into a local harness (file:// assets, real fonts) so the section height at 390 can be measured."""
import re, os, json
from liquid import Environment, FileSystemLoader

THEME = '/home/user/ElmsNest/theme'
HERE  = os.path.dirname(os.path.abspath(__file__))
SRC   = os.path.join(THEME, 'sections', 'elmsnest-s-pdp-weather.liquid')

src = open(SRC, encoding='utf-8').read()
src = re.sub(r'\{%-?\s*schema\s*-?%\}.*?\{%-?\s*endschema\s*-?%\}', '', src, flags=re.S)

env = Environment(loader=FileSystemLoader(os.path.join(THEME, 'snippets'), ext='.liquid'))
env.filters['asset_img_url'] = lambda name, size='': 'file://' + os.path.join(THEME, 'assets', str(name))
env.filters['asset_url']     = lambda name: 'file://' + os.path.join(THEME, 'assets', str(name))

# the schema defaults (the template passes settings:{}), read straight out of the schema block
schema = json.loads(re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}',
                              open(SRC, encoding='utf-8').read(), re.S).group(1))
SETTINGS = {s['id']: s.get('default', '') for s in schema['settings'] if s.get('id')}

ARCH = {
  'A': dict(title='פנס שביל סולארי מנירוסטה IP65',
            handle='stainless-steel-solar-path-light-ip65',
            description='<p>פנס שביל סולארי לגינה.</p><p>פרטים שכדאי לדעת</p><ul>'
                        '<li>עמידות IP65 לשימוש חיצוני</li><li>נעיצה בקרקע</li></ul>'),
  'B': dict(title='מנורת קיר LED דו-כיוונית לחוץ',
            handle='outdoor-bidirectional-led-wall-light-ip65',
            description='<p>מנורת קיר בחיבור לחשמל.</p><p>פרטים שכדאי לדעת</p><ul>'
                        '<li>עמידות IP65</li><li>חיבור 220V</li></ul>'),
  'C': dict(title='פרוז׳קטור סולארי לגינה',
            handle='powerful-solar-garden-light',
            description='<p>פרוז׳קטור סולארי חזק להארת עץ או ערוגה.</p><p>פרטים שכדאי לדעת</p><ul>'
                        '<li>עמידות IP67</li><li>פאנל סולארי מובנה</li></ul>'),
}

tpl = env.from_string(src)
out = {}
for k, p in ARCH.items():
    product = dict(p, metafields={'custom': {}})
    out[k] = tpl.render(product=product,
                        section={'id': 'ens-weather-' + k, 'settings': SETTINGS, 'blocks': []}).strip()
    open(os.path.join(HERE, f'section-{k}.html'), 'w', encoding='utf-8').write(out[k])
    print(k, len(out[k]), 'bytes')

# ---- the harness: the night ground + the real fonts, the section markup inlined verbatim ----
FONTS = '/home/user/ElmsNest/brief/assets/fonts'
face = lambda fam, file, w: (
    f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;"
    f"src:url('file://{FONTS}/{file}') format('woff2')}}")
faces = '\n'.join([
    face('Heebo', 'Heebo-hebrew-300.woff2', 300), face('Heebo', 'Heebo-latin-300.woff2', 300),
    face('Heebo', 'Heebo-hebrew-400.woff2', 400), face('Heebo', 'Heebo-latin-400.woff2', 400),
    face('Heebo', 'Heebo-hebrew-500.woff2', 500), face('Heebo', 'Heebo-latin-500.woff2', 500),
    face('Frank Ruhl Libre', 'FrankRuhlLibre-hebrew-700.woff2', 700),
    face('Frank Ruhl Libre', 'FrankRuhlLibre-latin-700.woff2', 700),
])
# the tokens the section relies on, copied from snippets/elmsnest-v2-core.liquid (§4)
CORE = """
:root{--env2-sky-2:#0f1a2f;--env2-sky-3:#070b15;--env2-sky-4:#020306;
 --env2-ink:#f4eee3;--env2-ink-2:#c9c4b8;--env2-gold:#e9b96e;--env2-glow:#ffd394;
 --env2-hair:rgba(244,238,227,.12);--env2-gut:clamp(20px,4vw,64px);--env2-w:1240px;
 --env2-serif:"Frank Ruhl Libre","Noto Serif Hebrew",serif;
 --env2-sans:"Heebo","Assistant",system-ui,sans-serif}
html{background:#020306}
body{margin:0;background-color:#020306;color:#f4eee3;
 background-image:linear-gradient(180deg,#0f1a2f 0%,#070b15 45%,#020306 100%);
 background-repeat:no-repeat;background-size:100% 100%;min-height:100vh}
.env2-section{position:relative;background:transparent;color:var(--env2-ink);font-family:var(--env2-sans);
 font-weight:300;font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:clip;
 direction:rtl;text-align:start}
.env2-section img{display:block;max-width:100%}
.env2-section bdi{unicode-bidi:isolate}
.env2-wrap{width:min(var(--env2-w),100% - 2*var(--env2-gut));margin-inline:auto}
.env2-h{font-family:var(--env2-serif);font-weight:700;line-height:.98;letter-spacing:-.01em;
 text-wrap:balance;margin:0;color:var(--env2-ink)}
"""
for k in ARCH:
    html = ('<meta charset="utf-8"><title>weather ' + k + '</title><style>' + faces + CORE +
            '</style>\n<div id="probe">' + out[k] + '</div>\n')
    open(os.path.join(HERE, f'harness-{k}.html'), 'w', encoding='utf-8').write(html)
print('harnesses written')
