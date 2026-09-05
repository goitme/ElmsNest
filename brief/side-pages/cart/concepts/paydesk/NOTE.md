# paydesk — «הקופה»

## The idea, in one sentence

The drawer opens **at the checkout, not at the list**: the total and the one button are the top of the panel,
sized as the decision; the basket is folded into a single honest line under them that opens in one tap when the
buyer wants proof — and the cart page is the exact inverse, everything unfolded, because that is what it is for.

## Why invert

`OWNER-NOTES` §6 makes the drawer the primary surface: it is what every add-to-cart opens. A buyer who has just
pressed **הוספה לסל** on the product page has already read the name, the variant and the price thirty seconds ago.
Making them scroll past a re-run of that page to find a 37 px button is the defect the inventory measured as
`dom=0.99` and `void=288–343`. Inverting removes both defects structurally rather than by tidying: **there is no
space above the subtotal to be empty, because the subtotal is the first thing in the panel.** The proof is one tap
away, still inside the drawer, for the buyer who wants it — offered, not imposed.

## Leak 1 — "is this the right one?"

Three answers, at three depths, so a buyer pays what attention they want to pay:

1. **Folded (default):** the summary line carries the two **product photographs** at 38 px, overlapping, beside
   `2 מנורות · 3 יחידות`. A photograph is the fastest possible "yes, that is the lamp" — and unlike a count it is
   never blank. `cart.item_count` and `cart.items.size` need no parsing and are always true.
2. **Unfolded (one tap, native `<details>`, no JS):** the full name on **two or three lines with no ellipsis**
   (`.li-name` has no `-webkit-line-clamp` and no `text-overflow` anywhere in the file), the chosen variant printed
   as a gold hairline-underlined chip — `צהוב חם`, `5 מ׳ / 20 נורות / צהוב` — the 84 px photograph, and a **line
   total in the serif at 20/24 px** (`339.80 ₪`) with `169.90 ₪ ליחידה` beneath it. The buyer never multiplies.
3. **The cart page:** all of the above, unfolded by default, with `סך הכל לשורה` labelled on every line.

The per-line light measure (`5 מ׳ / 20 נורות`) rides in the variant title where it is true; **there is no basket
headline of metres or bulbs.** `DERIVED-DATA.md` is right — metres exist in 5 of 27 products and none of the path
or wall lights; a headline that is blank on most real baskets is not an idea, and `1.5×1.5 מ׳` is an area. Removing
the headline from this concept removes nothing, because it never had one.

## Leak 2 — "what will this cost me and when does it come?"

Three of the four approved numbers sit **directly under the button**, verbatim, as a hairline ledger — never four
boxes, never a fourth column at 324 px:

| | |
|---|---|
| `0 ₪` | משלוח לנקודת איסוף — חינם. עד הבית 29.90 ₪. |
| `8–17 ימי עסקים` | לאספקה: 1–3 ימי טיפול ו־7–14 ימי משלוח. ייתכן משלוח ממחסן מחוץ לישראל. |
| `14 יום` | לביטול מקבלת המוצר, לפי חוק הגנת הצרכן. דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם. |

This is the moment they are worth most: a buyer paying a store they have never bought from, with a thumb over the
button. Today's drawer says **nothing** here (`terms=0/4`). The panel also states plainly what it does *not* know:
`כולל מיסים. את אופן המשלוח בוחרים בתשלום.` — no shipping cost is invented, because the cart cannot know it.

When the buyer opens the basket, the three terms hide (`.desk:has(+ .basket[open]) .terms`) and give their room to
the proof; closing the list brings them back. Pure CSS, both directions, no JS. Reassurance and proof are each one
tap from the other and never compete for the same 300 px.

## Leak 3 — "can I get out of this?"

`14 יום` is one of the three, in the same block, **with its fee sub-clause printed** (`דמי ביטול עד 5% או 100 ₪ —
הנמוך מביניהם`) rather than hidden behind a link. Stating the fee is the part that makes the promise credible; a
concept that prints "14 יום לביטול" and swallows the cost is doing PR. The cart page repeats it and adds the
disclaimer line the collection round licensed: `כאשר מידע אינו מאומת, איננו מציגים אותו כעובדה.`

## The fourth number, and where it goes

`1 תמונה` appears **only on the cart page**, as the mailto CTA (`לשלוח תמונה של המקום`, never "בוואטסאפ" —
`settings.whatsapp_number` is empty). It is a *pre-purchase* device: offering "send us a photo and we'll check the
fit" one line under **מעבר לתשלום** invites the decided buyer to un-decide. On `/cart` — the "let me look at this
properly" page — it is exactly right. Four terms on the page, three in the drawer, never a fifth anywhere.

## The nine measured defects, one by one

| inventory finding | what this concept does |
|---|---|
| 1 invisible scrim | scrim `rgba(2,3,6,.72)` + `blur(4px) saturate(.75)`, and the **panel is lighter than the page**: a `#101a2e → #05080f` gradient with a warm `rgba(255,211,148,.16)` glow at its top edge — a lit counter over a dark shop — plus a gold 1 px ring and a 90 px shadow |
| 2 two delete controls | **one** `<wrapp-remove-item-oncart>` per line, a 44 px text control `הסרה מהעגלה`; the stepper's minus stays a minus at quantity 1 |
| 3 name truncated | never truncated, 2–3 lines, `min-block-size:44px` on the link |
| 4 no line total | serif line total on every line, plus `× ליחידה` |
| 5 twin buttons | one filled pill. The only other control is a 13 px underlined `לעגלה המלאה` at the foot — `dom` collapses from 0.99 to roughly 0.25 by area |
| 6 37 px | 56 px (drawer) / 58 px (page); **every** control measures ≥ 44 px at 390, 360 and 320 (verified) |
| 7 `letter-spacing:3px` on Hebrew | zero letter-spacing anywhere in either file |
| 8 the 288–343 px hole | impossible: the panel is `block-size:auto`, so it is exactly as tall as its content and grows when the list opens |
| 9 nothing about delivery/cancellation | the three terms, above the fold, in both surfaces |

## The panel, and the desktop width

`min(90vw, 420px)` → **351 px at 390, 324 px at 360, 288 px at 320.** On desktop: **440 px**, not the current 340.
The width is set by the longest line the panel must never break badly — the product name at 14.5 px, which needs
about 26 characters beside an 84 px photograph — plus the `8–17 ימי עסקים` term, whose numeral column and text must
share one row. At 340 the name runs to four lines and the terms to three each; at 440 both settle at two. Wider
than 440 and it stops reading as a counter beside the shop and starts reading as a second page.

## No JS

The cart page is complete without JavaScript: `−` and `+` are plain links to `/cart/change?line=n&quantity=q±1`
(the fix `INVENTORY-DRAWER.md` prescribes — a quantity can be changed **without being forced into checkout**),
remove is the same kind of link, and checkout is `<button type="submit" name="checkout" form="CartPage-Form">`.
Inside the drawer — which does not exist without JS — the stepper keeps the contract's `<button name="minus">` /
`<input name="updates[]" data-index data-max>` / `<button name="plus">` verbatim. The fold/unfold is a native
`<details>`, so it works with JS off too, and `:has()` handles the terms swap without a line of script.
`hdt-cart-drawer[ref="hdt-cart"][section-id][data-count][data-total-price]`, `dialog#CartDrawer[ref="dialog"]
[pos="right"][scroll-lock]`, `button[ref="closeButton"][aria-controls]`, `hdt-line-item`, `hdt-quantity-wrapp`,
`wrapp-remove-item-oncart[data-index]` and the POST form are all present unchanged.

## The empty states

**Drawer:** `הקופה פתוחה, העגלה עוד ריקה.` — the desk admitting it has nothing to ring up — then the store's own
four places as a hairline ledger with outlined Frank Ruhl numerals 1–4 that fill with glow on hover, and
`כל 27 המוצרים ←`. No stock cart-with-an-✕ icon. Because the panel is auto-height it is ~420 px tall, not a 900 px
void with a button floating in it.

**Cart page:** the same sentence at h1 size, then the four places as **photographs** (the collection featured
images the homepage uses), dimmed to `brightness(.82)` and lighting on hover — the store's one motion idea,
applied where a cart page usually shows a shrug.

## What I dropped, and why

- **The basket light-measure headline** (`12 מטר · 70 נורות`). §5.1 kills it: blank on the two biggest families.
  Per-line only, from the variant the buyer actually chose.
- **"התשלום מאובטח…" / any trust line.** Written, shot, deleted. It is a fifth claim wearing the clothes of the
  four approved ones, and the brief permits four.
- **A second checkout button at the foot of the cart page.** One dominant control per surface; the desk is sticky
  on desktop and above the items on mobile, so the button is never more than a thumb away.
- **A "recently viewed" or "goes well with" row.** A cart is not a place to start a new argument (§1).
- **The `main-heading` band.** `<h1>ההזמנה שלך.</h1>` is visible, in the serif, on the page gradient.

## Numbers from the harness

```
drawer.html   desktop 2783 px   mobile 2615 px   horizontal-overflow=false   js-errors=0
cart.html     desktop 2246 px   mobile 3254 px   horizontal-overflow=false   js-errors=0
```
Both files carry three (drawer) / two (cart) full states in one document, so per-state the cart page is ~1 620 px
against today's 2 544 px for one state. Measured separately: **checkout top edge at y = 308 px at both 360×640 and
320×568** — inside the fold by 274 px and 202 px, against today's 932 px (below by 340 and 468). Drawer panel
width 324 px at 360 and 288 px at 320, no horizontal overflow at any of the four viewports, and **zero controls
under 44 px** at 360 and 320.

## Weakest point

On a phone, the unfolded list still scrolls once the basket passes three lines, and the terms are hidden while it
is open — so a buyer who wants to read the cancellation clause *and* stare at line four has to close the list to do
it. I judged that the right trade at 324 px (both are one tap apart, and the folded state is what 99 % of buyers
see), but it is a real compromise, and on a five-line basket the drawer becomes a scroller like any other.
