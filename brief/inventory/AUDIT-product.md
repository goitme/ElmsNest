# AUDIT — product family (pdp-single · pdp-multi · pdp-wall)

Inventory step, dev theme `154726400174`, mirrored 2026-09-02. Judged from the real renders
(`http-desktop.png` 1440×2, `http-mobile.png` 390×2, folds, sliced with `crops.py … http`) plus
`index.html` and `theme-src/`. Every claim below was checked in a screenshot unless marked (HTML).

All three products render the same template (`templates/product.elmsnest.json`, section ids
`template--21567616745646__*`): header → breadcrumb → main-product (Kalles) → elms_trust_strip →
elms_description → elms_showcase (night-gallery) → elms_installation → elms_comparison →
elmsnest_product_guidance → elms_faq (renders empty) → related-products (Kalles) → footer.
`elms_policy` (warranty-shipping) is in the theme-src copy of the template but is absent from the
render; the theme-src FAQ has 3 authored blocks yet the render is empty — the theme-src template
and the live dev template are not the same file. Reconcile before briefing.

Heights (CSS px, from `shot-http.log`): single 9532 / 11826 · multi 9599 / 11808 · wall 9672 / 11880.

---

## Shared facts (identical on all three pages)

**Header** — Kalles `header-inline-blocks`, `header_transparent: true`, opacity 0, colour scheme
`scheme-env2-night` in every state (normal / transparent / sticky). On the cream product page this
puts cream text on cream: the 7 menu labels, search and account icons are invisible on desktop; on
mobile the hamburger and search icons are invisible. Only the gold house logo
(`ElmsNest_Logo_Night.png`, 50 px) and the gold cart badge "0" read. Looks broken on every PDP.

**Footer** — already dark (`#020306`-black), gold logo, "שאלות על מוצר או על התאמה למקום? כתבו לנו:
info@elmsnest.com", 3 link columns (קולקציות ×4, מידע ×6, יצירת קשר: "עמוד יצירת קשר", "לשליחת
תמונה של המקום" → `/pages/contact-us`), bottom line "ElmsNest © 2026 · תנאי משלוח וביטול". Fine.

**Ground and type** — page `#f7f0e6` (`--en-surface-page: 247 240 230`), ink `#2b2118`, cards
`#fffdf7`, "night" `#12100e` (`--en-night: 18 16 14`, a brown-black, not sky-4), accent
`--en-amber #d9ad5f` (not the system gold `#e9b96e`). Font everywhere is the theme's Assistant
(FRL font loaded: False); h1/h2 are Assistant Bold. `border-radius: 0` in the elms CSS, but Kalles
components are round (sticky-bar thumb, price pill, sale badge circle, swatch circles, carousel nav).

**Sticky ATC** (Kalles `hdt-sticky-btn-atc`, mode "show when scrolled outside the form", scheme-1
cream with `backdrop-filter: blur(8px)`) — round product thumb, title, rounded pill
"צהוב חם - 169.90 ₪", dark button "הוסיפו להזמנה". Fixed; the full-page capture prints it across the
trust strip at y≈1800–1980 desktop, and at the bottom of the mobile fold where it clips the h1.

**Copy that is global, not product-specific (HTML + screenshots):** trust strip (4 items),
installation (4 steps), comparison (5 rows), guidance (3 cards + 3 accordions + link), showcase
heading/subheading/note. On every product the reader gets the same ~5,000 px of template.

**Consumer terms** — present and findable, five times per page: facts lines under the price
("המחיר כולל מס. משלוח לנקודת איסוף חינם; שליח עד הבית בתוספת 29.90 ₪." / "אספקה משוערת: 8–17 ימי
עסקים. למדיניות המשלוחים המלאה"), trust lines under the buttons ("ניתן לבטל עסקה עד 14 יום מקבלת
המוצר. למדיניות הביטולים" / "שאלות לפני ההזמנה? info@elmsnest.com"), the trust strip, the guidance
accordion ("הזמן הכולל המשוער הוא 8–17 ימי עסקים: 1–3 ימי טיפול ועוד 7–14 ימי משלוח. משלוח לנקודת
איסוף — חינם; שליח עד הבית — 29.90 ₪."), and the comparison row "ביטול עסקה … עד 14 יום".
Not on the page: "≤5% or 100₪", "warehouses outside Israel" (only behind the policy links), and any
WhatsApp (`whatsapp_number` empty; every "ask us" goes to `/pages/contact-us` or `mailto:`).

---

## 1. pdp-single — `stainless-steel-solar-path-light-ip65` (1 variant, 169.90)

### What renders — desktop 1440 (page 9532 px)
1. **Header** (0–100) — as above; nav invisible, gold logo, cart "0".
2. **Breadcrumb** (~140) — "בית › מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65", small Assistant on cream, `brc-nav-product` in its own colour scheme.
3. **Main product** (220–1050, Kalles `main-product`) — RTL two columns. Right: main image ≈670×670 (three bollards on a brick path, text-free) + a vertical strip of 6 thumbnails (100 px; thumb 3 is the "מידות והתקנה" spec slide with baked Hebrew). Left: h1 "מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65" (Assistant Bold ≈52 px, 2 lines), price "169.90 ₪" (≈32 px, brown), hairline, the two facts lines, hairline, **variant picker with one option** "צבע אור: צהוב חם" + a single filled dark button "צהוב חם", two identical full-width dark-brown rectangles "הוסיפו להזמנה" / "קנה את זה עכשיו", then the two trust lines with underlined links.
4. **Sticky ATC bar** — prints at 1800–1980 over the trust strip (capture artefact of a fixed bar).
5. **Trust strip** (`elms-pdp-trust-strip`, 1680–2200) — off-white `#fffdf7` band, 4 columns split by vertical hairlines, line icons (truck / refresh / drop / speech-bubble): "משלוח לנקודת איסוף חינם — שליח עד הבית — 29.90 ₪", "ביטול עסקה עד 14 יום — בהתאם לחוק הגנת הצרכן ולמדיניות הביטולים", "מיועד לשימוש בחוץ — דרגת העמידות המדויקת מופיעה במפרט הטכני", "אפשר לשאול לפני שמזמינים — נבדוק יחד אם המוצר מתאים למקום שלכם".
6. **Description** (`elms-pdp-description`, 2300–3500, cream) — renders `product.description`, which is merchant-authored `.elms-sales` HTML: tracked kicker "הדרך הביתה יכולה להרגיש אחרת כבר מהערב הראשון" with a short gold rule; h2 "משביל חשוך ולא גמור — לקו אור חם שמוביל את הדרך" (≈56 px, sans); lead paragraph; a "promise" block with a gold side-rule "אור חם. קו נקי. אפס כבלים."; h3 "האור הנכון הופך את הדרך לחלק מהעיצוב" + paragraph; a **2×2 grid of bordered off-white cards** ("מראה אלגנטי גם כשהיא כבויה", "עובדת בלי שתזכרו אותה", "מתקינים תוך דקות", "אור שמלווה את הערב"); h3 "יחידה אחת מאירה נקודה — שורה של יחידות יוצרת אפקט"; a **black panel** "פרטים שכדאי לדעת" with 7 gold-square bullets (גוף נירוסטה · גוון אור צהוב חם · טעינה ממוצעת כ־6 שעות · זמן עבודה כ־8–10 שעות · עמידות IP65 · נעיצה באדמה בעומק כ־5–10 ס״מ · לפני שימוש ראשון: מצב ON וטעינה של לפחות 3 שעות); hairline; text-only CTA "הפכו את השביל לפרט הראשון שמרשים בערב" (no button).
7. **Showcase** (`elms-pdp-night-gallery`, 3540–4900, `#12100e`) — gold kicker "מקרוב", white h2 "ככה זה נראה בפועל", sub "כל מה שחשוב לדעת לפני שמזמינים — ההתקנה, עוצמת האור והפעולה האוטומטית עם החשכה."; 2-column grid of 5 hairline-framed squares = product images 2–6 (`source: auto, skip_first 1, max 6`), last one centred; no captions; note "התמונות להמחשה. התוצאה בפועל משתנה לפי גובה ההתקנה, זווית הפאנל ומזג האוויר." Tile 1 (bollard by rocks) is a blank white square in the desktop capture — all tiles are `loading="lazy"`; it renders on mobile, so treat as a capture artefact and verify live.
8. **Installation** (`elms-pdp-installation`, 4950–6050, cream) — kicker "התקנה", h2 "ההתקנה ללא חוטים וללא חשמלאי", sub "רוב מוצרי התאורה הסולארית מותקנים בלי חיבור לחשמל ובלי הזמנת בעל מקצוע."; left: product image[3] (blank in the desktop capture, lazy; loads on mobile); right: 4 rows with large ochre numerals 1–4 and hairlines: "בוחרים מקום שמקבל שמש", "מקבעים את גוף התאורה", "מפעילים ומכוונים", "טעינה ראשונה"; footnote "דגמים המחוברים לרשת החשמל דורשים חיבור על ידי חשמלאי מוסמך…".
9. **Comparison** (`elms-pdp-comparison`, 6100–7100, `#12100e`) — kicker "השוואה", h2 "מה ההבדל מול מנורה סולארית זולה", sub "ההשוואה מתייחסת לאופן שבו אנחנו מוכרים — לא להבטחת ביצועים של מוצר מסוים."; a bordered 3-column table, ElmsNest column tinted with a gold top rule and a sun icon; square checkbox glyphs. Rows: "מפרט טכני מבוסס על נתוני היצרן" ✓ יש / – משתנה · "עמוד מוצר בעברית מלאה" ✓ יש / – לעיתים תרגום אוטומטי · "אפשר לשאול לפני ההזמנה" ✓ בוואטסאפ / – משתנה · "ביטול עסקה לפי חוק הגנת הצרכן" ✓ עד 14 יום / – תלוי במוכר · "נאמר לכם גם מתי המוצר לא מתאים" ✓ יש / ✕ לרוב לא. Note "אנחנו לא מתחייבים על ביצועי מוצרים של מוכרים אחרים…".
10. **Guidance** (`elmsnest-product-guidance`, 7150–8250, cream) — kicker "לפני שמזמינים", h2 "בודקים שהמוצר מתאים למקום שלכם", sub; three off-white cards with big gold numerals 01/02/03 and line icons: "מיקום ושימוש", "מקור חשמל", "מידות והתקנה" (the third sits alone, centred, on a second row); below, right: 3 `<details>` rows "זמן אספקה" (open), "מידע טכני", "צריכים עזרה לפני הקנייה?"; left: an off-white card with a wrench icon and the link "איך בוחרים תאורה לגינה?". The not-fit panel (`custom.not_fit_for`) does not render.
11. **FAQ** (`elms-pdp-faq`) — empty `<section>`; 0 px.
12. **Related products** (Kalles `related-products`, 8300–9100) — centred heading "מוצרים נוספים שכדאי להכיר"; 4-up carousel of white cards (8 loaded): images are mostly baked-text marketing slides ("תאורה סולארית אלגנטית למעקה", "האירו את המדרגות בשתי דרכים", "מוסיפה אווירה לכל שביל וגינה", "עמיד למים IP65"); red circle badge "-25%", strikethrough "199.90 ₪ → 149.90 ₪", ranges "219.90 ₪ - 529.90 ₪", two colour-swatch circles under the last card, "הוסף במהירות" quick-add, rounded nav.
13. **Footer** — dark, as above.

### What renders — mobile 390 (page 11826 px)
First screen (844 px): header 60 px (logo + cart; hamburger/search invisible) → 2-line breadcrumb → full-width square main image (160–520) → row of 4 thumbnails (one is the baked spec slide) → h1 at ≈44 px, three lines, the third line "IP65" cut by the sticky bar → **sticky bar**: pill "צהוב חם - 169.90 ₪" + full-width dark "הוסיפו להזמנה". So price + CTA are inside the fold only via the Kalles sticky bar; the native buy block starts at ≈880 px. Below: facts, one-button picker, two dark buttons, trust lines; trust strip as a 2×2 grid with hairlines; description stacked (kicker, h2 at ≈34 px, cards full-width, black specs panel); showcase as 5 stacked squares on `#12100e`; installation image + 4 steps; comparison **stacks into 15 boxes** (each row = header box + "ElmsNest" sub-box + "מנורה גנרית זולה" sub-box, ≈1,900 px for 5 rows); guidance = 3 stacked cards + accordions + link card; related = 2-up cards with cart-icon quick-add buttons and pagination dots; footer stacked.

### Against the design system
- Cream `#f7f0e6` on `#2b2118` everywhere, off-white bands and cards, brown-black `#12100e` "night" — the exact scheme that must go; no page gradient, nothing transparent, no stars, no dimming.
- Assistant throughout (h1, h2, prices, kickers); gold is `#d9ad5f`, not `#e9b96e`; price is brown Assistant, not glow FRL; kicker rules are the right idea but the wrong colour and face.
- Boxes: description 2×2 cards, black specs panel, comparison bordered table, guidance 3 cards + link card, trust band — "heading + four equal boxes" appears twice on one page.
- Radius: sticky-bar round thumb + pill, red circle badge, swatch circles, rounded carousel nav (Kalles), against radius 0.
- Default e-commerce kit: breadcrumb band, vertical thumb strip, two identical dark buttons with no hierarchy, a picker for a single variant ("צבע אור: צהוב חם"), quick-add + sale badge carousel, an empty FAQ section, a lone third card, blank lazy tiles in the capture.
- Same template copy on every product (installation, comparison, guidance, trust strip, showcase heading); shipping terms stated 5× — "everything repeated".
- Images: thumb 3 and showcase tile 2 are the baked "מידות והתקנה" slide; related cards are baked slides (ledger never-use list).
- Zero motion (`ani: none`); nothing lights on arrival; the honesty device (suits / does-not-suit) is absent.
- Mobile: h1 clipped by the sticky bar in the first screen; the buy block is a full screen below the fold; the comparison becomes 15 stacked boxes.

### Honesty check
- No ratings, review counts, "trusted by", countdowns, best-seller, customer quotes in the render (the theme-src `elms-pdp-reviews` "מה לקוחות כתבו" section exists in `product.elms-pdp.json` but is not used here — keep it out).
- Comparison table asserts facts about competitors: column "מנורה גנרית זולה": "משתנה", "לעיתים תרגום אוטומטי", "תלוי במוכר", "לרוב לא"; heading "מה ההבדל מול מנורה סולארית זולה". A disclaimer follows, but this is exactly the pattern.
- The ElmsNest column promises what the page does not deliver: "אפשר לשאול לפני ההזמנה — בוואטסאפ" (no WhatsApp on the page), "מפרט טכני מבוסס על נתוני היצרן — יש" (the metafield spec table `elmsnest-pdp-specs` renders nowhere; the trust strip and guidance also point to a "מפרט טכני" that does not exist — only the description's bullet list), "נאמר לכם גם מתי המוצר לא מתאים — יש" (no not-fit text anywhere on the page).
- Description claims are owner-authored and hedged ("כ־8–10 שעות בהתאם לתנאי הסביבה") — acceptable.

### Worth keeping
- `snippets/elmsnest-pdp-facts.liquid` (licensed price/shipping/ETA wording, `<bdi>` numerals; also the loader of `assets/elmsnest-pdp.css`) and `snippets/elmsnest-pdp-trust.liquid` (14-day + email; owner ban on warranty wording, phone, locality — 2026-08-14).
- `snippets/elmsnest-pdp-price.liquid` — clones the Kalles `hdt-price`/`.hdt-money` DOM contract so the price live-updates on `variant:change`; "מחיר מבצע" only when compare_at > price.
- `snippets/elmsnest-pdp-specs.liquid` (metafields `custom.battery/power_watt/lumens/charge_time_hours/light_hours/sensor_range_m/sensor_angle_deg/ip_rating/dimensions/material/color_temp/light_modes`, `<bdi dir="auto">`, drops when empty), `elmsnest-pdp-not-fit.liquid` (`custom.not_fit_for`), `elmsnest-pdp-direct-answer.liquid` (`custom.direct_answer`) — correct mechanics, empty data.
- The per-product `.elms-sales` HTML in `product.description` (kicker / h2 / lead / promise / story / benefits / specs / cta) — the actual copy source for all 27 products; restyle, do not rewrite.
- `elms-pdp-night-gallery.liquid` auto mode (`product.media` images, skip_first/max_images) and its honesty note; `elms-pdp-faq.liquid` (`<details>`, `custom.faq` list + blocks, a11y bridge) with the three authored Q&As in theme-src (delivery, cancellation, fit).
- Kalles mechanics: sticky ATC, variant buttons with live price/thumb sync, cart drawer.

### Verdict
"Same cream page as before with more boxes — nothing lights up, the menu is gone, and it tells me nothing about when this lamp is wrong for me."

---

## 2. pdp-multi — `solar-crystal-ball-string-lights` (24 variants = 6 lengths × 4 colours, 89.90–179.90)

### What renders — desktop 1440 (page 9599 px)
Identical skeleton to pdp-single; differences:
- **Main product**: h1 "גרילנדת כדורי קריסטל סולארית – 20 עד 200 נורות"; price "89.90 ₪" — the first variant's price only, no range and no "מ־". Picker "אורך ומספר נורות: 5 מ׳ / 20 נורות" = 6 outlined rectangles in two rows (5 מ׳ / 20 נורות · 6.5 מ׳ / 30 נורות · 9.5 מ׳ / 50 נורות · 11 מ׳ / 60 נורות · 13 מ׳ / 100 נורות · 22 מ׳ / 200 נורות), then "צבע תאורה: צהוב" = 4 rectangles (צהוב · כחול · צבעוני · לבן). No price or thumbnail per option; the price changes only after a click (JS). Main image = close-up crystal balls (text-free); thumbs include baked slides "22 מטר / 200 נורות LED", "התקנה פשוטה", "עמיד למים IP65".
- **Description** (`.elms-sales`): kicker "נקודות אור רגילות מאירות — כדורי הקריסטל גם מנצנצים"; h2 "ברק עדין שהופך מרפסת, פרגולה או גינה לרקע חגיגי"; promise "מראה חגיגי שמתחיל לבד בכל ערב."; h3 "הפרטים הקטנים הם אלה שנראים הכי טוב בתמונות"; cards "שמונה מצבים לאווירות שונות", "מאורך קטן ועד קישוט של חלל שלם", "צבע שמגדיר את האירוע", "מיועדת להישאר בחוץ"; h3 "בחרו אורך שמאפשר להשלים את המסגרת"; specs (5–22 מטר · 20–200 נורות LED · 8 מצבי תאורה · צהוב, כחול, צבעוני או לבן · טעינה סולארית · כ־8–10 שעות עבודה לאחר טעינה מלאה · עמידות IP65); CTA "הפכו את החלל מרגיל לחגיגי עוד לפני שהאור הראשון נדלק".
- **Showcase**: 5 squares — trellis close-up, "22 מטר / 200 נורות LED" slide (with a "סולארי" roundel), fence at dusk, "התקנה פשוטה" 5-step infographic (white background, baked Hebrew), "עמיד למים IP65" slide. All tiles loaded in this capture.
- **Installation**: image[3] = the "התקנה פשוטה" infographic (white square on cream) beside the 4 generic steps.
- **Related**: ענפי ליבנה מוארים (indoor décor, 89.90), גרילנדת כדורי LED USB או סוללות (89.90–179.90), רשת תאורת LED (109.90–469.90), תאורת גחליליות (99.90); baked-slide images.

### Mobile 390 (page 11808 px)
Fold: header → breadcrumb → square main image → 4 thumbs (3 with baked text) → h1 (2 lines, ≈44 px) → sticky bar pill "5 מ׳ / 20 נורות / צהוב - 89.90 ₪" + "הוסיפו להזמנה". Below the fold the 6 length buttons wrap into 3 rows of 2 (≈70 px tall each) and the 4 colours into one row of 4 — the picker alone is ≈420 px; then the two dark buttons and trust lines. Rest as pdp-single (comparison again 15 boxes).

### Against the design system
Everything listed for pdp-single, plus:
- A 24-variant matrix rendered as 10 plain rectangles with no prices — the buyer cannot see that 22 m costs 179.90 without clicking; the shown price "89.90 ₪" is the cheapest, unlabeled (spec §3.5 wants "מ־89.90 ₪").
- Two of five showcase tiles and the installation image are white-background baked-text slides sitting on the black ground — the darkest section holds the brightest, most catalogue-like images.
- Installation steps ("נועצים באדמה", "מכוונים את זווית התאורה") are path-light copy on a string light.

### Honesty check
Same comparison-table issues as pdp-single. Description: "נצנוץ עשיר יותר משרשרת LED רגילה" (a comparative claim vs. an unnamed product, mild). "8 מצבי תאורה", "כ־8–10 שעות" are owner-authored product facts, hedged. No reviews/ratings/countdown.

### Worth keeping
As pdp-single. Specific to this page: the option data itself (`אורך ומספר נורות` values already carry both length and bulb count — a ready-made ledger for a per-length price device), the close-up crystal-ball main image (text-free), the fence and trellis night photos (images 1, 3 in the showcase order).

### Verdict
"Twenty-four choices and I still don't know what the long one costs — and why is the installation picture a white catalogue slide on a black screen?"

---

## 3. pdp-wall — `waterproof-led-wall-light-ip65-6w-12w` (8 variants = 2 colours × 2 watt × 2 K, 219.90–252.90)

### What renders — desktop 1440 (page 9672 px)
Same skeleton; differences:
- **Main product**: h1 "מנורת קיר LED עמידה למים IP65 – ‏6W/12W" wraps with "6W/12W" alone on line 2; price "219.90 ₪" (first variant; the 219.90–252.90 range is not shown). Three pickers: "צבע גוף: לבן" (לבן · שחור), "עוצמה: 6W" (6W · 12W), "גוון אור: אור חם 3000K" (אור חם 3000K · אור קר 6000K). **Main image is a marketing slide**: beige card with baked Hebrew "תאורה שמעצבת אווירה / גוף תאורת קיר מעוצב עם הארה דו כיוונית" (product images[0]); the 6 thumbs are studio packshots on grey (single lamp, 2×2 black/white grid, wide black, wide white) plus one dusk exterior.
- **Description** (`.elms-sales`): kicker "חזית הבית נראית אחרת כשהאור מתוכנן נכון"; h2 "אלומות אור חדות שמעניקות לקיר נוכחות יוקרתית"; promise "תאורה שימושית ביום־יום, אפקט עיצובי בכל ערב."; h3 "גם קיר פשוט יכול להפוך לנקודת מוקד"; cards "מראה יוקרתי בלי להעמיס", "מתאימה באמת לחלל החוץ", "עוצמה שמתאימה לגודל הקיר" ("6W לאפקט עדין וממוקד; 12W לנוכחות חזקה יותר"), "אתם קובעים את הטון" ("3000K יוצר חמימות; 6000K מעניק מראה לבן, חד ומודרני"); h3 "תכננו את התוצאה, לא רק את מספר המנורות"; specs (גוף אלומיניום · עמידות IP65 · עוצמה 6W או 12W · אור חם 3000K או קר 6000K · צבע שחור או לבן · תאורה דו־כיוונית · מתאימה לפנים ולחוץ); CTA "הפכו קיר ריק לחלק המרשים של החזית". No mention of solar anywhere in the product's own copy (0 hits in main-product + description) — this is a mains LED.
- **Showcase** on `#12100e`: 4 of 5 tiles are light-grey/beige studio packshots (the 2×2 grid, black cube, white wide, black wide) + 1 dusk exterior; subheading still says "הפעולה האוטומטית עם החשכה" and the note "זווית הפאנל".
- **Installation**: h2 "ההתקנה ללא חוטים וללא חשמלאי", sub "רוב מוצרי התאורה הסולארית…", steps "בוחרים מקום שמקבל שמש", "מפעילים ומכוונים… זווית הפאנל לשמש", "טעינה ראשונה" — on a wired product; only the footnote ("דגמים המחוברים לרשת החשמל דורשים חיבור על ידי חשמלאי מוסמך") applies. Image = black wall light on a beige wall (blank in the desktop capture, lazy; loads on mobile).
- **Comparison**: "מה ההבדל מול מנורה סולארית זולה" — wrong category for this product.
- **Related**: wall lights (מנורת קיר סולארית עם חיישן תנועה 129.90–159.90, דו־כיוונית IP65 159.90–162.90, 6W Up & Down 109.90–193.90, גרסאות לפנים או לחוץ 99.90–121.90); two are baked-text slides, one is a packshot on white; dots below.

### Mobile 390 (page 11880 px)
Fold: header → breadcrumb ("6W/12W – IP65" line-2 renders in the right reading order) → square main image = the baked marketing slide → 4 grey packshot thumbs → h1 two lines ("מנורת קיר LED עמידה למים" / "6W/12W – IP65") → sticky bar pill "לבן / 6W / אור חם 3000K - 219.90 ₪" + "הוסיפו להזמנה". Below: three pickers (2 buttons each, three rows), two dark buttons, trust lines; then the same stack (trust 2×2, description, black specs panel, 5 stacked showcase images — four of them pale packshots on black — installation, 15-box comparison, guidance, related 2-up with dots, footer).

### Against the design system
Everything listed for pdp-single, plus:
- The first thing a buyer sees on both viewports is a baked-text marketing slide, not the lamp on a wall at night (ledger §3.6 never-use).
- The "night" showcase is four bright studio packshots on brown-black — the section reads as a catalogue page inverted.
- Template copy contradicts the product: solar installation steps, "אוטומטית עם החשכה", "זווית הפאנל", and a "solar" comparison on a wired 6W/12W lamp. The template has no power-source branch.
- Three pickers × 2 options, each a separate labelled row of rectangles; the 8-variant price spread (219.90–252.90) is invisible until clicked.
- h1 line-break leaves "6W/12W" orphaned (desktop); Latin tokens rely on an RLM in the title string, not `<bdi>`.

### Honesty check
Same comparison-table issues. Additionally the page states things that are false for this product: "ההתקנה ללא חוטים וללא חשמלאי", "רוב מוצרי התאורה הסולארית מותקנים בלי חיבור לחשמל" (as the section lead), "הפעולה האוטומטית עם החשכה", "זווית הפאנל" — a mains lamp that needs an electrician (which the page admits only in a footnote). Trust strip "מיועד לשימוש בחוץ — דרגת העמידות המדויקת מופיעה במפרט הטכני" points to a spec table that is not rendered. No reviews/ratings/countdown.

### Worth keeping
As pdp-single. Specific: the option structure (colour × watt × Kelvin) is exactly the "IP65, W, K spec sheet" the handoff asks for — the variant data can drive the spec device; the dusk exterior image (last thumb / showcase tile 5, `57f1e6…`) is the only night photo and is text-free; description lines about 6W vs 12W and 3000K vs 6000K are real, usable decision copy.

### Verdict
"It opens on a slogan card, it tells me to point the solar panel at the sun, and it is the same page as the garden light — nobody looked at this."

---

## Family summary — what a designer must know before briefing

1. **One template, one look, mostly global copy.** All products run `product.elmsnest.json`: Kalles `main-product` (Assistant, cream `#f7f0e6` / `#2b2118`, brown rectangles, vertical thumbs, sticky ATC) followed by seven "PDP Design v2" sections. Only two things change per product — the description (owner-authored `.elms-sales` HTML inside `product.description`, ~8 blocks + a spec bullet list per product) and the auto image galleries (images 2–7). Trust strip, installation, comparison, guidance, showcase headings and the (empty) FAQ are identical on every PDP; ≈5,000 of ≈9,600 desktop px repeat on every product. Pages are ≈9.5k px desktop / ≈11.8k px mobile.
2. **Variants are the real design problem.** 1 variant (still shows a one-button picker) · 24 = 6 lengths × 4 colours (89.90–179.90) · 8 = colour × watt × Kelvin (219.90–252.90); catalogue products carry 8–30 variants. The page shows the first variant's price only (no range, no "מ־"), rectangles carry no price/thumbnail, and on mobile the picker is 3–4 rows of big buttons; the Kalles sticky bar mirrors the selected variant title + price. Option values mix Hebrew and Latin ("22 מ׳ / 200 נורות", "6W", "אור חם 3000K").
3. **Data that exists vs. data that is empty.** Exists: `product.description` HTML, 6–7 images per product (several are baked-Hebrew marketing slides — the wall light's featured image is one, and Kalles uses images[0] as the main image and in related cards), variant options, compare-at prices (real "-25%" on one related product). Empty on all three samples: metafields `custom.faq`, `custom.not_fit_for`, `custom.direct_answer`, and every spec field (`ip_rating`, `power_watt`, `color_temp`, `light_hours`…) — so the spec table, not-fit panel, direct answer and FAQ render nothing, and there is no suits/does-not-suit device on the PDP at all (the four approved pairs live only in BRIEF §3).
4. **Honesty state.** No ratings, review counts, quotes, "trusted by" or countdowns are rendered (an unused `elms-pdp-reviews` section exists in theme-src — do not revive it). But the comparison table asserts facts about "מנורה גנרית זולה" and promises WhatsApp, a manufacturer spec sheet and "we tell you when it does not fit" — none of which the page delivers; and the solar-only installation/showcase/comparison copy is wrong on mains products (wall light). Shipping/cancellation terms are findable five times over; ≤5%/100₪ and "warehouses outside Israel" only via policy links; `whatsapp_number` is empty so every "ask us" is `/pages/contact-us` or `mailto:`.
5. **Two global bugs precede any PDP design.** (a) The header is transparent with `scheme-env2-night` in all states, so on every cream page the menu, search, account and mobile hamburger are invisible — the PDP's first screen must be dark (or the header needs a per-template scheme). (b) The theme-src copy of the template (3 FAQ blocks, an `elms_policy` section) does not match the live dev render (empty FAQ, no policy section); confirm which JSON is live before writing a spec against it.

## The three hardest technical constraints

1. **Kalles' JS-bound buy stack.** `hdt-variant-picker` → `hdt-price`/`.hdt-money` → `hdt-media-gallery` (main + thumbs) → `hdt-sticky-btn-atc` → cart drawer are wired by ids and DOM contracts (`form="product-form-<section>-<product>"`, `variant:change` events); the custom price snippet had to clone the DOM and re-attach `form` via an inline script at DOMContentLoaded. A redesigned buy box either keeps those contracts exactly or rebuilds variant selection, price update, sold-out state, `?variant=` URL sync, ATC and the drawer from scratch — and the mobile sticky bar must mirror whichever wins.
2. **Variant matrices with Hebrew+Latin values and no per-option price.** 24-variant products need a price-per-length ledger rendered in Liquid from `product.variants` (with `<bdi>`), unavailable-combination handling, and a mobile layout that is not 3–4 rows of rectangles; the price rule (single / min–max / "מ־") from `elmsnest-v2-price` has to replace the first-variant price without breaking live updates.
3. **Ground, header and images are page-level, not section-level.** `elmsnest-v2-base` targets `body.hdt-page-type-index` only; Kalles paints `#wrapper/main`, the breadcrumb section has its own colour scheme, `elmsnest-pdp.css` is loaded by the facts snippet and styles all `.elms-pdp-section` grounds (`cream`/`card`/`night` = `#12100e`), and the header only reads correctly over a dark first section. On top of that, Kalles picks images[0] for the main image and related cards — for several products that is a baked-text slide — and the gallery images are `loading="lazy"` without a lit/dim mechanism, so the "lamps light on arrival" idea needs its own image ledger per product plus eager loading for the first tiles.
