# AUDIT — collection family (dev theme 154726400174, mirrored 2026-09-02)

Pages: coll-all, coll-all-sorted, coll-wall, coll-path, coll-spot, coll-decor, coll-list, coll-sale.
Source of truth for this audit: the `http-*.png` renders (theme JS running) in `brief/inventory/<key>/`, the mirrored `index.html`, `INVENTORY-FACTS.md`, and the theme files under `brief/inventory/theme-src/` (no THEME-SRC.md exists; section names below are the Liquid file names). Heights are CSS px (renders are 2×).

## 0. Shared anatomy (identical on all six collection renders; deltas per page below)

| Slot | Source | What actually renders |
|---|---|---|
| Header | `sections/header-group.json` → `header-inline-blocks`, `header_colors`/`header_transparent_colors` = `scheme-env2-night`, `header_transparent: true`, `background_opacity_transparent: 0` | A 70 px strip that shows the **cream body (#f7f0e6) through a transparent header**, gold house-heart logo centred, and the menu links / search / account icons set in ink `#f4eee3` — **cream on cream, unreadable on desktop and mobile**. Only the logo and a gold "0" cart bubble (top-left) are visible. The DOM has `hdt-header-tranparent-true` + `color-scheme="scheme-env2-night"`; the sticky-on-scroll-up variant (`background_opacity_sticky: 0.9`) is dark, so the header flips from invisible to night-black the moment the user scrolls up. |
| Top strip | `top-list-collections` (id `collections_list_simple_4yRUED`, `scheme-1`, menu: footer, sort alphabetical) | 45 px light-cream bar, four brown Assistant links: "גרילנדות ותאורה דקורטיבית · ספוטים, פרוז׳קטורים ותאורה ניידת · תאורת קיר · תאורת שביל, עמוד וגינה". No active state for the current collection. Mobile: a horizontal scroller with chevrons, second item clipped mid-word ("ספוטים, פרוז׳קטורינ"). Not present on coll-list / coll-sale. |
| Banner | `sections/main-heading.liquid`, scheme `scheme-77e4ef58…` (cream `#f7f0e6` on brown `#2b2118`), image `bg_collections.jpg` under a 54 % brown overlay | ≈180 px desktop / ≈195 px mobile band that reads as flat grey-taupe (#8a8078). Centred title (Assistant ~32 px, a `div.hdt-heading-liquid`, not a heading) + breadcrumb "בית › …". The only `<h1>` is `sr-only` and prints `page_title`, so on the four collections the h1 is the SEO title, e.g. "תאורת קיר סולארית לגינה ולכניסה \| ElmsNest". `hdt-reveal="slide-in"` on title and breadcrumb. |
| Description | `main-collection.liquid`, `show_description: true`, `description_position: before`, `readmore-less` | Two paragraphs, Assistant 17 px brown, right-aligned across the full 1240 px container, ~80 px air above and below. `hdt-reveal="slide-in"`. Only on the four real collections. |
| Toolbar | `main-collection.liquid` (`enable_sorting`, `enable_filtering`, `enable_num_cols_selector` all true; filter block `disabled: true`) | Right: "סנן" + funnel icon → `hdt-drawer.hdt-filter` dialog (scheme-1, cream) containing Shopify's two default facets: checkboxes "במלאי (6)" / "לא במלאי (0)" (the latter disabled) and an **English "Price"** range slider. Centre: six grid-density toggles (6/5/4/3/2 columns + list; "4" active). Left: bordered select showing the current sort ("פופולריות" on the 4 collections, "שם, א-ת" on /all). 10 sort options incl. "הנמכרים ביותר" and "פופולריות" (= manual). Mobile: "סנן", 3 toggles (2-col active / 1-col / list), select that only ever says "מיין". |
| Grid + card | `snippets/card-product1.liquid` (+ `card-price`, `badges`, `scrolling_badge`, `card-product-media`); `col_dk 4 / col_tb 3 / col_mb 2`, `pr_border: none`, `image_ratio: custom-pr`, `pr_card_radius 0` | 4 columns desktop / 2 mobile, no card surface (image sits straight on cream), portrait image ≈5:7, always `product.images[0]`. Below: title (Assistant 16 px, `#2b2118`, `<h3><a class="hdt-line-clamp">`, 2 lines max, mobile ellipsis), price line "89.90 ₪ - 179.90 ₪" (hyphen range; `card-price`), colour-swatch circles when the product has a colour option (even a single value). A dark-brown 48 px square with a cart icon at the image's bottom-left = quick-add (`show_quick_add: true`): the 8 single-variant products carry a `/cart/add` form; all others open the Kalles quick-add popup (`hdt-tmp-quick` template) with a variant picker. Hover: image opacity effect (`hdt-pr-img__effect-opacity`). No vendor, no rating, no "new" badge (`use_new_badge: false`); sale badge is a `#91212a` circle with "-N%" (`badge_shape: circle`, `label_onsale_style: percentage`). |
| Pagination | `pagination_type: links`, 12 per page (`products_count: 12`), `enable_progressbar: true` (no progress text rendered) | 1 px `#d2cbc1` hairline, then "1 2 3 הבא" in brown 16 px. Only /all reaches it. |
| Footer | `sections/footer-group.json`, `scheme-env2-night` | Night block `#020306`, gold logo, "שאלות על מוצר או על התאמה למקום? כתבו לנו: info@elmsnest.com", columns "קולקציות / מידע / יצירת קשר" (underlined links: "מדריך לבחירת תאורה לגינה, למה תאורה סולארית, מי אנחנו, משלוחים ואספקה, זמני טיפול, שאלות נפוצות, עמוד יצירת קשר, לשליחת תמונה של המקום"), bottom line "ElmsNest © 2026 · תנאי משלוח וביטול". The **only** element already in the design system; the cream→night boundary is a hard horizontal edge on every page. |
| Fonts / tokens | `settings_data.json`: `font_family_shopify_1/2/3 = assistant_n4`, `font_base = --f_family_1` | Everything is Assistant 400. Frank Ruhl Libre / Heebo are not loaded (`FRL font loaded: False`, `env2 base loaded: False` on all eight pages). Theme radii are 0 everywhere (matches the system). |
| System sections | `cart-drawer.liquid` (56 KB, scheme-1 cream), `back_top.liquid` | Present in the DOM on all eight pages; cart drawer is what quick-add opens. |

Consumer terms: none of the eight pages mentions pickup / 29.90 door delivery / 8–17 business days / 14-day cancellation / "send a photo on WhatsApp". The only routes are footer links ("משלוחים ואספקה", "תנאי משלוח וביטול", "לשליחת תמונה של המקום" → `/pages/contact-us` because `settings.whatsapp_number` is empty).

---

## coll-all — `/collections/all` (27 products, page 1 of 3)

**1. What renders.** Desktop 1440 × **2531**: header (invisible menu) → top strip → banner "קטלוג" / "בית › קטלוג" → toolbar (select reads "שם, א-ת", grid "4" active) → 3 rows × 4 cards (12 products, alphabetical: גרילנדת כדורי LED …, גרילנדת כדורי קריסטל …, גרילנדת נורות אדיסון …, מנורות סולאריות למדרגות …, מנורת גינה דו־ראשית …, מנורת גינה סולארית עוצמתית …, מנורת עמוד LED …, four "מנורת קיר LED …", מנורת קיר נטענת מגנטית) → hairline → "1 2 3 הבא" → footer. No description (collection "all" has none).
Mobile 390 × **3483**: header → strip scroller → banner → toolbar ("סנן", 3 toggles, "מיין") → 6 rows × 2 cards → hairline → pagination → footer stacked (logo, note, three link columns, © line).
First screen: desktop fold (900 px) contains row 1 with four titles and prices (e.g. "גרילנדת כדורי LED דקורטיבית – USB או סוללות · 89.90 ₪ - 179.90 ₪"); the quick-add squares are not in the fold capture (they appear after JS init). Mobile fold (844 px) contains two product images, both titles and both prices (titles at ≈605 px, prices ≈650 px) — **product + price inside the fold, no explicit CTA**.
Readable card text: "מנורות סולאריות למדרגות ולדק באור חם – 1/4/8/12 יחידות · 69.90 ₪ - 349.90 ₪" (+ 2 swatches), "גרילנדת נורות אדיסון סולארית – 5 או 8 מטר · 139.90 ₪ - 179.90 ₪", "מנורת קיר LED מודרנית 6W עם תאורת Up & Down · 109.90 ₪ - 193.90 ₪", "מנורת קיר LED עמידה למים IP65 – 6W/12W · 219.90 ₪ - 252.90 ₪". 8 of 12 cards show a price range.
Images: 7 of 12 featured images carry baked-in Hebrew marketing text, clipped by the 5:7 crop ("תאורה סולארי… אלגנטית למע…", "…יד וחזק / …ורה ניתנת להחלפה", "נגיעת אור לכל פינה", "חיבור מגנטי חז… / התקנה ללא חי…", "תאורה שמעצבת אווירה", "יצוב מודרני, חוויית תאורה מושלמת", "אווי… יוקרת… בשבילי…"); the bollard image also carries a third-party mark "LUMIÈRE OUTDOOR LIGHTING".

**2. Against the design system.** (a) Ground is cream `#f7f0e6` with brown ink `#2b2118` — exactly the rejected scheme (`scheme-1`); banner is a photo drowned to flat taupe. (b) Assistant everywhere; the display title is a 32 px div, not editorial type. (c) Header unreadable (see §0) — the page has no navigation until the user scrolls up. (d) Off-the-shelf UI kit: six grid-density toggles, bordered select with chevron, funnel icon, filter drawer with an untranslated "Price" facet and a "לא במלאי (0)" checkbox that can never do anything. (e) Cards: dark-brown square quick-add button pasted on the photo; swatch circles under prices; SEO-length titles wrap to two lines and Latin tokens flip ("Up & Down" isolated on its own line; "1/4/8/12"; mobile ellipsis "…1/4/8/12"; "10W IP65 – 180°" re-orders on mobile as "מתכווננת °180 – 10W IP65"). (f) Motion is the wrong kind: `hdt-reveal="slide-in"` fades/slides the title, breadcrumb and cards in on scroll; nothing "lights". (g) No hairline discipline — sections are separated by empty cream gaps, then a single hairline before pagination, then a hard cut to the night footer. (h) Every screen is the same composition (4 equal columns); nothing a lighting store specifically would do.

**3. Honesty check.** No ratings, review counts, customer quotes, "trusted by", countdowns or guarantees in the DOM (`--color-pr-rating` is an unused CSS var). Two soft violations: the sort menu offers "הנמכרים ביותר" (best-selling) and the theme labels manual order "פופולריות" — both imply popularity data the brand has ruled out. The images themselves make claims the page cannot back ("50,000 שעות עבודה", "+30% יעילות טעינה", "עד 14 שעות תאורה", "עמיד למים IP65", "חיבור מגנטי חזק", "טווח עבודה: -20° עד 60°C"), and one shows another brand's logo.

**4. Worth keeping.** `collection` object + `paginate` with `products_count` (12); `sort_by` URL parameter and `collection.sort_options` (`?sort_by=price-ascending` works server-side); `snippets/card-price.liquid` (handles ranges, compare-at, unit price); the `/cart/add` form → `cart-drawer` mechanic for single-variant products; `collection.filters` (availability + price) as the only facet data that exists; breadcrumb block `_heading_brc`; the sr-only h1 pattern, if pointed at `collection.title`.

**5. Verdict.** "This is every Kalles store's catalogue page, in the cream I already rejected, under a header I can't read."

---

## coll-all-sorted — `/collections/all?sort_by=price-ascending`

**1. What renders.** Same skeleton as coll-all. Desktop 1440 × **2595**, mobile 390 × **3547** (taller because more two-line titles). Desktop select reads "מחיר, נמוך לגבוה"; **the mobile select still reads "מיין"** — the mobile control never reflects the active sort. Order on page 1: "מנורות סולאריות למדרגות … 69.90 ₪ - 349.90 ₪", "גרילנדת כדורי LED … 89.90 ₪ - 179.90 ₪", "ענפי ליבנה מוארים – 20 נורות LED לעיצוב הבית · 89.90 ₪", "שרשרת חבל סולארית לחוץ – 50 עד 300 נורות LED · 89.90 ₪ - 159.90 ₪", "גרילנדת כדורי קריסטל …", "מנורת קיר LED מודרנית – גרסאות לפנים או לחוץ · 99.90 ₪ - 121.90 ₪", "תאורת אבטחה סולארית LED 100 עם חיישן תנועה · 99.90 ₪" (+ 1 white swatch), "תאורת גחליליות סולארית לגינה – 10 נורות מתנדנדות · 99.90 ₪", "מנורת קיר LED מודרנית 6W עם תאורת Up & Down · 109.90 ₪ - 193.90 ₪", "רשת תאורת LED דקורטיבית לחוץ ולגינה – 1.5 עד 12 מטר · 109.90 ₪ - 469.90 ₪", "מנורת קיר סולארית LED עם חיישן תנועה – עמידה למים IP65 · 129.90 ₪ - 159.90 ₪" (+ black/white swatches), "מנורת עמוד LED מודרנית לגינה ולחצר – 5W IP65 · 129.90 ₪". Fold: same as coll-all (desktop row 1 with prices; mobile two products with prices).

**2. Against the design system.** Everything in coll-all, plus: price sort is by the variant minimum, so "109.90 ₪ - 469.90 ₪" (net lights, 30 variants) sits between 99.90 and 129.90 — with 8 of 12 cards showing ranges the "cheapest first" promise is visibly untrue; the mobile "מיין" label gives no feedback that a sort is applied; the URL is the only state.

**3. Honesty check.** As coll-all. Nothing added by sorting.

**4. Worth keeping.** Server-side `sort_by` (no JS needed, shareable URL); `collection.sort_options` list; the min-of-range ordering is Shopify behaviour and must be designed around (show "החל מ־" or the single per-unit price).

**5. Verdict.** "Sorting works, the page still looks like a spreadsheet of stickers."

---

## coll-wall — `/collections/solar-wall-lights` (6 products, 34 variants, 99.90–252.90 ₪)

**1. What renders.** Desktop 1440 × **2022**: header → strip → banner "תאורת קיר" / "בית › תאורת קיר" → description: "תאורת קיר סולארית לחוץ הבית — פתרונות תאורה נוחים לגינה, לחצר, לכניסה, למרפסת ולקירות חוץ. מתאימה ליצירת אור שימושי ואווירה נעימה בלי חיבור קבוע לחשמל ובלי התקנה מסובכת." / "בחרו תאורה לפי עוצמת האור, אזור ההתקנה והסגנון שמתאים לבית שלכם." → toolbar ("פופולריות") → row of 4 + row of 2 (right-aligned; left half of the second row empty) → footer. No pagination.
Cards: "מנורת קיר סולארית LED עם חיישן תנועה – עמידה למים IP65 · 129.90 ₪ - 159.90 ₪" (black/white swatches), "מנורת קיר LED חיצונית דו־כיוונית IP65 · 159.90 ₪ - 162.90 ₪", "מנורת קיר LED מודרנית 6W עם תאורת Up & Down · 109.90 ₪ - 193.90 ₪", "מנורת קיר LED מודרנית – גרסאות לפנים או לחוץ · 99.90 ₪ - 121.90 ₪", "מנורת קיר LED עמידה למים IP65 – 6W/12W · 219.90 ₪ - 252.90 ₪", "מנורת קיר נטענת מגנטית עם שליטה במגע · 159.90 ₪". 3 of 6 featured images have baked text; the two cleanest night photos (up/down cube on a wall, bidirectional cylinder at dusk) are the only ones that show light on a wall.
Mobile 390 × **2524**: header → strip → banner → description (8 lines) → toolbar → 3 rows × 2 → footer.
First screen: desktop fold = header, strip, banner, description, toolbar and the top ≈340 px of the first-row images — **no title, no price**. Mobile fold = banner + description + toolbar + the top of two images; first price at ≈1100 px. **Zero `/cart/add` forms** — every product is multi-variant, every quick-add opens the popup.

**2. Against the design system.** All of §0, plus: a 4 + 2 layout with an empty quarter-page; the description is a full-width text slab in body size (no kicker, no display line, no rule); the sr-only h1 is the SEO string "תאורת קיר סולארית לגינה ולכניסה | ElmsNest"; the copy promises "בחרו … לפי עוצמת האור, אזור ההתקנה והסגנון" but the only filters are stock and price; no wall, no night, no beam anywhere on a page about wall light; identical composition to the other three collections.

**3. Honesty check.** No fabricated claims in the DOM. Image-baked claims: "יצוב מודרני, חוויית תאורה מושלמת", "חיבור מגנטי חזק / התקנה ללא חירור", "תאורה שמעצבת אווירה". Sort options as coll-all.

**4. Worth keeping.** The two-paragraph description (honest, specific, already in `collection.description`); the wall products' clean alternate images (indexes 1–3, see WINNING-SPEC §3.6); `card-price` range logic; variant option data (W: 6W/12W, colour black/white, indoor/outdoor) as a future card-level chooser; the `main-heading` `_heading_brc` breadcrumb block.

**5. Verdict.** "A paragraph, a row of icons and six thumbnails — where is the wall at night?"

---

## coll-path — `/collections/תאורת-שביל-סולארית` (8 products, 22 variants, 69.90–999.90 ₪)

**1. What renders.** Desktop 1440 × **2036**: header → strip → banner "תאורת שביל, עמוד וגינה" / breadcrumb repeating it → description: "תאורת שביל סולארית לגינה, לכניסה, לחצר ולמעברים חיצוניים. פתרון פשוט להדגשת הדרך, לשיפור הנראות בלילה וליצירת מראה מסודר ונעים סביב הבית." / "מתאים במיוחד לשבילים, ערוגות, מדרגות, כניסות ופינות מעבר בגינה." → toolbar ("פופולריות") → 2 rows × 4 → footer.
Cards: "מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65 · 169.90 ₪", "סט מנורות שביל סולאריות רטרו באור חם – 2/4/6 יחידות · 219.90 ₪ - 529.90 ₪", "סט תאורת שביל סולארית מודרנית בצורת 7 – 4/8 יחידות · 549.90 ₪ - 999.90 ₪" (the store's most expensive product), "תאורה סולארית עמידה למים לדק ולמדרגות · 149.90 ₪ ~~199.90 ₪~~" with a **dark-red circle badge "-25%"** top-left of the image, "מנורות סולאריות למדרגות ולדק באור חם – 1/4/8/12 יחידות · 69.90 ₪ - 349.90 ₪" (2 swatches), "מנורת גינה סולארית עוצמתית LED – תאורה אוטומטית לחוץ · 179.90 ₪" (a tiny white pill with clipped text "תאור…" at the image's bottom-left — a Kalles custom/scrolling badge rendering at the wrong size), "סט מנורות שביל סולאריות מתנדנדות ברוח – 2/6 יחידות IP65 · 189.90 ₪ - 329.90 ₪", "מנורת עמוד LED מודרנית לגינה ולחצר – 5W IP65 · 129.90 ₪". 6 of 8 featured images carry baked text ("האירו את המד… בשתי ד…", "וסיפה אווירה לכל שביל וגינה · זמין בסט של 4 או 8 יחידות", "עמיד למים 65", "פאנל סולארי מוגדל · עד 14 שעות תאורה · +30% יעילות טעינה · 50,000 שעות עבודה", "תאורה סולארית אלגנטית…", plus the LUMIÈRE bollard).
Mobile 390 × **2840**: header → strip → banner (two-line title) → description (7 lines) → toolbar → 4 rows × 2 → footer.
First screen: desktop fold ends at the toolbar + top of images; mobile fold ends at the toolbar + top of two images. **No price in the fold on either device.**

**2. Against the design system.** All of §0 and coll-wall's points, plus: a red discount circle ("-25%", `badge_sale #91212a`) — a default e-commerce sticker on a brand that forbids urgency devices; the clipped badge pill; two cards whose images are essentially posters (stairs collage, "פאנל סולארי מוגדל" spec sheet); the 999.90 ₪ set sits in the same 270 px card as the 69.90 ₪ step light with nothing to explain the gap (units per set are only in the title).

**3. Honesty check.** "-25%" + struck "199.90 ₪": a compare-at price on `waterproof-solar-deck-step-lights` — allowed only if 199.90 was genuinely charged before (Israeli reference-price rules); the design must decide whether sale badges exist at all. Image-baked claims: "50,000 שעות עבודה", "+30% יעילות טעינה", "עד 14 שעות תאורה", "עמיד למים IP65", "זמין בסט של 4 או 8 יחידות". Sort options as coll-all.

**4. Worth keeping.** The description copy; the set-size variant structure (2/4/6, 4/8, 1/4/8/12 units) as data for a "per unit" price device (`card-price` already supports unit price, `show_volume_note: true`); `product.compare_at_price` handling in `card-price` (if kept honest); clean alternates for the stainless-steel and bollard products.

**5. Verdict.** "Same page, now with a red discount sticker — the one thing I said this brand never does."

---

## coll-spot — `/collections/ספוטים-ופרוז-קטורים-סולאריים` (6 products, 11 variants, 99.90–499.90 ₪)

**1. What renders.** Desktop 1440 × **2054**: header → strip → banner "ספוטים, פרוז׳קטורים ותאורה ניידת" with the breadcrumb repeating the full title 30 px below it → description: "ספוטים ופרוז׳קטורים סולאריים לחוץ הבית — פתרונות תאורה חזקים יותר לאזורים שצריכים נראות טובה, כמו כניסה לבית, חניה, חצר, שביל או קיר חיצוני." / "בחרו לפי אזור ההתקנה, עוצמת התאורה, זווית ההארה והצורך שלכם בין תאורת אווירה לתאורה שימושית." → toolbar ("פופולריות") → row of 4 + row of 2 (right-aligned) → footer.
Cards: "פנס סולארי לגינה 9 LED | עמיד למים ומתכוונן · 169.90 ₪" (a literal "|" in the title), "ספוט סולארי עוצמתי לגינה – 52 LED עם 3 מצבי תאורה · 219.90 ₪ - 429.90 ₪", "תאורת אבטחה סולארית LED 100 עם חיישן תנועה · 99.90 ₪" (one lone white swatch), "פרוז׳קטור סולארי IP67 עם שלט וטיימר – 72/128/200 LED · 199.90 ₪ - 499.90 ₪", "מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65 · 189.90 ₪", "פנס קמפינג טלסקופי נטען 360° עם תאורת צד · 189.90 ₪" (one lone swatch). 5 of 6 featured images are text posters ("עמידות לכל מזג אוויר · IP65 עמיד למים, לחום ולקור · טווח עבודה: -20° עד 60°C", "תאורה סולארית לגינה", "שליטה חכמה ונוחה · זמין בסט של 4 או 8", "נטען ביום, מאיר בלילה", "אור ח… בכל מק… מתאימה לקמפינג, חירום וטיולים"); only the dual-head product photo is clean.
Mobile 390 × **2532**: banner title wraps to 2 lines, description 6 lines, toolbar, 3 rows × 2, footer.
First screen: no title/price in either fold (desktop: toolbar + image tops; mobile: description + toolbar + image tops).

**2. Against the design system.** All of §0/coll-wall, plus: title repeated twice within 40 px (banner + breadcrumb); a camping lantern (indoor/portable) inside a "spots and floodlights" collection — the collection name was stretched to "…ותאורה ניידת" to cover it; single-value swatch circles under two cards read as UI debris; nothing shows what a floodlight does to a driveway — the poster images shout specs instead.

**3. Honesty check.** Image-baked claims: "טווח עבודה: -20° עד 60°C", "עמידות לכל מזג אוויר", "IP67", "זמין בסט של 4 או 8". Sort options as coll-all. Nothing fabricated in the DOM.

**4. Worth keeping.** The description copy (the "אווירה vs שימושי" distinction is a real product-level idea); variant data "3 מצבי תאורה", "72/128/200 LED" for a lumen/coverage device; the clean dual-head photo; `card-price`.

**5. Verdict.** "Six products, five of them posters, and a page that never shows a beam."

---

## coll-decor — `/collections/גרילנדות-ותאורה-דקורטיבית` (7 products, **105 variants**, 89.90–469.90 ₪)

**1. What renders.** Desktop 1440 × **2011**: header → strip → banner "גרילנדות ותאורה דקורטיבית" / breadcrumb → description: "גרילנדות ותאורה דקורטיבית לחצר, למרפסת, לפרגולה ולפינות ישיבה. תאורה שמוסיפה אווירה חמימה ונעימה לערבים בחוץ — בלי להפוך את ההתקנה לפרויקט." / "מתאים לאירוח, לפינת קפה, לשבילי גינה וליצירת מראה מעוצב סביב הבית." → toolbar ("פופולריות") → row of 4 + row of 3 (right-aligned) → footer.
Cards: "גרילנדת כדורי קריסטל סולארית – 20 עד 200 נורות · 89.90 ₪ - 179.90 ₪" (24 variants), "תאורת גחליליות סולארית לגינה – 10 נורות מתנדנדות · 99.90 ₪", "רשת תאורת LED דקורטיבית לחוץ ולגינה – 1.5 עד 12 מטר · 109.90 ₪ - 469.90 ₪" (30 variants), "גרילנדת כדורי LED דקורטיבית – USB או סוללות · 89.90 ₪ - 179.90 ₪" (30 variants), "ענפי ליבנה מוארים – 20 נורות LED לעיצוב הבית · 89.90 ₪", "שרשרת חבל סולארית לחוץ – 50 עד 300 נורות LED · 89.90 ₪ - 159.90 ₪" (16 variants), "גרילנדת נורות אדיסון סולארית – 5 או 8 מטר · 139.90 ₪ - 179.90 ₪". 5 of 7 featured images carry baked text ("נגיעת אור לכל פינה", "…ת תאורת LED לאווירה קסו…", "מראה קסום בגינה" collage, "תאורת מיתר סולא…", "…יד וחזק"); crystal balls and birch branches are clean and are the best night photos in the whole catalogue. Only 1 `/cart/add` form (firefly); four products hide 16–30 variants behind one range price and one cart icon.
Mobile 390 × **2815**: description 6 lines, toolbar, rows 2/2/2/1 (last card alone at the right), footer.
First screen: no title/price in either fold.

**2. Against the design system.** All of §0/coll-wall, plus: the most atmospheric products in the store rendered as beige stamps; an orphan 7th card; 30-variant products (length × power source) reduced to "89.90 ₪ - 179.90 ₪" with no hint of what the range means; a "USB or batteries" product (indoor-ish, not solar) sits next to solar garlands with no distinction; title "ענפי ליבנה… לעיצוב הבית" is an indoor product in an outdoor store.

**3. Honesty check.** Nothing fabricated in the DOM; image-baked: "מראה קסום בגינה", "להאיר כל רגע". Sort options as coll-all.

**4. Worth keeping.** Description copy; the crystal-ball and birch photos; the variant axes (length 1.5–12 m, 20–200 bulbs, 50–300 LEDs, USB/solar) as the raw material for a "how much light for how many metres" device; `card-price`.

**5. Verdict.** "Garlands are the most atmospheric thing I sell and this page shows them as stamps on beige."

---

## coll-list — `/collections` (list-collections template)

**1. What renders.** `templates/list-collections.json` → `main-heading` (image `bg-heading.jpg`, 56 % overlay, `text_size 4xl`) + `main-list-collections` (`display_type all`, `col_dk 3 / col_mb 2`, `image_ratio square`, `content_position end-center`, `show_count false`).
Desktop 1440 × **1591**: header (invisible menu, no top strip) → taupe banner "קטלוגים" with a **broken breadcrumb "בית ›"** (nothing after the chevron) → three square photo cards (wall / spot / decor) each with a cream label box floating at the bottom centre: "תאורת קיר", "ספוטים, פרוז׳קטורים ותאורה ניידת", "גרילנדות ותאורה דקורטיבית" → the fourth card ("תאורת שביל, עמוד וגינה") alone, centred, on a second row → footer. Roughly 1,100 of 1,591 px are chrome (header, banner, footer).
Mobile 390 × **1517**: banner → 2 × 2 cards with labels **truncated by ellipsis**: "גרילנדות ותאורה …", "ספוטים, פרוז׳קטו…", "תאורת שביל, עמו…", "תאורת קיר" → footer.
Images: the four `collection.image`s (decor/spot/path 960 × 1200 portrait, wall 1456 × 816 landscape — the one HANDOFF says needs a focal point) forced to squares. No product counts, no descriptions, no links to /collections/all.
First screen: desktop fold shows banner + three cards with labels; mobile fold shows banner + the top halves of two cards, no label. No product or price anywhere on the page (foldHasBuy: not applicable).

**2. Against the design system.** Cream/brown scheme-1; boxes (cream label plates on photos, the very "card" the system bans); 3 + 1 orphan grid; ellipsised collection names on mobile; broken breadcrumb; Assistant; different banner photo than the collection pages but the same taupe; `hdt-reveal` on the title; no story, no order (alphabetical), no "which one is for my place" — the homepage's `env2_places` section already does this job better, which is why HANDOFF proposes pointing the menu's קולקציות at `/#env2-places`.

**3. Honesty check.** Nothing to flag.

**4. Worth keeping.** The four collection photos (the only images in the family with no baked text — real night, real lamps); `collections` loop in `main-list-collections.liquid`; the `_heading_liquid` block accepts Liquid (`{{ page_title }}`) so the banner can be replaced without a new section.

**5. Verdict.** "Four photos with labels on them — not a page, a menu."

---

## coll-sale — `/collections/sale` (renders the 404 template)

**1. What renders.** `templates/404.json` → `main-404.liquid` (`scheme-1`, `link: /`, `min-height: 60vh`). Desktop 1440 × **1110**: header (invisible menu, no strip) → a cream void with, centred: "עמוד לא נמצא" (Assistant bold ≈40 px, **letter-spacing 8 px**), "404" (bold 16 px), "חזרה ל- דף הבית" (link with bottom border) → footer. Mobile 390 × **1445**: the same, void ≈1,100 px tall, then footer. `<title>` "404 לא נמצא – ElmsNest", h1 "עמוד לא נמצא". No search box, no collection links, no products, no WhatsApp/contact; exits are "דף הבית", the (invisible) header and the footer. Identical to `p404`. First screen: nothing to buy.

**2. Against the design system.** Letter-spaced Hebrew (`.error-404 h1 {letter-spacing:8px}` in `main-404.liquid`) — a typographic error in Hebrew; a "404" numeral in the same brown sans; cream void; a hyphenated "חזרה ל- דף הבית"; `text-transform: uppercase` rule on the h3; no hairline, no ink hierarchy, no way back into the catalogue; a collection URL that dead-ends because the "sale" collection is not published to the Online Store channel.

**3. Honesty check.** Nothing on the page. Structural note: if a "sale" collection is ever published, the theme will render "-N%" circles (`badge_sale`, `label_onsale_style: percentage`) on every discounted card — the family brief must decide whether "sale" exists as a concept at all (the brand bans countdowns/urgency; a permanent sale collection is the same signal).

**4. Worth keeping.** Nothing visual. `main-404.liquid` is 40 lines and can be replaced wholesale; keep the `link` setting and the `templates.404.*` locale keys; the `sale` handle should either be unpublished from every menu/footer or the 404 must route to `/collections/all`.

**5. Verdict.** "You sent me to an empty page in the wrong font, spaced out like a Latin logo."

---

## Family summary

### Five facts a designer must know
1. **Catalogue shape.** 27 products / 4 collections: path 8 (22 variants, 69.90–999.90 ₪), wall 6 (34 variants, 99.90–252.90), spot 6 (11 variants, 99.90–499.90), decor 7 (105 variants, 89.90–469.90). 172 variants in total; only 8 products are single-variant; four products carry 16–30 variants (net 30, globe 30, crystal 24, rope 16). 19 of 27 cards show a hyphenated price range. `/collections/all` paginates 12 per page → 3 pages (12/12/3); the four real collections never paginate (max 8) and never show an empty state.
2. **Images.** Every product has exactly 4 images, all AI-generated 1254 × 1254 PNG; index 0 is a marketing creative with baked-in Hebrew text on roughly two-thirds of products (coll-all p1 7/12, path 6/8, spot 5/6, wall 3/6, decor 5/7), one shows a third-party mark ("LUMIÈRE OUTDOOR LIGHTING"); indexes 1–3 are cleaner. The collection cards use `images[0]` blindly. `brief/WINNING-SPEC.md` §3.6 already has a per-product usable-index ledger and a never-use list — a card system must pick a non-zero index per product (ledger in Liquid or a metafield). The four `collection.image`s are clean night photos (wall one is landscape 1456 × 816).
3. **Data that exists (and doesn't).** `collection.title`, four honest two-paragraph `collection.description`s (quoted above; "בחרו לפי עוצמת האור / אזור ההתקנה / זווית ההארה" is a chooser the pages do not provide), `collection.image`, server-side `sort_by`, `collection.filters` = availability + price only — **no facets for W, IP, zone, beam, solar/USB/rechargeable** (no tags/metafield filters configured), one compare-at price in the whole store (deck-step lights 199.90 → 149.90, rendering "-25%"), no reviews app, no ratings, no inventory counts. Consumer terms (pickup / 29.90 / 8–17 days / 14-day cancellation / WhatsApp photo) appear on none of the eight pages; `settings.whatsapp_number` is empty.
4. **The header is broken on every non-index page.** `header_transparent: true` + `scheme-env2-night` + `background_opacity_transparent: 0` means ink `#f4eee3` menu text over the cream body: the menu, search and hamburger are invisible until the user scrolls up (then the sticky header turns night-black). This is a site-level decision (dark ground under every template, or a per-template header scheme) and must be settled before any collection concept is judged from a render.
5. **What the first screen sells.** On `/collections/all` the fold shows products with prices on both devices; on the four real collections it shows banner + description + toolbar and only the tops of two images — no price, no CTA, on desktop or mobile. `/collections` shows four labelled photos; `/collections/sale` shows "עמוד לא נמצא". Page heights: all 2531/3483, sorted 2595/3547, wall 2022/2524, path 2036/2840, spot 2054/2532, decor 2011/2815, list 1591/1517, sale 1110/1445 (desktop/mobile, CSS px).

### Three hardest technical constraints
1. **`main-collection.liquid` is an 85 KB JS organism**: `hdt-drawer` filter dialog + `snippets/facets.liquid` form re-rendered by AJAX (`?section_id=`), `hdt-price-range`, grid-density selector writing CSS vars, `readmore-less`, `hdt-reveal` scroll animations, `hdt-sticky-header`, `toolbar-mobile.liquid`; everything is `.hdt-*`-classed and `color-scheme`-attributed, and the Sense RTL app flips physical properties. Re-skinning inside it is fragile; a new `elmsnest-collection` section must re-implement sort (plain `?sort_by=` links work server-side), the two facets, `paginate`, and the description/heading — and still keep `hdt-page-type-collection` body hooks that Kalles JS expects.
2. **Card → quick-add → cart drawer chain**: `card-product1` renders `badges`, `scrolling_badge`, `card-price`, `product-variant-options`; multi-variant products (19 of 27) open the Kalles quick-add popup (`hdt-tmp-quick` template) and then `cart-drawer.liquid` (56 KB, scheme-1 cream). A redesigned card must decide between "go to PDP" and an in-card variant/length picker; either way the cart drawer must be re-skinned to night or every add-to-cart drops the user back into the old cream.
3. **Global plumbing is index-only**: `elmsnest-v2-base` (tokens, FRL/Heebo, lamps, `window.env2`) is rendered by the homepage hero and its gradient targets `body.hdt-page-type-index`; theme fonts are `assistant_n4` in `settings_data.json` (edit minimally, never rewrite); header/footer groups are shared by all templates; Kalles cascades `hdt-badge__shape-circle`, `--color-*` vars and `color-scheme` attributes onto everything. The collection family therefore needs the split HANDOFF §3 describes (global core from `layout/theme.liquid` + a per-template ground) before any section can look right in a real render, and `brief/lint.py` currently globs only `elmsnest-v2-*` + `templates/index.json`.
