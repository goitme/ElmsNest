# AUDIT — content-pages family (dev theme 154726400174, mirrored 2026-09-02)

Pages: page-guide, page-why-solar, page-about, page-shipping, page-faq, page-contact, page-processing.
Sources judged: `brief/inventory/<key>/http-desktop.png` / `http-mobile.png` (1440 / 390, 2×, theme JS running), the `*-fold.png` first screens, `index.html` mirrors, `INVENTORY-FACTS.md`, `THEME-SRC.md`, `theme-src/sections/elmsnest-content-page.liquid`, `main-heading.liquid`, `main-page.liquid`, `header-group.json`. Every claim below was checked in the pixels (crops in scratchpad `crops/`), not only in the HTML.

## 0. Facts common to all seven pages (read first)

- **Template plumbing.** Six pages use `templates/page.json` = `[editorial] elmsnest-content-page` → `[heading] main-heading` (scheme S-night77, `{{ page_title }}` 4xl, no image) → `[main] main-page` (`full_width: true`, `{{ page.content }}`). `contact-us` uses `page.contact-us.json` = `main-heading` (S-night77, uppercase 2xl) → `contact-form` (2 `_contact_col` blocks). `elmsnest-content-page.liquid` (37 196 B, no settings, no blocks) is a `case page.handle` that prints hard-coded Hebrew HTML for exactly five handles — `guide-garden-lighting`, `why-solar-lighting`, `processing-time`, `מי-אנחנו`, `help-faq` — and **nothing** for any other handle (the `{{ page.content }}` fallback at l.333 is unreachable). On those five it injects `<style>#shopify-section-…__editorial ~ [id$="__heading"], … ~ [id$="__main"]{display:none!important}</style>` to hide its two sibling sections.
- **Duplicate h1 on all five editorial pages** (facts.py: guide, why-solar, about, faq, processing each report 2 h1s). The hidden `main-heading` still renders `<h1 class="sr-only hdt-pe-none">{{ page_title }}</h1>` (main-heading.liquid l.50) inside a `display:none` section, so the DOM carries the editorial `<h1>` plus a second `<h1>` with a different text (e.g. "בוחרים תאורת גינה לפי המקום — לא לפי התמונה" + "מדריך לבחירת תאורה לגינה"). Shipping and contact have one h1 each — but it is invisible (below).
- **Header (identical on all 7): the navigation is invisible.** `sections/header-group.json` → `header-inline-blocks`, rendered as `<hdt-sticky-header class="… hdt-header-tranparent-true hdt-menu-split hdt-header-sticky-on_scroll_up" color-scheme="scheme-env2-night">`, `header_layout: logo_center`, logo 50 px, `sticky_type: on_scroll_up`. It was set up for the homepage hero (night ground). On these pages the body is `color_scheme_body: scheme-1` = cream `#f7f0e6`, and the header is transparent, so its ink `#f4eee3` labels sit on cream — measured pixel delta 3/255. Desktop (70 px tall): "דף הבית · קולקציות · מדריך לבחירה · [logo] · שאלות נפוצות · מי אנחנו · יצירת קשר", a search icon (right) and a cart icon (left) all exist in the DOM and are invisible; only the gold house/heart logo and the gold "0" cart badge show. Mobile (60 px): cart + search icons left, logo centre, hamburger right — same: only the logo and the "0" badge are visible. A visitor on any content page cannot see the menu, search or cart.
- **Footer (identical on all 7):** `scheme-env2-night` (#020306) — the v2 night footer: gold logo, "שאלות על מוצר או על התאמה למקום? כתבו לנו: info@elmsnest.com", 3 columns (קולקציות ×4 / מידע ×6 / יצירת קשר ×2 incl. "לשליחת תמונה של המקום" → `/pages/contact-us`), bottom bar "ElmsNest © 2026 · תנאי משלוח וביטול" (→ `/#env2-terms`). It belongs to the new system; everything between header and footer does not, so each page reads as a cream slab between two night slices.
- **Ground and type (all 7):** page `#f7f0e6`, text `#2b2118`, secondary `#584f45`, muted `#726960`, hairlines `rgb(43 33 24 / .16)` / strong `.30`, night band `--en-night` = `#12100e`, amber `#d9ad5f`, buttons `#2b2118` fill + `#f7f0e6` label, radius 0. Type: `font_family_shopify_1/2/3 = assistant_n4` — **every glyph on every page is Assistant**; the mirror reports `FRL font loaded: False`; Heebo is not loaded. `env2 base loaded: False`, `whatsapp float: False` (0 mentions of WhatsApp/וואטסאפ in any of the 7 HTML files; `settings.whatsapp_number` is empty).
- **Editorial vocabulary (the 5 hard-coded pages):** full-bleed night band (`.en-doc__band`, padding clamp(44px,7vw,84px), h1 clamp(30px,4.6vw,52px) Assistant 700, letter-spacing −.035em, cream) + `.en-doc__role` one-liner → `.en-doc__shell` (min(1040px,100%), gutters clamp(16px,4vw,40px) → ≈960 px column at 1440) → optional `.en-doc__toc` ruled strip → `section.en-doc__sec` blocks, each an h2 clamp(24px,3vw,34px) + `ol.en-doc__sched` ruled numbered rows (numeral 13 px muted, title 17 px 700, body 15 px) → `.en-doc__cta` (filled brown `.en-doc__btn` + outlined `--ghost`, min-height 52 px, radius 0) → `nav.en-doc__foot` "לדף הבית · לכל גופי התאורה · מדריך הבחירה · יצירת קשר". Mobile: TOC becomes `overflow-x:auto; flex-wrap:nowrap; scrollbar-width:none` (clips with no affordance), CTAs stack 100 %. The en-doc CSS ships in the global `{% stylesheet %}` bundle (`a/0a99c0d2…css`), so it also styles page.content on non-editorial pages.
- **JS:** every page logs 2 console errors in the mirror (`Failed to fetch dynamically imported module …/3f57b3796d8c16827c06e9356048d925.js` and `Cannot read properties of null (reading 'innerHTML')`); pages still render. Cart-drawer and back_top sections are rendered on every page. `hdt-reveal="slide-in"` timeline attributes sit on Kalles blocks (`animations_reveal_on_scroll: true`).
- **Live data on this family:** only `collections[…].products_count` on the guide page (8 / 6 / 6 / 7 = 27) and `pages[…].url` / `shop.shipping_policy.url` / `shop.refund_policy.url` links. No product, price, image or lamp appears on any of the seven pages except one stock photo (About).

---

## 1. page-guide — `/pages/guide-garden-lighting` (desktop 3246 px, mobile 3578 px)

### What renders
Desktop, top to bottom:
1. Header (70 px, cream, nav invisible — see §0).
2. Night band `#12100e`, ≈420 px: right-aligned h1 in 3 lines "בוחרים תאורת / גינה לפי המקום / — לא לפי התמונה" (≈52 px Assistant Bold, cream) + role "ארבע החלטות קצרות: איפה צריך אור, מה הוא צריך לעשות, איזה מקור חשמל מתאים, ומה בודקים לפני שמזמינים."
3. TOC strip, hairline above/below, 4 cells with vertical dividers: "לפי מקום | לפי מטרה | מקור חשמל | לפני ההזמנה" (14 px 600).
4. "01 · איפה צריך אור?" (34 px) + intro "בחרו את האזור הקרוב ביותר לצורך שלכם והמשיכו לקולקציה המתאימה. כל קולקציה מכילה רק מוצרים לאותו מקום." + 4 ruled collection rows: "שביל, עמוד וגינה — לסימון הדרך, לערוגות ולפינות הגינה — 8 מוצרים ←", "כניסה וקיר — לדלת, לחזית ולאזורי מעבר — 6 מוצרים ←", "הארה ממוקדת — לעץ, לקיר, לפינה חשוכה או לשטח — 6 מוצרים ←", "מרפסת ואירוח — לאור חם ולאווירה בפינת הישיבה — 7 מוצרים ←" (counts are live `products_count`).
5. "02 · מה האור צריך לעשות?" — 3 ruled rows lettered א / ב / ג: "לעזור להתמצא", "להאיר נקודה", "ליצור אווירה" ("…תאורת אווירה אינה מיועדת להאיר חזק — וזה בסדר, זה תפקידה.").
6. "03 · איזה מקור חשמל מתאים?" — intro "הנתונים משתנים בין מוצרים. בדקו תמיד את עמוד המוצר…" + rows 1/2/3: "סולארי — למקום שמקבל שמש" ("…אם המקום כמעט לא מקבל שמש — אל תבחרו סולארי…"), "סוללה או USB — לשליטה בטעינה", "חיבור לחשמל — להתקנה קבועה".
7. "04 · מה בודקים לפני ההזמנה?" — rows 01–05: "מידות המוצר והשטח הזמין", "מקור החשמל ואופן ההתקנה", "מה כלול באריזה", "נתוני אור ועמידות שמופיעים במפורש", "התאמה למיקום המתוכנן" + note "פרט חשוב חסר בעמוד המוצר? אל תנחשו. שלחו לנו את שם המוצר ואת השאלה — נבדוק לפני שתזמינו." (link → contact) + buttons: filled brown "לכל גופי התאורה", outlined "שאלה לפני הזמנה".
8. Foot nav "לדף הבית · לכל גופי התאורה · מדריך הבחירה · יצירת קשר" (the third link points to this same page).
9. Night footer.

Mobile: header 60 px (logo + "0" only); band ≈230 px, h1 in 2 lines (~30 px) + role; TOC nowrap strip — the 4th cell is cut mid-word at the left edge ("לפני ההז"), no scroll cue; "01 · איפה צריך אור?", intro and the first three collection rows (8 / 6 / 6 מוצרים) are inside the 844 px fold. **Fold contains no product, price or buy CTA** — three collection links with counts are the only commercial element. Buttons stack full-width near the bottom (≈3 100 px down).

### Against the design system
- Cream page `#f7f0e6`, brown ink `#2b2118`, brown filled button, beige hairlines — the exact old scheme that must go; no sky gradient, no transparent sections (the band is an opaque `#12100e` slab, not sky).
- Assistant for display and text; no Frank Ruhl Libre, no Heebo, no glow second line, no gold kicker.
- Header nav/search/cart invisible (§0). Duplicate h1 in the DOM (§0).
- One device repeated four times on one page (ruled numbered list: collections → א/ב/ג → 1/2/3 → 01–05) — the owner's "everything repeated" verbatim.
- Zero images, zero lamps, zero motion: a 3 246 px text document about *light* with no light in it.
- Mobile TOC clips without affordance (`scrollbar-width:none`, nowrap); foot nav links to itself.
- 2 JS errors on load.

### Honesty check
Clean. No ratings/reviews/counts/quotes/countdowns/"trusted by". `rating`×13 / `review`×5 in the HTML are Kalles card hooks in shared CSS/JS (`show_rating: false`). "כל קולקציה מכילה רק מוצרים לאותו מקום" is a structural statement, fine. The negatives ("אל תבחרו סולארי" for shade) match the approved "does not suit" spirit — designer must reconcile wording with the four approved pairs.

### Worth keeping
- The four-decision spine (place → purpose → power → checks) and all of its copy — `elmsnest-content-page.liquid` l.39–113.
- `.en-doc__links` rows fed by `collections['תאורת-שביל-סולארית'|'solar-wall-lights'|'ספוטים-ופרוז-קטורים-סולאריים'|'גרילנדות-ותאורה-דקורטיבית'].products_count` — the only live data in the family.
- The "missing spec → ask before ordering" fallback (`pages['contact-us'].url`) and `<bdi dir="ltr">` on every Latin token / numeral.
- Radius 0, hairline tokens `--rule/--rule-strong/--rule-night` (values must change, the idea stays).

### Verdict
"A well-written PDF with the menu missing — cream, brown, no pictures, and the same list four times."

---

## 2. page-why-solar — `/pages/why-solar-lighting` (desktop 2439 px, mobile 3007 px)

### What renders
Desktop:
1. Header (nav invisible).
2. Night band ≈420 px: h1 in 3 lines "למה תאורה / סולארית / — ומתי לא" (the third line is a lone dash + two words) + role "היתרון: פחות תלות בחיבור קבוע לחשמל. ההתאמה תלויה בשמש שהמקום מקבל, במטרת האור ובנתוני המוצר הספציפי."
3. "איך זה עובד בפועל" — rows 1/2/3: "ביום — הפאנל הסולארי נטען מאור היום. צל, כיוון הפאנל ועונת השנה משפיעים על הטעינה.", "בערב — התאורה נדלקת ועובדת על האנרגיה שנאגרה…", "מה זה אומר — השמש היא חלק מהמפרט. בימים מעוננים או בחורף הביצועים עשויים להיות חלשים יותר — זו לא תקלה, זה אופי הפתרון."
4. "מתי זה מתאים — ומתי עדיף פתרון אחר" — a **bordered two-column box** (`.en-doc__grid2`, 1 px `rgb(43 33 24/.30)`): right panel "יכול להתאים כאשר" 4 dash items (good daylight / no fixed connection wanted / purpose is mood, path-marking or spot / specs match); left panel "עדיף פתרון אחר כאשר" 3 items: "המקום כמעט ואינו מקבל אור יום — סולארי לא יספיק שם", "נדרש אור חזק וקבוע לאורך כל הלילה — תאורה סולארית לא תמיד מחליפה תאורה חשמלית חזקה", "יש דרישות התקנה מיוחדות — אז חיבור קבוע עם בעל מקצוע, או מוצר נטען ב־USB".
5. "שלוש בדיקות לפני שבוחרים" — rows 1/2/3 as questions ("כמה אור יום מגיע למקום?", "האם המטרה היא אווירה, התמצאות או הארה ממוקדת?", "אילו נתונים מופיעים במפורש בעמוד המוצר?") + note "חלק מהמוצרים בחנות מיועדים בעיקר לאווירה ולא לאור חזק…" + buttons: filled "איך בוחרים תאורה לגינה?", outlined "לכל גופי התאורה".
6. Foot nav, night footer.

Mobile: band ≈240 px, h1 2 lines; "איך זה עובד בפועל" and its three rows fill the fold; the grid2 box stacks into two stacked bordered panels; **no product/price/CTA in the fold**. Buttons at ≈2 300 px.

### Against the design system
- Cream/brown/Assistant/invisible header/duplicate h1 (§0).
- A bordered box with two bordered panels — "no boxes/cards, hairlines separate" broken.
- The page whose subject is *a lamp switching on at dusk* ("בערב התאורה נדלקת") has no lamp, no dusk, no image, no motion; the design system's central device is described in words here and not shown.
- Orphaned h1 line "— ומתי לא" at desktop width; the list device repeats the guide page.

### Honesty check
No fabricated claims. "זו לא תקלה, זה אופי הפתרון" fine. **Flag:** the does-not-suit list carries three general negatives (deep shade, all-night strong light, special installation) — the brief allows only the four approved suits/does-not-suit pairs; wording must be mapped onto them or dropped.

### Worth keeping
- The honest "sun is part of the spec" framing and the suits / does-not-suit pairing (`elmsnest-content-page.liquid` l.114–169) — content, not the box.
- Day/evening/meaning three-beat (it is a storyboard for the lamp-lights-on motion).
- Cross-links to the guide and the collections.

### Verdict
"The one page whose subject *is* light at dusk, delivered as a cream text document with a bordered table."

---

## 3. page-about — `/pages/מי-אנחנו` (desktop 2702 px, mobile 2987 px)

### What renders
Desktop:
1. Header (nav invisible).
2. Photo band ≈390 px (`.en-doc__band--media`): full-bleed **stock photo `pexels-taryn-elliott-4112233.jpg`** — a kerosene hurricane lantern on a table with cushions, plants, a wine bottle and a wooden ladder, sepia/brown, `filter: brightness(.6) contrast(1.06) saturate(.88)` + dark shade; eager, `fetchpriority: high`, `sizes 100vw`, widths 800–2200. Over it, right-aligned h1 "רק תאורת חוץ. וזה בכוונה." + role "אנחנו עוזרים להתאים גוף תאורה למקום שלכם — וגם אומרים כשמשהו לא מתאים."
3. "למה הקמנו את ElmsNest" (h2 with Latin brand) + one paragraph ("בחירת תאורה באינטרנט יכולה להיות מבלבלת… ElmsNest עוסקת בתחום אחד — תאורת חוץ — ומארגנת את הבחירה לפי מקום, מטרה ואופן שימוש…").
4. "העקרונות שמכוונים אותנו" — rows 01/02/03: "בהירות לפני הבטחות — כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה.", "בחירה לפי צורך", "שאלה לפני הזמנה".
5. "מה זה אומר בפועל" — rows 1/2/3: "אין אצלנו קטגוריה אחרת — …תאורת חוץ בלבד: סולארית, נטענת, בסוללה או בחיבור לחשמל.", "המפרט לפני הקנייה — …נתון שלא מופיע — לא ממציאים.", "וכשמשהו לא מתאים — אומרים — …עדיף לקוח שקנה נכון מלקוח שהתאכזב."
6. "מה תמצאו בחנות" — 4 ruled rows with "←" and **no counts**: "שביל, עמוד וגינה", "תאורת קיר", "ספוטים ותאורה ניידת", "אווירה ודקורציה" + buttons filled "לכל גופי התאורה", outlined "איך בוחרים תאורה לגינה?".
7. Foot nav, night footer.

Mobile: photo band ≈230 px with the h1 on one line + role; "למה הקמנו את ElmsNest" + paragraph + "העקרונות" h2 + row 01 inside the fold. **No product/price/CTA in the fold.**

### Against the design system
- The only photograph in the whole family is a Pexels stock image of a **kerosene** lantern — not a product, not solar, not outdoors, not theirs — on the page that says "רק תאורת חוץ". It is static (no dim → lit), sepia-brown, and sits over an otherwise cream page.
- Cream/brown/Assistant/invisible header/duplicate h1 (§0). Three identical ruled lists back to back (01–03, 1–3, 4 rows) then the same two buttons as every page.
- The four collections are named differently here ("הארה ממוקדת" on the guide, "ספוטים ותאורה ניידת" here, "ספוטים ופרוז׳קטורים" in the footer, "ספוטים, פרוז׳קטורים ותאורה ניידת" in the header menu) — four naming sets for the same four collections across one family.

### Honesty check
No ratings/quotes/counts. "בהירות לפני הבטחות" is a stance, fine. **Risk:** the stock lantern photo implies a scene/product that is not the store's — the brief's honesty bar ("no fabricated") extends to imagery on an About page.

### Worth keeping
- The h1 "רק תאורת חוץ. וזה בכוונה." — the strongest line in the family — and the role line.
- The three principles and "עדיף לקוח שקנה נכון מלקוח שהתאכזב" (`elmsnest-content-page.liquid` l.204–254).
- The media-band mechanics (`images[...] | image_url: width: 2200 | image_tag: loading:'eager', fetchpriority:'high'`, l.207) — swap the image for a real lamp that lights on arrival.

### Verdict
"A sincere manifesto stapled to a stock photo of a paraffin lamp we don't sell."

---

## 4. page-shipping — `/pages/shipping-delivery` (desktop 2491 px, mobile 2791 px)

Handle is **not** one of the five editorial handles → `elmsnest-content-page` prints nothing and does not hide its siblings, so the Kalles path renders.

### What renders
Desktop:
1. Header (nav invisible).
2. `main-heading` (S-night77, no image, `bg_overlay: 0`, pd 50/50): `<h1 class="sr-only">משלוחים והחזרות</h1>` + visible block `hdt-heading-liquid hdt-text-4xl` "משלוחים והחזרות" in the scheme's text colour `#f7f0e6` — but `main-heading` paints no background for its colour scheme (no `hdt-s-gradient`, only an empty `.hdt-heading-image` with overlay 0), so it is cream text on the cream body: **invisible**. Result: ≈200 px of blank cream under the header (threshold scan of the region: 0 text pixels).
3. `main-page` (`scheme-1`, `full_width: true` → `hdt-container-full`, pd 50/60): `page.content` written with en-doc classes (`en-doc`, `en-doc__sec`, `en-doc__sched`, `en-doc__num`, `en-doc__intro`, `en-doc__note`, `en-doc__cta`, `en-doc__btn`, `en-doc__btn--ghost`) but **without** `.en-doc__shell`, band or foot nav. The global en-doc CSS styles the rows, nothing constrains the width: h2s "עלויות משלוח", "זמני טיפול ואספקה", "ביטול עסקה והחזרות", "עברו 17 ימי עסקים והחבילה לא הגיעה?" and the numerals sit **flush against the right edge of the viewport, zero gutter**; hairlines span the full 1440 px; paragraphs run edge to edge. Content: "1 משלוח לנקודת איסוף בישראל — חינם / לכל הזמנה, בלי מינימום." · "2 שליח עד הבית — 29.90 ₪ / אפשרות המשלוח והמחיר הסופי מוצגים בקופה לפני התשלום." · "1 טיפול בהזמנה: 1–3 ימי עסקים" · "2 זמן הובלה משוער: 7–14 ימי עסקים / מוצרים עשויים להישלח ממחסנים מחוץ לישראל. הזמנה עם כמה פריטים עשויה להגיע בחבילות נפרדות, בלי חיוב נוסף." · "3 סה״כ משוער: 8–17 ימי עסקים / …יום עסקים: ראשון עד חמישי, למעט ערבי חג, חגים וימי שבתון." · tracking note + link "מדיניות המשלוחים המלאה" · "1 ביטול עד 14 ימים מקבלת המוצר / …5% ממחיר העסקה או 100 ₪, הנמוך מביניהם." · "2 מוצר פגום, חסר או שגוי" · "3 אל תשלחו מוצר לפני קבלת הנחיות" · "הנוסח המחייב: מדיניות הביטולים, ההחזרות וההחזרים." · "עברו 17 ימי עסקים והחבילה לא הגיעה?" + filled "ליצירת קשר" (glued to the top-right corner of the viewport) + outlined "מה קורה אחרי שהזמנתם" (→ processing-time).
4. Night footer directly (no foot nav).

Mobile: header; ≈150 px blank (invisible h1); "עלויות משלוח" and rows 1–2 flush to the right edge with no padding; "זמני טיפול ואספקה" row 1 enters at the fold. **No product/price/buy CTA in the fold.** Buttons full-width, also edge to edge.

### Against the design system
- **Invisible page title** (cream-on-cream `main-heading`) — the page has no visible name.
- **No gutters**: text touches the viewport edge on desktop and mobile; measure ≈1 400 px on desktop.
- No band, no shell, no foot nav — the page is a different species from its five siblings while using their classes.
- Cream/brown/Assistant/invisible header (§0). Ruled-list device again.
- The single most important consumer-terms page in the store looks unfinished.

### Honesty check
Clean, and it is the **one page that carries every consumer term**: free pickup, 29.90 ₪ door, 1–3 + 7–14 = 8–17 business days, "ממחסנים מחוץ לישראל", 14-day cancellation, 5 % or 100 ₪ whichever is lower, "אל תשלחו מוצר לפני קבלת הנחיות", 17-day escalation → contact. Every numeral is wrapped in `<bdi dir="ltr">`.

### Worth keeping
- All of the copy, verbatim (it mirrors the legal policies; `shop.shipping_policy.url` / `shop.refund_policy.url` links included).
- The "17 business days passed?" escalation block and the cross-link to `processing-time`.
- The numbered-row markup with `<bdi>` — reusable data, needs a real ground and a column.

### Verdict
"Looks broken — no title, text jammed against the edge of the screen — and these are the most important words in the store."

---

## 5. page-faq — `/pages/help-faq` (desktop 2229 px, mobile 2475 px)

### What renders
Desktop:
1. Header (nav invisible).
2. Night band ≈280 px: h1 "שאלות נפוצות" (one line, 52 px) + role "תשובות קצרות לפני ואחרי ההזמנה. לא מצאתם תשובה? כתבו לנו." (underlined link → contact).
3. TOC strip, 3 cells: "מוצרים והתאמה | הזמנות ומשלוח | ביטול והחזרות".
4. "מוצרים והתאמה" — 4 native `<details>` rows with "+" / "−" glyphs at the far left: "האם כל המוצרים בחנות סולאריים?" (open by default: "לא. ElmsNest מציעה תאורת חוץ בלבד, אבל מקורות החשמל שונים: סולארי, נטען ב־USB, סוללות או חיבור לחשמל…"), "האם תאורה סולארית עובדת גם בחורף?", "איך בוחרים תאורה שמתאימה למקום?", "נתון שחשוב לי לא מופיע בעמוד המוצר. מה עושים?".
5. "הזמנות ומשלוח" — 4 closed: "כמה עולה המשלוח?" (answer: "משלוח לנקודת איסוף בישראל — חינם. שליח עד הבית — 29.90 ₪…"), "תוך כמה זמן ההזמנה מגיעה?" ("8–17 ימי עסקים: 1–3 ימי טיפול ועוד 7–14 ימי משלוח"), "איך עוקבים אחרי ההזמנה?", "איך פונים לגבי הזמנה קיימת?".
6. "ביטול והחזרות" — 2 closed: "אפשר לבטל עסקה אחרי שהזמנתי?" ("…עד 14 ימים… 5% ממחיר העסקה או 100 ₪ — הנמוך מביניהם"), "קיבלתי מוצר פגום או שגוי. מה עושים?".
7. Buttons: filled "ליצירת קשר", outlined "למדיניות המלאה". Foot nav, night footer.

10 questions in 3 groups; only the first is open on first paint, so the shipping/cancellation figures are present in the DOM but not visible without a tap.

Mobile: band ≈180 px; TOC's 3 cells fit; "מוצרים והתאמה" h2, the open first Q&A and the second question are inside the fold. **No product/price/CTA in the fold** (the band's "כתבו לנו" link is the only action).

### Against the design system
- Cream/brown/Assistant/invisible header/duplicate h1 (§0).
- Plus/minus accordion = the default FAQ pattern of any theme; nothing a lighting store alone could have.
- A 280 px opaque black slab for two words; then the same button pair as every sibling.
- Consumer terms live inside closed `<details>` — findable by search/DOM, not by eye.

### Honesty check
Clean. "ואנחנו אומרים את זה גם כשזה אומר לוותר על מכירה" is a stance, not a claim. No FAQPage JSON-LD present in the page (not required, noted).

### Worth keeping
- The 10 Q&A texts — accurate, link-rich, consistent with the policies (`elmsnest-content-page.liquid` l.255–332).
- Native `<details>/<summary>` (no JS, keyboard-accessible, works when the theme JS fails as it does in the mirror).
- The three-group order (fit → order/ship → cancel/return).

### Verdict
"A competent FAQ from any theme; nothing in it says lighting, nothing says ElmsNest."

---

## 6. page-contact — `/pages/contact-us` (template `page.contact-us`; desktop 1293 px, mobile 2227 px)

### What renders
Desktop:
1. Header (nav invisible).
2. `main-heading` (S-night77, `use_dynamic_source: true`, no image, `hdt-uppercase`, 2xl): "יצירת קשר" — same cream-on-cream failure as shipping → **invisible**, ≈150 px of blank cream under the header.
3. `contact-form` section (`hdt-s-gradient`, `section_layout: container`, 2 columns ≥ md):
   - Right column — Shopify `{% form 'contact' %}` (`POST /contact`): labels "שם מלא", "כתובת מייל", "מספר טלפון", "הודעה (נדרשת)" above inputs that render as **solid dark-brown `#2b2118` slabs** (≈40 px high, no visible border; textarea `rows="20"` ≈ 330 px of brown); all four fields `required` (phone `pattern="[0-9\-]*"`); no placeholders; submit = full-width outlined "שליחה".
   - Left column — rich text: h3 "שאלה לפני הזמנה?" · "זה בדיוק בשבילנו. כדי שנוכל לבדוק התאמה למקום שלכם, צרפו להודעה:" · bullets "תמונה של המקום שרוצים להאיר", "קישור למוצר ששוקלים", "השאלה עצמה — למשל כמה שמש המקום מקבל, או אילו מידות דרושות" · "ואם משהו לא מתאים למקום — נגיד את זה מראש." · h3 "פנייה על הזמנה קיימת?" · "ציינו מספר הזמנה ואת האימייל ששימש לרכישה, ונבדוק את הפנייה." · "דוא״ל: info@elmsnest.com" · "ElmsNest, ישראל".
4. Night footer (no foot nav).

Mobile: header; ≈130 px blank; **the form comes first** — "שם מלא / כתובת מייל / מספר טלפון" labels and three brown slabs, then "הודעה (נדרשת)" with the textarea starting at the fold. The explanation of what to send sits *below* the 330 px textarea and the send button. **Fold: no CTA besides the form; no product/price.**

### Against the design system
- Invisible h1; dark-brown input bricks (brown is banned); two-column Kalles layout; Assistant; cream.
- The copy asks for "תמונה של המקום" but the Shopify contact form has no file field — the ask cannot be met on this page; there is no WhatsApp path (0 mentions; `whatsapp_number` empty) although every "שלחו תמונה / לשליחת תמונה של המקום" link in the store resolves here.
- Phone is required (friction for a pre-purchase question); textarea rows=20; on mobile the instructions are hidden below the form.

### Honesty check
Clean. "ואם משהו לא מתאים למקום — נגיד את זה מראש." is the store's stance.

### Worth keeping
- The instruction copy (photo / product link / the question; order-number + email for existing orders) — `templates/page.contact-us.json` `_contact_col` rich text.
- Shopify form mechanics (`contact[name]/[email]/[phone]/[body]`, `/contact` POST) and `info@elmsnest.com`.
- `sections/contact-form.liquid` as a schema reference for a rebuilt section (blocks, spacing settings).

### Verdict
"A blank space, four brown bricks and a send button — and it is where every 'send us a photo' link in the store lands."

---

## 7. page-processing — `/pages/processing-time` (desktop 1856 px, mobile 2330 px)

### What renders
Desktop:
1. Header (nav invisible).
2. Night band ≈440 px: h1 "זמני טיפול בהזמנה" + role "המספרים כאן זהים למדיניות המשלוחים המלאה — אין הבטחות נפרדות." + `dl.en-doc__plate`: a **bordered 3-cell plate** (1 px `rgb(232 227 217/.28)`, bg `#12100e/.86`, max-width 44 rem): "טיפול בהזמנה / 1–3 ימי עסקים", "זמן הובלה / 7–14 ימי עסקים", "סה״כ משוער / 8–17 ימי עסקים" — values in **amber `#d9ad5f`**, 21 px 700 (the only warm accent in the family).
3. "מה קורה אחרי שהזמנתם" — rows 1/2/3: "ההזמנה נקלטת — אישור נשלח לאימייל שהוזן ברכישה. בדקו שהשם, הטלפון והכתובת נכונים — ואם יש טעות, פנו אלינו מיד.", "ההזמנה מטופלת ונמסרת לשילוח — עד 3 ימי עסקים. כשמספר מעקב זמין — נשלח לכם אותו.", "ההזמנה בדרך — זמן ההובלה המשוער הוא 7–14 ימי עסקים. הזמנה עם כמה פריטים עשויה להגיע בחבילות נפרדות, בלי חיוב נוסף." + note "יום עסקים: ראשון עד חמישי, למעט ערבי חג, חגים וימי שבתון."
4. "עברו 17 ימי עסקים והחבילה לא הגיעה?" + paragraph + filled "ליצירת קשר", outlined "למדיניות המשלוחים המלאה".
5. Foot nav, night footer.

Mobile: band ≈470 px — h1, role, and the plate stacked as three rows with amber values fill most of the fold; "מה קורה אחרי שהזמנתם" enters at ≈800 px. **No product/price/CTA in the fold.**

### Against the design system
- The plate is a bordered box; amber `#d9ad5f` is not gold `#e9b96e` / glow `#ffd394` (close, off-system).
- The three numbers are the one thing here that could be a device (a 17-day strip, a dusk-to-dawn timeline) and they are a table; then the same numbered-list + two-buttons device as every sibling.
- Cream/brown/Assistant/invisible header/duplicate h1 (§0). 1 856 px for three numbers.
- "ממחסנים מחוץ לישראל" is **not** on this page (only shipping-delivery says it) though it explains the 7–14 days.

### Honesty check
Clean; "אין הבטחות נפרדות" is itself the honesty statement; "עד 3 ימי עסקים" is consistent with 1–3.

### Worth keeping
- The plate data as `<dl>` with `<bdi>` numerals (`elmsnest-content-page.liquid` l.170–203) — the data, not the box.
- The three-step "what happens after you order" copy and the 17-day escalation block.
- Strict consistency with the shipping policy (one source of numbers).

### Verdict
"Three honest numbers in a box, then the same numbered list as every other page."

---

## Family summary

### The five biggest facts a designer must know
1. **Nothing between header and footer is on-system, and the header is invisible.** All seven pages are cream `#f7f0e6` / brown `#2b2118` / Assistant (`font_family_shopify_1/2/3 = assistant_n4`; FRL and Heebo never load), with a `#12100e` opaque band as the only "night". The shared `header-inline-blocks` is `hdt-header-tranparent-true` + `scheme-env2-night` (built for the homepage hero): its ink `#f4eee3` menu labels, search and cart icons sit on the cream body at a 3/255 delta — desktop and mobile visitors see only the gold logo and a gold "0" badge. The footer is the v2 night footer, so every page is a cream slab between two night slices.
2. **Five pages are one hard-coded Liquid switch; two fall through and break.** `sections/elmsnest-content-page.liquid` (37 KB, no settings/blocks) prints full Hebrew HTML for `guide-garden-lighting`, `why-solar-lighting`, `processing-time`, `מי-אנחנו`, `help-faq` and hides the template's `main-heading` + `main-page` with injected CSS — leaving a second `<h1 class="sr-only">` in the DOM on all five (duplicate h1). `shipping-delivery` and `contact-us` are outside the switch: `main-heading` (S-night77) paints cream text on an unpainted cream ground → **invisible h1 on both**, and shipping's `page.content` (en-doc classes, no shell, `full_width: true`) runs **flush to the viewport edge with zero gutter**.
3. **One device, repeated.** Night band (h1 + one-liner) → ruled numbered list ×2–4 → filled-brown + outlined button pair → foot nav. Guide has four lists, About three, why-solar two plus a bordered 2-column panel, processing a bordered 3-cell plate plus one list, FAQ ten plus/minus `<details>`. No product, price, lamp, motion or photo anywhere except one Pexels stock **kerosene** lantern on About (`pexels-taryn-elliott-4112233.jpg`). The only live data in the family are the four `collections[…].products_count` rows on the guide (8 / 6 / 6 / 7 = 27). Heights: desktop 1 293–3 246 px, mobile 2 227–3 578 px; no fold on any page contains a product, price or buy CTA.
4. **The copy is honest, complete and reusable verbatim** — every consumer term is present with `<bdi>` numerals: all of them on shipping-delivery; 1–3 / 7–14 / 8–17 on processing; prices, days, 14-day / 5 % or 100 ₪ inside FAQ accordions; "ask before ordering" on the guide. Gaps: "warehouses outside Israel" appears on **one** page (shipping); "send a photo on WhatsApp" appears on **none** (0 mentions; `settings.whatsapp_number` empty) — every "send a photo" link lands on a contact form that cannot take a photo and requires a phone number; the four collections carry four different name sets across guide / About / footer / header menu.
5. **Honesty audit is clean on all seven.** No ratings, review counts, "trusted by", countdowns, best-sellers or customer quotes (the `rating`/`review` grep hits are Kalles card hooks in shared JS/CSS, `show_rating: false`). Two things need a decision: the stock lantern photo on About, and why-solar's three general does-not-suit negatives vs. the four approved pairs. Every page logs the same two JS errors in the mirror (failed dynamic `import()` + `null.innerHTML`) and still renders — the new pages must keep rendering fully without theme JS.

### The three hardest technical constraints
1. **Global header/body ground.** The header is a shared header-group section (`header-group.json`: transparent, `scheme-env2-night`, logo-centre, sticky-on-scroll-up) and the body scheme is global (`color_scheme_body: scheme-1`); `elmsnest-v2-base` scopes its gradient to `body.hdt-page-type-index`. Fixing the invisible menu means giving every non-index template a night ground under a transparent header (or switching the header scheme per template) from `layout/theme.liquid` / a page-agnostic base — not from the page template (HANDOFF §3 "page-agnostic core" split).
2. **Content plumbing.** `templates/page.json` is the default for *every* page; `elmsnest-content-page` is handle-keyed with no editor control and prints nothing for unknown handles; `main-heading` (l.50 `sr-only` h1, scheme background not painted) and `main-page` (`full_width`, `hdt-rte`) are Kalles sections shared with the four policy templates. A rebuild must choose per-handle Liquid vs. per-page section/block templates (`page.elmsnest-content.json` exists with only the content section), remove the duplicate h1 rather than hiding it, and give shipping-delivery/contact-us the same vocabulary as the five.
3. **Contact form and Kalles runtime.** `sections/contact-form.liquid` is Kalles (`hdt-s-gradient`, `hdt-form-input_wrap`, `hdt-btn-outline`, `hdt-reveal="slide-in"` timelines, scheme-driven `input_primary` colours); Shopify `{% form 'contact' %}` has no file upload, phone is `required` with `[0-9\-]*`; the WhatsApp path depends on an admin setting nobody can set from code (`whatsapp_number`). Cart-drawer, back_top and reveal animations run on every page with 2 JS errors, and the mobile TOC pattern (`overflow-x:auto; scrollbar-width:none`) clips without affordance — new sections need the `html.env2-js` guard, logical properties (Sense RTL flips physical ones) and `<bdi>` for every Latin token/number.
