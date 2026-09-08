# Concept «install» — notes (PDP round 3, 2026-09-07)

## The device, and why it is a different look

Two sections, one idea: **what happens by day, close up, framed.** The round-2 sections are a night photograph edge to edge with words under it, and a hairline row. These two are the opposite on every axis that the brief names:

- **Framed, not full-bleed.** Every photograph sits inside the wrap with the night ground around it — a 4:5 frame (a 7:6 window into the same crop at 390) beside the text in «התקנה», two 1:1 tiles (3:2 on desktop) in «בחוץ». No photograph touches the page edge.
- **Beside, not under.** On desktop the «התקנה» photograph stands at the inline-start (the right) and the two sentences sit at its left, hugging the frame, vertically centred; on the phone the photograph comes first and the heading and line follow it. The scene puts words under a band; this puts them next to a picture.
- **Daylight and detail tones, not blue-black night.** Hands on dry soil, a zinc screw and a red wall plug on a white ground, drops on a panel, blue crystal cells in hard sun, a white wall with red bougainvillea at noon, drops on a stem. The page stays night; the sections bring light into it — the white plug frame is the brightest thing on the page and it is deliberately small and framed.
- **Nothing written on a photograph.** All type sits on the night ground (ink and ink-2 on `#070b15`, no measurement needed: 14.6:1 and 10.4:1). The naming caption and the licence credit run as one 12 px line under each frame (`--env2-ink-2`, 10.4:1).
- **Practical, warm, close-up.** Every frame is a material or a gesture, never a place with a lamp and never a lamp — so nothing can be mistaken for the product, and the captions say what each frame is.

## Order in the template

`templates/product.elmsnest.json` → `order`: `main-product` → `ens_pdp_scene` → `ens_pdp_dusk` → **`ens_pdp_install`** → **`ens_pdp_weather`** → `ens_pdp_facts` → `ens_related`. Both new sections sit after the dusk row and before the facts: night scene → the sun → how it goes in → where it lives → the numbers. Nothing between the gallery and the button; nothing after `ens_related`. Files: `sections/elmsnest-s-pdp-install.liquid`, `sections/elmsnest-s-pdp-weather.liquid` (Hebrew `{% schema %}`, `enabled_on: templates: ["product"]`); the template edit is the two entries and the order.

## Measured heights at 390 (playwright, `getBoundingClientRect`, DPR 1)

| archetype | install | weather | new together | page (bands + new) | screens at 844 |
|---|---|---|---|---|---|
| A stainless path light (solar, photo scene) | 485.69 | 358.53 | 844.22 | 4249 | 5.03 |
| B waterproof wall light (mains, no dusk) | 485.69 | 358.53 | 844.22 | 4101 | 4.86 |
| C solar floodlight (text-only scene) | 485.69 | 358.53 | 844.22 | 3777 | 4.48 |

Caps: ≤ 520 per section ✓ (485.69), ≤ 1500 together ✓ (844.22), ≤ 7.5 screens ✓. Round-2 measured the live path page at 5.03 screens (4246 px with header and footer); with the two sections it becomes ≈ 5090 px ≈ 6.03 screens. `scrollWidth` = 390 on every archetype (no horizontal overflow).

At 1366 (for the record): install 695.39, weather 653.91; the install frame 440×550, the tiles 608×405. Fold shots (`shots/*-d-fold.png`, 1366×900) show the whole «התקנה» section and the head of «בחוץ».

## The gate per family (by rule, no product data)

**`elmsnest-s-pdp-install`** — family from `elmsnest-s-place emit:'word'`; the variant from the product's own title + description (`strip_html`), the dusk row's technique:

| family word | variant | products today | photograph slot (image_picker, asset default) |
|---|---|---|---|
| שביל, contains «נעיצ/נועצ» | stake | stainless, retro set, powerful garden light | `image_stake` → `ens-pdp-install-soil.jpg` |
| שביל, contains «ברגים/מדבקות» | screws | warm step/deck, waterproof deck | `image_screws` → `ens-pdp-install-plug.jpg` |
| שביל, neither | none | mains bollard, modern path set, swaying set | — |
| קיר (any) | wall | waterproof wall, bidirectional, 6W up-down, indoor-outdoor, solar motion sensor | `image_wall` → `ens-pdp-install-plug.jpg` |
| גינה, contains «נעיצ/נועצ» | stake | 52-LED spotlight | `image_stake` |
| גינה, contains «פאנל נפרד» | panel | solar floodlight | `image_panel` → `ens-pdp-install-plug.jpg` |
| גינה, neither | none | dual-head, security light, lantern 9-LED, camping lantern | — |
| מרפסת, contains «נעיצ» | stake | firefly lights | `image_stake` |
| מרפסת, contains «תולים/תליי» | hook | globe string, edison, crystal ball, rope | `image_hook` → **empty** (text-only until an own frame) |
| מרפסת, neither | none | net lights, birch branches | — |

The magnetic indoor spot is in the wall collection and would get the wall variant; its description says «בלי לקדוח» — the rule adds one exclusion: description contains «מגנטי» → none. Every line and caption is a `text` setting with these defaults; every credit is a `text` setting the owner clears when he replaces the asset with his own frame.

**`elmsnest-s-pdp-weather`** — prints when the title + description contains «IP» (the listing's own outdoor claim; indoor products print nothing). The two photographs switch on the solar test copied verbatim from `elmsnest-s-pdp-dusk` (`custom.power_source == 'סולארי'`, else «סולארי» in title + description): solar → `image_rain_solar` (`ens-pdp-weather-rain-panel.jpg`) + `image_sun_solar` (`ens-pdp-weather-cells.jpg`); not solar → `image_rain_other` (`ens-pdp-weather-drops.jpg`) + `image_sun_other` (`ens-pdp-weather-wall.jpg`). Copy identical for every family.

Per page, never more than three photographs: install 1 + weather 2 (hook variant: 0 + 2).

## Weight

Theme assets (q80, progressive), the largest candidate ≤ the file: soil 900×900 182 KB (`600x`, `900x`); plug 1024×680 28 KB (`600x`, `900x`, `1024x`); rain-panel 800×1200 159 KB (`600x`, `800x`); cells 1000×667 175 KB (`600x`, `1000x`); drops 1000×667 68 KB; wall 1000×750 186 KB. Per page: A ≈ 182 + 159 + 175 = 516 KB at the largest candidates, ≈ 250 KB at the 600 px candidates a 390 phone picks (frame 350 px, tiles 168 px); B ≈ 28 + 68 + 186 = 282 KB; C ≈ 28 + 159 + 175 = 362 KB. All `loading="lazy"`, `decoding="async"`, sized (`width`/`height`). No JS, no carousel, no parallax, no reveal, no second button, no second price. Radius 0, logical properties (the CSS zoom-crop of the soil frame uses `top/left` + `translate` because a crop offset is a physical thing about the photograph, not about reading direction).

## Is any of this twice?

Honestly: **one near-touch, no repeat.** The facts on A print «התקנה: נעיצה באדמה בעומק כ־5–10 ס״מ» and the install line says «נועצים באדמה» — the same verb, once as a number in the specs, once as the act beside a photograph; the number is not repeated and the section could drop the verb («מרכיבים את היתד, ולתוך האדמה.») if the owner reads it as twice. The dusk row says the panel gathers sun; C's line says where to put the panel — a different fact. On A and C the weather section shows two panel surfaces (rain on one, sun on another) — two weathers, one material; if that reads as twice, the sun tile switches to the white wall for solar products too (one setting). Nothing else on the page is said again: no place line, no price, no suits/not-for, no hours, no IP, no button, no link. Device-wise: nothing full-bleed, no hairline row, no words on a photograph — the round-2 devices are not repeated, and the home's two-frame figure (words on scrims) is not either.

## Open items for the lead

1. Merge `images/manifest.install.jsonl` into `../../images/manifest.jsonl` and take the Commons original of the plug photograph (4288×2848) when the rate limit lifts.
2. The «hook» variant ships text-only; an own frame of a plain hook on a pergola beam completes it.
3. The store's own stake in soil (hands only) can replace the BLM hands through the picker; until then the caption is honest about what the frame is.
