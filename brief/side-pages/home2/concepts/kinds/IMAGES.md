# Concept «kinds» — images

All five frames are the store's own product images (`images/own/`), so no credit line is needed and nothing in
the sections is «our product»-claimed — they are used as atmosphere for a kind of light. No file was edited:
every crop is CSS (`object-fit: cover`, `object-position` for the focus point, and a `transform: scale()` around
the same origin as the zoom), so the theme asset is the frame as it is.

## [A] ens-home-kinds — 2×2 mosaic, square frames

| tile | manifest id | file | why | crop (CSS) | license |
|---|---|---|---|---|---|
| 1 · שלולית אור | `own_stainless-steel-solar-path-light-ip65_1` | `own/own_stainless-steel-solar-path-light-ip65_1.jpg` | Shortlist #4, top score. Bollards along a hedge, the wet pavers lit under them — the cleanest «pool of light» in the set. Solar product. | focus 55 % 90 %, zoom 1.3 → window ≈ x 13–90 %, y 21–98 %: two bollards and the pavers they light | store-owned, no credit |
| 2 · שטיפת אור | `own_outdoor-bidirectional-led-wall-light-ip6_6` | `own/own_outdoor-bidirectional-led-wall-light-ip6_6.jpg` | Shortlist #8: warm up/down wash on textured slate — the clearest wall-wash in the set. Mains wall light, so atmosphere only (the line is about the light, not the product). | focus 42 % 50 %, zoom 1.35 → window ≈ x 11–85 %, y 13–87 %: lamp and its wash, the villa on the right mostly out | store-owned, no credit |
| 3 · אלומת אור | `own_dual-head-garden-light-10w-ip65_5` | `own/own_dual-head-garden-light-10w-ip65_5.jpg` | Shortlist #10: the adjustable spot bollard aiming a beam into planting, Mediterranean garden. Mains, atmosphere only. | focus 14 % 38 %, zoom 1.5 → window ≈ x 5–71 %, y 13–80 %: spot head and the tree; the baked «LUMIÈRE» sign starts at x ≈ 75 % and stays outside the box at both breakpoints | store-owned, no credit |
| 4 · שרשרת אור | `own_solar-edison-string-lights_4` | `own/own_solar-edison-string-lights_4.jpg` | Shortlist #3: Edison string running over a patio table, solar panel on its spike in the corner. Solar product. | focus 62 % 50 %, zoom 1.25 → window ≈ x 12–92 %, y 10–90 %: the bulbs over the table, a corner of the panel bottom-left | store-owned, no credit |

Frames are 1254 × 1254 source; on the theme they become `assets/ens-home-kind-pool.jpg`, `-wash.jpg`, `-beam.jpg`,
`-string.jpg` at ≤ 1000 px square, JPEG q78, each well under 220 KB (a 1:1 tile never renders wider than 560 px on
desktop and 175 px on a phone).

## [B] ens-home-solar — one wide frame

| manifest id | file | why | crop (CSS) | license |
|---|---|---|---|---|
| `own_solar-rope-string-lights_3` | `own/own_solar-rope-string-lights_3.jpg` | Shortlist #11: the solar panel staked at the base of the trunk, the rope light it feeds spiralled up the tree — the sentence's two halves (sun charges, light turns on) in one frame, no diagram. Solar product; used as the picture of the fact, not as a product pitch. | Phone (4:5 box): focus 75 % 100 %, zoom 1.5 → window ≈ x 35–88 %, y 33–100 %. Desktop (1366 × 540 band): `object-position: 50% 84%`, no zoom → band = y 51–90 % of the square. In both, the baked «IP65» badge (top-left, y < 30 %) is outside the box. | store-owned, no credit |

Theme asset: `assets/ens-home-solar.jpg`, 1254 px wide (source width), JPEG q78, ≤ 220 KB; rendered with
`asset_img_url` sizes 390 / 780 / 1254, `loading="lazy"`, `width`/`height` set.

## Considered and not used

- `ov_4fcf0ff1…` (villa pool at dusk, CC BY): the strongest CC wide frame, but a hotel pool reads as a resort, not a
  home garden, and the store's own rope-and-panel frame carries the solar sentence better with no credit line.
- `own_powerful-solar-garden-light_2` (night bollards): a second candidate for the wide band; the baked Hebrew caption
  forces an upper-band crop that loses the pavers, and the panel on the lamp heads is too small to read as «the sun».
- `own_solar-firefly-garden-lights_4`: a lovely fifth kind (glow among plants) — refused, the mosaic is four kinds.
- `wm_ffe3b052ef`, `wm_1cfe403a9a` (real path photos, CC BY / BY-SA): honest but cool-white; the mosaic wants four
  frames with one warm temperature so they read as one set.
