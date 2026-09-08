# `sections/elmsnest-s-pdp-weather.liquid` — measured (2026-09-08)

Harness: `render.py` renders the real section file (schema block stripped, schema **defaults** used as
`section.settings`, exactly as `templates/product.elmsnest.json` passes `"settings": {}`) through
python-liquid with the real `snippets/elmsnest-v2-bdi-range`, then inlines the markup + the section's own
`<style>` into `harness-<A|B|C>.html` together with the `elmsnest-v2-core` tokens, the night ground
gradient and `@font-face` for Heebo 300/400/500 and Frank Ruhl Libre 700 from
`brief/assets/fonts` (`file://`). Images are the real theme assets over `file://`.
Shot by `shoot.js` with playwright/chromium 1194, `deviceScaleFactor: 1`.

## Archetypes

| | product | IP token | solar test | rain tile | gate |
|---|---|---|---|---|---|
| A | solar path light (`stainless-steel-solar-path-light-ip65`, place word שביל) | IP65 | solar | `ens-pdp-rain-panel.jpg` | open |
| B | mains wall light (`outdoor-bidirectional-led-wall-light-ip65`, place word קיר) | IP65 | not solar | `ens-pdp-rain-stem.jpg` | open |
| C | solar floodlight (`powerful-solar-garden-light`, place word גינה) | IP67 | solar | `ens-pdp-rain-panel.jpg` | open |

The sun tile is `ens-pdp-sun-wall.jpg` in all three (R7). A and C render identically — the section reads
the IP token and the power source, never the place word — so their heights are the same by construction.

## Height of the section root (`.ens-pdp-weather`)

| archetype | 390×844 | budget | 1366×900 |
|---|---|---|---|
| A | **371 px** | ≤ 430 | 647 px |
| B | **389 px** | ≤ 430 | 647 px |
| C | **371 px** | ≤ 430 | 647 px |

B is 18 px taller because «טיפות על גבעול, אחרי הגשם» + «צילום: jenny downing (CC BY 2.0)» each wrap to
two lines in a 169 px column, where the solar pair's caption and credit take one line each.

Tile geometry, measured: **169×169 at 390** (1:1, two columns, 12 px gap inside the 350 px wrap) and
**610×407 at 1366** (3:2, 20 px gap inside the 1240 px wrap). `currentSrc` picked by the browser at
`deviceScaleFactor: 1`: the 400w candidate at 390, the 900w candidate at 1366 — every candidate is
capped at the file's real width (panel 1066, stem 1600, sun 1200), none is invented.

## Gate states (rendered byte count of the whole section)

| product | bytes printed |
|---|---|
| no IP token (`lighted-birch-branches-20-led`) | **0** |
| `IP44` only | **0** |
| no product (non-product template) | **0** |
| `IP68` + `custom.power_source = סולארי` | 4035 — panel tile |
| `IP65` + `custom.power_source = חשמל` | 4106 — stem tile |

Zero bytes means zero: no section root, no `<style>`, no wrapper and no padding.

## Contrast (`pdp2/verify/contrast.py`, background read from the `weather-bg/` no-text shots)

The harness places the section at the TOP of the ground gradient (`#0f1a2f`), which is the lightest
ground the section can ever sit on; on the real page it sits mid-template, where the ground is darker
and the ratios only improve.

| element | colour | size | 390 (p90) | 1366 (p90) |
|---|---|---|---|---|
| `__h` heading | `#f4eee3` (`--env2-ink`) | 25 / 44 px | 15.19:1 | 15.34:1 |
| `__line` (both tiles) | `#f4eee3` (`--env2-ink`) | 16 / 17 px | 16.45:1 | 17.23:1 |
| `__cap` caption | `#8f8b83` | 12 / 13 px | **5.68:1** | 5.87:1 |
| `__credit` | `#8f8b83` | 12 / 13 px | **5.72:1** | 5.90:1 |

Worst case across all three archetypes and both viewports: **5.68:1** (caption at 390). Every value is
≥ 4.5:1. Identical in A, B and C.

## Files kept here

`render.py` · `shoot.js` · `section-{A,B,C}.html` (the rendered markup) ·
`harness-{A,B,C}.html` · `weather-{A,B,C}-{390,1366}.png` · `sizes.json` ·
`../weather-bg/weather-*.png` (the same shots with the text hidden, for contrast.py).
