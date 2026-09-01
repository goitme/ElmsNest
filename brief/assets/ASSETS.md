# Local asset pack (for offline mockups)

Reference everything RELATIVELY from your mockup file. From `brief/concepts/<key>/index.html`
the paths are `../../assets/...`.

- `fonts.css` — @font-face rules for 12 Hebrew-capable families, local woff2. Include with
  `<link rel="stylesheet" href="../../assets/fonts.css">`. Families: Heebo, Rubik,
  Frank Ruhl Libre, Suez One, Secular One, Karantina, Bellefair, Assistant, Miriam Libre,
  Noto Serif Hebrew, David Libre, Alef.
- `img/<handle>-<0..3>.jpg` — product images, ≤1000px. Index 0 = Shopify featured image
  (often a marketing creative with baked-in text); 1–3 are alternates, usually cleaner.
  Handles are in `../catalog.json`.
- `img/collection-{path,wall,spot,decor}.jpg` — the four collection images (night scenes).
- `img/hero-desktop.webp` (2000×1125), `img/hero-mobile.webp` (750×900) — the current hero photos.
- `img/logo.png` — ElmsNest mark, gold on transparent-ish dark, 800×800.

Screenshot your mockup with:
`node /home/user/ElmsNest/brief/shot.js <your index.html> <out-prefix>` → writes
`<out-prefix>-desktop.png`, `-mobile.png`, plus `-desktop-fold.png` / `-mobile-fold.png`
(first screen only). Then Read the PNGs to check your own work before returning.
