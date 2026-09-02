# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-pdp-terms.liquid (WINNING-SPEC §4.6, "the four numbers") with the
REAL Liquid (python-liquid), the REAL preset blocks out of its own {% schema %}, and the REAL
elmsnest-v2-pdp-photo-cta snippet, on the real core CSS + the real PDP ground, into
build-preview/terms.html. Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-terms.py
    node brief/shot.js brief/side-pages/pdp/build-preview/terms.html brief/side-pages/pdp/build-preview/terms
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-pdp-terms.liquid')
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

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle):
    p = DATA[handle]
    imgs = [Img('../../../assets/img/' + handle + '-' + str(i) + '.jpg', i)
            for i in range(min(4, len(p['images'])))]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'variants': p['variants'], 'images': imgs, 'featured_image': imgs[0] if imgs else None,
            'metafields': {'custom': {}}}

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['money_without_currency'] = lambda v: '%.2f' % (v / 100.0)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'},
           'settings': {'whatsapp_number': ''}}
tpl = env.from_string(markup)

def render(product, sid='terms', over=None, blocks=None):
    st = dict(defaults); st.update(over or {})
    return tpl.render(product=product, section={'id': sid, 'settings': st,
                                                'blocks': blocks if blocks is not None else preset_blocks()},
                      **GLOBALS)

A = build('solar-crystal-ball-string-lights')
B = build('stainless-steel-solar-path-light-ip65')
C = build('waterproof-led-wall-light-ip65-6w-12w')

main = render(A, 'terms-a')

parts = []
def add(label, note, out):
    parts.append('<p class="fp-label"><b>%s</b> %s</p>\n%s' % (html.escape(label), html.escape(note), out))

parts.append(main)
add('B · stainless-steel-solar-path-light-ip65 — 1 variant',
    'Byte-for-byte the same ledger: this section reads no variant, no option, no image index and no metafield. Only the prefilled mail body (inside the photo-CTA snippet) names the product.',
    render(B, 'terms-b'))
add('C · waterproof-led-wall-light-ip65-6w-12w — MAINS / power unstated',
    'Nothing about power is said here at all, on any product, so §3.7 cannot be breached by this section.',
    render(C, 'terms-c'))
add('The merchant emptied the deck, the foot links and the 4th link (a robustness case)',
    'Head collapses to eyebrow + h2, the ledger closes itself, no foot nav, no CTA — and no empty element is printed.',
    render(A, 'terms-d', {'deck': '', 'foot_links': ''},
           blocks=[b for b in preset_blocks()][:3]))
add('One block carrying its own link_url (not the photo CTA)',
    'A block with a URL gets a plain anchor; a block with a label and no URL gets the shared photo-CTA snippet. No section ever builds a mailto of its own.',
    render(A, 'terms-e', blocks=(lambda bs: (bs[3]['settings'].__setitem__('link_url', '/policies/refund-policy'),
                                             bs[3]['settings'].__setitem__('link_label', 'לנוסח המלא'), bs)[-1])(preset_blocks())))

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl" class="env2-js"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — elmsnest-v2-pdp-terms</title>
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

out = os.path.join(HERE, 'terms.html')
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc), 'bytes')

nojs = doc.replace('<html lang="he" dir="rtl" class="env2-js">', '<html lang="he" dir="rtl">')
nojs = re.sub(r'<script>.*?</script>', '', nojs, flags=re.S)
out2 = os.path.join(HERE, 'terms-nojs.html')
open(out2, 'w', encoding='utf-8').write(nojs)
print('wrote', out2, len(nojs), 'bytes')

# ---- the rendered ledger, as text ----
print('\n--- A, the shipped preset ---')
for m in re.finditer(r'<li class="env2-pdp-terms__line".*?</li>', main, re.S):
    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(0))).strip()
    print('   ', txt)
for m in re.finditer(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', main, re.S):
    print('    link ->', m.group(1)[:96], '|', re.sub(r'<[^>]+>', '', m.group(2)).strip())
print('\n"בוואטסאפ" in output:', 'בוואטסאפ' in main)
print('bdi count:', main.count('<bdi'))
