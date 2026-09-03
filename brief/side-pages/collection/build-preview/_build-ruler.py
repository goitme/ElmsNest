# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-coll-ruler.liquid — the REAL section file, through python-liquid, against
data.json and the real snippets — into build-preview/ruler.html (decor) and ruler-path.html (path), plus
_ruler-{wall,spot,all}.html for the other three URLs. Nothing here ships.

    python3 brief/side-pages/collection/build-preview/_build-ruler.py
    node brief/shot.js brief/side-pages/collection/build-preview/ruler.html <prefix>

Two harness-only substitutions, both Shopify-tags python-liquid does not implement:
  * {% paginate collection.products by 50 %} / {% endpaginate %} are stripped and `paginate` is supplied
    as a 1-page object (27 products by 50 — the §3.7 case, where the control prints nothing);
  * {% stylesheet %} / {% javascript %} / {% schema %} are lifted out of the file and re-attached to the
    page as a <style> and a <script>, which is what Shopify does with them.
The MARKUP is otherwise the section's own bytes, and every number in it came out of the Liquid.
"""
import json, os, re, sys, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SECT = os.path.join(REPO, 'theme', 'sections')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/collection/data.json'), encoding='utf-8'))
IMG = '../../../assets/img/'

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle):
    p = DATA['products'][handle]
    n = min(4, len(p['images']))
    imgs = [Img(IMG + handle + '-' + str(i) + '.jpg', i) for i in range(n)]
    variants, vid = [], abs(hash(handle)) % 90000 + 10000
    for val in p['options'][0]['values']:
        for pr in p.get('firstAxis', {}).get(val, [p['priceMin']]):
            vid += 1
            variants.append({'id': vid, 'title': val, 'options': [val],
                             'price': int(round(pr * 100)), 'available': True, 'image': None})
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'price_min': int(round(p['priceMin'] * 100)), 'price_max': int(round(p['priceMax'] * 100)),
            'price_varies': p['priceMin'] != p['priceMax'], 'available': True,
            'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0] if imgs else None,
            'selected_or_first_available_variant': variants[0]}

SORT_OPTIONS = [{'value': v, 'name': v} for v in
                ('manual', 'best-selling', 'title-ascending', 'title-descending',
                 'price-ascending', 'price-descending', 'created-ascending', 'created-descending')]

def collection(handle, sort_by=None):
    if handle == 'all':
        handles = [h for ch in DATA['collections'] for h in DATA['collections'][ch]['handles']]
        title, url = 'קטלוג', '/collections/all'
    else:
        c = DATA['collections'][handle]
        handles, title, url = c['handles'], c['title'], '/collections/' + handle
    prods = [build(h) for h in handles]
    return {'handle': handle, 'title': title, 'url': url, 'products': prods,
            'products_count': len(prods), 'all_products_count': 27,
            'sort_by': sort_by, 'default_sort_by': 'manual', 'sort_options': SORT_OPTIONS,
            'image': None, 'description': ''}

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}

SRC = open(os.path.join(SECT, 'elmsnest-v2-coll-ruler.liquid'), encoding='utf-8').read()
def lift(tag, s):
    m = re.search(r'\{%-?\s*' + tag + r'\s*-?%\}(.*?)\{%-?\s*end' + tag + r'\s*-?%\}', s, re.S)
    if not m: sys.exit('no ' + tag + ' block in the section')
    return m.group(1), s[:m.start()] + s[m.end():]
CSS, SRC = lift('stylesheet', SRC)
JS, SRC = lift('javascript', SRC)
SCHEMA_TXT, SRC = lift('schema', SRC)
SCHEMA = json.loads(SCHEMA_TXT)
MARKUP = re.sub(r'\{%-?\s*(paginate .*?|endpaginate)\s*-?%\}', '', SRC, flags=re.S)

DEFAULTS = {}
for s in SCHEMA.get('settings', []):
    if s.get('type') == 'header': continue
    DEFAULTS[s['id']] = s.get('default', '')
PAGINATE = {'pages': 1, 'current_page': 1, 'items': 27,
            'previous': {'title': '', 'url': None, 'is_link': False},
            'next': {'title': '', 'url': None, 'is_link': False}, 'parts': []}

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-collection">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-collection.liquid'), encoding='utf-8').read(), re.S).group(1)
card_css = env.from_string("{% render 'elmsnest-v2-pdp-card', css: true %}").render(**GLOBALS)

PAGE = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
%(cardcss)s
<style>%(css)s</style>
</head>
<body class="hdt-page-type-collection template-collection">
<main id="MainContent" class="hdt-main-content">
<div class="shopify-section">%(markup)s</div>
</main>
<script>%(corejs)s</script>
<script>%(js)s</script>
</body></html>"""

def render_page(out, handle, sort_by=None, extra=None):
    st = dict(DEFAULTS)
    st.update(extra or {})
    sec = {'id': 'coll_ruler', 'settings': st, 'blocks': []}
    col = collection(handle, sort_by)
    markup = env.from_string(MARKUP).render(**dict(GLOBALS, section=sec, collection=col, paginate=PAGINATE))
    doc = PAGE % {'title': 'ruler · ' + handle, 'core': core_css, 'ground': ground,
                  'cardcss': card_css, 'css': CSS, 'markup': markup, 'corejs': core_js, 'js': JS}
    path = os.path.join(HERE, out)
    open(path, 'w', encoding='utf-8').write(doc)
    # report what the Liquid actually decided
    stops = re.findall(r'id="env2-stop-([A-Za-z0-9_]+)"', markup)
    rows = markup.count('class="env2-coll-ruler__row"')
    beyond = markup.count('data-state="beyond"')
    print('%-22s rows=%-3d stops=%-42s beyond-answers=%d  %s' %
          (out, rows, ','.join(stops), beyond, path))
    return markup

m_decor = render_page('ruler.html', 'גרילנדות-ותאורה-דקורטיבית')
m_path = render_page('ruler-path.html', 'תאורת-שביל-סולארית')
render_page('_ruler-wall.html', 'solar-wall-lights')
render_page('_ruler-spot.html', 'ספוטים-ופרוז-קטורים-סולאריים')
render_page('_ruler-all.html', 'all')
render_page('_ruler-sorted.html', 'גרילנדות-ותאורה-דקורטיבית', sort_by='price-ascending')

# ---- assertions the sign-off list (§7) turns on -------------------------------------------------
def answer(markup, title_fragment, stop):
    """the answer block a row prints at one stop, as rendered"""
    i = markup.find(title_fragment)
    if i < 0: return 'ROW NOT FOUND'
    seg = markup[i:markup.find('class="env2-coll-ruler__row"', i + 1) if markup.find('class="env2-coll-ruler__row"', i + 1) > 0 else len(markup)]
    m = re.search(r'data-stop="' + stop + r'"[^>]*data-state="([a-z]+)"(.*?)</span>\s*(?:<span class="env2-coll-rail__v"|</div>)', seg, re.S)
    if not m: return 'NO ANSWER AT ' + stop
    txt = re.sub(r'<[^>]+>', '', m.group(2))
    return m.group(1) + ' :: ' + ' '.join(txt.split())

print('\n-- decor at the 10 מ׳ stop (§7 check 4) --')
for frag in ('שרשרת חבל', 'קריסטל', 'כדורי LED', 'אדיסון'):
    print('  %-12s %s' % (frag, answer(m_decor, frag, '10')))
print('-- path at the 4 stop --')
for frag in ('לדק ולמדרגות', 'רטרו', 'מודרני'):
    print('  %-14s %s' % (frag, answer(m_path, frag, '4')))
