# ערב אחד — concept `evening` · critique

Files: `index.html` (decor, 7) · `path.html` (path, 8) · `all.html` (catalogue, 27) · `evening.css` · `evening.js`
Renders: `shot-*.png` · heights (desktop/mobile, CSS px): index **6636 / 6944** · path **6678 / 7301** · all **6991 / 10134**.
`shot.js`: no horizontal overflow, no JS errors on any of the six captures.

## 1. The one idea, in a sentence

**The collection page is one evening in one garden: you scroll from the gate to the table, every lamp appears
pinned to the place where it would actually stand, its card rises out of that photograph, and the collection
description is the caption of the scene** — the grid dissolves into a place, and browsing becomes walking
through the evening you are buying.

Only a lighting store can do this, because only a lighting store's catalogue is already sorted by *where the
light falls*. The device that carries it is the **pin**: a lit dot on the photograph with a hairline stem and
a gold tag (`מעל השולחן`, `בתחילת השביל`, `מנורה בכל שלח`). It lights with the lamp on arrival
(IntersectionObserver, `--lit` 0→1 over 1.6 s), so a still frame already shows the idea: light standing in a
place, not a product floating on a background.

## 2. How a visitor narrows the set — two axes, never a toolbar

**A. By place — «מסלול הערב» / «ארבע שעות של ערב».** A hairline index directly under the fold: numbered
stations with the real count and the real from-price, each an anchor. It is a filter built from the only
datum this store actually has (`collection` membership / `product_type`), and it doubles as the page's
table of contents.

- **7 lamps (decor)** → five stations: `01 מעל השולחן` (1) · `02 בין העצים ועל הפרגולה` (2) ·
  `03 בערוגה` (1) · `04 על הגדר, ברוחב` (1) · `05 אחרי הדלת` (2). A visitor with a pergola does not read
  seven cards; they tap `02`.
- **8 lamps (path)** → `בתחילת השביל` · `המדרגות והדק` · `בין השיחים ובערוגה` · `סטים לשביל שלם` ·
  `עד הכניסה, עד הסוף`.
- **27 lamps (all)** → four places with their scene photo, count, price span and the approved *suits* phrase.
  That index replaces the facet drawer entirely; the note says so out loud.

**B. By measure — the axis that carries the price.** Each page ends with a full-width hairline ledger built
from `firstAxis` in `data.json`, no invented numbers:

- **decor — «כמה מטר צריך?»** fourteen rows, one per length that exists anywhere in the collection
  (1.5 · 3 · 5 · 6 · 6.5 · 7 · 8 · 9.5 · 10 · 11 · 12 · 13 · 22 · 32 מ׳), each listing the garlands available
  at that length with the exact price. "I have a six-metre pergola" is answered in one row. A footnote names
  the three products measured differently (net by area, fireflies by 10 bulbs, birch by 72 cm).
- **path — «כמה מנורות צריך?»** six rows (1 · 2 · 4 · 6 · 8 · 12 lamps), every offer at that quantity with
  **the price per lamp**. This is the answer to the 14× span: 69.90 ₪ and 999.90 ₪ stop being incomparable
  once the page says 69.90 ₪/lamp against 124.99 ₪/lamp, and 29.16 ₪/lamp for twelve step lights. The
  headline of station 05 *is* that number: «שמונה מנורות לאורך הדרך, 124.99 ₪ כל אחת.»
- **all — the beam ledger** for the spot band: rows led by the number printed on the product
  (9 LED · 10W · 52 LED · 100 LED · 200 LED · 360 מעלות), with the honest caveat that LED counts, watts and
  degrees are not one scale — it is what the manufacturer states, not our comparison.

Ordering still exists and still works without JS: a hairline `סדר` strip of plain `?sort_by=` links
(`price-ascending`, `price-descending`, `title-ascending`, `created-descending`), with the default named
honestly `לפי סדר הערב` (= `manual`). No "best selling", no "popularity".

## 3. Composition — every screen different

index: full-bleed scene with the first lamp's card riding its bottom edge → hairline route → scene + two
stacked cards → **a 200 px photograph alone in a screen of night beside a 60 px serif line** (scale contrast)
→ a 100 %-wide net photograph with a six-value price ladder under it → two 146 px footnote thumbs → the
14-row ledger → order → terms → footer.
path: same opening, then a full-bleed stair band + two **stepped** cards on staggered baselines, then a photo
band with cards overlapping its lower edge, then **two price rails side by side and no big photograph at all**,
then the 999.90 ₪ finale full-bleed, then the quantity ledger.
all: four-place index with scene thumbs → 8 hairline walk rows → a **staggered wall** of six unequal cards
(300/238/278/208/264/222 px, five different aspect ratios) → the numeric beam ledger → a terrace band with a
scroll-snap card row overlapping it → the pagination note.
Nowhere are there four equal boxes in a row; nowhere is there a toolbar, a badge, a strikethrough, a star or
a percentage.

## 4. Honesty and system fidelity

Every title, price, option value, count and range is from `data.json`; the two collection descriptions are the
real `collection.description`, printed as the caption of the scene rather than a grey slab. The four approved
place → *suits* phrases are the card kickers, and each page prints one approved negative in the caption
(`לא מתאים אם צריך אור חזק — זו אינה מטרתה` / `לא מתאים אם המקום כמעט אינו מקבל אור יום`). `/collections/all`
says plainly: `אין כאן דירוגים, אין «הנמכרים ביותר» ואין מבצעים — עוד לא צברנו מה למדוד.` The consumer terms
sit on all three pages as four numerals (0 ₪ · 8–17 · 14 יום · תמונה אחת) with a `mailto:` photo check — never
"בוואטסאפ". The one compare-at price in the catalogue is never rendered.
Image ledger: **no `images[0]` of any never-use handle is rendered anywhere** (checked per card); every other
poster crop is removed in CSS with `aspect-ratio` + `object-position` + a `--z`/`--zx`/`--zy` scale utility,
i.e. by the same mechanism the theme snippet would use, not by editing files. Bright indoor shots
(globe garland, birch, two wall lamps) carry `.ph--veil` so they belong to the night.
System: sky-2→sky-4 gradient on the document, Frank Ruhl Libre display + Heebo body, product titles never in
the serif, radius 0 except pills and the pin/knob circles, logical properties throughout, prices as
`<bdi>…</bdi> ₪` with ranges inside a single `<bdi>` so they never reverse.

## 5. Where it sells hardest

The fold. On a 390 px phone all three pages show, above 844 px: the place as a photograph, the collection
title, a real product with a real price, a working action, the description, the real counts, and the first two
narrowing stations. `path.html` and `all.html` put an **add-to-cart button** in the fold (single-variant
products: מנירוסטה 169.90 ₪, דו־ראשית 189.90 ₪) — the audit's page showed no price at all there.
Second hardest: the price ladders. Six net sizes with six prices, or 4 יח׳/8 יח׳ with the per-lamp figure,
shown *before* the click, is the thing that makes a 469.90 ₪ or 999.90 ₪ product comprehensible instead of
frightening.

## 6. Where it is weakest

1. **The station copy is authored, and it does not exist in Shopify yet.** `מעל השולחן`, `בערוגה`,
   `על הגדר, ברוחב` are editorial groupings I assigned by reading each product. Shipping this needs one new
   metafield (`custom.evening_station`, a short string per product) plus a section block per station, or the
   merchant must re-assign a lamp by hand when a product is added. That is the single biggest cost of the idea.
2. **The wall band on `all.html` is the least "one evening" screen.** Six wall lamps against studio-ish
   photography is a good staggered wall but a weak *place* — it is the one band where the concept is carried by
   typography rather than by a scene.
3. **The 14-row metre ledger is tall on a phone** (~1,050 px of the 6,944). It is the most useful device on the
   page and I would not cut it, but it currently has no way to jump to a length.
4. **The per-unit prices are computed here by hand.** In Liquid they need the unit count parsed out of the
   option value (`6 יחידות` → 6) or a small metafield; the deck-step product, whose four quantities all cost
   149.90 ₪, is deliberately shown without a per-unit figure and flagged in the footnote rather than smoothed
   over — but a merchant who fixes that data must not have to touch the template.
5. `all.html` is 6,991 / 10,134 px. Honest for 27 products in one page, but the mobile page is long; the four
   anchors carry all of the burden of getting back out.

## 7. What one more day buys

- **A station picker that filters in place**: the route items become `?station=` links (server-side, no JS) so
  a visitor can collapse the page to one station; with JS they simply scroll. Same markup, one Liquid `if`.
- **A length/quantity jump on the ledger**: tapping a metre row scrolls to the product and pre-selects that
  variant via `?variant=`, so the ledger becomes a real buying path instead of a reference table.
- **Two more pins per scene** on `index.html` station 02 and on the `all.html` terrace band, with the leader
  line drawn to the card — the connection between pin and card currently relies on proximity and the number.
- **`collection.image` as the opening scene for the two collections that lack a hero-grade photo** (wall, spot)
  with a deliberate focal crop for the 1456×816 wall image, so the wall band gets its own place.
- A `prefers-reduced-motion` pass on the pins specifically (they are covered by the global rule, but the tag
  could still fade in one step rather than being instantly lit).
