# AUDIT — family `policies-home` (policy-shipping · policy-refund · policy-terms · policy-privacy · home)

Inventory step, dev theme `154726400174`, mirrors of 2026-09-02 in `brief/inventory/<key>/` (`http-*.png` = real render with theme JS at 1440 / 390, 2×). Every statement below was checked against the PNG slices (`scratchpad/crops/<key>-{desktop,mobile}-N.jpg`) and the mirrored `index.html`; pixel values are sampled from the 2× PNGs. Section order per page is from `INVENTORY-FACTS.md`; what each theme file does is from `THEME-SRC.md`.

## 0. Facts shared by all four `/policies/*` pages

| fact | value |
|---|---|
| Template | Shopify's built-in `policy` template. `body.hdt-page-type-policy`. **No template JSON, no sections** — `INVENTORY-FACTS` lists only `header_inline_blocks` → `footer` → `footer_bottom` → `cart-drawer` → `back_top`. The main content is `<main id="MainContent"><div class="shopify-policy__container"><div class="shopify-policy__title"><h1>…</h1></div><div class="shopify-policy__body"><div class="rte">…admin HTML…</div></div></div>`. Kalles JS adds `hdt-rte` to `.rte` after load (inline script) — there are **0** `.hdt-rte` CSS rules in the page, so it has no effect. |
| What reaches them | Only `layout/theme.liquid` (global CSS/JS, `request.page_type == 'policy'`), `css-variables` (body scheme `scheme-1`), the header/footer/system groups, and whatever the merchant types into Settings → Policies (`shop.shipping_policy.body` etc.). `env2 base loaded: False · FRL font loaded: False` on all four (the v2 base is rendered by the homepage hero only, gradient targets `body.hdt-page-type-index` — `theme/snippets/elmsnest-v2-base.liquid` l.25–39). |
| Ground | body background `#f7f0e6` (sampled (247,240,230)); ink `#2b2118` (sampled (43,33,24)) — **exactly the cream/brown scheme the design system bans**. |
| Type | `--f_family_1: Assistant` for everything (`settings_data`: all three font slots `assistant_n4`, `hd_fweight: 600`). h1 ≈54 px centred, h2 42 px, h3 34 px, body 16 px / 1.7, `<strong>` in Assistant 700, links underlined in ink. No Frank Ruhl Libre, no Heebo. |
| Measure | Shopify's own policy CSS (`a/0ea26fb…css`, 294 B) sets `.shopify-policy__container{max-width:65ch}` and `.shopify-policy__title{text-align:center}`; Kalles overrides it (`a/24853d4…css`): `.shopify-policy__container{max-width:unset!important;width:min(90rem,calc(100vw - 30px));padding:50px 0}` → on desktop every paragraph runs **≈1410 px wide** (visible in every desktop slice: lines span the full 1440 viewport minus 15 px each side). Title centred, everything else right-aligned. |
| Header state | `hdt-sticky-header … hdt-header-tranparent-true is-sticky color-scheme="scheme-env2-night"` with `enabled-transparent-header` present, `background_opacity_transparent: 0`. Result on the cream page: **the nav is invisible** — darkest pixel in the nav row is (244,238,227) = ink `#f4eee3` on `#f7f0e6` (contrast ≈1.03:1). Desktop: 9 menu links exist in the HTML (דף הבית · תאורת שביל, עמוד וגינה · תאורת קיר · ספוטים, פרוז׳קטורים ותאורה ניידת · גרילנדות ותאורה דקורטיבית · מדריך לבחירה · שאלות נפוצות · מי אנחנו · יצירת קשר) but only the gold house logo (centre) and a glow `#ffd394` circle with "0" (cart count, top-left) can be seen; the search icon (top-right) is invisible. Mobile: glow "0" badge top-left, cart/search icons and the hamburger (top-right) are cream-on-cream ghosts (see `crops/policy-mheader-zoom.png`). |
| Footer state | Night: `#020306` (sampled (2,3,6)), gold logo, "שאלות על מוצר או על התאמה למקום? כתבו לנו: info@elmsnest.com", columns קולקציות (4 links) / מידע (6 links) / יצירת קשר (2 links), bottom line "ElmsNest © 2026 · תנאי משלוח וביטול" → `/#env2-terms`. Correct per the system, but it meets the cream body with a **hard cream→black cut** (no gradient, no hairline). |
| Back-to-top | `<back-to-top class="… hdt-progress_bar_true …" style="--cricle-normal:#d2cbc1;--cricle-active:#2b2118">` — beige/brown progress ring appears on scroll (fixed element, not in the full-page shot). |
| Fold | Desktop 1440×900 and mobile 390×844 on all four: header → h1 → h2 (repeats the title) → bold date → intro paragraph → first h3 (+ bullets). **No product, no price, no CTA in any fold** (the "29.90 ₪" in the shipping fold is a fee, not a buy). |
| Links out | shipping / refund / privacy: only `mailto:info@elmsnest.com` and `/pages/contact-us` (printed as the literal URL). terms additionally links `/policies/shipping-policy`, `/policies/refund-policy`, `/policies/privacy-policy`. Nothing links to a product or collection; nothing links from one policy to the next (except terms). |
| JS errors (both viewports, all pages) | `Failed to fetch dynamically imported module …3f57b3796d8c…js` + `Cannot read properties of null (reading 'innerHTML')` — same two on every mirrored page incl. home; mirror artefacts, not page-specific. |

---

## 1. policy-shipping — `/policies/shipping-policy` — "מדיניות משלוחים – ElmsNest"

**Page height:** desktop 2070 px, mobile 2728 px (`shot-http.log`). 290 words, h1 ×1, h2 ×1, h3 ×8.

### 1.1 What renders
Desktop (top → bottom):
1. Header 70 px, transparent, invisible nav; gold logo; glow "0" badge top-left.
2. `h1` "מדיניות משלוחים" centred, Assistant 600 ≈54 px, `#2b2118` on `#f7f0e6`, ~50 px top padding.
3. `.rte`: `h2` "מדיניות משלוחים" (identical to the h1, right-aligned, 42 px) → `<p><strong>עודכן לאחרונה: 5 באוגוסט 2026</strong>` → intro "ב-ElmsNest חשוב לנו שתדעו מראש כיצד ההזמנה מטופלת, כמה עולה המשלוח ומתי היא צפויה להגיע."
4. `h3` "אזורי משלוח ועלויות" + 2 bold bullets "משלוח לנקודת איסוף בישראל: חינם." / "שליח עד הבית בישראל: 29.90 ₪." + "אפשרות המשלוח הזמינה והמחיר הסופי מוצגים בקופה לפני התשלום."
5. `h3` "זמני טיפול ואספקה" + 3 bullets (1–3 / 7–14 / 8–17 ימי עסקים, numbers bold) + business-day definition paragraph.
6. `h3` "מקור המשלוח וחבילות נפרדות" ("מוצרים עשויים להישלח ממחסנים מחוץ לישראל…") → `h3` "מעקב אחר ההזמנה" → `h3` "כתובת ופרטי קשר" → `h3` "עיכוב, חבילה חסרה או מוצר פגום" ("אם חלפו 17 ימי עסקים…") → `h3` "ביטול והחזרת משלוח" → `h3` "יצירת קשר" (דוא"ל + "טופס יצירת קשר: https://elmsnest.com/pages/contact-us").
7. Hard cut to the night footer at y≈1720 (desktop).
Mobile: same order, one column, 15 px gutters; the title block (h1 + h2 + date) takes the top ~40 % of the first screen; **above the 844 px fold** you get the h1, h2, date, intro, both cost bullets, the three delivery-time bullets and the business-day paragraph — the most information-dense fold of the four. The literal URL wraps mid-token at the bottom ("https://elmsnest.com/pages/contact-" / "us"). Full-page render is cream until y≈2300, then black footer.

### 1.2 Against the design system
- Ground `#f7f0e6` + ink `#2b2118` (body scheme `scheme-1`) — the banned cream/brown, on 83 % of the page height.
- Assistant for display and text; heading weight 600; no serif, no Heebo, no glow second line, no kicker/gold rule.
- Duplicate heading: h1 "מדיניות משלוחים" centred, then h2 "מדיניות משלוחים" right-aligned 60 px below it — reads as a template error.
- Invisible header: menu, search and (mobile) hamburger have no contrast on cream (ink on cream); the only visible header elements are the gold logo and a glow "0" cart badge — a policy page shows a cart count as its most prominent header element.
- Full-width measure (≈1410 px lines) on desktop; Shopify's 65ch was overridden by Kalles. Unreadable as prose.
- Default e-commerce/document patterns: disc bullets, bold-inline facts, underlined dark links, bold "last updated" line, printed raw URL as link text.
- Latin run inside RTL: "https://elmsnest.com/pages/contact-us" rendered as visible text, wraps "contact-" / "us" on mobile; "ב-ElmsNest" and "29.90 ₪" not wrapped in `<bdi>` (they render correctly here but are not protected).
- No hairlines anywhere; the only separation is white space; the page ends in a hard cream→`#020306` cut.
- Back-to-top ring in `#d2cbc1` / `#2b2118` (old palette).
- Dead end: no path to products, to the other policies, or to the homepage ledger; no TOC for 8 sections.
- Nothing unfinished per se — it is simply the stock Shopify policy page with the old Kalles scheme.

### 1.3 Honesty check
Clean. No ratings, counts, "trusted by", countdowns, best-seller, quotes, comparison tables. Every figure matches the homepage ledger and the PDP snippets: pickup free / door 29.90 ₪ / 1–3 + 7–14 = 8–17 business days / warehouses outside Israel / "אין בכך לגרוע מזכויות הלקוח לפי דין". "באחריות הלקוח להזין שם, טלפון וכתובת" is a responsibility clause, not a warranty. Cancellation terms (14 days, 5 % / 100 ₪) are **not** on this page — it defers to "מדיניות ההחזרים" without a link. WhatsApp is not mentioned (only mail + contact form).

### 1.4 Worth keeping
- The body copy itself (admin: Settings → Policies → Shipping; Liquid `shop.shipping_policy.body/.title/.url`): dated, lawful, consistent numbers, plain Hebrew. Do not rewrite the substance.
- The h3 skeleton (8 headings) — ready-made anchors for a generated TOC / side rail.
- The bold facts inside bullets ("חינם", "29.90 ₪", "1–3", "7–14", "8–17") — liftable into the homepage's glow-numeral ledger device (`env2_terms` "ארבעה מספרים שכדאי לדעת").
- Footer group as configured (`sections/footer-group.json`, `scheme-env2-night`) — already right.
- Header group config (`sections/header-group.json`: logo, split menu, icons) — right, only its ground is wrong on this template.
- Liquid lever: `layout/theme.liquid` (`theme/layout/theme.liquid` + `theme.liquid.patch.md` are in the repo) can branch on `request.page_type == 'policy'`, read all four `shop.*_policy` objects, and render content before/after `{{ content_for_layout }}`; CSS can target `.shopify-policy__container/__title/__body .rte`.

### 1.5 Verdict
"This is the beige nineties page again — I can't even see my menu — and it tells the customer everything except where to buy."

---

## 2. policy-refund — `/policies/refund-policy` — "מדיניות החזרים – ElmsNest"

**Page height:** desktop 2258 px, mobile 3167 px. 411 words, h1 ×1, h2 ×1, h3 ×8.

### 2.1 What renders
Desktop:
1. Same invisible header + glow "0".
2. `h1` "מדיניות החזרים" centred.
3. `h2` "מדיניות ביטולים, החזרות והחזרים" (different wording from the h1) → bold "עודכן לאחרונה: 5 באוגוסט 2026" → intro "מדיניות זו נועדה להסביר בצורה ברורה כיצד ניתן לבטל עסקה או לדווח על מוצר פגום. הוראות חוק הגנת הצרכן והדין המחייב גוברות בכל מקרה של סתירה."
4. `h3` "איך מבקשים לבטל עסקה": "ניתן למסור הודעת ביטול באמצעות:" + bullets דוא"ל / "טופס יצירת קשר: https://elmsnest.com/pages/contact-us" + "כדי שנוכל לאתר את העסקה במהירות, מומלץ לציין שם מלא, מספר הזמנה ופרטי קשר…"
5. `h3` "תקופת הביטול": "…עד 14 ימים ממועד קבלת המוצר או ממועד קבלת מסמך הגילוי, לפי המאוחר." + extended 4-month window for disabled / senior / new-immigrant consumers.
6. `h3` "דמי ביטול והחזר כספי": "דמי הביטול יהיו בשיעור של 5% ממחיר העסקה או 100 ₪ — הנמוך מביניהם." / no fee for defect / refund within 14 days of the notice.
7. `h3` "החזרת המוצר" (3 paragraphs) → `h3` "מוצר פגום, חסר או שגוי" → `h3` "חריגים" → `h3` "החלפות" → `h3` "יצירת קשר" (דוא"ל + "טופס: https://elmsnest.com/pages/contact-us").
8. Hard cut to the night footer at y≈1880.
Mobile: h2 wraps to 3 lines ("מדיניות ביטולים, החזרות / והחזרים"); **fold** = h1, h2, date, intro, "איך מבקשים לבטל עסקה", the two contact bullets and the start of "תקופת הביטול" ("…ועד 14 ימים ממועד") — the 14 days just make it into the fold, the 5 % / 100 ₪ rule is at ~1.5 screens. On mobile the contact-form URL sits on its own line (no mid-token wrap here).

### 2.2 Against the design system
- All of §0 (cream/brown ground, Assistant, invisible header, ≈1410 px measure, hard footer cut, brown back-to-top ring).
- h1/h2 pair with two different titles ("מדיניות החזרים" vs "מדיניות ביטולים, החזרות והחזרים") — the page names itself twice, differently.
- The two consumer numbers that matter (14 days; 5 % or 100 ₪) are inline bold fragments in paragraphs 4–6 of a 411-word wall; nothing sets them apart (the homepage renders the same numbers as 60 px glow numerals).
- Default document patterns as in §1.2; underlined dark links; printed raw URL.
- Long one-column text with no hairlines, no TOC, no rail; nothing to look at for 3167 mobile px.
- No link to the shipping policy it refers to ("בהתאם למדיניות המשלוחים" is plain text), no link to the contact-us page other than the raw URL, no "send a photo" path.

### 2.3 Honesty check
Clean. No fabricated patterns. "מומלץ להחזיר את המוצר עם כל האביזרים ובאריזתו, ככל שניתן" is advice, not a condition. Liability language ("ElmsNest תישא באחריות להחזרת המוצר ככל שנדרש לפי דין") is legal, not a warranty promise. The approved cancellation facts are all present and correctly worded. WhatsApp: absent.

### 2.4 Worth keeping
- The full text (admin: Settings → Policies → Refund; `shop.refund_policy`): the most consumer-protective copy in the store — keep verbatim.
- The 14 / 5 % / 100 ₪ / "לפי המאוחר" facts as a ledger triplet.
- The 8-heading skeleton for anchors.
- Footer/header groups as in §1.4; the same `theme.liquid` lever.

### 2.5 Verdict
"A lawyer's page in beige; the one thing a buyer wants to know — can I cancel and what does it cost — is buried in paragraph five."

---

## 3. policy-terms — `/policies/terms-of-service` — "תנאי שימוש – ElmsNest"

**Page height:** desktop 2605 px, mobile 3521 px (tallest of the four). 496 words, h1 ×1, h2 ×1, h3 ×13.

### 3.1 What renders
Desktop:
1. Invisible header + glow "0".
2. `h1` "תנאי שימוש" centred.
3. `h2` "תנאי שימוש ורכישה" → bold date → intro "ברוכים הבאים ל-ElmsNest. תנאים אלה חלים על הגלישה באתר elmsnest.com ועל רכישת מוצרים בו…"
4. 13 `h3` sections in this order: "כשירות ושימוש באתר" → "מוצרים ותיאורים" ("ייתכנו הבדלים קלים הנובעים מתצוגת המסך… כאשר עמידות למים או תקן אחר מצוינים, יש לפעול לפי הוראות המוצר") → "מחירים ותשלום" ("המחירים מוצגים בשקלים חדשים…") → "ביצוע וקבלת הזמנה" → "משלוחים" (repeats 1–3 / 7–14 / 8–17 / pickup free / 29.90 ₪ and **links** "מדיניות המשלוחים") → "ביטולים, החזרות והחזרים" (**links** "מדיניות הביטולים וההחזרים") → "מוצר פגום או אי-התאמה" → "אחריות ושימוש בטוח" ("אין לבצע התקנה חשמלית קבועה ללא בעל מקצוע מוסמך…") → "קניין רוחני" → "פרטיות ועוגיות" (**links** "מדיניות הפרטיות") → "זמינות ושינויים באתר" → "דין חל" ("…יחולו דיני מדינת ישראל") → "יצירת קשר".
5. Hard cut to the night footer at y≈2220.
Mobile: **fold** = h1, h2, date, intro, "כשירות ושימוש באתר" paragraph, "מוצרים ותיאורים" heading — no consumer number in the fold. The contact URL wraps "contact-" / "us" at the end. 3521 px of cream before the footer.

### 3.2 Against the design system
- All of §0.
- 13 headings, 496 words, one column, one weight of grey-brown — the longest unbroken wall in the family; no TOC, no numbering, no hairlines.
- h1 "תנאי שימוש" + h2 "תנאי שימוש ורכישה" duplicate.
- Three inline links (to the other policies) are the only navigation in the whole family and are styled as underlined body links indistinguishable from the raw URL at the bottom.
- The Latin "elmsnest.com", "ElmsNest" tokens sit unprotected in RTL sentences ("ברוכים הבאים ל-ElmsNest" renders fine; not `<bdi>`-wrapped).
- Everything else as §1.2 (measure, header, footer cut, brown ring).

### 3.3 Honesty check
Clean. "אחריות ElmsNest תחול בהתאם לדין ולכל התחייבות מפורשת שנמסרה לגבי המוצר. איננו מגבילים אחריות במקום שבו הדין אינו מאפשר זאת." is a liability clause consistent with the store rule of not authoring warranty promises (cf. `elmsnest-pdp-trust.liquid` comment). No comparison, no counts, no urgency.

### 3.4 Worth keeping
- The cross-links to the other three policies (`/policies/shipping-policy`, `/policies/refund-policy`, `/policies/privacy-policy`) — the seed of a "four documents" nav.
- The "משלוחים" and "ביטולים" summary paragraphs — a ready one-line digest of each policy.
- The safety line "אין לבצע התקנה חשמלית קבועה ללא בעל מקצוע מוסמך" (matches the PDP installation note) — true, useful, keep findable.
- Body from `shop.terms_of_service`; header/footer groups; `theme.liquid` lever.

### 3.5 Verdict
"Five hundred words of beige legal text with no way in and no way out — nobody will read it, and it looks like the old site."

---

## 4. policy-privacy — `/policies/privacy-policy` — "מדיניות הפרטיות – ElmsNest"

**Page height:** desktop 2366 px, mobile 3279 px. 424 words, h1 ×1, h2 ×1, h3 ×10.

### 4.1 What renders
Desktop:
1. Invisible header + glow "0".
2. `h1` "מדיניות הפרטיות" centred.
3. `h2` "מדיניות פרטיות" (drops the ה) → bold date → intro "ElmsNest מכבדת את פרטיות המשתמשים והלקוחות… השימוש באתר כפוף לחוק הגנת הפרטיות, התשמ"א–1981…"
4. `h3` "המידע שאנו עשויים לאסוף" + 5 bullets (contact details / order details / payment "מעובדים על ידי ספקי התשלום ואינם מוצגים לנו במלואם" / technical data "כתובת IP, סוג דפדפן ומכשיר" / marketing consent) → `h3` "מטרות השימוש במידע" → `h3` "מסירת מידע וספקי שירות" ("החנות פועלת על גבי Shopify… לרבות Google") → `h3` "העברת מידע מחוץ לישראל" → `h3` "עוגיות וטכנולוגיות דומות" → `h3` "שמירת מידע ואבטחה" ("אין מערכת המאובטחת באופן מוחלט") → `h3` "זכויות ובקשות" → `h3` "מידע על אחרים וקטינים" → `h3` "שינויים במדיניות" → `h3` "יצירת קשר בנושא פרטיות" (mail + raw URL).
5. Hard cut to the night footer at y≈2000.
Mobile: **fold** = h1, h2, date, intro, "המידע שאנו עשויים לאסוף" heading + all 5 bullets + "מטרות השימוש" heading. URL wraps "contact-" / "us".

### 4.2 Against the design system
- All of §0.
- h1/h2 near-duplicate ("מדיניות הפרטיות" / "מדיניות פרטיות") — looks like a typo, not a design.
- Latin tokens "Shopify", "Google", "IP" inline in RTL paragraphs, unprotected; the line "החנות פועלת על גבי Shopify. מידע עשוי להימסר… ל-Shopify, לספקי תשלום…" is the one place where mixed-direction punctuation visibly jitters on mobile (crop 2, ",Shopify-ל").
- Otherwise identical failings: cream/brown, Assistant, invisible header, 1410 px measure, disc bullets, dark underlined links, hard footer cut, brown ring, no TOC/rail, dead end.

### 4.3 Honesty check
Clean. States the limits honestly ("אינם מוצגים לנו במלואם", "אין מערכת המאובטחת באופן מוחלט"). No marketing claims at all. No cookie banner exists (`cookies` section DISABLED in `system-group.json`) — the policy describes cookies the site sets without any consent UI; not a fabrication, but a designer should know there is no banner to style.

### 4.4 Worth keeping
- Body from `shop.privacy_policy` — required by law and by Shopify; keep verbatim.
- The 10-heading skeleton for anchors.
- Header/footer groups; `theme.liquid` lever.

### 4.5 Verdict
"Fine as a document, wrong as a page: same beige, same invisible menu, same wall — it just has to stop looking like a different website."

---

## 5. home — reference render (NOT audited)

**Page height:** desktop 8573 px, mobile 8698 px. `env2 base loaded: True · FRL font loaded: True`. h1 "כשהשמש יורדת, הגינה נדלקת.", 6 h2, 9 product h3, 17 `[data-lamp]` elements, 3 add-to-cart forms, 23 images. Sections: `env2_hero → env2_first_lit → env2_places → env2_switch → env2_night_wall → env2_atmosphere → env2_terms → env2_goodnight` then the night footer.

What it looks like in these static shots (baseline for the merge):
1. One continuous sky: the hero's dusk-garden photo fades at its bottom edge into a blue `#4a6a9c`-ish band, which darkens through navy behind "מה שנדלק ראשון" and "ארבעה מקומות" (~`#1f3357`), to near-black behind the divider stage and the wall lamp (`#0f1a2f`/`#070b15`), to `#020306` at the ledger, goodnight and footer; faint stars appear from the "מתי לא" section down. No section has its own background.
2. Header is transparent over the hero photo and fully legible there (ink nav "דף הבית · קולקציות · מדריך לבחירה | logo | שאלות נפוצות · מי אנחנו · יצירת קשר", search right, cart + glow "0" badge left) — the same header that is invisible on the policy pages.
3. Type: Frank Ruhl Libre 900 headlines at ~120 px desktop / ~64 px mobile, line-height ≈1, last line in glow `#ffd394` ("הגינה נדלקת.", "גם מתי **לא**.", "קיר אחד מספיק."); gold kickers with a short gold rule ("01 · נדלקים עכשיו", "02 · לפני שקונים", "03 · הלילה", "04 · מרפסת ופינת ישיבה", "05 · לפני שמזמינים"); Heebo 300/400 body in ink-2; product titles in Heebo, never serif; prices in glow ("169.90 ₪", "159.90–162.90 ₪", "219.90–252.90 ₪").
4. Hero: full-bleed bollard photo, h1, lede, two pills (glow-filled "לארבע הקולקציות", outlined "לשלוח תמונה של המקום"), a scrim card "המנורה שבתמונה · שביל" with title / 169.90 ₪ / pill "הוספה לסל", a vertical **sun-rail** on the left ("שקיעה" → "לילה" with a tracking dot) and a small note "השעה הכחולה". Buy is inside both folds.
5. "מה שנדלק ראשון": a tall wall-lamp photo with a scrim caption card, and three loose product tiles (photo · kicker "שביל · לראות את הדרך" · title · price · pill) with no boxes — each tile composed differently from its neighbour.
6. "ארבעה מקומות. קטגוריה אחת.": the **staircase** — four photos stepping up 4→1 with 100 px glow numerals, captions "שביל 8 מוצרים / קיר 6 / גינה 6 / מרפסת 7", "לכל 27 המוצרים ←". Mobile turns it into a 2×2 stepped grid plus "01 שביל · 02 קיר · 03 גינה · 04 מרפסת" tabs.
7. "אנחנו נגיד לכם גם מתי לא.": the **divider stage** — unlit vs lit bollard with a ‹ › knob, labels "מתאים כדי / לראות את הדרך" and "לא מתאים כש־ / המקום כמעט אינו מקבל אור יום", a 4-row hairline list with a lit dot on the active row and a "דולק · כבוי" legend, then the «מי אנחנו» quote «"כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה."» and "למדריך המלא ←".
8. "הלילה כבר כאן. קיר אחד מספיק.": full-bleed dark wall-lamp photo, spec line (צבע גוף · עוצמה 6W/12W · גוון 3000K/6000K), price range, pill "לבחירת הספק", cross-sell line "גם לקיר: … 159.90 ₪ ←".
9. "אווירה": the word cut out of a bokeh photo, a real SVG string-light garland with three product photos hanging from it (89.90 ₪ each, "לבחירת אורך ←"), closing hairline "27 מוצרים · 69.90–999.90 ₪ · לכל המוצרים, לפי מקום ←".
10. "ארבעה מספרים שכדאי לדעת": the **hairline ledger** — four rows, glow numerals "0 ₪ / 8–17 ימי עסקים / 14 יום / 1 תמונה", Heebo explanations (pickup free · 29.90 door; 1–3 + 7–14, "חלק מהמוצרים נשלחים ממחסנים מחוץ לישראל — ולכן אנחנו כותבים את זה כאן, ולא מגלים אחרי"; 14 days, 5 % or 100 ₪; send a photo), a row of underlined links (משלוחים ואספקה · זמני טיפול · שאלות נפוצות · למה תאורה סולארית). Then the goodnight: "שלחו תמונה של המקום — נבדוק התאמה לפני ההזמנה." + pill + TikTok/Instagram rings, a garden-party photo with outlined serif "לילה טוב" and a one-line terms strip "משלוח חינם לנקודת איסוף · 8–17 ימי עסקים · ביטול תוך 14 יום לפי חוק הגנת הצרכן · לתנאים המלאים ←".

Devices visible in the static shots: **sky gradient ✔ · serif display type ✔ · hairline ledger ✔ · staircase ✔ · divider stage ✔ (knob, before/after, active-row dot) · lamps lighting — end state only** (every lamp is already lit in the full-page capture; the dim→lit transition cannot be seen in a static shot) · also visible: sun-rail, stars, scrim cards, cut-out "אווירה" letters, garland with hanging products, outlined "לילה טוב", glow prices, pill buttons, gold kickers/rules.

---

## 6. Family summary

### The 5 facts a designer must know before briefing this family
1. **There is no template to design.** The four policies are Shopify's fixed `policy` template: `h1` + `.rte` HTML typed in Settings → Policies. The only levers are `layout/theme.liquid` (guard on `request.page_type == 'policy'`; objects `shop.shipping_policy`, `shop.refund_policy`, `shop.privacy_policy`, `shop.terms_of_service` with `.title / .url / .body`, plus `page_title` and `request.path`) — which may inject markup **before and after** `{{ content_for_layout }}` but not inside it — and global CSS on `.shopify-policy__container / __title / __body .rte`. The body HTML is limited to `h2 / p / strong / h3 / ul li / a / br`; no classes, no anchors, no images — any TOC, numbering, ledger or anchor rail must be generated by CSS counters/JS from the h3s, or rendered from `theme.liquid` around the body.
2. **Today they are the old site.** Body scheme `scheme-1` = `#2b2118` on `#f7f0e6`, Assistant 600/400 everywhere, ≈1410 px measure at 1440 (Kalles overrides Shopify's 65ch), duplicate h1/h2 titles on all four, hard cream→`#020306` cut into the night footer, brown back-to-top ring. Heights 2070 / 2258 / 2605 / 2366 desktop, 2728 / 3167 / 3521 / 3279 mobile; 290 / 411 / 496 / 424 words; 8 / 8 / 13 / 10 h3s.
3. **The header is broken on every non-night page.** `header-group.json` is transparent (`background_opacity_transparent: 0`, `enabled-transparent-header` on every page) with `scheme-env2-night` ink — invisible on cream (measured contrast ≈1.03:1). Any side-page ground must be dark enough for the night header, or the transparent state must be scoped to the index. The glow "0" cart badge is the only visible header element besides the logo.
4. **The content is honest, consistent and already duplicated.** All four are dated "5 באוגוסט 2026"; the numbers (free pickup / 29.90 ₪; 1–3 + 7–14 = 8–17; warehouses outside Israel; 14 days; 5 % or 100 ₪; extended 4-month window; "לפי המאוחר") match the homepage ledger and the PDP snippets exactly. The same facts also live in `/pages/shipping-delivery`, `/pages/processing-time`, `/#env2-terms` and the PDP `elmsnest-pdp-facts/trust` snippets. Footer "מידע" links go to the **page** versions; only the copyright line (→ `/#env2-terms`), the terms policy, and PDP snippets (→ `/policies/shipping-policy`, `/policies/refund-policy`) reach the policies. Nothing links between the four policies except terms → the other three. "Send a photo on WhatsApp" appears in no policy (only mail + a raw `contact-us` URL that wraps mid-token on mobile).
5. **No buy anywhere, and no fold sells.** Zero product cards, zero forms, zero prices except the shipping fee; every fold is h1 → h2 → date → intro → first h3. The homepage already proves the device that fits here: the `env2_terms` ledger (glow numerals + hairlines + underlined links) and the one-line terms strip in `env2_goodnight` — the policies are the "לתנאים המלאים ←" destination and should look like where that link lands.

### The 3 hardest technical constraints visible
1. **Locked markup + admin-owned HTML.** `.shopify-policy__container > .shopify-policy__title h1 + .shopify-policy__body .rte` cannot be altered; Kalles' `!important` width override and Shopify's centred-title CSS must be beaten by specificity in `theme.liquid`; the `.rte` gets `hdt-rte` added by Kalles JS after load (no rules today, but Kalles typography for `.rte`/`blockquote` — cream `blockquote` panel — applies); the Sense RTL app flips physical properties, so everything must be logical-property CSS.
2. **Global header/footer/system groups, JS-driven.** `hdt-sticky-header` (`sticky_type: on_scroll_up`, transparent-with-opacity-0, `scheme-env2-night`), `<hdt-cart-drawer>` (opens on the glow "0"), `<back-to-top>` with its brown progress ring, and the `enabled-transparent-header` attribute are all set once for every template; fixing the policy header means either a page-type-scoped scheme/opacity override in `theme.liquid` or a dark ground under it — and the v2 gradient/base currently targets `body.hdt-page-type-index` only (`elmsnest-v2-base.liquid` l.25–39; HANDOFF §3 says split it into a global core + per-template ground).
3. **Fonts and tokens are not on this template.** `elmsnest-v2-fonts` / `-base` are rendered by the homepage hero section, so Frank Ruhl Libre, Heebo, `--env2` tokens, pills, hairlines and `window.env2` do not exist on `/policies/*`; the page falls back to Kalles' Assistant + `--f_family_*` + `css-variables` scheme colours. Everything the merge wants here (serif titles, glow numerals, ledger, lamps) has to be loaded from `layout/theme.liquid` for `page_type == 'policy'` — and with no images or sections available, "one idea only a lighting store could have" must come from type, hairlines, numerals and the header/footer photo-less sky alone.
