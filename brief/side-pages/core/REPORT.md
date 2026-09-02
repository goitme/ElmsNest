# Round 0 — shared core: integration report (2026-09-02)

Theme: `gid://shopify/OnlineStoreTheme/154726400174` — "ElmsNest - Homepage Rebuild 2026-09-01", role
**UNPUBLISHED**. Nothing was published. `templates/index.json` was not touched. No WhatsApp label was added.
Spec: `brief/side-pages/core/CORE-SPEC.md` §A–§F. This report closes §F.

Sections A–E were implemented and deployed in the previous session; this session verified them against the live
theme, ran the §F.4 acceptance with measurements, fixed four defects the measurements exposed, redeployed the one
file that changed, and re-rendered everything.

---

## 1. Repo ↔ live theme: byte-for-byte diff

Every file this round deploys was fetched from the theme (`theme(id){ files(filenames:[…]) { size checksumMd5 } }`)
and compared with the `theme/` copy. **All 38 files match**: the live `checksumMd5` equals the MD5 of the repo file
with its trailing newline stripped (the GraphQL block string drops the final newline on upsert), so live size =
repo size − 1 for every file that ends in a newline, and equal for the three that do not.

| Repo file | live size | live checksumMd5 | verdict |
|---|---|---|---|
| `snippets/elmsnest-v2-core.liquid` | 17197 | `5bcfd67401e687cb9f46f4336c484515` | match (after the §2 fix redeploy) |
| `snippets/elmsnest-v2-ground-index.liquid` | 1863 | `2ff11d9392b55cb0a09c5f3060f1a205` | match |
| `snippets/elmsnest-v2-photo-url.liquid` | 1380 | `2d50f2079c7aa72db12151e15722bbb9` | match |
| `snippets/elmsnest-v2-base.liquid` | 344 | `fd22e86f2b3243ee3476b293563ea964` | match (1-line deprecation comment) |
| `snippets/elmsnest-v2-fonts.liquid` | 1318 | `b0dc4336caf255b0154d0984edd8a959` | match |
| `snippets/css-variables.liquid` | 24265 | `6f5a37aa811259794e3c5cbdfc8f0044` | match |
| `layout/theme.liquid` | 11513 | `5a399c67536264d75e2465317cc7e7a8` | match |
| `sections/system-group.json` | 3520 | `8e3185a6efa881a4596ab0b1979bca4a` | match |
| `sections/elmsnest-v2-{hero,switch,terms,goodnight}.liquid` | 16414 / 37905 / 13047 / 15416 | — | match |
| `sections/elmsnest-v2-{atmosphere,first-lit,night-wall,places}.liquid` | 22530 / 14517 / 15229 / 14773 | — | match (untouched this round) |
| `templates/{404,blog,cart,collection,list-collections,page,page.contact-us,product.elmsnest,search}.json` | 554 / 4610 / 4006 / 3208 / 2632 / 1700 / 6868 / 25988 / 2165 | — | match |
| `templates/customers/*.json` (7 files) | 1572 / 733 / 1574 / 1488 / 1391 / 1495 / 1400 | — | match |
| `templates/index.json` | 14965 | `95c8a475255b4dcc838d7cc90cd510b5` | match — **not touched this round** |

**One formatting-only exception — `config/settings_data.json`.** Live size 9284, md5
`943f6ca0e8b456b809d826b4d6481892`; the repo copy is 13511 bytes. Shopify normalises this one file on write (it is
the platform's own settings store): the stored bytes are the compacted JSON — a compact re-serialisation of the repo
copy is 9258 bytes, 26 off the stored 9284 — while `body { content }` returns it pretty-printed. The returned live
content was compared with the repo copy key by key: identical. Same 122 keys under `current` in the same order, same
12 entries under `color_schemes` including `scheme-env2-night` with all 17 keys and the same values, same
`platform_customizations.custom_css` array with its three entries and its literal backslashes intact. No action
taken: the repo copy is the source of truth for the edit, Shopify owns the on-disk formatting.

**Hero line 7 (§A.2).** `theme/sections/elmsnest-v2-hero.liquid:7` is `{% render 'elmsnest-v2-ground-index' %}` —
it no longer renders `elmsnest-v2-fonts` or `elmsnest-v2-base`. The deployed hero has the same checksum as the repo
copy, and the mirrored HTML confirms the split at runtime: `id="env2-ground-index"` appears **once on home and zero
times on all 14 other pages**, while `id="env2-base"` (the core) and `id="env2-fonts"` appear exactly once on all 15.

---

## 2. What changed — file → lines

### Deployed before this session (§A–§E, verified above)

| File | Lines | Change |
|---|---|---|
| `snippets/elmsnest-v2-core.liquid` | new, 254 lines | §A.1 — everything page-agnostic from the old base: tokens, side-page ground (`html` / `body[class*="hdt-page-type-"]:not(.hdt-page-type-index)`), wrapper transparency, back-to-top hidden, footer font/link rules unscoped, `--f_family_1..3` → Heebo, `best-selling` sort hidden, `.hdt-badge__wrapp` hidden, the type/button/star/lamp helpers and `window.env2`. Line 1 is still the `env2-js` inline script. |
| `snippets/elmsnest-v2-ground-index.liquid` | new, 24 lines | §A.2 — the index-only dusk gradient, index wrapper transparency, first-child margin. |
| `snippets/elmsnest-v2-photo-url.liquid` | new, 18 lines | §A.5 — the one place that builds the "send a photo" URL; `wa.me` when `settings.whatsapp_number` is set, else `mailto:info@elmsnest.com` with `%20`-encoded subject and body. |
| `snippets/elmsnest-v2-base.liquid` | 238 → 1 line | §A.3 — deprecation comment only; nothing renders it. |
| `sections/elmsnest-v2-hero.liquid` | l.1–7, l.68–77 | §A.2 / §A.5 — renders `elmsnest-v2-ground-index` instead of fonts+base; `wa_href` from the snippet. |
| `sections/elmsnest-v2-switch.liquid` | l.10, l.13–17, l.147 | §A.5 — photo URL from the snippet; the `settings.whatsapp_number != blank` fallback that could print a WhatsApp label removed. |
| `sections/elmsnest-v2-terms.liquid` | l.12–14 | §A.5 — `wa_url` from the snippet. |
| `sections/elmsnest-v2-goodnight.liquid` | l.17–22 | §A.5 — `wa_href` from the snippet. |
| `layout/theme.liquid` | +l.161, +l.173–174 | §A.4 — `render 'elmsnest-v2-fonts'` after `render 'css-variables'`; `render 'elmsnest-v2-core'` after `content_for_header`, documented in an inline comment (the core must follow the section `{% stylesheet %}` bundle, as it did when the hero rendered the base). Nothing else in the file changed. |
| `snippets/css-variables.liquid` | l.73–94, l.116–119 | §D — the 26 `--en-*` values and only those. Verified by a full diff against `brief/inventory/theme-src/snippets/css-variables.liquid`: exactly two hunks, 26 lines. |
| `config/settings_data.json` | l.13, 15, 78, 97, 107 + new block at l.391–410 | §E — `color_scheme_body` / `color_scheme_dialog` → `scheme-env2-night`, `show_quick_add` → false, `hidden_badges` → true, `animations_reveal_on_scroll` → false, and the `scheme-env2-night` scheme. `badge_sale` and the fonts untouched. |
| `sections/system-group.json` | l.77, l.83 | §C — `cart-drawer.color_scheme` → `scheme-env2-night`, `discount_error_message` → "יש להזין קוד הנחה תקין". `back_top` left in place (hidden by CSS). |
| `templates/404.json` | l.15 | §B |
| `templates/blog.json` | l.12–51, l.181 | §B — `blog-slider` removed from `sections` and `order`. |
| `templates/cart.json` | l.37–38, 43–44, 121 | §B — heading scheme + `bg_overlay:0` + `image:""`; `main-cart` scheme. |
| `templates/collection.json` | l.12–29, l.131, l.61–63, l.114 | §B — `top-list-collections` removed; heading de-imaged; `main-collection` scheme. |
| `templates/list-collections.json` | l.43–45, l.82 | §B |
| `templates/page.json` | l.41, 47–48, 55 | §B |
| `templates/page.contact-us.json` | l.37, 43–44, 187 | §B |
| `templates/search.json` | l.12–30, l.96, l.57–58, 63, 87 | §B |
| `templates/product.elmsnest.json` | l.17, 228, 276 | §B — `brc-nav-product` and the two empty `color_scheme` keys → `scheme-env2-night`. The `elms-pdp-*` blocks and `main-product` were not touched. |
| `templates/customers/*.json` (7) | account 37–39, 50 · activate 15–16, 23 · addresses 37–39, 50 · login 33–35, 47 · order 34–36, 47 · register 33–35, 47 · reset_password 34–36, 47 | §B |

### Changed by this session (§F.4 fixes)

`snippets/elmsnest-v2-core.liquid` — **one block added, l.51–64**, inside the existing "Kalles chrome" area of
`<style id="env2-base">`. Nothing else in the file changed; nothing else in the theme changed.

```css
:root{--en-input-bg:17 29 51}
:root,[color-scheme]{--color-input-primary:var(--en-surface-elevated);--color-input-secondary:var(--en-color-light)}
.hdt-btn-accent{--hdt-btn-color:var(--en-text-inverse)}
:root{--color-tooltip-background:var(--en-surface-elevated);--color-tooltip-text:var(--en-color-light)}
```

All four are §D's closing instruction ("check every place that uses the `--en-*` tokens for its colour … override
that rule in the core; verify on the render, do not guess"), and all four were found by measuring the renders.

| # | Defect (measured before the fix) | Cause | After |
|---|---|---|---|
| F-1 | `page-contact`: the four form fields were a `#f4eee3` slab — 10.89 % of the desktop page, 14.75 % of mobile — with typed text at `#8f95a3`, **2.66:1**. Same fields on the account / login / register templates. | Kalles paints a field `background-color:rgb(var(--color-input-primary))` and writes it with `--color-input-secondary`; both the `:root` fallback (`css-variables` l.185–186 → `--en-text-primary` / `--en-text-muted`) and the night scheme's `input_primary` / `input_secondary` are cream-era values. | Field `#111d33`, text `#f4eee3` → **14.4:1**. `#f4eee3` on page-contact fell to 0.44 % desktop / 0.77 % mobile (text only). |
| F-2 | The `input[name="q"]` search field rendered `background:#fffdf7` — one of the two hexes §F.4 forbids outright. | `--en-input-bg: 255 253 247` was the last cream value left in the token block; §D's list did not include it. | `--en-input-bg: 17 29 51`. |
| F-3 | `cart-empty` CTA "חזור לחנות": white label on the `#ffd394` glow fill, **1.4:1** (read on the pre-fix `http-desktop-fold.png`). Same class on the cart drawer's checkout button. | Kalles hard-codes `.hdt-btn-accent{--hdt-btn-color: 255 255 255}`; under the night scheme the fill became glow. | `--en-text-inverse` (`2 3 6`) → **13.1:1**. Checked on 8 pages: every `.hdt-btn-accent` now computes `bg rgb(255,211,148)` / `color rgb(2,3,6)`; none is dark-on-dark. |
| F-4 | The swatch / tooltip bubble was ink-on-ink: `--color-tooltip-background` = `--en-color-dark` = `2 3 6` and `--color-tooltip-text` = `--en-text-inverse` = `2 3 6`, **1:1**. A §D regression — before §D the pair was brown bg / cream text. | `css-variables` l.201–202 pair two tokens that §D moved to the same value. | Bubble `#111d33`, label `#f4eee3`. Hover-only, so no static render changed. |

Homepage safety: every element these four rules touch was probed on `home` and each has a zero-size rect (they live
inside the closed cart / search / login drawers) or is hover-only, so none can move a homepage pixel — and the home
diff in §6.1 is byte-for-byte unchanged from before the fix.

---

## 3. Lint

`brief/lint.py` already carried the §F.1 extension: it globs `sections/elmsnest-v2-*.liquid`,
`snippets/elmsnest-v2-*.liquid`, `templates/*.json`, `templates/customers/*.json` and `sections/*-group.json`,
checks settings against the section schema per type (env2 sections from `theme/`, Kalles sections from the dumps in
`brief/inventory/theme-src/sections/`), and fails on the sequence of three double quotes anywhere under `theme/`.
No change was needed.

```
$ python3 brief/lint.py
LINT OK (0 issues)
```

Six informational notes remain (Kalles section types with no dumped schema, block types with no settings in a dumped
schema); they are not failures.

---

## 4. Deploy log

One file, one `themeFilesUpsert` call each, GraphQL block string, no `userErrors`:

```
snippets/elmsnest-v2-core.liquid   16808   F-1 · F-2 · F-3    userErrors: []
snippets/elmsnest-v2-core.liquid   17197   + F-4              userErrors: []
```

Live state after the deploy (`updatedAt` UTC):

| filename | size | updatedAt |
|---|---|---|
| `snippets/elmsnest-v2-core.liquid` | 17197 | 2026-09-02 13:25 |
| `snippets/elmsnest-v2-ground-index.liquid` | 1863 | 2026-09-02 09:04 |
| `snippets/elmsnest-v2-photo-url.liquid` | 1380 | 2026-09-02 09:04 |
| `snippets/elmsnest-v2-base.liquid` | 344 | 2026-09-02 09:04 |
| `snippets/elmsnest-v2-fonts.liquid` | 1318 | 2026-09-01 22:13 |
| `snippets/css-variables.liquid` | 24265 | 2026-09-02 09:17 |
| `sections/system-group.json` | 3520 | 2026-09-02 09:15 |
| `sections/elmsnest-v2-hero.liquid` | 16414 | 2026-09-02 09:05 |
| `sections/elmsnest-v2-terms.liquid` | 13047 | 2026-09-02 09:07 |
| `sections/elmsnest-v2-goodnight.liquid` | 15416 | 2026-09-02 09:08 |
| `sections/elmsnest-v2-switch.liquid` | 37905 | 2026-09-02 09:11 |
| `templates/collection.json` | 3208 | 2026-09-02 09:11 |
| `templates/search.json` | 2165 | 2026-09-02 09:11 |
| `templates/cart.json` | 4006 | 2026-09-02 09:11 |
| `templates/list-collections.json` | 2632 | 2026-09-02 09:11 |
| `templates/page.json` | 1700 | 2026-09-02 09:12 |
| `templates/page.contact-us.json` | 6868 | 2026-09-02 09:12 |
| `templates/404.json` | 554 | 2026-09-02 09:12 |
| `templates/blog.json` | 4610 | 2026-09-02 09:12 |
| `templates/customers/*.json` (7) | 733–1574 | 2026-09-02 09:12–09:14 |
| `templates/product.elmsnest.json` | 25988 | 2026-09-02 12:32 |
| `layout/theme.liquid` | 11513 | 2026-09-02 12:33 |
| `config/settings_data.json` | 9284 | 2026-09-02 09:17 |

---

## 5. Render harness

`bash brief/inventory/mirror-all.sh && bash brief/inventory/shot-all-http.sh` — 34 pages mirrored from
`https://elmsnest.com<path>?preview_theme_id=154726400174` and shot JS-enabled over localhost at 1440×900 and
390×844, deviceScaleFactor 2. Run three times: before the fix, after the F-1..F-3 deploy, after the F-4 deploy.
The numbers below are the final run, so the mirrors and PNGs on disk match the deployed theme.

---

## 6. Acceptance (§F.4)

### 6.1 Homepage unchanged

PIL mean-abs-diff, `brief/side-pages/core/before-home-*.png` (pre-round-0) vs `brief/inventory/home/http-*.png`:

| view | before px | after px | height Δ | mean abs diff | px differing >2 | max channel Δ |
|---|---|---|---|---|---|---|
| desktop fold | 2880×1800 | 2880×1800 | **0** | 0.2263 | 0.18 % | 223 |
| desktop full | 2880×17146 | 2880×17146 | **0** | 0.0552 | 0.04 % | 235 |
| mobile fold | 780×1688 | 780×1688 | **0** | **0.0** | **0 %** | **0 — pixel-identical** |
| mobile full | 780×17396 | 780×17396 | **0** | 0.1267 | 0.07 % | 235 |

Every differing pixel was located. On the desktop fold there is exactly **one** band: y 32–104, x 852–2024 (at 2×) —
the header menu. On the full pages the bands are the header (y 36–102) and the footer text (y 16386+ of 17146
desktop, y 16050+ of 17396 mobile). Nothing else differs anywhere, and no element moved: the page heights are
identical to the pixel.

The cause is §A.1's own requirement — `:root{--f_family_1..3: var(--env2-sans)}` puts the Kalles header menu and
footer in Heebo instead of the Shopify `assistant_n4`. `brief/side-pages/core/cmp-home-header-font.png` (top =
before, bottom = after) shows the same six items at the same positions in a different face. The mobile fold is
pixel-identical because the mobile header carries no menu text. **Homepage accepted: unchanged apart from the font
swap the spec asks for.**

### 6.2 Per-page table

`header legible` — the header band (y 8–64 CSS) of the desktop fold is split into glyph pixels (relative luminance
> 0.45) and ground pixels; the table gives the ground's median hex, and the contrast of the median glyph against it.
Every page was also read as an image: `brief/side-pages/core/headers-desktop-sheet.png` and
`headers-mobile-sheet.png` — the six menu items "דף הבית · קולקציות · מדריך לבחירה · שאלות נפוצות · מי אנחנו ·
יצירת קשר" are readable on every desktop fold; the mobile bar shows logo / cart / search / hamburger in ink and gold.

`cream found` — the whole full-page PNG is sampled at 1 px in 9 and matched at tolerance ±1 against `#f7f0e6`,
`#fffdf7` and `#2b2118`; the three percentages are given in that order. Anything ≤0.03 % is glyph antialiasing and
photo content, not a surface. The 12-point gutter sample per page (2 columns × 6 rows) returned only `#020306`,
`#070b15`, `#0f1a2f` and points inside product photography.

`core loaded` — `grep -c 'id="env2-base"'` on the mirrored HTML. `height` — `document.body.scrollHeight`,
desktop / mobile.

| page | header legible (ground · CR) | cream found | core loaded | height desk/mob | Liquid errors |
|---|---|---|---|---|---|
| home | yes — `#1b1a1d` (hero photo, L 0.0106 ≈ sky-2) · 13.8:1 | no — 0.000 / 0.001 / 0.012 % | 1 | 8573 / 8698 | 0 |
| coll-all | yes — `#0f1a2e` · 13.1:1 | no — 0.003 / 0.016 / 0.001 % | 1 | 2486 / 3438 | 0 |
| coll-wall | yes — `#0f192e` · 13.2:1 | no — 0.003 / 0.017 / 0.001 % | 1 | 1977 / 2479 | 0 |
| pdp-single | yes — `#0f1a2f` · 14.0:1 | no — 0.000 / 0.000 / 0.003 % | 1 | 9532 / 11915 | 0 |
| pdp-multi | yes — `#0f1a2f` · 14.0:1 | no — 0.000 / 0.001 / 0.001 % | 1 | 9599 / 11897 | 0 |
| cart-full | yes — `#0f192e` · 13.2:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 1791 / 2567 | 0 |
| cart-empty | yes — `#0f192e` · 13.2:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 1789 / 2322 | 0 |
| search-hits | yes — `#0f1a2e` · 13.1:1 | no — 0.000 / 0.001 / 0.006 % | 1 | 2559 / 3307 | 0 |
| search-none | yes — `#0e192e` · 13.2:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 1029 / 1299 | 0 |
| p404 | yes — `#0f192d` · 13.2:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 1110 / 1445 | 0 |
| page-guide | yes — `#0f1a2e` · 13.1:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 3246 / 3578 | 0 |
| page-shipping | yes — `#0f1a2e` · 13.1:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 2491 / 2819 | 0 |
| page-contact | yes — `#0f192d` · 13.2:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 1293 / 2227 | 0 |
| policy-shipping | yes — `#0f1a2e` · 13.1:1 | no — 0.000 / 0.000 / 0.000 % | 1 | 2070 / 2728 | 0 |
| coll-list | yes — `#0f192e` · 13.2:1 | no — 0.000 / 0.003 / 0.031 % | 1 | 1591 / 1517 | 0 |

Mobile grounds are the same sky-2 family (`#0f1a2e` / `#0f192d`) with menu-glyph contrast 12.4–12.5:1 on all 14 side
pages. The one row whose header ground is *not* at or below sky-2 is **home on mobile** (`#232019`, L 0.0146): that
is the hero photograph showing through the transparent header, not a painted surface, and the glyph contrast there
is 11.6:1.

Other §F.4 items, all on all 15 pages:

- **`env2-base` loaded exactly once** — `grep -c 'id="env2-base"'` = 1 everywhere; `id="env2-fonts"` = 1 everywhere;
  `id="env2-ground-index"` = 1 on home and 0 on the other 14, so the index ground is index-only as §A.2 requires.
- **FRL + Heebo requested** — one preconnect plus
  `https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500;700;900&family=Heebo:wght@300;400;500&display=swap`
  on every page.
- **`Liquid error` count 0** on every page.
- **The page ends in `#020306` before the footer** — the bottom edge pixel of every full-page PNG, sampled at six x
  positions, is `#020306` on all 15 pages in both viewports.
- **No horizontal overflow** on any page in either viewport.
- **No new JS errors.** Every page reports exactly the two known ones
  (`Failed to fetch dynamically imported module …`, `Cannot read properties of null (reading 'innerHTML')`).
  The three PDPs report a third, `<product-handle> not loaded json` — that is the mirror fetching
  `/products/<handle>.js` offline, not a theme error.
- **No WhatsApp label.** `grep -c 'בוואטסאפ'` = 0 on home and on 13 of the 15 pages; the photo-URL snippet renders
  the `mailto:` branch (`settings.whatsapp_number` is blank) three times on home — hero, terms, goodnight — the
  switch section's link is correctly suppressed because its label is blank, and `wa.me` appears nowhere. The one hit
  is on the PDPs and is pre-existing content, see §9.6.

### 6.3 Cart drawer

The `coll-all` mirror served over localhost; `/cart/add(.js)`, `/cart/update.js` and `/cart.js` stubbed with
`page.route` returning JSON; the first `form[action="/cart/add"]` submit clicked, then the dialog opened directly
because Kalles' cart module cannot load its dynamic import offline (the spec's note: what is judged is the drawer's
colours, not the network).

- `brief/side-pages/core/drawer-desktop.png` — 1440×900
- `brief/side-pages/core/drawer-mobile.png` — 390×844

Both: `<dialog id="CartDrawer" color-scheme="scheme-env2-night">` open, computed `background rgb(2,3,6)`
(`#020306`), title "העגלה שלך" in `rgb(244,238,227)` (`#f4eee3`), and the "חזור לחנות" CTA now dark ink on the glow
fill (F-3). Read as images: night ground, ink text, no cream anywhere in the panel or its scrim.

### 6.4 PDP interim sections

`elms-pdp-*` renders night / ink. The comparison table (`brief/inventory/pdp-single/http-desktop.png`, y
13200–14400) was read as an image: night cells, ink criteria, gold column rule, amber check glyphs — readable.
Buttons on glow have dark text: `.hdt-product-form__submit`, `.shopify-payment-button__button` and
`.hdt-sticky-atc__submit` all compute `--hdt-btn-color: 2 3 6` on `--hdt-btn-bg: 255 211 148`.
`pdp-sticky-desktop.png` / `pdp-sticky-mobile.png` in this folder are the sticky add-to-cart bar.

---

## 7. Evidence files

| Path | What |
|---|---|
| `brief/side-pages/core/before-home-{desktop,mobile}{,-fold}.png` | pre-round-0 homepage baseline |
| `brief/inventory/home/http-{desktop,mobile}{,-fold}.png` | homepage now |
| `brief/side-pages/core/cmp-home-header-font.png` | homepage header, before (top) vs after (bottom) — the only fold difference |
| `brief/side-pages/core/diff-home-desktop-fold.png` | the pixel diff of the desktop fold |
| `brief/side-pages/core/headers-desktop-sheet.png` | header + first heading of all 14 side pages, desktop |
| `brief/side-pages/core/headers-mobile-sheet.png` | the same at 390 |
| `brief/side-pages/core/drawer-{desktop,mobile}.png` | the open cart drawer |
| `brief/side-pages/core/pdp-sticky-{desktop,mobile}.png` | the PDP sticky bar |
| `brief/inventory/<key>/http-*.png`, `index.html`, `shot-http.log` | the 15 §F.3 pages, plus 19 more |

---

## 8. Interim, and the round that replaces it

Deliberately left as-is by §B/§D — the old Kalles sections stay, they only stop being cream:

| Item | Where | Replaced by |
|---|---|---|
| Kalles `main-collection` grid, cards and facets on `scheme-env2-night` | `templates/collection.json`, `search.json` | round 2 (collection + card rebuild) |
| `best-selling` sort option hidden by CSS instead of removed from the collection | `elmsnest-v2-core` l.49 | round 2 — the sort list is rebuilt with the collection |
| Sale badges hidden by `hidden_badges` + `.hdt-badge__wrapp{display:none}` | settings + core l.50 | round 2 |
| `show_quick_add:false` — cards link to the PDP instead of opening the cream Kalles popup | `settings_data.json` | round 2 (the card gets its own add) |
| The whole `elms-pdp-*` PDP and `main-product` | `templates/product.elmsnest.json` | round 1 (PDP) |
| `main-cart` on the night scheme, Kalles markup | `templates/cart.json` | the cart round of the side-pages plan |
| `contact-form`, `main-page`, `main-login` … on the night scheme, Kalles markup | the page and customer templates | rounds 3–6 |
| `snippets/elmsnest-v2-base.liquid` kept as a one-line deprecation comment | — | delete when nothing can reference it (end of the side-pages work) |
| `animations_reveal_on_scroll:false` | `settings_data.json` | permanent unless a later round re-introduces reveals through the `env2` lamps |

---

## 9. Open items for the lead — found, not fixed

Each of these would change something this round is told to protect, so they are reported rather than patched.

1. **`<a class="env2-btn">` loses its ink colour — homepage, pre-existing.** In `elmsnest-v2-core`,
   `.env2-section a{color:inherit}` (specificity 0,1,1) beats `.env2-btn{color:var(--env2-btn-ink)}` (0,1,0), so an
   anchor button renders `#f4eee3` on the `#ffd394` fill — **1.21:1**. Visible on the homepage hero
   ("לארבע הקולקציות"). `<button class="env2-btn">` is unaffected. The CONTRACT says the class "works on `<a>` and
   `<button>`", so this is a contract violation — but the pre-round-0 baseline renders it identically, so fixing it
   would change the homepage, which the do-not list forbids. One-line fix when the lead wants it:
   `.env2-section a.env2-btn{color:var(--env2-btn-ink)}` plus the `--ghost` pair.
2. **Notice text colours are cream-era.** `--en-warning-text: 96 64 0`, `--en-success-text: 23 90 56`,
   `--en-error-text: 145 33 42`, `--en-info-text: 26 83 108` were built for a cream page and §D did not list them.
   On the night ground they measure 2.19 / 1.4 / 1.8 / 1.7 : 1. The only one currently rendered is the warning —
   `search-none`, "לא נמצאו מוצרים התואמים את הבחירה שלך", 2.19:1
   (`brief/inventory/search-none/http-desktop.png`). Fixing it means choosing four new semantic colours, which is
   design, not round-0 engineering.
3. **Badge colour pairs are now dark-on-dark.** `--color-new-badge-background` / `-text` and
   `--color-custom-badge-background` / `-text` both resolve to `2 3 6` (1:1), and the on-sale badge is `2 3 6` on
   `145 33 42` (1.6:1). Harmless today because every badge is hidden (§E plus the core belt), but it will surface
   the moment badges come back in round 2.
4. **Product-card hover overlay labels are invisible.** "בחירת אפשרויות" / "הוסיפו להזמנה" compute `#020306` on
   `#020306` on `coll-all`, `coll-wall` and the PDP related-products row. Hover-only, so they do not appear in any
   static render; the card is rebuilt in round 2.
5. **The search drawer's category `<select>` writes `#2b2118`** (brown) on the night drawer. Inside a closed drawer
   on every page, so invisible in the renders; belongs with the header/nav round.
6. **"בוואטסאפ" on the PDP.** `templates/product.elmsnest.json` l.446 — the comparison row
   "אפשר לשאול לפני ההזמנה" has `"text_a": "בוואטסאפ"`. Pre-existing content inside an `elms-pdp-*` section, which
   §B says to leave untouched, and not a label this round added — but it does claim a WhatsApp channel the shop does
   not have. Round 1 replaces this template; if it should go sooner it is a one-string edit.
7. **Footer links render underlined** despite the core's
   `.shopify-section-group-footer-group a{text-decoration:none}` — a Kalles rule outranks it. Identical on the
   homepage and on every side page, so the §A.1 unscoping did land and this is not a round-0 regression; it needs a
   more specific selector when the footer is redesigned.
