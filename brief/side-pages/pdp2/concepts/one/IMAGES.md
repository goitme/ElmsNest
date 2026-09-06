# Concept «one» — the frames

One photograph per product page (BRIEF §2.6: ≤ 3 — this concept loads 1). The section renders, in this order:
(1) the block of the per-product map whose `product` matches `product.handle` (`image_picker` + two object-position
texts), else (2) the per-collection default asset `ens-pdp-<path|wall|spot|decor>.jpg` with the collection's
`credit_product` — the store product that frame shows — printed as «בתמונה: …», else (3) nothing (the section
collapses to the text alone; never a foreign frame). All frames are the store's own gallery images
(`home2/images/own/`, 1254×1254 PNG originals re-encoded to JPEG); none is a gallery frame 1; none is a featured creative.

## Rendered in the mockup

| archetype | manifest id | product it shows | gallery position | crop (CSS, no editing) | why | caption |
|---|---|---|---|---|---|---|
| A | `own_stainless-steel-solar-path-light-ip65_6` (t25 · clean 5 · own) | the page's own product | 6 of 6 — never the phone's frame 1 | 390: 390×300 box, `object-position 50% 55%` → the three lamps, the steps and the fern; 1366: 1366×520, `50% 44%` → all three lamp heads whole, the steps under them | the inventory's «best depth and calm»; a night garden, wide, in place — the desire picture the carousel hides at position 6 | none — it is this product |
| B | `own_waterproof-led-wall-light-ip65-6w-12w_6` (t24 · clean 5 · own) | the page's own product | 6 of 6 | 390: `50% 62%` → the sconce on the pillar, the pergola, the lit garden spikes; 1366: `50% 46%` → the sconce whole at the top third, the terrace and the spikes at the left | the only lifestyle dusk frame this product has; the blue-hour sky at the left edge is kept — it is what «dusk» looks like | none — it is this product |
| C | `own_dual-head-garden-light-10w-ip65_3` (t18 · clean 2 · **crop-only**) | ANOTHER store product: `dual-head-garden-light-10w-ip65` (spot collection, MAINS) | 3 of 6 of that product | mockup: the box is widened 5 % and pulled 2.5 % past each edge, `object-position 50% 88%` at 390 / `50% 30%` at 1366 — the baked caption («אור חם ונעים», y 90–108, x 94–273), the logo (y 16–259, x 1000–1237) and the gold frame line (x 17 / x 1236 / y 16) stay outside the visible window | the spot collection has no clean night frame of any product; this is its only dark, in-place frame (a terrace at night, a warm beam on a rendered wall, a planter) | **«בתמונה: מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65»** linked to `/products/dual-head-garden-light-10w-ip65` |

### Where a baked pre-crop is needed (BRIEF §3 image rule 4)

- **C — `ens-pdp-spot.jpg`** must be a pre-crop baked into the asset, because a CSS crop still ships the baked
  text inside the file: crop `own_dual-head-garden-light-10w-ip65_3` to **x 20–1234, y 220–1234 → 1214×1014**
  (short side 1014 ≥ 1000 ✓). Measured on the file (high-pass over a 12 px blur, threshold 60): the caption's
  line-art ends at y 141, the logo's at y 191, the gold frame line sits at x 17 / x 1236 / y 16 — all outside the
  crop, with 29 rows to spare above it. On the baked asset the object-positions become `50% 100%` (390) and
  `50% 8%` (1366). Progressive JPEG, ≤ 220 KB.
- A and B need no pre-crop: the files carry no text.

## The per-collection defaults the Liquid would ship (four theme assets, owner-overridable)

| collection | asset | frame | shows | caption product |
|---|---|---|---|---|
| path | `ens-pdp-path.jpg` | `own_stainless-steel-solar-path-light-ip65_6` | steps, three bollards | `stainless-steel-solar-path-light-ip65` |
| wall | `ens-pdp-wall.jpg` | `own_outdoor-bidirectional-led-wall-light-ip65_6` (t24 · clean 5) | night slate wall, up-down light, palm, villa | `outdoor-bidirectional-led-wall-light-ip65` |
| spot | `ens-pdp-spot.jpg` | `own_dual-head-garden-light-10w-ip65_3` pre-cropped as above | dark terrace, warm beam | `dual-head-garden-light-10w-ip65` |
| decor | `ens-pdp-decor.jpg` | `own_solar-crystal-ball-string-lights_3` (t24 · clean 5) | crystal string along a wooden trellis at night | `solar-crystal-ball-string-lights` |

`own_solar-crystal-ball-string-lights_5` (the fence) is NOT used: it is the home band's photograph (twice).
On the product that the default shows (e.g. the stainless path light itself, if its map entry were removed), the
caption is suppressed by rule: `credit_product.handle == product.handle` → no line.

## Weight

One `<img>` per page: `loading="lazy" decoding="async"`, `width`/`height` set, `sizes="100vw"`,
`asset_img_url` candidates `600x, 900x, 1254x` (never a 1600 candidate — the source is 1254). At 390 the browser
picks 600x (DPR 1) or 900x (DPR 2); at 1366 the 1254x. The mockup uses the raw files from `home2/images/own/`.
