# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-pdp-related.liquid (WINNING-SPEC §4.8 — the related module and THE
product card) with the REAL Liquid (python-liquid), the REAL preset blocks out of its own
{% schema %}, and the REAL snippets (elmsnest-v2-pdp-card -> -pdp-image / -price / -buy), on the real
core CSS + the real PDP ground, into build-preview/related.html. Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-related.py
    node brief/shot.js brief/side-pages/pdp/build-preview/related.html brief/side-pages/pdp/build-preview/related
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-pdp-related.liquid')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/pdp/products.json'), encoding='utf-8'))
IMG  = '../../../assets/img/'

src = open(SEC, encoding='utf-8').read()
def block(tag):
    m = re.search(r'\{%-?\s*' + tag + r'\s*-?%\}(.*?)\{%-?\s*end' + tag + r'\s*-?%\}', src, re.S)
    return m.group(1) if m else ''
css, js, schema_txt = block('stylesheet'), block('javascript'), block('schema')
markup = re.sub(r'\{%-?\s*(stylesheet|javascript|schema)\s*-?%\}.*?\{%-?\s*end\1\s*-?%\}', '', src, flags=re.S)
schema = json.loads(schema_txt)

defaults = {s['id']: s.get('default', False if s['type'] == 'checkbox' else '')
            for s in schema['settings'] if s.get('id')}
bdefaults = {b['type']: {s['id']: s.get('default', '') for s in b['settings'] if s.get('id')}
             for b in schema['blocks']}
print('settings:', ', '.join(sorted(defaults)))
print('block settings:', {k: sorted(v) for k, v in bdefaults.items()})

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle):
    p = DATA[handle]
    # the local pack carries 0..3 for every product (plus any extra frame pulled in for a ledger row)
    imgs = []
    for i in range(len(p['images'])):
        f = os.path.join(REPO, 'brief/assets/img', '%s-%d.jpg' % (handle, i))
        if not os.path.exists(f):
            break
        imgs.append(Img(IMG + handle + '-' + str(i) + '.jpg', i))
    variants = [{'id': v['id'], 'title': v['title'], 'options': v['options'],
                 'price': int(round(v['price'] * 100)), 'available': v['available'], 'image': None}
                for v in p['variants']]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'price_min': int(round(p['price_min'] * 100)), 'price_max': int(round(p['price_max'] * 100)),
            'price_varies': p['price_min'] != p['price_max'], 'available': True,
            'variants': variants, 'images': imgs, 'featured_image': imgs[0],
            'selected_or_first_available_variant': variants[0], 'metafields': {'custom': {}},
            'collections': []}

# ---- the four real place collections (titles + handles read from the Admin API on 2026-09-02),
#      plus "מבצעים", which the section must never draw from ----------------------------------
COLS = {'תאורת שביל, עמוד וגינה': 'תאורת-שביל-סולארית',
        'תאורת קיר': 'solar-wall-lights',
        'גרילנדות ותאורה דקורטיבית': 'גרילנדות-ותאורה-דקורטיבית',
        'ספוטים, פרוז׳קטורים ותאורה ניידת': 'ספוטים-ופרוז-קטורים-סולאריים'}
PRODUCTS = {h: build(h) for h in DATA}
COLLECTIONS = {}
for title, handle in COLS.items():
    COLLECTIONS[title] = {'title': title, 'handle': handle, 'url': '/collections/' + handle,
                          'products': [p for p in PRODUCTS.values() if p['type'] == title]}
SALE = {'title': 'מבצעים', 'handle': 'sale', 'url': '/collections/sale',
        'products': [PRODUCTS['warm-solar-step-deck-lights']]}
for p in PRODUCTS.values():
    # every product sits in its place collection; one of them also sits in "מבצעים" (as in the shop)
    p['collections'] = ([SALE] if p is SALE['products'][0] else []) + [COLLECTIONS[p['type']]]

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'},
           'settings': {'whatsapp_number': ''}}
tpl = env.from_string(markup)

def preset_blocks(over=None):
    out = []
    for n, b in enumerate(schema['presets'][0].get('blocks', [])):
        st = dict(bdefaults[b['type']]); st.update(b.get('settings', {}))
        if over and n in over: st.update(over[n])
        out.append({'id': 'b%d' % n, 'type': b['type'], 'settings': st,
                    'shopify_attributes': 'data-block-id="b%d"' % n})
    return out

def render(product, sid='related', over=None, blocks=None):
    st = dict(defaults); st.update(over or {})
    return tpl.render(product=product, section={'id': sid, 'settings': st,
                                                'blocks': blocks if blocks is not None else preset_blocks()},
                      **GLOBALS)

A = PRODUCTS['solar-crystal-ball-string-lights']
B = PRODUCTS['stainless-steel-solar-path-light-ip65']
C = PRODUCTS['waterproof-led-wall-light-ip65-6w-12w']

main = render(A, 'related-a')
if '~~' in main or '{%' in main or '{{' in main:
    raise SystemExit('unrendered Liquid left in the output')

parts = [main]
def add(label, note, out):
    parts.append('<p class="fp-label"><b>%s</b> %s</p>\n%s' % (html.escape(label), html.escape(note), out))

add('B · stainless-steel-solar-path-light-ip65 — 1 variant, place = שביל',
    'Eyebrow, heading, deck and the collection link all follow product.type. Six of the eight path '
    'products are never-use handles and B is the seventh, so ONE honest card is left — and the heading '
    'says "עוד אחד", not "עוד שלושה". The rest are reached through the collection link.',
    render(B, 'related-b'))
add('C · waterproof-led-wall-light-ip65-6w-12w — MAINS, power unstated, place = קיר',
    'Nothing about power is said here on any product, so §3.7 cannot be breached by this section.',
    render(C, 'related-c'))
add('The merchant deleted a block (a robustness case)',
    'The heading counts what actually renders: "עוד שניים …", never "עוד שלושה", and the two remaining '
    'cards keep their staggered widths.',
    render(A, 'related-d', blocks=preset_blocks()[:2]))
add('One product, hand-picked: a single-variant product (solar-firefly-garden-lights)',
    'Singular Hebrew ("עוד אחד למרפסת"), a resolved single price and a REAL add-to-cart form — the '
    'card action every no-JS visitor can use.',
    render(A, 'related-e', {'auto_fill': False},
           blocks=preset_blocks({0: {'product': PRODUCTS['solar-firefly-garden-lights'],
                                     'card_width': 300, 'card_aspect': '1/1.05'}})[:1]))
add('Merchant overrides: own heading, own deck, own action labels, explicit image index',
    'Every derived string is a default, never a lock.',
    render(A, 'related-f', {'heading': 'שלושה שאפשר לתלות באותו ערב', 'deck': 'שלושתם מאותה מרפסת.',
                            'link_label': 'לכל הגרילנדות', 'link_url': '/collections/x'},
           blocks=preset_blocks({0: {'card_action_label': 'לבחירת אורך', 'card_image_index': 3},
                                 1: {'card_action_label': 'לבחירת אורך'},
                                 2: {'card_action_label': 'לבחירת גוון'}})))
add('A never-use product hand-picked with no photograph of its own (decorative-led-net-lights)',
    'All six of its images are cream marketing boards, and solar-rope-string-lights (block 3) has no '
    'frame a centre crop can keep either — so both blocks are SKIPPED and the heading counts down to '
    'one. This is the only place a merchant setting is overridden, and §3.6 is why. Giving either '
    'block a card_image of its own brings it straight back.',
    render(A, 'related-noimg', {'auto_fill': False},
           blocks=preset_blocks({0: {'product': PRODUCTS['decorative-led-net-lights']},
                                 1: {'product': PRODUCTS['solar-edison-string-lights']},
                                 2: {'product': PRODUCTS['solar-rope-string-lights']}})))
add('A product that also sits in the "מבצעים" collection (warm-solar-step-deck-lights)',
    'The shelf is drawn from the PLACE collection, matched on product.type — so the sale collection '
    'can never become the source and no sale UI can reach the page.',
    render(PRODUCTS['warm-solar-step-deck-lights'], 'related-sale'))
empty = render(PRODUCTS['solar-firefly-garden-lights'], 'related-g',
               {'auto_fill': False}, blocks=preset_blocks({0: {'product': ''}, 1: {'product': ''},
                                                           2: {'product': ''}}))
add('No product resolves at all (auto-fill off, no pickers)',
    'The section prints NOTHING — %d characters of output — rather than an empty shelf or a heading '
    'that promises three.' % len(empty.strip()),
    '<p class="fp-note">(empty)</p>' + empty)

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl" class="env2-js"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — elmsnest-v2-pdp-related</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(css)s</style>
<style>
/* stands in for Kalles' own global reset (*,:after,:before{box-sizing:border-box;border-width:0}),
   which the core CSS assumes and which the offline harness would otherwise lack — without it an
   <a class="env2-btn"> is content-box and renders 72px tall instead of 45px. */
*,*::before,*::after{box-sizing:border-box}
body{margin:0}
.fp-label{width:min(1240px,100%% - 2*var(--env2-gut));margin:0 auto;padding-block:44px 0;font:13px/1.6 var(--env2-sans);color:var(--env2-mute);border-top:1px dashed rgba(244,238,227,.18)}
.fp-label b{display:block;font-weight:500;font-size:13.5px;letter-spacing:.06em;color:var(--env2-gold)}
.fp-note{width:min(1240px,100%% - 2*var(--env2-gut));margin:6px auto 0;font:13px var(--env2-sans);color:var(--env2-mute)}
</style></head>
<body class="hdt-page-type-product template-product">
%(parts)s
<script>%(core_js)s</script>
<script>%(js)s</script>
</body></html>""" % {'core': core_css, 'ground': ground, 'css': css, 'js': js,
                     'parts': '\n'.join(parts), 'core_js': core_js}

out = os.path.join(HERE, 'related.html')
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc), 'bytes')

# ---- a no-JS twin: same markup, no core JS, no section JS, no html.env2-js -> every lamp lit ----
nojs = doc.replace('<html lang="he" dir="rtl" class="env2-js">', '<html lang="he" dir="rtl">')
nojs = re.sub(r'<script>.*?</script>', '', nojs, flags=re.S)
out2 = os.path.join(HERE, 'related-nojs.html')
open(out2, 'w', encoding='utf-8').write(nojs)
print('wrote', out2, len(nojs), 'bytes')
