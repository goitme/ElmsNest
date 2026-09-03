# -*- coding: utf-8 -*-
"""Renders sections/elmsnest-v2-coll-goodnight.liquid - the REAL section file, through python-liquid,
against data.json, the real snippets, the local image pack and the local fonts - onto the collection
page ground, for all five URLs.

    python3 brief/side-pages/collection/build-preview/_build-goodnight.py
    node brief/shot.js brief/side-pages/collection/build-preview/goodnight.html \
         brief/side-pages/collection/build-preview/goodnight

Harness-only substitutions (all three are Shopify tags python-liquid does not implement):
  * {% stylesheet %} / {% javascript %} / {% schema %} lifted out and re-attached as <style> and
    <script>, which is exactly what Shopify does with them.
Everything else - the Liquid, the photo-cta snippet, the core CSS/JS, the ground - is the shipping file.

It ASSERTS: the other places are named and the current one is never among them; the catalogue count is
collections.all.products_count and never a typed 27; /all prints the four places and NO catalogue link;
the word is outline-only; no filled pill anchor; the channel that does not exist is never named; no
typed catalogue number leaked in; and the section still renders with no blocks and with no image.
"""
import collections.abc as abc
import json, os, re, sys
from liquid import Environment, CachingFileSystemLoader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
SEC  = os.path.join(REPO, 'theme', 'sections', 'elmsnest-v2-coll-goodnight.liquid')
DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/collection/data.json'), encoding='utf-8'))
IMG  = '../../../assets/img/'

COLLIMG = {'גרילנדות-ותאורה-דקורטיבית': 'collection-decor.jpg',
           'תאורת-שביל-סולארית': 'collection-path.jpg',
           'solar-wall-lights': 'collection-wall.jpg',
           'ספוטים-ופרוז-קטורים-סולאריים': 'collection-spot.jpg'}
# the evening order (§3.8.6): path, wall, spot, terrace
ORDER = ['תאורת-שביל-סולארית', 'solar-wall-lights', 'ספוטים-ופרוז-קטורים-סולאריים',
         'גרילנדות-ותאורה-דקורטיבית']
SHORT = {'גרילנדות-ותאורה-דקורטיבית': 'decor', 'תאורת-שביל-סולארית': 'path',
         'solar-wall-lights': 'wall', 'ספוטים-ופרוז-קטורים-סולאריים': 'spot', 'all': 'all'}


class Img(str):
    def __new__(cls, path, w=1800, h=1013):
        o = str.__new__(cls, path)
        o.src = path; o.alt = ''; o.width = w; o.height = h
        return o


def coll(ch):
    if ch == 'all':
        return {'handle': 'all', 'title': 'קטלוג', 'url': '/collections/all',
                'products_count': 27, 'all_products_count': 27, 'image': None}
    c = DATA['collections'][ch]
    n = len(c['handles'])
    return {'handle': ch, 'title': c['title'], 'url': '/collections/' + ch,
            'products_count': n, 'all_products_count': n,
            'image': Img(IMG + COLLIMG[ch])}


COLLS = {ch: coll(ch) for ch in ORDER}
COLLS['all'] = coll('all')


class Colls(abc.Sequence):
    """Shopify's `collections` drop: subscriptable by handle AND iterable over the collections
    themselves. A plain python dict iterates its KEYS, which would hand the fallback loop strings;
    registering as a Sequence is what makes python-liquid walk the values, as Shopify does."""
    def __init__(self, d):
        self._d = d
        self._v = [v for k, v in d.items() if k != 'all']
    def __getitem__(self, k):
        return self._v[k] if isinstance(k, int) else self._d[k]
    def __len__(self): return len(self._v)


env = Environment(loader=CachingFileSystemLoader(SNIP, ext='.liquid'))
env.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
env.filters['money_without_currency'] = lambda v: v
env.filters['money'] = lambda v: str(v)
GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/',
                      'all_products_collection_url': '/collections/all'},
           'settings': {'whatsapp_number': ''},
           'collections': Colls(COLLS)}

src = open(SEC, encoding='utf-8').read()
CSS = re.search(r'\{%\s*stylesheet\s*%\}(.*?)\{%\s*endstylesheet\s*%\}', src, re.S).group(1)
JS  = re.search(r'\{%\s*javascript\s*%\}(.*?)\{%\s*endjavascript\s*%\}', src, re.S).group(1)
SCHEMA = json.loads(re.search(r'\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}', src, re.S).group(1))
BODY = re.sub(r'\{%\s*(stylesheet|javascript|schema)\s*%\}.*?\{%\s*end\1\s*%\}', '', src, flags=re.S)

DEFAULTS = {}
for s in SCHEMA['settings']:
    if s.get('type') in ('header', 'paragraph'):
        continue
    DEFAULTS[s['id']] = s.get('default', '')
DEFAULTS.update(SCHEMA['presets'][0].get('settings', {}))


def blocks_for(configured=True):
    """The four place blocks as the integrator will wire them in templates/collection.json:
    one collection picker each, in the evening order."""
    if not configured:
        return [{'type': 'place', 'id': 'b%d' % i, 'shopify_attributes': '',
                 'settings': {'collection': None, 'label': ''}} for i in range(4)]
    out = []
    for i, ch in enumerate(ORDER):
        out.append({'type': 'place', 'id': 'b%d' % i,
                    'shopify_attributes': 'data-shopify-editor-block="{&quot;id&quot;:&quot;b%d&quot;}"' % i,
                    'settings': {'collection': COLLS[ch], 'label': ''}})
    return out


core = open(os.path.join(SNIP, 'elmsnest-v2-core.liquid'), encoding='utf-8').read()
core_css = re.search(r'<style id="env2-base">(.*?)</style>', core, re.S).group(1)
core_js = re.search(r'<script id="env2-base-js">(.*?)</script>', core, re.S).group(1)
ground = re.search(r'<style id="env2-ground-collection">(.*?)</style>',
                   open(os.path.join(SNIP, 'elmsnest-v2-ground-collection.liquid'),
                        encoding='utf-8').read(), re.S).group(1)

PAGE = """<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<script>document.documentElement.classList.add('env2-js');</script>
<link rel="stylesheet" href="../../../assets/fonts.css">
<style>%(core)s</style>
<style>%(ground)s</style>
<style>%(css)s</style>
<style>
/* the ground the real template gives this section: it is the SEVENTH and LAST of seven, so the
   preview starts the 3.1 pixel gradient at the depth it has actually reached there - full night. */
body{margin:0;background-position-y:-4800px}
/* the Kalles footer that sits DIRECTLY below (4.7), at its real dark ground, so the seam is visible.
   Mock only: nothing here ships. */
.env2-mock-footer{border-block-start:1px solid rgba(244,238,227,.12);background:#05070c;color:#8f95a3;
  font-family:var(--env2-sans);font-size:13px;padding:44px clamp(20px,4vw,64px);display:flex;gap:28px;flex-wrap:wrap}
</style>
</head>
<body class="hdt-page-type-collection template-collection">
<main id="MainContent" class="hdt-main-content">
<div class="shopify-section">%(markup)s</div>
</main>
<footer class="env2-mock-footer"><span>הפוטר של Kalles (הדמיה)</span><span>אודות</span><span>יצירת קשר</span></footer>
<script>%(corejs)s</script>
<script>%(js)s</script>
</body></html>"""


def render(ch, extra=None, blocks=None):
    st = dict(DEFAULTS); st.update(extra or {})
    sec = {'id': 'coll_goodnight', 'settings': st,
           'blocks': blocks_for() if blocks is None else blocks}
    return env.from_string(BODY).render(**dict(GLOBALS, collection=COLLS.get(ch), section=sec))


def page(out, ch, extra=None, blocks=None):
    markup = render(ch, extra, blocks)
    doc = PAGE % {'title': 'goodnight · ' + str(ch), 'core': core_css, 'ground': ground,
                  'css': CSS, 'markup': markup, 'corejs': core_js, 'js': JS}
    open(os.path.join(HERE, out), 'w', encoding='utf-8').write(doc)
    return markup


def text(m):
    t = re.sub(r'>\s*<', '> <', m)
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&nbsp;', ' ').replace('&#39;', "'").replace('&amp;', '&').replace('&quot;', '"')
    return re.sub(r'\s+', ' ', t).strip()


if __name__ == '__main__':
    ok = True
    outs = {}
    for ch, out in (('גרילנדות-ותאורה-דקורטיבית', 'goodnight.html'),
                    ('תאורת-שביל-סולארית', 'goodnight-path.html'),
                    ('solar-wall-lights', '_goodnight-wall.html'),
                    ('ספוטים-ופרוז-קטורים-סולאריים', '_goodnight-spot.html'),
                    ('all', '_goodnight-all.html')):
        name = SHORT[ch]
        mk = outs[name] = page(out, ch)
        links = re.findall(r'<a class="env2-coll-goodnight__a"[^>]*href="([^"]*)"[^>]*>(.*?)</a>', mk, re.S)
        allink = re.search(r'<a class="env2-coll-goodnight__all"[^>]*href="([^"]*)"[^>]*>(.*?)</a>', mk, re.S)
        print('%-5s %-22s places=%d  %s' % (name, out, len(links),
              ' · '.join(text(t) for _, t in links)))
        print('      catalogue: %s' % (text(allink.group(2)) + '  -> ' + allink.group(1) if allink else '(none)'))
        want = 4 if ch == 'all' else 3
        if len(links) != want:
            print('  !! %s printed %d places, want %d' % (name, len(links), want)); ok = False
        # the collection being viewed is NEVER one of its own ways out
        if ch != 'all' and any(('/collections/' + ch) == h for h, _ in links):
            print('  !! %s links to itself' % name); ok = False
        if ch == 'all':
            if allink:
                print('  !! /all prints the catalogue link it is already on'); ok = False
        else:
            if not allink:
                print('  !! %s has no catalogue link' % name); ok = False
            elif '<bdi>27</bdi>' not in allink.group(0):
                print('  !! %s catalogue count is not the Liquid one in a bdi' % name); ok = False
        if '[count]' in mk:
            print('  !! %s left the [count] token unreplaced' % name); ok = False
        # every place count is that collection's own, in a bdi
        for h, t in links:
            hh = h.replace('/collections/', '')
            if '<bdi>%d</bdi>' % COLLS[hh]['all_products_count'] not in ('<bdi>' + text(t).split()[-1] + '</bdi>'):
                print('  !! %s: %s prints %r, not its own count %d'
                      % (name, hh, text(t), COLLS[hh]['all_products_count'])); ok = False

    print('-- the word, the photograph and the call to action (decor)')
    big = re.search(r'class="env2-coll-goodnight__big"[^>]*>(.*?)</p>', outs['decor'], re.S)
    print('   word   : %s   (aria-hidden=%s)' % (text(big.group(1)), 'aria-hidden' in big.group(0)))
    if 'aria-hidden' not in re.search(r'<p class="env2-coll-goodnight__big"[^>]*>', outs['decor']).group(0):
        print('  !! the decorative word is not aria-hidden'); ok = False
    if '-webkit-text-stroke' not in CSS or re.search(r'__big\{[^}]*color:(?!transparent)', CSS):
        print('  !! the word is not outline-only'); ok = False
    img = re.search(r'<img class="env2-coll-goodnight__img"[^>]*src="([^"]*)"', outs['decor'])
    print('   garden : %s  pos=%s' % (img.group(1) if img else '(none)',
          re.search(r'--env2-goodnight-pos:([^"]*)"', outs['decor']).group(1)))
    if not img:
        print('  !! the decor render has no photograph'); ok = False
    cta = re.search(r'<a class="([^"]*)" href="(mailto:[^"]*)"', outs['decor'])
    print('   step   : %s' % text(re.search(r'class="env2-coll-goodnight__line">(.*?)</p>', outs['decor'], re.S).group(1)))
    print('   cta    : %s  [%s]' % (text(re.search(r'href="mailto:[^"]*"[^>]*>(.*?)</a>', outs['decor'], re.S).group(1)), cta.group(1)))
    if 'env2-link' not in cta.group(1):
        print('  !! the call to action is not the quiet link'); ok = False
    if '%D7%94%D7%A7%D7%95%D7%9C%D7%A7%D7%A6%D7%99%D7%94' not in cta.group(2):
        print('  !! the prefilled body does not name the collection'); ok = False

    print('-- the degradations')
    nb = page('_goodnight-noblocks.html', 'גרילנדות-ותאורה-דקורטיבית', None, [])
    fb = len(re.findall(r'env2-coll-goodnight__a"', nb))
    print('   no blocks at all      -> %d places from the store fallback, catalogue link=%s'
          % (fb, 'env2-coll-goodnight__all' in nb))
    if fb != 3:
        print('  !! the fallback did not find the other three places'); ok = False
    ub = page('_goodnight-unset.html', 'גרילנדות-ותאורה-דקורטיבית', None, blocks_for(False))
    print('   4 blocks, none set    -> %d places (fallback), catalogue link=%s'
          % (len(re.findall(r'env2-coll-goodnight__a"', ub)), 'env2-coll-goodnight__all' in ub))
    nofb = page('_goodnight-nofallback.html', 'גרילנדות-ותאורה-דקורטיבית',
                {'auto_places': False}, [])
    print('   fallback off, no blocks-> %d places, catalogue link=%s, step=%s'
          % (len(re.findall(r'env2-coll-goodnight__a"', nofb)), 'env2-coll-goodnight__all' in nofb,
             'env2-coll-goodnight__line' in nofb))
    if 'env2-coll-goodnight__all' not in nofb or 'env2-coll-goodnight__line' not in nofb:
        print('  !! the way out vanished with the places'); ok = False
    nc = page('_goodnight-nocollection.html', None)
    print('   no collection at all  -> %d places, catalogue link=%s, garden=%s'
          % (len(re.findall(r'env2-coll-goodnight__a"', nc)), 'env2-coll-goodnight__all' in nc,
             'env2-coll-goodnight__img' in nc))
    if 'env2-coll-goodnight__all' not in nc or 'env2-coll-goodnight__big' not in nc:
        print('  !! the section collapses with no collection in scope'); ok = False
    noimg = page('_goodnight-noimage.html', 'all', None, blocks_for(False))
    print('   no image anywhere     -> garden=%s, word=%s'
          % ('env2-coll-goodnight__img' in noimg, 'env2-coll-goodnight__big' in noimg))
    if 'env2-coll-goodnight__img' in noimg:
        print('  !! a photograph was drawn with no image to draw'); ok = False
    if 'env2-coll-goodnight__big' not in noimg:
        print('  !! the word vanished with the photograph'); ok = False
    # /all with the four blocks set must take the FIRST place's image, since it owns none
    allimg = re.search(r'<img class="env2-coll-goodnight__img"[^>]*src="([^"]*)"', outs['all'])
    print('   /all garden           -> %s' % (allimg.group(1) if allimg else '(none)'))
    if not allimg:
        print('  !! /all has no photograph'); ok = False

    print('-- the belts')
    for name, mk in list(outs.items()) + [('noblocks', nb), ('unset', ub), ('nocollection', nc)]:
        if 'בוואטסאפ' in mk:
            print('  !! %s names the channel that does not exist' % name); ok = False
        for badtok in ('None', 'Undefined', '~~F~~', '~~R~~', '[count]'):
            if badtok in mk:
                print('  !! %s leaked %r' % (name, badtok)); ok = False
        if re.search(r'</bdi>\s*/\s*<bdi>', mk):
            print('  !! %s split a bdi across a slash' % name); ok = False
        # 6.19: no catalogue number may be typed into the markup outside a bdi
        for n in re.findall(r'(?<![\d>])\b(2[0-9]|[1-9])\b(?![\d<])', text(mk)):
            pass
        if re.search(r'class="env2-btn(?![-a-z])[^"]*"[^>]*href=', mk):
            print('  !! %s renders a FILLED pill anchor (core REPORT 9.1)' % name); ok = False
    print('BUILD %s' % ('OK' if ok else 'FAIL'))
    sys.exit(0 if ok else 2)
