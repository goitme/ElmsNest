# Round 0 — shared core: engineering spec (2026-09-02)

Goal: every template of the dev theme (`gid://shopify/OnlineStoreTheme/154726400174`, unpublished) renders on the
design system's ground with a legible header, the shared tokens/fonts/lamps available, a night cart drawer and no
cream bands — while the homepage looks exactly as it does now. This round is engineering, not design: the old Kalles
sections stay in place (they are replaced page by page in rounds 1–6); they only stop being cream.
Read first: `HANDOFF.md` §3–§4, `brief/build-preview/CONTRACT.md`, `brief/inventory/INVENTORY.md` §2,
`brief/side-pages/OWNER-NOTES.md`, `brief/DEPLOY.md`. Source files: `theme/` (repo mirror) and
`brief/inventory/theme-src/` (verbatim dumps of the theme's own files — read, never deploy from there blindly).

## A. Split the base into a global core and an index-only ground

1. **`snippets/elmsnest-v2-core.liquid`** (new) = everything in `snippets/elmsnest-v2-base.liquid` EXCEPT the
   index-only block (`:root:has(body.template-index)… body.hdt-page-type-index{background…}`, the wrapper-transparency
   rules scoped to index, the first-child margin rule, the index-scoped back-to-top and footer rules). Line 1 stays the
   `env2-js` inline script. Add, page-agnostic:
   - `html{background:#020306}` and `body[class*="hdt-page-type-"]{background-color:#020306;color:#f4eee3}` — the
     side-page ground: `background-image:linear-gradient(180deg,#0f1a2f 0%,#070b15 45%,#020306 100%)`,
     `background-repeat:no-repeat;background-size:100% 100%;min-height:100vh` — **but not on `hdt-page-type-index`**
     (the index keeps its own dusk gradient from the ground snippet; write the selector as
     `body[class*="hdt-page-type-"]:not(.hdt-page-type-index)`).
   - Kalles wrappers transparent on every page type: `#wrapper, main, #MainContent, .hdt-main-content,
     .hdt-page-content, .shopify-section {background:transparent}` (verify the footer group still paints its own
     scheme through its inner `.hdt-section-spacing[color-scheme]` — it does on the index today).
   - Back-to-top hidden on every page: `.hdt-back-to-top, back-to-top{display:none!important}`.
   - Footer group font + link rules, unscoped (today they are index-scoped).
   - Kalles chrome type: after Kalles' `css-variables` (the core is rendered after it), override
     `:root{--f_family_1:var(--env2-sans);--f_family_2:var(--env2-sans);--f_family_3:var(--env2-sans)}` so header
     menu, drawer, quick-add popup, facets and the old sections use Heebo (`--env2-sans` is defined by the fonts
     snippet, so the fonts snippet must be rendered BEFORE the core). Check `snippets/css-variables.liquid` l.218–231
     for the exact variable names (`--f_family_1..3`; the theme uses Shopify fonts `assistant_n4`).
   - Sort entries that imply sales data are hidden in the UI (interim until the collection is rebuilt):
     `option[value="best-selling"]{display:none}` plus the popover item — find its markup in
     `brief/inventory/theme-src/sections/main-collection.liquid` / `snippets/sort-by-popover` equivalents and hide it.
   - Sale badges never render: settings change in E; additionally `.hdt-badge__wrapp{display:none}` as a belt.
2. **`snippets/elmsnest-v2-ground-index.liquid`** (new) = the removed index-only block (the dusk gradient, index
   wrapper transparency, first-child margin). Rendered by `sections/elmsnest-v2-hero.liquid` line 7 **instead of**
   `elmsnest-v2-base` (the hero must no longer render fonts or base; both are global now).
3. **`snippets/elmsnest-v2-base.liquid`** stays in the theme as a one-line deprecation comment (so nothing that still
   renders it can error); nothing renders it after this round.
4. **`layout/theme.liquid`**: fetch the live file first (DEPLOY rules), then a minimal edit inside `<head>`, after the
   `render 'css-variables'` line and before `render 'scripts'`:
   `render 'elmsnest-v2-fonts'` then `render 'elmsnest-v2-core'`. Keep the index and product preloads as they are.
5. **`snippets/elmsnest-v2-photo-url.liquid`** (new): the single place that builds the "send a photo of the place" URL.
   Inputs: none. Output (captured by the caller with `{% capture %}` or rendered as text):
   - if `settings.whatsapp_number` is non-blank → `https://wa.me/<digits>?text=<url_encode of 'שלום, אשמח לבדוק התאמה — מצרף/ת תמונה של המקום.'>`
   - else → `mailto:info@elmsnest.com?subject=<url_encode 'בדיקת התאמה — תמונה של המקום'>&body=<url_encode 'שלום, מצרף/ת תמונה של המקום שרוצים להאיר. המוצר ששוקלים: '>`
   Then update the four homepage sections that build this URL themselves (`elmsnest-v2-hero` l.70–72, `-switch`
   l.13–15, `-terms` l.13–18, `-goodnight` l.18–25) to use the snippet, and make sure no label says "בוואטסאפ" while
   the number is empty (the sections already guard their labels — verify each label's fallback reads "לשליחת תמונה"
   / "לשלוח תמונה של המקום"). Owner decision: there is no WhatsApp number yet; the email path is the fallback.

## B. Templates: no cream first sections, no cream main sections (interim schemes)

Fetch each live template JSON first, edit minimally, keep every section id. For each of `templates/collection.json`,
`search.json`, `cart.json`, `list-collections.json`, `page.json`, `page.contact-us.json`, `templates/customers/*.json`:
- remove the `top-list-collections` section (collection.json, search.json) from `sections` and `order`;
- `main-heading` sections: set `color_scheme` to `scheme-env2-night`, remove `image` (set to `""`), `bg_overlay: 0`;
- main sections (`main-collection`, `main-search`, `main-cart`, `main-list-collections`, `main-page`, `contact-form`,
  `main-login`, `main-register`, `main-account`, `main-addresses`, `main-order`, `main-reset-password`,
  `main-activate-account`) and any `colors_by_section`-driven section: set `color_scheme` to `scheme-env2-night`
  where the key exists in that section's schema (check `brief/inventory/theme-src/sections/<file>.liquid` schema);
- `templates/404.json` `main-404`: `color_scheme: scheme-env2-night`;
- `templates/product.elmsnest.json` (the live PDP template — all 27 products use it): `brc-nav-product`
  `color_scheme: scheme-env2-night`; leave the `elms-pdp-*` sections and `main-product` untouched (they take their
  colours from the `--en-*` tokens, see D) — this template is replaced in round 1.
- `templates/blog.json`: remove the `blog-slider` section (demo content on a public URL).
Do not touch `templates/index.json` beyond what A.2 needs (nothing).

## C. System group

`sections/system-group.json` (fetch, edit minimally): `cart-drawer` → `color_scheme: "scheme-env2-night"`,
`discount_error_message: "יש להזין קוד הנחה תקין"`; leave `back_top` in place (hidden by CSS in A.1).

## D. Retarget the old `--en-*` tokens (interim, one edit)

`snippets/css-variables.liquid` l.72–137 (fetch live, edit only these values):
`--en-color-dark: 2 3 6` · `--en-color-light: 244 238 227` · `--en-surface-page: 15 26 47` · `--en-surface-elevated: 17 29 51` ·
`--en-surface-card: 17 29 51` · `--en-surface-inverse: 244 238 227` · `--en-text-primary: 244 238 227` ·
`--en-text-secondary: 201 196 184` · `--en-text-muted: 143 149 163` · `--en-text-inverse: 2 3 6` ·
`--en-border-subtle: 58 63 75` · `--en-border-default: 110 116 130` · `--en-border-strong: 143 149 163` ·
`--en-button-primary: 255 211 148` · `--en-button-primary-hover: 233 185 110` · `--en-button-primary-active: 214 165 92` ·
`--en-button-disabled-bg: 40 48 66` · `--en-button-disabled-text: 143 149 163` · `--en-button-disabled-border: 58 63 75` ·
`--en-focus-light: 255 211 148` · `--en-focus-dark: 255 211 148` · `--en-focus-contrast: 2 3 6` ·
`--en-night: 7 11 21` · `--en-ink: 244 238 227` · `--en-amber: 233 185 110` · `--en-amber-soft: 255 211 148`.
Then check every place that uses `--en-button-primary` for its text colour: buttons with glow fill need dark text
(`--en-text-inverse`); if a rule pairs `--en-button-primary` with `--en-color-light` text, override that rule in the
core (`.elms-pdp-section .btn…{color:#1a1206}`) — verify on the PDP render, do not guess.

## E. `config/settings_data.json` (fetch live; minimal, surgical edits; never rewrite; backslashes pass literally)

`color_scheme_body: "scheme-env2-night"`, `color_scheme_dialog: "scheme-env2-night"`, `hidden_badges: true`,
`show_quick_add: false` (the quick-add popup is the cream Kalles modal; cards link to the PDP until the card is
rebuilt), `animations_reveal_on_scroll: false` (Kalles slide-in reveals fight the lamp idea and hid every grid in
`file://` renders), `badge_sale` unchanged (badges are hidden). Do not touch fonts (A.1 overrides them in CSS).

## F. Lint + verification (must pass before the report)

1. `brief/lint.py`: extend the globs to `sections/elmsnest-v2-*.liquid`, `snippets/elmsnest-v2-*.liquid` and every
   `templates/*.json` + `templates/customers/*.json` we deploy (schema ↔ settings check per section type using the
   dumped schemas in `brief/inventory/theme-src/sections/`), plus a new check: no section in `theme/` contains `"""`.
2. Deploy order: snippets (fonts, core, ground-index, photo-url, base stub) → sections (hero + the three photo-URL
   sections) → templates → `sections/system-group.json` → `snippets/css-variables.liquid` → `config/settings_data.json`
   → `layout/theme.liquid`. One file per `themeFilesUpsert` call, GraphQL block string; stop on any `userErrors`.
3. Mirror + shoot (JS-enabled) with `bash brief/inventory/mirror-all.sh && bash brief/inventory/shot-all-http.sh`
   (or per page: `python3 brief/mirror.py <url> <dir>` then `node brief/shot-http.js <dir>/index.html <dir>/http`).
   Required pages: home, coll-all, coll-wall, pdp-single, pdp-multi, cart-full, cart-empty, search-hits, search-none,
   p404, page-guide, page-shipping, page-contact, policy-shipping, coll-list.
4. Acceptance, checked on the PNGs and the HTML:
   - home: `http-desktop-fold.png` / `http-mobile-fold.png` visually identical to `brief/inventory/home/` before the
     change (same heights ±20 px, same first screen); `grep -c 'env2-base' index.html` shows the core is loaded once,
     `Liquid error` count 0.
   - every other page: header menu text visible on the first screen (sample the pixel colour behind the menu: it must
     be sky-2 or darker; the menu items "דף הבית · קולקציות · …" readable in the desktop fold); no cream (`#f7f0e6`,
     `#fffdf7`) or brown (`#2b2118`) surface anywhere (sample 12 points per page with PIL; report the sampled colours);
     `env2-base loaded` true on every page (grep `id="env2-base"` or the core's id); FRL + Heebo requested on every
     page; page ends in `#020306` before the footer (no hard cut).
   - cart drawer: serve `brief/inventory/coll-all` over `python3 -m http.server`, click the first `/cart/add` form's
     submit with Playwright, wait for `hdt-cart-drawer[open]` (or the drawer's visible state), screenshot at 1440 and
     390: the drawer must be night (`#020306`/`#070b15` ground, ink text), not cream. Note: the mirror's `/cart/add.js`
     request will fail offline — stub it with `page.route` returning a minimal JSON `{}` and dispatch the
     `cart:update` event if needed; what is being judged is the drawer's colours, not the network.
   - PDP: the `elms-pdp-*` sections render night/ink (interim), buttons readable (dark text on glow).
   - no new JS errors beyond the two known (`Failed to fetch dynamically imported module`, `innerHTML of null`).
5. Report: `brief/side-pages/core/REPORT.md` — what changed (file → lines), the deploy log (filename → size), the
   acceptance table (page → header legible / cream found / core loaded / height), the drawer screenshots' paths,
   and anything left interim with the round that will replace it.

## Do-not list
- Do not change the look of the homepage. Do not rewrite `settings_data.json` or `theme.liquid`. Do not deploy from
  `brief/inventory/theme-src/` copies of Kalles files. Do not add a WhatsApp label anywhere. Do not remove the old
  `elms-pdp-*` sections yet (round 1). Do not touch the MAIN theme (the tool blocks it anyway). Do not publish.
