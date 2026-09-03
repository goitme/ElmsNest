# INDEX — «האינדקס» · critique

Files: `index.html` (גרילנדות ותאורה דקורטיבית, 7/105) · `path.html` (תאורת שביל, עמוד וגינה, 8/22, 69.90–999.90)
· `all.html` (הקטלוג, 27/172) · `index.css` · `index.js`.
Renders: `shot-*.png` (desktop 1440, mobile 390, full page + fold). Heights: index 2279 / 3733 · path 2616 / 4143
· all 4158 / 8444. No horizontal overflow, no JS errors on any of the six captures.

## 1. The one idea

**The collection is not a grid of photographs — it is an index: one hairline row per lamp, and on every row the
whole price ladder of that lamp is printed, so the entire collection (and, on `/collections/all`, the entire
27-product store) is legible without opening a single product.**

The device only a lighting store can build is the fourth column — *הסולם*. It is the PDP's price rail (§4.4),
lifted out of the product page and repeated once per row: the price-bearing option axis (metres, bulbs, units,
LEDs, m²) drawn as a hairline with one stop per value and the real price under each stop. Seven rows of the decor
collection put **26 option values and 26 prices on one 900 px screen**; the path collection puts 22 variants and,
where a set is priced by quantity, the derived **price per unit** under each stop (`≈29.16 ליח׳` for 12 units at
349.90) — which is the only honest way to compare a 69.90 ₪ single light with a 999.90 ₪ set of eight.

The photographs are earned, not decorative: each row's plate starts as a 56 px dark sliver and, when the row is
reached, grows to 120 px and lights (IntersectionObserver, 1.6 s filter curve, permanent). The serial numeral
fills from hairline outline to glow at the same moment. No JS / reduced motion = every row lit and full-size.
That is the one motion on the page, and it is the store's own metaphor: you walk down the index and the lamps
come on as you pass them.

## 2. How a visitor narrows the set

**7 lamps (`index.html`).** The whole collection is one screen. Narrowing happens by *reading*, not by filtering:
the row tells you the axis (אורך / גודל / גוון / כמות), how far it reaches (1.5 → 12 מ׳, 20 → 200 נורות), and what
each step costs. A visitor who knows "I have six metres of pergola" finds the two products that reach six metres
and the exact price of that length in one pass. Three additional routes are stacked above the index and both are
inside the mobile fold: the four collections with their counts (the place, which is how this store sells), the
server-side ordering links (`?sort_by=title|price-ascending|price-descending`, plain `<a>`s, active state
underlined in glow), and the price column. A row is one tap to the product page; the eight single-variant
products add to the cart from the row itself.

**8 lamps under a 14× span (`path.html`).** The same rows, plus one instrument the decor page does not have: a
**price scale** across the full width, one glowing tick per model at its opening price, and a hollow tick at
999.90 joined by a hairline to model 08 — which says, in one graphic, that the 14× gap is not a better lamp but
the same lamp in eight units. The compression of the scale is disclosed in its own caption ("המרחקים דחוסים, לא
ליניאריים"). The index below is ordered `price-ascending` (server-side), and every set carries its per-unit price,
so "expensive" and "cheap" become comparable rather than intimidating.

**27 lamps (`all.html`).** A book's front matter: **תוכן העניינים** — four entries, each with its place, count,
price span and its first three product names — then the index itself in four labelled runs, numbered 01–27
continuously. No pagination and a stated reason: `paginate collection.products by 50` with the control printed
only when `paginate.pages > 1`; any `?sort_by=` drops the grouping and prints one flat index in the same row
markup. Three screens, no page 2, every price in the store visible.

## 3. Where it sells hardest / weakest

**Hardest.** The fourth column. A catalogue that shows "89.90–179.90 ₪" hides the decision; this one prints
89.90 · 89.90 · 99.90 · 109.90 · 129.90 · 179.90 with the metres above them. It also disarms the store's ugliest
data problem — 105 variants behind one range — by saying out loud which axis moves the price and which does not
("הצבע אינו משנה את המחיר", "× 4 צבעי אור"). And it is dense in the way a specialist is dense: the whole shop,
priced, in the time it takes to read a page.

**Weakest.** Three things.
1. **Desire.** The photographs are 120 × 60 px slivers. Against the product page's full-bleed night stage, the
   index is cool. The one enormous plate per page (the place, its approved "suits" and "does not suit" pair, at
   104 px display type) carries all of the atmosphere, and it arrives only on screen two.
2. **Image quality is the ceiling.** 15 of 27 products have marketing text baked into every photograph. Every
   plate here is a deliberate crop of a permitted index (never `images[0]` on the never-use list), and the wide
   3.75:2 aperture cuts most of the type off — but a few plates (net lights, retro set, the spot posters) still
   carry a legible fragment, and two products are only available as bright cream studio shots that sit oddly on
   the night ground even dimmed to 62–70 %.
3. **Row density on a phone.** A desktop row is one line; a mobile row is four (title, price, a scrolling scale,
   an action). 27 of those is an 8 400 px page. It works — the scale scrolls with a mask, exactly as the PDP rail
   does — but the "one screen" claim is a desktop claim.

## 4. With one more day

- **A quiet reach filter.** The data supports one honest facet that Shopify's does not hold: the first-axis value
  itself. "עד כמה מטר?" as five hairline links (3 / 6 / 12 / 22 / 32 מ׳) that dim the rows whose ladder does not
  reach — client-side progressive enhancement over a server-rendered full index, so the no-JS page is unchanged.
- **Ranged brackets on the path scale** for all eight models, not only for 08, on a four-level stagger.
- **A per-row hover preview**: enlarge the plate to ~360 px in place on hover/focus, so the index can be browsed
  as pictures without leaving it.
- **Card parity check.** The row is an extension of `elmsnest-v2-pdp-card`, not a fork: same image resolver, same
  `elmsnest-v2-price` rule (single / narrow range / `מ־`), same `elmsnest-v2-buy` branch. It still needs the
  related-row variant of the card re-tested on the product page after the ledger column is added as an optional
  block.
- **Real Liquid pass** on the ledger: `product.options_with_values[n]` grouped by `variant.option1` with
  `min(price)` per value — the only new snippet the concept needs (`elmsnest-v2-ladder.liquid`).
