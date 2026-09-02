# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-pdp-ledger.liquid (§4.4, the variant / price ledger) with the REAL
Liquid (python-liquid), the REAL product descriptions pulled from the storefront (_desc-<handle>.json),
the REAL elmsnest-v2-pdp-variants snippet, the real core CSS and the real PDP ground, into
build-preview/ledger.html (JS on) and ledger-nojs.html (JS off). Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-ledger.py
    node brief/shot.js brief/side-pages/pdp/build-preview/ledger.html brief/side-pages/pdp/build-preview/ledger
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-pdp-ledger.liquid')
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
    dpath = os.path.join(HERE, '_desc-' + handle + '.json')
    desc = json.load(open(dpath, encoding='utf-8'))['description'] if os.path.exists(dpath) else ''
    variants = [{'id': v['id'], 'title': v['title'], 'options': v['options'],
                 'price': int(round(v['price'] * 100)), 'available': v['available'], 'image': None}
                for v in p['variants']]
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    first_avail = next((v for v in variants if v['available']), variants[0])
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'description': desc, 'price_min': int(round(p['price_min'] * 100)),
            'price_max': int(round(p['price_max'] * 100)), 'price_varies': p['price_min'] != p['price_max'],
            'available': True, 'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0] if imgs else None,
            'selected_or_first_available_variant': first_avail, 'metafields': {'custom': {}}}

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}
tpl = env.from_string(markup)

def blk(label, handle, use):
    return {'type': 'row', 'shopify_attributes': 'data-shopify-editor-block="x"',
            'settings': {'label': label, 'handle': handle, 'use_caption': use,
                         'unit_label': '', 'bulbs_label': ''}}

HA = 'solar-crystal-ball-string-lights'
HB = 'stainless-steel-solar-path-light-ip65'
HC = 'waterproof-led-wall-light-ip65-6w-12w'
# graft A / graft C captions — every phrase quoted from the product's own description (§4.4).
BLOCKS = [
    blk('5 מ׳ / 20 נורות',   HA, 'לפינת ישיבה קטנה או לשולחן אחד'),
    blk('6.5 מ׳ / 30 נורות', HA, 'אותו מחיר, מטר וחצי יותר'),
    blk('9.5 מ׳ / 50 נורות', HA, 'לאורך גדר או מעקה'),
    blk('11 מ׳ / 60 נורות',  HA, 'מסגרת לפרגולה'),
    blk('13 מ׳ / 100 נורות', HA, 'כמעט פי שניים נורות לאותו מרחק'),
    blk('22 מ׳ / 200 נורות', HA, 'קישוט של חלל שלם'),
    blk('1', HB, 'יחידה אחת מאירה נקודה'),
    blk('2', HB, 'משני צידי כניסה'),
    blk('3', HB, 'שורה קצרה'),
    blk('4', HB, 'לאורך שביל'),
    blk('6', HB, 'מהשער אל הדלת'),
    blk('8', HB, 'מסביב למדשאה'),
    blk('6W / אור חם 3000K',  HC, 'אפקט עדין וממוקד'),
    blk('6W / אור קר 6000K',  HC, 'עדין, בגוון לבן וחד'),
    blk('12W / אור חם 3000K', HC, 'נוכחות חזקה יותר על שטח גדול'),
    blk('12W / אור קר 6000K', HC, 'חזק, בגוון לבן וחד'),
]

def render(product, sid='ledger', over=None, blocks=None):
    st = dict(defaults); st.update(over or {})
    return tpl.render(product=product, section={'id': sid, 'settings': st, 'blocks': blocks if blocks is not None else BLOCKS}, **GLOBALS)

A = build(HA); B = build(HB); C = build(HC)
NET  = build('decorative-led-net-lights')
EDIS = build('solar-edison-string-lights')

# the stage's JSON tag, rendered ONCE per page exactly as the stage does it (CONTRACT-PDP §3.5) —
# the ledger only READS it, so the preview must provide it for product A.
jtpl = env.from_string("{% render 'elmsnest-v2-pdp-variants', product: product, emit: 'json' %}")
jsontag = jtpl.render(product=A, **GLOBALS)

parts = []
def add(label, note, out):
    parts.append('<p class="np-label"><b>%s</b> %s</p>\n%s' % (html.escape(label), html.escape(note), out))

add('A · solar-crystal-ball-string-lights — 24 variants, the section as it ships',
    'Six rows on hairlines, one per length. Every price visible before choosing; per-metre to the agora (17.98 / 13.83 / 10.52 / 9.99 / 9.99 / 8.18); the __use caption from a "row" block, quoted from the description; the string is drawn to scale in CSS so it survives with JS off. Headline and lead derived, not typed.',
    render(A, 'ledger-a'))
add('B · stainless-steel-solar-path-light-ip65 — 1 variant, so a QUANTITY ledger (graft C)',
    'The model says mode=single: no picker anywhere, the rows are 1 / 2 / 3 / 4 / 6 / 8 with running totals from Liquid and quoted meanings. The single option (צבע אור: צהוב חם) has ONE value, so nothing about it is rendered as a control (BRIEF §11).',
    render(B, 'ledger-b'))
add('C · waterproof-led-wall-light-ip65-6w-12w — two price-bearing axes, MAINS',
    'עוצמה x גוון אור -> four rows at 219.90 / 222.90 / 249.90 / 252.90. No per-unit column: a price per watt is meaningless. The quiet axis is צבע גוף (2 values) and is a control only inside the row forms. Nothing about power (§3.7).',
    render(C, 'ledger-c'))
add('EDGE · A with NO caption blocks — the honest degradation',
    'templates/product.elmsnest.json carries no matching block: the __use column is simply empty. §4.4 is "quoted, never invented", so absence is the correct state, not a placeholder.',
    render(A, 'ledger-a0', blocks=[]))
add('EDGE · decorative-led-net-lights — a §3.6 never-use handle',
    'A different option shape and no matching blocks. Headline, lead, quiet-axis line and per-unit all degrade on their own.',
    render(NET, 'ledger-net'))
add('EDGE · solar-edison-string-lights',
    'A second string product: a different value vocabulary, the same ledger.',
    render(EDIS, 'ledger-edis'))

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)

SHELL = """<!doctype html><html lang="he" dir="rtl"%(jsclass)s><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — elmsnest-v2-pdp-ledger%(t)s</title>
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
%(tag)s
%(parts)s
%(script)s
</body></html>"""

doc = SHELL % {'jsclass': ' class="env2-js"', 't': '', 'core': core_css, 'ground': ground, 'css': css,
               'tag': jsontag, 'parts': '\n'.join(parts), 'script': '<script>%s</script>' % js}
open(os.path.join(HERE, 'ledger.html'), 'w', encoding='utf-8').write(doc)

nojs = SHELL % {'jsclass': '', 't': ' (no JS)', 'core': core_css, 'ground': ground, 'css': css,
                'tag': '', 'parts': '\n'.join(parts), 'script': ''}
open(os.path.join(HERE, 'ledger-nojs.html'), 'w', encoding='utf-8').write(nojs)
print('wrote ledger.html', len(doc), '/ ledger-nojs.html', len(nojs))

for name, p in (('A', A), ('B', B), ('C', C)):
    h = render(p, 'x')
    print('---', name)
    print(' h2   :', [re.sub(r'\s+', ' ', x) for x in re.findall(r'id="env2-pdp-ledger-h2">(.*?)</h2>', h, re.S)])
    print(' lead :', re.findall(r'env2-pdp-ledger__lead">(.*?)</p>', h, re.S))
    print(' n    :', [re.sub(r'<[^>]+>', '', x).strip() for x in re.findall(r'ledger__n">(.*?)</span>', h, re.S)])
    print(' b    :', re.findall(r'ledger__b">(.*?)</span>', h, re.S))
    print(' use  :', re.findall(r'ledger__use">(.*?)</span>', h, re.S))
    print(' price:', re.findall(r'ledger__price"><bdi>(.*?)</bdi>', h, re.S))
    print(' pm   :', [re.sub(r'<[^>]+>', '', x).strip() for x in re.findall(r'ledger__pm">(.*?)</span>', h, re.S)])
    print(' forms:', len(re.findall(r'class="env2-pdp-ledger__form"', h)), 'selects:', len(re.findall(r'ledger__sel', h)))
    print(' quiet:', re.findall(r'ledger__qvals">(.*?)</p>', h, re.S), re.findall(r'ledger__qdesc">(.*?)</p>', h, re.S))
    print(' qty  :', re.findall(r'name="quantity" value="(\d+)"', h))
