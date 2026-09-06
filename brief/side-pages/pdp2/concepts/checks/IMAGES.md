# Concept «checks» — every photograph

All frames are the store's own product images (`home2/images/own/`, INVENTORY.md ids). No CC candidate, no featured
creative, no gallery-1 frame. A PDP loads at most TWO new files here (band + one sliced tile file); C loads one.
Crops in the mock are CSS only (`object-fit` / `object-position`, and for C `object-view-box`); the real files are
untouched. Where a baked pre-crop is needed for the production asset it is said below.

| archetype · section | INVENTORY id · frame | file | what it shows | crop (390 / 1366) | why | caption needed |
|---|---|---|---|---|---|---|
| A · scene band | `stainless-steel-solar-path-light-ip65` · 4 (t24, clean 5, own) | `own_stainless-steel-solar-path-light-ip65_4.jpg` 1254² | two steel bollards by shrubs along a brick house at dusk | 390×400 cover, 50% 55% / 1366×520 cover, 50% 55% | the page's own product, *in place, at dusk, wide* — a home, not a studio; and it is gallery frame 4, not frame 1, so the phone shopper has not seen it (frame 1 is the hedge/wet-pavers shot) | none — it IS the product |
| A · checks, tiles 1–3 | `stainless-steel-solar-path-light-ip65` · 6 (t25, clean 5, own) | `own_stainless-steel-solar-path-light-ip65_6.jpg` 1254² | three bollards lighting stone garden steps, rocks, ferns, bamboo | one file, three crops: 390×104 strips at 50% 0% / 50% 50% / 50% 100% (top · middle · bottom band of the square); 1366: 4:3 tiles at the same positions | one request for three tiles (weight rule §2-6); the top slice is trees and sky (sun), the middle the lamps (reach), the bottom the lit steps (winter) | none |
| B · scene band | `waterproof-led-wall-light-ip65-6w-12w` · 6 (t24, clean 5, own) | `own_waterproof-led-wall-light-ip65-6w-12w_6.jpg` 1254² | dusk terrace, white sconce on a stone pillar, pergola, lit garden spikes behind | 390×400 cover, 50% 45% / 1366×520 cover, 50% 38% | the only lifestyle frame of this product; gallery 6 — the phone never shows it; the white variant of the page's product, mains light shown as a mains light | none |
| B · checks, tiles 1–2 | `waterproof-led-wall-light-ip65-6w-12w` · 4 (t18, clean 5, own) | `own_waterproof-led-wall-light-ip65-6w-12w_4.jpg` 1254² | black slim up-down sconce angled on a grey wall, warm beams | one file, two crops: 390×104 strips at 50% 0% (the up-beam) and 50% 100% (the down-glow); 1366: 2:1 tiles at the same positions | the product's own detail, honest for «how far must the light reach» (the beam) and «where does the power come from» (the wall it hangs on) | none |
| C · scene band | `dual-head-garden-light-10w-ip65` · 3 (t18, clean 2, **crop**) | `own_dual-head-garden-light-10w-ip65_3.jpg` 1254² | lit black dual-head bollard on a dark terrace, warm beam, planter | mock: `object-view-box: inset(17.6% 3.2% 2.4% 3.2%)` then cover, 50% 30% / 50% 0% | the spot collection's only night scene that survives a legal pre-crop; the floodlight has no clean frame of its own | **yes** — «בתמונה: מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65», linked to `/products/dual-head-garden-light-10w-ip65` |
| C · checks | — | — | the typographic fallback: outlined gold numerals (the facts numeral's stroke), hairlines, no photograph | — | a second frame of another product on this page would need a second caption; the fallback is honest without one and still reads as the same section | — |

## Baked pre-crop needed (production assets)

- **`ens-pdp-spot.jpg`** (from `own_dual-head-garden-light-10w-ip65_3.jpg`): the file carries a thin gold frame line on
  all four sides, a small Hebrew caption «אור חם ונעים» top-start and a lotus logo top-end. Pre-crop **x 40–1214,
  y 220–1224** → 1174×1004 px (short side 1004 ≥ 1000, rule §3-4), JPEG progressive ≤ 220 KB. The mock's
  `object-view-box` reproduces exactly this window on the un-edited file. No other frame in the concept needs a pre-crop.
- The per-collection defaults for the products without a clean frame (10 of 27) would be: path →
  `own_stainless-steel-solar-path-light-ip65_6` (captioned «בתמונה: מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65»
  on every path product but the stainless light itself), wall → `own_outdoor-bidirectional-led-wall-light-ip6_6`
  (night slate wall; captioned), spot → `ens-pdp-spot.jpg` above (captioned), decor →
  `own_solar-edison-string-lights_5` (Edison bulbs under a pergola; captioned). All four are clean own frames
  (INVENTORY «own»), none is any product's gallery image 1 except the crystal-ball frames, which is why the decor
  default is the Edison frame 5 and not crystal frame 1.

## Weight (BRIEF §2-6)

A: 2 files (band + tile file) · B: 2 · C: 1. All `loading="lazy"`, `decoding="async"`, `width`/`height` set.
Production `asset_img_url` sizes: band 600/900/1254 with `sizes="100vw"`; tile file 600/900 with
`sizes="(min-width:901px) 420px, 100vw"` — the tile never renders wider than 420 px, so no 1254 candidate.
