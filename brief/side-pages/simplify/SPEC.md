# ElmsNest — SIMPLIFY spec (round 3, 2026-09-05)

Supersedes the env2 page compositions in `brief/side-pages/pdp/WINNING-SPEC.md` and
`brief/side-pages/collection/WINNING-SPEC.md` for STRUCTURE. The env2 design system
(`brief/WINNING-SPEC.md` §3: sky tokens, Frank Ruhl Libre + Heebo, gold, hairlines, radius 0)
stays as the visual language. The honesty rules of `brief/BRIEF.md` §3 stay verbatim.

## 0. Why this round exists — the owner's verdict of 2026-09-05 (verbatim, Arabic)

1. «صممتها تصميم بصري جميل جداً لكنه معقد ومش زابط للمتجر — العميل لما بدو يشتري بيتعقد لأنه
   أول مرة بشوف هيك اشي. هدفي أفضل تصميم بصري لكن بسيط للعميل.»
2. «في كل الصفحات كثير شغلات مكررة مرتين — سكشن معاد مرتين بنفس الطريقة وبطريقة ثانية.»
3. «خربت صور المنتجات — منتجات بالكولكشن غيّرتها وحطيت صور ثانية.»
4. «ضل مبدع، ما تحط قيود لنفسك، بس خذ بعين الاعتبار اللي قلته.»

Measured behind it (mobile 390×844, `brief/side-pages/simplify/audits.txt`): home 10.3 screens,
collection /all 25.8 screens with the 27 products listed ≈74 times, PDP 10.2 screens with three
add-to-cart forms plus a gold link that looks like a fourth; the four consumer terms twice per page;
«שלחו תמונה של המקום» 3–5× per page; 16 of 27 collection cards drawn as SVG plates captioned
«איור · אין תצלום נקי», 5 more showing a non-featured frame; the whole theme on `rgb(2,3,6)`.

## 1. The owner's five answers (2026-09-05, verbatim, binding)

| # | Question | Answer | Consequence |
|---|---|---|---|
| 1 | Visual direction | «النظرة الليلية الداكنة بس مبسّطة» | Keep the night look and the env2 tokens. Rebuild the STRUCTURE with standard shopping patterns. The dev homepage on 154726400174 is rebuilt in this language too (the live v3 paper homepage on 154652737710 stays untouched — publishing is a separate owner decision). |
| 2 | Images | «موافق» | `product.featured_image` first, everywhere, now — posters included. No glyph plates, no index resolver, no `image_index` overrides. Reordering the 5 products with a clean frame and generating clean renders for the 14 without one is a SEPARATE content task that waits for the owner's approval of a sheet. |
| 3 | «שלחו תמונה של המקום» | «فش رقم واتس، خلي البريد» | Keep the promise, on email, ONCE per page in the body + the footer line. Built by `snippets/elmsnest-v2-photo-url.liquid` (mailto). Never the word «וואטסאפ». Known risk, owner-accepted: elmsnest.com has no MX record (re-measured 2026-09-05), so mail to info@ does not arrive until the owner fixes DNS — Notion goal #1. |
| 4 | Collection naming | «هيك» | Label = the Shopify collection title; the place word (שביל / קיר / גינה / מרפסת) is a one-word subtitle. The four collections are the primary entry; `/collections/all` is a standard grid with a collection filter row. ONE order everywhere = the main-menu order: תאורת שביל, עמוד וגינה → תאורת קיר → ספוטים, פרוז׳קטורים ותאורה ניידת → גרילנדות ותאורה דקורטיבית. |
| 5 | Cookie banner | «بنقدر نصغّره» | It is Shopify's own Customer-privacy banner (the theme's `cookies` section is disabled, no app embed). Not reachable from theme code or the Admin API → owner action, §9. |

## 2. Principles (acceptance criteria, testable)

P1 **Every ACTION uses the pattern a Shopify shopper already knows.** Browse = one grid of identical
cards. Choose = variant pills/dropdown inside the buy box. Quantity = a stepper. Buy = ONE
add-to-cart form per PDP (+ the sticky bar that submits the same form). After add = the Kalles
cart drawer. Sort = a native select. Filter = a row of collection links.
Creativity lives only in the non-action layer: the hero photograph, the collection header photograph,
typography, the IP-numeral on the PDP, restrained motion in the hero.

P2 **Each buyer question is answered exactly once per page.** The question map is §3. No section
may answer a question another section on the same page already answers. The four consumer terms
appear once per page (one compact strip). The photo/email CTA appears once in the body (+ footer).
The four places appear once (+ header menu + footer, which we do not control).

P3 **Images: the store's own images, in the store's own order.** Cards and the first gallery slide
use `product.featured_image`; galleries show `product.media` in Shopify order. No resolver, no
banned indexes, no glyphs, no `[data-lamp]` dimming on any product image, no opacity-until-lit.
`loading="lazy"` is fine below the fold only.

P4 **Copy is Hebrew, verbatim, and makes no claim.** Place pairs only from BRIEF §3. Terms only the
licensed wording (§5). No reviews, no counts, no urgency, no "best", no baked-in text of ours.
CTA vocabulary, site-wide, exactly: «הוספה לסל» (PDP form) · «לכל המוצרים» · «למדריך המלא» ·
«לשלוח תמונה של המקום». Cards carry NO button text — the whole card is the link.

P5 **Length.** Mobile 390×844: home ≤ 6 screens, collection ≤ 8 screens for 27 products,
PDP ≤ 6 screens (footer included). Desktop 1366×900 proportionally shorter.

P6 **No-JS and a11y.** Every buy path is a native `<form action="/cart/add">`. Sorting works with
`?sort_by=`. 44 px tap targets. Contrast ≥ 4.5:1 for text. `prefers-reduced-motion` respected.
`<bdi>` around every Latin/number token inside Hebrew lines (IP65, LED, 10W, ranges, prices).

P7 **Nothing is deleted from the theme in this round.** The old env2 sections stay as files but leave
the templates. Deleting files is a later cleanup after the owner's verdict (rollback stays trivial).

## 3. Question map (the acceptance test for P2)

| Question | Home | Collection | PDP |
|---|---|---|---|
| Where am I / what is this store? | hero | header | breadcrumb + kicker line |
| Which four places / collections? | collections tiles | filter row | — (kicker names one) |
| Which products, what price? | featured grid (4) | THE grid (all) | related (4) |
| Does it suit my place / when not? | fit block (4 lines) | one deck line in header | not-for line under the buy box |
| How do I choose length / colour / quantity? | — | — | variant picker + quantity stepper |
| How do I buy? | card → PDP | card → PDP | the ONE add-to-cart (+ sticky bar) |
| What does it cost per metre / per unit? | — | — | one caption line under the price |
| Specs / what is it made of / IP? | — | — | facts section (numeral + table) |
| Terms (shipping, delivery, cancellation)? | terms strip | terms strip | one-line strip under the button → links to /pages |
| Not sure? | email CTA in fit block | email CTA in guide strip | email CTA in not-for line |
| Where next? | footer | footer | related + footer |

## 4. Design tokens (unchanged, from `snippets/elmsnest-v2-core.liquid`)

- Ground: `html{background:#020306}`; index page gets the dusk→night gradient from
  `elmsnest-v2-ground-index` (rendered by the hero); collection and product pages get their ground
  from `elmsnest-v2-ground-collection` / `elmsnest-v2-ground-product` (rendered by the first section).
- Ink `#f4eee3`, muted `#c9c4b8`, gold `#e9b96e`, glow `#ffd394`, hairline `#1f1e1d`, card ground
  `#05070c`. Radius 0 everywhere except pill buttons (999px).
- Type: Frank Ruhl Libre 700/900 for display and product titles; Heebo for everything else.
  Mobile display 30–34 px, section headings 24–26 px, body 16 px, captions 13 px (never below 12.5).
- Motion: lamps (`[data-lamp]`) ONLY inside the hero. Nothing else animates on scroll.

## 5. Shared pieces (new files, all small)

### 5.1 `snippets/elmsnest-s-skin.liquid`
One `<style>` block, rendered from `layout/theme.liquid` right after `elmsnest-v2-core`, that dresses
the STOCK Kalles components in the night language so we can use them unmodified:
- `.hdt-card-product`: ground `#05070c`, hairline border, radius 0, title Frank Ruhl Libre 17/1.3
  clamped to 2 lines (`-webkit-line-clamp:2`), price Heebo 16 gold; hide everything else the card can
  render — swatches, size lists, quick-view, wishlist, compare, badges, vendor, "sale" labels,
  compare-at prices (`.hdt-price__compare, s, del{display:none}`), rating stars.
- `.hdt-price`: gold; the "מ־" prefix for `price_varies` in muted ink.
- `main-collection` toolbar: only the sort select visible; hide the filter button, the column
  switcher, the list/grid toggle and the "showing N of M" line; sort select styled as a hairline pill.
- `main-product`: title Frank Ruhl Libre 28/32 mobile, 38 desktop; price 26 gold; variant pills
  hairline / selected = gold fill + ink `#1a1206`; quantity stepper hairline; `.hdt-btn` add-to-cart =
  gold pill, full width, 52 px; sticky bar ground `#05070c` hairline top.
- `cart-drawer`: ground `#05070c`, hairlines, gold checkout button, Frank Ruhl Libre line titles.
- Related products: same card rules.
Max ~250 lines. No `!important` unless a Kalles rule forces it (comment each one).

### 5.2 `snippets/elmsnest-s-place.liquid`
Input: `collection` (a collection object) or `product`. Output via `emit`:
`emit:'word'` → the place word; `emit:'yes'` → the "suits" phrase; `emit:'no'` → the "does not suit"
phrase. Mapping by collection handle (BRIEF §3, verbatim):
- `תאורת-שביל-סולארית` → שביל · לראות את הדרך · המקום כמעט אינו מקבל אור יום
- `solar-wall-lights` → קיר · להאיר נקודה מסוימת · נדרש אור חזק וקבוע לאורך כל הלילה
- `ספוטים-ופרוז-קטורים-סולאריים` → גינה · הארה ממוקדת של עץ או ערוגה · נדרשת התקנה מיוחדת או חיבור קבוע
- `גרילנדות-ותאורה-דקורטיבית` → מרפסת · ליצור אווירה · צריך אור חזק — זו אינה מטרתה
For a product: the first of `product.collections` that matches (in the menu order above). No match →
prints nothing (callers must tolerate blank).

### 5.3 `snippets/elmsnest-s-terms.liquid`
The four consumer terms as ONE compact strip: four rows on hairlines, numeral (Frank Ruhl Libre 26,
gold) + one short line each, then a foot line with the four policy links. ≤ 0.5 screen on mobile.
Licensed wording, verbatim from `sections/elmsnest-v2-terms.liquid` schema defaults:
- **0 ₪** — משלוח חינם לנקודת איסוף · משלוח עד הבית 29.90 ₪
- **8–17 ימי עסקים** — 1–3 ימי טיפול + 7–14 ימי משלוח; ייתכן משלוח ממחסנים מחוץ לישראל
- **14 יום** — ביטול עסקה לפי חוק הגנת הצרכן, עד 14 יום מקבלת המוצר; דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם
- **1 תמונה** — שולחים תמונה של המקום במייל ואנחנו בודקים התאמה לפני שמזמינים
Links: /policies/shipping-policy · /pages/processing-time · /policies/refund-policy · /pages/help-faq.
Wrapped by `sections/elmsnest-s-terms.liquid` (schema: heading text, default «ארבעה מספרים שכדאי לדעת»)
for home and collection. The PDP uses the one-line variant (§8).

### 5.4 `snippets/elmsnest-s-contact.liquid`
ONE line: «לא בטוחים? שלחו תמונה של המקום ואנחנו נבדוק התאמה לפני שמזמינים.» + a hairline-underlined
link «לשלוח תמונה של המקום ←» whose href is `{% render 'elmsnest-v2-photo-url', subject:…, body:… %}`
(mailto). Accepts `product` to prefill the subject with the product title. Never mentions WhatsApp.

### 5.5 `snippets/elmsnest-s-card.liquid` — NOT built. Cards are Kalles `card-product1` skinned by 5.1.
(One card implementation site-wide: grid, related, search, and the drawer's upsells all match.)

## 6. HOME — `templates/index.json` (target ≤ 6 screens mobile)

1. `elmsnest-v2-hero` (existing) — edit the section minimally: add settings `show_card`
   (default false) and `show_secondary_cta` (default false). With both off it renders: the dusk
   photograph, eyebrow, the two-line headline, the lead, ONE gold pill «לכל המוצרים» →
   `/collections/all`, and the lamp motion. Keep `show_sun_rail`. Nothing else changes.
   Settings: keep the current copy; `cta_primary_label: "לכל המוצרים"`, `cta_primary_link: "/collections/all"`.
2. `elmsnest-s-collections` (new) — heading «לפי המקום» (Frank Ruhl Libre 26). A 2×2 grid
   (mobile) / 4-across (desktop) of collection tiles: `collection.image` (object-fit cover, 4/5,
   NO dimming), the place word small in gold above the Shopify title (Frank Ruhl Libre 20), the count
   «N מוצרים» muted. Whole tile is the link. Blocks: 4 × `collection` in the menu order. ~1.2 screens.
3. `elmsnest-s-products` (new) — heading «מה שנדלק ראשון» (keep, it is the store's line). A 2-col
   grid of exactly 4 `card-product1` cards from a `product_list` setting, default: the four of
   first-lit (outdoor-bidirectional-led-wall-light-ip65, powerful-solar-garden-light,
   solar-edison-string-lights, solar-firefly-garden-lights). No buttons. ~1.4 screens.
4. `elmsnest-s-fit` (new) — heading «אנחנו נגיד לכם גם מתי לא.» Four rows on hairlines, one per
   place in the menu order: place word (gold) · «מתאים כדי {yes}» · «לא מתאים כש־{no}» (from 5.2).
   Foot: «למדריך המלא ←» → /pages/guide-garden-lighting, and the contact line (5.4). ~1 screen.
5. `elmsnest-s-terms` (5.3). ~0.5 screen.
Then the Kalles footer. Removed from the template: first-lit, places, switch, night-wall, atmosphere,
goodnight, the hero card, the hero photo button. Expected total ≈ 5–5.5 screens.

## 7. COLLECTION — `templates/collection.json` (target ≤ 8 screens for 27 products)

1. `elmsnest-s-coll-header` (new) — renders `elmsnest-v2-ground-collection` first (it is the first
   section). `collection.image` (or on /all the decor collection image, setting `all_image`) as a
   ~42 vh night header, veil to `#020306` at the bottom, `<h1>` = `collection.title` (Frank Ruhl
   Libre 32), the place word as a gold eyebrow above it, one muted line under it:
   «{count} מוצרים · {price_min}–{price_max} ₪» (from `collection.products` — no typing), and on
   per-place collections the approved deck line «מתאים כדי {yes} · לא מתאים כש־{no}» (5.2).
   Under the header: the FILTER ROW — hairline pills «הכל» + the four collection titles in the menu
   order, current one gold-filled; each is a plain `<a>` to the collection. ~0.9 screen.
2. `main-collection` (stock Kalles) — settings from the pre-env2 template with these changes:
   `enable_filtering: false`, `enable_num_cols_selector: false`, `enable_sorting: true`,
   `products_count: 28` (27 products → one page), `col_mb: "2"`, `col_tb: "3"`, `col_dk: "4"`,
   `image_ratio: "portrait"` or the theme's 4/5 equivalent, `show_description: false`,
   `pagination_type: "links"`, `color_scheme: "scheme-env2-night"`, `colors_by_section: true`,
   `space_items: "x"`, no filter block. The skin (5.1) hides the rest of the toolbar. ~5 screens.
3. `elmsnest-s-guide-strip` (new) — one hairline row: «כמה אור צריך המקום?» · «למדריך המלא ←»
   (/pages/guide-garden-lighting) and the contact line (5.4). ~0.4 screen.
4. `elmsnest-s-terms` (5.3). ~0.5 screen.
Footer. Removed: scene, ruler, bands, span, ledger, coll-terms, coll-goodnight. Expected ≈ 7 screens.
The sort select must offer: מומלץ (manual) · מחיר: מהנמוך לגבוה · מחיר: מהגבוה לנמוך · א–ב.

## 8. PDP — `templates/product.elmsnest.json` (target ≤ 6 screens)

Reminder (HANDOFF §7 / WINNING-SPEC §8.1): the file is `product.elmsnest.json`; all 27 products carry
`templateSuffix: "elmsnest"`; NEVER touch `templateSuffix` and NEVER write `templates/product.json`.

1. `brc-nav-product` (stock breadcrumb) — «דף הבית › {collection title} › {product}».
2. `main-product` (stock Kalles) — the first section that renders `elmsnest-v2-ground-product`
   (via a `_liquid` block at the top of the group, one line: `{% render 'elmsnest-v2-ground-product' %}`).
   `_product-medias` static block: `mobile_media_layout: "thumbnails"`, `desktop_media_layout:
   "thumbnail_left"`, `image_ratio: "adapt_image"`, `image_zoom: "zoom_lightbox"`,
   `use_select_varaint_change_media: true`, `show_first_media: false` — all of `product.media`, Shopify
   order, featured first (P3).
   `_group-product` block order (nothing else):
   1. `_liquid` kicker: `{% render 'elmsnest-s-pdp-kicker', product: product %}` → one gold small
      line «{place word} · מתאים כדי {yes}» (5.2), blank if no place.
   2. `_product-title` (h1, Frank Ruhl Libre via skin).
   3. `_product-price` (stock; the skin hides compare-at).
   4. `_liquid` per-unit caption: `{% render 'elmsnest-pdp-unit-price', product: product %}` — the
      EXISTING snippet (verify it prints «≈ X ₪ למטר / ליחידה» for the selected variant and updates on
      variant change; if it does not update, the engineer adds the data attribute the Kalles variant
      script already dispatches on and a ≤ 20-line inline script). One line, muted, 13 px.
   5. `_product-variant-picker`: `picker_type: "block"` (pills), `color_picker_type: "block"`.
   6. `_product-buy-button`: `show_quantity_selector: true`, `show_dynamic_checkout: false`
      (checkout is disabled on this plan — a "buy now" button that fails is worse than none),
      `show_wishlist: false`, `show_compare: false`, `btn_fullwidth: true`, `btn_style: ""`.
   7. `_liquid` terms line: `{% render 'elmsnest-s-pdp-terms-line' %}` → ONE line, 13 px muted, with
      `<bdi>`: «משלוח חינם לנקודת איסוף · אספקה 8–17 ימי עסקים · ביטול עד 14 יום» + «לכל התנאים ←»
      → /policies/shipping-policy.
   8. `_liquid` not-for + contact: `{% render 'elmsnest-s-pdp-notfor', product: product %}` → two
      lines on a hairline: «לא מתאים כש־{no}.» (5.2) then the contact line (5.4) with the product
      title prefilled. The ONLY photo CTA in the body.
   Section settings: `hdt_show_sticky_atc: true`, `sticky_atc` as the stock default,
   `color_scheme: "scheme-env2-night"`, `colors_by_section: true`. ~1.8 screens mobile.
3. `elmsnest-s-pdp-facts` (new) — the PDP's one signature device kept from env2: the big outlined
   numeral (IP65 / the LED count / the wattage — derived exactly as `elmsnest-v2-pdp-facts` derives
   it; copy that derivation, not the layout) beside a standard spec table `<dl>` from the description
   bullets (the same fallback chain as env2-facts: `<li>` under «פרטים שכדאי לדעת», else the « · »
   run under «פרטים טכניים»). Below it a read-only variant table when the product has > 1 variant:
   variant title · price · ≈ per unit (no buttons, no radios). Then the product description OPEN
   (`product.description`, the `.elms-sales` HTML the store already carries), with a «קרא עוד» clamp
   at 8 lines. NO «מה שלא כתוב» row, NO «אין לנו מה למדוד» line. ~1.6 screens.
4. `related-products` (stock Kalles): `limit: 4`, `col_mb: "2"`, `col_dk: "4"`, `display_type: "grid"`
   (no carousel on mobile), `collection` = auto (same collection), heading via its `section-heading`
   block: «עוד לאותו מקום». ~1.2 screens.
Footer. Removed: stage, fit, night, ledger, facts (env2), terms (env2), ask, related (env2).
Expected ≈ 5.3 screens. The number of `form[action*="/cart/add"]` on the page must be exactly 1
(the sticky bar reuses it).

## 9. Owner admin actions (outside theme code — written for the report, not done by us)

- **Cookie banner** (his answer 5): Shopify Admin → Settings → Customer privacy → Cookie banner →
  choose the compact bottom-bar position and colours; optionally limit the regions. We do not
  assert what the law requires — his call.
- **Images content task** (his answer 2, later): a sheet listing the 5 products with a clean frame to
  move to position 1 (firefly → images[3], edison → images[3], powerful-garden → images[2],
  indoor/outdoor wall → images[4], waterproof wall → images[1]) and the 14 with none; approve before
  any Admin change.
- **compare-at price** on waterproof-solar-deck-step-lights (199.90) — clear it in Admin (OWNER-NOTES
  2026-09-02, "no sales"); the skin hides compare-at meanwhile.
- **Mailbox**: Notion goal #1; the email CTA exists by his decision but cannot receive until DNS is fixed.

## 10. Files

New (all ≤ 12 KB each): `snippets/elmsnest-s-skin.liquid`, `snippets/elmsnest-s-place.liquid`,
`snippets/elmsnest-s-terms.liquid`, `snippets/elmsnest-s-contact.liquid`,
`snippets/elmsnest-s-pdp-kicker.liquid`, `snippets/elmsnest-s-pdp-terms-line.liquid`,
`snippets/elmsnest-s-pdp-notfor.liquid`, `sections/elmsnest-s-collections.liquid`,
`sections/elmsnest-s-products.liquid`, `sections/elmsnest-s-fit.liquid`,
`sections/elmsnest-s-terms.liquid`, `sections/elmsnest-s-coll-header.liquid`,
`sections/elmsnest-s-guide-strip.liquid`, `sections/elmsnest-s-pdp-facts.liquid`.
Edited: `sections/elmsnest-v2-hero.liquid` (two settings), `layout/theme.liquid` (one render line),
`templates/index.json`, `templates/collection.json`, `templates/product.elmsnest.json`.
Untouched: everything under `templates/customers`, `config/settings_data.json`, all Kalles files,
the old env2 sections (they simply leave the templates).

Section files use `{% schema %}` with Hebrew labels ≤ 70 chars, `"presets"` so they appear in the
editor, and `{% style %}`/`<style>` (NOT `{% stylesheet %}`) so CSS is in the HTML and measurable.
No `"""` sequence anywhere (deploy uses GraphQL block strings). Liquid: never a `{n}` placeholder
inside `{{ }}` (Ruby Liquid closes the tag at the first `}`).

## 11. Deploy and verification (the lead does this from the main loop)

Order: snippets → sections → `layout/theme.liquid` (read current, add one line) → the three templates.
`themeFilesUpsert` on `gid://shopify/OnlineStoreTheme/154726400174` only. `userErrors` must be `[]`.
Then `brief/side-pages/simplify/verify.js` (Playwright, real preview URL, JS on and off) checks per
page and viewport (390×844, 360×640, 1366×900):
- screens ≤ target; no horizontal overflow; 0 «Liquid error»; 0 `svg` plates; 0 occurrences of «איור»;
- every `.hdt-card-product img` src contains the product's featured image filename (compare with
  the Admin API list) — 27/27 on /collections/all;
- PDP: exactly 1 `form[action*="/cart/add"]`; a quantity input; variant pills; price updates on pill
  change (JS on) and the form still posts the right `id` (JS off); add-to-cart opens the drawer;
- terms strip count = 1 per page; `a[href^="mailto:"]` in `<main>` = 1 per page; «וואטסאפ» = 0;
- the four places in the same order on the home tiles and the collection filter row as in the header menu.
Screenshots of the whole flow (home → collection → PDP → drawer) at 390×844 go into the owner artifact.
