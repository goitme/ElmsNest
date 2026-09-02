# Round 0 — shared core: integration report (2026-09-02)

Theme: `gid://shopify/OnlineStoreTheme/154726400174` — "ElmsNest - Homepage Rebuild 2026-09-01", role
**UNPUBLISHED**. Nothing was published. `templates/index.json` was not touched. No WhatsApp label was added.
Spec: `brief/side-pages/core/CORE-SPEC.md` §A–§F. This report closes §F.

Sections A–E were implemented and deployed in the previous session; this session verified them against the live
theme, ran the §F.4 acceptance with measurements, fixed four defects the measurements exposed, redeployed the one
file that changed, and re-rendered everything.

> **A second verification pass then found ten more items (2 must, 8 should). They were reproduced, fixed and
> re-verified — see [§10 Fix pass](#10-fix-pass-second-verification-round-2026-09-02-1414-1431-utc) at the end of
> this report. §2, §6.2, §6.3, §6.4, §7 and §9 below have been corrected in place where that pass proved them
> wrong; every correction is marked `[fix pass]` and cross-referenced to the finding id.**

---

## 1. Repo ↔ live theme: byte-for-byte diff

Every file this round deploys was fetched from the theme (`theme(id){ files(filenames:[…]) { size checksumMd5 } }`)
and compared with the `theme/` copy. **All 38 files match**: the live `checksumMd5` equals the MD5 of the repo file
with its trailing newline stripped (the GraphQL block string drops the final newline on upsert), so live size =
repo size − 1 for every file that ends in a newline, and equal for the three that do not.

| Repo file | live size | live checksumMd5 | verdict |
|---|---|---|---|
| `snippets/elmsnest-v2-core.liquid` | 21614 | `87f570fb1f007d4a0fa5102090377ae9` | match — **[fix pass]** value, after the §10 redeploy (was 17197 / `5bcfd674…`) |
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
| `templates/product.elmsnest.json` | l.17, 228, 276 | §B — **[fix pass, R0-02] corrected.** Three lines changed, not one: l.17 is the `breadcrumb` section (`brc-nav-product`) that §B allows; **l.276 is `main-product`'s own `color_scheme`** and **l.228 is `main-product`'s static `main-product-sidebar` block (`_product_sidebar`) `color_scheme`** — both went from `""` to `scheme-env2-night`. §B says to leave `main-product` untouched, so this is a carve-out that needs the lead's sign-off (§10 R0-02). It is not load-bearing: with `""` the PDP still renders night (measured), just one step lighter. |
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
| F-1 | `page-contact`: the four form fields were a `#f4eee3` slab — 10.89 % of the desktop page, 14.75 % of mobile — with typed text at `#8f95a3`, **2.66:1**. Same fields on the account / login / register templates. | Kalles paints a field `background-color:rgb(var(--color-input-primary))` and writes it with `--color-input-secondary`; both the `:root` fallback (`css-variables` l.185–186 → `--en-text-primary` / `--en-text-muted`) and the night scheme's `input_primary` / `input_secondary` are cream-era values. | Field `#111d33`, text `#f4eee3` → **14.4:1**. `#f4eee3` on page-contact fell to 0.44 % desktop / 0.77 % mobile (text only). **[fix pass, V-5]** measured on `page-contact` only — the account / login / register templates are never rendered by this storefront (§10 V-5), so the rule reaches them in CSS but there is no render to show. |
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

**[fix pass, V-1]** the `cream found` column samples the *page*; it did not open the header search drawer, which
is on every one of these 15 pages and was itself painted in Kalles' cream `scheme-1`. Fixed and re-measured in
§10 V-1; the drawer is now `#020306` on all 15.

**[fix pass, V-5]** the seven `templates/customers/*.json` files §B edited are **not represented in this table and
cannot be** — this storefront is on Shopify's *new customer accounts*: `/account/login` and `/account/register`
(with the preview token) answer `302 → https://shopify.com/68949278894/account?locale=he…`, and that endpoint
returns `406 Not Acceptable` to the mirror. `brief/inventory/account-{login,register}/index.html` are 14-byte
"Not Acceptable" strings (`mirror-all.log`: `mirrored 0/0 assets … (0 KB)`), and the four PNGs that sat beside
each of them were screenshots of that error text — they have been deleted and replaced by a `FAILED-MIRROR.txt`.
Those seven template edits are inert; see §8 and §10 V-5.

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

**[fix pass, R0-03] this section was taken on the EMPTY drawer and has been redone on a populated one.** The
original `drawer-{desktop,mobile}.png` showed "העגלה שלך ריקה" and a single "חזור לחנות" CTA, so the controls this
round actually changed (line-item row, qty stepper, subtotal, `.hdt-btn-accent` checkout button) were never
rendered. Both the empty and the populated drawer are now shot from post-fix-pass mirrors — see §10 R0-03 for the
populated measurements. Summary:

| shot | mirror | what is in it | drawer bg | cream |
|---|---|---|---|---|
| `drawer-{desktop,mobile}.png` | `brief/inventory/coll-all` (empty cart) | empty state, "חזור לחנות" CTA | `rgb(2,3,6)` | 0 % / 0 % |
| `drawer-full-{desktop,mobile}.png` | `brief/inventory/cart-drawer` (mirrored with a 3-item cart cookie) | 2 line items, qty steppers, subtotal 429.70 ₪, view-cart + checkout | `rgb(2,3,6)` | 0 % / 0 % |

Both: `<dialog id="CartDrawer" color-scheme="scheme-env2-night">` open, computed `background rgb(2,3,6)`
(`#020306`), title "העגלה שלך" in `rgb(244,238,227)` (`#f4eee3`). On the populated drawer the checkout button
computes `rgb(2,3,6)` on `rgb(255,211,148)` (F-3, **14.7:1**) and the view-cart button `rgb(26,18,6)` on the same
glow. Read as images: night ground, ink text, no cream anywhere in the panel or its scrim.

The drawer's discount field is **not rendered at all** — `sections/system-group.json` carries
`show_cart_discount: false` — so §C's `discount_error_message` string is stored but inert until that setting is
turned on. Noted for the cart round.

### 6.4 PDP interim sections

`elms-pdp-*` renders night / ink. The comparison table (`brief/inventory/pdp-single/http-desktop.png`, y
13200–14400) was read as an image: night cells, ink criteria, gold column rule, amber check glyphs — readable.
Buttons on glow have dark text: `.hdt-product-form__submit`, `.shopify-payment-button__button` and
`.hdt-sticky-atc__submit` all compute `--hdt-btn-color: 2 3 6` on `--hdt-btn-bg: 255 211 148`.
`pdp-sticky-desktop.png` / `pdp-sticky-mobile.png` in this folder are the sticky add-to-cart bar — **[fix pass,
V-3] both were re-shot** (the previous pair was 3 h 46 m older than the deploy they claimed to evidence and showed
a cream bar with a brown button). Measured on the current pair: bar `rgb(2,3,6)`, label `rgb(244,238,227)`, submit
"הוסיפו להזמנה" `rgb(26,18,6)` on `rgb(255,211,148)`; `#f7f0e6` = 0.000 %, `#2b2118` = 0.001 % desktop / 0.000 %
mobile.

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
| `brief/side-pages/core/drawer-{desktop,mobile}.png` | the open cart drawer, empty cart (re-shot in the fix pass) |
| `brief/side-pages/core/drawer-full-{desktop,mobile}.png` | **[fix pass, R0-03]** the open cart drawer with two real lines |
| `brief/side-pages/core/pdp-sticky-{desktop,mobile}.png` | the PDP sticky bar — **[fix pass, V-3]** re-shot from the current mirror |
| `brief/side-pages/core/search-drawer-{desktop,mobile}.png` · `search-drawer-mobile-before.png` | **[fix pass, V-1]** the header search drawer, after / before |
| `brief/side-pages/core/ask-modal-{desktop,mobile}.png` · `ask-modal-mobile-before.png` | **[fix pass, V-4]** the "שאל שאלה" modal, after / before |
| `brief/side-pages/core/v2-card-btn-390-{before,after}.png` · `v2-collall-mobile-band-after.png` | **[fix pass, V-2]** the product-card action button at 390 |
| `brief/side-pages/core/v6-search-none-after.png` | **[fix pass, V-6]** the no-results notice on the night ground |
| `brief/side-pages/core/cmp-home-footer-links.png` | **[fix pass, R0-01]** homepage footer links, before (top) vs after (bottom) |
| `brief/side-pages/core/tools/*.{js,py}` | the fix-pass harness: `accept.py`, `dialog-probe.js`, `drawer-shot.js`, `sticky-shot.js`, `header-sheet.py` |
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
| **[fix pass, V-5]** the 7 `templates/customers/*.json` edits are **inert** — the store uses Shopify's new customer accounts, so `/account/*` redirects off the theme and those templates never render | `templates/customers/*.json` | nobody: the lead should decide whether to keep the edits as dead code or drop them from the round's scope |
| **[fix pass, R0-02]** `main-product` and its `_product_sidebar` block were put on `scheme-env2-night`, which §B told us not to touch | `templates/product.elmsnest.json` l.228, l.276 | round 1 (PDP) — but the lead should sign the carve-out off now, or ask for a revert; both states render night (§10 R0-02) |

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
2. **Notice text colours are cream-era — ~~open~~ PARTLY CLOSED [fix pass, V-6].** `--en-success-text: 23 90 56`,
   `--en-error-text: 145 33 42` and `--en-info-text: 26 83 108` were built for a cream page, §D did not list them,
   and on the night ground they still measure 1.4 / 1.8 / 1.7 : 1. **None of the three is rendered anywhere in the
   15 pages** — choosing three new semantic colours is design, not round-0 engineering, so they stay open.
   `--en-warning-text` was the one that *was* rendered (`search-none`, "לא נמצאו מוצרים התואמים את הבחירה שלך",
   2.19:1) and has been fixed: `:root{--en-warning-text:255 211 148}` in the core, measured **14.73:1** on the
   current render — `brief/side-pages/core/v6-search-none-after.png`. That is a token swap onto the amber the
   design system already owns, not a new colour decision.
3. **Badge colour pairs are now dark-on-dark.** `--color-new-badge-background` / `-text` and
   `--color-custom-badge-background` / `-text` both resolve to `2 3 6` (1:1), and the on-sale badge is `2 3 6` on
   `145 33 42` (1.6:1). Harmless today because every badge is hidden (§E plus the core belt), but it will surface
   the moment badges come back in round 2.
4. **~~Product-card hover overlay labels are invisible.~~ CLOSED [fix pass, V-2] — and the "hover-only, so they do
   not appear in any static render" claim was wrong.** `.hdt-card-product__btn-ultra` computed `#020306` on
   `#020306` (1:1). On a pointer device it is revealed on card hover, but **at 390 there is no hover state to wait
   for, so it painted an opaque `#020306` square over the photo on every card** — measured on a faithful 390
   viewport render before the fix: `visibility: visible`, `background-color: rgb(2,3,6)`, `color: rgb(2,3,6)`,
   3037 px of `#020306` in one 90×45 device-px box over a product photograph
   (`brief/side-pages/core/v2-card-btn-390-before.png`). Fixed in the core: legible pair for the pointer case
   (`rgb(2,3,6)` on `rgb(255,211,148)`, 14.7:1) and `visibility:hidden` under `(hover:none),(max-width:900px)`,
   which is where the card already links to the PDP and `show_quick_add` is off. After:
   `v2-card-btn-390-after.png` (photo, no square) and `v2-collall-mobile-band-after.png`. Page heights unchanged.
5. **~~The search drawer's category `<select>` writes `#2b2118`.~~ CLOSED [fix pass, V-1] — and it understated the
   defect by an order of magnitude.** The `<select>` was the small half of it: the whole panel
   (`<hdt-predictive-search … color-scheme="scheme-1">`, present on all 15 pages) was painted in Kalles' cream
   `scheme-1` — `#f7f0e6` ground, `#fffdf7` background2, `#2b2118` foreground, i.e. the three hexes §F.4 forbids.
   Measured before: `#drawer-search-form` `background-color: rgb(247,240,230)`, 84.17 % of the open panel at 390 /
   22.18 % at 1440. Fixed by remapping `[color-scheme="scheme-1"]` onto the night pair in the core (the attribute
   is hard-coded in a Kalles core section, so `settings.color_scheme_dialog` cannot reach it). After: panel
   `rgb(2,3,6)`, `<select>` `rgb(244,238,227)` on `rgb(17,29,51)` (14.6:1), cream 0.00 % in both viewports —
   `brief/side-pages/core/search-drawer-{desktop,mobile}.png`.
6. **"בוואטסאפ" on the PDP.** `templates/product.elmsnest.json` l.446 — the comparison row
   "אפשר לשאול לפני ההזמנה" has `"text_a": "בוואטסאפ"`. Pre-existing content inside an `elms-pdp-*` section, which
   §B says to leave untouched, and not a label this round added — but it does claim a WhatsApp channel the shop does
   not have. Round 1 replaces this template; if it should go sooner it is a one-string edit.
7. **~~Footer links render underlined … not a round-0 regression.~~ WRONG, AND NOW FIXED [fix pass, R0-01].** It
   *was* a round-0 homepage regression, and this report asserted the opposite. The old base carried
   `body.hdt-page-type-index .shopify-section-group-footer-group a{text-decoration:none}` = (0,2,2), which beat
   Kalles' `.hdt-rte a:not(.hdt-btn){…underline}` = (0,2,1); §A.1's unscoped rewrite dropped it to (0,1,1) and lost.
   Pixel proof: seven 2-px bands on the desktop homepage (y16500-1, 16578-9, 16656-7, 16734-5, 16812-3, 16888-9,
   17100-1) and thirteen on mobile that were not in `before-home-*.png`. Fixed with
   `body .shopify-section-group-footer-group a:not(.hdt-btn)` = (0,2,2) (hover (0,3,2)). After the redeploy all
   seven desktop bands are **byte-identical** to the pre-round-0 baseline (max channel delta 0 in every one), and
   the whole-page diff is back to the header + footer-heading font bands §A.1 asks for.
   `brief/side-pages/core/cmp-home-footer-links.png` (before top, after bottom).


---

## 10. Fix pass — second verification round (2026-09-02 14:14–14:31 UTC)

Two verifiers (one code lens, one visual lens) raised ten findings against the report above: **2 must** and
**8 should**. Every one was reproduced first from the file or the PNG it cited, then fixed, then re-measured on a
fresh mirror + screenshot of the deployed theme. Nothing outside `snippets/elmsnest-v2-core.liquid` was touched, and
no template, section, setting or Kalles file was changed in this pass.

### 10.1 Deploy log

| # | file | live size | live checksumMd5 | updatedAt (UTC) | carries |
|---|---|---|---|---|---|
| 1 | `snippets/elmsnest-v2-core.liquid` | 21313 | `eb99dc2ed98cdedb8d8e837fc4a94f53` | 2026-09-02 14:14:16 | R0-01 · V-1 · V-2 · V-4 · V-6 |
| 2 | `snippets/elmsnest-v2-core.liquid` | 21614 | `87f570fb1f007d4a0fa5102090377ae9` | 2026-09-02 14:31:21 | V-2 widened to `(hover:none),(max-width:900px)` |

One file per `themeFilesUpsert`, GraphQL block string, `userErrors: []` both times. After each upsert the live
`checksumMd5` was compared with `head -c -1 theme/snippets/elmsnest-v2-core.liquid | md5sum` — equal both times, so
the deployed bytes are the repo bytes. `python3 brief/lint.py` → `LINT OK (0 issues)`.
`bash brief/inventory/mirror-all.sh && bash brief/inventory/shot-all-http.sh` was then re-run in full (35 mirrors,
70 screenshots), so every PNG and `index.html` under `brief/inventory/` matches the theme as deployed.

### 10.2 What changed in the core

`theme/snippets/elmsnest-v2-core.liquid`, two places:

- **l.40–47** the footer-group link rules, re-specified (R0-01).
- **l.70–110** a new commented block `fix pass, round 0 second pass`, after the existing tooltip rule and before
  the `.env2-section` helpers (V-1, V-4, V-6, V-2).

```css
body .shopify-section-group-footer-group a:not(.hdt-btn){text-decoration:none}                 /* R0-01 */
body .shopify-section-group-footer-group a:not(.hdt-btn):hover,
body .shopify-section-group-footer-group a:not(.hdt-btn):focus-visible{text-decoration:underline}
[color-scheme="scheme-1"]{ /* 24 tokens: cream scheme remapped onto the night pair */ }         /* V-1 */
#drawer-search-form select,#drawer-search-form option{
  background-color:rgb(var(--en-surface-elevated));color:rgb(var(--en-color-light))}            /* V-1 / old §9.5 */
#modal-contactFormAsk{background:rgb(var(--en-surface-elevated));color:rgb(var(--en-text-primary))} /* V-4 */
:root{--en-warning-text:255 211 148}                                                            /* V-6 */
.hdt-card-product__btn-ultra{--atc-cl:rgb(var(--en-text-inverse));--atc-bg-cl:rgb(var(--en-button-primary));
  --atc-cl-hover:rgb(var(--en-text-inverse));--atc-bg-cl-hover:rgb(var(--en-button-primary-hover))}  /* V-2 */
@media (hover:none),(max-width:900px){.hdt-card-product__btn-ultra{visibility:hidden}}          /* V-2 */
```

The `scheme-1` remap deliberately omits `--color-input-primary` / `--color-input-secondary`: the earlier
`:root,[color-scheme]{…}` rule owns that pair at the same specificity and has to keep winning, or F-1 would regress
inside the search drawer.

### 10.3 Finding by finding

| id | sev | reproduced (measurement before) | what changed | evidence it is closed |
|---|---|---|---|---|
| **R0-01** | must | PIL diff `before-home-desktop.png` vs `brief/inventory/home/http-desktop.png`: seven 2-px bands at y16500-1 / 16578-9 / 16656-7 / 16734-5 / 16812-3 / 16888-9 / 17100-1, thirteen more on mobile — underline rows under every footer link. Cause confirmed in the CSS: old base `body.hdt-page-type-index .shopify-…-footer-group a` = (0,2,2) beat Kalles' `.hdt-rte a:not(.hdt-btn)` = (0,2,1); §A.1's unscoped rewrite was (0,1,1). | core l.40–47: `body .shopify-section-group-footer-group a:not(.hdt-btn)` (0,2,2), hover/focus (0,3,2). | Re-diff after redeploy: **max channel delta 0 in all seven desktop bands**; whole-page bands now only `(32,107)` desktop = the header menu font and `(16382,16415)` desktop / `(16048,16081) (16452,16475) (17006,17033)` mobile = the footer *heading* font — the Heebo swap §A.1 requires. Desktop fold mean-abs-diff 0.2221, mobile fold **0.0000, pixel-identical**. Heights unchanged (17146 / 17396). `cmp-home-footer-links.png`. |
| **V-1** | must | `dialog-probe.js` on the coll-all mirror: `#drawer-search-form` `background-color: rgb(247,240,230)` = `#f7f0e6`, `color: rgb(88,79,69)`, category `<select>` `rgb(43,33,24)` = `#2b2118`, at 1440 and 390. Panel census `#f7f0e6` **84.17 %** mobile / **22.18 %** desktop. The attribute `color-scheme="scheme-1"` is written by the Kalles `header-inline-blocks` section (not in `theme/` and not in `brief/inventory/theme-src/`), so §E's `color_scheme_dialog` cannot reach it; grep confirms exactly one such element on each of the 15 pages, and no other element on any page carries `scheme-1`. | core: `[color-scheme="scheme-1"]{…}` remapped onto the night pair (24 tokens), plus the drawer's `<select>`/`<option>`. | Same probe after redeploy: panel `rgb(2,3,6)`, body text `rgb(201,196,184)` (**11.9:1**), `<select>` `rgb(244,238,227)` on `rgb(17,29,51)` (**14.6:1**). Panel census `#f7f0e6` **0.00 %**, `#fffdf7` 0.00 %, `#2b2118` 0.00 % at both viewports. `search-drawer-{desktop,mobile}.png` vs `search-drawer-mobile-before.png`. Homepage safety: `scheme-1` appears on exactly one element there too (the closed search panel) — the home diff above is the proof it moved no pixel. |
| **V-2** | should | The finding's own coordinates re-measured — and the cause is worse than reported. On a **faithful** 390 viewport (`fullPage:false`, mobile emulation live) the button is `visibility: visible`, `background-color: rgb(2,3,6)`, `color: rgb(2,3,6)` — a 1:1 opaque square over the photo on every card, 3037 px of `#020306` in one 90×45 device-px box. (The `#0d0d0f` the finding cites comes from the full-page PNG, where the square renders over a dark photo; see the harness caveat below.) | core: `--atc-*` set to the night pair on the button, and `visibility:hidden` under `(hover:none),(max-width:900px)`. | Faithful 390 viewport after: `visibility: hidden`; the same box is product photography (`#e2d1bd`…), `#020306` gone. Pointer case: `rgb(2,3,6)` on `rgb(255,211,148)` = **14.7:1** (was 1:1) — this also closes old §9 item 4. Full-page mobile PNG: the V-2 box is `#0f1a2f`/photo, and the desktop fold is unchanged (no button is painted statically on a pointer device). Page heights identical to the pre-fix run on every page — `visibility` does not reflow. `v2-card-btn-390-{before,after}.png`, `v2-collall-mobile-band-after.png`. |
| **V-3** | should | `stat` on `pdp-sticky-mobile.png` → mtime 2026-09-02 09:39:30, i.e. 3 h 46 m older than the 13:25:25 deploy it was offered as evidence for. Bottom-120-px census of that file: `#f7f0e6` 25176 px, `#2b2118` 14256 px — a cream bar with a brown button, under a table that says "cream found: no". | Both PNGs re-shot from the current `brief/inventory/pdp-single` mirror with `tools/sticky-shot.js` (the bar is `position:fixed; transform:translate3d(0,100%,0)` until Kalles' scroll JS reveals it, which cannot run offline, so the script reveals it by hand and clips to the bar's own rect). | New pair, measured: bar `rgb(2,3,6)`, text `rgb(244,238,227)`, submit "הוסיפו להזמנה" `rgb(26,18,6)` on `rgb(255,211,148)`. Census: `#f7f0e6` **0.000 %** both; `#2b2118` 0.001 % desktop / 0.000 % mobile; `#020306` 86.7 % / 55.4 %; `#ffd394` 5.0 % / 31.7 %. §6.4 restated. |
| **V-4** | should | `dialog-probe.js`: `<dialog id="modal-contactFormAsk">` computes `background-color: rgb(255,255,255)` at both viewports — the UA canvas, because no rule in the theme paints `.hdt-dialog-modal` — while its `hdt-modal` wrapper's `scheme-env2-night` paints the ink: heading "שאל שאלה" `rgb(244,238,227)` on white = **1.15:1**, labels `rgb(201,196,184)` = **1.74:1**. White = 24.62 % of the desktop shot, 56.18 % of mobile. Present on all 15 pages. | core: `#modal-contactFormAsk{background:rgb(var(--en-surface-elevated));color:rgb(var(--en-text-primary))}`. | After: dialog `rgb(17,29,51)`, heading `rgb(244,238,227)` = **14.6:1**, labels `rgb(201,196,184)` = **9.7:1**, submit `rgb(2,3,6)` on `rgb(255,211,148)`. `#ffffff` **0.00 %** in both shots. `ask-modal-{desktop,mobile}.png` vs `ask-modal-mobile-before.png`. The caveat stands: no template currently exposes an opener for this modal, so it is unreachable by a shopper today — but it is now correct when a round exposes it. |
| **V-5** | should | `wc -c brief/inventory/account-{login,register}/index.html` = **14** each, content `Not Acceptable`; `mirror-all.log` lines 14 and 19 read `mirrored 0/0 assets … (0 KB)`; `grep -c 'id="env2-base"'` = 0 on both. Root cause confirmed with curl: `/account/login?preview_theme_id=…` → **302** → `https://shopify.com/68949278894/account?locale=he…` (Shopify **new customer accounts**), and that endpoint answers **406** to the mirror. Same for `/account/register`. | No code change — this is a scope fact, not a defect. The four fake PNGs and the sheet next to each mirror were **deleted**, and `brief/inventory/account-{login,register}/FAILED-MIRROR.txt` now says what the directory is and why. §6.2 and §8 state it. | The two directories no longer contain anything that looks like a theme render. **Consequence for the round: the seven `templates/customers/*.json` edits (account, activate_account, addresses, login, order, register, reset_password) are inert** — the storefront never renders those templates. They are deployed and byte-correct (§1), they simply do nothing. The lead should decide whether to keep them as dead code or drop them from the round's accepted set. The §2 F-1 row has been corrected: F-1 was measured on `page-contact`, and there is no render for the account templates to measure. |
| **V-6** | should | `brief/inventory/search-none/http-desktop.png` y840-900 x1880-2450: glyph `#604000` on ground `#020306` = **2.19:1** (matches the report's own figure). Source: `.hdt-no-result-product{border:1px solid rgb(var(--color-warning-text));color:rgb(var(--color-warning-text))}` ← `--en-warning-text: 96 64 0`, a cream-page value §D did not list. | core: `:root{--en-warning-text:255 211 148}` — a swap onto the amber the design system already owns, not a new colour. Checked both other consumers: `.toast.warning{border-left:4px solid …}` and `.toast-icon.warning{background:…;color:rgb(var(--en-text-inverse))}` both stay legible. | Same band after: glyph `#ffd394` (883 px) on `#020306` (29893 px) = **14.73:1**. `v6-search-none-after.png`. §9 item 2 narrowed to the three unrendered semantic colours. |
| **R0-02** | should | `diff` of `brief/inventory/theme-src/templates/product.elmsnest.json` against the repo copy: exactly three changed lines. Walking the JSON: **l.17** = section `breadcrumb`, type `brc-nav-product` (the one §B allows); **l.276** = section `main-product`'s own `color_scheme`; **l.228** = the `main-product-sidebar` static block (`_product_sidebar`) inside `main-product`. Live checksum `817cf79e…` equals the repo file, so the edited version is what is deployed. §B says "leave the `elms-pdp-*` sections and `main-product` untouched", and §2's row claimed they were untouched. | **No revert** — the verifier is right that this needs the lead, not a blind rollback. §2's row and §8 have been corrected to say exactly what changed and why. | **And it is now a decision with evidence, not a guess.** `main-product.liquid` writes `section.settings.color_scheme` straight into `color-scheme="…"` on `<hdt-sticky-btn-atc>` (l.60) and on the sidebar, *ungated* by `colors_by_section`. Blanking that attribute back to `""` on the live pdp-single mirror and re-reading the computed styles: sticky bar `rgb(15,26,47)` instead of `rgb(2,3,6)`, text still `rgb(244,238,227)`, button still `rgb(255,211,148)` with `rgb(2,3,6)` ink — because `css-variables` writes the body scheme's tokens onto `:root`, and `color-scheme=""` matches no scheme rule and therefore inherits them. **So the carve-out is cosmetic (one step darker), not load-bearing: reverting it would not bring cream back.** Lead: sign it off or ask for the revert; either is safe, and the revert is two lines in one file. |
| **R0-03** | should | `drawer-desktop.png` read as an image: the panel says "העגלה שלך ריקה" with a single "חזור לחנות" CTA — the acceptance was taken on the **empty** drawer, so the line-item row, qty stepper, subtotal and `.hdt-btn-accent` checkout button the round changed were never rendered, while §2 and §6.3 asserted results about them. | No code change. A new mirror `brief/inventory/cart-drawer/` was made by seeding `cj.txt` from the `cart-full` cookie jar (3 items, 429.70 ₪) and mirroring `/collections/all` with it, so Shopify server-renders the drawer **with its lines**. `tools/drawer-shot.js` opens it and measures every control. | Populated drawer, both viewports: `<dialog id="CartDrawer" color-scheme="scheme-env2-night">`, `background rgb(2,3,6)`, **2 line items**. Title `rgb(244,238,227)`; item title `rgb(244,238,227)`; variant meta `rgb(201,196,184)`; price `rgb(244,238,227)`; qty stepper `rgb(244,238,227)`; remove `rgb(244,238,227)`; subtotal `rgb(244,238,227)`; **"צפה בעגלת הקניות"** `rgb(26,18,6)` on `rgb(255,211,148)`; **"תשלום"** (the `.hdt-btn-accent` checkout button, F-3) `rgb(2,3,6)` on `rgb(255,211,148)` = **14.7:1**. Cream census of the shots: `#f7f0e6` 0.000 %, `#fffdf7` 0.000 %, `#2b2118` 0.009 % / 0.001 %. `drawer-full-{desktop,mobile}.png`. **The discount field is absent** because `show_cart_discount:false`, so §C's `discount_error_message` is stored but never displayed — recorded in §6.3 and §8. |

Two nits from the verifiers were folded in rather than skipped: old §9 item 4 (card overlay labels) is closed by
V-2, and old §9 item 5 (search-drawer `<select>`) by V-1.

### 10.4 Homepage: still pixel-identical apart from the font swap §A.1 asks for

`before-home-*.png` (pre-round-0) vs `brief/inventory/home/http-*.png` after both redeploys:

| view | size | height Δ | mean abs diff | px differing >2 | differing bands |
|---|---|---|---|---|---|
| desktop fold | 2880×1800 | **0** | 0.2221 | 0.184 % | y32–107 only — the header menu in Heebo |
| desktop full | 2880×17146 | **0** | 0.0339 | 0.027 % | y32–107 (header) + y16382–16415 (footer headings) |
| mobile fold | 780×1688 | **0** | **0.0000** | **0 %** | none — pixel-identical |
| mobile full | 780×17396 | **0** | 0.0506 | 0.032 % | y16048–16081, y16452–16475, y17006–17033 (footer headings) |

The seven desktop and thirteen mobile underline bands the previous run carried are gone (max channel delta 0 in
every one). No band remains that is not a glyph rendered in a different face at the same position, which is the
`--f_family_1..3` → Heebo swap §A.1 mandates.

### 10.5 Acceptance re-run, all 15 required pages

`core loaded` and `fonts loaded` = 1 everywhere; `id="env2-ground-index"` = 1 on home and 0 on the other 14;
`Liquid error` = 0 everywhere; the `[color-scheme="scheme-1"]` night remap present on all 15; bottom edge `#020306`
at six x positions in both viewports on all 15; no horizontal overflow; JS errors unchanged (the two known ones,
plus the PDPs' offline `/products/<handle>.js`); `wa.me` = 0 and "בוואטסאפ" = 0 except the two PDPs (pre-existing
content, §9.6); Frank Ruhl Libre + Heebo requested on all 15. **Every page height is identical to the pre-fix-pass
run**, so nothing reflowed.

| page | header ground · glyph CR | cream `#f7f0e6`/`#fffdf7`/`#2b2118` desktop | mobile | height desk/mob |
|---|---|---|---|---|
| home | `#191b21` (hero photo) · 13.6:1 | 0.000 / 0.001 / 0.014 % | 0.000 / 0.000 / 0.007 % | 8573 / 8698 |
| coll-all | `#0f1a2e` · 13.6:1 | 0.003 / 0.013 / 0.001 % | 0.005 / 0.004 / 0.002 % | 2486 / 3438 |
| coll-wall | `#0f192e` · 13.7:1 | 0.003 / 0.017 / 0.001 % | 0.008 / 0.007 / 0.001 % | 1977 / 2479 |
| pdp-single | `#0f1a2f` · 13.8:1 | 0.001 / 0.000 / 0.002 % | 0.001 / 0.000 / 0.004 % | 9532 / 11915 |
| pdp-multi | `#0f1a2f` · 13.8:1 | 0.000 / 0.001 / 0.001 % | 0.000 / 0.001 / 0.001 % | 9599 / 11897 |
| cart-full | `#0f192e` · 13.7:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 1791 / 2567 |
| cart-empty | `#0f192e` · 13.7:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 1789 / 2322 |
| search-hits | `#0f1a2e` · 13.6:1 | 0.000 / 0.001 / 0.006 % | 0.000 / 0.001 / 0.010 % | 2559 / 3307 |
| search-none | `#0e192d` · 13.8:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 1029 / 1299 |
| p404 | `#0e192d` · 13.8:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 1110 / 1445 |
| page-guide | `#0f1a2e` · 13.6:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 3246 / 3578 |
| page-shipping | `#0f1a2e` · 13.6:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 2491 / 2819 |
| page-contact | `#0f192d` · 13.7:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 1293 / 2227 |
| policy-shipping | `#0f192e` · 13.7:1 | 0.000 / 0.000 / 0.000 % | 0.000 / 0.000 / 0.000 % | 2070 / 2728 |
| coll-list | `#0f192e` · 13.7:1 | 0.000 / 0.002 / 0.034 % | 0.000 / 0.000 / 0.021 % | 1591 / 1517 |

Plus, new in this pass, the two chrome surfaces the page census cannot see, opened and measured on every viewport:

| surface | ground | worst text pair | cream in the shot |
|---|---|---|---|
| header search drawer (all 15 pages) | `#020306` | `#c9c4b8` on `#020306` — 11.9:1 | 0.00 / 0.00 / 0.00 % |
| "שאל שאלה" modal (all 15 pages) | `#111d33` | `#c9c4b8` on `#111d33` — 9.7:1 | `#ffffff` 0.00 % |
| cart drawer, 2 lines | `#020306` | checkout `#020306` on `#ffd394` — 14.7:1 | 0.000 / 0.000 / 0.009 % |
| PDP sticky bar | `#020306` | submit `#1a1206` on `#ffd394` — 13.2:1 | 0.000 / — / 0.001 % |

`headers-{desktop,mobile}-sheet.png` were rebuilt from the current folds: the six menu items
"דף הבית · קולקציות · מדריך לבחירה · שאלות נפוצות · מי אנחנו · יצירת קשר" are readable on all 14 side pages.

### 10.6 One harness caveat the next round must know

**Playwright's `fullPage: true` capture drops Chromium's mobile emulation in this build.** Measured directly: in a
`{isMobile:true, hasTouch:true, width:390}` context `matchMedia('(hover:none)')`, `(pointer:coarse)`,
`(any-pointer:coarse)` and `(any-hover:none)` are all `true` before the screenshot and all `false` after it, and a
test element styled only by `@media (hover:none)` renders in its *desktop* colour inside the full-page PNG. Width
queries are unaffected.

Consequences: (a) every `http-mobile.png` / `http-mobile-fold.png` in `brief/inventory/` is faithful for
width-based CSS and unfaithful for any `hover`/`pointer` media query — `http-*-fold.png` (`fullPage:false`) is
faithful for both; (b) this is why V-2's own evidence read `#0d0d0f` (the desktop branch over a photo) rather than
the real `#020306`; (c) the V-2 rule was therefore written as `(hover:none),(max-width:900px)` so the shipped
mobile PNGs and a real phone agree. Any future check of a touch-conditional style must be taken from a
`fullPage:false` viewport shot, not from the full-page PNG.

### 10.7 What is still open after this pass

Unchanged from §9 unless marked: item 1 (`<a class="env2-btn">` ink — pre-existing, fixing it moves the homepage),
item 2 **narrowed** to `--en-success-text` / `--en-error-text` / `--en-info-text` (none rendered anywhere; three new
semantic colours is a design call), item 3 (badge pairs, all hidden until round 2), item 6 ("בוואטסאפ" string on the
PDP template). Items 4, 5 and 7 are **closed**. Two new items for the lead, both from this pass:

1. **Sign off or revert the §B carve-out** in `templates/product.elmsnest.json` (R0-02). Evidence for the decision
   is in §10.3; both states render night.
2. **Decide what the 7 `templates/customers/*.json` edits are for** (V-5). The store is on new customer accounts,
   so they are inert dead code. Keeping them costs nothing; counting them as delivered work is misleading.
