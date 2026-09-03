# «המקום ממשיך» — places · self-critique

Files: `index.html` (גרילנדות ותאורה דקורטיבית, 7/105/89.90–469.90) · `path.html` (תאורת שביל, עמוד וגינה,
8/22/69.90–999.90) · `all.html` (הקטלוג, 27/172/69.90–999.90).
Renders: `shot-*`, `shot-path-*`, `shot-all-*`. Heights (desktop/mobile CSS px):
index 9175 / 10364 · path 10128 / 11583 · all 6335 / 9507. No horizontal overflow, no JS errors on any render.

## 1. The one idea, in a sentence

**The homepage's «ארבעה מקומות» section opens: the visitor is still standing in the place they chose, and before
the page shows a single product it asks — and answers — the one question that place is actually bought by
(«כמה מטר צריך לכסות?» for the terrace, «כמה נקודות אור צריך השביל?» for the path) — then draws all the products
of that place as spans on a single measured ruler, sorted by their answer.**

The ruler is the thing only a lighting store can do. Nothing else in the catalogue is comparable across products
— but *reach* is: metres of run, or points of light. Both numbers already exist in Shopify, as the first option
axis of every product, with a price per value. The page turns that axis into geometry.

## 2. How a visitor narrows 7 / 8 / 27 lamps

**7 (decor).** The place's question is «כמה מטר צריך לכסות?». Four hairline rows answer it directly — *up to 6 m /
6–12 m / 13 m and over / not measured in metres* — and each row names the cheapest product that actually reaches
that length with its exact variant and price («כדורי קריסטל · 5 מ׳ / 20 נורות — 89.90 ₪»). Two taps: measure,
then read one line. The rows are plain anchors, so they work with JS off. Below them the ruler (0–32 m) shows all
seven at once with a derived, labelled ₪/metre; the products then arrive ordered by the reach they max out at
(8 m → 12 m → 22 m → 32 m → not-in-metres), each with the full length↔price ladder from its real option axis.

**8 (path).** The same system, different unit: the axis is **נקודות אור** (1–12) and the derived number is
**₪ לנקודת אור** — which is the only honest way to explain a 14× price span. The dedicated «פי ארבעה־עשר» screen
puts the store's cheapest (69.90 ₪ = one lamp = 69.90 ₪/point), its most expensive (999.90 ₪ = eight lamps =
124.99 ₪/point) and its cheapest per point (149.90 ₪ = eight units = 18.74 ₪/point) side by side. After that
screen the 999.90 ₪ set is no longer frightening and the 149.90 ₪ set is no longer invisible.

**27 (all).** The house from outside: four doors, each with its numeral, place name, its own question, its count,
its span and one named product with a price — then the whole catalogue as one continuous hairline ledger grouped
by place, lead product large, the rest as rows (thumb · title · the real option axis as a caption · variant count ·
price · buy). **No pagination**, stated as a design decision on its own screen (`paginate collection.products by 30`),
and ordering as four plain `?sort_by=` links on a hairline — no toolbar, no drawer, no density selector.

## 3. Where it sells hardest

- **Every fold has a real product and a real price.** Mobile 390: decor shows the place, the approved suits/doesn't-
  suit pair, 7 מוצרים · 105 גדלים · 89.90–469.90 ₪, the question and the first answer row with a named product at
  89.90 ₪ — all above 844 px. Path shows the same shape ending at 69.90 ₪. `/collections/all` shows door 1 with
  169.90 ₪ and an add-to-cart. The audit's worst finding (no price, no product in the fold on four of five URLs)
  is dead.
- **The ladders are the sell.** Every price the visitor can pay is visible before they click: 6 rows for the net,
  6 for the crystal balls, 4 for the deck lights. On the old page those 105 variants were one hyphenated range.
- **Eight add-to-cart forms** across the three pages (firefly on decor; stainless, bollard and powerful on path;
  the same eight single-variant products in the `all` ledger), all as `<form method="post" action="/cart/add">`.
- **The one genuinely new fact:** the deck lights cost the same at 2, 4, 6 and 8 units. Printed plainly, with the
  price-per-point falling from 74.95 ₪ to 18.74 ₪. That is a sale the current page hides.

## 4. Where it is weakest

1. **The wall and spot collections are asserted, not proven.** Their questions («כמה חזק, ובאיזה גוון?»,
   «כמה רחוק צריך להגיע האור?») appear on `all.html` and in the "other rooms" strips, but I only built the ruler for
   a length axis and a quantity axis. Wall's real first axis is colour, and its meaningful axis (6W/12W, 3000K/6000K)
   is the *second* — the ruler would need a second rule for W and Kelvin. Until it is drawn, those two questions
   are a promise. **This is the weakest point.**
2. **Overlapping bands.** The narrowing rows and the product sections use two different groupings — the rows by
   "who reaches this length", the sections by "what this product maxes out at". It is honest (a note says so) but
   it is two mental models where one would be better.
3. **Poster images.** Nine of the 27 products have no clean photograph at all; I reach them with tight crops
   (`object-position` + a scale) and a `.ph--dim` treatment. That is fragile: any merchant re-upload breaks the
   crop. In Liquid it becomes per-slot settings, which is more work than the ledger the PDP already ships.
4. **The derived numbers are ours.** ₪/metre and ₪/point are computed from the pricelist, not supplied by the
   vendor. Every one carries a note saying so, and every one is arithmetic on published prices — but it is one
   more thing an owner must agree to publish.
5. **The desktop first screen is quiet.** A large night photograph with the text pushed to the start side leaves
   the end half nearly empty. It matches the product page, but on a 1440 monitor it spends a lot of pixels.

## 5. With one more day

- Build the **W / Kelvin ruler** for wall and the **coverage ruler** (LED count, beam) for spots, so the four
  questions all have the same proof. One extra rule: an axis of numbers becomes a scale; an axis of names becomes
  a hairline radio line (PDP §3.6).
- Collapse the two groupings into one: keep "who reaches this length" and drop the max-reach sections, so a
  product can appear once per band with the exact variant for that band.
- Make the ruler rows **hover-live**: pointer along the axis → each row shows the cheapest variant that reaches
  that point. It is 20 lines of JS on top of markup that already carries every number, and the page stays complete
  without it.
- Give the four collection photographs a per-collection focal point setting (the wall image is 1456×816 and is
  the one that really needs it).
- Add the sticky mobile "ask" line the PDP has (`mailto:` photo check) at the foot of the first screen.

## 6. System fidelity — checked against `WINNING-SPEC` §3 and `pdp/WINNING-SPEC` §3.5–3.6, §4.8

Night ground as one document gradient (sky-2 → sky-4), stars per section (.18 → .55), Frank Ruhl Libre for
display / numerals / prices only, Heebo for every product title, radius 0 except the pills, logical properties
throughout, Latin and numerals in `<bdi>`, `[data-lamp]` + IntersectionObserver with a scroll sweep (no-JS and
`prefers-reduced-motion` render everything lit; the ruler bars are drawn at full length), the card reused from
PDP §4.8 (kicker · Heebo title · price by the `elmsnest-v2-price` rule · form-or-link action, no badge, no swatch
row, no stars, no hover-swap). Never renders `images[0]` of any handle on the never-use list. No sale badge, no
strikethrough, no compare-at, no ratings, no urgency, no English UI, no cream, no brown, no four equal boxes in a
row, no toolbar. Consumer terms appear on all three pages.
