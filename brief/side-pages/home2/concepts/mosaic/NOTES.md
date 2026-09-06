# Concept «mosaic» — one section, one mosaic

## What it is
One new section, **«איך זה עובד»** (`sections/elmsnest-s-home-mosaic.liquid`), inserted between «מתי כן, ומתי לא» and the terms
strip. A 4×3 photograph grid on desktop — one big cell (the store's own bollards at night), its daytime twin beside it, a
panel-and-string frame, a cold winter dusk, a fence of crystal bulbs and a band of lamps down stone steps. Three notes are
woven into the grid as grid cells that share an area with a photograph (align-self: end, a scrim gradient) — no absolute
positioning, no JS:

- the solar fact over the night frame: «ביום נטען. בלילה נדלק.» + three tiny sentences (seed 1)
- the winter note over the winter frame: «ובחורף?» (seed 3)
- the guide question over the steps: «לפני שקונים», three questions, the page's one guide link (seed 2)

The page reads text → photos → text around it (fit block → mosaic → terms), and the guide link moves one section down
(fit's `guide_label` blank in `templates/index.json`).

## Phone (390)
The grid collapses to two columns: the day/night pair as two small squares with their «ביום / בלילה» tags, the solar note
as a plain row under them, the winter note as a sky-blue text tile (its photograph hidden), then the steps band with the
questions and the guide link over its foot. Three photographs shown, three hidden by CSS. Top to bottom it is one story:
by day it charges · by night it lights · but winter · so ask these three · guide.

## Measured (playwright, getBoundingClientRect, real fonts)
- 390×844: section **656 px** (grid 538 px) — under the 675 cap; the page grows from 5.12 to ≈ 5.9 screens.
- 1366×900: section 878 px (grid 676 px) — the whole section fits the desktop fold.
- No horizontal overflow at either width.

## What it refuses
- A second section. The owner asked for 2–3 sections of image-led content; this gives three seeds' content in one grid so
  nothing is answered twice and the page stays short. If the count matters more than the length, the winter cell can be
  lifted out as its own 300 px band without changing anything else.
- Any mains wall-light frame: «בלי כבל» must be true of every product in the grid, so only solar frames are in it.
- Reviews, numbers, hours, lumens, IP claims, urgency; a fifth place list; a second contact line; a second product grid.
- CC BY frames: every image here is store-owned or CC0, so no credit caption is needed.
- Carousels, parallax, lamps that light on scroll, hover reveals. The only transition is the stock link colour.

## Engineering
- One Liquid section, `{% schema %}` with `image_picker` for the six frames (theme assets `ens-home-mosaic-*.jpg` as the
  default rendering when a picker is empty), `text` settings for the heading, the two tags, the three notes and the link.
- Images `loading="lazy"` with width/height; `asset_img_url` sizes 400/800/1200.
- Tokens only: `--env2-*` colours, `--ens-card` / `--ens-hair` from the skin, radius 0, logical properties, RTL grid
  (column 1 is the right edge). Reduced motion respected.
