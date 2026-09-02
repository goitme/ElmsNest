# -*- coding: utf-8 -*-
"""Renders the PDP plumbing snippets with the REAL Liquid (python-liquid), local images and local fonts,
into build-preview/_plumbing.html — the offline proof for elmsnest-v2-pdp-{image,variants,card,buybar,
photo-cta} and elmsnest-v2-ground-product. Nothing here ships; it is the harness the plumbing is proved on.
    python3 brief/side-pages/pdp/build-preview/_build-plumbing.py
    node brief/shot.js brief/side-pages/pdp/build-preview/_plumbing.html brief/side-pages/pdp/build-preview/_plumbing
"""
import json, os, re, html
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/pdp/products.json'), encoding='utf-8'))
IMG  = '../../../assets/img/'

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    """stands in for a Shopify image drop: str(image) and image | image_url both give the local path"""
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle):
    p = DATA[handle]
    n = min(4, len(p['images']))                       # the local pack carries 0..3
    imgs = [Img(IMG + handle + '-' + str(i) + '.jpg', i) for i in range(n)]
    variants = [{'id': v['id'], 'title': v['title'], 'options': v['options'],
                 'price': int(round(v['price'] * 100)), 'available': v['available'],
                 'image': None} for v in p['variants']]
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    return {'handle': handle, 'title': p['title'], 'type': p['type'], 'url': '/products/' + handle,
            'price_min': int(round(p['price_min'] * 100)), 'price_max': int(round(p['price_max'] * 100)),
            'price_varies': p['price_min'] != p['price_max'], 'available': True,
            'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0], 'selected_or_first_available_variant': variants[0]}

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)

GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}
def render(src, **kw):
    return env.from_string(src).render(**dict(GLOBALS, **kw))

A, B, C = (build('solar-crystal-ball-string-lights'),
           build('stainless-steel-solar-path-light-ip65'),
           build('waterproof-led-wall-light-ip65-6w-12w'))

# ---------- the shared core CSS + the PDP ground, taken from the real snippets ----------
core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-product">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-product.liquid'), encoding='utf-8').read(), re.S).group(1)
card_css = render("{% render 'elmsnest-v2-pdp-card', css: true %}")

# ---------- the ledger model, per archetype ----------
MODEL = "{%- capture m -%}{%- render 'elmsnest-v2-pdp-variants', product: product, axis: axis -%}{%- endcapture -%}{{ m }}"
def model(p, axis=''):
    recs = render(MODEL, product=p, axis=axis).split('~~R~~')
    return [r.split('~~F~~') for r in recs]

META_NAMES = ['rec','mode','axis','axis2','axis_name','axis2_name','quiet_axis','quiet_name','quiet_values',
              'rows','default_row','default_variant_id','price_min','price_max','price_varies','unit',
              'count_unit','per_unit_label','axis_values','end']
ROW_NAMES  = ['rec','i','key','key_a','key_b','label','n1','u1','n2','u2','price','price_cents','per_unit',
              'per_unit_label','available','variant_id','variant_count','quiet','image','end']

def e(x): return html.escape(str(x))

def ledger_html(p, title):
    recs = model(p)
    meta = recs[0]
    out = ['<div class="plumb-block"><h3 class="plumb-h3">%s</h3>' % e(title)]
    out.append('<p class="plumb-note">%s · %s variants · %s rows</p>' % (e(p['handle']), len(p['variants']), meta[9]))
    out.append('<table class="plumb-t"><tbody>')
    for k, v in zip(META_NAMES, meta):
        if k in ('rec', 'end'): continue
        out.append('<tr><th>meta.%s</th><td>%s</td></tr>' % (e(k), e(v) if v else '<i>—</i>'))
    out.append('</tbody></table>')
    out.append('<table class="plumb-t plumb-rows"><thead><tr>' +
               ''.join('<th>%s</th>' % e(h) for h in ['i','key_a','key_b','n1','u1','n2','u2','price','per_unit','per_unit_label','avail','variant_id','#','quiet']) +
               '</tr></thead><tbody>')
    for r in recs[1:]:
        d = dict(zip(ROW_NAMES, r))
        q = d['quiet'].split(';')
        out.append('<tr>' + ''.join('<td>%s</td>' % (e(x) if x else '<i>—</i>') for x in
                   [d['i'], d['key_a'], d['key_b'], d['n1'], d['u1'], d['n2'], d['u2'],
                    d['price'] + ' ₪', d['per_unit'], d['per_unit_label'], d['available'],
                    d['variant_id'], d['variant_count'], ' · '.join(x.split('^')[1] or '—' for x in q)]) + '</tr>')
    out.append('</tbody></table></div>')
    return '\n'.join(out)

# ---------- the pieces ----------
CARD = "{% render 'elmsnest-v2-pdp-card', product: product, width: w, aspect: ar, action_label: al %}"
cards = (render(CARD, product=A, w=300, ar='1/1.05', al='לבחירת אורך') +
         render(CARD, product=B, w=210, ar='1/1.4',  al='לבחירת דגם') +
         render(CARD, product=C, w=260, ar='1/.9',   al='לבחירת גוון'))
bar_a = render("{% render 'elmsnest-v2-pdp-buybar', product: product %}", product=A)
bar_c = render("{% render 'elmsnest-v2-pdp-buybar', product: product, mirror: 'לבן · 6W · אור חם 3000K' %}", product=C)
bar_static = re.sub(r'<style id="env2-pdp-bar-css">.*?</style>', '', bar_a, flags=re.S)
bar_static_c = re.sub(r'<style id="env2-pdp-bar-css">.*?</style>', '', bar_c, flags=re.S)
cta = (render("{% render 'elmsnest-v2-pdp-photo-cta', product: product %}", product=A) +
       render("{% render 'elmsnest-v2-pdp-photo-cta', product: product, style: 'ghost' %}", product=A))
cta_wa = env.from_string("{% render 'elmsnest-v2-pdp-photo-cta', product: product, style: 'link' %}").render(
    routes=GLOBALS['routes'], settings={'whatsapp_number': '+972 54-000-0000'}, product=A)

# ---------- the image resolver table ----------
RES = "{%- render 'elmsnest-v2-pdp-image', product: product, slot: slot, index: idx -%}"
res_rows = []
for p, ban in ((A, '1, 3'), (B, '2'), (C, '0')):
    for slot in ('hero', 'context', 'close', 'card', 'wall-pair', 'big', 'small', 'thumb'):
        i = render(RES, product=p, slot=slot, idx='').strip()
        res_rows.append((p['handle'], ban, slot, '—', i))
    for want in (1, 2, 3, 4):
        i = render(RES, product=p, slot='hero', idx=want).strip()
        res_rows.append((p['handle'], ban, 'hero', want, i))
for h in ('decorative-led-net-lights', 'dual-head-garden-light-10w-ip65', 'solar-edison-string-lights'):
    p = build(h)
    ban = {'decorative-led-net-lights': '0', 'dual-head-garden-light-10w-ip65': '1, 2, 3', 'solar-edison-string-lights': 'none'}[h]
    for slot in ('card', 'close'):
        res_rows.append((h, ban, slot, '—', render(RES, product=p, slot=slot, idx='').strip()))

res_html = ('<table class="plumb-t plumb-rows"><thead><tr><th>handle</th><th>banned</th><th>slot</th>'
            '<th>index setting</th><th>→ images[i]</th></tr></thead><tbody>' +
            ''.join('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><b>%s</b></td></tr>' % tuple(e(x) for x in r) for r in res_rows) +
            '</tbody></table>')

doc = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest PDP — plumbing proof</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
%(cardcss)s
<style>
body{margin:0;font-family:var(--env2-sans);color:var(--env2-ink)}
.plumb{width:min(1240px,100%% - 2*var(--env2-gut));margin-inline:auto;padding-block:56px 120px}
.plumb-h1{font-family:var(--env2-serif);font-weight:700;font-size:clamp(34px,4.4vw,62px);line-height:.98;margin:0 0 10px}
.plumb-h2{font-family:var(--env2-serif);font-weight:700;font-size:clamp(24px,2.6vw,36px);line-height:1;margin:64px 0 6px;color:var(--env2-glow)}
.plumb-h3{font-family:var(--env2-sans);font-weight:500;font-size:15px;letter-spacing:.06em;margin:26px 0 4px;color:var(--env2-gold)}
.plumb-note{font-size:13px;color:var(--env2-ink-2);margin:0 0 12px}
.plumb-t{border-collapse:collapse;font-size:13px;margin-block-end:14px;max-width:100%%}
.plumb-t th,.plumb-t td{border-top:1px solid var(--env2-hair);padding:6px 12px;text-align:start;vertical-align:top}
.plumb-t th{color:var(--env2-ink-2);font-weight:400;white-space:nowrap}
.plumb-rows{width:100%%}
.plumb-rows thead th{color:var(--env2-gold);font-size:11.5px;letter-spacing:.12em}
.plumb-scroll{overflow-x:auto}
.plumb-cards{display:flex;align-items:flex-end;gap:clamp(20px,3.4vw,56px);flex-wrap:wrap;margin-block:18px 8px}
.plumb-barbox{position:relative;margin-block:14px;border:1px dashed var(--env2-hair)}
.plumb-barbox .env2-pdp-bar{position:relative;display:block;transform:none}
.plumb-ctas{display:flex;align-items:center;gap:24px;flex-wrap:wrap;margin-block:14px}
</style></head>
<body class="hdt-page-type-product template-product">
<main class="env2-section plumb" dir="rtl">
  <h1 class="plumb-h1">שרברבות — הוכחה אופליין</h1>
  <p class="plumb-note">Rendered from theme/snippets/elmsnest-v2-pdp-{image,variants,card,buybar,photo-cta}.liquid and
  elmsnest-v2-{ground-product,core,price,buy}.liquid by python-liquid, with the local image pack. No hand-written markup below this line.</p>

  <h2 class="plumb-h2">1 · elmsnest-v2-pdp-card</h2>
  <p class="plumb-note">§4.8 · staggered 300 / 210 / 260 px at 1/1.05 · 1/1.4 · 1/.9 — never equal cells. Place kicker from the four approved pairs, title in Heebo, price by the elmsnest-v2-price rule, single variant → a real add-to-cart form (B), multi → a ghost link (A, C). No badge, no swatch, no star, no quick-add.</p>
  <div class="plumb-cards">%(cards)s</div>

  <h2 class="plumb-h2">2 · elmsnest-v2-pdp-buybar</h2>
  <p class="plumb-note">§4.9 · 46px thumb · title 14px · mirror 13px · price 22px · pill. Fixed and hidden above 900px; shown here in a static box so the desktop capture carries it too. The live fixed copy is at the bottom of this page on ≤900px.</p>
  <div class="plumb-barbox">%(bar)s</div>
  <div class="plumb-barbox">%(barc)s</div>

  <h2 class="plumb-h2">3 · elmsnest-v2-pdp-photo-cta</h2>
  <p class="plumb-note">settings.whatsapp_number empty → mailto, label "לשלוח תמונה של המקום", never "בוואטסאפ". Third one is the same snippet with a number filled.</p>
  <div class="plumb-ctas">%(cta)s</div>
  <div class="plumb-ctas">%(ctawa)s <span class="plumb-note">← the wa.me branch (number filled)</span></div>

  <h2 class="plumb-h2">4 · elmsnest-v2-pdp-image — the resolver</h2>
  <p class="plumb-note">§3.5 + §3.6 never-use ledger. The resolver never returns a banned index: the setting is honoured when it is clean and stepped forward when it is not.</p>
  <div class="plumb-scroll">%(res)s</div>

  <h2 class="plumb-h2">5 · elmsnest-v2-pdp-variants — the ledger model</h2>
  <p class="plumb-note">One pass over product.variants. A: one price axis (6 lengths × 4 colours, colour quiet). B: single variant → quantity ledger. C: TWO price axes (עוצמה × גוון אור) → 4 rows, body colour quiet.</p>
  <div class="plumb-scroll">%(ledgers)s</div>
</main>
%(fixedbar)s
</body></html>""" % {
  'core': core_css, 'ground': ground, 'cardcss': card_css, 'cards': cards,
  'bar': bar_static, 'barc': bar_static_c, 'cta': cta, 'ctawa': cta_wa, 'res': res_html,
  'ledgers': ledger_html(A, 'A — crystal balls · 24 variants') + ledger_html(B, 'B — path light · 1 variant') + ledger_html(C, 'C — wall light · 8 variants'),
  'fixedbar': bar_a }

open(os.path.join(HERE, '_plumbing.html'), 'w', encoding='utf-8').write(doc)
print('wrote', os.path.join(HERE, '_plumbing.html'), len(doc), 'bytes')
