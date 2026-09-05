# ElmsNest cart — winning spec, re-scoped under the owner's verdict (round 3, 2026-09-05)

## 0. What changed between the brief and this spec

The brief (`BRIEF.md`) was written on the morning of 2026-09-05 under the env2 bar. That afternoon the owner's verdict
arrived through the other session (`brief/side-pages/simplify/OWNER-ANSWERS-2026-09-05.md`): the env2 pages are
*"beautiful but complex — the customer gets confused when they want to buy"*, and the store is being simplified onto
the stock Kalles components in the night language (`brief/side-pages/simplify/SPEC.md`, P1–P7). P1 says it outright:
**"After add = the Kalles cart drawer."**

So this spec does not choose among the five concepts as designs to build. It rules on what each of them proved, and
it applies the proof **inside the stock drawer**: `sections/cart-drawer.liquid` and `snippets/item-cart.liquid`
keep their structure and their JS contract (`INVENTORY-DRAWER.md` §"The contract a rebuild must keep"); the skin
(`snippets/elmsnest-s-skin.liquid` §6) already paints them; what remains is the short list of **measured defects that
the skin cannot reach because they are markup**, plus the one thing every concept agreed on.

## 1. The ruling

Five judges scored five concepts (`JUDGES.json`): slip 8.32 · window 7.96 · meters 7.44 · threestep 7.38 ·
paydesk 6.54 (shopper and conversion weighted ×1.5). Four judges put **slip** first; the shopper put **window** first.
Under the verdict, neither is built as drawn — a serif sentence per line (slip) and a lit-surface material system
(window) are exactly the kind of invention the owner asked to stop. What survives is what the panel agreed on
unanimously and what the harness measured on every concept:

| device | proved by | rule for the stock drawer |
|---|---|---|
| the product's full name, never clipped | all five (`trunc=[false,false]` on every concept vs `[true,true]` today) | `-webkit-line-clamp` on `.hdt-mini-cart__title` goes from 2 to **none**; the title wraps |
| the chosen variant promoted, not greyed | all five | `.hdt-mini-cart__meta-variant` in `--env2-gold`, 13 px, directly under the name |
| a line total when qty > 1 | all five (unit price beneath it; suppressed at qty 1) | `item.final_line_price` printed in the price slot when `item.quantity > 1`, unit price as a 12 px mute line beneath |
| one remove control per line | all five (`removes=[1,1]` vs `[1,2]`) | the second `<wrapp-remove-item-oncart>` inside the stepper is replaced by a **disabled minus** at qty 1 |
| checkout dominant, the exit demoted | threestep, window, paydesk, meters | the skin already does 52 px gold vs 48 px ghost; the ghost «צפה בעגלת הקניות» becomes a **text link** (`.env2-link`), so `dom` measures ≥ 1.8 |
| the terms before the button, verbatim | threestep, window, slip, meters (3 of 4 numbers) | **one line** above the subtotal — the PDP's own `elmsnest-s-pdp-terms-line` wording, which the buyer has just read on the product page: «משלוח חינם לנקודת איסוף · אספקה משוערת 8–17 ימי עסקים · ביטול עד 14 יום מקבלת המוצר» — rendered by the same snippet so it is written once (P2) |
| the void above the subtotal filled | all five | the terms line takes the space; the list no longer flexes to fill |
| no basket headline of metres | threestep, window, paydesk, slip (and `DERIVED-DATA.md`) | nothing derived above the list; `cart.item_count` in the header title only («העגלה שלך · 3 פריטים») |

What is **refused**: slip's serif recognition sentence (authored copy per line — invention the owner rejected);
window's lifted surface and halos (material invention); meters' rail (a device whose headline is blank on 22 of 27
products); paydesk's folded basket (proof hidden by default — the shopper judge scored it lowest on leak 1).

The **cart page** (`sections/main-cart.liquid`, `templates/cart.json`): the Kalles `main-heading` band goes
(P7: the file stays, the template drops it); `elmsnest-cart-guidance`'s three boxes go and its three honest lines
become the same one terms line; the checkout button moves **above** the item list on mobile (every concept but
threestep did this, and threestep's button fell outside the 360×640 fold) so the round-2 contract holds —
**checkout inside the fold at 360×640**. Quantity without JS: the `−`/`+` are rendered as links to
`/cart/change?line=N&quantity=M` beside the `updates[]` input, so the no-JS buyer can change a quantity without
being sent to checkout (`INVENTORY-DRAWER.md` §"The no-JS cart page").

## 2. Acceptance (measured with `verify.js`, drawer and page, 390×844 / 360×640 / 320×568 / 1440×900)

- `trunc=[false,false]`, `removes=[1,1]`, `tracked=[]`, `under44=0` on both surfaces.
- drawer `dom ≥ 1.8`; page `insideFold=true` at 360×640; `voidAboveSubtotal ≤ 40` at 390×844.
- `terms.days` and `terms.cancel` true on both surfaces (the one line carries both); no fourth or fifth term.
- `exitLinks`: 2 on the drawer (the two photographs), ≤ 3 on the page.
- 0 Liquid errors; no horizontal overflow; the drawer opens after the stock main form's add (P1) and after the
  sticky bar's add; the empty drawer shows the four collection links in menu order, nothing else.

## 3. Files

`sections/cart-drawer.liquid` (edit: header title count, view-cart → text link, terms line above the subtotal),
`snippets/item-cart.liquid` (edit: no clamp, variant colour, line total, one bin), `sections/main-cart.liquid`
(edit: checkout block first on mobile, terms line, no-JS quantity links), `templates/cart.json` (drop
`main_heading_zHKQUU` and `elmsnest_cart_guidance`), `snippets/elmsnest-s-skin.liquid` §6 (the clamp rule and the
view-cart rule change). Nothing new is created. Kalles' JS contract survives verbatim.

Build after the SIMPLIFY critique closes; measure before and after with `verify.js` (baseline in
`INVENTORY-DRAWER.md`).
