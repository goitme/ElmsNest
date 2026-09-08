# `ens_pdp_print` — measured (build harness, 2026-09-08)

Section: `theme/sections/elmsnest-s-pdp-print.liquid` (13,915 bytes).
Harness: `render.py` renders the section file itself with python-liquid, the REAL snippets
(`elmsnest-s-place`, `elmsnest-v2-bdi-range`) and the schema's own defaults as `section.settings`;
assets resolve to `file:///home/user/ElmsNest/theme/assets/…`. Page carries the env2 `:root` tokens,
`.env2-section` / `.env2-wrap` copied from `snippets/elmsnest-v2-core.liquid`, the night ground, and
`@font-face` for Frank Ruhl Libre 400/700 + Heebo 300/400 from `brief/assets/fonts`.
Measured with `measure.js` (playwright, chromium 1194, `--no-sandbox`, deviceScaleFactor 1).

## Heights (section root `.ens-pdp-print`, border-box)

| archetype | product used | place word | print | 390×844 | 1366×900 |
|---|---|---|---|---|---|
| A — solar path light, IP65, gate open, solar pair | `stainless-steel-solar-path-light-ip65` | שביל | `ens-pdp-print-path.jpg` | **379 px** | 488 px |
| B — mains wall light, IP65, gate open, plain pair | `waterproof-led-wall-light-ip65-6w-12w` | קיר | `ens-pdp-print-wall.jpg` | **379 px** | 488 px |
| C — solar floodlight, IP67 | `dual-head-garden-light-10w-ip65` | גינה | `ens-pdp-print-garden.jpg` | **379 px** | 488 px |

Budget SPEC §5: ≤ 420 px at 390 — **passes with 41 px of headroom** on all three.
The height is identical across archetypes by construction: the mat is driven by the wrap width and the
aspect ratio, not by the file, and the caption/credit are one line each at 390.

Rendered photograph: 322×215 at 390 (3:2, bleeding to the mat's inner edge inside 14 px of cream),
619×348 at 1366 (16:9, inline-end column). `sizes="(min-width:901px) 620px, (min-width:500px) calc(92vw - 28px),
calc(100vw - 68px)"` — 620 vs the measured 619, and 322 = 390 − 2×20 gutter − 2×14 mat padding.

## srcset candidates vs the real file width (CHOSEN.md)

| asset | file | candidates emitted | max candidate |
|---|---|---|---|
| `ens-pdp-print-path.jpg` | 1200×781 | 400w 700w 1000w 1200w | 1200 = file width |
| `ens-pdp-print-wall.jpg` | 1600×1063 | 400w 700w 1000w 1300w | 1300 < 1600 |
| `ens-pdp-print-garden.jpg` | 1000×667 | 400w 700w 1000w | 1000 = file width |
| `ens-pdp-print-balcony.jpg` | 1600×1067 | 400w 700w 1000w 1300w | 1300 < 1600 |

No candidate exceeds the file. Every `<img>` carries `width`/`height`, `loading="lazy"`,
`decoding="async"` and a `sizes` matching the rendered width.

## Contrast (pdp2/verify/contrast.py on these screenshots, ≥ 4.5:1 required)

| text | colour | ground | p50 | p90 |
|---|---|---|---|---|
| `.ens-pdp-print__cap` (caption, 11 px) | `#6b6558` | mat `#efe7d8` | 4.71:1 | **4.71:1** |
| `.ens-pdp-print__credit` (credit, 11 px) | `#6b6558` | mat `#efe7d8` | 4.71:1 | **4.71:1** |
| `.ens-pdp-print__line` (serif sentence, 19 px / 27.3 px) | `#f4eee3` (`--env2-ink`) | night ground | 15.21:1 | **15.10:1** (390) · 15.06:1 (1366) |

Worst p90 across all six shots: 4.71:1 — the spec's `#6b6558` on `#efe7d8` passes as written, so the
ink token was **not** adjusted.

## Closed gate (`gate-check.py`)

Renders to the empty string — no root, no `<style>`, no wrapper, no padding — for: a product with no
place collection (`sale` only), `lighted-birch-branches-20-led`, `rechargeable-telescopic-camping-lantern`,
and a page with no product.

## Files here

`render.py` · `measure.js` · `gate-check.py` · `archetype-{A,B,C}.html` · `sizes.json` ·
`print-{A,B,C}-{390,1366}.png`
