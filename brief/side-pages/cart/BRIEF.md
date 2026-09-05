# ElmsNest cart — creative brief (round 3, 2026-09-05)

Read in this order: this file · `brief/side-pages/cart/INVENTORY-DRAWER.md` (**the drawer, captured for the first
time — measurements and the DOM contract**) · `brief/WINNING-SPEC.md` §3 (the design system — binding) ·
`brief/side-pages/PLAN.md` §2 · `brief/side-pages/pdp/WINNING-SPEC.md` §3.5–§3.6, §4.8 (image ledger, the card) ·
`brief/side-pages/collection/WINNING-SPEC.md` §4.6 (the terms strip and its four approved numbers) ·
`brief/inventory/AUDIT-cart-search-404.md` §1–§2 · `brief/side-pages/OWNER-NOTES.md` · `brief/side-pages/core/REPORT.md` §9.
Look at the real renders before you draw: `shots/drawer-full-{desktop,mobile}.png`, `shots/drawer-empty-mobile.png`,
`shots/cart-full-mobile.png` — and at the finished product and collection pages, which are the level.

## 1. The job

**This is the only round where nothing is being sold and everything can be lost.** The visitor has already decided.
The drawer's job is to make the decision feel correct and let them pay; the cart page's job is to let them check it
properly. Neither is a place to start a new argument.

**The drawer is the primary surface** (`OWNER-NOTES` §6). It is what every single add-to-cart in the new store opens:
the product page's sticky buy bar, the stage buy line, and the single-variant form on the catalogue card. Most buyers
will never see `/cart` at all. The cart page is (a) the no-JS fallback, (b) the "let me look at this properly" page,
(c) where a shared or bookmarked cart link lands.

Four screens: **drawer-full, drawer-empty, cart-full, cart-empty**.

### The three leaks, in this store specifically

A cart in a 27-product lighting store with **one test order**, no reviews and no brand recognition leaks in three
places. Every concept must plug all three, and may plug them differently:

1. **"Is this the right one?"** — 4 of the 27 products carry 16–30 variants of length × colour, and 19 of 27 show a
   price *range* on the card. The buyer chose `5 מ׳ / 20 נורות / צהוב` two clicks ago. Today the drawer prints that
   variant in grey 13 px and **cuts the product's name off with an ellipsis**, and prints no line total. The first
   thing the drawer owes is *proof that the right lamp is in the basket*.
2. **"What will this cost me and when does it come?"** — the drawer says nothing; the cart page says
   "משלוח מחושב בעת התשלום" and puts the rest in three boxes *below* the checkout button. The four approved numbers
   (below) answer it completely and are already written and already licensed. The moment they are most valuable is
   the moment before paying, from a store you have never bought from.
3. **"Can I get out of this?"** — 14 days by law, cancellation fee capped at the lower of 5 % or 100 ₪. Never said.

### The one thing only a lighting store can say here

The basket is not a list of SKUs; it is an amount of light. `line_item.variant.title` carries the metres and the bulb
counts (`5 מ׳ / 20 נורות`, `7 מ׳ / 50 נורות`, `1.5×1.5 מ׳ / 96 LED`), and `line_item.quantity` multiplies them.
A basket total of **"12 מטר · 70 נורות · 3 מנורות"** is derived, verifiable, free of any claim — and no generic cart
in the world prints it. This is offered as the strongest idea available; a concept may reject it, but must then say
what it puts in its place. **If you use it, it must degrade honestly**: a lamp with no metres in its variant title
contributes nothing to the metre count and must not be guessed at.

## 2. Owner decisions that bound this round

- **The drawer is primary; the cart page is the fallback.** Design the drawer first and hardest.
- **No sales exist.** No badge, no strikethrough, no "-N %", no compare-at rendering, no "you saved".
- **No WhatsApp number.** Any "send a photo of the place" CTA is the `mailto:` path
  (`snippets/elmsnest-v2-pdp-photo-cta.liquid`). Never write "בוואטסאפ".
- **Image ledger locked**: never render `images[0]` of a never-use product (`brief/WINNING-SPEC.md` §3.6). Cart line
  images must go through `snippets/elmsnest-v2-pdp-image.liquid`, not `item.image`.
- **Honesty (`brief/BRIEF.md` §3)**: no ratings, no counts, no "trusted by", no urgency, no countdown, no invented
  fact. **No free-shipping progress bar** — "you are 70 ₪ from free delivery" is manufactured urgency and the
  free-pickup term is not a threshold. The only negatives permitted anywhere are the four approved
  suits/doesn't-suit pairs.

## 3. The four approved numbers (verbatim — do not rewrite, do not add a fifth)

| numeral | unit | headline | sub |
|---|---|---|---|
| `0` | `₪` | משלוח לנקודת איסוף — חינם. | עד הבית 29.90 ₪. |
| `8–17` | `ימי עסקים` | לאספקה: 1–3 ימי טיפול ו־7–14 ימי משלוח. | ייתכן משלוח ממחסן מחוץ לישראל. |
| `14` | `יום` | לביטול מקבלת המוצר, לפי חוק הגנת הצרכן. | דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם. |
| `1` | `תמונה` | שולחים תמונה של המקום ואנחנו בודקים התאמה לפני ההזמנה. | — |

The drawer is 324–351 px wide on a phone. **Four numbers will not fit as four numbers.** Deciding which of them
belongs in the drawer, in what form, and which waits for the cart page, is part of the concept — not a detail.

## 4. What is wrong today (measured — `INVENTORY-DRAWER.md` has the full table)

**Drawer:** an invisible scrim (black panel, black page); **two identical delete controls** on every quantity-1 line;
the product name truncated; no line total; **the two footer buttons identical in fill and size, with the weaker one
on top**; 37 px tall (under 44); `letter-spacing:3px` on Hebrew; a **288–343 px hole** above the subtotal; and no
delivery, cost or cancellation information at all. Empty state: the stock grey cart-with-an-✕ icon.

**Cart page:** **the checkout button's top edge is at y = 932 px at both 390×844 and 360×640** — 88 px below the fold
on the first and 292 px below on the second — at 108×48 px, with the three bordered "לפני שממשיכים לתשלום" boxes
below it as the page's heaviest element. Kalles `main-heading` band; `<h1>` is `sr-only`. Three dashed
label rows per line item on mobile (מחיר / כמות / סך הכל). 2 544 px of document for two products.

## 5. The data you may use (all real)

`cart.item_count`, `cart.total_price`, `cart.items[]` with `product.title`, `variant.title`, `quantity`,
`original_line_price`, `final_line_price`, `url`, `product.handle`, `product.type`, `variant.available`,
`item.error_message`. Product images through the resolver. `cart.items_subtotal_price`.
Derivable and honest: units, distinct lamps, metres and bulb counts parsed out of `variant.title`
(`מ׳` / `נורות` / `LED` / `יח`), and the place kicker the card already computes.
**Not available:** shipping cost before checkout, stock levels, delivery date, any rating, any order history.

## 6. The bar

The homepage and the product and collection pages. A drawer that a competitor could paste into a shoe shop has
failed. Frank Ruhl Libre for display, Heebo for text, gold `#e9b96e`, glow `#ffd394`, radius 0 except pills,
hairlines not boxes, lamps that light on arrival, logical properties only. The drawer is 324 px wide: **this is a
typographic problem before it is a layout problem.**

## 7. Hard constraints

1. **The Kalles contract in `INVENTORY-DRAWER.md` §"The contract a rebuild must keep" survives verbatim.** Restructure
   and restyle inside it; do not replace `<hdt-cart-drawer>`, `<dialog id="CartDrawer">`, `<hdt-line-item>`,
   `<hdt-quantity-wrapp>`, `updates[]`, `<wrapp-remove-item-oncart>`, or `button[name="checkout"]`.
2. **Works with JavaScript off.** The cart page must update quantities and check out through the native form. The
   drawer does not exist without JS — that is exactly why the cart page must be complete on its own.
3. **RTL, logical properties only.** `<bdi>` around every number-plus-unit. No `letter-spacing` on Hebrew.
4. **44 px minimum on every control**, steppers included; the two bins become one.
5. **Checkout is the single dominant control** in both surfaces and, on the cart page, **inside the fold at 360×640**
   — the contract set in round 2: *360×640 must stay inside the fold; any change that pushes it out is a regression.*
6. No progress bar, no note field, no discount field, no gift wrap, no estimator (all off in `system-group.json`,
   and none of them honest or useful here).
7. Empty states are not error screens. An empty cart in a lighting store is an invitation, and the four places
   (שביל · קיר · גינה · מרפסת) are the store's own vocabulary.

## 8. Deliverables (offline mockups, judged from the renders)

Per designer, in `brief/side-pages/cart/concepts/<slug>/`:
- `NOTE.md` — the idea in one sentence, then how it plugs leak 1, leak 2, leak 3; what you dropped and why.
- `drawer.html` + `cart.html` — self-contained mockups, real Hebrew copy, the real basket (2 lines / 3 units /
  429.70 ₪: `מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65` / `צהוב חם` / ×2 / 169.90 ₪ and
  `גרילנדת כדורי קריסטל סולארית – 20 עד 200 נורות` / `5 מ׳ / 20 נורות / צהוב` / ×1 / 89.90 ₪), plus the empty state
  of each in the same file below a `<hr>`.
- Shot at 390×844 and 1440×900 with `node brief/shot.js`.
**Five genuinely different answers.** If two of you arrive at "a tidier version of the same drawer", both have failed.

## 9. Judging (from the screenshots first)

Weights: **does it close the three leaks (35)** · is it unmistakably this store and not a theme (25) · does it work
at 324 px and with JS off (20) · honesty, including what it refuses to claim (10) · does the empty state earn its
screen (10). A concept that is beautiful and answers none of the three questions loses to a plain one that answers
all three.
