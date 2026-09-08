# Concept «daylight» — the photographs (PDP round 3, 2026-09-07)

Every file is referenced by relative path from `index.html`; nothing is edited — every crop is CSS (`object-fit:cover`,
`object-position`, and a `transform:scale()` around the same point for a detail). Licence, author and source page as in
`../../images/manifest.jsonl` (pdp3) and `../../../home2/images/manifest.jsonl` (home2). No faces, no brand marks, no
baked text in any crop shown. **No photograph here is the product, and each one is named as what it is by a caption on
the same card.** Per page: A 2 files · B 1 file · C 2 files (the checks tiles re-use the day file) — under the 3-file cap.

| id | pool | author | licence | credit as drawn | file | crop (CSS) | role | the words that say what it is |
|---|---|---|---|---|---|---|---|---|
| `wm_54cd152739` | home2 | Joshua Tree National Park (US NPS) | Public domain | **none** (PDM — no credit owed) | 3840×2563, 3.4 MB source | day card: 16:10, `object-position:50% 62%` (the path, cacti and the mountain foot; the sky held to a sliver) · desktop: the 7/12 column, min 420 px tall, same point · checks tiles: `8% 42%` ×2.2 (a sunlit cactus), `50% 80%` ×1.7 (the path running away), `50% 6%` ×1.9 (the sky and the ridge) | the «ביום» photograph of the **path** family (A) and the three «לפני שקונים» details on A | «שביל בגן קקטוסים, לפנות ערב» on the card; «שלושה פרטים מתוך תמונת היום» under the tiles. A gravel path between cholla cacti at sunset — a place, no lamp of any kind in frame. |
| `ov_7379ba54-775e-4044-b839-56ce83f7deb1` | pdp3 | Carol M Highsmith | CC0 1.0 | **none** (CC0) | 3840×2881 (rawpixel / LoC), 4.2 MB source | day card: 16:10, `object-position:62% 46%` ×1.25 (the yellow wall, the bush and the white wall; the barred window kept small at the edge) · checks tiles (two): `30% 60%` ×1.9 (the white wall corner and gravel — the run from a light to what it must show), `18% 8%` ×1.9 (the sky over the wall) | the «ביום» photograph of the **wall** family (B) and the two details on B | «קיר בשמש הצהריים» on the card; «שני פרטים מתוך תמונת היום». A rendered house wall with bougainvillea at noon — no fixture anywhere in the frame. |
| `wm_b1fa34fd63` | pdp3 | Josh Evnin (from Chicago, IL, USA) | CC BY-SA 2.0 | **צילום: Josh Evnin (CC BY-SA 2.0)** — 11.5 px muted on the sand (6.4:1), and again under the checks tiles on the night ground (11.3:1) | 3840×2550, 1.8 MB source | day card: `object-position:0% 100%` ×2.3 — the lower-left 43 % of the frame: cypress row, terracotta beds, the palm; the city, the bay and the balustrade with its municipal globe lamps are OUT of the crop · desktop: same point, the wider column shows a sliver more to the right (still short of the balustrade) · checks tiles: `34% 78%` ×2.6 (the palm in sun), `12% 84%` ×2.2 (the cypress row — distance), `50% 4%` ×1.9 (sky, sea, the city — outdoors) | the «ביום» photograph of the **spot / garden** family (C) and the three details on C | «גינה מדורגת בחיפה, בצהריים» on the card. A terraced garden at noon, a real Israeli place; nothing in the crop resembles a garden light. Share-alike attaches to the photograph, not to the page. |
| `wm_701ca719a2` | pdp3 | Bastique | CC BY 4.0 | **צילום: Bastique (CC BY 4.0)** — 11.5 px muted on the sand, beside the tile | 3840×2560, 2.6 MB source | 1:1 tile (132 px at 390, 200 px at ≥ 901), `object-position:72% 78%` ×1.6 — glass, busbars and the sun's reflection only; the pines and sky of the full frame are out | the «מקרוב» detail (A, C; the section prints nothing on B) | «תא סולארי. הצד שפונה לשמיים.» — the line names the material. A commercial PV module on a roof, shown at a scale where it is a surface, not a lamp. |
| `ov_c3ee8ae1-df10-4137-93dd-1ae268c66148` | pdp3 | tillwe | CC BY-SA 2.0 | **צילום: tillwe (CC BY-SA 2.0)** | 2048×1366, 320 KB source | day card: 16:10, `object-position:70% 55%` (the tomato plant against the sunlit trees; the block of flats to the left cropped away) | the **decor / balcony** slot default — **not rendered in A/B/C** (no decor archetype this round); named here so the fourth `image_picker` has an honest empty default | «מרפסת בשעת בין ערביים». A city balcony at golden hour — a place. Second choice for the slot if the owner wants warmer colour: `ov_93506e94` (purple sage backlit, BPPrice, CC BY 2.0). |

## Deploy assets (what `prepare-assets.py` would export — not done here; the concept references the source files)

| asset | from | export | measured at q80 progressive |
|---|---|---|---|
| `ens-pdp-day-path.jpg` | `wm_54cd152739` | the 16:10 band (y 5–67.5 %), 1100×688 + `800x` candidate | 1200×750 = 258 KB → at 1100 / q78 ≈ 205 KB; `800x` = 115 KB |
| `ens-pdp-day-wall.jpg` | `ov_7379ba54` | x 12–92 %, y 10–60 %, 1200×750 + `800x` | 223 KB → q76 ≈ 200 KB; `800x` ≈ 100 KB |
| `ens-pdp-day-spot.jpg` | `wm_b1fa34fd63` | x 0–60 %, y 50–87.5 %, 1200×750 + `800x` | 219 KB (≤ 220) ; `800x` ≈ 100 KB |
| `ens-pdp-cell.jpg` | `wm_701ca719a2` | x 45–95 %, y 50–100 %, 600×600 + `400x` | 91 KB ; `400x` = 45 KB |
| `ens-pdp-day-decor.jpg` | `ov_c3ee8ae1` | 16:10 band, 1200×750 | est. ≈ 150 KB |

The checks tiles are the **same asset** as the day card (another `object-position` and a zoom), so a page never loads a
fourth file. At 390 the browser takes the `800x` candidate for the 350 px card; a ×2.2 tile detail from that candidate
is displayed at 102 CSS px (204 device px) from a ≈ 360 px source region — sharp enough for a tile; at ≥ 901 the 1200 px
candidate feeds 392 px tiles. Every `<img>` is `loading="lazy"`, `decoding="async"`, has `width`/`height`, and the
`srcset` candidates stay ≤ the file's width (the home round's R26 rule).
