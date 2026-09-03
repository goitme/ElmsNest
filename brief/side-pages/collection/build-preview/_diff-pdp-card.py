# -*- coding: utf-8 -*-
"""Proof for collection WINNING-SPEC §5.3: the round-2 edits to snippets/elmsnest-v2-pdp-card.liquid and
snippets/elmsnest-v2-pdp-image.liquid are ADDITIVE — the PDP related row (sections/elmsnest-v2-pdp-related
.liquid, which passes none of the new parameters) renders BYTE-IDENTICALLY to the pre-edit snippet.

It rebuilds the pre-edit snippets from git (HEAD) into a shadow snippet directory, renders the related
section's exact card call for ALL 27 products through both directories, and diffs.

    python3 brief/side-pages/collection/build-preview/_diff-pdp-card.py
"""
import json, os, re, subprocess, sys, difflib

REPO = '/home/user/ElmsNest'
SNIP = os.path.join(REPO, 'theme', 'snippets')
HERE = os.path.dirname(os.path.abspath(__file__))
SHADOW = os.path.join(HERE, '_before-snippets')
EDITED = ['elmsnest-v2-pdp-card.liquid', 'elmsnest-v2-pdp-image.liquid']

from liquid import Environment, CachingFileSystemLoader

# ---- 1. a shadow snippet dir: every current snippet, except the two edited ones which come from git HEAD
os.makedirs(SHADOW, exist_ok=True)
for f in os.listdir(SNIP):
    src, dst = os.path.join(SNIP, f), os.path.join(SHADOW, f)
    if f in EDITED:
        try:
            blob = subprocess.check_output(['git', '-C', REPO, 'show', 'HEAD:theme/snippets/' + f])
        except subprocess.CalledProcessError:
            print('!! cannot read HEAD:theme/snippets/' + f); sys.exit(2)
        open(dst, 'wb').write(blob)
    else:
        open(dst, 'wb').write(open(src, 'rb').read())

DATA = json.load(open(os.path.join(REPO, 'brief/side-pages/collection/data.json'), encoding='utf-8'))

def money(v):
    try: n = float(v)
    except Exception: return ''
    return '{:,.2f}'.format(n / 100.0)

class Img(str):
    def __new__(cls, path, i):
        o = str.__new__(cls, path); o.src = path; o.alt = ''; o.position = i + 1; return o

def mkenv(d):
    e = Environment(loader=CachingFileSystemLoader(d, ext='.liquid'))
    e.filters['money_without_currency'] = money
    e.filters['money'] = lambda v: money(v) + ' ₪'
    e.filters['image_url'] = lambda v, width=None, **k: str(v) if v else ''
    e.filters['json'] = lambda v, *a, **k: 'null' if (v is None or v.__class__.__name__ == 'Undefined') else json.dumps(v, ensure_ascii=False)
    return e

def build(h):
    p = DATA['products'][h]
    imgs = [Img('../../../assets/img/%s-%d.jpg' % (h, i), i) for i in range(min(4, len(p['images'])))]
    variants, vid = [], 1000
    for val in p['options'][0]['values']:
        for pr in p.get('firstAxis', {}).get(val, [p['priceMin']]):
            vid += 1
            variants.append({'id': vid, 'title': val, 'options': [val],
                             'price': int(round(pr * 100)), 'available': True, 'image': None})
    opts = [{'name': o['name'], 'values': o['values'], 'position': i + 1} for i, o in enumerate(p['options'])]
    return {'handle': h, 'title': p['title'], 'type': p['type'], 'url': '/products/' + h,
            'price_min': int(round(p['priceMin'] * 100)), 'price_max': int(round(p['priceMax'] * 100)),
            'price_varies': p['priceMin'] != p['priceMax'], 'available': True,
            'options_with_values': opts, 'variants': variants, 'images': imgs,
            'featured_image': imgs[0] if imgs else None,
            'selected_or_first_available_variant': variants[0]}

GLOBALS = {'routes': {'cart_add_url': '/cart/add', 'root_url': '/'}, 'settings': {'whatsapp_number': ''}}

# the EXACT call sections/elmsnest-v2-pdp-related.liquid makes (lines 186-193), plus the css:true call
CALL = ("{%- render 'elmsnest-v2-pdp-card', product: env2_p, kicker: env2_ck, width: w, aspect: ar, "
        "image_index: ii, image: im, action_label: al -%}")
CSS  = "{% render 'elmsnest-v2-pdp-card', css: true %}"

before, after = mkenv(SHADOW), mkenv(SNIP)
# the three block variants the related section ships (§4.8 staggers 300/210/260 at 1/1.05 · 1/1.4 · 1/.9)
SHAPES = [(300, '1/1.05', 'לבחירת אורך'), (210, '1/1.4', 'לבחירת דגם'), (260, '1/.9', 'לבחירת גוון')]

diffs, n = [], 0
for h in DATA['products']:
    p = build(h)
    for w, ar, al in SHAPES:
        for ck in ('', 'none'):
            for ii in ('', 1, 4):
                kw = dict(GLOBALS, env2_p=p, env2_ck=ck, w=w, ar=ar, ii=ii, im=None, al=al)
                a = before.from_string(CALL).render(**kw)
                b = after.from_string(CALL).render(**kw)
                n += 1
                if a != b:
                    diffs.append((h, w, ar, ck, ii,
                                  '\n'.join(list(difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm=''))[:24])))

css_a = before.from_string(CSS).render(**GLOBALS)
css_b = after.from_string(CSS).render(**GLOBALS)
# the stylesheet must be a PURE APPEND: every byte the PDP already had, unchanged, plus new rules.
head_a = css_a.replace('</style>', '')
pure_append = css_b.startswith(head_a)
tail = css_b[len(head_a):] if pure_append else css_b
css_removed = [] if pure_append else ['(the stylesheet is not a pure append)']
css_added = [l for l in tail.splitlines() if l.strip()]
# every selector in the appended tail must need a class the PDP never emits
ROUND2 = ('env2-pdp-card--scene', 'env2-pdp-card__axis', 'env2-pdp-card__unit', 'env2-coll-glyph')
tail_nc = re.sub(r'/\*.*?\*/', '', tail, flags=re.S)
selectors = [m.group(1).strip() for m in re.finditer(r'(?m)^([^{}@\n][^{}\n]*)\{', tail_nc)]

print('PDP related-row card markup: %d renders compared (27 products x 3 shapes x 2 kickers x 3 image_index)' % n)
print('MARKUP DIFFS: %d' % len(diffs))
for d in diffs[:5]:
    print('  !!', d[0], d[1], d[2], repr(d[3]), d[4]); print(d[5])
print('CSS lines removed: %d   CSS lines added: %d' % (len(css_removed), len(css_added)))
for l in css_removed:
    print('  !! removed:', l)
stray = [sel for sel in selectors if not any(k in sel for k in ROUND2)]
print('CSS: pure append = %s   selectors added = %d' % (pure_append, len(selectors)))
for sel in selectors:
    print('     +', sel)
print('CSS selectors added that could match PDP DOM: %d' % len(stray))
for l in stray:
    print('  !!', l)
ok = (len(diffs) == 0 and len(css_removed) == 0 and len(stray) == 0)
print('RESULT:', 'IDENTICAL' if ok else 'CHANGED')
sys.exit(0 if ok else 1)
