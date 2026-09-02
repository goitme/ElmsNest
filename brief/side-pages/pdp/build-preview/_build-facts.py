# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-pdp-facts.liquid (§4.5, "what could go wrong") with the REAL Liquid
(python-liquid) and the REAL product descriptions pulled from the storefront (_desc-<handle>.json),
on the real core CSS + the real PDP ground, into build-preview/facts.html. Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-facts.py
    node brief/shot.js brief/side-pages/pdp/build-preview/facts.html brief/side-pages/pdp/build-preview/facts
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-pdp-facts.liquid')
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
        defaults[s['id']] = s.get('default', False if s['type'] == 'checkbox' else '')
print('settings:', ', '.join(sorted(defaults)))

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
            'description': desc, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0] if imgs else None,
            'metafields': {'custom': metafields or {}}}

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}
tpl = env.from_string(markup)

def render(product, sid='facts', over=None, blocks=None):
    st = dict(defaults); st.update(over or {})
    return tpl.render(product=product, section={'id': sid, 'settings': st, 'blocks': blocks or []}, **GLOBALS)

A = build('solar-crystal-ball-string-lights')
B = build('stainless-steel-solar-path-light-ip65')
C = build('waterproof-led-wall-light-ip65-6w-12w')
A_meta = build('solar-crystal-ball-string-lights', {'power_source': 'סולארי'})
D = build('dual-head-garden-light-10w-ip65')          # no <ul> at all — the " · " spec-run fallback
E = build('led-globe-string-lights')                  # never-use handle, USB/battery bullets gated

parts = []
def add(label, note, out):
    parts.append('<p class="fp-label"><b>%s</b> %s</p>\n%s' % (html.escape(label), html.escape(note), out))

add('A · solar-crystal-ball-string-lights — HOW IT RENDERS TODAY',
    'custom.* is empty on all 27 products, so power_source is unstated: the "טעינה סולארית" bullet is dropped and "מקור החשמל" is not claimed either way. Every other row is a description bullet, verbatim.',
    render(A, 'facts-a'))
add('A · the same section once custom.power_source is approved and written as "סולארי"',
    'Nothing in the file changed. One metafield value did, and the product may now name its own power source.',
    render(A_meta, 'facts-a2'))
add('B · stainless-steel-solar-path-light-ip65 — 1 variant',
    'Seven bullets, seven rows; the giant is IP65 by the auto rule (giant_source: "hours" would print 8–10 instead). "לפני שימוש ראשון: …" labels itself on its own colon.',
    render(B, 'facts-b'))
add('B · the same section with giant_source = hours (the §4.5 B still)',
    'The 8–10 numeral the spec asks for on B, with its sub-line quoted from the bullet it came from.',
    render(B, 'facts-b2', {'giant_source': 'hours'}))
add('C · waterproof-led-wall-light-ip65-6w-12w — MAINS, and unstated',
    'No power row and no power sentence anywhere (§3.7); the unknown row therefore names מקור החשמל first, exactly as §4.5 C asks.',
    render(C, 'facts-c'))
add('D · dual-head-garden-light-10w-ip65 — a product with NO bullet list',
    'Fallback 2: the " · " spec run under "פרטים טכניים" becomes the ledger, each item labelled by its own colon. The two power items (מתח, מקור מתח) are dropped while power_source is empty.',
    render(D, 'facts-d'))
add('E · led-globe-string-lights — the caveat that must survive the power gate',
    '"USB או קופסת סוללות" is a power source and is dropped; "סוללות אינן כלולות" is a disclosure, not a claim, and stays.',
    render(E, 'facts-e'))

add('A · the preserved description, open',
    'The owner\'s .elms-sales copy keeps every word and loses its cream card: no background, no border, no 22px radius, no Rubik — headings in Heebo, bullets on hairlines. This is the same <details> the buyer opens.',
    render(A, 'facts-open').replace('<details class=', '<details open class='))

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl" class="env2-js"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — elmsnest-v2-pdp-facts</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(css)s</style>
<style>
body{margin:0}
.fp-label{width:min(1240px,100%% - 2*var(--env2-gut));margin:0 auto;padding-block:44px 0;font:13px/1.6 var(--env2-sans);color:var(--env2-mute);border-top:1px dashed rgba(244,238,227,.18)}
.fp-label b{display:block;font-weight:500;font-size:13.5px;letter-spacing:.06em;color:var(--env2-gold)}
</style></head>
<body class="hdt-page-type-product template-product">
%(parts)s
<script>%(core_js)s</script>
<script>%(js)s</script>
</body></html>""" % {'core': core_css, 'ground': ground, 'css': css, 'js': js,
                     'parts': '\n'.join(parts), 'core_js': core_js}

out = os.path.join(HERE, 'facts.html')
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc), 'bytes')

# the same page with JavaScript switched off: no html.env2-js, no bundle. Everything must still be
# there and lit — the ledger, the numeral (--lit defaults to 1) and the <details>, which is native.
nojs = doc.replace('<html lang="he" dir="rtl" class="env2-js">', '<html lang="he" dir="rtl">')
nojs = re.sub(r'<script>.*?</script>', '', nojs, flags=re.S)
out2 = os.path.join(HERE, 'facts-nojs.html')
open(out2, 'w', encoding='utf-8').write(nojs)
print('wrote', out2, len(nojs), 'bytes')

# ---- the ledger, as text, for every one of the 27 products ----
def rows_of(h):
    p = render(build(h), 'x')
    out = []
    for m in re.finditer(r'<div class="env2-pdp-facts__row[^"]*"[^>]*>\s*(?:<dt[^>]*>(.*?)</dt>\s*)?<dd[^>]*>(.*?)</dd>', p, re.S):
        out.append(((m.group(1) or '').strip(), re.sub(r'<[^>]+>', '', m.group(2)).strip()))
    g = re.search(r'facts-giant><bdi>(.*?)</bdi>', p)
    s = re.search(r'__giantsub">(.*?)</span>', p, re.S)
    return (g.group(1) if g else ''), (s.group(1).strip() if s else ''), out

if __name__ == '__main__':
    for h in sorted(DATA):
        giant, sub, rr = rows_of(h)
        print('\n### %s   giant=%r' % (h, giant))
        if sub: print('    sub: %s' % sub)
        for lab, val in rr:
            print('    %-16s | %s' % (lab or '—', val))
