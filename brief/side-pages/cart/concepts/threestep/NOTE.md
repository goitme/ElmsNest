# threestep — שלושה צעדים

## The idea, in one sentence

The drawer is a countdown, not a container: three numbered bands in one fixed column — **01 מה בחרת · 02 מה יעלה
לקבל את זה · 03 תשלום** — sized so that a two- or three-item basket never scrolls, the two questions a first-time
buyer has not asked out loud are answered *above* the button, and the button is then the only thing left to do.

## Leak 1 — "is this the right one?"

Everything the buyer needs to recognise their own choice is printed, none of it abbreviated:

- **The product name wraps; it is never truncated.** Two lines at 14.5 px (17–18 px on desktop and on the cart page),
  Heebo 400 — never the serif. The measured defect (`מנורת שביל סולארית מנירוס…`) does not exist here at 324 px.
- **The variant is promoted, not demoted.** `צהוב חם` / `5 מ׳ / 20 נורות / צהוב` sits directly under the name in
  gold at 12 px, on its own line. It is the second thing you read, not grey 13 px filler.
- **The arithmetic is on the page.** Every line prints `169.90 ₪ ליחידה` above `339.80 ₪` — unit price, quantity and
  line total adjacent, in that reading order, with the line total in the display face in glow. Where the quantity is
  1, the "ליחידה" row is suppressed: printing `89.90 ₪ ליחידה` above `89.90 ₪` is noise, not proof.
- **One remove control per line, never two.** `<wrapp-remove-item-oncart>` renders once, as the word **הסרה** under
  the thumbnail at 64×44 px. The minus button at quantity 1 is `disabled` rather than silently mutating into a
  second bin. `removes=[1,1]`, not `[1,2]`.
- **No basket headline is derived.** `DERIVED-DATA.md` kills the "12 מטר · 70 נורות" headline: metres exist in the
  variant title of 5 products of 27 and `1.5×1.5 מ׳` is an area. What replaces it is the honest version of the same
  instinct — the metres and the bulbs are already inside `variant.title`, so they are simply shown per line, where
  they are true, and the header counts only what needs no parsing: `<bdi>3</bdi> פריטים` from `cart.item_count`.

## Leak 2 — "what will this cost me and when does it come?"

Band 02 is the spine of the drawer, not a footnote below the button. Three of the four approved terms, **verbatim,
headline and sub**, as a hairline ledger — the collection page's §4.6 shape, never four boxes:

| | |
|---|---|
| `0 ₪` | משלוח לנקודת איסוף — חינם. · עד הבית 29.90 ₪. |
| `8–17 ימי עסקים` | לאספקה: 1–3 ימי טיפול ו־7–14 ימי משלוח. · ייתכן משלוח ממחסן מחוץ לישראל. |
| `14 יום` | לביטול מקבלת המוצר, לפי חוק הגנת הצרכן. · דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם. |

Measured: at 390×844 the strip occupies y 386→540 and the checkout button starts at y 641 — **the terms are read
before the finger reaches the button, on the same screen, with no scroll.** On the cart page they are at y 392→520
at 360×640, i.e. also above the fold and also above the button.

The subs are kept because they are the part that costs the store something: `עד הבית 29.90 ₪`, the out-of-Israel
warehouse, and the cancellation fee. A terms strip that prints only the flattering half is an advertisement.

## Leak 3 — "can I get out of this?"

The third row of that same strip, in the same weight as the shipping row, immediately above the pay control. It is
the last thing read before pressing, and it carries the fee, not only the fourteen days.

## What is dominant, and what is not

`מעבר לתשלום · 429.70 ₪` — full-width pill, **59 px** at 390 (63 px at 1440, 54 px at 360×640), glow fill, the
amount repeated inside it in the display face, and a soft ember halo. The route to `/cart` is a **12.5 px underlined
text link** in ink-2 — `לפתוח את עגלת הקניות ולבדוק שוב` — 44 px tall for the finger, and visually about a tenth of
the button. The twin-button defect (`dom=0.99`) is answered with roughly a 9:1 ratio, and the weaker route is now
*below* the sale, not above it.

There is **no dead hole above the subtotal**. The bands stack from the top with vh-elastic padding; whatever height
is left over at the bottom of a tall panel falls to `.foot` — 93 px at 390×844, 110 px at 1440×900 — which is not
empty space but a warm radial floor-glow, as if the lit button were a lamp standing on it. On the empty drawer the
same foot is ~215 px and does the same job.

## The empty state

Not an error screen and not a grey cart-with-an-✕. `עוד לא בחרת / מה נדלק אצלך.` in the serif, one sentence of
orientation, then the store's own four places as hairline rows with the homepage's outlined numerals — שביל · קיר ·
גינה · מרפסת, each 56–92 px tall — and one ghost pill to `לכל 27 המוצרים`. The panel foot keeps its glow, so the
empty drawer is still lit.

On the **empty cart page** the fourth approved term finally appears — `1 תמונה` with the `mailto:` photo CTA and the
note `כאשר מידע אינו מאומת, איננו מציגים אותו כעובדה.` That is the one screen where "send a photo of the place
before ordering" is help rather than a distraction.

## What I dropped, and why

- **The fourth approved number is not in the drawer.** Four numbers do not fit in 324 px without shrinking the three
  that answer the question actually being asked, and inviting a buyer with a full basket to go and email a photo is
  a route out of checkout at the worst possible moment. It lives on the empty cart page and on the product page.
- **The derived basket headline** (§1's "12 מטר · 70 נורות · 3 מנורות"). See leak 1: it would be blank or wrong on
  most real baskets of this catalogue.
- **The Kalles `main-heading` band** on the cart page; `<h1>ההזמנה שלך</h1>` is visible type, not `sr-only`.
- **The three bordered "לפני שממשיכים לתשלום" boxes** below the cart page's button — the same content, in the
  approved wording, moved above it as band 02.
- **`letter-spacing`** — it is not set anywhere in either file, on any element.

## Numbers

Drawer, measured:

```
390×844   panel 351   items 89→357   terms 386→540   checkout 641→700 (319×59)   link 700→744   foot 93
360×640   panel 324   items 82→278*  terms 303→445   checkout 536→590 (292×54)   link 590→634   foot 0
1440×900  panel 420   items 90→375   terms 404→569   checkout 675→738 (388×63)   link 738→782   foot 110
```

Cart page, checkout button: `390×844 t606 b662` · **`360×640 t578 b634 — inside the fold`** · `1440×900 t439 b503`.
`shot.js`: drawer `desktop 1801 px / mobile 1689 px`, cart `desktop 2049 px / mobile 2387 px`, no horizontal
overflow and no JS errors on either.

\* At 360×640 — a 640 px-tall viewport with three bands and a 44 px minimum on every control — the item list is the
only thing that gives: it scrolls ~99 px while bands 02 and 03 stay pinned and fully visible. At 360×740 and above,
and at 390×844, **nothing scrolls at two or three items**, which is the claim the concept actually makes. I would
rather say that than pretend a 640 px screen is a 844 px screen.

## Desktop panel width: 420 px

The drawer today is 340 px at 1440 (24 % of the viewport) — narrower, relative to its content, than the phone panel,
so the desktop drawer inherits the phone's cramping for no reason. 420 px is the width at which the longest real
product title (`מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65`) sets on two lines at 18 px, and each terms row's
headline sets on one line beside its numeral. It is still 29 % of 1440, so the catalogue behind stays legible as the
place you are returning to if you close the panel.

## Weakest point

Band 02 is the same three rows whether the basket is 89.90 ₪ or 2,400 ₪ and whether it is one lamp or nine — it is a
fixed 154 px tax on every open, and on a very short viewport it is what pushes the item list into scrolling. A
version that showed only the delivery row until the buyer had scrolled the items would fit more comfortably; I did
not build it, because the row that would get hidden is the cancellation row, and hiding the cancellation row is
exactly the behaviour this brief exists to end.

## Kalles contract

Kept verbatim: `<hdt-cart-drawer id data-count data-total-price>`, `<dialog id="CartDrawer" pos="right">`,
`button[aria-controls="CartDrawer"]`, `<form action="{{ routes.cart_url }}" method="POST">` +
`<button type="submit" name="checkout">`, `<hdt-line-item>`, `<hdt-quantity-wrapp>` with
`button[name="minus"] / input[name="updates[]"][data-index][data-max] / button[name="plus"]`, and
`<wrapp-remove-item-oncart data-index>`. On the cart page the stepper and the remove are plain links to
`/cart/change?line=n&quantity=q`, and the checkout button reaches its form through `form="CartPage-Form"` — so
quantity can be changed **and the page stays put** without JavaScript, which is the one thing the live page cannot do.
