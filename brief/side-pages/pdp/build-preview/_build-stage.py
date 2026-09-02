# -*- coding: utf-8 -*-
"""Renders the REAL sections/elmsnest-v2-pdp-stage.liquid (markup + its {% stylesheet %} + its
{% javascript %}) through python-liquid, with the local image pack and local fonts, into
build-preview/stage.html — the offline proof for §4.1. Nothing here ships.

    python3 brief/side-pages/pdp/build-preview/_build-stage.py [A|B|C]
    node brief/shot.js brief/side-pages/pdp/build-preview/stage.html brief/side-pages/pdp/build-preview/stage
"""
import json, os, re, sys
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SECT = os.path.join(REPO, 'theme', 'sections')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/pdp/products.json'), encoding='utf-8'))
IMG = '../../../assets/img/'


def money(v):
    try:
        n = float(v)
    except Exception:
        return ''
    return '{:,.2f}'.format(n / 100.0)


class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path)
        o.src = path
        o.alt = ''
        o.width = 1200
        o.height = 1200
        o.position = i + 1
        return o


def build(handle):
    p = DATA[handle]
    n = min(4, len(p['images']))
    imgs = [Img(IMG + handle + '-' + str(i) + '.jpg', i) for i in range(n)]
    variants = [{'id': v['id'], 'title': v['title'], 'options': v['options'],
                 'price': int(round(v['price'] * 100)), 'available': v['available'],
                 'image': None} for v in p['variants']]
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'price_min': int(round(p['price_min'] * 100)), 'price_max': int(round(p['price_max'] * 100)),
            'price_varies': p['price_min'] != p['price_max'], 'available': True,
            'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0], 'selected_or_first_available_variant': variants[0],
            'metafields': {'custom': {}}}


def image_tag(v, **kw):
    src = str(v)
    attrs = ['src="%s"' % src]
    if kw.get('widths'):
        attrs.append('srcset="%s"' % ', '.join('%s %sw' % (src, w.strip()) for w in str(kw['widths']).split(',')))
    for k in ('sizes', 'alt', 'loading'):
        if kw.get(k) is not None:
            attrs.append('%s="%s"' % (k, kw[k]))
    if kw.get('fetchpriority'):
        attrs.append('fetchpriority="%s"' % kw['fetchpriority'])
    if kw.get('class'):
        attrs.append('class="%s"' % kw['class'])
    attrs.append('width="1200" height="1200"')
    return '<img ' + ' '.join(attrs) + '>'


env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['image_tag'] = image_tag
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)

SRC = open(os.path.join(SECT, 'elmsnest-v2-pdp-stage.liquid'), encoding='utf-8').read()
css = re.search(r'\{%\s*stylesheet\s*%\}(.*?)\{%\s*endstylesheet\s*%\}', SRC, re.S).group(1)
js = re.search(r'\{%\s*javascript\s*%\}(.*?)\{%\s*endjavascript\s*%\}', SRC, re.S).group(1)
schema = json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}', SRC, re.S).group(1))
markup = re.split(r'\{%\s*stylesheet\s*%\}', SRC)[0]

defaults = {s['id']: (s['default'] if s.get('default') is not None else '') for s in schema['settings'] if s.get('id')}
preset = schema['presets'][0].get('settings', {})
settings = dict(defaults)
settings.update(preset)

WHICH = (sys.argv[1] if len(sys.argv) > 1 else 'A').upper()
HANDLE = {'A': 'solar-crystal-ball-string-lights',
          'B': 'stainless-steel-solar-path-light-ip65',
          'C': 'waterproof-led-wall-light-ip65-6w-12w'}[WHICH]
PRODUCT = build(HANDLE)

# the per-product section config the template will ship (§4.1 copy for A; B and C get their own)
PER = {
    'A': {'heading_line1': 'הערב מתחיל', 'heading_line2': 'מהכדור הראשון.', 'stage_device': 'string'},
    'B': {'heading_line1': 'הדרך הביתה', 'heading_line2': 'נדלקת לבד.', 'stage_device': 'path'},
    'C': {'heading_line1': 'קיר אחד.', 'heading_line2': 'שתי אלומות.', 'stage_device': 'halo',
          'device_x': '46%', 'device_y': '40%'},
}[WHICH]
settings.update(PER)

section = {'id': 'pdp_stage', 'settings': settings, 'blocks': [], 'index': 0}
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/', 'cart_url': '/cart'},
           'settings': {'whatsapp_number': ''},
           'request': {'design_mode': False},
           'section': section,
           'product': PRODUCT}

body = env.from_string(markup).render(**GLOBALS)

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s · ElmsNest — stage %(which)s</title>
<script>document.documentElement.classList.add('env2-js')</script>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(css)s</style>
<style>
body{margin:0}
.mock-hdr{position:absolute;inset-block-start:0;inset-inline:0;height:70px;z-index:40;display:flex;align-items:center;
  justify-content:center;font-family:var(--env2-sans);font-size:13px;color:var(--env2-ink);gap:26px}
.mock-hdr img{width:40px;height:40px;object-fit:contain}
.mock-after{min-height:820px;padding-block:110px 90px;color:var(--env2-ink-2);font-family:var(--env2-sans);font-size:15px}
.mock-after h2{font-family:var(--env2-serif);font-weight:700;font-size:clamp(34px,4.9vw,72px);line-height:.98;margin:0 0 14px;color:var(--env2-ink)}
.mock-foot{background:#020306;padding-block:80px;color:var(--env2-mute);font-family:var(--env2-sans);font-size:13px;text-align:center}
</style></head>
<body class="hdt-page-type-product template-product">
<div id="MainContent" class="hdt-main-content">
<header class="mock-hdr"><span>דף הבית</span><span>קולקציות</span><img src="../../../assets/img/logo.png" alt=""><span>מי אנחנו</span><span>יצירת קשר</span></header>
<div class="shopify-section">%(body)s</div>
<section class="env2-section" id="env2-pdp-fit" dir="rtl" style="scroll-margin-top:90px"><div class="env2-wrap mock-after"><h2>«זה יתאים למרפסת שלי?»</h2><p>— כאן נמצא הסקשן הבא (4.2). הוא קיים בעמוד הזה רק כדי שהקישור והסרגל הדביק יתנהגו כמו בעמוד האמיתי.</p></div></section>
<section class="env2-section" id="env2-pdp-ledger" dir="rtl" style="scroll-margin-top:90px"><div class="env2-wrap mock-after"><h2>הליגר (4.4)</h2><p>— כל השורות, כל המחירים, טופס לכל שורה. הסרגל הדביק חייב להיעלם כשהחלק הזה על המסך.</p></div></section>
<section class="env2-section" id="env2-pdp-terms" dir="rtl" style="scroll-margin-top:90px"><div class="env2-wrap mock-after"><h2>ארבעה מספרים, לפני שמשלמים.</h2></div></section>
<div class="mock-foot">ElmsNest — פוטר</div>
</div>
<script>%(corejs)s</script>
<script>%(js)s</script>
</body></html>""" % {'title': PRODUCT['title'], 'which': WHICH, 'core': core_css, 'css': css,
                     'body': body, 'corejs': core_js, 'js': js}

out = os.path.join(HERE, 'stage.html' if WHICH == 'A' else 'stage-%s.html' % WHICH.lower())
open(out, 'w', encoding='utf-8').write(doc)
print('wrote', out, len(doc), 'bytes')
