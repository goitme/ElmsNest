# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-pdp-ask.liquid (WINNING-SPEC §4.7 — the specialist line + the small
step) with the REAL Liquid (python-liquid), the REAL preset block out of its own {% schema %}, the
REAL elmsnest-v2-pdp-variants + elmsnest-v2-pdp-photo-cta snippets, on the real core CSS and the real
PDP ground, into build-preview/ask.html (JS on) and ask-nojs.html (JS off). Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-ask.py
    node brief/shot.js brief/side-pages/pdp/build-preview/ask.html brief/side-pages/pdp/build-preview/ask
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-pdp-ask.liquid')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/pdp/products.json'), encoding='utf-8'))

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

def preset_blocks(i=0):
    out = []
    for n, b in enumerate(schema['presets'][i].get('blocks', [])):
        st = dict(bdefaults[b['type']]); st.update(b.get('settings', {}))
        out.append({'id': 'b%d' % n, 'type': b['type'], 'settings': st,
                    'shopify_attributes': 'data-block-id="b%d"' % n})
    return out

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle, meta=None):
    p = DATA[handle]
    imgs = [Img('../../../assets/img/' + handle + '-' + str(i) + '.jpg', i)
            for i in range(min(4, len(p['images'])))]
    variants = [{'id': v['id'], 'title': v['title'], 'options': v['options'],
                 'price': int(round(v['price'] * 100)), 'available': v['available'], 'image': None}
                for v in p['variants']]
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    first_avail = next((v for v in variants if v['available']), variants[0])
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'price_min': int(round(p['price_min'] * 100)), 'price_max': int(round(p['price_max'] * 100)),
            'price_varies': p['price_min'] != p['price_max'], 'available': True,
            'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0] if imgs else None,
            'selected_or_first_available_variant': first_avail,
            'metafields': {'custom': meta or {}}}

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}
tpl = env.from_string(markup)

def render(product, sid='ask', over=None, blocks=None):
    st = dict(defaults); st.update(over or {})
    return tpl.render(product=product, section={'id': sid, 'settings': st,
                                                'blocks': preset_blocks() if blocks is None else blocks},
                      **GLOBALS)

A = build('solar-crystal-ball-string-lights')
B = build('stainless-steel-solar-path-light-ip65')
C = build('waterproof-led-wall-light-ip65-6w-12w')
# the same product on the day the owner approves its metafield sheet: §4.2 prints a negative, so the
# lead's first sentence becomes the §4.7 wording verbatim.
A_neg = build('solar-crystal-ball-string-lights',
              {'not_fit_for': 'צריך אור חזק — זו אינה מטרתה', 'power_source': 'סולארי'})
# a fourth shape nobody designed for: a price axis whose values carry no number at all
D = build('solar-firefly-garden-lights')
E = build('modern-led-wall-light-6w-up-down')

main = render(A, 'ask-a')

parts = [main]
def add(label, note, out):
    parts.append('<p class="fp-label"><b>%s</b> %s</p>\n%s' % (html.escape(label), html.escape(note), out))

add('B · stainless-steel-solar-path-light-ip65 — 1 variant (mode single)',
    'No picker anywhere: the small step is the quantity phrase, and the lead ends "או להתחיל מיחידה אחת".',
    render(B, 'ask-b'))
add('C · waterproof-led-wall-light-ip65-6w-12w — 8 variants, MAINS, power unstated',
    'The step is the low wattage, in one <bdi>. This section says nothing about power on any product, so §3.7 cannot be breached here.',
    render(C, 'ask-c'))
add('A on the day custom.not_fit_for is approved',
    'The only difference: the first sentence becomes §4.7 verbatim — "אמרנו למעלה מתי היא לא מתאימה."',
    render(A_neg, 'ask-a2'))
add('solar-firefly-garden-lights — a price axis with no number in its values',
    'The step degrades to price only ("להתחיל מ־…"), and the lead drops its last clause instead of inventing a unit.',
    render(D, 'ask-d'))
add('modern-led-wall-light-6w-up-down — another catalogue product',
    'A fourth shape, unchanged code path.',
    render(E, 'ask-e'))
add('The merchant switched the step off and emptied the quote block',
    'One CTA, no empty element, no orphan hairline; the lead ends after its first sentence + the photo clause.',
    render(A, 'ask-f', {'show_start_small': False}, blocks=[]))

add('No product at all (the section dropped on a template that has none)',
    'The store copy still renders; the small step is simply absent, because its words are the product\'s.',
    tpl.render(section={'id': 'ask-g', 'settings': dict(defaults), 'blocks': preset_blocks()}, **GLOBALS))

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl" class="env2-js"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — elmsnest-v2-pdp-ask</title>
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

out = os.path.join(HERE, 'ask.html')
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc), 'bytes')

nojs = doc.replace('<html lang="he" dir="rtl" class="env2-js">', '<html lang="he" dir="rtl">')
nojs = re.sub(r'<script>.*?</script>', '', nojs, flags=re.S)
out2 = os.path.join(HERE, 'ask-nojs.html')
open(out2, 'w', encoding='utf-8').write(nojs)
print('wrote', out2, len(nojs), 'bytes')

# ---------------------------------------------------------------- what actually rendered
def show(tag, out):
    print('\n---', tag)
    for m in re.finditer(r'<p class="env2-lead[^"]*">(.*?)</p>', out, re.S):
        print('  lead  :', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip())
    for m in re.finditer(r'<a class="([^"]*)" href="([^"]*)"([^>]*)>(.*?)</a>', out, re.S):
        print('  a     :', m.group(1), '|', m.group(2)[:70], '|',
              re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(4))).strip(), '|', m.group(3).strip()[:60])
    for m in re.finditer(r'<blockquote[^>]*>(.*?)</blockquote>', out, re.S):
        print('  quote :', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip())

for tag, o in (('A', main), ('B', render(B, 'x')), ('C', render(C, 'x')),
               ('A+notfit', render(A_neg, 'x')), ('firefly', render(D, 'x'))):
    show(tag, o)
print('\n"בוואטסאפ" anywhere:', 'בוואטסאפ' in doc)
print('bdi count in A:', main.count('<bdi'))
print('~~F~~ leak:', '~~F~~' in doc or '~~R~~' in doc)

# ---------------------------------------------------------------- all 27 products, one line each
print('\n--- the whole catalogue: the derived step label + the lead\'s last clause ---')
bad = 0
for h in sorted(DATA):
    o = render(build(h), 'x')
    lab = re.search(r'class="env2-btn env2-pdp-ask__start" href="([^"]*)"[^>]*>(.*?)</a>', o, re.S)
    lead = re.search(r'<p class="env2-lead[^"]*">(.*?)</p>', o, re.S)
    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', lab.group(2))).replace('&nbsp;', ' ').replace('&#8362;', '₪').strip() if lab else '(no step)'
    tail = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', lead.group(1))).split('תמונה')[-1].strip() if lead else ''
    if '~~' in o or 'Liquid error' in o or '<bdi></bdi>' in o: bad += 1; txt += '  !! BROKEN'
    print('  %-46s %-34s %s' % (h[:46], txt, tail))
print('broken:', bad)
