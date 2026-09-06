# Concept «dusk» — the frames (store-owned only; INVENTORY.md ids; files `../../../home2/images/own/own_<handle[:40]>_<n>.jpg`)

Every crop is CSS only (object-fit / object-position, or zoom + focal for the tiles); no file was edited. A frame the
page's phone gallery shows first (frame 1) is never used. All frames are 1254 × 1254.

| where | manifest id (product · gallery frame) | shows | crop (mockup CSS) | why this frame | caption needed | baked pre-crop for the dev-theme asset |
|---|---|---|---|---|---|---|
| A · dusk tile 1 «בין ערביים» | `stainless-steel-solar-path-light-ip65` · 4 | two steel bollards along a brick house at dusk, blue still in the windows | zoom 2.0, focal 72% / 47% → a 627 px square around the near bollard's head, the window and the brick | the page's own product at the exact moment of the angle (light already on, sky not yet gone) — a detail, not the home's landscape | none (own product) | none — clean; `ens-pdp-stainless-dusk.jpg` = the full frame, ≤ 1800 px, the crop stays in CSS so the owner can re-aim it |
| A · dusk tile 2 «לילה» | `stainless-steel-solar-path-light-ip65` · 2 | one lit bollard beside shrubs on a stone path, deep night | zoom 1.6, focal 33% / 42% → the lit head and the leaves | the same product, the same head, full night; the close-up the shopper never swiped to | none | none — clean |
| A · scene band | `stainless-steel-solar-path-light-ip65` · 6 | three bollards lighting stone garden steps at night | object-position 50% 62% (390 × 300) / 50% 58% (1366 × 480) | the widest, calmest own night scene: steps, rocks, ferns — «in place, at night, page-wide» | none | none — clean |
| B · scene band | `waterproof-led-wall-light-ip65-6w-12w` · 6 | dusk terrace, the white sconce on a stone pillar, pergola, lit garden spikes behind | object-position 50% 42% / 50% 40% | the product's only lifestyle frame, and its own; the sentence sits on the dark pergola side | none (own product; the lit spikes in the background are scenery, not a claim) | none — clean |
| C · scene band (spot collection default) | `dual-head-garden-light-10w-ip65` · 3 | the black dual-head bollard on a dark terrace, one warm beam, planter | side zoom 1.08 (cuts the thin gold border lines at both edges), object-position 50% 76% at 390 / 50% 30% at 1366 — both keep the source's top 274 px (mobile) / 244 px (desktop) out of view | the only night frame in the spot collection without a foreign brand sign (frame 5 has LUMIÈRE); a beam on a wall is the family's light | **yes** — «בתמונה: מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65», linked. It is a MAINS product on a solar product's page: the band's sentence says nothing about power, and the dusk section above it carries no photograph of anything | **yes** — `ens-pdp-spot.jpg` must be a baked pre-crop of frame 3: x 40 – 1214, y 210 – 1234 → 1174 × 1024 (short side ≥ 1000), which removes the small Hebrew caption top-left (y < 150), the lotus logo top-right (y < 190) and all four border lines; then the CSS crop is a plain object-position with no zoom |
| C · dusk pair | — (no photograph) | the TYPE pair: «יום» outlined gold on the sky-0 → sky-1 gradient, «לילה» in glow on sky-2 → sky-4 with the house star layer and a static warm pool | — | the fallback for a solar product with no clean own frame: nothing is implied, no other product is shown | none | none |

## Collection defaults the Liquid would ship (four assets, `assets/ens-pdp-<slug>.jpg`, ≤ 220 KB, ≤ 1800 px, progressive JPEG)

Only the scene band has collection defaults. The dusk pair NEVER falls back to another product's photograph — a
day/night pair of a lamp that is not this lamp would imply what the rule forbids — so its fallback is the type pair.

| collection | asset | source frame | pre-crop | caption on a product that is not the pictured one |
|---|---|---|---|---|
| path | `ens-pdp-path.jpg` | `stainless-steel-solar-path-light-ip65` · 6 | none | «בתמונה: מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65» |
| wall | `ens-pdp-wall.jpg` | `outdoor-bidirectional-led-wall-light-ip65` · 6 (night slate wall, villa) | none | «בתמונה: מנורת קיר LED חיצונית דו־כיוונית IP65» |
| spot | `ens-pdp-spot.jpg` | `dual-head-garden-light-10w-ip65` · 3 | x 40–1214, y 210–1234 (1174 × 1024) | «בתמונה: מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65» |
| decor | `ens-pdp-decor.jpg` | `solar-crystal-ball-string-lights` · 3 (trellis; NOT frame 5, which the home band already uses) | none | «בתמונה: גרילנדת כדורי קריסטל סולארית – 20 עד 200 נורות» |

Per-product map (section blocks: `product` + `image_dusk_1` + `image_dusk_2` + `image_scene` + zoom/focal/object-position
text settings) — the mockup's A and B rows are what the map would hold for those two handles; any product the owner
adds a block for gets its own frames without a code change. The other products with clean own frames per INVENTORY.md
(`powerful-solar-garden-light` 3, `outdoor-bidirectional-led-wall-light-ip65` 1/5/6, `solar-crystal-ball-string-lights`
1/3/5, `solar-edison-string-lights` 4/5, `solar-firefly-garden-lights` 4/5) are the next map entries.

## Rejected

- `powerful-solar-garden-light` · 3 (clean daylight, the disc panel visible) as the «day» tile on A: it is another product;
  in a pair it would read as this product's panel even with a caption. The pair shows the page's own product or no
  product at all.
- `dual-head-garden-light-10w-ip65` · 5 for C: the LUMIÈRE OUTDOOR LIVING sign (x > 930) would need a crop that loses
  the composition's right third, and the frame is dusk, not the family's beam.
- Every frame INVENTORY.md marks «—» (baked claims, infographics, faces, foreign marks), the featured creatives, the CC
  lamps of the home round.
