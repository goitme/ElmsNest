# Home, round 2 — SPEC (2026-09-06): three image-led sections

> **Amended after the critique of the deployed render** (`critique/LEAD-DECISIONS.md`, 2026-09-06): section A has a
> heading instead of an eyebrow, no corner labels by default, ONE line under the frames instead of three numbered
> steps, desktop crops per frame (day and night «50% 30%»); the band's desktop crop is «50% 35%» (40% after the critique,
> 35% after the post-fix re-review — one bulb was still cut at the top edge); the winter figure has no border and the
> neighbours' heading scale. The amended text is inline below; the original wording is in git (b27711c).

Lead's synthesis after five concepts and five judges (`concepts/`, ranking dusk 50.75 · kinds 43.5 · band 41.5 ·
questions 39 · mosaic 38.5; every judge put **dusk** first). Built: dusk's two sections, with the fixes the judges
asked for, plus band's single best screen as the page's breath. Three sections, all photographs the store's own
product frames, no credit lines owed, nothing on the page answered twice.

## 1. The sections and where they go

`templates/index.json` order becomes: `env2_hero` → `ens_collections` → `ens_products` → **`ens_home_solar`** →
**`ens_home_winter`** → `ens_fit` → **`ens_home_band`** → `ens_terms`. Rhythm: photos (tiles, cards) → the diptych
with three steps → the winter note → the text rows → one full-bleed photograph with one sentence → the three
numbers → footer. Nothing existing changes (the fit block keeps its guide link and its contact line).

| # | section file | template id | at 390 (cap) | what |
|---|---|---|---|---|
| A | `sections/elmsnest-s-home-solar.liquid` | `ens_home_solar` | ≤ 520 px (dusk measured 481; built 499, amended ≈ 440) | heading · day/night diptych with the headline split across the frames · one line |
| B | `sections/elmsnest-s-home-winter.liquid` | `ens_home_winter` | ≤ 520 px | «ובחורף?» — the rainy-evening frame + heading + three lines |
| C | `sections/elmsnest-s-home-band.liquid` | `ens_home_band` | ≤ 520 px (band measured 520) | one full-bleed photograph, one sentence, nothing else |

Page estimate at 390×844: 4321 px now + ≈ 1500 px = ≈ 6.9 screens (cap 7.5). Each section is `loading="lazy"`
photographs with `width`/`height` attributes (no layout shift).

### A — `elmsnest-s-home-solar` («ElmsNest S — סולארי»)

Layout (from `concepts/dusk`, desktop shot is the reference): heading «איך עובדת תאורה סולארית?» in the neighbours'
`env2-h` scale (`clamp(25px,3.4vw,44px)`; the honesty critique measured the original 13 px eyebrow as too weak to
scope the facts to solar products — the scope word now sits at heading weight, and the question form leads into
«ובחורף?»); a two-frame figure grid — **day frame on the inline-start (right in RTL), night frame on the
inline-end** — the headline sitting on each frame's foot on a bottom scrim (corner labels «יום»/«לילה» exist as
settings `label_day`/`label_night` but are EMPTY by default: the headlines already say day and night, and the
critique measured the day label at 1.2–1.8:1 on the foliage; a typed label renders on a `.85` night backing): day frame «ביום נטען.» in cream, night frame «בלילה נדלק.» in glow, Frank Ruhl Libre 700, 28 px at
390 / 44 px at ≥ 901. Frames: 4:5 at 390 (two side by side, 4 px gutter), 16:10 at ≥ 901. Scrim: the day frame is
bright, so its scrim is `linear-gradient(180deg, transparent 45%, rgba(5,8,14,.78) 100%)` — lighter than the
mockup's .86 so it does not turn to mud at 1366 (designer); the headline sits on the pavement's shadow; the night
frame's scrim is `rgba(5,8,14,0) 36% → rgba(5,8,14,.84)` (measured 6.4:1 behind the glow headline at 360). Under
the frames ONE line on hairlines (fit block hairlines): «בלי חיבור לחשמל, בלי חשמלאי.» — settings `line_1` (that
default), `line_2`, `line_3` (empty). The three numbered steps of the first build were cut by the critique: «ביום
נטען.» was step 1, «בלילה נדלק.» plus the hero's «כשהשמש יורדת, הגינה נדלקת.» were step 2 (the owner's «nothing
twice»), and «בלי כבל» was not true of the separate-panel products (the listings say «בלי חיבור לחשמל»). No
button, no link, no card chrome. Desktop crops per frame: `object_position_day_desktop` «50% 30%» and
`object_position_night_desktop` «50% 30%» (≥ 901, 16:10 — the nearest panel crown and the far lamp heads were
cut at 50%/40%; the re-review found the day frame's second and third heads still cut at 40%, so both frames take 30%).

Images: day = `assets/ens-home-day.jpg` (store frame `own_powerful-solar-garden-light_3`, full 1254² — panel on
every head, lamps off); night = `assets/ens-home-night.jpg` (store frame `own_powerful-solar-garden-light_2`
**pre-cropped to the top 1090 px** so the baked caption at its foot is gone from the file itself — the engineer's
and the honesty judge's fix: no CSS crop hides anything, and an owner-picked replacement gets a plain
`object-position` setting per frame, default «50% 50%» day / «50% 40%» night).

### B — `elmsnest-s-home-winter` («ElmsNest S — חורף»)

The seasonal half of the store's honesty, right after the three steps. Layout: at 390 the photograph is a 16:9
band on top (full width of the wrap, ≈ 200 px) and the text below it on the night ground; at ≥ 901 the
photograph takes the inline-end half (16:10) and the text sits in the inline-start half, vertically centred.
Text: heading «ובחורף?» (Frank Ruhl Libre 700, the neighbours' `clamp(25px,3.4vw,44px)`; no border on the figure — photographs on this page carry no frame) then three lines, Heebo 300, 16 px / 17 px, ink:
«בחורף השמש קצרה יותר, והפאנל נטען פחות.» · «פחות טעינה ביום, פחות אור בלילה.» · «זה נכון לכל תאורה סולארית,
גם שלנו.» (the last line is the brand's honesty said out loud — every judge asked for it). No link.

Image: `assets/ens-home-winter.jpg` = store frame `own_modern-solar-path-lights-set_6` **pre-cropped to
x 150 · y 450 · 1100 × 580** (the rainy evening: wet stone path, the store's bollards on wet lawn, lit windows
in the rain; the marketing headline, badge and icon strip of the source are outside the crop). Store-owned; no
credit. It replaces dusk's CC0 public-park frame, which the owner and shopper judges both flagged as somebody
else's lamps.

### C — `elmsnest-s-home-band` («ElmsNest S — נשימה»)

From `concepts/band` §A, the judges' single best screen: one full-bleed photograph (edge to edge at every width),
`min-block-size` 520 px at 390 / 560 px at ≥ 901, and ONE sentence «חושך הוא לא סוף הערב.» in glow serif
(34 px / 52 px), bottom inline-start inside the wrap, on the dark fence — no scrim, or at most a 30 % bottom
fade if the render needs it for 4.5:1. No eyebrow, no link, no button. Image: `assets/ens-home-fence.jpg` = store
frame `own_solar-crystal-ball-string-lights_5` (crystal bulbs on a picket fence at blue hour, bougainvillea,
city bokeh), full 1254², `object-position` default «50% 50%» at 390 and «50% 35%» at ≥ 901 (measured: at 60% the lower
string of bulbs ran through the sentence, 3.5:1; at 40% the sentence sits on the dark boards, 6.6:1, but one bulb of the top
string was cut at the top edge; 35% keeps it whole; a heavier fade only reached 4.6:1 and dirtied the frame). The img is in
flow (520 / 560 px tall) so the figure's height is the photograph's. Store-owned.

## 2. Copy — every Hebrew sentence, verbatim (guillemets are notation)

| where | text | source / why it is claim-free |
|---|---|---|
| A heading | «איך עובדת תאורה סולארית?» | question; the scope word |
| A headlines | «ביום נטען.» · «בלילה נדלק.» | how any solar light works |
| A line | «בלי חיבור לחשמל, בלי חשמלאי.» | the listings' own phrase; a solar light has no mains connection (a floodlight's panel lead is not one) |
| ~~A labels~~ | ~~«יום» · «לילה»~~ | settings, empty by default (critique #1) |
| ~~A steps 1–3~~ | ~~«הפאנל נטען לאור היום.» · «כשמחשיך, האור נדלק לבד.» · «בלי כבל, בלי חשמלאי.»~~ | cut (critique #3, #4) |
| B heading | «ובחורף?» | question |
| B lines | «בחורף השמש קצרה יותר, והפאנל נטען פחות.» · «פחות טעינה ביום, פחות אור בלילה.» · «זה נכון לכל תאורה סולארית, גם שלנו.» | physics of daylight; the honest note |
| C sentence | «חושך הוא לא סוף הערב.» | a sentence, not a claim |

Rules: no «+», no «;», sentences keep their period, headings have none (a question mark is not a period); every
digit/Latin token inside Hebrew in `<bdi dir="ltr">` (none on the page since the numerals went). `alt` on every image is empty (decorative;
the text carries the meaning) — the owner can set an alt through a setting if he wants one.

## 3. Images — theme assets on the DEV theme

| asset | source frame | crop | credit |
|---|---|---|---|
| `assets/ens-home-day.jpg` | `own_powerful-solar-garden-light_3` | none | none — store-owned |
| `assets/ens-home-night.jpg` | `own_powerful-solar-garden-light_2` | top 1254 × 1090 | none — store-owned |
| `assets/ens-home-winter.jpg` | `own_modern-solar-path-lights-set_6` | 150,450 → 1100 × 580 | none — store-owned |
| `assets/ens-home-fence.jpg` | `own_solar-crystal-ball-string-lights_5` | none | none — store-owned |

Prepared by `images/prepare-assets.py` (≤ 1800 px, JPEG ≤ 220 KB, progressive), uploaded with `themeFilesUpsert`
BASE64, ledger in `images/CHOSEN.md`. Rendered with `asset_img_url` sizes 600/900/1200/1600 and `sizes`
matching the layout; `width`/`height` attributes from the real file. Nothing goes to the store's Files library.
The four frames are the owner's own product photographs (secondary images of three listings), so no image on the
page pretends to be anything but the store's products — the round's honesty rule met by construction.

## 4. File rules

- Each section: `{% schema %}` in Hebrew with a setting for EVERY text (`text` / `textarea`, defaults = §2) and an
  `image_picker` per photograph (`image_day`, `image_night`; `image`; `image`) + a `text` `object_position` per
  photograph (default per §1). When the picker is empty the theme asset renders. `"class": "ens-home-section
  hdt-section"`, `"presets": [...]`, `"enabled_on": {"templates": ["index"]}`. Section root `<section
  class="env2-section ens-home-solar" dir="rtl">` etc.; logical properties only; radius 0; no JS; reduced-motion
  block even if empty of transitions; `<style>` inside the section (like `elmsnest-s-fit`).
- `templates/index.json`: three new entries with type = section file name, settings as §4 defaults where the
  spec differs from the schema default (it does not — omit settings, keep `"settings": {}`), and the new order.
  Keep the /* */ header. Nothing else in the file changes.
- No edit to `elmsnest-s-fit`, the skin, core, or any Kalles file. Lint clean.

## 5. Acceptance (verify-mirror.js on the re-mirrored home, 390×844 / 360×640 / 1366×900, JS on and off)

- home ≤ 7.5 screens at 390×844 (was 5.12); each new section ≤ 520 px at 390 (measured `sections[].h`).
- Every text painted over a photograph ≥ 4.5:1 against the brightest tenth of its true background at 360, 390 and
  1366 (`home2/shoot-sections.js` + `--hide-text`, `home2/verify/contrast.py`).
- Every SIMPLIFY §11 home check still holds: terms strip = 1, «תמונה של המקום» in main = 1, mailto in main = 1,
  the four places in the same order everywhere, 0 WhatsApp, 0 glyph plates, 0 Liquid errors, no overflow-x,
  reduced-motion clean.
- The three sections render their four images (`img` count in each section = 2 / 1 / 1, each with width and
  height attributes and `loading="lazy"`); the mirror's request log shows the four assets served from the theme.
- Copy on the page byte-identical to §2 (grep the mirror). No new counts, ranks, claims.
- The fold shots at 390 show: the diptych headline legible on both frames (cream ≥ 4.5:1 on the day scrim);
  the fence sentence legible; the winter text on the night ground under the photograph.
