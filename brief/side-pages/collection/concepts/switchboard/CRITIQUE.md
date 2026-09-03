# THE SWITCHBOARD — לוח המתגים · critique

Files: `index.html` (גרילנדות ותאורה דקורטיבית, 7 · 105 · 89.90–469.90) · `path.html` (תאורת שביל, עמוד וגינה,
8 · 69.90–999.90) · `all.html` (הקטלוג, 27 · 172 · 69.90–999.90) · shared `switchboard.css` / `switchboard.js`.
Renders: `shot-*`, `shot-path-*`, `shot-all-*` (desktop 1440 / mobile 390, fold + full page).

## 1. The one idea, in a sentence

The collection is a **board of lamps you can switch on**: a small bank of honest toggles built only from data the
catalogue actually holds (the place, the power source, the maximum length, the entry price) sits above the grid, and
flipping one lights the lamps that match and leaves the rest **dark on the same page** — nothing is hidden, nothing is
removed, narrowing *is* switching lights on, and the state lives in the URL so it works server-side without JS.

## 2. How a visitor narrows 7 / 8 / 27 lamps to a choice

**7 (index.html).** The decor collection has no real price spread — every entry price sits between 89.90 and 139.90 —
so a price switch there would be theatre. The two axes its data *does* support become the board: **מקור מתח**
(סולארי 4 · USB או סוללות 1 · חשמל 220V 1 · **לא צוין 1**) and **אורך מרבי** (עד 8 מ׳ 1 · 9–15 מ׳ 2 · מעל 15 מ׳ 2 ·
פריט בודד 2). A visitor wrapping a 12 m pergola flips "מעל 15 מ׳" and two lamps stay lit out of seven; a visitor with
no outdoor socket flips "סולארי" and four stay lit. Two switches from different banks intersect. Every switch carries a
**pip row** — one pip per lamp on the board, lit where it matches — so the whole mapping is legible in a still, before
anything is clicked. `לא צוין` is a real switch with a real count: the birch branches state no power source anywhere in
the catalogue, and the page says so rather than guessing.

**8 (path.html).** Here the story is the 14× span, so the panel *is* a **price ladder**: eight rungs, each a real
product with a linear bar — solid to its entry price, hairline onward to its highest price — grouped into three banks
whose headers are the switches (עד 150 ₪ ⟨3⟩ · 150–350 ₪ ⟨4⟩ · מעל 350 ₪ ⟨1⟩). A second bank, **כמות**, splits
"אפשר יחידה אחת" ⟨4⟩ from "נמכר בסט" ⟨5⟩ — one product is honestly in both, and the page says why. So the visitor sees
every price in the collection in one screen, picks a band, and the photo board below darkens to match. The
`פי ארבע־עשרה, וזאת הסיבה` diptych then answers the question the ladder raises, with both full price ledgers.

**27 (all.html).** Two banks: **מקום** (8 · 6 · 6 · 7 — the four real collections) and **מחיר כניסה**
(עד 120 ₪ ⟨10⟩ · 121–250 ₪ ⟨16⟩ · מעל 250 ₪ ⟨1⟩). Because the board is composed as four place-boards in order, each
place switch's 27-pip row reads as a contiguous block — the catalogue's whole structure is visible as a picture in the
first screen. "קיר וחזית" + "עד 120 ₪" together leave two lamps lit out of twenty-seven, on one page, with one address.

**Ordering.** Not a toolbar: one hairline line inside the panel — `כפי שסודר בחנות · מחיר עולה · מחיר יורד` — plain
`?sort_by=` links that reorder the board and re-stamp the position rhythm (Liquid does the same with `forloop.index`).

## 3. Where it sells hardest

- Every fold on both viewports carries the place, a real product, a real ₪ price and a route to buy: index shows lamp
  01 (crystal balls, מ־89.90 ₪, לבחירת אורך); path shows four named products with prices in the ladder; all shows the
  two ends of the catalogue (מ־69.90 ₪ · מ־549.90 ₪) plus the four place switches.
- Eight single-variant products across the three pages add to cart **from the board** (`הוספה לסל`); every multi-variant
  card links with the honest verb for its own axis (לבחירת אורך / גודל / כמות / גוון / עוצמה / צבע / דגם).
- The `מ־` price never stands alone: each card prints the axis and its real prices under the title
  (`2 יחידות 219.90 · 4 יחידות 389.90 · 6 יחידות 529.90 ₪`), and index's full-bleed section opens lamp 05's six sizes
  and six prices before you enter the product.
- A dark lamp keeps its title and its price and stays clickable — switching off never destroys the shop.

## 4. Where it sells weakest — and the honest problems

1. **The dark state is a promise the still cannot keep.** With no switch flipped the whole board is lit, which is the
   right arrival state (and the no-JS state), so a judge reading only a screenshot sees the pips, not the darkness. The
   pip rows are my mitigation; a hover preview and the live toggles are the real thing. If I could ship one more still
   it would be `index.html?on=pwr-solar`.
2. **Fifteen of twenty-seven products have no clean photograph at any index** — every alternate is a marketing creative
   with baked-in Hebrew. I turned that into a system (every tile is a hard zoom/origin crop into the one clean patch),
   but three tiles are tighter and softer than I would like: `solar-security-light-100-led` (a silhouette, wordless
   overlay icons cropped out at z 3.9), `solar-garden-spotlight-52-led` (a product on cream), `led-globe-string-lights`
   (a lifestyle interior, a book spine in frame). This is a photography problem the page cannot solve alone.
3. **The board's rhythm is looser on `all.html`** than on the two collection pages: to keep the 27-tile page inside a
   readable height I used three-per-row bands with unequal spans, which is correct but less surprising than index's
   3/5/8/12 rhythm.
4. **Two switches inside one bank are OR, two banks are AND** — true, useful, and one sentence of explanation. One
   sentence is one sentence too many for some visitors.
5. **`אפשר יחידה אחת` / `נמכר בסט` overlap** (`warm-solar-step-deck-lights` is in both, so 4 + 5 > 8). Honest, labelled,
   and still the kind of arithmetic a shopper may read twice.

## 5. Feasibility

One section, `elmsnest-collection`, replaces `main-collection.liquid`. Switch banks are **schema blocks**: a group label
plus 2–4 switches, each with a name, a count, and a rule expressed as a product list or a price range — so the merchant
composes the board per collection instead of the theme inventing facets Shopify does not have. The state is
`request.query` (`?on=a,b`), resolved in Liquid to a `data-off` attribute on the non-matching cards: **the page works
with JS disabled and the switches are plain links.** `paginate collection.products by 40` — 27 products never split, and
`all.html` says so in words instead of faking a control. Sorting is plain `?sort_by=` links. The card is the shipped
`elmsnest-v2-pdp-card` with two additions that also improve the PDP related row: the axis caption line and the `כבויה`
marker. Images resolve through `elmsnest-v2-pdp-image.liquid` with two extra numbers per slot (`zoom`, `origin`) — the
same never-index-0 guard, plus the crop the ledger already does with `object-position`.

## 6. What I would fix with one more day

- Ship a second still per page with a switch already flipped, and add a 400 ms "bank sweep" so flipping reads as current
  travelling down the board rather than a state change.
- Re-crop the three weak photographs against the full-resolution originals, and write the merchant a one-page brief for
  the fifteen products that need one clean night photograph each.
- Give `all.html` the index rhythm back by letting each place-board choose its own span pattern from three presets, and
  add a sticky one-line board meter (`דולקות 4 מתוך 27 · הדליקו הכל`) once the panel scrolls away.
- Add keyboard-only affordance to the pips (they are `aria-hidden` decoration today; the counts carry the meaning).
