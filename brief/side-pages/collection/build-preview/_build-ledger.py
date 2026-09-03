# -*- coding: utf-8 -*-
# Renders sections/elmsnest-v2-coll-ledger.liquid - the REAL section file, through python-liquid,
# against data.json and the real snippets - onto the collection page ground.
#     python3 brief/side-pages/collection/build-preview/_build-ledger.py
# Harness-only substitutions (Shopify tags python-liquid does not implement):
#   * {% stylesheet %} / {% javascript %} / {% schema %} lifted out and re-attached as <style> and
#     <script>, which is what Shopify does with them.
# It also ASSERTS every row of WINNING-SPEC 4.5's decor table and every path row, from the parser.
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
            'products_count': len(prods), 'all_products_count': len(prods),
            'sort_by': sort_by, 'default_sort_by': 'manual', 'sort_options': SORT_OPTIONS,
            'image': img, 'description': ''}


env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}

SRC = open(os.path.join(SECT, 'elmsnest-v2-coll-ledger.liquid'), encoding='utf-8').read()


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
PRESET_BLOCKS = [{'type': b['type'], 'settings': dict(
    [(x['id'], x.get('default', '')) for bt in SCHEMA.get('blocks', []) if bt['type'] == b['type']
     for x in bt.get('settings', []) if x.get('id')], **b.get('settings', {})),
    'shopify_attributes': '', 'id': 'b%d' % i} for i, b in enumerate(PRESET.get('blocks', []))]

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-collection">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-collection.liquid'), encoding='utf-8').read(), re.S).group(1)
pag = open(os.path.join(SNIP, 'elmsnest-v2-coll-paginate.liquid'), encoding='utf-8').read()
pag_css = re.search(r'<style id="env2-coll-paginate-css">(.*?)</style>', pag, re.S).group(1)

PAGE = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(pag)s</style>
<style>%(css)s</style>
<style>
/* the ground the real template gives this section: the ledger is the fifth of seven sections, so the
   preview starts the 3.1 pixel gradient at the depth it has actually reached there. */
body{margin:0;background-position-y:-3200px}
/* a stand-in for the ruler section that sits above it in the template, so the row links have the
   real anchor and the real radios to check. */
.env2-ruler-stub{padding:40px 0;border-block-end:1px solid var(--env2-hair)}
.env2-ruler-stub p{margin:0;font:300 14px/1.5 var(--env2-sans);color:var(--env2-mute)}
</style>
</head>
<body class="hdt-page-type-collection template-collection">
<main id="MainContent" class="hdt-main-content">
<div class="shopify-section"><section id="env2-coll-ruler" data-unit-key="%(unitkey)s" class="env2-section env2-coll env2-ruler-stub" dir="rtl" style="scroll-margin-top:90px">
<div class="env2-wrap">%(radios)s<p>סרגל המידה (קטע אחר) — כאן רק כדי שקישורי השורות יוכלו לבדוק את העצירה.</p></div></section></div>
<div class="shopify-section">%(markup)s</div>
</main>
<script>%(corejs)s</script>
<script>%(js)s</script>
</body></html>"""


def render(handle, extra=None, blocks=None):
    st = dict(DEFAULTS)
    st.update(extra or {})
    sec = {'id': 'coll_ledger', 'settings': st, 'blocks': blocks if blocks is not None else PRESET_BLOCKS}
    col = collection(handle)
    return env.from_string(MARKUP).render(**dict(GLOBALS, section=sec, collection=col)), col


def page(out, handle, extra=None, blocks=None, unitkey='len', stops=()):
    markup, col = render(handle, extra, blocks)
    radios = ''.join('<input type="radio" name="env2-stop" id="env2-stop-%s" style="position:absolute;opacity:0">' % k
                     for k in stops)
    doc = PAGE % {'title': 'ledger · ' + handle, 'core': core_css, 'ground': ground, 'pag': pag_css,
                  'css': CSS, 'markup': markup, 'corejs': core_js, 'js': JS,
                  'unitkey': unitkey, 'radios': radios}
    open(os.path.join(HERE, out), 'w', encoding='utf-8').write(doc)
    rows = re.findall(r'class="env2-coll-ledger__row"', markup)
    offers = re.findall(r'class="env2-coll-ledger__o"', markup)
    print('%-24s rows=%-3d offers=%-3d bytes=%d' % (out, len(rows), len(offers), len(markup.strip())))
    return markup


def table(markup):
    """[(measure, [(name, second, price, per)])] as the markup really prints it."""
    out = []
    for row in re.findall(r'<li class="env2-coll-ledger__row">(.*?)</ul>\s*</li>', markup, re.S):
        k = re.search(r'<bdi>([\d.]+)</bdi><small[^>]*>(.*?)</small>', row, re.S)
        offers = []
        for o in re.findall(r'<li class="env2-coll-ledger__o">(.*?)</li>', row, re.S):
            nm = re.search(r'class="env2-coll-ledger__name"[^>]*>(.*?)</a>', o, re.S)
            sec = re.search(r'class="env2-coll-ledger__second"><bdi>(\d+)</bdi> (.*?)</span>', o, re.S)
            pr = re.search(r'class="env2-coll-ledger__price"><bdi>([\d,.]+)</bdi>', o, re.S)
            pu = re.search(r'class="env2-coll-ledger__per"><bdi>≈([\d,.]+)</bdi> (.*?)</span>', o, re.S)
            offers.append((re.sub(r'<[^>]+>', '', nm.group(1)).strip() if nm else '?',
                           (sec.group(1) + ' ' + sec.group(2)) if sec else '',
                           pr.group(1) if pr else '?',
                           (pu.group(1) + ' ' + pu.group(2)) if pu else ''))
        out.append(((k.group(1), k.group(2)) if k else ('?', '?'), offers))
    return out


# WINNING-SPEC 4.5 - the decor table, verbatim: measure -> [(name fragment, price)]
WANT_DECOR = [
    ('1.5', [('כדורי LED', '10 נורות', '89.90')]),
    ('3',   [('כדורי LED', '20 נורות', '99.90')]),
    ('5',   [('כדורי קריסטל', '20 נורות', '89.90'), ('נורות אדיסון', '10 נורות', '139.90')]),
    ('6',   [('כדורי LED', '40 נורות', '119.90')]),
    ('6.5', [('כדורי קריסטל', '30 נורות', '89.90')]),
    ('7',   [('שרשרת חבל', '50 נורות', '89.90')]),
    ('8',   [('נורות אדיסון', '20 נורות', '179.90')]),
    ('9.5', [('כדורי קריסטל', '50 נורות', '99.90')]),
    ('10',  [('כדורי LED', '80 נורות', '169.90')]),
    ('11',  [('כדורי קריסטל', '60 נורות', '109.90')]),
    ('12',  [('שרשרת חבל', '100 נורות', '99.90'), ('כדורי LED', '100 נורות', '179.90')]),
    ('13',  [('כדורי קריסטל', '100 נורות', '129.90')]),
    ('22',  [('שרשרת חבל', '200 נורות', '119.90'), ('כדורי קריסטל', '200 נורות', '179.90')]),
    ('32',  [('שרשרת חבל', '300 נורות', '159.90')]),
]
# path - 1 2 4 6 8 12, price and per-unit, straight off the parser
WANT_PATH = [
    ('1',  [('69.90', '69.90')]),
    ('2',  [('149.90', '74.95'), ('189.90', '94.95'), ('219.90', '109.95')]),
    ('4',  [('149.90', '37.48'), ('159.90', '39.98'), ('389.90', '97.48'), ('549.90', '137.48')]),
    ('6',  [('149.90', '24.98'), ('329.90', '54.98'), ('529.90', '88.32')]),
    ('8',  [('149.90', '18.74'), ('269.90', '33.74'), ('999.90', '124.99')]),
    ('12', [('349.90', '29.16')]),
]

if __name__ == '__main__':
    ok = True
    print('-- the five URLs, at the shipped defaults')
    for name, h in (('wall', 'solar-wall-lights'), ('spot', 'ספוטים-ופרוז-קטורים-סולאריים'), ('all', 'all')):
        mk, _ = render(h)
        if mk.strip():
            print('  !! %s printed %d bytes at the defaults' % (name, len(mk.strip()))); ok = False
        else:
            print('%-24s prints NOTHING (4.5 / 3.8.5: no shared unit)' % (name + ' (default)'))

    m_decor = page('ledger.html', 'גרילנדות-ותאורה-דקורטיבית', unitkey='len',
                   stops=('1_5', '6', '7', '10', '12', '32', 'all'))
    m_path = page('ledger-path.html', 'תאורת-שביל-סולארית', unitkey='qty',
                  stops=('1', '2', '4', '6', '8', '12', 'all'))
    page('_ledger-all.html', 'all', {'show_on': 'always'}, unitkey='qty', stops=('1', '2', '4', '6', '8', '12'))
    page('_ledger-spot.html', 'ספוטים-ופרוז-קטורים-סולאריים', {'show_on': 'always'}, unitkey='band')
    page('_ledger-wall.html', 'solar-wall-lights', {'show_on': 'always'}, unitkey='band')
    page('_ledger-noblocks.html', 'גרילנדות-ותאורה-דקורטיבית', None, [], unitkey='len')
    page('_ledger-nolinks.html', 'גרילנדות-ותאורה-דקורטיבית', {'link_rows': False, 'short_titles': False,
                                                              'show_unit_price': 'always'}, unitkey='len')

    print('-- 4.5 decor table, row by row')
    got = table(m_decor)
    if len(got) != len(WANT_DECOR):
        print('  !! %d rows, 4.5 wants %d' % (len(got), len(WANT_DECOR))); ok = False
    for (k, offs), (wk, woffs) in zip(got, WANT_DECOR):
        line = ' · '.join('%s %s — %s ₪' % (n, s, p) for n, s, p, _ in offs)
        print('   %-5s %-3s %s' % (k[0], k[1], line))
        if k[0] != wk: print('  !! measure %s, 4.5 wants %s' % (k[0], wk)); ok = False
        if len(offs) != len(woffs):
            print('  !! %s has %d offers, 4.5 wants %d' % (k[0], len(offs), len(woffs))); ok = False
            continue
        for (n, s, p, _), (wn, ws, wp) in zip(offs, woffs):
            if wn not in n or s != ws or p != wp:
                print('  !! %s: got (%r,%r,%r) want (%r,%r,%r)' % (k[0], n, s, p, wn, ws, wp)); ok = False

    print('-- path table, price and per-unit')
    gotp = table(m_path)
    if [k[0] for k, _ in gotp] != [k for k, _ in WANT_PATH]:
        print('  !! path measures %s' % [k[0] for k, _ in gotp]); ok = False
    for (k, offs), (wk, woffs) in zip(gotp, WANT_PATH):
        print('   %-4s %-3s %s' % (k[0], k[1], ' · '.join('%s — %s ₪ · %s' % (n[:24], p, u) for n, _, p, u in offs)))
        gp = [(p, u.split(' ')[0]) for _, _, p, u in offs]
        if gp != woffs: print('  !! %s: got %s want %s' % (k[0], gp, woffs)); ok = False

    print('-- the foot')
    for label, mk in (('decor', m_decor), ('path', m_path)):
        f = re.search(r'class="env2-coll-ledger__rest">(.*?)</p>', mk, re.S)
        txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', f.group(1))).strip() if f else '(none)'
        print('   %-6s %s' % (label, txt))
        if label == 'decor':
            for must in ('שלוש', 'לפי שטח', '1.5×1.5 מ׳', '12×2 מ׳', '6×4 מ׳', 'דגם אחד: 10 נורות', 'צבע תאורה'):
                if must not in txt: print('  !! decor foot is missing %r' % must); ok = False
        note = re.search(r'class="env2-coll-paginate__note">(.*?)</p>', mk, re.S)
        print('   %-6s %s' % ('', re.sub(r'<[^>]+>', '', note.group(1)).strip() if note else '  !! no page note'))

    print('-- leaks and forbidden markup')
    for nm, mk in (('decor', m_decor), ('path', m_path)):
        for bad in ('None', 'Undefined', '{n_word', '{name}', '{value}', '{min}', '{max}', '{axis}',
                    '{unit}', '{n}', 'compare', 'מבצע'):
            if bad in mk: print('  !! %s leaked %r' % (nm, bad)); ok = False
        if re.search(r'</bdi>\s*/\s*<bdi>', mk): print('  !! %s split a bdi pair' % nm); ok = False
        if '₪ למטר≈' in mk or '≈</bdi>' in mk: print('  !! %s put the ≈ outside the bdi' % nm); ok = False
        if 'env2-btn' in mk: print('  !! %s carries an .env2-btn (REPORT 9.1)' % nm); ok = False
    print('LINT-ISH %s' % ('OK' if ok else 'FAIL'))
    sys.exit(0 if ok else 2)
