# Concept «places» — every frame used (store-owned only; `../../images/INVENTORY.md` ids)

All files are 1254×1254 (`brief/side-pages/home2/images/own/own_<handle[:40]>_<n>.jpg`, n = gallery position). Crops
in the mockup are CSS only (`object-fit: cover` + `object-position` per breakpoint; for the one frame with baked
marks, a `transform: scale()` from a chosen origin) — no file was edited. On the dev theme each frame lands as
`assets/ens-pdp-<slug>.jpg` (≤ 220 KB, ≤ 1800 px, progressive JPEG) and the owner can override it per product with
the block's `image_picker`. Sizes served: 600w / 900w / 1254w for the lead tile (390 → 100 vw), 400w / 600w for the
small tiles (≤ 50 vw), 900w for a desktop 4:5 tile (410 px rendered, ×2 = 820) — never a 1600w candidate (home2
critique E7). Three photographs per PDP at most (B and A load three, C one), all `loading="lazy"
decoding="async"` with width/height.

## A — `stainless-steel-solar-path-light-ip65` (own frames; nothing to say — every tile IS the product)

| tile | id | INVENTORY | crop 390 (tile) | crop ≥ 901 (4:5) | why | pre-crop |
|---|---|---|---|---|---|---|
| lead «מדרגות» | own_stainless-steel-solar-path-light-ip65_6 | frame 6 · t25 · clean 5 · own | 390×220 · object-position 50% 60% (image rows ≈ 328–1036: the three heads and the steps) | 66% 50% (columns ≈ 166–1169: the left lamp in, the right lamp whole but one) | the best depth and calm of the set; steps = a place the gallery's frame 1 (the hedge) does not show | none |
| «כניסה» | own_stainless-steel-solar-path-light-ip65_4 | frame 4 · t24 · clean 5 · own | 193×160 · 50% 55% | 55% 50% | the only frame with a house: windows, brick, the entrance | none |
| «בין השיחים» | own_stainless-steel-solar-path-light-ip65_2 | frame 2 · t24 · clean 5 · own | 193×160 · 50% 50% | 45% 50% | one bollard close, the second in bokeh: the scale of a single unit | none |

Frame 1 (the hedge, gallery frame 1 = what the phone shows) is deliberately not reused; frame 5 (ferns) was the
fourth candidate and is left for the owner's picker.

## B — `waterproof-led-wall-light-ip65-6w-12w` (one own place frame + two sibling frames, credited)

| tile | id | INVENTORY | crop 390 | crop ≥ 901 | why | caption |
|---|---|---|---|---|---|---|
| lead «פרגולה» | own_waterproof-led-wall-light-ip65-6w-12w_6 | frame 6 · t24 · clean 5 · own | 390×220 · 50% 40% (rows ≈ 218–926: sconce, pergola, the lit spikes behind) | 55% 50% | the page's own product in a real dusk place; gallery frame 6, which the phone shopper never swiped to (NOTES.md) | none — it is the product |
| «חצר» | own_outdoor-bidirectional-led-wall-light-ip6_5 | outdoor-bidirectional-led-wall-light-ip65 frame 5 · t24 · clean 5 · own | 193×160 · 50% 45% | 45% 50% | the same kind of up-down wall light, square body — the closest sibling form to the slim sconce; blue hour, patio chairs | «חצר, אבן צפחה — בתמונה: מנורת קיר LED חיצונית דו־כיוונית IP65» linked |
| «אבן צפחה» | own_outdoor-bidirectional-led-wall-light-ip6_6 | same product, frame 6 · t24 · clean 5 · own | 193×160 · 50% 50% | 45% 50% | deep night, the wash on textured slate — the wall family's strongest night frame | same line (one line per sibling product, listing its tiles) |

The studio frames 2/4/5 of the product itself (grey wall, no place) were rejected for this section: a studio wall is
not «a place». Both sibling frames are MAINS lights like the page's product, so no solar implication is made.

## C — `solar-floodlight-ip67-remote-timer` (no clean own frame; the spot family's one place frame, credited)

| tile | id | INVENTORY | crop 390 | crop ≥ 901 | why | caption |
|---|---|---|---|---|---|---|
| single «ליד האדנית» | own_dual-head-garden-light-10w-ip65_3 | dual-head-garden-light-10w-ip65 frame 3 · t18 · clean 2 · **crop** | 390×300 · object-position 50% 80% + scale 1.06 from 50% 80% → image region ≈ x 35–1218, y 275–1185 | one 4:5 tile · 100% 50% + scale 1.25 from 80% 85% → ≈ x 411–1213, y 213–1216 | the only spot-family frame that is a place at night (a dark terrace, warm beam, planter); the floodlight's own six frames all carry headlines, icon strips or the «Solar Light IP67» product marking | «בתמונה: מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65» linked |

**Baked pre-crop needed on the dev theme** (BRIEF §3 image rule 4): the file carries a Hebrew caption «אור חם ונעים»
top-left (rows ≈ 80–150), a round logo top-right (≈ 80–195) and a thin gold frame line ≈ 28 px inside every edge.
Clean region: **x 30–1224, y 200–1226 → 1194×1026, short side 1026 ≥ 1000.** The asset
`ens-pdp-spot-terrace.jpg` is that region (no other edit); the CSS values above then become plain
`object-position` on the pre-cropped asset (390: 50% 78% · ≥ 901: 100% 50% without scale).

Rejected for C: own_dual-head-garden-light-10w-ip65_5 (the dusk garden path — the LUMIÈRE OUTDOOR LIVING sign starts
at x ≈ 935, so the clean slice is 930 px wide, under the 1000 px floor); own_solar-floodlight-ip67-remote-timer_2
(the pleasant dusk entrance is a ≈ 730×600 inner region, far under the floor, and the product marking sits beside
it); own_dual-head-garden-light-10w-ip65_1 / _6 (clean but studio — a beige set is not a place).

## Frames read as «twice» risk (BRIEF §3 image rule 6)

- A: gallery frames 6, 4, 2 — not frame 1. The phone shows frame 1 with «1/6»; the shopper who never swipes has not
  seen these three.
- B: gallery frame 6 of the product — same argument; the two siblings are not in this product's gallery at all.
- C: not in the product's gallery (another product's frame, credited).
