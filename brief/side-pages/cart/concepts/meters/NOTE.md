# `meters` — המידה

**The idea in one sentence:** the basket is measured in light, not in SKUs — the drawer opens with one derived,
checkable line (`5 מטר · 20 נורות · 2 מנורות`), every item shows the share it contributed to that line, and the
whole thing is drawn on the same rail the catalogue uses to ask "how much light does the place need?" —
bulbs *hang* on a wire because they have a length, lamps *stand* on the ground because they do not.

The real basket produces **`5 מטר · 20 נורות · 2 מנורות`**, and every digit is read out of `variant.title` ×
`quantity`: `5 מ׳ / 20 נורות / צהוב` × 1 gives the metres and the bulbs; `צהוב חם` × 2 carries no measure at all,
so the path lights are **counted as two lamps and never converted into metres**. The drawing says the same thing
twice: a lit 5 m span carrying exactly **twenty countable bulbs**, then the wire *stops* (a dashed break), then
two standing bollard marks on a bare ground line. You can count the picture against the number, and the number
against your own garden.

## Leak 1 — "is this the right one?"

- The **product name is never truncated**: it wraps to as many lines as it needs, at 14 px in the 324–351 px
  panel and 16 px in the 460 px desktop panel. `IP65` sits in its own LTR run.
- The variant (`5 מ׳ / 20 נורות / צהוב`, `צהוב חם`) sits directly under it in ink-2, one size down — not grey 13 px
  at the bottom of the row.
- Under the variant, a third line the theme has never had: **the line's contribution to the measure**, with a
  micro-glyph of the same rail — `תרומה למידה: 5 מטר · 20 נורות` / `2 מנורות · בלי מידת אורך`. For the garland this
  is literally the variant re-read as a quantity; for the path light it is the honest statement that there is
  nothing to measure. A buyer who picked the wrong length sees `5` where they wanted `9.5`.
- **A line total is printed whenever it can differ from the unit price**: the ×2 line shows
  `169.90 ₪ ליחידה` above `339.80 ₪`. The ×1 line prints one number, because printing `89.90 ₪ ליחידה` above
  `89.90 ₪` is the same number twice and teaches the eye to stop reading. That is the "provably unnecessary" case.
- **One bin per line.** The stepper's minus stays a minus and is disabled at quantity 1; removal is the single
  44 × 44 trash beside the stepper.

## Leak 2 — "what will this cost me and when does it come?"

- **Three of the four approved numbers are in the drawer**, verbatim, as a hairline ledger directly above the
  subtotal — `0 ₪`, `8–17 ימי עסקים`, `14 יום`, each with its headline and, where it costs money, its sub. They are
  the block that fills the space the old drawer wasted, so the answer arrives *before* the button, not after it.
- The subtotal note names the two real shipping numbers instead of deferring everything:
  `כולל מע״מ. דמי המשלוח נבחרים ומחושבים בתשלום.` — and the cart page's summary spells out
  `0 ₪ לנקודת איסוף, 29.90 ₪ עד הבית`.
- The cart page carries **all four** as the 2-column hairline ledger of the collection spec (never four boxes),
  with the `mailto:` photo CTA and `כאשר מידע אינו מאומת, איננו מציגים אותו כעובדה.`
- No progress bar, no threshold, no estimator. `0 ₪` is a *term*, not a target to be chased.

## Leak 3 — "can I get out of this?"

- `14 יום` is the third row of the drawer's ledger, sitting immediately above the checkout button, and it carries
  the part that costs the buyer money — `דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם.` — rather than only the
  reassuring half.
- On the cart page it is repeated in the ledger **and** in one line under the checkout button
  (`הביטול אפשרי 14 יום מקבלת המוצר.`), so it is inside the fold at 360 × 640 with the button.

## The three defects of the old drawer, measured against

| defect (INVENTORY §"nine findings") | here |
|---|---|
| invisible scrim | panel is **sky-3 `#070b15` on a `#020306` page**, page dimmed to `rgba(2,3,6,.66)` **+ 6 px blur**, gold hairline, and a 90 px black cast — the panel is lighter than the page it covers |
| two bins | one, 44 × 44; minus disabled at qty 1 |
| name truncated | wraps, never clipped |
| no line total | printed at qty > 1 |
| two identical buttons, weak one on top | one glow pill `מעבר לתשלום` at **52 px** (56 px on the cart page); `לעגלה המלאה` is an underlined 44 px text link *below* it |
| 37 px controls | every control ≥ 44 px (stepper, input, trash, close, links) |
| `letter-spacing:3px` on Hebrew | `letter-spacing:0` on `body` and on every button; no tracking anywhere |
| 288–343 px hole above the subtotal | the body is a flex column whose **terms ledger takes `margin-block-start:auto`** — leftover height falls as breathing room *under the goods*, never as a void above the money. At 390 × 844 the body measures 610 px into 610 px of space: zero slack |
| nothing about delivery/cost/cancellation | three numbers, verbatim |
| stock grey cart-with-an-✕ | see below |

## The cart page's one number

Today the checkout button's top edge is at **y = 932** at both 390 × 844 and 360 × 640. Here it is at
**y = 410 at 360 × 640**, y = 413 at 390 × 844, y = 430 at 320 × 568 — inside the fold at all three, because the
page opens with a summary block (measure → subtotal → the button) and the goods follow it. 56 px tall, the only
filled control on the page.

**Works with JavaScript off.** One `<form action="/cart" method="post">` wraps everything: `updates[]` number
inputs plus a `עדכון כמויות` submit, `±` are real `/cart/change?line=n&quantity=m` links, removal is the same,
and `button[name="checkout"]` is a native submit inside the same form. Nothing on the page needs a script.

## The empty states

Not an error screen and not a stock icon. The measure is still the subject: a **bare wire** across the panel and
`חוט ריק — 0 מטר · 0 נורות · 0 מנורות.` under `עדיין לא נדלק כלום.` Then the store's own four places
(שביל · קיר · גינה · מרפסת) as a hairline list that **flexes to fill the panel at any height** — so the empty
drawer has no void either — each row naming *the unit that place is measured in* (`נמדד במטרים ובמנורות`,
`נמדד במנורות`, …), which is this concept applied where there is nothing to count yet. Below them the fourth
approved number, `1 תמונה`, with the `mailto:` CTA — the right offer for someone with an empty basket. One
primary control: `לכל 27 המוצרים`.

## Decisions and justifications

- **Desktop panel width 460 px** (today: 340 px = 24 % of 1440). 460 px gives ~426 px of text column: the long
  product name sets on two lines at 16 px, the rail's twenty bulbs are individually countable, and the terms
  ledger keeps numeral and headline on one row. It is still only 32 % of the viewport, so the page behind stays
  legibly a page. It also keeps the *same single-column composition* as the phone — one layout, no reflow, one
  section to maintain.
- **Which of the four numbers waits.** `1 תמונה` is a *pre-purchase* step: it asks the buyer to stop and send a
  photo before ordering. In the drawer the buyer has already chosen and is one tap from paying; putting it there
  either gets ignored or actively pulls them out of the sale. It appears on the cart page (the "let me look at
  this properly" surface) and in **both** empty states, where it is exactly the right next move.
- **What the rail refuses.** It never invents a metre. The `refuse` note says so in words on both surfaces:
  *"למנורת השביל אין אורך — היא נספרת, לא נמדדת"* / on the cart page, *"אנחנו לא משלימים מספר שאינו כתוב."*
  A basket of only wall lights would render `2 מנורות` with a bare span and no bulbs at all — the drawing
  degrades to nothing rather than to a guess.
- **Dropped:** the `main-heading` band (the `<h1>` is visible type now); the three bordered boxes below the
  button; the second glow button; the per-line dashed `מחיר / כמות / סך הכל` label rows on mobile (the numbers are
  labelled once by position instead); and any wording about free-shipping thresholds, stock, dates or savings.
- **Kalles contract kept verbatim:** `<hdt-cart-drawer … ref="hdt-cart" section-id data-count data-total-price>`,
  `<dialog id="CartDrawer" ref="dialog" pos="right" scroll-lock>`, `<button ref="closeButton" aria-controls>`,
  `<form action="/cart" method="POST">` + `<button type="submit" name="checkout">`, `<hdt-line-item>`,
  `<hdt-quantity-wrapp>` with `button[name=minus]` / `input[name="updates[]"][data-index][data-max]` /
  `button[name=plus]`, and `<wrapp-remove-item-oncart data-index>`.

## Weakest point

The measure is only as interesting as the basket. This basket has one measurable line, so the rail carries one lit
span and two standing marks — a basket of three wall lights would print `3 מנורות` and draw three marks on a bare
wire, which is honest but visually thin, and a single-item basket makes the whole block feel like a lot of
apparatus for one number. I chose not to pad it (no invented scale, no "typical garden" reference), so on the
smallest baskets the drawer's top block earns its space with type alone.

## Shot

`node brief/shot.js …/drawer.html …/shot` → desktop `height=1801px horizontal-overflow=false js-errors=0`,
mobile `height=1689px horizontal-overflow=false js-errors=0`.
`node brief/shot.js …/cart.html …/shot-cart` → desktop `height=2666px horizontal-overflow=false js-errors=0`,
mobile `height=4393px horizontal-overflow=false js-errors=0`.
(Both files are two full screens plus an `<hr>`; the drawer stages are `100vh` each.)
