# ElmsNest — SIMPLIFY spec v2 (round 3, 2026-09-05)

v2 = v1 after three adversarial critiques (`SPEC-CRITIQUE.txt`): 31 defects, all resolved below.
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

Measured behind it (mobile 390×844, `audits.txt`): home 10.3 screens, collection /all 25.8 screens
with the 27 products listed ≈74 times, PDP 10.2 screens with three add-to-cart forms plus a gold link
that looks like a fourth; the four consumer terms twice per page; «שלחו תמונה של המקום» 3–5× per
page; 16 of 27 collection cards drawn as SVG plates captioned «איור · אין תצלום נקי», 5 more showing a
non-featured frame; the whole theme on `rgb(2,3,6)`.

## 1. The owner's five answers (2026-09-05, verbatim, binding)

| # | Question | Answer | Consequence |
|---|---|---|---|
| 1 | Visual direction | «النظرة الليلية الداكنة بس مبسّطة» | Keep the night look and the env2 tokens. Rebuild the STRUCTURE with standard shopping patterns. The dev homepage on 154726400174 is rebuilt in this language too (the live v3 paper homepage on 154652737710 stays untouched — publishing is a separate owner decision). |
| 2 | Images | «موافق» | `product.featured_image` first, everywhere, now — posters included. No glyph plates, no index resolver, no `image_index` overrides. Reordering the 5 products with a clean frame and generating clean renders for the 14 without one is a SEPARATE content task that waits for the owner's approval of a sheet. |
| 3 | «שלחו תמונה של המקום» | «فش رقم واتس، خلي البريد» | Keep the promise, on email, ONCE in the body of each page + once in the footer. URL from `snippets/elmsnest-v2-photo-url.liquid` (mailto). Never the word «וואטסאפ»; `settings.whatsapp_number` stays empty this round. Known risk, owner-accepted: elmsnest.com has no MX record (re-measured 2026-09-05), so mail to info@ does not arrive until DNS is fixed — Notion goal #1. |
| 4 | Collection naming | «هيك» | Label = the Shopify collection title. The place word (שביל / קיר / גינה / מרפסת) appears as a short muted sub-line only where it carries information (collection header meta line, PDP kicker, the home fit rows) — never as a gold eyebrow above a title. The four collections are the primary entry; `/collections/all` is a standard grid with a collection filter row. ONE order everywhere = the main-menu order: תאורת שביל, עמוד וגינה → תאורת קיר → ספוטים, פרוז׳קטורים ותאורה ניידת → גרילנדות ותאורה דקורטיבית (= שביל → קיר → גינה → מרפסת). |
| 5 | Cookie banner | «بنقدر نصغّره» | It is Shopify's own Customer-privacy banner (the theme's `cookies` section is disabled; no app embed). Not reachable from theme code or the Admin API → owner action, §9. |

## 2. Principles (acceptance criteria, testable)

P1 **Every ACTION uses the pattern a Shopify shopper already knows.** Browse = one grid of identical
cards (stock Kalles `card-product1`). Choose = the stock variant pills inside the buy box. Quantity =
the stock stepper. Buy = the stock main form; the stock sticky bar is a SECOND form kept in sync
(§8.2.9). After add = the Kalles cart drawer. Sort = a native `<select name="sort_by">` (ours; the
stock popover is off). Filter = a wrapping row of collection links. Creativity lives only in the
non-action layer: the hero photograph and its dusk darkening + sun rail, the collection header
photograph, typography, the IP numeral on the PDP.

P2 **Each buyer question is answered exactly once per page** (map in §3). The consumer terms
appear once on the home (strip) and once on the PDP (one line under the button); the collection has
none (footer links suffice; BRIEF §3 only requires them findable on the homepage). The photo/email
promise appears once in the body of each page (the contact line, §5.4) and once in the footer. The
four place words appear in the body only in the home fit block and the collection header meta line.
Header and footer groups are OUR files (`sections/header-group.json`, `footer-group.json`) and are
held to the same rules.

P3 **Images: the store's own images, in the store's own order.** Cards use
`img.hdt-card-product__media--main` = `product.featured_image` (hover image off via settings);
galleries show `product.media` in Shopify order, starting on media 1. No resolver, no banned
indexes, no glyphs, no `[data-lamp]` on any product image, no opacity-until-lit, no reveal-on-scroll
on cards.

P4 **Copy is Hebrew, verbatim, and makes no claim.** Place pairs from BRIEF §3 in the env2-licensed
joined forms (§5.2). Terms only in the licensed wording (§5.3, copied byte-for-byte from
`templates/collection.json` coll_terms rows). No reviews, no sales/popularity counts or ranks
(«הנמכרים ביותר» must not render), no urgency, no "best", no baked-in text of ours. Catalogue facts
(product counts, price ranges) are allowed. Buttons: the stock Kalles labels («הוסיפו להזמנה» on
the PDP form and sticky bar) and our one gold pill «לכל המוצרים». Text links use the ל־ infinitive
form only: «לשלוח תמונה של המקום ←», «למדריך לבחירת תאורה ←», «לכל התנאים ←», «כל מה שכתוב על
המוצר». Cards carry NO button and no overlay control — the whole card is the link. Section headings carry
no terminal period (the two-line hero sentence «כשהשמש יורדת, / הגינה נדלקת.» kept by §6.1 is exempt). No «+» and no «;» in storefront Hebrew. Guillemets «» in this spec are notation,
never typed into defaults.

P5 **Length.** Mobile 390×844, footer included: home ≤ 6 screens, collection ≤ 8 for 27 products,
PDP ≤ 6 (measured on solar-rope-string-lights 16 variants, decorative-led-net-lights 30 variants,
stainless-steel-solar-path-light-ip65 1 variant). Desktop 1366×900 proportionally shorter.

P6 **No-JS and a11y.** The main PDP form posts a variant id without JS via a `<noscript><select
name="id">` (§8.2.6). Sorting works with `?sort_by=` without JS. 44 px tap targets (pills
`min-height:44px`). Contrast ≥ 4.5:1 for text. `prefers-reduced-motion` respected. Every en-dash
range and every Latin/number token that sits inside a Hebrew line is `<bdi dir="ltr">…</bdi>`
(reuse `snippets/elmsnest-v2-bdi-range.liquid` or the v2-terms loop): «<bdi>8–17</bdi> ימי עסקים»,
«<bdi dir="ltr">89.90–999.90</bdi> ₪», IP65, LED, 10W, «7 מ׳ / 50 נורות» values.

P7 **Nothing is deleted from the theme in this round.** Old env2 sections stay as files but leave
the templates (rollback = restore three JSON files). Deleting files is a later cleanup.

## 3. Question map (the acceptance test for P2)

| Question | Home | Collection | PDP |
|---|---|---|---|
| Where am I / what is this store? | hero | header (h1 + meta line) | kicker line (collection link) |
| Which four places / collections? | collection tiles (title + count) | filter row | — |
| Which products, what price? | featured grid (4 cards) | THE grid (all) | related grid (4) |
| Does it suit my place / when not? | fit block (4 rows) | one deck line in the header | not-for line under the buy box (solar-gated) |
| How do I choose length / colour / quantity? | — | — | variant pills + quantity stepper |
| How do I buy? | card → PDP | card → PDP | the main form button (+ sticky bar) |
| What does it cost per metre / per unit? | — | — | one caption line under the price |
| Specs / IP? | — | — | facts section (numeral + dl + collapsed description) |
| Terms? | terms strip (3 numerals) | — (footer links) | one line under the button → /pages/shipping-delivery |
| Not sure? | contact line in the fit block | contact line in the guide strip | contact line in the not-for block |
| Where next? | footer | footer | related + footer |

## 4. Design tokens (unchanged, from `snippets/elmsnest-v2-core.liquid` on the DEV THEME)

- Ground: `html{background:#020306}`; index page gets the dusk→night gradient from
  `elmsnest-v2-ground-index` (rendered by the hero); collection pages from
  `elmsnest-v2-ground-collection` (rendered by `elmsnest-s-coll-header`); product pages from
  `elmsnest-v2-ground-product` (rendered by the first `_liquid` block of the buy box).
- Ink `#f4eee3`, muted `#c9c4b8`, gold `#e9b96e`, glow `#ffd394`, hairline `#1f1e1d`, card ground
  `#05070c`. Radius 0 everywhere except pill buttons (999px).
- Type: Frank Ruhl Libre 700/900 for display and product titles; Heebo for everything else.
  Mobile display 30–34 px, section headings 24–26 px, body 16 px, captions 13 px (never below 12.5).
- Motion: the hero's dusk darkening (`--env2-p`) and sun rail only. No lamps anywhere (the hero
  card, its only `[data-lamp]`, is off). Nothing else animates on scroll.
- The dev theme's copies of `elmsnest-v2-hero.liquid`, `elmsnest-v2-core.liquid` and
  `product.elmsnest.json` differ from the repo copies (critique proof, md5). The repo copies are
  re-synced from the dev theme before this round's edits (the lead does it, §11).

## 5. Shared pieces (new files, all small)

### 5.1 `snippets/elmsnest-s-skin.liquid`
One `<style>` block (plain `<style>`, not `{% stylesheet %}`), rendered from `layout/theme.liquid`
right after `{%- render 'elmsnest-v2-core' -%}`, dressing the STOCK Kalles components in the night
language. Exact selectors (verified in the critique against Kalles 5.4.2):
- Cards: `.hdt-card-product{background:#05070c;border:1px solid #1f1e1d;border-radius:0}`; title
  `.hdt-card-product__title` Frank Ruhl Libre 17/1.3, ink, clamped 2 lines; price `hdt-price.hdt-price`
  Heebo 16 gold — the range form «₪69.90 - ₪159.90» is accepted as is (`price_varies_style` "1").
  Hide: `.hdt-card-product .hdt-product-btns, .hdt-card-product .hdt-badge__wrapp, .hdt-card-product
  .hdt-badge, .hdt-card-product__media--hover, .hdt-card-product hdt-variant-option,
  .hdt-scrolling-badge, hdt-compare-at-price {display:none}`. Force visible:
  `hdt-reval-items[reveal-on-scroll=true] .hdt-card-product{opacity:1!important;transform:none!important}`
  (comment: Kalles base.css:1782 starts cards at opacity 0 until intersection).
- Collection toolbar: `.hdt-shop-control{display:none}` (our sort select replaces it).
- main-product: `h1` product title Frank Ruhl Libre 28/32 mobile, 38 desktop; price 26 gold;
  variant pills `.hdt-product-form__values label{min-height:44px}` hairline, selected = gold fill +
  ink `#1a1206`; quantity stepper hairline; `.hdt-product-form__submit.hdt-btn` gold pill full width
  52 px; sticky bar `.hdt-sticky-btn-atc{background:#05070c;border-top:1px solid #1f1e1d}` and
  `.hdt-sticky-atc__qty-selector{display:none}` (one quantity control on the page);
  `@media(max-width:900px){html body.hdt-page-type-product{padding-block-end:0}}` (the env2 ground
  reserved 78px for a buy bar that no longer exists; Kalles' sticky bar reserves its own).
- Description container (inside `<details>`): `.elms-sales{background:transparent;border:0;
  border-radius:0;color:inherit;font-family:inherit;padding:0} .elms-sales__cta,.elms-sales__specs,
  .elms-sales__kicker{display:none}` (the stored description is a cream, rounded, Rubik sales card).
- `cart-drawer`: ground `#05070c`, hairlines, gold checkout button, Frank Ruhl Libre line titles.
- Related grid = the same card rules (one card implementation site-wide).
≤ 300 lines. `!important` only where a Kalles rule forces it, each one commented with the source line.

### 5.2 `snippets/elmsnest-s-place.liquid`
Input: `collection` or `product`, plus `emit`. Output (text, nothing else):
`emit:'word'` → the place word; `emit:'yes'` → the infinitive suits-phrase (so «מתאים כדי {yes}»
parses); `emit:'no'` → the full licensed sentence; `emit:'collection'` → the matched collection handle.
Mapping by collection handle, env2-licensed joined forms (sources: BRIEF §3; `elmsnest-v2-coll-scene`
lines 98–107; `elmsnest-v2-pdp-fit` allowed list):
- `תאורת-שביל-סולארית` → שביל · לראות את הדרך · «לא מתאים כשהמקום כמעט אינו מקבל אור יום.»
- `solar-wall-lights` → קיר · להאיר נקודה מסוימת · «לא מתאים כשנדרש אור חזק וקבוע לאורך כל הלילה.»
- `ספוטים-ופרוז-קטורים-סולאריים` → גינה · להאיר עץ או ערוגה · «לא מתאים כשנדרשת התקנה מיוחדת או חיבור קבוע.»
- `גרילנדות-ותאורה-דקורטיבית` → מרפסת · ליצור אווירה · «לא מתאים אם צריך אור חזק — זו אינה מטרתה.»
For a product: the first of `product.collections` that matches, in the menu order above (this skips
the `sale` collection). No match → prints nothing.
**Solar gate (P4):** for a product in the path / wall / spot collections, `emit:'no'` prints nothing
unless the product is solar — copy the env2 test from `elmsnest-v2-pdp-fit.liquid` lines 98–112
(`custom.power_source == 'סולארי'`, else title + description contain «סולארי»). The decor pair is
ungated. Home rows and collection headers speak of the collection and keep the pair.

### 5.3 `snippets/elmsnest-s-terms.liquid` + `sections/elmsnest-s-terms.liquid` (HOME only)
THREE rows on hairlines: numeral (Frank Ruhl Libre 26, gold, inside `<bdi>`) + unit + headline +
sub-line — copied BYTE-FOR-BYTE from the current dev-theme `templates/collection.json` →
`coll_terms` block settings for the rows 0 ₪ / 8–17 / 14 (the «1 תמונה» row is dropped: the contact
line §5.4 is the only photo promise). Foot line: the four links with labels verbatim from
`elmsnest-v2-coll-terms.liquid` line 335 («משלוחים ואספקה · זמני טיפול · מדיניות ביטולים · שאלות
נפוצות») pointing to /pages/shipping-delivery · /pages/processing-time · /policies/refund-policy ·
/pages/help-faq. Section schema: `heading` (label «כותרת», default «ארבעה מספרים שכדאי לדעת» → use
«שלושה מספרים שכדאי לדעת»; three rows now). The section root carries `id="env2-terms"` so the
footer's existing `/#env2-terms` link keeps working. ≤ 0.5 screen.

### 5.4 `snippets/elmsnest-s-contact.liquid`
One line: «לא בטוחים? נבדוק התאמה לפני שתזמינו.» then the link «לשלוח תמונה של המקום ←» (hairline
underline). href = `{% render 'elmsnest-v2-photo-url', body: <body> %}` where body =
«שלום, מצרף/ת תמונה של המקום שרוצים להאיר.» and, only when `product` is given, appended with
« המוצר ששוקלים: {{ product.title }}» (the logic of `elmsnest-v2-pdp-photo-cta`). Subject = the
builder's default. Never says a channel name. The phrase «תמונה של המקום» must occur exactly once in
`<main>` per page (§11).

### 5.5 Cards — NOT built. Kalles `card-product1` skinned by 5.1, rendered by main-collection and by
`elmsnest-s-products`. Any custom section that renders the card MUST load
`{{ 'product-card.css' | asset_url | stylesheet_tag }}{{ 'collection-products.css' | asset_url | stylesheet_tag }}`
(the index template never loads `product-styles`) and wrap the cards in
`<div class="hdt-collection-products hdt-row-grid hdt-grid-cols-2 md:hdt-grid-cols-2 lg:hdt-grid-cols-4 hdt-ratio--portrait">`
calling `render 'card-product1', card_product: p, section_id: section.id, sizes: '(min-width:1150px) 25vw, 50vw', image_ratio: 'portrait', class: 'hdt-pr-style1', btn_wishlist_code: '', show_vendor: false`.

## 6. HOME — `templates/index.json` (target ≤ 6 screens mobile; estimate ≈ 4.7)

1. `elmsnest-v2-hero` — edit the DEV-THEME copy minimally: one new setting `show_card`
   (checkbox, label «להציג את כרטיס המוצר בהירו», default false) gating lines 121–141 (the card,
   including the design_mode branch). Keep lines 10–29 (the product still feeds the background).
   Template settings: `show_card: false`, `note_title: ""`, `note_text: ""` (the section hides an
   empty note), `cta_secondary_label: ""` (hidden when blank), `cta_primary_label: "לכל המוצרים"`,
   `cta_primary_link: "/collections/all"`, `lead: "מנורות שביל, קיר, גינה ומרפסת. קטגוריה אחת בלבד — ואם מוצר לא מתאים למקום שלכם, נגיד את זה לפני שתזמינו."`
   (menu order), keep eyebrow/headline/`show_sun_rail` (the headline keeps its terminal period; P4 exempts it). ~1 screen.
2. `elmsnest-s-collections` (new, name «ElmsNest S — קולקציות») — heading «איפה צריך אור?». 2×2 grid
   (mobile) / 4-across (desktop) of tiles: `collection.image` (object-fit cover, 4/5, per-block
   `object_position` text setting, default «50% 50%», wall tile «0% 50%»), the Shopify title (Frank
   Ruhl Libre 20), «<bdi>N</bdi> מוצרים» muted. No place word, no numerals. Whole tile is the link.
   Blocks: 4 × `collection` in the menu order. ~1.2 screens.
3. `elmsnest-s-products` (new, name «ElmsNest S — מוצרים») — settings: `heading` (default «מה שנדלק
   ראשון»), `source` select (`list` | `related`), `product_list` (label «ארבעת המוצרים בעמוד הבית»,
   limit 4). `list` mode: a 2-col grid of exactly 4 `card-product1` cards per §5.5; defaults:
   outdoor-bidirectional-led-wall-light-ip65, powerful-solar-garden-light, solar-edison-string-lights,
   solar-firefly-garden-lights. `related` mode (PDP, §8.4): the place collection via 5.2
   `emit:'collection'`, skip the current product, first 4. ~1.4 screens.
4. `elmsnest-s-fit` (new, name «ElmsNest S — מתי לא») — heading «מתי כן, ומתי לא». Four rows on
   hairlines, menu order: place word (gold, Frank Ruhl Libre) · «מתאים כדי {yes}» · «{no}» (full
   sentence from 5.2). Foot: «למדריך לבחירת תאורה ←» → /pages/guide-garden-lighting, then the
   contact line (5.4). ~1 screen.
5. `elmsnest-s-terms` (5.3, `id="env2-terms"`). ~0.5 screen.
Then the Kalles footer (≈ 1 screen). Removed from the template: first-lit, places, switch, night-wall,
atmosphere, goodnight, the hero card, the hero photo button.

## 7. COLLECTION — `templates/collection.json` (target ≤ 8 screens; estimate ≈ 7.3 incl. footer)

1. `elmsnest-s-coll-header` (new, name «ElmsNest S — כותרת») — renders `elmsnest-v2-ground-collection`
   first. `collection.image` (on /all: setting `all_image` image_picker, label «תמונת הכותרת בעמוד כל
   המוצרים», fallback = the decor collection image) as a ~40 vh night header with a veil to `#020306`
   at the bottom; `<h1>` = `collection.title` (Frank Ruhl Libre 32) — on /all the setting `all_title`
   (label «כותרת עמוד כל המוצרים», default «כל המוצרים»); meta line, muted, 14 px:
   «{place word} · <bdi>N</bdi> מוצרים · <bdi dir="ltr">{min}–{max}</bdi> ₪» (place word omitted on
   /all; numbers from `collection.products` — nothing typed); on per-place collections the deck line
   «מתאים כדי {yes} · {no}» from 5.2. Then the FILTER ROW: `display:flex;flex-wrap:wrap;gap:8px`,
   pills `min-height:44px`, never truncated, right-aligned: «כל המוצרים» (→ /collections/all) + the
   four Shopify titles in menu order, the current one gold-filled; plain `<a>` each. Then the SORT:
   `<form method="get" action="{{ collection.url }}"><select name="sort_by" onchange="this.form.submit()">`
   with exactly four options — `manual` «מומלץ», `price-ascending` «מחיר: מהנמוך לגבוה»,
   `price-descending` «מחיר: מהגבוה לנמוך», `title-ascending` «א–ב» — selected =
   `collection.sort_by | default: collection.default_sort_by`, `<noscript><button>מיון</button></noscript>`,
   hairline pill style, `aria-label="מיון"`. ~1 screen.
2. `main-collection` (stock Kalles), settings: `"product_des":"1","enable_list_default":false,
   "image_ratio":"portrait","image_size":true,"show_vendor":false,"pr_border":"none",
   "products_count":28,"col_dk":"4","col_tb":"3","col_mb":"2","space_items":"x",
   "pagination_type":"links","enable_progressbar":false,"paginate_pos":"center","dis_pagination":40,
   "enable_sorting":false,"enable_filtering":false,"enable_num_cols_selector":false,
   "show_description":false,"colors_by_section":true,"color_scheme":"scheme-env2-night",
   "background_opacity":1,"section_layout":"container","pd":",,30px,","pd_mb":",,22px,"`, no
   blocks. (A tester who once used the old column switcher has `cart.attributes.products_items_per_row`
   overriding columns — verify in a fresh context.) ~4.8 screens.
3. `elmsnest-s-guide-strip` (new, name «ElmsNest S — מדריך») — one hairline block: «כמה אור צריך
   המקום?» · «למדריך לבחירת תאורה ←» (/pages/guide-garden-lighting), then the contact line (5.4).
   ~0.4 screen.
Then the footer. No terms strip on the collection. Removed: scene, ruler, bands, span, ledger,
coll-terms, coll-goodnight.

## 8. PDP — `templates/product.elmsnest.json` (target ≤ 6 screens; estimate ≈ 5.2)

Reminder (HANDOFF §7 / WINNING-SPEC §8.1): the file is `product.elmsnest.json`; all 27 products carry
`templateSuffix: "elmsnest"`; NEVER touch `templateSuffix` and NEVER write `templates/product.json`.
The `main-product` section key in the JSON MUST be exactly `main-product` (its form id is
`product-form-main-product{{ product.id }}` and the sticky form id is `form-product-sticky{{ product.id }}`).
No breadcrumb section (stock brc-nav-product prints only «בית › product» here).

1. `main-product` (stock). Section settings: `"sticky_atc":true,
   "hdt_show_sticky_atc":"hdt_show_scrolls_outside_the_scope_of_the_form",
   "hdt_layout_atc_mob":"hdt_layout_atc_mob_default","colors_by_section":true,
   "color_scheme":"scheme-env2-night","background_opacity":1,"fullwidth":false`.
   Static blocks: copy `main-product-sidebar` (`_product_sidebar`, static) and `main-product-medias`
   (`_product-medias`, static) from `brief/inventory/theme-src/templates/product.elmsnest.json`, with
   `"show_first_media":true,"use_select_varaint_change_media":false,"mobile_media_layout":"thumbnails",
   "desktop_media_layout":"thumbnail_left","image_ratio":"adapt_image","image_zoom":"zoom_lightbox"`.
   `_group-product` child blocks, in this order and nothing else:
   1. `_liquid` ground: `{% render 'elmsnest-v2-ground-product' %}`.
   2. `_liquid` kicker: `{% render 'elmsnest-s-pdp-kicker', product: product %}` → one 13 px line:
      `<a href="{{ collection.url }}">{{ collection.title }}</a> · מתאים כדי {yes}` (collection = the
      5.2 match; blank line if none).
   3. `_product-title` with `"tag":"h1"`.
   4. `_product-price` (stock).
   5. `_liquid` per-unit caption: `{% render 'elmsnest-s-pdp-unit', product: product %}` (new
      snippet): pre-render one `<span data-en-variant="{{ v.id }}" hidden>` per variant; if an option
      name contains «אורך» → metres = the leading number before «מ׳»/«מטר» → «≈ <bdi dir="ltr">X ₪</bdi>
      למטר»; else if an option is named «כמות» and its leading integer > 1 (or the value is «זוג» = 2)
      → «<bdi dir="ltr">X ₪</bdi> ליחידה» («≈» only when not exact); nothing otherwise. Never repeat
      the full price. Toggle on `variant:change` dispatched on `form.hdt-main-product-form` (copy lines
      40–64 of `elmsnest-pdp-unit-price.liquid`). Muted, 13 px.
   6. `_product-variant-picker`: `"picker_type":"block","color_picker_type":"block"`.
      Then a `_liquid` no-JS fallback block: `<noscript><select name="id" form="product-form-main-product{{ product.id }}" aria-label="גרסה">{% for v in product.variants %}<option value="{{ v.id }}"{% if v.id == product.selected_or_first_available_variant.id %} selected{% endif %}>{{ v.title }} – {{ v.price | money }}</option>{% endfor %}</select></noscript>`.
   7. `_product-buy-button`: `"show_quantity_selector":true,"show_dynamic_checkout":false,
      "show_gift_card_recipient":false,"show_wishlist":false,"show_compare":false,"btn_fullwidth":true,
      "btn_style":"","ani":"none"`. Label stays the theme's «הוסיפו להזמנה».
   8. `_liquid` terms line: `{% render 'elmsnest-s-pdp-terms-line' %}` → ONE 13 px muted line:
      «משלוח חינם לנקודת איסוף · אספקה משוערת <bdi dir="ltr">8–17</bdi> ימי עסקים · ביטול עד <bdi>14</bdi> יום מקבלת המוצר» + «לכל התנאים ←» → /pages/shipping-delivery.
      The same snippet carries the ≤ 10-line sticky sync script:
      `document.forms['product-form-main-product{{ product.id }}'].addEventListener('variant:change',function(e){var f=document.forms['form-product-sticky{{ product.id }}'];if(f&&f.id&&e.detail&&e.detail.variant)f.id.value=e.detail.variant.id});`
   9. `_liquid` not-for + contact: `{% render 'elmsnest-s-pdp-notfor', product: product %}` → on a
      hairline: «{no}» (5.2, solar-gated → possibly blank) then the contact line (5.4) with the
      product. The ONLY «תמונה של המקום» in the body.
   ~1.9 screens.
2. `elmsnest-s-pdp-facts` (new, name «ElmsNest S — נתונים») — the PDP's one signature device: the big
   outlined numeral = the IP code if the product's own bullets contain one (IP65 / IP67), else no
   numeral; its caption = that bullet, verbatim. Beside/below it a `<dl>` spec table from the bullets
   (same fallback chain as `elmsnest-v2-pdp-facts`: `<li>` under «פרטים שכדאי לדעת», else the « · »
   run under «פרטים טכניים»), every Latin/number token in `<bdi>`. Then `<details><summary>כל מה שכתוב
   על המוצר</summary>{{ product.description }}</details>` (skin 5.1 neutralises the card). No variant
   table. No «מה שלא כתוב» row, no «אין לנו מה למדוד» line. ~1 screen.
3. `elmsnest-s-products` in `related` mode, heading «עוד לאותו מקום» — 4 cards, plain 2/4-col grid.
   ~1.2 screens.
Footer. Removed: stage, fit, night, ledger, facts (env2), terms (env2), ask, related (env2).

## 9. Owner admin actions (outside theme code — for the report, not done by us)

- **Cookie banner**: Shopify Admin → Settings → Customer privacy → Cookie banner → compact
  bottom-bar position and colours; regions are his call.
- **Menu**: main-menu item «קולקציות» points to /collections (the stock cream list page); repoint to
  /collections/all (menus are store-wide, shared with the live theme → owner action).
- **Images content task** (answer 2, later): sheet of the 5 products with a clean frame to move to
  position 1 (firefly → images[3], edison → images[3], powerful-garden → images[2], indoor/outdoor
  wall → images[4], waterproof wall → images[1]) and the 14 with none; approve before any change.
- **compare-at** on waterproof-solar-deck-step-lights (199.90) — clear in Admin; the skin hides it.
- **Mailbox**: Notion goal #1. `whatsapp_number` stays empty.

## 10. Files

New (≤ 12 KB each): `snippets/elmsnest-s-skin.liquid`, `elmsnest-s-place.liquid`,
`elmsnest-s-terms.liquid`, `elmsnest-s-contact.liquid`, `elmsnest-s-pdp-kicker.liquid`,
`elmsnest-s-pdp-unit.liquid`, `elmsnest-s-pdp-terms-line.liquid`, `elmsnest-s-pdp-notfor.liquid`;
`sections/elmsnest-s-collections.liquid`, `elmsnest-s-products.liquid`, `elmsnest-s-fit.liquid`,
`elmsnest-s-terms.liquid`, `elmsnest-s-coll-header.liquid`, `elmsnest-s-guide-strip.liquid`,
`elmsnest-s-pdp-facts.liquid`.
Edited (from the DEV-THEME bodies): `sections/elmsnest-v2-hero.liquid` (one setting + the two editor labels of the secondary button, which no longer name the messenger),
`layout/theme.liquid` (one render line after core), `sections/footer-group.json` (four collection
labels = Shopify titles in menu order; © link stays `/#env2-terms` (kept alive by 5.3) or →
/pages/shipping-delivery; photo link label «לשלוח תמונה של המקום» with the same mailto as 5.4;
«כתבו לנו: info@elmsnest.com» unchanged — Shopify's richtext validator refuses `<bdi>` and `data-*` attributes there, so P6 and the `data-ens-place` markers do not apply to the footer; the order test reads the footer links' hrefs; `sections/header-group.json` gets the P6 `<bdi>` on the address in `note_mobile` (an HTML setting) — its only edit), `config/settings_data.json` (two keys only:
`"show_ultra_btn": false, "show_secondary_image": false`), `templates/index.json`,
`templates/collection.json`, `templates/product.elmsnest.json`.
Untouched: `templates/customers/*`, all Kalles files, locales, the old env2 sections.

Schema constraints: section/block `name` ≤ 25 chars, setting `id` ≤ 25 chars `[a-z0-9_]`, labels
≤ 70 chars, `presets[].name` ≤ 25, every section has `presets`. Use `{% style %}` or `<style>`, not
`{% stylesheet %}`. No `"""` anywhere. No `{n}` placeholder inside `{{ }}`. `_liquid` blocks cannot
see `section` or `settings`; the s-pdp-* snippets read only `product`, `collection`, `shop`, `routes`.

## 11. Deploy and verification (the lead, from the main loop)

Order: sync hero/core/footer-group/product template from the dev theme into the repo → engineers
edit → snippets → sections → `layout/theme.liquid` → `config/settings_data.json` → the three
templates. `themeFilesUpsert` on `gid://shopify/OnlineStoreTheme/154726400174` only; `userErrors`
must be `[]`. Then `verify.js` on the real preview, viewports 390×844 / 360×640 / 1366×900, JS on
and off, pages: home, /collections/all, the path collection, PDPs rope (16 variants), net (30),
stainless path (1):
- screens ≤ target; no horizontal overflow; 0 «Liquid error»; 0 «איור»; 0 «הנמכרים ביותר»;
  0 «וואטסאפ» / «ווטסאפ» / «WhatsApp» / `wa.me`; `.en-wa` count 0;
- cards: `img.hdt-card-product__media--main` src = the featured filename (featured.json) 27/27 on
  /all; 0 `svg` ≥ 100×100 inside `.hdt-card-product__media`; 0 `.hdt-card-product form`;
- PDP: `form.hdt-main-product-form` = 1, `form.hdt-sticky-atc__form` = 1, visible quantity inputs = 1,
  `noscript select[name=id]` present (JS off: submit reaches /cart with that id); pill change →
  price updates AND the sticky form's `input[name=id]` equals the chosen variant; clicking the sticky
  button adds the chosen variant (drawer line item id); the drawer opens after the main button;
- home: terms strip = 1 (`#env2-terms`); collection: terms strip = 0; PDP: `.ens-terms-line` = 1;
- «תמונה של המקום» occurrences in `<main>` = 1 per page; `main a[href^="mailto:"]` = 1; footer
  mailto = 1;
- the four collection names appear in the same order in the header menu, the home tiles, the hero
  lead, the collection filter row and the footer (`[data-ens-place]` order);
- every en-dash range inside `<main>` text sits inside a `<bdi>` — except inside the merchant's own description, which `elmsnest-s-pdp-facts` shows verbatim behind `<details>` by design (measured separately as `rangesInRawDescription`); the `sr-only` radios behind the 44 px pills are not tap targets; a `display:none` element cannot animate;
- reduced-motion: no transitions on `.hdt-card-product`.
- The screen targets bind at 390×844 (P5); 360×640 and 1366×900 are recorded for information. The PDP's
  «one terms line» count excludes the cart drawer, which (round 3) carries the same line inside `#CartDrawer`.
Screenshots of the whole flow (home → collection → PDP → drawer) at 390×844 go into the owner artifact.
