# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-coll-scene.liquid (§4.1, the gate) with the REAL Liquid through
python-liquid, against the real collection snippets, the local image pack and the local fonts, into
build-preview/scene.html (DECOR) and scene-path.html (PATH). Nothing here ships — it is the offline
proof the section is measured on.

    python3 brief/side-pages/collection/build-preview/_build-scene.py
    node brief/shot.js brief/side-pages/collection/build-preview/scene.html \
         brief/side-pages/collection/build-preview/scene
"""
import json, os, re, sys
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-coll-scene.liquid')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/collection/data.json'), encoding='utf-8'))
IMG  = '../../../assets/img/'

# the two collection descriptions the audit quotes verbatim (brief/inventory/AUDIT-collection.md)
DESC = {
 'גרילנדות-ותאורה-דקורטיבית':
   '<p>גרילנדות ותאורה דקורטיבית לחצר, למרפסת, לפרגולה ולפינות ישיבה. תאורה שמוסיפה אווירה חמימה ונעימה '
   'לערבים בחוץ — בלי להפוך את ההתקנה לפרויקט.</p><p>מתאים לאירוח, לפינת קפה, לשבילי גינה וליצירת מראה '
   'מעוצב סביב הבית.</p>',
 'תאורת-שביל-סולארית':
   '<p>תאורת שביל סולארית לגינה, לכניסה, לחצר ולמעברים חיצוניים. פתרון פשוט להדגשת הדרך, לשיפור הנראות '
   'בלילה וליצירת מראה מסודר ונעים סביב הבית.</p><p>מתאים במיוחד לשבילים, ערוגות, מדרגות, כניסות ופינות '
   'מעבר בגינה.</p>',
 'solar-wall-lights':
   '<p>תאורת קיר סולארית לחוץ הבית — פתרונות תאורה נוחים לגינה, לחצר, לכניסה, למרפסת ולקירות חוץ. מתאימה '
   'ליצירת אור שימושי ואווירה נעימה בלי חיבור קבוע לחשמל ובלי התקנה מסובכת.</p>'
   '<p>בחרו תאורה לפי עוצמת האור, אזור ההתקנה והסגנון שמתאים לבית שלכם.</p>',
 'ספוטים-ופרוז-קטורים-סולאריים':
   '<p>ספוטים ופרוז׳קטורים סולאריים לחוץ הבית — פתרונות תאורה חזקים יותר לאזורים שצריכים נראות טובה, כמו '
   'כניסה לבית, חניה, חצר, שביל או קיר חיצוני.</p>'
   '<p>בחרו לפי אזור ההתקנה, עוצמת התאורה, זווית ההארה והצורך שלכם בין תאורת אווירה לתאורה שימושית.</p>',
 'all': '',
}
COLLIMG = {'גרילנדות-ותאורה-דקורטיבית': 'collection-decor.jpg',
           'תאורת-שביל-סולארית': 'collection-path.jpg',
           'solar-wall-lights': 'collection-wall.jpg',
           'ספוטים-ופרוז-קטורים-סולאריים': 'collection-spot.jpg',
           'all': ''}


def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)


class Img(str):
    def __new__(cls, path, i, w=960, h=1200):
        o = str.__new__(cls, path)
        o.src = path; o.alt = ''; o.position = i + 1; o.width = w; o.height = h
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
    # data.json holds the REAL total variant count; the first-axis rows above are one per priced option
    # value, so pad the list back up to the real size (same values, same prices) — otherwise the counts
    # line in the render would print a variant total the shop does not have.
    i = 0
    while len(variants) < p['variants'] and variants:
        src = variants[i % len(variants)]
        vid += 1
        variants.append(dict(src, id=vid))
        i += 1
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'price_min': int(round(p['priceMin'] * 100)), 'price_max': int(round(p['priceMax'] * 100)),
            'price_varies': p['priceMin'] != p['priceMax'], 'available': True,
            'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0] if imgs else None,
            'selected_or_first_available_variant': variants[0]}


ALL_PRODUCTS = {h: build(h) for h in DATA['products']}


def collection(ch):
    if ch == 'all':
        handles = [h for c in DATA['collections'].values() for h in c['handles']]
        title, img = 'קטלוג', ''
    else:
        c = DATA['collections'][ch]
        handles, title = c['handles'], c['title']
        img = COLLIMG[ch]
    prods = [ALL_PRODUCTS[h] for h in handles]
    return {'handle': ch, 'title': title, 'description': DESC.get(ch, ''),
            'products': prods, 'products_count': len(prods), 'all_products_count': 27,
            'image': Img(IMG + img, 0, 960, 1200) if img else None,
            'url': '/collections/' + ch, 'sort_by': None}


env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'},
           'settings': {'whatsapp_number': ''}, 'all_products': ALL_PRODUCTS}

# the section file, minus the three tags python-liquid does not know; the CSS and the JS are lifted out
# and inlined into the page exactly as Shopify would serve them.
src = open(SEC, encoding='utf-8').read()
CSS = re.search(r'\{%\s*stylesheet\s*%\}(.*?)\{%\s*endstylesheet\s*%\}', src, re.S).group(1)
JS  = re.search(r'\{%\s*javascript\s*%\}(.*?)\{%\s*endjavascript\s*%\}', src, re.S).group(1)
SCHEMA = json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}', src, re.S).group(1))
BODY = re.sub(r'\{%\s*(stylesheet|javascript|schema)\s*%\}.*?\{%\s*end\1\s*%\}', '', src, flags=re.S)

# the section's settings come from the ONE preset the schema ships, filled out with every schema default,
# so the preview is exactly what a merchant gets when they drop the section in.
defaults = {}
for s in SCHEMA['settings']:
    if 'id' in s and 'default' in s:
        defaults[s['id']] = s['default']
preset = SCHEMA['presets'][0]
settings = dict(defaults, **preset.get('settings', {}))
for s in SCHEMA['settings']:
    if 'id' in s:
        settings.setdefault(s['id'], '')
blocks = [{'type': b['type'], 'settings': b.get('settings', {}), 'shopify_attributes': '',
           'id': 'b%d' % i} for i, b in enumerate(preset.get('blocks', []))]
SECTION = {'id': 'coll_scene', 'settings': settings, 'blocks': blocks}

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core = re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', '', core, flags=re.S).strip()

PAGE = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
%(core)s
<style>
body{margin:0}
/* the Kalles header the real page renders above the section, at its real height, transparent over the
   scene exactly as §4.1 requires — so the fold measurement below is the one the visitor gets. */
.env2-mock-header{position:absolute;inset-block-start:0;inset-inline:0;block-size:70px;z-index:9;
  display:flex;align-items:center;justify-content:space-between;padding-inline:clamp(20px,4vw,64px);
  font-family:var(--env2-sans);font-size:13px;letter-spacing:.14em;color:var(--env2-ink);pointer-events:none}
@media (max-width:900px){.env2-mock-header{block-size:60px}}
</style>
<style>%(css)s</style>
</head>
<body class="hdt-page-type-collection template-collection">
<div class="env2-mock-header"><span>ElmsNest</span><span>סל</span></div>
<div id="MainContent"><div class="shopify-section">%(html)s</div></div>
<script>%(js)s</script>
</body></html>"""


def render_page(ch, out, extra_settings=None):
    st = dict(settings, **(extra_settings or {}))
    sec = dict(SECTION, settings=st)
    html = env.from_string(BODY).render(**dict(GLOBALS, collection=collection(ch), section=sec))
    doc = PAGE % {'title': 'ElmsNest — מסך פתיחה · ' + ch, 'core': core, 'css': CSS, 'js': JS, 'html': html}
    open(os.path.join(HERE, out), 'w', encoding='utf-8').write(doc)
    print('wrote', out, len(doc), 'bytes')
    return html


if __name__ == '__main__':
    GLOBALS['collections'] = {ch: collection(ch) for ch in list(DATA['collections']) + ['all']}
    h1 = render_page('גרילנדות-ותאורה-דקורטיבית', 'scene.html')
    render_page('תאורת-שביל-סולארית', 'scene-path.html')
    render_page('solar-wall-lights', 'scene-wall.html')
    render_page('ספוטים-ופרוז-קטורים-סולאריים', 'scene-spot.html')
    render_page('all', 'scene-all.html')
    for tag in ('<h1', 'env2-coll-scene__pin', 'env2-pdp-card--scene', 'env2-coll-scene__counts'):
        print(('  OK  ' if tag in h1 else '  !!  ') + tag)
