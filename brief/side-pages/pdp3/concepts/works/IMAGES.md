# Concept «works» — the photographs

Three internet photographs on the solar pages (A, C), one on the mains page (B). Nothing store-owned is reused. No
photograph carries type on it: every word sits on the cream mat around it (caption ink `#1a1206` on `#f4eee3` = 16.05:1,
credit `#6f675b` on `#f4eee3` = 4.83:1, both measured). Crops are CSS only (`object-fit: cover` + `object-position`), no
file edited. Every internet photograph is named by a caption that says what it is, so it never reads as this product.

| id | file | author · licence · source | credit drawn | crop (CSS) | role | the sentence that names it |
|---|---|---|---|---|---|---|
| `wm_5869e6ea3a` (pdp3) | `../../images/candidates/wm_5869e6ea3a.jpg` 3840×2560 | Guilhem Vellut · CC BY 2.0 · https://commons.wikimedia.org/wiki/File:Close-up_of_a_polycrystalline_solar_PV_panel.jpg | «צילום: Guilhem Vellut (CC BY 2.0)» — 11 px muted, on the mat under the tiles | tile 3:4 at 390 (≈ 105×140), 4:5 at ≥ 901 (≈ 200×250); `object-position: 50% 50%` — the centre cells and busbars | «איך זה עובד» tile 1: the cell in daylight — a material; its cool blue is itself the «different colour» | caption «שמש על תא סולארי» |
| `ov_30d8e75d-02ad-4c23-86e1-b9d364d9220a` (pdp3) | `../../images/candidates/ov_30d8e75d-02ad-4c23-86e1-b9d364d9220a.jpg` 1024×683 ⚠ | aenigmatēs · CC BY 2.0 · https://www.flickr.com/photos/54264114@N06/52189396832 | «צילום: aenigmatēs (CC BY 2.0)» — same credit line | tile 3:4 / 4:5 as above; `object-position: 66% 50%` — the vertical strip that keeps the purple-amber sky over the tall tree silhouettes; the file's full height is used, so the 683 px source is sharp in a ≤ 250 px tile | «איך זה עובד» tile 2: the sky at dusk — a place, nothing in it can be mistaken for a lamp | caption «השמיים בין ערביים» |
| — (no photograph) | — | — | none | tile 3: the page's own night ground (sky-2 → sky-4) with one CSS radial glow (`--env2-glow` / `--env2-ember`, a small bright core and a soft halo) | «איך זה עובד» tile 3: the night — drawn, not photographed, so the page keeps three photographs and the third frame is honestly «the night you are already on» | caption «לילה» (and `aria-hidden` on the tile) |
| `ov_42864d07-e921-4b30-b71c-adbcb12f7869` (pdp3) | `../../images/candidates/ov_42864d07-e921-4b30-b71c-adbcb12f7869.jpg` 1024×667 ⚠ | Corey Leopold · CC BY 2.0 · https://www.flickr.com/photos/97708873@N00/51485607579 | «צילום: Corey Leopold (CC BY 2.0)» — 11 px muted, on the mat beside the caption | 3:2 at 390 (330×220, the whole frame); 16:9 at ≥ 901 (≈ 620×349), `object-position: 50% 48%` — the band on sky, wall and paving | `ens_pdp_place`: a real garden path and dry-stone wall at golden hour — atmosphere, the most Israeli-looking golden frame in the pool, no lamp anywhere in it | caption «גינה בשעת בין ערביים» under the sentence «האור האחרון של היום.» |

⚠ = 1024 px as downloaded (under the 1200 px floor). The sky is only ever a ≤ 250 px tile, so the file is enough as is.
The garden path is displayed at ≤ 330 px (390) and ≤ 620 px (1366) — fine at 1×, soft at 2× on desktop; **before deploy
re-fetch the Flickr original** (page URL above; the shortlist says the same) and export the theme asset at 1600 px
wide, ≤ 220 KB. Fallback if the original cannot be fetched: `wm_54cd152739` (home2, public domain, 3840 px, desert path
at sunset, no credit needed) with the caption «שביל בשעת בין ערביים».

Faces: none. Brand marks: none. Baked text: none. Filters: none (the path has mild in-camera HDR, noted in the
shortlist; no filter added). Alt attributes are empty on purpose — the figcaptions carry the meaning, the neighbours'
convention (`elmsnest-s-home-band`, `elmsnest-s-pdp-scene`).

## Theme assets to export (deploy, not this concept)

| asset | from | size target | served widths (`asset_img_url`) |
|---|---|---|---|
| `ens-pdp-works-cell.jpg` | `wm_5869e6ea3a`, 3:4 centre crop | 900×1200, ≤ 120 KB | 300x, 450x, 600x, 900x (tile ≤ 250 px → 600x at 2×) |
| `ens-pdp-works-dusk.jpg` | `ov_30d8e75d`, 3:4 crop at 66 % | 512×683 as is, ≤ 90 KB | 300x, 450x, 512x |
| `ens-pdp-place-garden.jpg` | `ov_42864d07` original (re-fetched) | 1600×1042, ≤ 220 KB | 600x, 900x, 1200x, 1600x |

Per page: A / C ≈ 2 × 35 KB (tiles at 600x) + ≈ 120 KB (garden at 1200x) ≈ 190 KB of images; B ≈ 120 KB. All lazy, all sized.
