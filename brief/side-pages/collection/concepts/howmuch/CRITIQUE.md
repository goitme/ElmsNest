# howmuch · «כמה אור» — critique

## 1. The one idea, in a sentence

**The collection is a ruler, not a grid: every product is laid on the axis the buyer actually thinks in — metres of
string, points of light along a path, shekels per point of light — at its real values, and choosing means moving along
that axis until the prices under your number appear.**

The device is the same drawn instrument on all three pages, with the unit swapped: a hairline scale with the products'
real variant values marked on it as dots, a glowing segment that lights left-to-right when the row arrives, and a
vertical cursor that lands on the number you picked. It is the product page's variant ledger
(`pdp/WINNING-SPEC.md` §4.4 — the rail of `5 · 6.5 · 9.5 · 11 · 13 · 22 מ׳` at the bottom of the PDP fold) promoted to
the level of the whole collection. A shopper who came from the PDP recognises it instantly; a shopper who goes to the
PDP next finds it again, one product deep.

Why only a lighting store can do this: the axes are not invented facets, they are the option axes Shopify already
holds — `אורך ומספר נורות`, `כמות`, `גודל`. No wattage/IP/zone data exists (AUDIT §162), so no honest facet toolbar can
exist; but "how much light" is *already* in the data, once per product, with a price attached to every value.

## 2. How a visitor narrows the set

**7 lamps · `/collections/גרילנדות-ותאורה-דקורטיבית` (`index.html`).**
The question in the h1 is «כמה מטרים של אור?». Five of the seven are measured in metres, so they are on one rail from
0 to 34 m; the two that are not (fireflies on stalks, birch branches) are pulled out into their own diptych with the
photographs, so no row lies about what it is. The visitor taps a metre stop (3 · 6 · 10 · 15 · 22 · 30). At **10 מ׳**
the numeral turns to **4**, the cursor drops at 10 m, and each row collapses from a range to one real answer:
rope `12 מ׳ · 100 נורות · 99.90 ₪`, crystal `11 מ׳ · 60 נורות · 109.90 ₪`, globe `10 מ׳ · 80 נורות · 169.90 ₪`,
net `12×2 מ׳ · 780 LED · 469.90 ₪`; the Edison garland dims and says **«האורך המרבי: 8 מ׳»** — it is not hidden, it is
answered. 7 → 4 comparable offers with exact prices, in one tap, and the second axis (bulbs per metre) is right there
to break the tie.

**8 lamps · `/collections/תאורת-שביל-סולארית` (`path.html`).**
The unit becomes points of light. Five sets sit on a 1→12 rail; the three lamps sold as a single unit are lifted into
their own band with add-to-cart forms, because "one" is not a range. The 14× price span is not smoothed over, it is
*explained*: every row carries the price **per point** at the chosen count. At **4 נקודות** the five sets read
149.90 / 159.90 / 329.90 / 389.90 / 549.90 ₪ — same coverage, 3.7× spread — and per point 37.48 / 39.98 / 54.98 /
97.48 / 137.48 ₪. The closing screen is that column alone, sorted, from 18.74 ₪ to 124.99 ₪ per point. The 999.90 ₪ set
stops being a shock and becomes a choice.

**27 lamps · `/collections/all` (`all.html`).**
The catalogue admits it has three units, not one, and says so in the first screen as three numerals — **17 · 5 · 5** —
which are also the jump links. Chapter 01 (17 single lamps) uses price itself as the axis: each row's bar is its
starting price, so the whole chapter is a legible staircase from 89.90 ₪ to 219.90 ₪, with the dashed tail showing how
far the bigger version goes (the floodlight's 199.90 → 499.90 is visible as a dotted line, not as a surprise at
checkout); the budget stops (עד 120 / 150 / 180 ₪) narrow 17 → 5 / 7 / 12. Chapters 02 and 03 are the units and the
metres rails, compressed. **There is no pagination**, and that is the argument, not an oversight: 12-per-page would cut
a ruler in half and destroy the only comparison the page exists to enable. 27 rows on one document is ~5,500 px on
desktop — shorter than the current three-page catalogue's 2,531 × 3.

## 3. Where it sells hardest

- **Everything is priced, always.** No card shows only «89.90 ₪ - 179.90 ₪». Either the honest range rule
  (`מ־ / min–max / single`, §3.5) or, once a number is chosen, the one price that answers it.
- **The 8 single-variant products add to cart from the collection page** (fireflies here, three path lamps there, eight
  rows in chapter 01), which is the whole point of having them.
- **The per-point column** on `path.html` is the strongest commercial idea in the three pages: it makes the big sets
  arguable instead of expensive, and it is arithmetic on real prices, not a claim.
- **The mobile fold** on all three pages carries: the place (gold kicker), the question, the stops, and at least one
  real product with a real price — measured, not hoped for.

## 4. Where it sells weakest — and the honest constraints behind it

- **The rail has almost no photography.** That is partly a decision (a chart of light is not a photo grid) and partly
  the ledger: on `/collections/תאורת-שביל-סולארית` only **2 of 8** products own a photograph free of baked-in Hebrew
  marketing text, and `led-globe-string-lights` and `modern-led-bollard-light-5w-ip65` have **none at all** across
  indexes 1–3 (index 0 is barred for both). A photo-led concept cannot be built on this catalogue without lying about
  which picture belongs to which product. Where a photograph exists and is clean it is used large (the diptych, the
  three solo lamps, the closing bands); where it does not, the bollard gets a drawn light-glyph labelled
  «איור · אין תצלום נקי». Honest, but a shopper who buys with their eyes gets less here than on the PDP.
- **The wall collection is the weak case for the idea.** Its axis is 6W/12W and up/down — a two-value scale, too short
  to draw. It would run as chapter 01 does (price as the axis) with the wattage printed as a fact, which is correct but
  is the least exciting of the four pages. That page is not in this round and I have not proved it.
- **`עד 120 ₪` filters on the starting price**, so a product whose big version costs 499.90 ₪ can appear under it. The
  page says so («הסינון לפי מחיר ההתחלה של הדגם») and draws the dashed tail, but a footnote is a weaker answer than a
  mechanism.
- **The 4-metre answer is "the smallest option that covers you", not "the best one"** — a genuinely useful default, but
  a shopper who wants to overshoot has to open the product page to see the longer variants' prices.

## 5. Feasibility (what the build actually has to do)

- **The narrowing is pure CSS.** N radios + `~` sibling rules; no JavaScript, no AJAX, no facet drawer. With JS off the
  page is fully usable and every lamp is lit. The stop set is a section setting with a fixed count, so the state rules
  are static CSS with no Liquid inside `{% stylesheet %}` (CONTRACT). Each row's `no-<stop>` classes and its per-stop
  readouts are one `for` loop over the first option axis in Liquid.
- **The values are Liquid, not typed.** Lengths/counts come from `option.values` (`"11 מ׳ / 60 נורות"` → split), prices
  from the matching `variant.price`; dot positions are `value | divided_by: scale | times: 100`. Counts
  (`7`, `27`, `172`) are `collection.products_count` / `collection.all_variants`.
- **Ordering is server-side**: plain `?sort_by=` links, no JS, shareable. The default order is
  `collection.products` (the merchant's manual order), because Liquid cannot sort by a parsed option value — that is
  the one thing the row order cannot promise, and the sort links cover it.
- **The card is the PDP's card (§4.8), extended, not forked**: kicker = place + approved suits phrase, title in Heebo
  with `unicode-bidi:isolate`, price via `elmsnest-v2-price`, single variant → `<form>` ATC, else a ghost link. The rail
  row is that card unrolled onto a line; the diptych and the three solo lamps are the card in its normal shape, at
  staggered widths (340 / 236 / 290 px, aspects 1/1.02 · 1/1.38 · 1/.86).
- `paginate collection.products by 27` on `/all`; the four real collections never paginate.

## 6. What one more day would buy

1. **A second axis on the rail: colour temperature.** Six of the 27 carry `גוון אור` 3000K/6000K; a warm→cool tint on
   the row's glow (not a swatch row — §3.6 bans that) would make the rail say two things at once.
2. **A "מה נכנס לתמונה" band on `index.html`** — the crystal/Edison/rope photographs at the three real lengths, so the
   metres stop being abstract for the shopper who cannot picture 22 m.
3. **Wall proof.** Build `/collections/solar-wall-lights` in this system to check that a two-value axis does not break
   the rail — the honest answer is probably that wall runs on the price axis with the wattage as a fact.
4. **A `?len=` URL parameter** carried by the section as a `section.settings` default plus a tiny progressive-enhancement
   script, so a chosen length is shareable and survives a reload (today the state is a radio, which is not).
5. **A real empty state** for `עד 120 ₪` combinations that could return one row, with the nearest answer offered.
