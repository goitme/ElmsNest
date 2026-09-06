# Concept «scene» — every frame used (store-owned only; `../../../home2/images/own/` in the mockup)

The rule this concept follows: a photograph on a product page is read as *this product*. So the map is
**own frame first** (a later gallery frame, never gallery frame 1), the **collection scene** only when the product
has no clean frame, and then only with the «בתמונה: …» line. No CC image, no featured creative, no frame with baked
text unless the deployed asset is a baked pre-crop that leaves ≥ 1000 px on the short side.

| # | manifest id (file) | product | archetype · slot | crop in the mockup (CSS, no editing) | why | caption |
|---|---|---|---|---|---|---|
| 1 | `own_stainless-steel-solar-path-light-ip65_6` (1254×1254, t25, clean 5) | `stainless-steel-solar-path-light-ip65` — the page's own product | **A · section 1** (the night scene) | 390: box 390×480, `object-fit:cover`, `object-position:78% 50%` (three heads in frame, the left one at the edge); 1366: box 1366×560, `50% 58%` (the steps under the sentence) | the best depth and calm of the six; gallery position 6 — the phone shopper who never swiped sees it here for the first time; gallery frame 1 (`_1`, what the phone shows) is deliberately not reused | none — it is the product |
| 2 | `own_stainless-steel-solar-path-light-ip65_4` (1254×1254, t24, clean 5) | same product | **A · section 2** (the dusk detail) | a 300×300 px slice of the source, x 760–1060 · y 560–860 (the right bollard's head at blue hour), shown 132 px square at 390 and 200 px at ≥ 901: `inline-size:418%`, `inset-inline-start:-65%`, `inset-block-start:-187%` | the only own frame at dusk — the moment the light comes on; the head carries the panel; framed as a detail, unlike the home's two landscapes | none |
| 3 | `own_waterproof-led-wall-light-ip65-6w-12w_6` (1254×1254, t24, clean 5) | `waterproof-led-wall-light-ip65-6w-12w` — the page's own product | **B · section 1** | 390: `object-position:62% 50%` (sconce centre-right, sentence over the shrub); 1366: `50% 34%` (pergola, pillar, sconce; sentence over the dark glass) | the only lifestyle frame of this product (2/4/5 are studio walls); gallery position 6, not frame 1 (the featured creative with baked Hebrew) | none — it is the product |
| 4 | `own_dual-head-garden-light-10w-ip65_5` (1254×1254, t20, clean 1 → **crop-only**) | `dual-head-garden-light-10w-ip65` — ANOTHER store product (mains) | **C · section 1** (the spot collection's scene — the fallback) | the source is anchored at its left edge and oversized so the sign never enters the frame: 390: `inline-size:135.3%`, `inset-inline-start:-35.3%`, `inset-block-start:-5.3%` → source x 0–927, y 60–1200; 1366: `134.8%`, `-34.8%`, `-86.6%` → source x 0–930, y 330–711 | the only spot-family frame that is a *place* at night (tree, bed, house, a lit bollard spot); `_3` (the terrace) was tried and rejected — at 1366 it reads as a product macro, not a place | **«בתמונה: מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65»**, linked to `/products/dual-head-garden-light-10w-ip65` |

## Where a baked pre-crop is needed (deployed assets, ≤ 220 KB, ≤ 1800 px, progressive JPEG)

- **#4 `ens-pdp-spot.jpg`** — MUST be pre-cropped: the foreign brand sign «LUMIÉRE OUTDOOR LIVING» is baked in at
  x > 935 (letters from x ≈ 1010, y 560–650). Pre-crop **x 0–1000, y 0–1254 → 1000×1254** (short side exactly 1000,
  rule 4). The strip x 935–1000 holds only the sign's dark panel edge behind the hedge, no letter; the section's crop
  above never shows even that (x ≤ 930 at both widths). If the judges want zero panel in the file, x 0–930 gives
  930×1254 and breaks the 1000 px floor — that is the trade, stated.
- **#1, #2, #3** — no pre-crop, the files are clean; they deploy as they are (`ens-pdp-stainless-steps.jpg`,
  `ens-pdp-stainless-dusk.jpg`, `ens-pdp-wall-terrace.jpg`), rendered with `asset_img_url` sizes 600 / 900 / 1254
  (never a 1600 candidate: the source is 1254 — home2 critique E7). The detail (#2) is shown ≤ 200 px, so it loads the
  600 candidate; at 2× DPR the 300 px slice is ~1:1 — acceptable, and the owner's `image_picker` for the detail slot
  can replace it with a tighter upload.

## Weight per PDP

A: 2 photographs (scene + detail) · B: 1 · C: 1 (the detail slot is empty, the row is text). All
`loading="lazy"`, `decoding="async"`, width/height set. Never more than 2 new files on a page (BRIEF §2 item 6 allows 3).

## The map the Liquid follows (no product data changes)

1. **Per-product map** (section blocks: `product` + `image_picker` scene + `image_picker` detail + `object_position`
   ×2 per block, matched on `product.handle`): A → #1 / #2; B → #3; the other 15 products with a clean own frame per
   `INVENTORY.md` get their block the same way (e.g. `outdoor-bidirectional-led-wall-light-ip65` → `_6`, the slate
   wall; `solar-edison-string-lights` → `_4`; `solar-crystal-ball-string-lights` → `_3`, since `_5` is the home band).
2. **Per-collection fallback** (four theme assets, each an `image_picker` setting with a `product` setting for the
   «בתמונה» link): path → `own_stainless-steel-solar-path-light-ip65_5` (asparagus fern; not `_6`, so a path product
   never shows the same frame as A's own scene) · wall → `own_outdoor-bidirectional-led-wall-light-ip6_6` · spot →
   #4 · decor → `own_solar-edison-string-lights_5` (pergola). The fallback ALWAYS prints the «בתמונה» line with the
   linked title, even when the fallback product happens to be the page's own product — except that the Liquid skips
   the line when `fallback_product.handle == product.handle`.
3. **No frame at all** (a product whose collection is not in the map): section 1 prints nothing; section 2 still
   renders as the text row on solar products.
4. **Detail slot** (section 2): map only — no collection fallback, because a detail of another product's panel on
   «כשמחשיך» would be a lie. Empty slot → text row (C).
