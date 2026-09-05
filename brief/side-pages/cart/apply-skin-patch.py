#!/usr/bin/env python3
"""Apply the round-3 cart skin patch (SKIN-PATCH.json, from the two build engineers) plus the lead's extras to
snippets/elmsnest-s-skin.liquid §6, anchored on selector text rather than line numbers so it survives the
SIMPLIFY critique fixer's edits elsewhere in the file. Idempotent: refuses to run twice.
Usage: python3 brief/side-pages/cart/apply-skin-patch.py [--dry]"""
import json, sys, re
P = '/home/user/ElmsNest/theme/snippets/elmsnest-s-skin.liquid'
PATCH = json.load(open('/home/user/ElmsNest/brief/side-pages/cart/SKIN-PATCH.json', encoding='utf-8'))
by = {(e['from'], e['selector']): e['newRule'] for e in PATCH}
s = open(P, encoding='utf-8').read()
if '.ens-cart-empty' in s:
    raise SystemExit('already applied (found .ens-cart-empty in the skin)')
lines = s.split('\n')

def find(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    if len(idx) != 1:
        raise SystemExit(f'anchor {prefix!r}: {len(idx)} matches')
    return idx[0]

# D4 title: replace the clamp rule
i = find('#CartDrawer .hdt-mini-cart__title{')
lines[i] = by[('drawer', '#CartDrawer .hdt-mini-cart__title')]
# D5 variant: split the ink-2 rule; the gold rule MUST follow it (same specificity, source order decides)
i = find('#CartDrawer :is(.hdt-mini-cart__meta-variant,')
lines[i:i + 1] = by[('drawer', '#CartDrawer :is(.hdt-mini-cart__meta-variant,.hdt-text-secondary,.hdt-cart-tax)')].split('\n')
# D6 unit line: after the price/gold rule
i = find('#CartDrawer :is(.hdt-mini-cart__price .hdt-price,')
lines.insert(i + 1, by[('drawer', '#CartDrawer .hdt-mini-cart__unit')])
# D3 void: after the bottom rule
i = find('#CartDrawer .hdt-mini-cart__bottom{')
lines[i + 1:i + 1] = by[('drawer', '#CartDrawer .hdt-mini-cart__main')].split('\n')
# dead selector: the empty-state button no longer renders (D8/C6)
for k in range(len(lines)):
    if lines[k].startswith('#CartDrawer :is(.hdt-mini-cart__btn-checkout,.hdt-mini-cart__emty-button).hdt-btn'):
        lines[k] = lines[k].replace(':is(.hdt-mini-cart__btn-checkout,.hdt-mini-cart__emty-button).hdt-btn', '.hdt-mini-cart__btn-checkout.hdt-btn', 1)
# D2 view-cart: replace the two pill rules
i = find('#CartDrawer .hdt-mini-cart__btn-viewcart.hdt-btn{')
lines[i] = by[('drawer', '#CartDrawer .hdt-mini-cart__btn-viewcart.hdt-btn')]
i = find('#CartDrawer .hdt-mini-cart__btn-viewcart.hdt-btn:is(')
lines[i] = by[('drawer', '#CartDrawer .hdt-mini-cart__btn-viewcart.hdt-btn:is(:hover,:focus-visible)')]
# new rules, appended after the view-cart hover rule, in this order
extra = [
    by[('drawer', '#CartDrawer .ens-cart-empty')],
    by[('drawer', '#CartDrawer .ens-cart-terms .ens-terms-line')],
    # the disabled minus at qty 1, both surfaces (reviewer finding, lead-approved)
    '#CartDrawer .hdt-quantity-cart-item button:disabled,#hdt-page-cart .hdt-quantity-cart-item button:disabled{opacity:.35;cursor:default}',
    # 44 px controls on both surfaces (WINNING-SPEC §2 under44=0): Kalles keeps the stepper at 4rem = 40 px and the remove link at the icon's height
    '#CartDrawer .hdt-quantity-cart-item,#hdt-page-cart .hdt-quantity-cart-item{block-size:auto;min-block-size:44px}',
    '#CartDrawer .hdt-quantity-cart-item :is(button,input),#hdt-page-cart .hdt-quantity-cart-item :is(button,input){min-block-size:44px;block-size:44px}',
    '#CartDrawer .hdt-mini-cart__remove,#hdt-page-cart .hdt-mini-cart__remove{display:inline-flex;align-items:center;min-block-size:44px;padding-inline:8px}',
    # the cart page: the checkout button full width in the night language (C7: the block schema has no full-width setting)
    by[('page', '#hdt-page-cart .hdt-main-cart__button-checkout.hdt-btn')],
    by[('page', '#hdt-page-cart .hdt-main-cart__button-checkout.hdt-btn:is(:hover,:focus-visible)')],
    # the cart page's own new bits: the four-collection empty state and the no-JS quantity links
    '#hdt-page-cart .ens-cart-empty{display:grid;gap:14px;justify-items:center;margin-block-start:18px}',
    '#hdt-page-cart .ens-cart-qtylink{display:inline-flex;align-items:center;justify-content:center;min-inline-size:44px;min-block-size:44px;color:var(--env2-ink);text-decoration:none;font-size:18px}',
]
lines[i + 1:i + 1] = extra
out = '\n'.join(lines)
n = len(out.encode('utf-8'))
print(f'skin: {len(s.encode("utf-8"))} -> {n} bytes')
if '"""' in out:
    raise SystemExit('block-string terminator in the skin')
if '--dry' in sys.argv:
    seg = out[out.index('/* ---- 6.'):]
    print(seg[:seg.index('/* ----', 10)] if '/* ----' in seg[10:] else seg)
else:
    open(P, 'w', encoding='utf-8').write(out)
    print('written')
