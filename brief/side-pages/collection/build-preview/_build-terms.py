# -*- coding: utf-8 -*-
# Renders sections/elmsnest-v2-coll-terms.liquid - the REAL section file, through python-liquid,
# against data.json and the real snippets - onto the collection page ground.
#     python3 brief/side-pages/collection/build-preview/_build-terms.py
# Harness-only substitutions (both are Shopify tags python-liquid does not implement):
#   * {% stylesheet %} / {% javascript %} / {% schema %} lifted out and re-attached as <style> and
#     <script>, which is what Shopify does with them.
# It ASSERTS the four WINNING-SPEC 4.6 strings read back verbatim, that the deck's count is the
# collection's own on all five URLs, that the word for the other channel never appears, and that no
# typed catalogue number leaked in.
import json, os, re, sys, unicodedata
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SECT = os.path.join(REPO, 'theme', 'sections')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/collection/data.json'), encoding='utf-8'))

TITLES = {'גרילנדות-ותאורה-דקורטיבית': 'decor', 'תאורת-שביל-סולארית': 'path',
          'solar-wall-lights': 'wall', 'ספוטים-ופרוז-קטורים-סולאריים': 'spot'}


def collection(handle):
    if handle == 'all':
        n = 27
        return {'handle': 'all', 'title': 'קטלוג', 'url': '/collections/all',
                'products': [], 'products_count': n, 'all_products_count': 27, 'description': ''}
    c = DATA['collections'][handle]
    return {'handle': handle, 'title': c['title'], 'url': '/collections/' + handle,
            'products': [], 'products_count': len(c['handles']), 'all_products_count': 27,
            'description': ''}


env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['money_without_currency'] = lambda v: v
env.filters['money'] = lambda v: str(v)
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}

SRC = open(os.path.join(SECT, 'elmsnest-v2-coll-terms.liquid'), encoding='utf-8').read()


def lift(tag, s):
    m = re.search(r'\{%-?\s*' + tag + r'\s*-?%\}(.*?)\{%-?\s*end' + tag + r'\s*-?%\}', s, re.S)
    if not m: sys.exit('no ' + tag + ' block in the section')
    return m.group(1), s[:m.start()] + s[m.end():]


CSS, SRC = lift('stylesheet', SRC)
JS, SRC = lift('javascript', SRC)
SCHEMA_TXT, SRC = lift('schema', SRC)
SCHEMA = json.loads(SCHEMA_TXT)
MARKUP = SRC

DEFAULTS = {}
for s in SCHEMA.get('settings', []):
    if s.get('type') in ('header', 'paragraph'): continue
    DEFAULTS[s['id']] = s.get('default', '')
PRESET = SCHEMA['presets'][0]
DEFAULTS.update(PRESET.get('settings', {}))
BLOCK_DEF = {b['type']: {x['id']: x.get('default', '') for x in b['settings']} for b in SCHEMA['blocks']}
PRESET_BLOCKS = []
for i, b in enumerate(PRESET.get('blocks', [])):
    st = dict(BLOCK_DEF[b['type']]); st.update(b.get('settings', {}))
    PRESET_BLOCKS.append({'type': b['type'], 'settings': st, 'shopify_attributes': '', 'id': 'b%d' % i})

core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-collection">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-collection.liquid'), encoding='utf-8').read(), re.S).group(1)

PAGE = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<script>document.documentElement.classList.add('env2-js');</script>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(css)s</style>
<style>
/* the ground the real template gives this section: it is the SIXTH of seven sections, so the preview
   starts the 3.1 pixel gradient at the depth it has actually reached there (full night). */
body{margin:0;background-position-y:-4400px}
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
    st = dict(DEFAULTS); st.update(extra or {})
    sec = {'id': 'coll_terms', 'settings': st, 'blocks': blocks if blocks is not None else PRESET_BLOCKS}
    col = collection(handle) if handle else None
    return env.from_string(MARKUP).render(**dict(GLOBALS, section=sec, collection=col))


def page(out, handle, extra=None, blocks=None):
    markup = render(handle, extra, blocks)
    doc = PAGE % {'title': 'terms · ' + str(handle), 'core': core_css, 'ground': ground,
                  'css': CSS, 'markup': markup, 'corejs': core_js, 'js': JS}
    open(os.path.join(HERE, out), 'w', encoding='utf-8').write(doc)
    return markup


def text(m):
    # element boundaries are word boundaries: the markup is whitespace-trimmed by {%- -%}, so a
    # numeral <bdi> and the <small> unit sit flush in the source and apart on the screen.
    t = re.sub(r'>\s*<', '> <', m)
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&nbsp;', ' ').replace('&#39;', "'").replace('&amp;', '&').replace('&quot;', '"')
    return re.sub(r'\s+', ' ', t).strip()


WANT = [
    '0 ₪ משלוח לנקודת איסוף — חינם. עד הבית 29.90 ₪.',
    '8–17 ימי עסקים לאספקה: 1–3 ימי טיפול ו־7–14 ימי משלוח. ייתכן משלוח ממחסן מחוץ לישראל.',
    '14 יום לביטול מקבלת המוצר, לפי חוק הגנת הצרכן. דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם.',
    '1 תמונה שולחים תמונה של המקום ואנחנו בודקים התאמה לפני ההזמנה.',
]

if __name__ == '__main__':
    ok = True
    outs = {}
    for handle, name, out in (('גרילנדות-ותאורה-דקורטיבית', 'decor', 'terms.html'),
                              ('תאורת-שביל-סולארית', 'path', 'terms-path.html'),
                              ('solar-wall-lights', 'wall', '_terms-wall.html'),
                              ('ספוטים-ופרוז-קטורים-סולאריים', 'spot', '_terms-spot.html'),
                              ('all', 'all', '_terms-all.html')):
        outs[name] = page(out, handle)
        col = collection(handle)
        rows = re.findall(r'<li class="env2-coll-terms__line".*?</li>', outs[name], re.S)
        deck = text(re.search(r'class="env2-coll-terms__deck">(.*?)</p>', outs[name], re.S).group(1))
        bdis = len(re.findall(r'<bdi', outs[name]))
        print('%-6s %-24s rows=%d bdi=%-3d deck: %s' % (name, out, len(rows), bdis, deck))
        if len(rows) != 4:
            print('  !! %s printed %d rows, want 4' % (name, len(rows))); ok = False
        want_count = str(col['products_count'])
        if ('<bdi>%s</bdi>' % want_count) not in outs[name]:
            print('  !! %s deck does not carry the collection count %s in a bdi' % (name, want_count)); ok = False
        if '[count]' in outs[name]:
            print('  !! %s left the [count] token unreplaced' % name); ok = False

    print('-- 4.6 copy, read back off the DECOR render')
    rows = re.findall(r'<li class="env2-coll-terms__line".*?</li>', outs['decor'], re.S)
    for got_html, want in zip(rows, WANT):
        got = text(got_html)
        print('   %s' % got)
        if got != want:
            print('  !! does not match 4.6\n      got  %r\n      want %r' % (got, want)); ok = False

    print('-- the call to action and the note')
    cta = re.search(r'<a class="([^"]*)" href="(mailto:[^"]*)"', outs['decor'])
    note = re.search(r'class="env2-coll-terms__note">(.*?)</p>', outs['decor'], re.S)
    print('   classes: %s' % cta.group(1))
    print('   href   : %s' % cta.group(2)[:150])
    print('   label  : %s' % text(re.search(r'<a class="[^"]*" href="mailto:[^"]*"[^>]*>(.*?)</a>', outs['decor'], re.S).group(1)))
    print('   note   : %s' % text(note.group(1)))
    if 'env2-btn--ghost' not in cta.group(1):
        print('  !! the CTA is not the outlined ghost'); ok = False
    if 'env2-btn--ghost' in cta.group(1) and re.search(r'class="[^"]*env2-btn(?![-a-z])[^"]*"[^>]*>\s*הוספה', outs['decor']):
        print('  !! a filled pill anchor is present'); ok = False
    if text(note.group(1)) != 'כאשר מידע אינו מאומת, איננו מציגים אותו כעובדה.':
        print('  !! the note is not the 4.6 sentence'); ok = False
    # the mailto body must name the collection, not a product
    if '%D7%94%D7%A7%D7%95%D7%9C%D7%A7%D7%A6%D7%99%D7%94' not in cta.group(2):
        print('  !! the prefilled body does not name the collection'); ok = False

    print('-- the belts')
    for name, mk in outs.items():
        if 'בוואטסאפ' in mk: print('  !! %s names the channel that does not exist' % name); ok = False
        for bad in ('None', 'Undefined', '~~F~~', '~~R~~', '[count]'):
            if bad in mk: print('  !! %s leaked %r' % (name, bad)); ok = False
        if re.search(r'</bdi>\s*/\s*<bdi>', mk): print('  !! %s split a bdi across a slash' % name); ok = False
    # a page with no collection at all (the theme editor, a page template) must not say "0 המנורות"
    none_mk = page('_terms-nocollection.html', None)
    print('   no collection -> deck: %s' % text(re.search(r'class="env2-coll-terms__deck">(.*?)</p>', none_mk, re.S).group(1)))
    if '0' in text(re.search(r'class="env2-coll-terms__deck">(.*?)</p>', none_mk, re.S).group(1)):
        print('  !! the no-collection deck prints a zero'); ok = False
    # no blocks at all
    nb = page('_terms-noblocks.html', 'גרילנדות-ותאורה-דקורטיבית', None, [])
    if 'env2-coll-terms__ledger' in nb: print('  !! an empty ledger was printed'); ok = False
    if 'env2-coll-terms__act' not in nb: print('  !! the CTA vanished with the blocks'); ok = False
    print('   no blocks -> %d bytes, ledger=%s act=%s' % (len(nb.strip()),
          'env2-coll-terms__ledger' in nb, 'env2-coll-terms__act' in nb))
    print('LINT-ISH %s' % ('OK' if ok else 'FAIL'))
    sys.exit(0 if ok else 2)
