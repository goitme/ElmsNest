# -*- coding: utf-8 -*-
"""Renders the COLLECTION plumbing snippets with the REAL Liquid (python-liquid), the local image pack
and the local fonts, into build-preview/_plumbing.html — the offline proof for
elmsnest-v2-{ground-collection,coll-axis,coll-rail,coll-glyph,coll-paginate} and for the additive edits
to elmsnest-v2-pdp-{card,image}. Nothing here ships; it is the harness the plumbing is proved on.

    python3 brief/side-pages/collection/build-preview/_build-plumbing.py
    node brief/shot.js brief/side-pages/collection/build-preview/_plumbing.html \
         brief/side-pages/collection/build-preview/_plumbing
"""
import json, os, re, html, sys
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/collection/data.json'), encoding='utf-8'))
IMG  = '../../../assets/img/'

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def build(handle):
    """A product drop built from data.json. firstAxis holds the real prices per first-option value, so
    the variants below carry the REAL price at the REAL option value — which is all the axis parser reads."""
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

env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = money
env.filters['money'] = lambda v: money(v) + ' ₪'
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}
def render(src, **kw): return env.from_string(src).render(**dict(GLOBALS, **kw))
def e(x): return html.escape(str(x))

FS, RS = '~~F~~', '~~R~~'
META = ['rec','handle','axis','unit','unit_label','unit_word','per_unit_label','stops','numbered',
        'measured','is_area','min','max','max_price','price_min','price_max','price_varies',
        'variants','values','available','default_variant_id','end']
STOP = ['rec','i','value','number','unit','unit_label','area_h','number2','unit2','unit2_label',
        'price','price_cents','price_max','per_unit','per_unit_label','available','variant_id',
        'variant_count','end']
AXIS = "{%- render 'elmsnest-v2-coll-axis', product: product -%}"
def axis(p):
    recs = render(AXIS, product=p).split(RS)
    return dict(zip(META, recs[0].split(FS))), [dict(zip(STOP, r.split(FS))) for r in recs[1:]]

# ---------------------------------------------------------------- 1. the axis table, all 27 products
COLL_ORDER = ['גרילנדות-ותאורה-דקורטיבית', 'תאורת-שביל-סולארית', 'solar-wall-lights', 'ספוטים-ופרוז-קטורים-סולאריים']
rows, counted = [], 0
for ch in COLL_ORDER:
    c = DATA['collections'][ch]
    rows.append('<tr class="plumb-grp"><th colspan="12">%s · <bdi>%s</bdi> · %d מוצרים</th></tr>'
                % (e(c['title']), e(ch), c['count']))
    for h in c['handles']:
        p = build(h); m, st = axis(p); counted += 1
        rows.append('<tr class="plumb-meta"><td class="plumb-h" colspan="2"><bdi>%s</bdi> · %s</td>'
                    '<td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>'
                    '<td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                    % (e(h), e(m['axis']), e(m['unit'] or '—'), e(m['unit_label'] or '—'),
                       e(m['unit_word'] or '—'),
                       'measured' if m['measured'] == '1' else '<span class="plumb-no">not measured</span>',
                       'area' if m['is_area'] == '1' else '—', e(m['min'] or '—'), e(m['max'] or '—'),
                       e(m['max_price'] or '—'), '<bdi>' + e(m['price_min'] + '–' + m['price_max']) + '</bdi>'))
        for s in st:
            rows.append('<tr><td class="plumb-i">%s</td><td class="plumb-v"><bdi>%s</bdi></td>'
                        '<td class="plumb-n">%s</td><td>%s</td><td>%s</td><td>%s</td><td class="plumb-n">%s</td>'
                        '<td>%s</td><td class="plumb-p">%s ₪</td><td class="plumb-p">%s</td>'
                        '<td>%s</td><td class="plumb-n">%s</td></tr>'
                        % (e(s['i']), e(s['value']), e(s['number'] or '—'), e(s['unit'] or '—'),
                           e(s['unit_label'] or '—'), e(s['area_h'] or '—'),
                           e(s['number2'] or '—'), e(s['unit2_label'] or '—'),
                           e(s['price']), ('<bdi>≈' + s['per_unit'] + '</bdi>') if s['per_unit'] else '—',
                           e(s['per_unit_label'] or '—'), e(s['variant_count'])))
axis_table = ('<table class="plumb-t plumb-axis"><thead><tr>'
              '<th>#</th><th>ערך האופציה / handle</th><th>number</th><th>unit</th><th>unit_label</th>'
              '<th>area_h</th><th>number2</th><th>unit2</th><th>price</th><th>per_unit</th>'
              '<th>per_unit_label</th><th>variants</th></tr></thead><tbody>'
              + '\n'.join(rows) + '</tbody></table>')

# the union of the decor and path rails, built exactly as §3.4 tells the ruler section to build it
def union(collection_handle, unit):
    seen, out = set(), []
    for h in DATA['collections'][collection_handle]['handles']:
        m, st = axis(build(h))
        if m['measured'] != '1' or m['unit'] != unit: continue
        for s in st:
            if s['number'] and s['unit'] == unit and s['number'] not in seen:
                seen.add(s['number']); out.append(float(s['number']))
    return sorted(out)
u_decor = union('גרילנדות-ותאורה-דקורטיבית', 'm')
u_path  = union('תאורת-שביל-סולארית', 'qty')
def fmt(xs): return ' · '.join(('%g' % x) for x in xs)

# ---------------------------------------------------------------- 2. the rail, live, with the radios
STOPS = '3,6,10,15,22,30'
rail_css_static = render("{% render 'elmsnest-v2-coll-rail', css: true %}")
rail_css_stops  = render("{% render 'elmsnest-v2-coll-rail', emit: 'css', stops: st, rail_max: 32, scope: '.plumb-ruler' %}", st=STOPS)
RAIL = ("{%- render 'elmsnest-v2-coll-rail', product: product, stops: st, unit: 'm', rail_max: 32, "
        "off_note: onote -%}")
SHORT = "{%- render 'elmsnest-v2-coll-rail', product: product, stops: st, unit: 'm', emit: 'short' -%}"
radios = ''.join('<input type="radio" name="env2-stop" id="env2-stop-%s" class="plumb-sr"%s>'
                 % (k, ' checked' if k == 'all' else '') for k in ['all'] + STOPS.split(','))
pills = ''.join('<label class="plumb-pill" for="env2-stop-%s">%s</label>'
                % (k, 'הכול' if k == 'all' else k + ' מ׳') for k in ['all'] + STOPS.split(','))
rail_rows = []
for h in DATA['collections']['גרילנדות-ותאורה-דקורטיבית']['handles']:
    p = build(h)
    note = 'נמדדת לפי שטח, לא לפי אורך' if h == 'decorative-led-net-lights' else 'לא נמדדת במטרים'
    short = render(SHORT, product=p, st=STOPS).strip()
    rail_rows.append('<div class="plumb-row"%s><div class="plumb-row__t"><bdi>%s</bdi><span>%s</span></div>%s</div>'
                     % ((' data-short="%s"' % e(short)) if short else '', e(p['title']),
                        e(axis(p)[0]['axis']), render(RAIL, product=p, st=STOPS, onote=note)))
rail_block = ('<div class="plumb-stops">%s<div class="plumb-pills">%s</div>'
              '<div class="plumb-ruler"><div class="plumb-master"><span class="env2-coll-rail__line"></span>'
              '<span class="env2-coll-rail__cursor"></span></div>%s</div></div>'
              % (radios, pills, '\n'.join(rail_rows)))

# ---------------------------------------------------------------- 3. the glyph plate
glyph_sprite = render("{% render 'elmsnest-v2-coll-glyph', sprite: true %}")
glyphs = ''.join('<div class="plumb-gl"><div class="plumb-gl__box">%s</div><p class="plumb-note">%s</p></div>'
                 % (render("{% render 'elmsnest-v2-coll-glyph', glyph: g, aspect: '1/1.15' %}", g=g), g)
                 for g in ('bollard', 'cube', 'string', 'net', 'spot'))
NOCLEAN = "{%- render 'elmsnest-v2-pdp-image', product: product, emit: 'no_clean' -%}"
nc_rows = []
for ch in COLL_ORDER:
    for h in DATA['collections'][ch]['handles']:
        p = build(h)
        nc = render(NOCLEAN, product=p).strip()
        idx = render("{%- render 'elmsnest-v2-pdp-image', product: product, slot: 'card' -%}", product=p).strip()
        gl = render("{%- render 'elmsnest-v2-pdp-image', product: product, slot: 'card', glyph: true -%}", product=p).strip()
        nc_rows.append('<tr class="%s"><td><bdi>%s</bdi></td><td>%s</td><td>%s</td><td><b>%s</b></td></tr>'
                       % ('plumb-nc' if nc == '1' else '', e(h),
                          'אין תצלום נקי' if nc == '1' else 'יש', e(idx), e(gl)))
nc_table = ('<table class="plumb-t plumb-rows"><thead><tr><th>handle</th><th>emit:no_clean</th>'
            '<th>slot card → index</th><th>glyph:true →</th></tr></thead><tbody>'
            + '\n'.join(nc_rows) + '</tbody></table>')

# ---------------------------------------------------------------- 4. the card in its new modes
card_css = render("{% render 'elmsnest-v2-pdp-card', css: true %}")
A, B, C = build('solar-crystal-ball-string-lights'), build('warm-solar-step-deck-lights'), build('led-globe-string-lights')
mA, sA = axis(A); mB, sB = axis(B)
cap_a = ' · '.join(s['value'] for s in sA[:2])
cap_b = ' · '.join(s['value'] for s in sB[:2])
CARD = ("{% render 'elmsnest-v2-pdp-card', product: product, width: w, aspect: ar, action_label: al, "
        "axis_caption: cap, unit_price_line: up, variant: v, glyph: g %}")
cards_plain = (render(CARD, product=A, w=300, ar='1/1.05', al='לבחירת אורך', cap='', up='', v='', g='') +
               render(CARD, product=A, w=300, ar='1/1.05', al='לבחירת אורך', cap=cap_a,
                      up='<bdi>≈' + sA[0]['per_unit'] + '</bdi> ' + sA[0]['per_unit_label'], v='', g='') +
               render(CARD, product=B, w=210, ar='1/1.4', al='לבחירת כמות', cap=cap_b,
                      up='<bdi>≈' + sB[0]['per_unit'] + '</bdi> ' + sB[0]['per_unit_label'], v='', g='auto') +
               render(CARD, product=C, w=260, ar='1/.9', al='לבחירת אורך', cap='', up='', v='', g='auto'))
card_scene = render(CARD, product=A, w=420, ar='1/1.05', al='לבחירת אורך', cap=cap_a,
                    up='<bdi>≈' + sA[0]['per_unit'] + '</bdi> ' + sA[0]['per_unit_label'], v='scene', g='')

# ---------------------------------------------------------------- 5. pagination
pag_css = render("{% render 'elmsnest-v2-coll-paginate', css: true %}")
def part(t, url=None): return {'title': t, 'url': url, 'is_link': url is not None}
PAG = {'pages': 3, 'current_page': 2, 'items': 27,
       'previous': part('&laquo;', '/collections/all?page=1'),
       'next': part('&raquo;', '/collections/all?page=3'),
       'parts': [part(1, '/collections/all?page=1'), part(2), part(3, '/collections/all?page=3')]}
PAG1 = {'pages': 1, 'current_page': 1, 'items': 27, 'previous': part('&laquo;'), 'next': part('&raquo;'), 'parts': []}
COL = {'all_products_count': 27, 'sort_by': 'price-ascending', 'products_count': 27}
pag_on  = render("{% render 'elmsnest-v2-coll-paginate', paginate: paginate, collection: collection %}", paginate=PAG, collection=COL)
pag_off = render("{% render 'elmsnest-v2-coll-paginate', paginate: paginate, collection: collection %}", paginate=PAG1, collection=COL)
pag_note = render("{% render 'elmsnest-v2-coll-paginate', collection: collection, emit: 'note' %}", collection=COL)

# ---------------------------------------------------------------- 6. the JSON emit
json_tag = render("{%- render 'elmsnest-v2-coll-axis', product: product, emit: 'json' -%}", product=A)
json_body = re.search(r'<script[^>]*>(.*?)</script>', json_tag, re.S).group(1).strip()
try:
    json.loads(json_body); json_ok = 'JSON.parse OK'
except Exception as ex:
    json_ok = 'JSON INVALID: ' + str(ex); print('!! ' + json_ok); sys.exit(2)

# ---------------------------------------------------------------- the page
core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-collection">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-collection.liquid'), encoding='utf-8').read(), re.S).group(1)

doc = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ElmsNest collection — plumbing proof</title>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
%(cardcss)s
%(railcss)s
%(railstops)s
%(pagcss)s
<style>
body{margin:0;font-family:var(--env2-sans);color:var(--env2-ink)}
.plumb{width:min(1240px,100%% - 2*var(--env2-gut));margin-inline:auto;padding-block:56px 120px}
.plumb-h1{font-family:var(--env2-serif);font-weight:700;font-size:clamp(34px,4.4vw,62px);line-height:.98;margin:0 0 10px}
.plumb-h2{font-family:var(--env2-serif);font-weight:700;font-size:clamp(24px,2.6vw,36px);line-height:1;margin:64px 0 6px;color:var(--env2-glow)}
.plumb-note{font-size:13px;color:var(--env2-ink-2);margin:0 0 12px;max-width:78ch}
.plumb-t{border-collapse:collapse;font-size:13px;margin-block-end:14px;width:100%%}
.plumb-t th,.plumb-t td{border-top:1px solid var(--env2-hair);padding:5px 10px;text-align:start;vertical-align:top}
.plumb-t thead th{color:var(--env2-gold);font-size:11.5px;letter-spacing:.12em;font-weight:500;white-space:nowrap}
.plumb-grp th{color:var(--env2-glow);font-family:var(--env2-serif);font-size:19px;padding-block:18px 6px;border-top:1px solid rgba(255,211,148,.35)}
.plumb-meta td{color:var(--env2-ink-2);background:rgba(255,211,148,.045)}
.plumb-meta .plumb-h{color:var(--env2-ink);font-weight:500}
.plumb-n,.plumb-p,.plumb-i{font-variant-numeric:tabular-nums;white-space:nowrap}
.plumb-p{color:var(--env2-glow)}
.plumb-v{color:var(--env2-ink)}
.plumb-no{color:var(--env2-ember)}
.plumb-nc td{background:rgba(247,162,74,.07)}
.plumb-scroll{overflow-x:auto;overscroll-behavior-inline:contain}
.plumb-cards{display:flex;align-items:flex-end;gap:clamp(20px,3.4vw,56px);flex-wrap:wrap;margin-block:18px 8px}
.plumb-scene{position:relative;padding:34px;margin-block:18px;background:linear-gradient(180deg,#0a1424,#050a14);display:flex;justify-content:flex-end}
.plumb-gl{inline-size:180px}
.plumb-gls{display:flex;gap:24px;flex-wrap:wrap;margin-block:18px}
.plumb-sr{position:absolute;inline-size:1px;block-size:1px;opacity:0;pointer-events:none}
.plumb-stops{position:relative;margin-block:18px}
.plumb-pills{display:flex;gap:8px;flex-wrap:wrap;margin-block-end:26px}
.plumb-pill{display:inline-flex;align-items:center;justify-content:center;min-block-size:48px;padding-inline:20px;
  border:1px solid rgba(244,238,227,.25);border-radius:999px;font-size:15px;cursor:pointer;color:var(--env2-ink-2)}
.plumb-master{position:relative;block-size:22px;margin-block-end:26px}
.plumb-row{display:grid;grid-template-columns:minmax(0,240px) minmax(0,1fr);gap:20px;align-items:start;
  padding-block:16px;border-top:1px solid var(--env2-hair);transition:opacity .28s}
.plumb-row__t{font-size:15px;color:var(--env2-ink)}
.plumb-row__t span{display:block;font-size:13px;color:var(--env2-mute);margin-block-start:4px}
.plumb-pre{font-family:ui-monospace,Menlo,monospace;font-size:12px;line-height:1.5;color:var(--env2-ink-2);
  background:rgba(255,255,255,.03);padding:14px;overflow-x:auto;white-space:pre-wrap;word-break:break-all;direction:ltr;text-align:left}
.plumb-ok{color:var(--env2-glow);font-size:13px}
@media (max-width:900px){
  .plumb-row{grid-template-columns:minmax(0,1fr)}
  .plumb-t{font-size:12px}
  .plumb-t th,.plumb-t td{padding:4px 6px}
}
</style></head>
<body class="hdt-page-type-collection template-collection">
%(sprite)s
<main class="env2-section plumb" dir="rtl">
  <h1 class="plumb-h1">שרברבות הקולקציה — הוכחה אופליין</h1>
  <p class="plumb-note">Rendered from theme/snippets/elmsnest-v2-{ground-collection,coll-axis,coll-rail,coll-glyph,coll-paginate}.liquid
  and elmsnest-v2-{pdp-card,pdp-image,core,price,buy}.liquid by python-liquid, with the local image pack.
  Every number below came out of the Liquid; none is typed. The body carries hdt-page-type-collection, so the
  §3.1 ground is the real one.</p>

  <h2 class="plumb-h2">1 · elmsnest-v2-coll-axis — the parse, all %(n)d products</h2>
  <p class="plumb-note">§3.4 / §6.19. The first option axis of every product in the catalogue, as the snippet reads it.
  A gold row is the axis meta (unit · unit_label · unit_word · measured · is_area · min · max · price at max · price span · stops);
  the plain rows under it are its stop records. "measured = לא" means the product is NOT on a rail in its own unit —
  a colour/model axis, an axis with no number, or an area — and §3.4 lifts it into its own band with a real card.</p>
  <p class="plumb-note">The rail unions these numbers exactly as §3.4 tells the ruler section to:
  decor (m) → <b>%(udecor)s</b> · path (qty) → <b>%(upath)s</b>. Both match §3.4 to the digit.</p>
  <div class="plumb-scroll">%(axis)s</div>

  <h2 class="plumb-h2">2 · elmsnest-v2-coll-rail — the three stop states, live, with no JavaScript</h2>
  <p class="plumb-note">§4.2 · graft C1. The pills below are &lt;label&gt;s over radio inputs and the whole mechanism is
  <b>#env2-stop-N:checked ~ …</b> CSS generated by the snippet itself (emit:'css'). There is no script on this page.
  Tap <b>10 מ׳</b>: rope answers 12 מ׳ / 99.90 ₪, crystal 11 מ׳ / 109.90 ₪, globe 10 מ׳ / 169.90 ₪, and Edison
  <b>dims to .4 and prints האורך המרבי: 8 מ׳</b> — it is never hidden (§6.6). Tap <b>3 מ׳</b> and rope/crystal/Edison
  go to <b>below</b>: their smallest offering overshoots the stop, and they say which one it is.
  The net and the birch and the fireflies are <b>off</b> — no dots, no span, only the honest note.</p>
  %(rail)s

  <h2 class="plumb-h2">3 · elmsnest-v2-coll-glyph — the plate for the fifteen</h2>
  <p class="plumb-note">§3.6.3 · graft C3. Five shape families, one &lt;symbol&gt; sprite, ground #080d18, stroke
  rgba(244,238,227,.45), a warm --env2-ember halo at 22 %% where the light source is, and the caption
  <b>איור · אין תצלום נקי</b>. Radius 0. No cream, no beige, no "coming soon".</p>
  <div class="plumb-gls">%(glyphs)s</div>
  <p class="plumb-note">And the ledger behind it: elmsnest-v2-pdp-image now answers <b>emit:'no_clean'</b> and
  <b>glyph:true</b>. The index column proves the ADDITIVE promise — the slot resolver still returns exactly the index
  it returned before, for every one of the 27 products.</p>
  <div class="plumb-scroll">%(nc)s</div>

  <h2 class="plumb-h2">4 · elmsnest-v2-pdp-card — the same card, four modes</h2>
  <p class="plumb-note">§3.5. Left to right: today's card (nothing passed, byte-identical to the PDP's);
  the same card with <b>axis_caption</b> and <b>unit_price_line</b>; a card whose product has no clean photograph at
  any index, with <b>glyph:'auto'</b>; and another. Staggered 300 / 210 / 260 px at 1/1.05 · 1/1.4 · 1/.9 — never equal cells.</p>
  <div class="plumb-cards">%(cards)s</div>
  <p class="plumb-note"><b>variant:'scene'</b> — the scrim card that rides a photograph, the only card surface on the page (§3.1), used exactly twice.</p>
  <div class="plumb-scene">%(scene)s</div>

  <h2 class="plumb-h2">5 · elmsnest-v2-coll-paginate</h2>
  <p class="plumb-note">§3.7. First: a simulated 3-page catalogue with ?sort_by=price-ascending carried onto every link.
  Second: the real case — paginate.pages = 1, and the snippet prints <b>absolutely nothing</b> (the empty rule below).
  Third: the emit:'note' line §4.5's foot prints.</p>
  %(pagon)s
  <p class="plumb-note">pages = 1 → [%(pagoff)s] ← nothing between the brackets.</p>
  %(pagnote)s

  <h2 class="plumb-h2">6 · elmsnest-v2-coll-axis, emit:'json'</h2>
  <p class="plumb-note">One &lt;script type="application/json"&gt; per product for the eleven-line ruler enhancement. %(jsonok)s.</p>
  <div class="plumb-pre">%(json)s</div>
</main>
</body></html>""" % {
  'core': core_css, 'ground': ground, 'cardcss': card_css, 'railcss': rail_css_static,
  'railstops': rail_css_stops, 'pagcss': pag_css, 'sprite': glyph_sprite,
  'n': counted, 'axis': axis_table, 'udecor': fmt(u_decor), 'upath': fmt(u_path),
  'rail': rail_block, 'glyphs': glyphs, 'nc': nc_table,
  'cards': cards_plain, 'scene': card_scene,
  'pagon': pag_on, 'pagoff': pag_off.strip(), 'pagnote': pag_note,
  'json': e(json_body), 'jsonok': json_ok }

open(os.path.join(HERE, '_plumbing.html'), 'w', encoding='utf-8').write(doc)
print('wrote', os.path.join(HERE, '_plumbing.html'), len(doc), 'bytes ·', counted, 'products ·', json_ok)
print('decor union:', fmt(u_decor))
print('path  union:', fmt(u_path))
