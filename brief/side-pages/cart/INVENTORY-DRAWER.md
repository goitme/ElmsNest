# The cart drawer, captured for the first time (2026-09-05)

`brief/inventory/AUDIT-cart-search-404.md` §0 had to say: *"no `<hdt-cart-drawer>` markup was captured … it is
**closed in every render; its look cannot be judged from this inventory**"*. That hole is now closed, and one of the
audit's statements about it turns out to have been a statement about its **configuration**, not about what it paints.

## How it was captured (repeatable)

Chromium cannot reach the storefront through this sandbox's proxy (`ERR_CONNECTION_RESET`, `ws_closed_mid_exchange`),
so the drawer was captured the same way every other page was — curl to mirror, local HTTP to render:

1. `curl -c jar -L 'https://elmsnest.com/?preview_theme_id=154726400174'` → a preview session.
2. `curl -b jar -X POST https://elmsnest.com/cart/add.js -d '{"items":[{"id":48880938221742,"quantity":1},{"id":48632265310382,"quantity":2}]}'`
   — a cart with 2 lines / 3 units / 429.70 ₪ (crystal-ball string 5 m, and the stainless path light ×2). This is a
   **cookie-scoped cart**; it touches no store data.
3. `sections/cart-drawer.liquid` line 27 is `{%- if request.page_type != 'cart' -%}` — **the drawer does not exist on
   `/cart`**. So it must be mirrored from another template: `python3 brief/mirror.py '…/collections/all?preview_theme_id=…' <dir>`
   with the jar copied to `<dir>/cj.txt` first (mirror.py reuses `cj.txt`, so the cart travels with it).
4. `node brief/shot-drawer.js <dir>/index.html <prefix>` — new; identical to `shot-http.js` except that it calls the
   theme's own `hdt-cart-drawer.open()` before shooting, and shoots the viewport rather than the full page.

Shots: `shots/drawer-{full,empty}-{desktop,mobile}.png`, `shots/cart-{full,empty}-{desktop,mobile}.png`.
Mirrors kept under `mirrors/` (four states). Measurements below from `measure-cart.js` at 390×844, 360×640, 1440×900.

## What it actually looks like

**The audit's "scheme `S-e0b7` (light cream `#fffdf7`)" is the theme-editor setting. It does not paint.** Round 0's
core remaps the Kalles schemes, so the drawer today is already on the night ground: `dialog` background
`rgb(2,3,6)`, prices in gold, buttons in glow `#ffd394`. The drawer is the one piece of Kalles chrome that arrived
half-way onto the system by itself. What is wrong with it is therefore **composition and behaviour**, not palette.

| | 390×844 | 360×640 | 1440×900 |
|---|---|---|---|
| dialog width | 351 px (90 %) | 324 px (90 %) | **340 px (24 %)** |
| backdrop | `rgba(2,3,6,.5)` | same | same |
| checkout button | t 787 → b 824, 311×37 | 583→620, 284×37 | 843→880, 300×37 |
| "צפה בעגלת הקניות" | t 740 → b 777, 311×37 | 536→573 | 796→833 |
| dead space, last line → subtotal | **288 px** | 84 px | **343 px** |

### The nine findings

1. **The scrim cannot be seen.** The backdrop is `rgba(2,3,6,.5)` over a page that is already `#020306`. On the new
   collection and product pages the dimming is arithmetically real and visually nil: a black panel on a black page,
   separated only by a 1 px gold hairline. (My first read of the desktop shot was "there is no scrim at all" — the
   computed style says otherwise. The defect is that a correct scrim does no work here.)
2. **Two delete controls on any line at quantity 1.** `snippets/item-cart.liquid` renders
   `<wrapp-remove-item-oncart>` both outside the stepper *and* inside it in place of the minus button. Measured:
   `trashes: 1` on the qty-2 line, **`trashes: 2`** on the qty-1 line. Two bins, 40 px apart, same icon, same action.
3. **The product's name is cut off.** "מנורת שביל סולארית מנירוס…" / "גרילנדת כדורי קריסטל סולא…" — one line with an
   ellipsis, in a 351 px panel. The name is the only thing that tells a buyer they picked the right lamp.
4. **No line total.** The qty-2 line shows `169.90 ₪` and `2`. The buyer multiplies. (The cart *page* does print
   `סך הכל 339.80 ₪` — the drawer, which is the primary surface, does not.)
5. **The two footer buttons are identical.** Same glow fill `#ffd394`, same 311×37 box, stacked, and the weaker one
   ("צפה בעגלת הקניות") is **above** checkout. Nothing says which one is the sale.
6. **37 px tall** — under the 44 px touch minimum, and under the 48 px `elmsnest-cart-guidance` already forces on the
   cart page's own checkout button.
7. **`letter-spacing: 3px` on Hebrew.** Hebrew does not track. `צ פ ה  ב ע ג ל ת  ה ק נ י ו ת`.
8. **A 288–343 px hole** between the last line and the subtotal, because the item list flexes to fill. With two lines
   the drawer looks emptier than the cart is.
9. **Not one word about delivery, cost, or cancellation** — at the exact moment the buyer is deciding whether to pay a
   store they have never bought from. The empty state is worse: the stock Kalles grey cart-with-an-✕ line icon,
   "העגלה שלך ריקה", and a single glow button to `/collections`.

## The cart page, re-measured on the night ground

The audit's §1–§2 composition is unchanged; only the palette moved. The one number that matters:

> **The checkout button's top edge is at y = 932 px on both 390×844 and 360×640** — 88 px below the fold on the
> first, **292 px below on the second** — and it is 108×48 px. The subtotal lands at y = 843, i.e. exactly on the
> fold line of a 390×844 phone. Below the button sit the three bordered "לפני שממשיכים לתשלום" boxes, which are the
> heaviest thing on the page. The document is 2 544 px tall for two products.

The `<h1>` is `sr-only` (1×1 px at y 109); the visible "ההזמנה שלך" is the Kalles `main-heading` band, a flat
lighter-navy strip with `{{ page_title }}` in Heebo — the same band the collection round removed.

## The contract a rebuild must keep

The drawer is opened by the core's own buy handler (`elmsnest-v2-core.liquid`, `form[data-env2-buy]` → `/cart/add.js`
with `sections=<drawer section id>` → `cart:update` with `actionAfterATC: 'open_cart_drawer'`), and by Kalles' header
cart button. Everything below is read by theme JS and must survive verbatim:

| element / attribute | why |
|---|---|
| `<hdt-cart-drawer id="{{ section.id }}" ref="hdt-cart" section-id data-count data-total-price>` | the element the core queries and the count the header mirrors |
| `<dialog id="CartDrawer" ref="dialog" pos="right" scroll-lock>` | `.open()` / focus trap / scroll lock |
| `<button ref="closeButton" aria-controls="CartDrawer">` | close |
| `<form action="{{ routes.cart_url }}" id="{{ form_id }}" method="POST">` + `<button type="submit" name="checkout">` | checkout, and the no-JS path |
| `<hdt-line-item>` per line | line replacement on quantity change |
| `<hdt-quantity-wrapp>`, `<button name="minus">`, `<input name="updates[]" data-index data-max>`, `<button name="plus">` | the stepper |
| `<wrapp-remove-item-oncart data-index>` | remove |

Everything else in the section — order, wording, type, spacing, what is shown and what is not — is ours.

## The acceptance harness and the baseline it records

`brief/side-pages/cart/verify.js <mirror>/index.html <label> [--drawer]` — serves the mirror, optionally opens the
drawer through the theme's own element, and prints one JSON line per viewport (390×844, 360×640, 320×568, 1440×900)
with every number this round is judged on. Three of its readings were wrong on the first pass and were fixed against
the screenshots before this baseline was recorded: `a[href*="/products/"]` matched the **image** anchor, which never
overflows, so truncation read `false` on titles that are visibly cut (now the title is selected explicitly); the
terms check read `document.body`, which on a drawer render is *the page behind it* (now scoped to the open dialog);
and the "largest rival control" was the product photograph (photo links are now counted separately, as **exits**).

**Baseline, the drawer as it is today** (identical at all four viewports except the void):

```
dom=0.99 vs 'צפה בעגלת הקניות'   exits=2   trunc=[True,True]   removes=[1,2]
tracked=[{'צפה בעגלת הקניות','3px'},{'תשלום','3px'}]   under44=10   terms=0/4
void=288 (390×844) · 84 (360×640) · 12 (320×568) · 343 (1440×900)
```

`dom=0.99` is the twin-button defect as a number: the checkout control and the link that leaves the cart are the
same size to within one percent. `terms=0/4` is finding 9. `removes=[1,2]` is finding 2, and it appears on the
second line only because that is the line at quantity 1.

**Baseline, the cart page as it is today:**

```
390×844   checkout t932 b980 108×48   BELOW THE FOLD BY 136   dom=0.58   exits=5  under44=25  terms=3/4  doc 2544
360×640   checkout t932 b980 108×48   BELOW THE FOLD BY 340   dom=0.68   exits=5  under44=25  terms=3/4  doc 2567
320×568   checkout t988 b1036 108×48  BELOW THE FOLD BY 468   dom=0.65   exits=5  under44=23  terms=3/4  doc 2683
1440×900  checkout t795 b843 108×48   inside                  dom=0.73   exits=5  under44=33  terms=3/4  doc 1791
```

The rival that beats the checkout button on every viewport is **a product title link** — on the cart page the
largest thing a decided buyer can press is a route back out of the cart. Five such exits per two-item cart.

**One thing was checked and found NOT to be broken.** `brief/side-pages/core/REPORT.md` §9.2 leaves
`--en-error-text` (145 33 42, 1.8:1 on the night ground) open, and the cart is the one surface that renders an
error (`הכמות שבחרת אינה זמינה`, on every line). Measured: the message computes `rgb(201,196,184)` on `rgb(2,3,6)` —
**11.86:1**. Kalles styles it from `--color-foreground2`, not from the semantic token, so §9.2 stays correctly
deferred and the rebuild is free to choose its own error treatment rather than inheriting a broken one.
