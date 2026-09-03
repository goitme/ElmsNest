# -*- coding: utf-8 -*-
# Renders sections/elmsnest-v2-coll-span.liquid - the REAL section file, through python-liquid,
# against data.json and the real snippets - onto the collection page ground.
#     python3 brief/side-pages/collection/build-preview/_build-span.py
# Harness-only substitutions (both are Shopify tags python-liquid does not implement):
#   * {% paginate %} / {% endpaginate %} stripped, `paginate` supplied;
#   * {% stylesheet %} / {% javascript %} / {% schema %} lifted out and re-attached as <style> and
#     <script>, which is what Shopify does with them.
# It also ASSERTS every figure of WINNING-SPEC 4.4's two closing tables and the three band counts.
import json, os, re, sys
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

SRC = open(os.path.join(SECT, 'elmsnest-v2-coll-span.liquid'), encoding='utf-8').read()


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
/* the ground the real template gives this section: it sits below the ruler and the bands, so the
   preview starts the 3.1 pixel gradient at the depth it has actually reached there. */
body{margin:0;background-position-y:-2600px}
</style>
</head>
<body class="hdt-page-type-collection template-collection">
<main id="MainContent" class="hdt-main-content">
<div class="shopify-section">%(markup)s</div>
</main>
<script>%(corejs)s</script>
<script>%(js)s</script>
</body></html>"""


def render(handle, extra=None, blocks=None):
    st = dict(DEFAULTS)
    st.update(extra or {})
    sec = {'id': 'coll_span', 'settings': st, 'blocks': blocks if blocks is not None else PRESET_BLOCKS}
    col = collection(handle)
    return env.from_string(MARKUP).render(**dict(GLOBALS, section=sec, collection=col, paginate=PAGINATE)), col


def page(out, handle, extra=None, blocks=None):
    markup, col = render(handle, extra, blocks)
    doc = PAGE % {'title': 'span · ' + handle, 'core': core_css, 'ground': ground,
                  'css': CSS, 'markup': markup, 'corejs': core_js, 'js': JS}
    open(os.path.join(HERE, out), 'w', encoding='utf-8').write(doc)
    rungs = len(re.findall(r'class="env2-coll-span__rung"', markup))
    bands = re.findall(r'class="env2-coll-span__bandlabel">(.*?)</h3>', markup, re.S)
    counts = re.findall(r'class="env2-coll-span__bandn"><bdi>(\d+)</bdi>', markup)
    tbl = len(re.findall(r'<table', markup))
    print('%-26s rungs=%-3d bands=%-3d counts=%-12s tables=%d' %
          (out, rungs, len(bands), ','.join(counts), tbl))
    for b, c in zip(bands, counts):
        print('     band %-22s <%s>' % (re.sub(r'<[^>]+>', '', b).strip(), c))
    return markup


def cells(markup, caption_num):
    # returns [(title, price, per_unit)] of the closing table whose caption carries caption_num
    blocks = re.split(r'<table', markup)
    for b in blocks:
        m = re.search(r'<caption[^>]*>.*?<bdi>([\d.]+)</bdi>', b, re.S)
        if not m or m.group(1) != caption_num: continue
        rows = re.findall(r'<tr>\s*<th scope="row"><a[^>]*>(.*?)</a></th>\s*'
                          r'<td><span class="env2-price"><bdi>([\d,.]+)</bdi> ₪</span></td>\s*'
                          r'<td[^>]*><bdi>≈([\d,.]+)</bdi></td>', b, re.S)
        return [(t.strip(), p, u) for t, p, u in rows]
    return []


T = {'waterproof-solar-deck-step-lights': DATA['products']['waterproof-solar-deck-step-lights']['title'],
     'warm-solar-step-deck-lights': DATA['products']['warm-solar-step-deck-lights']['title'],
     'retro-solar-path-lights-set': DATA['products']['retro-solar-path-lights-set']['title'],
     'modern-solar-path-lights-set': DATA['products']['modern-solar-path-lights-set']['title'],
     'swaying-solar-path-lights-ip65': DATA['products']['swaying-solar-path-lights-ip65']['title']}
WANT4 = [(T['waterproof-solar-deck-step-lights'], '149.90', '37.48'),
         (T['warm-solar-step-deck-lights'], '159.90', '39.98'),
         (T['retro-solar-path-lights-set'], '389.90', '97.48'),
         (T['modern-solar-path-lights-set'], '549.90', '137.48')]
WANT8 = [(T['waterproof-solar-deck-step-lights'], '149.90', '18.74'),
         (T['warm-solar-step-deck-lights'], '269.90', '33.74'),
         (T['modern-solar-path-lights-set'], '999.90', '124.99')]

if __name__ == '__main__':
    ok = True
    print('-- the five URLs, at the shipped defaults')
    m_decor_off, _ = render('גרילנדות-ותאורה-דקורטיבית')
    m_wall_off, _ = render('solar-wall-lights')
    for name, mk in (('decor', m_decor_off), ('wall', m_wall_off)):
        if mk.strip():
            print('  !! %s printed %d bytes at the defaults - 4.4 keeps this screen off it' % (name, len(mk.strip()))); ok = False
        else:
            print('%-26s prints NOTHING (4.4: off on this collection)' % (name + ' (default)'))
    m_path = page('span-path.html', 'תאורת-שביל-סולארית')
    m_spot = page('_span-spot.html', 'ספוטים-ופרוז-קטורים-סולאריים')
    m_all = page('_span-all.html', 'all')
    # decor and wall, forced on, so the degraded shape is provable too
    m_decor = page('span.html', 'גרילנדות-ותאורה-דקורטיבית', {'show_on': 'always'})
    page('_span-wall.html', 'solar-wall-lights', {'show_on': 'always'})
    page('_span-noblocks.html', 'תאורת-שביל-סולארית', None, [])

    print('-- 4.4 closing columns, against the spec tables')
    for stop, want in (('4', WANT4), ('8', WANT8)):
        got = cells(m_path, stop)
        print('   at %s: %s' % (stop, ' | '.join('%s %s %s' % (t[:22], p, u) for t, p, u in got)))
        if got != want:
            print('  !! at %s does not match 4.4' % stop)
            for a, b in zip(got, want):
                if a != b: print('      got %r want %r' % (a, b))
            if len(got) != len(want): print('      %d rows, want %d' % (len(got), len(want)))
            ok = False
    if T['swaying-solar-path-lights-ip65'] in ''.join(str(cells(m_path, s)) for s in ('4', '8')):
        print('  !! swaying appears in a per-unit column it does not sell'); ok = False
    note = re.search(r'class="env2-coll-span__note">(.*?)</li>', m_path, re.S)
    print('   note: %s' % re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', note.group(1))).strip() if note else '  !! no note')
    if not note or 'swaying' not in note.group(0) and T['swaying-solar-path-lights-ip65'] not in note.group(0):
        print('  !! swaying has no honest stops note'); ok = False

    print('-- the derived copy')
    for label, mk in (('path', m_path), ('spot', m_spot), ('all', m_all), ('decor(forced)', m_decor)):
        eb = re.search(r'class="env2-eyebrow[^"]*">(.*?)</p>', mk, re.S)
        dk = re.search(r'class="env2-lead[^"]*">(.*?)</p>', mk, re.S)
        rs = re.search(r'class="env2-coll-span__res">(.*?)</p>', mk, re.S)
        for nm, m in (('eyebrow', eb), ('deck', dk), ('res', rs)):
            if m: print('   %-13s %-8s %s' % (label, nm, re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()))
    if 'פי 14' not in re.sub(r'<[^>]+>', '', m_path): print('  !! the 14x sentence is not 14 on path'); ok = False
    if 'סט של 8 יחידות' not in re.sub(r'<[^>]+>', '', m_path): print('  !! the set-of-8 clause is missing'); ok = False
    if 'שמונה מנורות לאורך הדרך, 124.99 ₪ כל אחת.' not in re.sub(r'<[^>]+>', '', m_path):
        print('  !! the resolution line does not match 4.4'); ok = False
    for nm, mk in (('path', m_path), ('spot', m_spot), ('all', m_all), ('decor', m_decor)):
        for bad in ('None', 'Undefined', '{ratio', '{units', '{price', '{value'):
            if bad in mk: print('  !! %s leaked %r' % (nm, bad)); ok = False
    print('LINT-ISH %s' % ('OK' if ok else 'FAIL'))
    sys.exit(0 if ok else 2)
