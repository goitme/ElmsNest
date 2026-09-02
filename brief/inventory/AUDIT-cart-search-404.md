# AUDIT — family `cart-search-404` (dev theme 154726400174, mirrored 2026-09-02)

Pages: `cart-empty`, `cart-full`, `search-hits`, `search-none`, `search-blank`, `p404`, `page-accessibility`, `blog-news`.
Judged from `http-desktop.png` / `http-mobile.png` (1440 / 390, 2x, theme JS running) sliced with `crops.py`, plus `index.html`. The stale `shot-*` renders were ignored.

## 0. Facts shared by every page in this family (read once)

- **Ground.** Every page body is Kalles `scheme-1`: text `#2b2118` on cream `#f7f0e6` (sampled `(247,240,230)`), secondary surface `#fffdf7`. `elmsnest-v2-base` is not rendered (`env2 base loaded: False`), so there is no sky gradient, no `--env2` tokens, no lamp logic. Only the header/footer carry `scheme-env2-night` (`#020306` / `#f4eee3`).
- **Type.** `--f_family_1/2/3: Assistant, sans-serif`. Frank Ruhl Libre and Heebo are not loaded on any page of this family (`FRL font loaded: False`; 0 matches for "Frank"/"Heebo" in the HTML).
- **Header (all 8 pages).** `<hdt-sticky-header class="… hdt-header-tranparent-true … is-sticky" color-scheme="scheme-env2-night">`, `background_opacity_transparent: 0`. Because the header is transparent with night-scheme ink, on a cream page the 9 nav links (`דף הבית · קולקציות ▾ · מדריך לבחירה · שאלות נפוצות · מי אנחנו · יצירת קשר`) and the search / cart / hamburger icons render **ink `#f4eee3` on cream `#f7f0e6` — invisible**. Visible at rest: only the gold house-heart logo (50 px) and the gold cart-count bubble ("0", "3"). Verified by pixel crop of the 0–80 px strip on desktop and mobile. The sticky (scroll-up) state paints it 90 % `#020306` — not visible in these static renders. Header height 70 / 60 px.
- **Footer (all 8 pages).** Already night-scheme: `#020306` ground, gold logo 72 px, 4 right-aligned columns in Assistant with underlined links: contact line "שאלות על מוצר או על התאמה למקום? כתבו לנו: info@elmsnest.com"; **קולקציות** (4 links); **מידע** (6 links: מדריך לבחירת תאורה לגינה, למה תאורה סולארית, מי אנחנו, משלוחים ואספקה, זמני טיפול, שאלות נפוצות); **יצירת קשר** (עמוד יצירת קשר, לשליחת תמונה של המקום — both → `/pages/contact-us`). Bottom bar: "ElmsNest © 2026 · תנאי משלוח וביטול" → `/#env2-terms` (homepage anchor). Desktop footer ≈ 450 px; mobile ≈ 900 px stacked. The cream page ends in a hard cut against the black footer on every page.
- **Cart drawer.** `sections--21567608946862__cart-drawer` is present on every page but the mirrored wrapper contains only a `<style>` rule — no `<hdt-cart-drawer>` markup was captured (it is injected by theme JS / Section Rendering). It is **closed in every render; its look cannot be judged from this inventory.** Configured (system-group.json): scheme `S-e0b7` (light cream `#fffdf7`), `btn_checkout` accent, discount/note/gift/estimator/complementary all off, `agree` and `img_trust` disabled, English `discount_error_message: "Enter a valid discount code"`.
- **Back-to-top** (`back_top`, progress ring `#d2cbc1` / `#2b2118`) is rendered on every page (hidden until scroll).
- **Console.** Every render logs the same 2 JS errors: `Failed to fetch dynamically imported module …3f57b3796d8c16827c06e9356048d925.js` and `Cannot read properties of null (reading 'innerHTML')` — likely a mirror artefact (a lazily imported Kalles module missing from the mirror), but keep in mind that quick-add / drawer / sort popovers were not exercised.
- `noindex,follow` is set on cart and search (correct, from `layout/theme.liquid`).

---

## 1. `cart-empty` — `/cart` with nothing in it

**Heights:** desktop 1789 px · mobile 2299 px.

### 1.1 What renders
Desktop (top → bottom):
1. Header, transparent, invisible nav (see §0); gold bubble "0".
2. **Title band** `main_heading_zHKQUU`: 120 px flat taupe-grey band (`#2b2118` scheme with `--bg-overlay:.54` → sampled `(136,128,119)`), no image, "ההזמנה שלך" white Assistant ~24 px centred. (`uppercase: true` has no effect on Hebrew.)
3. **`main-cart` empty state** (`scheme-1`, `pd: 70px,,50px`): ~290 px of cream whitespace, then a 90 px grey line icon of a cart with an ✕, "העגלה שלך ריקה" (h3, `hdt-text-12xl`, bold, ~28 px), two lines of Kalles translation copy — "לפני שתמשיך לקופה, עליך להוסיף כמה מוצרים לעגלת הקניות שלך." / "תמצא הרבה מוצרים מעניינים בדף "חנות" שלנו." — and a dark-brown square button **"חזור לחנות"** (`#2b2118`, 152×40 px) → `/collections` (the list-collections page, not a collection).
4. **`elmsnest-cart-guidance`** (custom, 2784 B): a bordered `#f7f0e6` panel on a `#fffdf7` band, h2 "לפני שממשיכים לתשלום" (~36 px bold), three white boxed cards with 1 px borders: **"זמן אספקה"** — "8–17 ימי עסקים בסך הכל: 1–3 ימי טיפול ועוד 7–14 ימי משלוח."; **"אפשרויות משלוח"** — "האפשרויות והעלות יוצגו בתשלום לפי הכתובת והזמינות."; **"בודקים את הפרטים"** — "ודאו שהמוצר, הכמות והגרסה שבחרתם נכונים לפני המעבר לתשלום."; then "חסר לכם פרט חשוב על מוצר? **פנו אלינו לפני ההזמנה**." → `/pages/contact-us`.
5. Footer (§0).

Mobile: same order; the band is ~130 px; icon + heading + copy + button sit in the middle of the first screen (button at ≈ 640 px CSS, inside the 844 px fold); the guidance panel becomes three stacked boxes (~900 px); footer ~900 px. **Mobile fold:** header, band, icon, "העגלה שלך ריקה", copy, "חזור לחנות" — no product, no price; the only CTA leads to `/collections`.

### 1.2 Against the design system
- Cream `#f7f0e6` page, `#fffdf7` guidance band, taupe band: the exact scheme that must go. Brown button `#2b2118`.
- Assistant everywhere; the h3 "העגלה שלך ריקה" is a generic sans, no serif display, no gold kicker.
- Three boxed cards + a bordered panel (`--en-radius-md/sm` from the PDP token set → radius present) — boxes inside a box, the "four equal boxes" pattern the owner rejected.
- Default Kalles empty-state device: grey cart-✕ icon, translation-file copy in masculine singular ("תמשיך", "תמצא"), quotes around "חנות" for a page that is called קטלוג/קולקציות here.
- Guidance section headed "לפני שממשיכים לתשלום" on a page where there is nothing to pay for — copy contradicts state.
- Band + 290 px of empty cream before the icon: half a desktop screen of nothing.
- Invisible header nav (cream-on-cream) — the only way back into the catalogue is the one brown button.
- Empty state offers zero products, zero collections, zero lamps.

### 1.3 Honesty check
No ratings/reviews/trust/countdown/best-seller/quotes in the rendered page. The only "rating"/"review"/"star" strings in the HTML are `--color-pr-rating:` CSS vars, Shopify preview-bar script URLs and the unused `hdt_star` SVG symbols. Guidance copy states only 1–3 + 7–14 = 8–17 business days. Missing (not fabricated): pickup / 29.90 ₪ door delivery, 14-day cancellation, "warehouses outside Israel" — none of the consumer terms except delivery time is on the cart page; the footer link "תנאי משלוח וביטול" points to the homepage anchor `/#env2-terms`.

### 1.4 Worth keeping
- `sections/elmsnest-cart-guidance.liquid`: the three lines of copy (delivery-time arithmetic, "costs shown at checkout", "check model/qty/variant") and the contact link are honest and correct — keep the words, drop the boxes. Its global touch-target overrides (`.hdt-main-cart__button-checkout{min-height:48px}`, `.hdt-quantity__button{44px}`) are worth carrying.
- `settings.empty_cart_link: shopify://collections` mechanic; `main-cart.liquid` `<hdt-main-cart>` / `CartPage-Form` skeleton.
- Footer group (already night scheme).

### 1.5 Verdict
"An empty grey cart icon on a beige page, with three boxes telling me about payment for nothing — this is the theme's default, not our store."

---

## 2. `cart-full` — `/cart` with 2× path light + 1 crystal-ball string

**Heights:** desktop 1791 px · mobile 2544 px.

### 2.1 What renders
Desktop:
1. Header (invisible nav), gold bubble **"3"**; the hidden mini-cart link reads "3 429.70 ₪".
2. Title band "ההזמנה שלך" (same taupe band as cart-empty).
3. **`main-cart` table** (`scheme-1`, width 1170): column heads right→left "מוצר | מחיר | כמות | סך הכל" over a hairline, then two rows separated by hairlines:
   - 120 px square photo (crystal balls at dusk — image index 0, clean, no baked text) · **"גרילנדת כדורי קריסטל סולארית – 20 עד 200 נורות"** (bold Assistant 16) · "אורך ומספר נורות: **5 מ׳ / 20 נורות**" · "צבע תאורה: **צבעוני**" · trash icon · price "89.90 ₪" · qty box (1 px dark border, 120×40, "+ 1 🗑" — trash replaces minus at qty 1) · total "89.90 ₪".
   - photo (three bollards on a hedge path — index 0, clean) · **"מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65"** · "צבע אור: **צהוב חם**" · trash · "169.90 ₪" · "+ 2 −" · "339.80 ₪".
   - Each row also carries a hidden error line "הכמות שבחרת אינה זמינה." and sr-only "מחיר מבצע" labels.
4. **Totals**, left-aligned (RTL start): "סכום ביניים  429.70 ₪" (h3 xl semibold), "כולל מיסים. משלוח מחושב בעת התשלום." (משלוח → `/policies/shipping-policy`), dark-brown square button **"תשלום"** (108×50 px, `#2b2118` / cream text, `name="checkout"`), empty `additional-checkout` container (accelerated buttons not rendered), `payment-terms` block. No note, discount, gift, estimator, trust icons (all off/disabled).
5. `elmsnest-cart-guidance` (identical to cart-empty).
6. Footer.

Mobile: header + band, then each line becomes a stacked block: photo right (240 px), title, variant lines, trash, then three dashed-rule rows "מחיר / כמות / סך הכל"; both items fit in the first screen. **Mobile fold (844 px):** header, band, both products with prices, qty steppers — the subtotal lands at ≈ 857 px and the **"תשלום" button at ≈ 920–975 px, i.e. just below the fold**; no sticky checkout. Desktop fold (900 px) contains everything down to the checkout button.

### 2.2 Against the design system
- Same cream/taupe/brown palette and Assistant type; price in plain ink, no glow.
- Classic 4-column e-commerce table with header row; qty stepper is a bordered box; checkout is a small brown rectangle bottom-left, visually lighter than the "לפני שממשיכים לתשלום" heading below it.
- Guidance boxes (three cards in a panel) sit *after* the checkout button — the heaviest visual on the page is the informational box set, not the sale.
- On mobile the buy button is below the fold and there is no sticky bar; three dashed separators per item are busy.
- No cross-sell, no "lamp" moment, no image of the product lit; nothing only a lighting store could have.
- Invisible header nav; band with no purpose.

### 2.3 Honesty check
Nothing fabricated. Prices/variants come from `cart.items`. "מחיר מבצע" is sr-only Kalles wording (translation of "sale price") applied to non-sale items — mislabels regular prices as sale prices for screen-reader users. Consumer terms: delivery time present (8–17 = 1–3 + 7–14); pickup/29.90 ₪, warehouses outside Israel, 14-day cancellation ≤5 % / 100 ₪, "send a photo on WhatsApp" — **not on the cart page** (contact link goes to the contact page because `whatsapp_number` is empty).

### 2.4 Worth keeping
- `sections/main-cart.liquid` mechanics: `<hdt-main-cart>` + `<cart-items-component>`, `CartPage-Form` (`action="/cart"`, `updates[]` inputs, `/cart/change?line=n&quantity=0` remove links → works without JS), `name="checkout"` submit, `additional-checkout` slot, `payment-terms`.
- `snippets/item-cart-page.liquid` variant-line output ("אורך ומספר נורות: 5 מ׳ / 20 נורות") — correct data.
- Cart images index 0 for these two products are clean photos (usable per WINNING-SPEC image ledger).
- Guidance copy (see §1.4).

### 2.5 Verdict
"A spreadsheet with a beige background; the pay button is smaller than the help boxes, and on the phone I have to scroll to find it."

---

## 3. `search-hits` — `/search?q=שביל` (13 results)

**Heights:** desktop 2603 px · mobile 3352 px. 13 product cards, 5 direct `/cart/add` forms (single-variant products), 8 quick-add buttons.

### 3.1 What renders
Desktop:
1. Header (invisible nav), bubble "0".
2. **`top-list-collections`** (`collections_list_simple_4yRUED`): a 45 px cream strip under a hairline with four text links "גרילנדות ותאורה דקורטיבית · ספוטים, פרוז׳קטורים ותאורה ניידת · תאורת קיר · תאורת שביל, עמוד וגינה" (menu `footer`, alphabetical, no images).
3. **Title band `main_heading_xYyUyq`: 100 px flat taupe band with NOTHING in it** — the `_heading_search` block is disabled; the h1 'חיפוש: 13 תוצאות עבור "שביל"' is in the DOM as `<h1 class="sr-only hdt-pe-none">`. The query and the count are never shown to a sighted user.
4. **Toolbar** (`main-search`, `scheme-1`): right "סנן" + funnel icon (opens `<hdt-drawer class="hdt-filter">`); centre six view icons (list, 2, 3, **4 active**, 5, 6 columns — `enable_num_cols_selector`); left a 190×40 bordered select-look popover "רלוונטיות ▾" (options: רלוונטיות / מחיר, נמוך לגבוה / מחיר, גבוה לנמוך).
5. **Grid 4 × (4,4,4,1)**, `card-product1`, ratio `asos` (portrait ≈ 4:5), `pr_border: none`, 30 px gutters. Card = image, title (Assistant medium 16, 2 lines, right-aligned), price (regular weight): e.g. "סט מנורות שביל סולאריות מתנדנדות ברוח – 2/6 יחידות IP65 — 189.90 ₪ - 329.90 ₪", "מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65 — 169.90 ₪", "תאורה סולארית עמידה למים לדק ולמדרגות — ~~199.90 ₪~~ 149.90 ₪" with a red circle badge rendered **"%25-"** (RTL-flipped "-25%", `#91212a`), "מנורות סולאריות למדרגות ולדק באור חם – 1/4/8/12 יחידות — 69.90 ₪ - 349.90 ₪" with two colour swatch dots (שחור / חום). Hover: secondary image (opacity effect) and quick-add "הוסף במהירות" (cart icon over the image, `aria-controls="hdt-quick-add-modal"`) or a direct "הוסיפו להזמנה" form for single-variant items. Variant pickers (`<hdt-variant-option hidden>`) are in the DOM for every card ("כמות: 2 יחידות / 6 יחידות", "צבע תאורה: צהוב / כחול / צבעוני / לבן", "Title: Default Title").
6. The 13th card sits alone in the last row; then a hard cut to the footer. No pagination (13 < `products_count: 16`), no result count, no "did you mean", no collection/article results.

Mobile: header; the top-list becomes a **slider with ‹ › arrows and clipped text ("…ספוטים, פרוז׳קטורינ")**; empty taupe band 80 px; toolbar "סנן" / three view icons (list, 1-col, 2-col) / "מיין ▾"; **2-column grid** with the quick-add cart icon as a dark square at the bottom-left of every image; titles truncate with an ellipsis ("סט מנורות שביל סולאריות מתנדנדות ברוח – 2/6 יחידו…"). **Mobile fold:** header, top-list slider, empty band, toolbar, two cards with titles and price ranges (189.90–329.90 ₪; 219.90–529.90 ₪) — product + price inside the fold; the quick-add icons appear on the full-page render.

Product images used (index 0) — eight of thirteen carry baked-in Hebrew marketing text: "מוסיפה אווירה לכל שביל וגינה", "עמיד למים IP65", "פאנל סולארי מוגדל · עד 14 שעות תאורה · +30% יעילות טעינה · 50,000 שעות עבודה", "תאורה סולארית לגינה", "האירו את המדרגות בשתי דרכים", "אווירה יוקרתית בשבילי ה…" (crops through the text), "תאורת מיתר סולארי", "עמידות לכל מזג אוויר · טווח עבודה −20° עד 60°C", "תאורה סולארית אלגנטית למעקה"; one image shows a third-party logo "LUMIÈRE OUTDOOR LIGHTING". Only five cards use clean photographs.

### 3.2 Against the design system
- Cream ground, taupe band, brown/dark UI, Assistant — none of the system.
- **Empty 100 px band** that says nothing; query and count hidden (`sr-only`).
- Full Kalles browse kit: filter drawer, six grid-size icons, sort popover, list view — a UI kit for a 13-result page.
- Facet labels untranslated: "**Availability**", "**Price**" (English), "0 נבחרו", "במלאי (13) / לא במלאי (0)"; price range 0–1000 inputs.
- Default product cards (portrait crop, title + price only), red circle sale badge that flips to "%25-", colour dots, quick-add cart squares on mobile; `hdt-line-clamp` truncation eats variant counts.
- Image ledger violated: baked-in text images at index 0, one competitor/supplier logo, crops cutting words in half.
- Orphan 13th card; no pagination logic needed but no closing device either — grid ends straight into the black footer.
- Latin/number flip: "%25-"; "Title: Default Title" leaks (hidden) for the 9-LED lantern.
- Mobile top-list slider clips text; three separate row-controls (סנן / views / מיין) for a phone.
- No lamp moment, no "search as a lighting store would", no suggestions.

### 3.3 Honesty check
- No review/rating/trusted/countdown/best-seller markup active (`show_rating: false`, `hdt_show_countdown_timer: false`; `hdt_star` symbols unused).
- Baked-in image claims: "50,000 שעות עבודה", "+30% יעילות טעינה", "עד 14 שעות תאורה", "טווח עבודה −20° עד 60°C", "IP65" on the "פאנל סולארי מוגדל" and spotlight images — numeric performance claims presented as image graphics, not sourced from product metafields; and the "LUMIÈRE OUTDOOR LIGHTING" brand mark on the bollard image.
- Sale: one genuine `compare_at` (199.90 → 149.90) rendered as "-25%"; sr-only "מחיר מבצע" is applied to every price.

### 3.4 Worth keeping
- `sections/main-search.liquid` data plumbing: `hdt-facet-filters-form` (`GET /search`, `q`, `type=product`, `sort_by`, `filter.v.availability`, `filter.v.price.gte/lte`, `options[prefix]=last`, `options[unavailable_products]=last`) — real Shopify search filters, works without JS.
- Per-card `<form action="/cart/add">` for single-variant products and `<hdt-variant-option>` data for multi-variant ones (the variant vocabulary — כמות / צבע תאורה / אורך ומספר נורות / גוון אור / הספק — is already in Hebrew and correct).
- Price-range output "189.90 ₪ - 329.90 ₪" (`price_varies_style: 1`) is the right data, wrong type.
- The five clean photos (crystal balls, bollards on hedge, stainless bollards on a path, fireflies, rope light).

### 3.5 Verdict
"A generic shop grid with a grey stripe above it and half the photos shouting Hebrew slogans — I can't even see what I searched for."

---

## 4. `search-none` — `/search?q=zzqqxx` (0 results)

**Heights:** desktop 1074 px · mobile 1344 px.

### 4.1 What renders
Desktop: header (invisible nav) → top-list-collections strip (4 links) → **empty taupe band** (h1 'חיפוש: 0 תוצאות עבור "zzqqxx"' sr-only) → `main-search` empty state: 90 px thin magnifier line icon, then a **full-width 1170 px box with a 1 px dark-brown border** containing a warning-triangle icon and "לא נמצאו מוצרים התואמים את הבחירה שלך." → 110 px cream → footer. **There is no search input on this page** — the user cannot retype the query except through the (invisible) header icon; no suggestions, no collections, no products.
Mobile: same; the message box spans the width at ≈ 440–510 px; footer starts at ≈ 590 px CSS. **Mobile fold:** header, clipped top-list slider, empty band, magnifier, warning box, top of footer — no product, no CTA.

### 4.2 Against the design system
- Cream/taupe/brown; Assistant.
- Empty band; the query is never echoed.
- Kalles translation copy "התואמים את הבחירה שלך" (filter-wording, not search-wording) in a bordered alert box with a warning icon — an error pattern for a normal outcome.
- No search form, no route forward, no lamps; 60 % of the desktop viewport is cream void.

### 4.3 Honesty check
Nothing fabricated; nothing at all, in fact.

### 4.4 Worth keeping
- Only the mechanic: `search.results_count == 0` branch of `main-search.liquid`; `search.terms` is available to echo the query and to link the four collections. The `top-list-collections` data source (footer menu, alphabetical) proves the collection menu is reachable in Liquid.

### 4.5 Verdict
"It tells me nothing was found and then leaves me on a beige wall with no box to try again."

---

## 5. `search-blank` — `/search` with no query

**Heights:** desktop 900 px (exactly one viewport) · mobile 1178 px.

### 5.1 What renders
Desktop: header → top-list strip → **empty taupe band** (h1 "חיפוש" sr-only) → a single 700×46 px search field, placeholder "חיפוש", cream `#fffdf7` fill, 1 px `#d2cbc1` border, with a 46×46 dark-brown square submit button (magnifier) on the RTL start side → 100 px cream → footer fills the rest of the viewport. Form: `GET /search`, hidden `resources[options][fields]=title,body,tag,product_type,variants.title,vendor,variants.sku`, `resources[limit_scope]=each`; `products_suggest: []` so no suggested products; predictive search (`predictive_search_enabled: true`) runs only after typing.
Mobile: field 340 px wide at ≈ 270–320 px; footer starts at ≈ 400 px CSS. **Mobile fold:** header, clipped slider, band, one input, half the footer.

### 5.2 Against the design system
- Same palette/type; square brown button; bordered input.
- Empty band above an empty page; no starting points (collections as words only, no lamps, no popular searches, no "search by place" idea).
- The page exists only as the fallback for the header icon; nothing on it earns the visit.

### 5.3 Honesty check — none.

### 5.4 Worth keeping
- `snippets/search-form.liquid` form (`data-frm-search`, `data-input-search`, `data-submit-search` hooks, the `resources[…]` hidden inputs that scope predictive search to products). `hdt_predictive-search.liquid` exists (renders `pr_loop_item`, `collection_loop_item`) and is the JS-driven suggestion engine to reuse.

### 5.5 Verdict
"One input box between a grey stripe and a black footer."

---

## 6. `p404` — a missing URL

**Heights:** desktop 1110 px · mobile 1445 px.

### 6.1 What renders
Desktop: header (invisible nav) → `main-404` (`scheme-1`, `min-height:60vh`, centred): **"עמוד לא נמצא"** h1 `hdt-h0` bold ~64 px with **`letter-spacing: 8px` applied to Hebrew**, "404" h3 xl semibold, "חזרה ל- **דף הבית**" (`letter-spacing: 2px`, link underlined with a 1 px brown rule, hover inverts to a brown block) → 130 px cream → footer. No search, no collections, no products, no image.
Mobile: 230 px of cream, then the three lines at ≈ 300–440 px, cream to ≈ 700 px, footer. **Mobile fold:** header, headline, "404", link, top of footer.

### 6.2 Against the design system
- Cream ground, brown ink, Assistant, letter-spaced Hebrew (a typographic error — Hebrew is never tracked out), a hyphen with a space "ל- דף" from the `link_html` translation.
- Kalles default 404 verbatim; nothing about lamps, dusk, or the store; no way into the catalogue except the home link and the invisible nav.
- 60vh of centred void on desktop, hard cut to the footer.

### 6.3 Honesty check — none.

### 6.4 Worth keeping
- Only `templates/404.json` → `main-404` slot and `routes.root_url`; the section is 2.5 KB and should be replaced whole (the copy "עמוד לא נמצא / חזרה לדף הבית" is fine as words).

### 6.5 Verdict
"The theme's 404 with our logo pasted on."

---

## 7. `page-accessibility` — `/pages/accessibility-statement` (unpublished → renders 404)

**Heights:** desktop 1110 px · mobile 1445 px — **pixel-identical to `p404`** on both viewports (image diff = no difference); same `<title>404 לא נמצא – ElmsNest</title>`, body `hdt-page-type-404`.

### 7.1–7.2 What renders / against the system
Exactly §6. The fact that matters: the store has the `sense-rtl` accessibility app block enabled and links nothing to a statement; the handle `accessibility-statement` (listed in HANDOFF §5 as a page to design) does not exist or is unpublished on the dev theme, and `elmsnest-content-page.liquid` only renders content for five hard-coded handles (`guide-garden-lighting`, `why-solar-lighting`, `processing-time`, `מי-אנחנו`, `help-faq`) — an accessibility page would fall into its `else` branch and would need `page.content` or a sixth branch.

### 7.3 Honesty check — none (nothing renders).

### 7.4 Worth keeping — nothing; the page must be created (admin) before it can be designed.

### 7.5 Verdict
"The accessibility link goes to a 404 — that is a legal exposure in Israel, not a design question."

---

## 8. `blog-news` — `/blogs/news` (empty default blog)

**Heights:** desktop 900 px (one viewport) · mobile 1364 px. No h1 on the page; `<title>News – ElmsNest</title>` (English).

### 8.1 What renders
Desktop:
1. Header (invisible nav).
2. **`blog-slider`** (`blog_slider_h7yXkz`, configured to blog handle **"fashion"** — Kalles demo, does not exist): a full-width 245 px strip of **8 placeholder cards** (3 visible per view, `nav_style: outline` arrows hidden on mobile) using Shopify's onboarding SVGs — isometric cardboard boxes, spools of thread, a sewing machine (`hdt-placeholder-svg`, 8 of them) — each with a translucent dark-brown lower panel reading "**מאת : שם המחבר**", "**Tech , Design**" (links to `/admin/blogs`), "**כותרת הפוסט שלך**", "**November30**" (date format `%b %d` glued together). Card links have `href=""`.
3. **`main-blog`**: an empty `<hdt-reval-items … lg:hdt-grid-cols-2>` grid — the "news" blog has 0 articles, so the section renders 60 px + 60 px of padding around nothing (the 245 px cream gap under the slider).
4. Footer.
Mobile: one placeholder card (sewing machine, 1 per view) 60–600 px, cream void, footer from ≈ 610 px. **Mobile fold:** header, one sewing-machine card, void, top of footer.

The blog is linked from nowhere (0 `/blogs/` hrefs in header/footer/menus) — reachable only by URL.

### 8.2 Against the design system
- Template demo content on the live dev theme: sewing-machine illustrations, "Tech, Design", "Your post title", admin links — the single most unfinished-looking screen in the inventory.
- Cream ground, brown overlay panels, Assistant, English page title, glued date.
- No h1, no intro, no articles, no relation to lighting.

### 8.3 Honesty check
Placeholder author/title/tags are theme onboarding, not claims; nothing fabricated about the store — but "מאת : שם המחבר / Tech, Design" published on a customer-facing URL reads as fake content.

### 8.4 Worth keeping
- Nothing visual. Mechanics: `templates/blog.json` → `main-blog` (`article_des: 1`, 2 columns, `blogs_count: 6`, pagination links) and `sections/blog-slider.liquid` exist if the store ever writes articles; the `blog: "fashion"` setting must be changed or the section removed. Decision needed: either the blog gets real content (the guide/why-solar pages could live here) or the template should be a redirect/hidden.

### 8.5 Verdict
"Sewing machines and 'your post title' on my lighting store — delete it or fill it."

---

## 9. Family summary

### 9.1 Five facts a designer must know before briefing this family
1. **Data is thin and real.** 27 products / 4 collections; a search for "שביל" returns 13 products (`products_count: 16`, so no pagination case exists in practice); price ranges are the norm (10 of 13 hits are multi-variant: qty sets 2/4/6/8, lengths 5–22 m × 4 colours, 1/4/8/12 units × 2 colours); one genuine compare-at sale (199.90 → 149.90); the cart carries real variant lines ("אורך ומספר נורות: 5 מ׳ / 20 נורות", "צבע אור: צהוב חם"). No reviews, no ratings, no countdowns anywhere — the honesty rules are already met by absence.
2. **Every page of the family is Kalles default on the old cream scheme** (`scheme-1` body, Assistant, brown buttons, taupe title band), while header and footer are already `scheme-env2-night`. Consequence: the transparent night-scheme header is **invisible on all eight pages** (cream ink on cream) and every page ends in a hard cream→black cut. Porting `elmsnest-v2-base` to a page-agnostic core (HANDOFF §3 ⚠) is the precondition for the whole family.
3. **The empty states say the theme's words, not ours.** Cart: "העגלה שלך ריקה / לפני שתמשיך לקופה… בדף "חנות" שלנו / חזור לחנות" → `/collections`. Search: "לא נמצאו מוצרים התואמים את הבחירה שלך." in a warning box with no input to retry. 404: "עמוד לא נמצא / 404 / חזרה ל- דף הבית" letter-spaced. Blog: Shopify onboarding placeholders ("כותרת הפוסט שלך", sewing machines) because `blog-slider` points at the non-existent demo blog "fashion" and "news" has 0 articles. Accessibility statement: does not exist (404, pixel-identical). Search band on all three search pages is an **empty 100 px grey strip**: the h1 with the query and count is `sr-only`.
4. **The only custom section in the family is `elmsnest-cart-guidance`** (static, 3 boxes, `--en-*` PDP tokens with radius): its copy is honest (8–17 business days = 1–3 + 7–14; costs at checkout; check variant; contact before ordering) but it appears on the empty cart too, and none of the other consumer terms (free pickup / 29.90 ₪ door, warehouses outside Israel, 14-day cancellation ≤5 % or 100 ₪, WhatsApp photo — `whatsapp_number` is empty so every WhatsApp CTA falls back to `/pages/contact-us`) is on the cart; the footer's "תנאי משלוח וביטול" goes to `/#env2-terms`.
5. **Search cards reuse the collection card (`card-product1`)** with the image ledger unenforced: 8 of 13 index-0 images carry baked-in Hebrew slogans and numeric claims ("50,000 שעות עבודה", "+30% יעילות טעינה", "עד 14 שעות תאורה", "−20° עד 60°C") and one carries a third-party "LUMIÈRE OUTDOOR LIGHTING" logo; the sale badge flips to "%25-"; colour swatch dots appear on one card only; mobile titles truncate. Whatever the collection family decides for cards must be inherited here (WINNING-SPEC §3.6 image indexes).

### 9.2 Three hardest technical constraints visible
1. **Kalles JS-driven components with server-rendered fallbacks.** Cart page = `<hdt-main-cart>` / `<cart-items-component>` with `updates[]`, `/cart/change` links and `name="checkout"`; search = `<hdt-facet-filters-form>` (GET `/search` with `filter.v.*`, `sort_by`, `type=product`), `<hdt-popover-sorting>`, `<hdt-view-layout-switch>`, `<hdt-drawer class="hdt-filter">`, per-card `<hdt-variant-option>` + `<hdt-swatch-card>` + quick-add modal (`aria-controls="hdt-quick-add-modal"`) and direct `/cart/add` forms. A redesign must either keep these element names/attributes (so `global.min.js` keeps working) or replace the whole section and its JS; the 2 console errors in every render show the module graph is fragile in a mirror.
2. **The cart drawer (`sections--…__cart-drawer`, `<hdt-cart-drawer>`) is injected by JS and is not in the static HTML** — it is styled by `scheme-e0b7` (light cream) in `system-group.json` and will open on every add-to-cart on every page; it cannot be judged, designed or QA'd from mirrors; needs an interactive session over `http.server`, and its scheme must be switched alongside the page ground or it will pop cream over the night pages.
3. **Header transparency and ground coupling.** `header_transparent: true` + `scheme-env2-night` + `background_opacity_transparent: 0` assume a dark first section (the homepage hero has `section-allow-transparent`); on these templates the first section is a cream band/strip, so the nav disappears. Fixing it means either a night ground on every template (page-agnostic v2 base with a per-template ground, HANDOFF §3) or per-template header colours — and the `top-list-collections` / `main-heading` bands (`scheme-77e4…`, `--bg-overlay:.54`) are the sections that would have to carry `section-allow-transparent hdt-section` or be removed from `templates/search.json` and `cart.json`. Also unsettled: `blog.json`'s `blog: "fashion"` and the missing `accessibility-statement` page are admin/data fixes no Liquid can paper over.
