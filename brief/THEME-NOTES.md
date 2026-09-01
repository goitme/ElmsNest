# Theme mechanics for the build (read after WINNING-SPEC.md)

Target theme: **ElmsNest - Homepage Rebuild 2026-09-01**, id `gid://shopify/OnlineStoreTheme/154726400174`, UNPUBLISHED (safe). Kalles v5.4.2.
Preview: https://elmsnest.com/?preview_theme_id=154726400174

## Header (do not rebuild — configure)
`sections/header-group.json` → one section `header-inline-blocks`:
- `header_transparent: true` on the index page, using `logo_transparent` = ElmsNest_Logo_Night.png (gold mark) and the dark colour scheme. So the hero can and should run BEHIND the header; the first ~70px (60px mobile) of the hero is under a transparent bar.
- `header_height: 70`, `header_height_mb: 60`, `sticky_type: on_scroll_up`, `sticky_glass: true`.
- Menu: `main-menu` linklist. Cart icon on, search icon on.
- If the concept needs a different header colour/opacity, change settings in header-group.json — do not write a new header section.

## Footer (configure, not rebuild)
`sections/footer-group.json` → Kalles `footer` with five `_footer-column` blocks (logo, קישורים מהירים, מידע ושירות, מדריכים ומידע, newsletter) on `scheme-1` (cream). For a dark page switch `colors_by_section: true` + `color_scheme` to the dark scheme id `scheme-77e4ef58-56a9-4631-876a-12098ba7d57d` (text #f7f0e6 on #2b2118) on both footer sections. If the winning palette is a true black rather than #2b2118, add a new colour scheme in `config/settings_data.json` `color_schemes` and reference it.

## Colour schemes available (settings_data.json)
- `scheme-1`: text #2b2118 on #f7f0e6 (cream)
- `scheme-77e4ef58-56a9-4631-876a-12098ba7d57d`: text #f7f0e6 on #2b2118 (night)
- `scheme-6707cc8e-6558-49d9-8759-f7d934d9fe4f`: text #2b2118 on #d9ad5f (gold)

## Section file conventions (Kalles / OS 2.0)
- `sections/<name>.liquid` = markup + `{% stylesheet %}…{% endstylesheet %}` + optional `{% javascript %}…{% endjavascript %}` + `{% schema %}{…}{% endschema %}`.
- `{% stylesheet %}` CSS is bundled by Shopify into one file per page (no per-instance scoping) — namespace all selectors (e.g. `.env2-hero__…`).
- `{% javascript %}` is also bundled and runs once per page; use `document.querySelectorAll('[data-env2-hero]')` and init each instance. Or inline `<script>` inside the section if you need `section.id`. Both are fine.
- Section settings: `section.settings.x`; blocks: `section.blocks` with `block.settings.x` and `{{ block.shopify_attributes }}` on the block's root element (theme editor needs it).
- Images: `{{ image | image_url: width: 1600 | image_tag: loading: 'lazy', widths: '…', sizes: '…', alt: '…' }}`. Products: `product.featured_image`, `product.images[1]` (0-based) for alternates, `product.url`, `product.selected_or_first_available_variant.price | money`, `product.variants.size`.
- Money filter renders `89.90 ₪` — wrap in `<bdi>` inside RTL text.
- Collection settings: `{ "type": "collection", "id": "collection" }` → `section.settings.collection` is a collection object (or blank).
- Product settings: `{ "type": "product", "id": "product" }` → product object; `product_list` gives a list.
- Fonts: emit `<link rel="preconnect" href="https://fonts.googleapis.com">` + `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=…&display=swap">` from ONE snippet `snippets/elmsnest-v2-fonts.liquid` and `{% render 'elmsnest-v2-fonts' %}` at the top of the first section only (hero). Do not load fonts in every section.
- Hero images: assets `elmsnest-hero-desktop-performance.webp` / `elmsnest-hero-mobile-performance.webp` are preloaded by layout/theme.liquid for the index template. If the hero uses different images, either use `image_picker` settings and accept the extra preload, or edit the preload in layout/theme.liquid to match.
- The `elmsnest-whatsapp` snippet renders a floating WhatsApp button bottom-left on every page — design around it (don't put a fixed control in the bottom-left corner).
- Add-to-cart without JS: `<form method="post" action="{{ routes.cart_add_url }}"><input type="hidden" name="id" value="{{ variant.id }}"><input type="hidden" name="quantity" value="1"><button type="submit">…</button></form>`.
- Approved non-negotiable copy is in BRIEF.md §3.

## Deploying (done by the lead, not by build agents)
Files are written to the repo under `/home/user/ElmsNest/theme/` mirroring theme paths, then upserted with `themeFilesUpsert` — sections first, then `templates/index.json`, then the group JSONs. The lead screenshots the live preview via a curl-mirror (`brief/shot.js` works on a local mirror) and iterates.

## Offline test harness for build agents
You cannot load the Shopify preview in Chromium from this sandbox, but you CAN render a static HTML approximation: keep a `brief/build-preview/index.html` that stitches the sections' rendered markup with local assets (`brief/assets/…`) and run `node brief/shot.js` on it. Treat Liquid output as what you'd get from the template — hand-substitute the settings you put in index.json.
