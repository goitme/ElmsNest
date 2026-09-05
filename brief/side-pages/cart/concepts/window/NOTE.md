# `window` — החלון

**The idea in one sentence:** the cart is where the light comes on — the page behind genuinely darkens and the
drawer opens as a raised, lit surface whose brightness rises from the checkout button the way a lamp is the
brightest point in every photograph this store sells, so at 324 px material and light carry the hierarchy that
layout cannot.

The defect the inventory measured is not a spacing defect. `dialog` is `rgb(2,3,6)` on a page that is
`rgb(2,3,6)`, separated by one gold hairline; the backdrop is arithmetically real and visually nil (finding 1).
Every other fault — the twin buttons, the 37 px controls, the 288–343 px void — is a *composition* fault stacked on
top of a *material* fault. This concept fixes the material one first and lets it do the rest of the work.

## The three physical facts the concept is built from

1. **The page is pushed down, not tinted.** The scrim is `rgba(2,3,6,.62)` **plus**
   `backdrop-filter: blur(5px) brightness(.55) saturate(.65)`. Brightness reduction works on black; alpha does not.
   In `shot-desktop-fold.png` the catalogue behind is still legible *as a page* — it has not been deleted, it has
   been turned down — and the panel is unmistakably a separate, nearer object.
2. **The panel is lifted, not recoloured.** Its ground is a navy lift (`#0f182b → #0d1729`, between sky-3 and
   sky-2) with three warm radials laid over it, the largest anchored at `50% 103%` — i.e. *under the checkout
   button*. There is no brown and no cream anywhere; the warmth is light falling on a night surface, which is
   exactly what the product photographs are. The edge facing the page is a 1 px gradient hairline that brightens
   toward the sill: the window frame.
3. **Each line is a small lit plate.** A faint `rgba(244,238,227,.055 → .014)` lift, a warm hairline above, and a
   radial `mix-blend-mode: screen` halo bled 30 px around the photograph, so the lamp in the picture appears to
   light its own row. The photographs carry `brightness(1.07)`: inside the window, things are on.

## Leak 1 — "is this the right one?"

- **The full product name, never truncated.** Verified programmatically at 390, 360 and 320:
  `trunc=[false,false]`. The title wraps to three lines at 324 px and that is correct — the name is the only proof
  the buyer picked the right lamp, and three lines of 15 px Heebo cost 59 px, which the drawer can afford once the
  288 px void is gone.
- **The variant is promoted to gold**, 13 px, directly under the name: `צהוב חם` / `5 מ׳ / 20 נורות / צהוב`. It is
  the chosen fact, so it is coloured like the other facts in this store, not greyed like metadata.
- **A line total exists, and it is the biggest number on the row** — `339.80 ₪` in Frank Ruhl Libre glow, with
  `169.90 ₪ ליחידה` in mute beneath it. The arithmetic is shown, not left to the buyer (finding 4).
- **One remove control, not two** (finding 2): `<wrapp-remove-item-oncart>` renders a single 44 px text link,
  `הסרה מהעגלה`. The stepper's minus stays a minus at quantity 1 and the second bin is deleted.
- **I refuse the basket headline.** `DERIVED-DATA.md` is decisive: metres appear in 5 variant titles of 27, bulb
  counts in 7. A headline that is blank on most real baskets is not an idea. I also dropped the *per-line* restatement
  (`5 מטר · 20 נורות`) after seeing it rendered: it copies the variant line that sits 4 px above it. The variant
  title already **is** the light measure where a light measure exists, which is the honest version of the same claim
  and costs nothing on a wall light. What plugs leak 1 here is name + variant + line total, all three visible without
  scrolling.

## Leak 2 — "what will this cost me and when does it come?"

Three of the four approved numbers are printed **verbatim, headline and sub, inside the drawer**, as a hairline
ledger between the last line and the sill — which is precisely where the 288–343 px hole used to be. The hole is not
closed by shrinking things; it is *occupied* by the answer to the question the buyer is asking at that moment.

`0 ₪` משלוח לנקודת איסוף — חינם. / עד הבית 29.90 ₪. · `8–17 ימי עסקים` לאספקה… / ייתכן משלוח ממחסן מחוץ לישראל. ·
`14 יום` לביטול… / דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם.

The ledger is the flex-grower (`justify-content: space-evenly`), so on a two-line basket the leftover space
distributes *between hairlines as air*, not as one dead rectangle. The subtotal then sits on a lit sill:
`429.70 ₪` at 33 px with a `text-shadow` halo, and one honest sentence, `כולל מיסים. דרך המשלוח נבחרת בעמוד התשלום.`
No estimator, no threshold, no progress bar.

**The fourth number waits.** `1 תמונה` is not a payment fact; it belongs *before* the decision, not in the second
before paying. It appears in the drawer's **empty** state and in full on the cart page. Four numbers do not fit in
324 px as four numbers; three of them are what a paying buyer needs.

## Leak 3 — "can I get out of this?"

`14 יום` is in the drawer, third row, with its cancellation-fee sub — the number the buyer of a store with one test
order actually needs, printed at the moment of maximum doubt rather than in a box below the button. On the cart page
it is one of four numbers in a two-column hairline ledger (collection §4.6 shape, never four boxes), followed by
`כאשר מידע אינו מאומת, איננו מציגים אותו כעובדה` and an explicit refusal:
*עלות המשלוח בפועל נקבעת בעמוד התשלום, ולכן היא אינה מוצגת כאן כמספר סופי.*

## The single dominant control

The checkout button is a 56–58 px glow pill with a three-layer shadow (`1 px` ring, 46 px lift, 110 px ember bloom)
carrying its own amount: `לתשלום · 429.70 ₪`. Nothing else on either screen is filled. `צפה בעגלת הקניות` — the old
twin, which was *above* checkout and identically sized (`dom = 0.99`) — is demoted to a 13 px underlined text link
(`לעמוד העגלה`) sharing a 44 px row with the tax note. It is still reachable and it is no longer a rival.
`letter-spacing` is `0` everywhere; no Hebrew is tracked.

## The cart page

Same window, full size. **The sill comes first in the source on a phone** and becomes a sticky column at 1440.
Measured: the checkout button's top edge is at **y = 324 px at both 360×640 and 390×844** — the round-2 contract was
"stay inside the fold at 360×640"; the baseline was y = 932, i.e. 292 px below it. The document is **1 800 px** for
two products against the current 2 544 px.

Putting the amount and the button above the lines is a deliberate inversion: the decision was made two clicks ago,
and everything a buyer comes to `/cart` to *check* — names, variants, line totals, quantities — is directly beneath,
one thumb-length away, with a `מה שכדאי לדעת` link in the sill for the terms. There is exactly one checkout button
on the page; a second one at the bottom would rebuild the defect I am removing.

**JS off.** `−` and `+` are `<a href="/cart/change?line=N&quantity=q±1">` on the cart page, as
`INVENTORY-DRAWER.md` recommends — the quantity changes and the buyer stays on the page, which the live cart cannot
do. `הסרה` is the same kind of link. `<input name="updates[]">` survives for Kalles' JS to enhance in place, and
`button[name="checkout"]` carries `form="CartPage-Form"`, so the native POST still works. The drawer keeps
`<button name="minus">` / `name="plus"` verbatim, because the drawer does not exist without JS and the theme's
handlers read those names. The whole Kalles contract survives: `<hdt-cart-drawer … data-count data-total-price>`,
`<dialog id="CartDrawer" ref="dialog" pos="right" scroll-lock>`, `ref="closeButton"`, `<hdt-line-item>`,
`<hdt-quantity-wrapp>`, `<wrapp-remove-item-oncart data-index>`.

## The empty state

Not an error screen and not a stock icon. It is **the window with nothing in it**: a CSS-drawn lit pane with a
mullion cross and a real falloff — the same shape as the panel it lives in, four panes wide.
*האור כבר דולק. / חסר רק המקום.* Then the store's own four places as 50 px hairline rows
(שביל · קיר · גינה · מרפסת), then the number that belongs here and nowhere else — `1 תמונה`, with the `mailto:`
photo CTA (never the word בוואטסאפ) — anchored to the bottom of the pane so the composition has a floor. The sill
still holds the brightest control: `לכל 27 המוצרים`.

## Desktop width: 420 px, and why

Today's drawer is 340 px at 1440 — the same crushed measure as the phone, on a screen with 1 100 px to spare, which
is why the desktop void is the worst of the four (343 px). 420 px gives a 92 px photograph and a ~272 px text
column: about 36 Hebrew characters per line, which is the comfortable measure and drops the product name from three
lines to two. It stops there deliberately. Wider and the ledger's `auto 1fr` grid stretches into a table, and the
1 020 px of darkened page left over is what makes the panel read as a *window* rather than as a sidebar that has
taken over the screen. The concept needs the dark page to be visible to work.

## What I dropped, and why

- **The derived basket headline** (`5 מטר · 20 נורות · 2 מנורות`) — §5.1 forbids it as a headline and I agree with
  the reasoning; on this catalogue it is blank or misleading more often than it is useful.
- **The per-line derived measure** — it duplicated the variant title verbatim. Removed after seeing it rendered.
- **The `1 תמונה` number in the full drawer** — kept for the empty drawer and the cart page.
- **The `main-heading` band, the three dashed label rows per line, and the three bordered boxes below checkout** —
  the boxes' content survives as the ledger; the band and the labels do not survive at all.
- **A second checkout button on the cart page**, and any `לפני שממשיכים לתשלום` heavy block.

## The weakest point

The concept is carried by `backdrop-filter`. Where it is unsupported (older Firefox with the flag off, some
in-app browsers), the scrim degrades to `rgba(2,3,6,.62)` — a real dim, but the fixed-alpha dim that the inventory
correctly called invisible on a black page. The panel still separates, because it is *lighter* than the page
rather than the same colour, and it keeps its lit frame edge and its outward shadow; but roughly a third of the
separation is gone. The honest mitigation, if this ships: raise the scrim's opacity in an
`@supports not (backdrop-filter: blur(1px))` block, and accept that the fallback reads as a heavier curtain rather
than a dimmed room.

Second weakest: at 320 px the panel is 288 px and the product name runs to four lines. Nothing breaks
(`overflow=false`, `under44=0`), but the plate is tall, and a five-line basket will scroll the terms ledger out of
view. The sill is pinned, so the subtotal and the button never move — but on a very long basket the numbers become
a scroll rather than a sight.

## Measured

```
drawer   1440×900  height=1802  horizontal-overflow=false  js-errors=0
drawer    390×844  height=1690  horizontal-overflow=false  js-errors=0
cart     1440×900  height=2571  horizontal-overflow=false  js-errors=0
cart      390×844  height=3601  horizontal-overflow=false  js-errors=0
(both stages per file; one viewport each, plus the <hr>)

drawer  360×640  panel=324  checkout 56 px  under44=0  trunc=[false,false]  overflow=false
drawer  320×568  panel=288  checkout 56 px  under44=0  trunc=[false,false]  overflow=false
cart    360×640  checkout top y=324 (INSIDE the fold; baseline y=932)  h=58  under44=0  overflow=false
cart    320×568  checkout top y=324                                    h=58  under44=0  overflow=false
```
