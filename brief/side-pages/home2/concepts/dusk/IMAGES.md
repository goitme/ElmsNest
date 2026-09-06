# Concept «dusk» — images

All three come from the shortlist; none is edited. Cropping is `object-fit: cover` + `object-position` only. Every `<img>` carries width/height and `loading="lazy"` (both sections sit below the hero).

| section | manifest id | file | role | why this frame | license · credit |
|---|---|---|---|---|---|
| [A] day frame | `own_powerful-solar-garden-light_3` | `images/own/own_powerful-solar-garden-light_3.jpg` (1254×1254) | «ביום נטען.» | The only daylight frame in the set where the solar panel is visible on every lamp head, lamps off. Same product, same red-leaved hedge as the night frame, so the pair reads as one place at two hours. Crop at 390: 4:5, `object-position 18% 50%` (front bollard and its panel). At 1366: 16:10, `30% 50%`. A daylight photo is allowed here because the concept is a day/night pair (BRIEF §2). | store-owned · none |
| [A] night frame | `own_powerful-solar-garden-light_2` | `images/own/own_powerful-solar-garden-light_2.jpg` (1254×1254) | «בלילה נדלק.» | The same bollards lit, warm patterns on the pavers. The file carries a baked Hebrew caption bottom-left («אור חם ומרשים», y > 92 %). At 390 the image is drawn at 116 % of the box height, top-aligned, `object-position 90% 0` — the bottom 14 % is outside the box, so the caption never shows. At 1366 the 16:10 box shows y 11–74 % (`70% 30%`), caption outside as well. Verified in both shots. | store-owned · none |
| [B] winter | `wm_03d6246a95` | `images/candidates/wm_03d6246a95.jpg` (3840×2560) | «ובחורף?» mood | The one frame in the set that feels like a short cold evening: blue dusk, spruces, white bollards, cool light. Used for atmosphere only — the lamps are not the store's. At 390 the box (390×520) shows only the right-hand third (`78% 46%`): bollards and spruces, no pergola, no power poles. At 1366 the band is wider than the photo, so the pergola stays at the left edge; a side scrim dims it and `object-position 50% 62%` drops the wires at the top. | CC0 (System XciX, Wikimedia Commons «The Sundre Light Garden at dusk») · no credit required; IMAGES.md keeps the source for the record |

Not used, and why: `own_solar-edison-string-lights_4` (panel detail) — a third frame would break the «two frames» idea; the panel is already visible on the day frame. `own_modern-solar-path-lights-set_6` (rain) — needs a heavy crop, and the winter idea here is the short day, not the weather.

## Theme assets (on deploy)

`assets/ens-home-day.jpg` · `assets/ens-home-night.jpg` (from the two 1254 px squares, JPEG q78 — well under 220 KB) · `assets/ens-home-winter.jpg` (resized to 1800 px wide, JPEG q78, ≤ 220 KB). Each section's `{% schema %}` exposes an `image_picker` per frame; the theme asset renders when the picker is empty.
