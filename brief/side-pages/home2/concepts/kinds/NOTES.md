# Concept «kinds» — what light does what

## The idea

Two sections about the light itself — not the place (the tiles and the fit block own that) and not the product
(the cards own that). **[A]** is a 2×2 mosaic of four tightly cropped square photographs, one per kind of light
— a pool on the ground, a wash on a wall, a beam aimed at a point, a string overhead — with the kind-word set in
serif on the frame and one plain line under it. The photographs do the talking; the copy only names what the eye
already sees. **[B]** is the one solar fact in one sentence over one wide frame: the panel on its spike at the
foot of a trunk, and the rope light it feeds spiralled up the tree — «מה שהשמש טוענת ביום, נדלק לבד בערב.»

Editorial and graphic: 2 px gutters inside the mosaic, radius 0, gold kind-words, cream lines, no card chrome, no
button, no link. All five frames are the store's own images, so the sections need no credit line and the owner can
swap any of them from the section settings.

## Where the sections go (`templates/index.json`)

- **[A] `elmsnest-s-home-kinds`** — after «מה שנדלק ראשון» (cards), before «מתי כן, ומתי לא» (fit). The buyer has
  seen where (tiles) and what (cards); A says *what kind of light* before the fit block says when it fits. It is
  kept away from the fit block's four place rows so the four kinds never read as the four places again.
- **[B] `elmsnest-s-home-solar`** — after the fit block, before the terms strip. Fit ends on the guide link and the
  contact line; B is one full-bleed breath of photograph with the category's one fact, then the numbers.

Rhythm at 390 becomes: photo (hero) → photos (tiles) → photos (cards) → **mosaic + lines (A)** → text (fit) →
**one photo + one sentence (B)** → text (terms) → footer.

## Measured heights (playwright, `getBoundingClientRect`, fonts and images loaded)

| section | 390 × 844 | 1366 × 900 |
|---|---|---|
| [A] ens-home-kinds | **656.69 px** | 696 px |
| [B] ens-home-solar | **487.50 px** | 540 px |

Both ≤ 675 px (0.8 screen). Page in the mockup at 390: 5485 px = **6.50 screens** (was 5.12; the two sections add
1164 px including B's 8 px top margin) — under the 7.5 cap. Horizontal scroll width = 390 / 1366, nothing bleeds.

Shots: `shots/m-fold.png` (390×844, scroll 0 of A), `shots/m-full.png`, `shots/d-fold.png` (1366×900 of A),
`shots/d-full.png`; plus `shots/m-solar.png` and `shots/d-solar.png`, the same two viewports scrolled to B, so
the second section can be judged at fold size too.

## What it refuses

- A third section. Four kinds and one fact is the whole concept.
- A caption that says more than its photo: the beam frame shows a spot aimed at planting, so its line says «aimed
  at one point», not «up into the tree».
- Any product claim: no hours, no lumen, no IP, no «all our lights». S7 is a category fact (COPY.md).
- A fifth place list, a second product grid, a second guide link, a second contact line, prices, a button.
- Editing images: crops are CSS only; the baked sign (beam frame) and badge (solar frame) are cropped out by the
  box, never retouched.
- Motion: none. No carousel, no parallax, no scroll-lamps, no hover reveal; reduced-motion has nothing to switch off.
- Daylight photographs, faces, foreign brand marks, generated imagery.

## Engineering notes (P1–P7)

- Stock patterns: a `<section>` with a heading and four `<figure>`s in a CSS grid; B is one `<figure>` with a
  `<figcaption>`. Works with JS off; no JS is added.
- Mosaic grid: at ≤ 900 px the figures are `display: contents` and photo / caption cells are placed by `grid-area`
  so captions form a row under each pair of frames; at ≥ 901 px each figure is a block, the caption moves inside
  the frame over the scrim, and the heading sits beside the mosaic in a two-column wrap (heading on the start side).
- Crops: `object-fit: cover` + `object-position` for the focus + `transform: scale()` with `transform-origin` at the
  same point. Both are plain CSS; the `<img>` keeps `width`/`height` and `loading="lazy"`. The crop origins are
  written as two custom properties per frame (`--o`, `--z`) so the Liquid section can expose them as settings.
- Text on photographs: bottom scrim `rgba(5,8,14,.78–.9)`; kind-words in `--env2-glow` (≥ 8:1 on the scrim), lines
  in `--env2-ink` / `--env2-ink-2` (≥ 7:1). On desktop the solar sentence sits on the end side (left), over the dark
  sofa corner, with a side scrim — the lit trunk is on the right of that frame.
- Logical properties throughout (`inset-inline-*`, `padding-block`, `margin-block`), `dir="rtl"`, radius 0.
- Liquid: every text and every image becomes a section setting (`image_picker` empty → theme asset default via
  `asset_img_url`); the mosaic has four blocks (word + line + image + focus) so the owner can reorder or swap a
  kind. Template edit = `templates/index.json` only. Nothing published to the live theme.
- Weight: five JPEGs, each ≤ 220 KB, all below the hero, lazy. The 1:1 tiles never render above 560 px, so they
  can ship at 1000 px square.
