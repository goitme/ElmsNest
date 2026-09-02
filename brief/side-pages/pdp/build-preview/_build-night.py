# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-pdp-night.liquid (§4.3, the night gallery) with the REAL Liquid
(python-liquid), the REAL product descriptions pulled from the storefront (_desc-<handle>.json), the
REAL elmsnest-v2-pdp-image + elmsnest-v2-pdp-variants snippets, the real core CSS and the real PDP
ground, into build-preview/night.html. Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-night.py
    node brief/shot.js brief/side-pages/pdp/build-preview/night.html brief/side-pages/pdp/build-preview/night
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-pdp-night.liquid')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/pdp/products.json'), encoding='utf-8'))
IMG  = '../../../assets/img/'

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
        defaults[s['id']] = s.get('default', False if s['type'] == 'checkbox' else '')
print('settings:', ', '.join(sorted(defaults)))

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle, nimg=None):
    p = DATA[handle]
    n = min(4, len(p['images'])) if nimg is None else nimg
    imgs = [Img(IMG + handle + '-' + str(i) + '.jpg', i) for i in range(n)]
    desc = json.load(open(os.path.join(HERE, '_desc-' + handle + '.json'), encoding='utf-8'))['description']
    variants = [{'id': v['id'], 'title': v['title'], 'options': v['options'],
                 'price': int(round(v['price'] * 100)), 'available': v['available'], 'image': None}
                for v in p['variants']]
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'description': desc, 'price_min': int(round(p['price_min'] * 100)),
            'price_max': int(round(p['price_max'] * 100)), 'price_varies': p['price_min'] != p['price_max'],
            'available': True, 'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0] if imgs else None,
            'selected_or_first_available_variant': variants[0], 'metafields': {'custom': {}}}

def image_tag(v, **kw):
    s = str(v)
    a = ['src="%s"' % s]
    if kw.get('widths'):
        a.append('srcset="%s"' % ', '.join('%s %sw' % (s, w.strip()) for w in str(kw['widths']).split(',')))
    for k in ('sizes', 'alt', 'loading'):
        if kw.get(k) is not None:
            a.append('%s="%s"' % (k, html.escape(str(kw[k]), quote=True)))
    if kw.get('class'):
        a.append('class="%s"' % kw['class'])
    a.append('width="1200" height="1200"')
    return '<img ' + ' '.join(a) + '>'

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['image_tag'] = image_tag
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}
tpl = env.from_string(markup)

def render(product, sid='night', over=None, blocks=None):
    st = dict(defaults); st.update(over or {})
    return tpl.render(product=product, section={'id': sid, 'settings': st, 'blocks': blocks or []}, **GLOBALS)

A = build('solar-crystal-ball-string-lights')
B = build('stainless-steel-solar-path-light-ip65')
C = build('waterproof-led-wall-light-ip65-6w-12w')
ONE = build('solar-crystal-ball-string-lights', nimg=1)      # a product with a single usable photograph
NET = build('decorative-led-net-lights')                     # a §3.6 never-use handle (index 0 banned)

parts = []
def add(label, note, out):
    parts.append('<p class="np-label"><b>%s</b> %s</p>\n%s' % (html.escape(label), html.escape(note), out))

add('A · solar-crystal-ball-string-lights — the section as it ships',
    'Wide frame = images[2] (the string on the wooden trellis), close-up = images[0], both through the §3.5 resolver: 1 and 3 are banned on this handle. Headline tail from the product title\'s own noun. Lead parsed verbatim from the description. Scale cue built from the 24-variant ledger model.',
    render(A, 'night-a'))
add('B · stainless-steel-solar-path-light-ip65 — 1 variant',
    'The model says mode=single, so NO number is printed and no scale is claimed. Wide = images[3], close-up = images[1]; index 2 (the dimensions slide) is banned. Nothing about power anywhere.',
    render(B, 'night-b'))
add('C · waterproof-led-wall-light-ip65-6w-12w — MAINS, power_source unstated',
    'Two price-bearing axes; the scale cue becomes the wattage pair. Wide = images[3], close-up = images[2]; index 0 (the slogan slide) is banned. No solar sentence, no mains sentence — §3.7.',
    render(C, 'night-c'))
add('EDGE · the same product with a single usable photograph',
    'Both slots resolve to the same picture, so the section renders ONE figure instead of the same frame twice.',
    render(ONE, 'night-one'))
add('EDGE · decorative-led-net-lights — a §3.6 never-use handle, and no lead in the description',
    'index 0 carries baked-in text and is stepped over by the resolver. Whatever the description does not give, the section does without.',
    render(NET, 'night-net'))

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl" class="env2-js"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — elmsnest-v2-pdp-night</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(css)s</style>
<style>
body{margin:0}
.np-label{width:min(1240px,100%% - 2*var(--env2-gut));margin:0 auto;padding-block:52px 0;font:13px/1.6 var(--env2-sans);color:var(--env2-mute);border-top:1px dashed rgba(244,238,227,.18)}
.np-label b{display:block;font-weight:500;font-size:13.5px;letter-spacing:.06em;color:var(--env2-gold)}
</style></head>
<body class="hdt-page-type-product template-product">
%(parts)s
<script>%(js)s</script>
</body></html>""" % {'core': core_css, 'ground': ground, 'css': css, 'js': js, 'parts': '\n'.join(parts)}

out = os.path.join(HERE, 'night.html')
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc), 'bytes')
for name, p in (('A', A), ('B', B), ('C', C)):
    h = render(p, 'x')
    print(name, 'h2   :', re.findall(r'class="env2-h env2-pdp-night__h2"[^>]*>(.*?)</h2>', h, re.S))
    print(name, 'lead :', re.findall(r'class="env2-lead env2-pdp-night__lead">(.*?)</p>', h, re.S))
    print(name, 'capB :', [re.sub(r'\s+', ' ', x).strip() for x in re.findall(r'cap--big">(.*?)</figcaption>', h, re.S)])
    print(name, 'capS :', re.findall(r'cap--small">(.*?)</figcaption>', h, re.S))
    print(name, 'imgs :', re.findall(r'src="([^"]+)"', h))
