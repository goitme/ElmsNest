# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-pdp-fit.liquid (§4.2, the not-for device) with the REAL Liquid
(python-liquid), the REAL product descriptions pulled from the storefront (_desc-<handle>.json),
the real elmsnest-v2-pdp-photo-cta snippet, the real core CSS and the real PDP ground, into
build-preview/fit.html. Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-fit.py
    node brief/shot.js brief/side-pages/pdp/build-preview/fit.html brief/side-pages/pdp/build-preview/fit
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-pdp-fit.liquid')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/pdp/products.json'), encoding='utf-8'))

src = open(SEC, encoding='utf-8').read()
def block(tag):
    m = re.search(r'\{%-?\s*' + tag + r'\s*-?%\}(.*?)\{%-?\s*end' + tag + r'\s*-?%\}', src, re.S)
    return m.group(1) if m else ''
css, js, schema_txt = block('stylesheet'), block('javascript'), block('schema')
markup = re.sub(r'\{%-?\s*(stylesheet|javascript|schema)\s*-?%\}.*?\{%-?\s*end\1\s*-?%\}', '', src, flags=re.S)
schema = json.loads(schema_txt)

defaults = {}
for s in schema['settings']:
    if s.get('id'):
        defaults[s['id']] = s.get('default', '' if s['type'] != 'checkbox' else False)
print('settings:', ', '.join(sorted(defaults)))

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle, metafields=None):
    p = DATA[handle]
    n = min(4, len(p['images']))
    imgs = [Img('../../../assets/img/' + handle + '-' + str(i) + '.jpg', i) for i in range(n)]
    desc = json.load(open(os.path.join(HERE, '_desc-' + handle + '.json'), encoding='utf-8'))['description']
    variants = [{'id': v['id'], 'title': v['title'], 'options': v['options'],
                 'price': int(round(v['price'] * 100)), 'available': v['available']} for v in p['variants']]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'description': desc, 'variants': variants, 'images': imgs, 'featured_image': imgs[0],
            'metafields': {'custom': metafields or {}}}

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}
tpl = env.from_string(markup)

def render(product, sid='fit', over=None, blocks=None):
    st = dict(defaults); st.update(over or {})
    return tpl.render(product=product, section={'id': sid, 'settings': st, 'blocks': blocks or []}, **GLOBALS)

A = build('solar-crystal-ball-string-lights')
B = build('stainless-steel-solar-path-light-ip65')
C = build('waterproof-led-wall-light-ip65-6w-12w')
# the same product ONCE THE OWNER APPROVES the metafield sheet: the switch mode + graft B
A_meta = build('solar-crystal-ball-string-lights',
               {'not_fit_for': 'צריך אור חזק — זו אינה מטרתה',
                'power_source': 'סולארי'})
REDIRECT = ('<p>לאור חזק על קיר או בכניסה יש אצלנו מקום אחר — '
            '<a href="/collections/wall">תאורת קיר</a>. לאווירה, זו.</p>')

parts = []
def add(label, note, out):
    parts.append('<p class="fitp-label"><b>%s</b> %s</p>\n%s' % (html.escape(label), html.escape(note), out))

add('A · solar-crystal-ball-string-lights — HOW IT RENDERS TODAY',
    'custom.not_fit_for empty on all 27 products, so: no negative, no switch, no solar question. The suits half is printed and the two choosing sentences are parsed verbatim out of the product description.',
    render(A, 'fit-a'))
add('A · the same section once custom.not_fit_for + power_source are approved and written',
    'MODE 1 — the approved pair as a physical switch, plus graft B (the sun question). Nothing in the section changed; two metafield values did.',
    render(A_meta, 'fit-a2', {'redirect_html': REDIRECT}))
add('A · MODE 1 with the switch already thrown (the off radio pre-checked in this static copy)',
    'This is the still the spec asks for: the light is genuinely out, the refusal line has printed, the knob has travelled.',
    render(A_meta, 'fit-a3', {'redirect_html': REDIRECT}).replace('value="off" data-env2-pdp-fit-r="off"', 'value="off" checked data-env2-pdp-fit-r="off"').replace('value="on" checked', 'value="on"'))
add('B · stainless-steel-solar-path-light-ip65 — 1 variant',
    'Place = the path pair. Still no negative (metafield empty), and per the spec B omits the second question by default. No one-value picker anywhere in this section.',
    render(B, 'fit-b'))
add('C · waterproof-led-wall-light-ip65-6w-12w — MAINS',
    'power_source is unstated, so the section says NOTHING about power: no solar sentence, no electrician note, no sun question. The choosing sentences are the two the spec quotes, parsed, not typed.',
    render(C, 'fit-c'))

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl" class="env2-js"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — elmsnest-v2-pdp-fit</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(css)s</style>
<style>
body{margin:0}
.fitp-label{width:min(1240px,100%% - 2*var(--env2-gut));margin:0 auto;padding-block:44px 0;font:13px/1.6 var(--env2-sans);color:var(--env2-mute);border-top:1px dashed rgba(244,238,227,.18)}
.fitp-label b{display:block;font-weight:500;font-size:13.5px;letter-spacing:.06em;color:var(--env2-gold)}
</style></head>
<body class="hdt-page-type-product template-product">
%(parts)s
<script>%(js)s</script>
</body></html>""" % {'core': core_css, 'ground': ground, 'css': css, 'js': js,
                     'parts': '\n'.join(parts)}

out = os.path.join(HERE, 'fit.html')
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc), 'bytes')
for name, h in (('A today', render(A, 'x')), ('C today', render(C, 'x'))):
    for pat in (r'class="env2-pdp-fit__word">([^<]*)<', r'class="env2-pdp-fit__ch">([^<]*)<', r'class="env2-pdp-fit__itext">([^<]*)<'):
        print(name, re.findall(pat, h))
