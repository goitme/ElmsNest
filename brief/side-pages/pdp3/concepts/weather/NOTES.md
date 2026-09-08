# Concept «weather» — «בחוץ, כל השנה» · «בין ערביים» (PDP round 3)

## The device, and why it is a different look

The two round-2 sections are one device: a night photograph edge to edge, words under it on the night ground, and a
hairline row. This concept adds two sections that use **the opposite device**: photographs **framed inside the wrap**
(never full-bleed), **no text on any photograph** (no scrim, no headline on a frame), a **12 px muted caption under
each frame that names what the photograph is and carries the credit**, and — the different colour — **daylight**:

1. **`ens_pdp_weather`** — a **pair of detail photographs side by side** (4:5 tiles at 390, 3:2 at ≥ 901): rain drops
   on the grey glass of a panel · a solar cell surface in hard sun, cool blue. Wet grey and hard daylight, material,
   close, textured — the opposite tonality of the amber night band above it. One short line under each tile, no
   number (the IP code stays in the facts, which sit directly under this section so the numeral answers the pictures
   without a word). Mains products get the same layout with a garden pair (drops on a stem · a white wall at noon)
   so no panel ever appears on a non-solar page.
2. **`ens_pdp_hour`** — **one warm dusk photograph beside text** (5:4 framed at 390; at ≥ 901 the photograph takes
   the inline-end 7/12 column and the heading + glow line sit bottom-aligned in the inline-start column — the only
   place on the page where a heading sits beside a picture rather than under it). Warm windows and a lit sky bring
   amber and cream onto the night ground. The line uses the licensed place word; the caption names the place.

Not used anywhere: full-bleed, scrim, type on a photograph, hairline rows, a second guide link, a button, a price,
motion, JS. Radius 0, logical properties, stock `<figure>` / `<figcaption>`.

The optional third section (the guide link as an image-led strip) is **deliberately not delivered**: the scene already
carries the PDP's only guide link, a second would be «twice», and a strip would need a fourth photograph on the page.
Two sections, three photographs per page.

## Order in the template (`templates/product.elmsnest.json`)

`main` → `ens_pdp_scene` → `ens_pdp_dusk` (solar only) → **`ens_pdp_weather`** → `ens_pdp_facts` → **`ens_pdp_hour`** →
`ens_related` → footer. Nothing between the gallery and the button; nothing after `ens_related`. The weather pair
before the facts (rain, sun → the IP numeral); the hour photograph after the facts as the warm breath before the
related grid.

Files: `sections/elmsnest-s-pdp-weather.liquid`, `sections/elmsnest-s-pdp-hour.liquid`, Hebrew `{% schema %}`,
`enabled_on: templates: ["product"]`, image pickers with the theme assets as empty defaults, per-breakpoint
`object_position` text settings as in `elmsnest-s-home-solar`, the facts' `<bdi>` token loop on every text setting.

## Gate per family (by rule, no product data)

- **weather**: prints when a bullet of the product's own description carries an outdoor IP code — the facts' numeral
  loop, tokens IP65 / IP66 / IP67 / IP68 (IP44 and lower, or no code, → nothing: the birch branches, the camping
  lantern, the USB globe string, the net lights print nothing). Which pair: the dusk row's solar test, copied verbatim
  (`custom.power_source == 'סולארי'`, else title + description contain «סולארי») → solar pair; anything else → garden
  pair. Family-independent otherwise (path, wall, spot, decor all get the same two lines).
- **hour**: prints when `elmsnest-s-place emit:'word'` is not blank; the line is picked by the word
  (שביל / קיר / גינה / מרפסת); the two handles the scene overrides (`lighted-birch-branches-20-led` → indoors,
  `rechargeable-telescopic-camping-lantern` → the field) print nothing, because a courtyard is not their place.
  One photograph for all families (one asset, one picker); a per-family picker is an easy addition if the owner
  brings four dusk frames.

Archetypes this round: A stainless path light (solar, IP65) → solar pair + «השביל»; B waterproof wall light (mains,
IP65) → garden pair + «הקיר» (no dusk row on that page); C solar floodlight (solar, IP67, text-only scene) → solar
pair + «הגינה» — on C the weather pair is the first photograph after the gallery.

## Measured heights at 390 (playwright, `getBoundingClientRect`, fonts loaded, images decoded — `shots/measure.json`)

| archetype | `ens_pdp_weather` | `ens_pdp_hour` | both | page today | page with both | screens (÷ 844) |
|---|---|---|---|---|---|---|
| A path (solar) | 416.31 | 445.89 | 862.2 | 4246 (5.03) | 5108 | **6.05** |
| B wall (mains) | 433.70 | 445.89 | 879.6 | 4081 (4.84) | 4961 | **5.88** |
| C flood (solar, text scene) | 416.31 | 445.89 | 862.2 | 3791 (4.49) | 4653 | **5.51** |

Every section ≤ 520 (max 433.7); both together ≤ 1500 (max 879.6); every page under the 7.5-screen cap (max 6.05).
B is 17 px taller only because the credit «jenny downing (CC BY 2.0)» takes its own line in a 169 px tile.
At 1366: weather 652.3, hour 611.8 (tiles 608×405, the hour photograph 691×460).

## Type and contrast (no text on any photograph, so nothing to measure there)

Heading: Frank Ruhl Libre 700, clamp(25px, 3.4vw, 44px) — the neighbours' h2 scale. Lines: Heebo 400 16 px (18 at
≥ 901), ink #f4eee3 — 17.0:1 on sky-3. The hour line: Frank Ruhl 700 20 px (28 at ≥ 901) in glow #ffd394 — 14.6:1 on
the ground where it sits (~78 % of the page, ≈ #030408). Captions and credits: Heebo 400 12 px, `--env2-mute` #8f95a3 —
6.55:1 on sky-3 (#070b15, where the weather section sits), 5.79:1 even on sky-2 at the very top, 6.87:1 on sky-4.
All ≥ 4.5:1. Credits never wrap mid-token (`white-space:nowrap` on the `<bdi>`).

## Weight estimate

Per page three lazy photographs below the fold: solar pages ≈ 177 + 146 + 210 ≈ 530 KB, mains pages ≈ 56 + 154 + 210 ≈
420 KB (assets prepared at 1000 px for the tiles — 608 CSS px at 1366 — and 1200 px for the hour photograph, q70–72,
each ≤ 220 KB; `asset_img_url` candidates 600/900/1000 or 1200, never wider than the file). CSS ≈ 2.5 KB inline per
section, no JS, no fonts beyond the page's own.

## Is any of this twice? (honest)

- The two weather lines are a deliberate refrain of one grammar («גשם של ינואר. …» / «שמש של אוגוסט. …») — one idea
  said in two weathers, not two ideas; if the owner reads a refrain as «twice», the sun line can be cut to
  «שמש של אוגוסט.» alone.
- «בין ערביים» and the dusk row's «כשמחשיך» name the same hour. The dusk row says what the sun does to the lamp;
  the hour section shows a place at that hour and says nothing about the lamp — a different sentence, but the
  same hour twice on solar pages, and this is the honest weak spot of the concept.
- The place word now appears three times on a page (kicker «תאורת שביל, עמוד וגינה», the scene's «בלילה, על השביל»,
  and «השביל, רגע לפני שצריך אור.») — by design, the licensed vocabulary; still three.
- The hour photograph is the same courtyard on every family; a path page shows a courtyard. The caption keeps it honest;
  it is one atmosphere, not four.
- Nothing else repeats: no second full-bleed, no second hairline row, no second guide link, no price, no button, no
  claim already in the facts.
