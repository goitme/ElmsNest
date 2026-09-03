# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-coll-bands.liquid — the REAL section file, through python-liquid,
against data.json and the real snippets — into build-preview/bands.html (decor) and bands-path.html
(path), plus _bands-{wall,spot,all}.html for the other three URLs. Nothing here ships.

    python3 brief/side-pages/collection/build-preview/_build-bands.py
    node brief/shot.js brief/side-pages/collection/build-preview/bands.html <prefix>

Harness-only substitutions, both Shopify tags python-liquid does not implement:
  * {% paginate collection.products by 50 %} / {% endpaginate %} are stripped, `paginate` supplied;
  * {% stylesheet %} / {% javascript %} / {% schema %} are lifted out and re-attached as <style> and
    <script>, which is what Shopify does with them.
The markup is otherwise the section's own bytes, and every number in it came out of the Liquid.

It also ASSERTS the two rules the section cannot be shipped without (§4.3 n-n 1 and n-n 5): no two
bands share a composition, and every product of the collection appears in exactly one band.
"""
import json, os, re, sys, collections
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
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1
        o.width = 1600; o.height = 1200
        return o


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


COLLIMG = {'גרילנדות-ותאורה-דקורטיבית': 'collection-decor.jpg',
           'תאורת-שביל-סולארית': 'collection-path.jpg',
           'solar-wall-lights': 'collection-wall.jpg',
           'ספוטים-ופרוז-קטורים-סולאריים': 'collection-spot.jpg'}

SORT_OPTIONS = [{'value': v, 'name': v} for v in
                ('manual', 'title-ascending', 'price-ascending', 'price-descending')]


def collection(handle, sort_by=None):
    if handle == 'all':
        handles = [h for ch in DATA['collections'] for h in DATA['collections'][ch]['handles']]
        title, url, img = 'קטלוג', '/collections/all', None
    else:
        c = DATA['collections'][handle]
        handles, title, url = c['handles'], c['title'], '/collections/' + handle
        img = Img(IMG + COLLIMG[handle], 0)
    prods = [build(h) for h in handles]
    return {'handle': handle, 'title': title, 'url': url, 'products': prods,
            'products_count': len(prods), 'all_products_count': 27,
            'sort_by': sort_by, 'default_sort_by': 'manual', 'sort_options': SORT_OPTIONS,
            'image': img, 'description': ''}


env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}

SRC = open(os.path.join(SECT, 'elmsnest-v2-coll-bands.liquid'), encoding='utf-8').read()


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
    if s.get('type') in ('header', 'paragraph'): continue
    DEFAULTS[s['id']] = s.get('default', '')
PRESET = SCHEMA['presets'][0]
DEFAULTS.update(PRESET.get('settings', {}))
PRESET_BLOCKS = [{'type': b['type'], 'settings': b.get('settings', {}), 'shopify_attributes': '',
                  'id': 'b%d' % i} for i, b in enumerate(PRESET.get('blocks', []))]
PAGINATE = {'pages': 1, 'current_page': 1, 'items': 27,
            'previous': {'title': '', 'url': None, 'is_link': False},
            'next': {'title': '', 'url': None, 'is_link': False}, 'parts': []}

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-collection">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-collection.liquid'), encoding='utf-8').read(), re.S).group(1)

PAGE = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(css)s</style>
<style>
/* the page ground the real template gives this section: it sits BELOW the ruler, so the preview
   starts it at the depth the §3.1 pixel gradient has actually reached there (about 1500px in). */
body{margin:0;background-position-y:-1500px}
</style>
</head>
<body class="hdt-page-type-collection template-collection">
<main id="MainContent" class="hdt-main-content">
<div class="shopify-section">%(markup)s</div>
</main>
<script>%(corejs)s</script>
<script>%(js)s</script>
</body></html>"""


def render_page(out, handle, sort_by=None, extra=None, blocks=None):
    st = dict(DEFAULTS)
    st.update(extra or {})
    sec = {'id': 'coll_bands', 'settings': st, 'blocks': blocks if blocks is not None else PRESET_BLOCKS}
    col = collection(handle, sort_by)
    markup = env.from_string(MARKUP).render(**dict(GLOBALS, section=sec, collection=col, paginate=PAGINATE))
    doc = PAGE % {'title': 'bands · ' + handle, 'core': core_css, 'ground': ground,
                  'css': CSS, 'markup': markup, 'corejs': core_js, 'js': JS}
    path = os.path.join(HERE, out)
    open(path, 'w', encoding='utf-8').write(doc)

    comps = re.findall(r'env2-coll-bands__band env2-coll-bands__band--(\w+)', markup)
    cards = re.findall(r'href="/products/([a-z0-9\-]+)"', markup)
    hrefs = collections.Counter(re.findall(r'class="env2-pdp-card__title"><a href="/products/([a-z0-9\-]+)"', markup))
    if not hrefs:
        hrefs = collections.Counter(re.findall(r'<h3 class="env2-pdp-card__title">\s*<a href="/products/([a-z0-9\-]+)"', markup))
    want = [p['handle'] for p in col['products']]
    labels = [re.sub(r'<[^>]+>', '', x).strip() for x in
              re.findall(r'class="env2-h env2-coll-bands__h2">(.*?)</h2>', markup, re.S)]
    ok = True
    if len(comps) != len(set(comps)):
        print('  !! a composition repeats: %s' % comps); ok = False
    missing = [h for h in want if hrefs.get(h, 0) < 1]
    extra_h = [h for h, n in hrefs.items() if n > 1]
    if missing: print('  !! products missing from every band: %s' % missing); ok = False
    if extra_h: print('  !! products carded twice: %s' % extra_h); ok = False
    scrim = len(re.findall(r'<article class="[^"]*env2-pdp-card--scene', markup))
    if scrim > 1: print('  !! %d scrim cards — the page allows ONE here (§3.1)' % scrim); ok = False
    kick = len(re.findall(r'<p class="env2-kicker env2-pdp-card__kicker"', markup))
    if kick > 1: print('  !! kicker printed %d times' % kick); ok = False
    plates = markup.count('class="env2-coll-glyph"')
    print('%-20s bands=%-2d comps=%-28s cards=%-3d plates=%-3d scrim=%d kicker=%d %s'
          % (out, len(comps), ','.join(comps), sum(hrefs.values()), plates, scrim, kick,
             'OK' if ok else 'FAIL'))
    print('     labels: ' + ' | '.join(l.strip() for l in labels))
    return markup, ok


if __name__ == '__main__':
    allok = True
    for out, h in (('bands.html', 'גרילנדות-ותאורה-דקורטיבית'),
                   ('bands-path.html', 'תאורת-שביל-סולארית'),
                   ('_bands-wall.html', 'solar-wall-lights'),
                   ('_bands-spot.html', 'ספוטים-ופרוז-קטורים-סולאריים'),
                   ('_bands-all.html', 'all')):
        _, ok = render_page(out, h)
        allok = allok and ok
    _, ok = render_page('_bands-sorted.html', 'גרילנדות-ותאורה-דקורטיבית', sort_by='price-ascending')
    allok = allok and ok
    sys.exit(0 if allok else 2)
