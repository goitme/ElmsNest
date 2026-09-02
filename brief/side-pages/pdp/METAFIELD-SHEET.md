# PDP metafield sheet — 27 products (for owner approval before any Shopify write)

Generated 2026-09-02 from the saved Admin GraphQL result (all 27 active products: title, options, descriptionHtml, metafields). Rules: every value is quoted from the product's own description / option values / title; nothing is inferred; image-only claims are never used; `not_fit_for` may only be one of the four BRIEF §3 clauses, verbatim, and only where it is literally true for the product. Machine-readable twin: `metafields.json` (same folder). **Nothing has been written to Shopify.**

## Summary

1. Products: 27. Spec fields filled (of 27): ip_rating 17 · charge_time_hours 4 · light_hours 10 · color_temp 21 · sensor_range_m 2 · sensor_angle_deg 2 · material 9 · dimensions 7 · power_watt 5 · lumens 2 · battery 4 · light_modes 5.
2. power_source (proposed new definition) known for 24/27; "לא צוין" on 3: modern-led-wall-light-6w-up-down, waterproof-led-wall-light-ip65-6w-12w, outdoor-bidirectional-led-wall-light-ip65.
3. direct_answer 27/27 · faq 27/27 · not_fit_for 20/27 · home_card_line 12/27 (existing values only, none invented).
4. Spec fields empty everywhere: none. Rarest: sensor_range_m (2), sensor_angle_deg (2), lumens (2), charge_time_hours (4).
5. not_fit_for left EMPTY on 7 products because no approved clause is literally true (mains / unknown power / portable): modern-led-wall-light-6w-up-down, modern-led-wall-light-indoor-outdoor, waterproof-led-wall-light-ip65-6w-12w, outdoor-bidirectional-led-wall-light-ip65, modern-led-bollard-light-5w-ip65, rechargeable-telescopic-camping-lantern, dual-head-garden-light-10w-ip65.
6. not_fit_for filled by judgment (owner to confirm): magnetic-rechargeable-touch-wall-light (pair 2, indoor), lighted-birch-branches-20-led (pair 3, indoor), solar-floodlight-ip67-remote-timer (pair 2; pair 4 also true), solar-firefly-garden-lights (pair 3; pair 4 also true).
7. Products with NO numeric spec at all in their description: powerful-solar-garden-light — every spec field empty; the title "עוצמתית" is unbacked.
8. Products whose description holds no `.elms-sales` "פרטים שכדאי לדעת" bullet list (older plain format with a "פרטים טכניים" line instead): modern-led-bollard-light-5w-ip65, rechargeable-telescopic-camping-lantern, swaying-solar-path-lights-ip65, powerful-solar-garden-light, dual-head-garden-light-10w-ip65.
9. Bullets present but qualitative only (no hours / IP / battery numbers): retro-solar-path-lights-set (IP65 only), warm-solar-step-deck-lights (no IP, no numbers), solar-garden-lantern-9-led (IP65 only).
10. Outdoor products with NO IP rating in the text: warm-solar-step-deck-lights, decorative-led-net-lights (220V!), solar-edison-string-lights, powerful-solar-garden-light, modern-led-wall-light-indoor-outdoor (aluminium "עמיד למים" without a number), rechargeable-telescopic-camping-lantern ("עמידות למים לשימוש יומיומי").
11. Contradictions (details in each section):
    - rechargeable-telescopic-camping-lantern — title "360°" vs images[0] "270°"; description silent
    - swaying-solar-path-lights-ip65 — description "עד כ־12 שעות" vs images[0] "עד 14 שעות" (+ "50,000 שעות", "+30%")
    - modern-led-bollard-light-5w-ip65 — description "אחריות יצרן: שנתיים" vs images[0] "שנה אחריות" + third-party LUMIÈRE mark; mains lamp in the solar path collection
    - solar-floodlight-ip67-remote-timer — images[0] badge "זמין בסט של 4 או 8 יחידות" vs single-unit 72/128/200 LED variants; option wattages 100/200/300W not in the description
    - modern-led-wall-light-indoor-outdoor — option "ABS – לא עמיד למים" vs "אלומיניום – עמיד למים" (no product-level waterproof claim possible); wired lamp tagged "תאורת קיר סולארית"
    - modern-led-wall-light-6w-up-down — indoor "לשימוש פנימי באזור יבש", power source unstated, yet in solar-wall-lights + tag "תאורת קיר סולארית"
    - waterproof-led-wall-light-ip65-6w-12w · outdoor-bidirectional-led-wall-light-ip65 · magnetic-rechargeable-touch-wall-light — tagged "תאורת קיר סולארית" / in solar-wall-lights with no solar wording (two have no stated power source; one is USB-rechargeable indoor)
    - dual-head-garden-light-10w-ip65 — mains (AC 85–265V) in the solar spotlights collection
12. Specs that exist ONLY as image pixels (verified by viewing the featured images): stainless-steel-solar-path-light-ip65 dimensions (43 ס״מ, Ø6, panel 4 ס״מ on images[2]); solar-garden-spotlight-52-led "-20° עד 60°C"; warm-solar-step-deck-lights "ABS + אלומיניום, עדשת זכוכית, עמידות למים"; retro set "עמיד לחום/לחורף"; magnetic wall light "הדבקה ללא קידוח"; swaying lights "עד 14 שעות / 50,000 שעות / +30%". None used.
13. Reference product solar-wall-light-motion-sensor-ip65: live values kept verbatim (its not_fit_for is a 3-sentence owner text, not one of the four pairs; its faq includes two policy answers). Writing metafields.json changes nothing on it.
14. Owner-banned or unverifiable wording found in descriptions and deliberately NOT mapped: "אחריות יצרן: שנתיים" (bollard, dual-head), "תקן CE", "CE, RoHS, UL, FCC, LVD" (swaying), supplier SKU tag "YN-PL3-BS" (stainless).
15. Before the write step the owner must decide: (a) power_source for the 3 "לא צוין" products; (b) whether 100/200/300W option labels on the floodlight are real; (c) whether the 4 judgment not_fit_for values stay; (d) whether to add the four wired/indoor products' honest restrictions ("לשימוש פנימי באזור יבש") as a 5th approved pair.

### The four approved pairs (BRIEF §3) — the only `not_fit_for` texts allowed

| # | place | suits | does NOT suit (clause written to `not_fit_for`) |
|---|-------|-------|--------------------------------------------------|
| 1 | שביל, מדרגות ומעברים | לראות את הדרך | המקום כמעט אינו מקבל אור יום |
| 2 | כניסה, קיר וחזית | להאיר נקודה מסוימת | נדרש אור חזק וקבוע לאורך כל הלילה |
| 3 | מרפסת ופינת ישיבה | ליצור אווירה | צריך אור חזק — זו אינה מטרתה |
| 4 | הדגשת אזור בגינה | הארה ממוקדת של עץ או ערוגה | נדרשת התקנה מיוחדת או חיבור קבוע |

---

## 01. `waterproof-solar-deck-step-lights`

**תאורה סולארית עמידה למים לדק ולמדרגות** · collection: path · תאורת-שביל-סולארית (שביל) + sale · variants 4 · ₪149.9–149.9

Options: כמות: 2 'יח / 4 'יח / 6 'יח / 8 'יח

**power_source (proposed):** סולארי  — source: כל יחידה נטענת מהשמש ופועלת באופן עצמאי, כך שההתקנה נשארת נקייה.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours | עד כ־10 שעות, בהתאם לטעינה | • עד כ־10 שעות תאורה בהתאם לטעינה |
| color_temp | גוון חם 3000K | • גוון אור חם 3000K |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery | 800mAh | • סוללה 800mAh |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 24 נורות LED בכל יחידה · התקנה באמצעות מדבקות חזקות או ברגים

**direct_answer** (15 words): תאורת מדרגות סולארית שמוסיפה פס אור חם לכל מדרגה, דק או שביל — בלי כבלים גלויים.

**not_fit_for** (pair 1 · שביל, מדרגות ומעברים): המקום כמעט אינו מקבל אור יום
  Why: שביל/מדרגות; מוצר סולארי (״כל יחידה נטענת מהשמש״) — הסעיף נכון מילולית.

**faq**:
- Q: כמה שעות התאורה פועלת?  
  A: עד כ־10 שעות תאורה בהתאם לטעינה.  
  source: «• עד כ־10 שעות תאורה בהתאם לטעינה»
- Q: איך מתקינים?  
  A: התקנה באמצעות מדבקות חזקות או ברגים.  
  source: «• התקנה באמצעות מדבקות חזקות או ברגים»
- Q: צריך להדליק בכל ערב?  
  A: במהלך היום הסוללה נטענת. כשמחשיך, התאורה נדלקת אוטומטית — בלי לזכור להפעיל ובלי לרוץ לכבות בבוקר.  
  source: «במהלך היום הסוללה נטענת. כשמחשיך, התאורה נדלקת אוטומטית — בלי לזכור להפעיל ובלי לרוץ לכבות בבוקר.»
- Q: האם עמידה בגשם?  
  A: עמידות IP65.  
  source: «• עמידות IP65»

**home_card_line:** (empty — none exists)

**Flags:**
- images[0] is a baked creative ("האירו את המדרגות בשתי דרכים", "2 אפשרויות התקנה — בצד או במרכז", "עמידות במים IP65"); IP65 matches the description, the "בצד או במרכז" placement claim exists only as image pixels — not used.
- No charge time, LED count has no metafield (24 LED per unit stays in the description only).
- Product sits in the `sale` collection with a compare-at price (owner decided 2026-09-02 to clear it) — not a metafield matter, noted for completeness.

---

## 02. `solar-garden-lantern-9-led`

**פנס סולארי לגינה 9 LED | עמיד למים ומתכוונן** · collection: spot · ספוטים-ופרוז-קטורים-סולאריים (גינה) · variants 1 · ₪169.9–169.9

**power_source (proposed):** סולארי  — source: מכוונים גם את הפאנל לאזור מואר ביום, כדי לנצל טוב יותר את הטעינה הסולארית.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp |  |  |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 9 נורות LED · ראש תאורה מתכוונן · פאנל סולארי מתכוונן · התקנה ללא חיבור לחשמל

**direct_answer** (16 words): ספוט סולארי מתכוונן שהופך עץ, עציץ, קיר אבן או שביל חשוך לנקודת עניין — בלי תשתית חשמל.

**not_fit_for** (pair 4 · הדגשת אזור בגינה): נדרשת התקנה מיוחדת או חיבור קבוע
  Why: הדגשת אזור בגינה (״לעצים, שיחים, ערוגות, פסלים״); סולארי ללא חיווט קבוע — הסעיף נכון מילולית.

**faq**:
- Q: אפשר לכוון את האור?  
  A: הראש המתכוונן מאפשר להפנות את האור אל האלמנט שרוצים להדגיש, במקום להאיר שטח לא רלוונטי.  
  source: «הראש המתכוונן מאפשר להפנות את האור אל האלמנט שרוצים להדגיש, במקום להאיר שטח לא רלוונטי.»
- Q: נדלק לבד?  
  A: התאורה פועלת אוטומטית עם החשכה.  
  source: «לא צריך לצאת החוצה בכל ערב — התאורה פועלת אוטומטית עם החשכה.»
- Q: אפשר להזיז אחרי ההתקנה?  
  A: אין חיווט קבוע, לכן אפשר לשנות את מיקום הספוט כאשר מסדרים מחדש את הגינה.  
  source: «אין חיווט קבוע, לכן אפשר לשנות את מיקום הספוט כאשר מסדרים מחדש את הגינה.»
- Q: איפה למקם את הפאנל?  
  A: מכוונים גם את הפאנל לאזור מואר ביום, כדי לנצל טוב יותר את הטעינה הסולארית.  
  source: «מכוונים גם את הפאנל לאזור מואר ביום, כדי לנצל טוב יותר את הטעינה הסולארית.»

**home_card_line:** 9 נורות LED · ראש תאורה מתכוונן · עמידות IP65

**Flags:**
- No light hours, charge time, lumens or battery anywhere in the description — all left empty.
- images[0] is a baked creative ("תאורה סולארית לגינה", "טעינה אוטומטית ביום", "תאורה אוטומטית בלילה") — no numbers, nothing to reconcile.
- Title says "עמיד למים"; description states IP65 — consistent.

---

## 03. `solar-wall-light-motion-sensor-ip65`

**מנורת קיר סולארית LED עם חיישן תנועה – עמידה למים IP65** · collection: wall · solar-wall-lights (קיר) · variants 4 · ₪129.9–159.9

Options: צבע: לבן / שחור; כמות: 1 'יח / 2 'יח

**power_source (proposed):** סולארי  — source: הטעינה הסולארית מאפשרת להתקין במקומות שבהם אין נקודת חשמל זמינה.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | גוון חם | • תאורת LED בגוון חם |
| sensor_range_m | עד כ־6 מטרים | • טווח זיהוי עד כ־6 מטרים |
| sensor_angle_deg | 120° | • זווית זיהוי 120° |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes | 3 | • 3 מצבי תאורה |

Stated facts with no matching metafield (stay in the description): חיישן תנועה PIR · בחירה בין שחור ללבן

**direct_answer** (existing, unchanged): מנורת קיר סולארית עם חיישן תנועה PIR — לכניסה, לחצר, לגדר ולמעברים צדדיים. האור החם נדלק כשמתקרבים, ללא תשתית חשמל. מתאימה לקיר שמקבל שמש ישירה במהלך היום.

**not_fit_for** (existing, unchanged — not one of the four pairs): מנורה סולארית תלויה באור שמש ישיר. היא לא תמיד מחליפה תאורה חשמלית חזקה, ובחורף הביצועים עשויים להיות חלשים יותר. אם הקיר או הכניסה שלכם מוצלים רוב היום — כדאי לשקול חלופה עם חיבור לחשמל.
  Note: הערך החי נשמר (ראו דגלים). אם הבעלים יעדיף את אחד מארבעת הזוגות: זוג 2 — ״נדרש אור חזק וקבוע לאורך כל הלילה״ (סולארי + חיישן).

**faq** (existing, unchanged):
- Q: מתי ההזמנה מגיעה?  
  A: הזמן הכולל המשוער ממועד ההזמנה הוא 8–17 ימי עסקים: 1–3 ימי טיפול ועוד 7–14 ימי משלוח. משלוח לנקודת איסוף בישראל — חינם; שליח עד הבית — 29.90 ₪.  
  source: live metafield (description + shipping/cancellation policy)
- Q: האם המנורה עמידה בגשם?  
  A: למנורה עמידות בתקן IP65 והיא מיועדת להתקנה חיצונית. אנחנו מסתמכים רק על נתונים שמפורסמים בעמוד — נתון שאינו מצוין כאן אינו מובטח.  
  source: live metafield (description + shipping/cancellation policy)
- Q: איך עובדים שלושת מצבי התאורה?  
  A: בוחרים מצב אחד: אור חזק בעת תנועה, אור חלש שמתחזק כשמתקרבים, או תאורה קבועה לאורך הלילה.  
  source: live metafield (description + shipping/cancellation policy)
- Q: אפשר לבטל את ההזמנה?  
  A: ניתן למסור הודעת ביטול עד 14 ימים ממועד קבלת המוצר, בהתאם למדיניות הביטולים וההחזרים.  
  source: live metafield (description + shipping/cancellation policy)

**home_card_line:** חיישן תנועה PIR · 3 מצבי תאורה · עמידות IP65

**Flags:**
- REFERENCE PRODUCT — the only one with live custom.* values. All spec values below equal the live ones; direct_answer / not_fit_for / faq are kept exactly as live (writing metafields.json is a no-op for this product).
- Live not_fit_for is a 3-sentence owner text, NOT one of the four BRIEF §3 pairs verbatim. If the owner wants uniformity, the matching pair is 2 ("נדרש אור חזק וקבוע לאורך כל הלילה"). Not changed here.
- Live faq contains two policy answers (8–17 business days, 29.90 ₪, 14-day cancellation) whose source is the shipping/cancellation policy, not the description — legitimate published facts, kept.
- No light hours, charge time or battery in the description — those fields stay empty (never filled live either).

---

## 04. `stainless-steel-solar-path-light-ip65`

**מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65** · collection: path · תאורת-שביל-סולארית (שביל) · variants 1 · ₪169.9–169.9

Options: צבע אור: צהוב חם

**power_source (proposed):** סולארי  — source: היא נטענת ביום, נדלקת לבד בלילה ויוצרת תחושת סדר בכל מעבר.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours | כ־6 שעות בממוצע | • טעינה ממוצעת כ־6 שעות |
| light_hours | כ־8–10 שעות | • זמן עבודה כ־8–10 שעות |
| color_temp | גוון צהוב חם | • גוון אור צהוב חם |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | נירוסטה | • גוף נירוסטה |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): נעיצה באדמה בעומק כ־5–10 ס״מ · לפני שימוש ראשון: מצב ON וטעינה של לפחות 3 שעות

**direct_answer** (14 words): מנורת שביל סולארית מנירוסטה — נטענת ביום, נדלקת לבד בלילה, לאורך שביל, מדשאה או כניסה.

**not_fit_for** (pair 1 · שביל, מדרגות ומעברים): המקום כמעט אינו מקבל אור יום
  Why: שביל; סולארי (״נטענת ביום, נדלקת לבד בלילה״) — הסעיף נכון מילולית.

**faq**:
- Q: כמה זמן היא מאירה?  
  A: לאחר טעינה טובה בשמש, התאורה יכולה לפעול כ־8–10 שעות בהתאם לתנאי הסביבה.  
  source: «לאחר טעינה טובה בשמש, התאורה יכולה לפעול כ־8–10 שעות בהתאם לתנאי הסביבה.»
- Q: איך מתקינים?  
  A: מרכיבים את היתד ונועצים באדמה — ללא חפירה, חיווט או חיבור לחשמל.  
  source: «מרכיבים את היתד ונועצים באדמה — ללא חפירה, חיווט או חיבור לחשמל.»
- Q: מה עושים לפני השימוש הראשון?  
  A: לפני שימוש ראשון: מצב ON וטעינה של לפחות 3 שעות.  
  source: «• לפני שימוש ראשון: מצב ON וטעינה של לפחות 3 שעות»
- Q: צריך להדליק ולכבות?  
  A: החיישן מדליק את המנורה בחושך ומכבה אותה בבוקר באופן אוטומטי.  
  source: «החיישן מדליק את המנורה בחושך ומכבה אותה בבוקר באופן אוטומטי.»

**home_card_line:** גוף נירוסטה · עמידות IP65 · זמן עבודה כ־8–10 שעות

**Flags:**
- DIMENSIONS EXIST ONLY AS IMAGE PIXELS: images[2] is a "מידות והתקנה" slide (height 43 ס״מ / 16.9″, tube Ø 6 ס״מ, panel 4 ס״מ, 4-step assembly). Not in the description → `dimensions` left empty; owner may add the numbers to the description first.
- Tag "YN-PL3-BS" is a supplier SKU visible on the storefront tag list.

---

## 05. `retro-solar-path-lights-set`

**סט מנורות שביל סולאריות רטרו באור חם – 2/4/6 יחידות** · collection: path · תאורת-שביל-סולארית (שביל) · variants 3 · ₪219.9–529.9

Options: כמות: 2 יחידות / 4 יחידות / 6 יחידות

**power_source (proposed):** סולארי  — source: • טעינה סולארית

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | גוון חם | • גוון אור חם |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): עיצוב נורת פילמנט רטרו · הדלקה אוטומטית בחושך · התקנה בנעיצה באדמה · סטים של 2, 4 או 6 יחידות

**direct_answer** (17 words): מנורות שביל סולאריות בעיצוב רטרו עם נורת פילמנט חמה — לאורך שביל, סביב ערוגה או ליד פינת הישיבה.

**not_fit_for** (pair 1 · שביל, מדרגות ומעברים): המקום כמעט אינו מקבל אור יום
  Why: שביל; סולארי (״כל מנורה נטענת מהשמש״) — הסעיף נכון מילולית.

**faq**:
- Q: צריך חיבור לחשמל?  
  A: כל מנורה נטענת מהשמש ופועלת באופן עצמאי, כך שנשאר רק לבחור את המיקום.  
  source: «כל מנורה נטענת מהשמש ופועלת באופן עצמאי, כך שנשאר רק לבחור את המיקום.»
- Q: איך מתקינים?  
  A: התקנה בנעיצה באדמה.  
  source: «• התקנה בנעיצה באדמה»
- Q: כמה יחידות לבחור?  
  A: סטים של 2, 4 או 6 יחידות מאפשרים ליצור קו קצר בכניסה או רצף מלא לאורך השביל.  
  source: «סטים של 2, 4 או 6 יחידות מאפשרים ליצור קו קצר בכניסה או רצף מלא לאורך השביל.»

**home_card_line:** טעינה סולארית · עמידות IP65 · סטים של 2, 4 או 6 יחידות

**Flags:**
- No light hours, charge time, battery or LED count in the description — the spec list is qualitative only.
- images[0] baked: "עמיד למים IP65" (consistent), "עמיד לחום", "עמיד לחורף" — the heat/winter claims exist only as image pixels; not used.

---

## 06. `warm-solar-step-deck-lights`

**מנורות סולאריות למדרגות ולדק באור חם – 1/4/8/12 יחידות** · collection: path · תאורת-שביל-סולארית (שביל) · variants 8 · ₪69.9–349.9

Options: כמות: 1 יחידה / 4 יחידות / 8 יחידות / 12 יחידות; צבע: שחור / חום

**power_source (proposed):** סולארי  — source: • תאורה סולארית בגוון חם

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | גוון חם | • תאורה סולארית בגוון חם |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): הדלקה אוטומטית בשעות החשכה · מתאימה למדרגות, דק, גדר ושביל · צבע שחור או חום · כמויות: 1, 4, 8 או 12 יחידות

**direct_answer** (14 words): מנורות סולאריות קומפקטיות באור חם למדרגות, לדק, לגדר ולשביל — בלי כבלים ובלי עבודת חשמל.

**not_fit_for** (pair 1 · שביל, מדרגות ומעברים): המקום כמעט אינו מקבל אור יום
  Why: מדרגות/דק/שביל; סולארי (״כל יחידה פועלת באופן עצמאי באמצעות השמש״) — הסעיף נכון מילולית.

**faq**:
- Q: צריך חשמלאי?  
  A: אין צורך להעביר כבלים או להוסיף שקעים. כל יחידה פועלת באופן עצמאי באמצעות השמש.  
  source: «אין צורך להעביר כבלים או להוסיף שקעים. כל יחידה פועלת באופן עצמאי באמצעות השמש.»
- Q: נדלקות לבד?  
  A: הדלקה אוטומטית בשעות החשכה.  
  source: «• הדלקה אוטומטית בשעות החשכה»
- Q: לאן האור מופנה?  
  A: התאורה מופנית כלפי מטה ומדגישה את אזור הדריכה בלי להציף את כל החצר באור מיותר.  
  source: «התאורה מופנית כלפי מטה ומדגישה את אזור הדריכה בלי להציף את כל החצר באור מיותר.»

**home_card_line:** (empty — none exists)

**Flags:**
- NO IP RATING, no hours, no battery, no material anywhere in title/description/tags — every numeric spec field is empty.
- SPEC EXISTS ONLY AS IMAGE PIXELS: images[0] ("תאורה סולארית אלגנטית למעקה") claims "עמידות למים", "ABS איכותי בשילוב אלומיניום", "עדשת זכוכית" — none of it is in the description; not used.

---

## 07. `modern-led-wall-light-6w-up-down`

**מנורת קיר LED מודרנית 6W עם תאורת Up & Down** · collection: wall · solar-wall-lights (קיר) · variants 8 · ₪109.9–193.9

Options: צבע גוף: לבן / שחור; גוון אור: אור חם 3000K / אור קר 6500K; כמות: יחידה אחת / זוג

**power_source (proposed):** לא צוין  — source: התיאור אינו מציין מקור מתח (לא סולארי, לא ״חיבור לחשמל״). ראו דגלים.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | אור חם 3000K או אור קר 6500K | • 3000K או 6500K (אפשרויות: ״אור חם 3000K״ / ״אור קר 6500K״) |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | אלומיניום | • גוף אלומיניום |
| dimensions |  |  |
| power_watt | 6W | • עוצמה 6W |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): תאורת Up & Down · שחור או לבן · יחידה אחת או זוג · לשימוש פנימי באזור יבש

**direct_answer** (18 words): מנורת קיר Up & Down בעוצמה 6W לשימוש פנימי — למסדרון, לסלון, לחדר השינה או לקיר שרוצים לתת לו נוכחות.

**not_fit_for:** EMPTY — מוצר פנימי (״לשימוש פנימי באזור יבש״) ומקור המתח לא צוין. סעיף זוג 2 (״נדרש אור חזק וקבוע לאורך כל הלילה״) אינו נכון מילולית למנורה שאינה סולארית; זוג 1 אינו רלוונטי. ההגבלה האמיתית — ״לשימוש פנימי באזור יבש״ — אינה אחד מארבעת הזוגות המאושרים, לכן השדה נשאר ריק.

**faq**:
- Q: מתאימה לחוץ?  
  A: לשימוש פנימי באזור יבש.  
  source: «• לשימוש פנימי באזור יבש»
- Q: איזה גוון לבחור?  
  A: אור חם 3000K מתאים לרוגע ואירוח; אור קר 6500K מעניק מראה בהיר וחד יותר.  
  source: «אור חם 3000K מתאים לרוגע ואירוח; אור קר 6500K מעניק מראה בהיר וחד יותר.»
- Q: יחידה אחת או זוג?  
  A: בחרו מנורה בודדת לנקודת עניין או זוג משני צידי מיטה, תמונה או מעבר.  
  source: «בחרו מנורה בודדת לנקודת עניין או זוג משני צידי מיטה, תמונה או מעבר.»

**home_card_line:** לשימוש פנימי באזור יבש

**Flags:**
- POWER SOURCE NOT STATED. A 6W indoor wall light is presumably mains-wired, but the description never says so — power_source = "לא צוין" until the owner confirms.
- CATALOGUE CONTRADICTION: an indoor, non-solar lamp (bullet "לשימוש פנימי באזור יבש") sits in collection `solar-wall-lights` and carries the tag "תאורת קיר סולארית".
- No IP rating (correct for an indoor product) — must not inherit any "עמיד למים" wording.

---

## 08. `modern-led-wall-light-indoor-outdoor`

**מנורת קיר LED מודרנית – גרסאות לפנים או לחוץ** · collection: wall · solar-wall-lights (קיר) · variants 8 · ₪99.9–121.9

Options: צבע גוף: לבן / שחור; סוג גוף: ABS – לא עמיד למים / אלומיניום – עמיד למים; גוון אור: אור חם 3000K / אור קר 6500K

**power_source (proposed):** חשמל 220V  — source: • חיבור קבוע לחשמל — המתח (220V) הוא תווית הקטגוריה, לא נתון מהתיאור.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | אור חם 3000K או אור קר 6500K | • אור חם 3000K או קר 6500K |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | ABS (גרסת פנים) או אלומיניום עמיד למים (גרסת חוץ) | • גרסת ABS לשימוש פנימי · • גרסת אלומיניום עמידה למים לחוץ |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): אפקט תאורה Up & Down · צבע שחור או לבן · חיבור קבוע לחשמל

**direct_answer** (15 words): מנורת קיר LED דו־כיוונית — גרסת ABS לחללים יבשים בפנים, גרסת אלומיניום עמידה למים לאזורי חוץ.

**not_fit_for:** EMPTY — מוצר בחיבור קבוע לחשמל: סעיף זוג 2 (״נדרש אור חזק וקבוע לאורך כל הלילה״) אינו נכון מילולית; זוגות 1/3/4 אינם רלוונטיים לקיר מחווט. ההגבלה האמיתית (״גרסת ABS מיועדת לפנים״) אינה אחד מארבעת הזוגות — השדה ריק.

**faq**:
- Q: איזו גרסה לבחור למרפסת?  
  A: לאזור חיצוני או חשוף ללחות בחרו בגרסת האלומיניום העמידה למים. לחלל פנימי ויבש אפשר לבחור בגרסת ABS.  
  source: «לאזור חיצוני או חשוף ללחות בחרו בגרסת האלומיניום העמידה למים. לחלל פנימי ויבש אפשר לבחור בגרסת ABS.»
- Q: צריך חיבור לחשמל?  
  A: חיבור קבוע לחשמל.  
  source: «• חיבור קבוע לחשמל»
- Q: מה ההבדל בין הגוונים?  
  A: 3000K מתאים לאווירה רגועה; 6500K מעניק נראות בהירה וחדה יותר.  
  source: «3000K מתאים לאווירה רגועה; 6500K מעניק נראות בהירה וחדה יותר.»

**home_card_line:** (empty — none exists)

**Flags:**
- WATERPROOF CONTRADICTION BY VARIANT: option "סוג גוף" = "ABS – לא עמיד למים" vs "אלומיניום – עמיד למים". A product-level ip_rating would be wrong for half the variants → left empty; no IP number is stated for the aluminium version either.
- Wired lamp ("חיבור קבוע לחשמל") in collection `solar-wall-lights`, tagged "תאורת קיר סולארית" — not solar.
- No wattage anywhere.

---

## 09. `waterproof-led-wall-light-ip65-6w-12w`

**מנורת קיר LED עמידה למים IP65 – ‏6W/12W** · collection: wall · solar-wall-lights (קיר) · variants 8 · ₪219.9–252.9

Options: צבע גוף: לבן / שחור; עוצמה: 6W / 12W; גוון אור: אור חם 3000K / אור קר 6000K

**power_source (proposed):** לא צוין  — source: התיאור אינו מציין מקור מתח; אפשרויות: עוצמה 6W / 12W בלבד. ראו דגלים.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | אור חם 3000K או אור קר 6000K | • אור חם 3000K או קר 6000K |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | אלומיניום | • גוף אלומיניום |
| dimensions |  |  |
| power_watt | 6W או 12W | • עוצמה 6W או 12W |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): תאורה דו־כיוונית · צבע שחור או לבן · מתאימה לפנים ולחוץ

**direct_answer** (16 words): מנורת קיר מאלומיניום עם אור כלפי מעלה ומטה ועמידות IP65 — לכניסה, למרפסת, למדרגות וגם לחללים פנימיים.

**not_fit_for:** EMPTY — מקור המתח לא צוין (6W/12W מרמז על חיבור לחשמל אך אינו כתוב). לא ניתן לקבוע שאיזה מארבעת הסעיפים נכון מילולית — השדה ריק עד שהבעלים יאשר את מקור המתח.

**faq**:
- Q: מתאימה לחוץ?  
  A: עמידות IP65 מאפשרת התקנה באזורים חיצוניים החשופים לתנאי מזג אוויר משתנים.  
  source: «עמידות IP65 מאפשרת התקנה באזורים חיצוניים החשופים לתנאי מזג אוויר משתנים.»
- Q: 6W או 12W?  
  A: 6W לאפקט עדין וממוקד; 12W לנוכחות חזקה יותר על שטח גדול.  
  source: «6W לאפקט עדין וממוקד; 12W לנוכחות חזקה יותר על שטח גדול.»
- Q: איזה גוון לבחור?  
  A: 3000K יוצר חמימות; 6000K מעניק מראה לבן, חד ומודרני.  
  source: «3000K יוצר חמימות; 6000K מעניק מראה לבן, חד ומודרני.»
- Q: כמה מנורות צריך?  
  A: בכניסה צרה אפשר להסתפק ביחידה. על חזית רחבה או לאורך מעבר, התקנה סימטרית או רציפה תיצור אפקט שלם ומרשים יותר.  
  source: «בכניסה צרה אפשר להסתפק ביחידה. על חזית רחבה או לאורך מעבר, התקנה סימטרית או רציפה תיצור אפקט שלם ומרשים יותר.»

**home_card_line:** (empty — none exists)

**Flags:**
- POWER SOURCE NOT STATED anywhere (description, options, tags). Tagged "תאורת קיר סולארית" and in `solar-wall-lights` although nothing says solar and 6W/12W wattages suggest mains.
- images[0] is a baked slide ("תאורה שמעצבת אווירה / גוף תאורת קיר מעוצב עם הארה דו כיוונית") — no numbers.

---

## 10. `magnetic-rechargeable-touch-wall-light`

**מנורת קיר נטענת מגנטית עם שליטה במגע** · collection: wall · solar-wall-lights (קיר) · variants 2 · ₪159.9–159.9

Options: צבע גוף: לבן / שחור

**power_source (proposed):** נטען  — source: • סוללה נטענת 1200mAh · • טעינה באמצעות USB

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | 3000K, 4000K או 6000K | • 3000K, 4000K או 6000K |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery | סוללה נטענת 1200mAh | • סוללה נטענת 1200mAh |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): טעינה באמצעות USB · שליטה ועמעום במגע · סיבוב 360° והטיה עד 90° · חיבור מגנטי נשלף · צבע שחור או לבן

**direct_answer** (16 words): מנורת קיר מגנטית נטענת — תאורה ליד המיטה, במסדרון, במטבח או בפינת העבודה בלי נקודת חשמל קבועה.

**not_fit_for** (pair 2 · כניסה, קיר וחזית): נדרש אור חזק וקבוע לאורך כל הלילה
  Why: שיקול דעת: מוצר פנימי לקיר; הסעיף ״נדרש אור חזק וקבוע לאורך כל הלילה״ נתמך ב־״תאורה אישית ורכה בלי להציף את כל החלל״ + סוללה נטענת. הבעלים רשאי להעדיף ריק.

**faq**:
- Q: איך טוענים?  
  A: טעינה באמצעות USB.  
  source: «• טעינה באמצעות USB»
- Q: אפשר לכוון את האור?  
  A: החיבור המגנטי מאפשר סיבוב של 360° והטיה של עד 90° לכיוון מדויק.  
  source: «החיבור המגנטי מאפשר סיבוב של 360° והטיה של עד 90° לכיוון מדויק.»
- Q: איך מעמעמים?  
  A: שליטה במגע ועמעום בלחיצה ארוכה מאפשרים להתאים את העוצמה בלי לקום.  
  source: «שליטה במגע ועמעום בלחיצה ארוכה מאפשרים להתאים את העוצמה בלי לקום.»
- Q: צריך לקדוח?  
  A: הסוללה הנטענת והבסיס המגנטי שומרים על התקנה נקייה וגמישה.  
  source: «הסוללה הנטענת והבסיס המגנטי שומרים על התקנה נקייה וגמישה.»

**home_card_line:** (empty — none exists)

**Flags:**
- Indoor rechargeable lamp in `solar-wall-lights`, tagged "תאורת קיר סולארית" — not solar, not outdoor.
- images[0] baked: "הדבקה קלה ללא קידוח", "ניתן להסרה והצמדה מחדש" — the adhesive/no-drill mounting claim exists only as image pixels (description says only "בסיס מגנטי"); not used.
- No runtime, charge time or IP in the description. light_modes left empty: the three values are colour tones (גוונים), not modes.

---

## 11. `outdoor-bidirectional-led-wall-light-ip65`

**מנורת קיר LED חיצונית דו־כיוונית IP65** · collection: wall · solar-wall-lights (קיר) · variants 4 · ₪159.9–162.9

Options: עיצוב: דגם A / דגם B; גוון אור: אור חם 3000K / אור לבן 6000K

**power_source (proposed):** לא צוין  — source: התיאור אינו מציין מקור מתח ולא הספק. ראו דגלים.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | אור חם 3000K או לבן 6000K | • אור חם 3000K או לבן 6000K |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): תאורת LED דו־כיוונית · גוף שחור מודרני · דגם A או דגם B · מתאימה לפנים ולחוץ

**direct_answer** (16 words): מנורת חוץ שחורה עם אור כלפי מעלה ומטה — לכניסה, למרפסת או למעבר; עמידות IP65 לקירות חוץ.

**not_fit_for:** EMPTY — מקור המתח לא צוין; לא ניתן לטעון שסעיף זוג 2 נכון מילולית. השדה ריק עד אישור הבעלים.

**faq**:
- Q: מתאימה לקיר חיצוני?  
  A: עמידות IP65 מתאימה לכניסות, מרפסות, גינות ומעברים חשופים.  
  source: «עמידות IP65 מתאימה לכניסות, מרפסות, גינות ומעברים חשופים.»
- Q: מה ההבדל בין דגם A לדגם B?  
  A: דגם A ו־דגם B מאפשרים לבחור את צורת האלומה והאופי שמתאימים לחזית.  
  source: «דגם A ו־דגם B מאפשרים לבחור את צורת האלומה והאופי שמתאימים לחזית.»
- Q: איזה גוון לבחור?  
  A: 3000K מעניק חמימות מזמינה; 6000K יוצר מראה לבן, מודרני ובולט.  
  source: «3000K מעניק חמימות מזמינה; 6000K יוצר מראה לבן, מודרני ובולט.»

**home_card_line:** עמידות IP65 · אור חם 3000K או לבן 6000K

**Flags:**
- POWER SOURCE AND WATTAGE NOT STATED; tagged "תאורת קיר סולארית" without any solar wording.
- The description never explains what differs between "דגם A" and "דגם B" beyond "צורת האלומה והאופי" — the FAQ answer is weak but is all that exists.

---

## 12. `solar-garden-spotlight-52-led`

**ספוט סולארי עוצמתי לגינה – 52 LED עם 3 מצבי תאורה** · collection: spot · ספוטים-ופרוז-קטורים-סולאריים (גינה) · variants 4 · ₪219.9–429.9

Options: כמות: יחידה אחת / 2 יחידות; גוון אור: לבן חם / לבן קר

**power_source (proposed):** סולארי  — source: הפאנל נטען ביום והספוט נדלק בלילה, בלי הפעלה ידנית ובלי צריכת חשמל ביתית.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours | עד כ־15/10/6 שעות לפי העוצמה | • עד כ־15/10/6 שעות לפי העוצמה |
| color_temp | לבן חם או לבן קר | אפשרות ״גוון אור״: לבן חם · לבן קר |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes | 3 | • 3 מצבי עוצמה |

Stated facts with no matching metafield (stay in the description): 52 נורות LED · התקנה בקרקע או על הקיר · ראש מתכוונן עד 90° · יחידה אחת או זוג

**direct_answer** (19 words): ספוט סולארי עוצמתי שיוצר נקודת אור ברורה על עץ, קיר, שביל או פינת גינה — התקנה בקרקע או על הקיר.

**not_fit_for** (pair 4 · הדגשת אזור בגינה): נדרשת התקנה מיוחדת או חיבור קבוע
  Why: הדגשת אזור בגינה (עץ, קיר אבן, צמחייה); סולארי ״בלי להעביר אפילו כבל אחד״ — הסעיף נכון מילולית.

**faq**:
- Q: כמה שעות הוא מאיר?  
  A: עד כ־15/10/6 שעות לפי העוצמה.  
  source: «• עד כ־15/10/6 שעות לפי העוצמה»
- Q: איך מתקינים?  
  A: נועצים בקרקע כספוט נוף או מחברים לקיר בעזרת אביזרי ההתקנה המצורפים.  
  source: «נועצים בקרקע כספוט נוף או מחברים לקיר בעזרת אביזרי ההתקנה המצורפים.»
- Q: מה שלושת המצבים?  
  A: בחרו תאורה נמוכה לערב ארוך, בינונית לאיזון או גבוהה כשצריך נוכחות חזקה יותר.  
  source: «בחרו תאורה נמוכה לערב ארוך, בינונית לאיזון או גבוהה כשצריך נוכחות חזקה יותר.»
- Q: חם או קר?  
  A: אור חם יוצר עומק ואווירה רכה סביב צמחייה; אור קר נותן נראות בהירה ובולטת יותר לשבילים ולכניסות.  
  source: «אור חם יוצר עומק ואווירה רכה סביב צמחייה; אור קר נותן נראות בהירה ובולטת יותר לשבילים ולכניסות.»

**home_card_line:** 52 נורות LED · 3 מצבי עוצמה · עד כ־15/10/6 שעות

**Flags:**
- SPEC EXISTS ONLY AS IMAGE PIXELS: images[0] claims "טווח עבודה: -20° עד 60°C", "עמיד לחום ולקור", "עמידות לכל מזג אוויר" — the temperature range is nowhere in the description; not used.
- No charge time, lumens or battery stated.

---

## 13. `solar-security-light-100-led`

**תאורת אבטחה סולארית 100 LED עם חיישן תנועה** · collection: spot · ספוטים-ופרוז-קטורים-סולאריים (גינה) · variants 1 · ₪99.9–99.9

Options: צבע: שחור

**power_source (proposed):** סולארי  — source: • טעינה סולארית

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp |  |  |
| sensor_range_m | כ־6–8 מטרים | • טווח זיהוי כ־6–8 מטרים |
| sensor_angle_deg | 120° | • זווית זיהוי 120° |
| material | PC ו־ABS | מבנה PC ו־ABS עם עמידות IP65 מתאים לגשם ולמזג אוויר משתנה. |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes | 3 | • 3 מצבי תאורה |

Stated facts with no matching metafield (stay in the description): 100 נורות LED · חיישן PIR

**direct_answer** (14 words): תאורת אבטחה סולארית עם חיישן תנועה — לכניסה, לשער, לחניה או למעבר צדדי, בלי חיווט.

**not_fit_for** (pair 2 · כניסה, קיר וחזית): נדרש אור חזק וקבוע לאורך כל הלילה
  Why: כניסה/שער/חזית; סולארי עם חיישן — הסעיף נתמך מילולית ב־״בלי להשאיר אור חזק דולק כל הלילה״.

**faq**:
- Q: מאיזה מרחק החיישן מזהה?  
  A: חיישן PIR בזווית 120° ובטווח של כ־6–8 מטרים מגיב עוד לפני שמגיעים אל המנורה.  
  source: «חיישן PIR בזווית 120° ובטווח של כ־6–8 מטרים מגיב עוד לפני שמגיעים אל המנורה.»
- Q: מה שלושת המצבים?  
  A: אור קבוע, אור חלש שמתחזק בעת תנועה או אור חזק שמופעל רק כשמישהו מתקרב.  
  source: «אור קבוע, אור חלש שמתחזק בעת תנועה או אור חזק שמופעל רק כשמישהו מתקרב.»
- Q: עמידה בגשם?  
  A: מבנה PC ו־ABS עם עמידות IP65 מתאים לגשם ולמזג אוויר משתנה.  
  source: «מבנה PC ו־ABS עם עמידות IP65 מתאים לגשם ולמזג אוויר משתנה.»
- Q: איזה מצב לבחור?  
  A: למעבר פעיל בחרו אור חלש שמתחזק. לאזור שצריך להאיר רק בעת תנועה, בחרו הפעלה חזקה וממוקדת.  
  source: «למעבר פעיל בחרו אור חלש שמתחזק. לאזור שצריך להאיר רק בעת תנועה, בחרו הפעלה חזקה וממוקדת.»

**home_card_line:** 100 נורות LED · חיישן PIR · טווח זיהוי כ־6–8 מטרים

**Flags:**
- No colour temperature, hours, lumens or battery in the description.
- images[0] baked ("נטען ביום, מאיר בלילה", "טעינה סולארית") — no numbers.

---

## 14. `modern-solar-path-lights-set`

**סט תאורת שביל סולארית מודרנית בצורת 7 – ‏4/8 יחידות** · collection: path · תאורת-שביל-סולארית (שביל) · variants 2 · ₪549.9–999.9

Options: כמות: 4 יחידות / 8 יחידות

**power_source (proposed):** סולארי  — source: הטעינה מתבצעת ביום, וההפעלה האוטומטית חוסכת התעסקות בכל ערב.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours | כ־4–8 שעות | • טעינה כ־4–8 שעות |
| light_hours | כ־8–12 שעות בהתאם לתנאים | • עבודה כ־8–12 שעות בהתאם לתנאים |
| color_temp | גוון חם 2700K | • גוון חם 2700K |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens | כ־15 לומן לכל מנורה | • כ־15 לומן לכל מנורה |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 6 נורות LED בכל גוף · סט של 4 או 8 יחידות

**direct_answer** (17 words): סט מנורות שביל סולאריות בצורת 7 שמפנות אור חם כלפי מטה — רצף נקי לאורך שבילים, ערוגות ומדשאות.

**not_fit_for** (pair 1 · שביל, מדרגות ומעברים): המקום כמעט אינו מקבל אור יום
  Why: שביל; סולארי (״הטעינה מתבצעת ביום״) — הסעיף נכון מילולית.

**faq**:
- Q: כמה שעות עובדות?  
  A: עבודה כ־8–12 שעות בהתאם לתנאים.  
  source: «• עבודה כ־8–12 שעות בהתאם לתנאים»
- Q: כמה זמן טעינה?  
  A: טעינה כ־4–8 שעות.  
  source: «• טעינה כ־4–8 שעות»
- Q: 4 או 8 יחידות?  
  A: 4 יחידות מתאימות למקטע ממוקד; 8 יחידות יוצרות רצף מלא ומרשים יותר.  
  source: «4 יחידות מתאימות למקטע ממוקד; 8 יחידות יוצרות רצף מלא ומרשים יותר.»
- Q: האור מסנוור?  
  A: האלומה יורדת אל הקרקע ומייצרת נראות נעימה בלי סנוור ישיר לעיניים.  
  source: «האלומה יורדת אל הקרקע ומייצרת נראות נעימה בלי סנוור ישיר לעיניים.»

**home_card_line:** גוון חם 2700K · עמידות IP65 · סט של 4 או 8 יחידות

**Flags:**
- images[0] baked ("מוסיפה אווירה לכל שביל וגינה", badge "זמין בסט של 4 או 8 יחידות") — consistent with the variants; no other numbers.

---

## 15. `solar-floodlight-ip67-remote-timer`

**פרוז׳קטור סולארי IP67 עם שלט וטיימר – 72/128/200 LED** · collection: spot · ספוטים-ופרוז-קטורים-סולאריים (גינה) · variants 3 · ₪199.9–499.9

Options: דגם: 72 LED / 100W / 128 LED / 200W / 200 LED / 300W

**power_source (proposed):** סולארי  — source: הפאנל הנפרד נטען מהשמש, הפרוז׳קטור מאיר את השטח והשלט מאפשר לקבוע עוצמה וזמן פעולה

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP67 | • עמידות IP67 |
| charge_time_hours | כ־6–8 שעות | • טעינה כ־6–8 שעות |
| light_hours | כ־8–10 שעות בהתאם לתנאים | • עבודה כ־8–10 שעות בהתאם לתנאים |
| color_temp |  |  |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt | 100W / 200W / 300W לפי הדגם | אפשרות ״דגם״: 72 LED / 100W · 128 LED / 200W · 200 LED / 300W |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 72, 128 או 200 נורות LED · שלט רחוק · טיימר 3/5/8 שעות · פאנל סולארי נפרד

**direct_answer** (14 words): פרוז׳קטור סולארי עם פאנל נפרד, שלט וטיימר — לחצר, לחניה, לכניסה או לאזור עבודה בחוץ.

**not_fit_for** (pair 2 · כניסה, קיר וחזית): נדרש אור חזק וקבוע לאורך כל הלילה
  Why: שיקול דעת: המקום ״כניסה/חצר״; הסעיף ״נדרש אור חזק וקבוע לאורך כל הלילה״ נתמך בטיימר 3/5/8 שעות ו־״עבודה כ־8–10 שעות בהתאם לתנאים״ (לא קבוע כל הלילה). זוג 4 נכון גם הוא (סולארי, ללא חיבור קבוע) — הבעלים יכריע.

**faq**:
- Q: מה עושים אם המקום מוצל?  
  A: ההפרדה ביניהם מאפשרת לקבל טעינה טובה גם כאשר אזור ההארה עצמו מוצל או נמצא מתחת לקירוי.  
  source: «ההפרדה ביניהם מאפשרת לקבל טעינה טובה גם כאשר אזור ההארה עצמו מוצל או נמצא מתחת לקירוי.»
- Q: איך עובד הטיימר?  
  A: משנים עוצמה ומפעילים טיימר של 3, 5 או 8 שעות בלי לטפס ובלי לגשת למנורה.  
  source: «משנים עוצמה ומפעילים טיימר של 3, 5 או 8 שעות בלי לטפס ובלי לגשת למנורה.»
- Q: כמה שעות עובד?  
  A: עבודה כ־8–10 שעות בהתאם לתנאים.  
  source: «• עבודה כ־8–10 שעות בהתאם לתנאים»
- Q: איזה דגם לבחור?  
  A: לאזור כניסה או מרפסת דגם קטן עשוי להספיק. לחניה או חצר רחבה, מספר LED גבוה יותר יעניק כיסוי משמעותי יותר.  
  source: «לאזור כניסה או מרפסת דגם קטן עשוי להספיק. לחניה או חצר רחבה, מספר LED גבוה יותר יעניק כיסוי משמעותי יותר.»

**home_card_line:** (empty — none exists)

**Flags:**
- IMAGE CONTRADICTS THE VARIANTS: images[0] carries the badge "זמין בסט של 4 או 8 יחידות" (copied from the path-set creative) — this product sells single units of 72/128/200 LED. Never render images[0].
- power_watt comes ONLY from the option labels ("72 LED / 100W" …). 100–300W for a solar floodlight is almost certainly a marketing-equivalent figure — owner must confirm before it is written; otherwise leave power_watt empty.
- light_modes left empty: the description says "משנים עוצמה" without a count.
- images[0] also shows "IP67" on the housing — consistent with the description.

---

## 16. `decorative-led-net-lights`

**רשת תאורת LED דקורטיבית לחוץ ולגינה – 1.5 עד 12 מטר** · collection: decor · גרילנדות-ותאורה-דקורטיבית (מרפסת) · variants 30 · ₪109.9–469.9

Options: גודל: 1.5×1.5 מ׳ / 96 LED / 3×2 מ׳ / 196 LED / 6×2 מ׳ / 380 LED / 9×2 מ׳ / 580 LED / 12×2 מ׳ / 780 LED / 6×4 מ׳ / 672 LED; צבע תאורה: לבן חם / כחול / RGB צבעוני / לבן קר / סגול

**power_source (proposed):** חשמל 220V  — source: • חיבור 220V

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | לבן חם, לבן קר, כחול, סגול או RGB | • לבן חם, לבן קר, כחול, סגול או RGB |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions | מ־1.5×1.5 עד 12×2 או 6×4 מטר | • מידות מ־1.5×1.5 עד 12×2 או 6×4 מטר |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 96 עד 780 נורות LED לפי המידה · מתאימה לקירות, גדרות ופרגולות · יש להשתמש בחיבור חשמל מתאים ומוגן באזור חוץ

**direct_answer** (18 words): רשת תאורת LED בחיבור 220V שפורסים על גדר, קיר או פרגולה — רקע מואר למסיבה, לאירוח או לערב בגינה.

**not_fit_for** (pair 3 · מרפסת ופינת ישיבה): צריך אור חזק — זו אינה מטרתה
  Why: מרפסת/אירוח — ליצור אווירה; ״רשת אור צפופה שממלאת את החלל באווירה״ — הסעיף ״צריך אור חזק — זו אינה מטרתה״ נכון מילולית (מוצר מחווט; סעיפי הסולארי לא רלוונטיים).

**faq**:
- Q: איך מחברים לחשמל?  
  A: חיבור 220V. יש להשתמש בחיבור חשמל מתאים ומוגן באזור חוץ.  
  source: «• חיבור 220V · • יש להשתמש בחיבור חשמל מתאים ומוגן באזור חוץ»
- Q: איזו מידה לבחור?  
  A: מדדו את הקיר או הגדר לפני ההזמנה. לרקע מלא בחרו מידה שקרובה ככל האפשר לשטח שאותו רוצים לכסות.  
  source: «מדדו את הקיר או הגדר לפני ההזמנה. לרקע מלא בחרו מידה שקרובה ככל האפשר לשטח שאותו רוצים לכסות.»
- Q: כמה נורות יש?  
  A: 96 עד 780 נורות LED לפי המידה.  
  source: «• 96 עד 780 נורות LED לפי המידה»

**home_card_line:** חיבור 220V · מ־1.5×1.5 עד 12×2 או 6×4 מטר

**Flags:**
- NO IP RATING for a 220V product sold "לחוץ ולגינה" — the only protection wording is the caution bullet; ip_rating stays empty. Owner should obtain the rating before selling it as outdoor.
- images[0] baked ("רשת תאורת LED לאווירה קסומה", "מתאים לחוץ ולפנים") — no numbers.

---

## 17. `led-globe-string-lights`

**גרילנדת כדורי LED דקורטיבית – USB או סוללות** · collection: decor · גרילנדות-ותאורה-דקורטיבית (מרפסת) · variants 30 · ₪89.9–179.9

Options: אורך ומספר נורות: 1.5 מ׳ / 10 נורות / 3 מ׳ / 20 נורות / 6 מ׳ / 40 נורות / 10 מ׳ / 80 נורות / 12 מ׳ / 100 נורות; מקור מתח: USB / קופסת סוללות; צבע תאורה: לבן חם / לבן קר / צבעוני

**power_source (proposed):** USB או סוללות (לפי הווריאנט)  — source: • USB או קופסת סוללות (אפשרות ״מקור מתח״: USB / קופסת סוללות)

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | לבן חם, לבן קר או צבעוני | • לבן חם, לבן קר או צבעוני |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions | אורך 1.5 עד 12 מטר; קוטר כדור כ־1 ס״מ | • 1.5 עד 12 מטר · • קוטר כדור כ־1 ס״מ |
| power_watt |  |  |
| lumens |  |  |
| battery | קופסת סוללות — סוללות אינן כלולות | • USB או קופסת סוללות · • סוללות אינן כלולות |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 10 עד 100 נורות LED

**direct_answer** (16 words): גרילנדת כדורי LED עדינים ב־USB או בסוללות — למדף, למרפסת, לאוהל או לשולחן; שכבה של אור ואווירה.

**not_fit_for** (pair 3 · מרפסת ופינת ישיבה): צריך אור חזק — זו אינה מטרתה
  Why: מרפסת/פינה — ליצור אווירה; ״הן לא נועדו להאיר חדר שלם״ — הסעיף נכון מילולית.

**faq**:
- Q: USB או סוללות?  
  A: USB לשימוש ממושך ליד מקור מתח; קופסת סוללות למקומות שבהם אין שקע קרוב.  
  source: «USB לשימוש ממושך ליד מקור מתח; קופסת סוללות למקומות שבהם אין שקע קרוב.»
- Q: הסוללות כלולות?  
  A: סוללות אינן כלולות.  
  source: «• סוללות אינן כלולות»
- Q: איזה אורך לבחור?  
  A: 1.5–3 מטר מתאימים למדף או שולחן; 6–12 מטר מאפשרים לעטוף מסגרת, קיר, אוהל או אזור ישיבה רחב.  
  source: «1.5–3 מטר מתאימים למדף או שולחן; 6–12 מטר מאפשרים לעטוף מסגרת, קיר, אוהל או אזור ישיבה רחב.»
- Q: מאירה חדר?  
  A: הן לא נועדו להאיר חדר שלם — הן נועדו לגרום לו להרגיש אחרת.  
  source: «הן לא נועדו להאיר חדר שלם — הן נועדו לגרום לו להרגיש אחרת»

**home_card_line:** 1.5 עד 12 מטר · 10 עד 100 נורות LED · USB או סוללות

**Flags:**
- No IP rating and no outdoor claim beyond "מרפסת"/"אוהל" — do not present as weatherproof.
- Battery type/count not stated (only "קופסת סוללות", "סוללות אינן כלולות").
- images[0] baked ("נגיעת אור לכל פינה", "מתאים לחללים קטנים") — no numbers.

---

## 18. `lighted-birch-branches-20-led`

**ענפי ליבנה מוארים – 20 נורות LED לעיצוב הבית** · collection: decor · גרילנדות-ותאורה-דקורטיבית (מרפסת) · variants 2 · ₪89.9–89.9

Options: צבע תאורה: לבן חם / לבן קר

**power_source (proposed):** סוללות  — source: • הפעלה באמצעות 2 סוללות AA

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | לבן חם או לבן קר | • לבן חם או לבן קר |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions | גובה כ־72 ס״מ | • גובה כ־72 ס״מ |
| power_watt |  |  |
| lumens |  |  |
| battery | 2 סוללות AA — אינן כלולות | • הפעלה באמצעות 2 סוללות AA · • סוללות אינן כלולות |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 20 נורות LED · ענפים לבנים וגמישים

**direct_answer** (16 words): ענפי ליבנה מוארים עם 20 נורות LED בסוללות — לאגרטל על קונסולה, במרכז שולחן או בפינת הסלון.

**not_fit_for** (pair 3 · מרפסת ופינת ישיבה): צריך אור חזק — זו אינה מטרתה
  Why: שיקול דעת: מוצר פנימי (״לעיצוב הבית״), אין מקום מארבעת המקומות. הסעיף ״צריך אור חזק — זו אינה מטרתה״ נכון מילולית (״אור רך במקום תאורה חזקה״). הבעלים רשאי להעדיף ריק.

**faq**:
- Q: איך מפעילים?  
  A: הפעלה באמצעות 2 סוללות AA. סוללות אינן כלולות.  
  source: «• הפעלה באמצעות 2 סוללות AA · • סוללות אינן כלולות»
- Q: מה הגובה?  
  A: גובה כ־72 ס״מ.  
  source: «• גובה כ־72 ס״מ»
- Q: אפשר לעצב את הענפים?  
  A: הענפים גמישים, כך שאפשר לפתוח, לכופף ולסדר אותם לפי צורת האגרטל והסגנון הרצוי.  
  source: «הענפים גמישים, כך שאפשר לפתוח, לכופף ולסדר אותם לפי צורת האגרטל והסגנון הרצוי.»

**home_card_line:** גובה כ־72 ס״מ · 20 נורות LED · לבן חם או לבן קר

**Flags:**
- Indoor décor item ("לעיצוב הבית") in an outdoor-lighting catalogue (BRIEF §2 says all 27 are outdoor) — none of the four places applies; not_fit_for is a loose fit.
- No IP rating (correct — indoor).

---

## 19. `solar-firefly-garden-lights`

**תאורת גחליליות סולארית לגינה – 10 נורות מתנדנדות** · collection: decor · גרילנדות-ותאורה-דקורטיבית (מרפסת) · variants 1 · ₪99.9–99.9

Options: דגם: 10 נורות

**power_source (proposed):** סולארי  — source: • טעינה סולארית

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours | כ־6–12 שעות לאחר טעינה מלאה | • כ־6–12 שעות תאורה לאחר טעינה מלאה |
| color_temp |  |  |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 10 נקודות אור · ענפים גמישים ומתנדנדים · הפעלה אוטומטית בחושך · התקנה בנעיצה באדמה

**direct_answer** (17 words): תאורת גחליליות סולארית — עשר נקודות אור על ענפים גמישים שנעים ברוח, בין פרחים, ליד שביל או בעציץ.

**not_fit_for** (pair 3 · מרפסת ופינת ישיבה): צריך אור חזק — זו אינה מטרתה
  Why: ליצור אווירה (״לא נועדה רק להאיר — נועדה לגרום לגינה להרגיש חיה״) — הסעיף נכון מילולית. המקום הוא ערוגה/דשא ולא מרפסת; זוג 4 נכון גם הוא (סולארי בנעיצה, ללא חיבור קבוע) — הבעלים יכריע.

**faq**:
- Q: כמה שעות מאירה?  
  A: כ־6–12 שעות תאורה לאחר טעינה מלאה.  
  source: «• כ־6–12 שעות תאורה לאחר טעינה מלאה»
- Q: איפה למקם?  
  A: ליד ערוגה, בקצה הדשא או לצד פינת ישיבה — אזור פתוח יאפשר לענפים לנוע ולהציג את האפקט בצורה ברורה יותר.  
  source: «ליד ערוגה, בקצה הדשא או לצד פינת ישיבה — אזור פתוח יאפשר לענפים לנוע ולהציג את האפקט בצורה ברורה יותר.»
- Q: נשארת בגשם?  
  A: עמידות IP65 מתאימה לגשם, שמש ולתנאי מזג אוויר משתנים.  
  source: «עמידות IP65 מתאימה לגשם, שמש ולתנאי מזג אוויר משתנים.»
- Q: איך מתקינים?  
  A: נועצים באדמה, מכוונים את הפאנל לשמש ונותנים לרוח ליצור את האפקט.  
  source: «נועצים באדמה, מכוונים את הפאנל לשמש ונותנים לרוח ליצור את האפקט.»

**home_card_line:** (empty — none exists)

**Flags:**
- No charge time or battery stated. Images 2–3 carry small captions (ledger) — no numeric claims seen.

---

## 20. `solar-rope-string-lights`

**שרשרת חבל סולארית לחוץ – 50 עד 300 נורות LED** · collection: decor · גרילנדות-ותאורה-דקורטיבית (מרפסת) · variants 16 · ₪89.9–159.9

Options: אורך ומספר נורות: 7 מ׳ / 50 נורות / 12 מ׳ / 100 נורות / 22 מ׳ / 200 נורות / 32 מ׳ / 300 נורות; צבע תאורה: לבן חם / לבן קר / כחול / צבעוני

**power_source (proposed):** סולארי  — source: הפאנל הסולארי נטען מהשמש ומשחרר אתכם מכבלים שמגבילים את המיקום.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | לבן חם, לבן קר, כחול או צבעוני | • לבן חם, לבן קר, כחול או צבעוני |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions | אורך 7, 12, 22 או 32 מ׳ | • 7 מ׳ / 50 נורות · • 12 מ׳ / 100 נורות · • 22 מ׳ / 200 נורות · • 32 מ׳ / 300 נורות |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): 50 / 100 / 200 / 300 נורות לפי האורך · הפעלה אוטומטית בחושך

**direct_answer** (19 words): שרשרת חבל סולארית עד 32 מטר — להקיף עצים, לעבור לאורך גדר או למלא פרגולה בנקודות אור, בלי תלות בשקע.

**not_fit_for** (pair 3 · מרפסת ופינת ישיבה): צריך אור חזק — זו אינה מטרתה
  Why: ליצור אווירה (״נקודות אור״, ״האווירה״); הסעיף ״צריך אור חזק — זו אינה מטרתה״ נכון מילולית.

**faq**:
- Q: איזה אורך לבחור?  
  A: בעת ליפוף סביב עץ או פרגולה נדרש יותר אורך ממה שנראה לעין. בחרו מידה עם מרווח כדי להגיע לתוצאה מלאה ולא להיעצר באמצע.  
  source: «בעת ליפוף סביב עץ או פרגולה נדרש יותר אורך ממה שנראה לעין. בחרו מידה עם מרווח כדי להגיע לתוצאה מלאה»
- Q: צריך שקע?  
  A: הפאנל הסולארי נטען מהשמש ומשחרר אתכם מכבלים שמגבילים את המיקום.  
  source: «הפאנל הסולארי נטען מהשמש ומשחרר אתכם מכבלים שמגבילים את המיקום.»
- Q: נדלקת לבד?  
  A: השרשרת נטענת ביום ופועלת אוטומטית עם רדת החשכה.  
  source: «השרשרת נטענת ביום ופועלת אוטומטית עם רדת החשכה.»

**home_card_line:** (empty — none exists)

**Flags:**
- No light hours or charge time in the description — unusual for a solar product; left empty.
- images[2] shows an IP65 badge — consistent with the description.

---

## 21. `solar-edison-string-lights`

**גרילנדת נורות אדיסון סולארית – 5 או 8 מטר** · collection: decor · גרילנדות-ותאורה-דקורטיבית (מרפסת) · variants 2 · ₪139.9–179.9

Options: אורך ומספר נורות: 5 מ׳ / 10 נורות / 8 מ׳ / 20 נורות

**power_source (proposed):** סולארי  — source: • טעינה סולארית

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours | כ־5–6 שעות לאחר טעינה מלאה | • כ־5–6 שעות תאורה לאחר טעינה מלאה |
| color_temp | גוון חם | • גוון אור חם |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions | אורך 5 מטר (10 נורות) או 8 מטר (20 נורות) | • 5 מטר / 10 נורות · • 8 מטר / 20 נורות |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): הדלקה אוטומטית בלילה · מתאימה למרפסת, פרגולה, גינה וקמפינג

**direct_answer** (18 words): גרילנדת נורות אדיסון סולארית — אור חם מעל פינת הישיבה, לאורך הפרגולה או באוהל, בלי שקע ובלי כבל מאריך.

**not_fit_for** (pair 3 · מרפסת ופינת ישיבה): צריך אור חזק — זו אינה מטרתה
  Why: מרפסת ופינת ישיבה; ״במקום אור לבן וחזק שמקלקל את האווירה״ — הסעיף נכון מילולית.

**faq**:
- Q: כמה שעות מאירה?  
  A: כ־5–6 שעות תאורה לאחר טעינה מלאה.  
  source: «• כ־5–6 שעות תאורה לאחר טעינה מלאה»
- Q: 5 או 8 מטר?  
  A: 5 מטר עם 10 נורות לפינה ממוקדת; 8 מטר עם 20 נורות לכיסוי רחב ועשיר יותר.  
  source: «5 מטר עם 10 נורות לפינה ממוקדת; 8 מטר עם 20 נורות לכיסוי רחב ועשיר יותר.»
- Q: צריך להדליק כל ערב?  
  A: לאחר ההגדרה הראשונית, הפאנל נטען ביום והגרילנדה נדלקת אוטומטית בלילה.  
  source: «לאחר ההגדרה הראשונית, הפאנל נטען ביום והגרילנדה נדלקת אוטומטית בלילה.»
- Q: איך לתלות?  
  A: השארת ירידה עדינה בין נקודות התלייה מעניקה לגרילנדה מראה טבעי, רך ומזמין יותר.  
  source: «השארת ירידה עדינה בין נקודות התלייה מעניקה לגרילנדה מראה טבעי, רך ומזמין יותר.»

**home_card_line:** (empty — none exists)

**Flags:**
- NO IP RATING for an outdoor solar string light (sold for "מרפסת, פרגולה, גינה וקמפינג") — ip_rating empty.
- No charge time stated.

---

## 22. `solar-crystal-ball-string-lights`

**גרילנדת כדורי קריסטל סולארית – 20 עד 200 נורות** · collection: decor · גרילנדות-ותאורה-דקורטיבית (מרפסת) · variants 24 · ₪89.9–179.9

Options: אורך ומספר נורות: 5 מ׳ / 20 נורות / 6.5 מ׳ / 30 נורות / 9.5 מ׳ / 50 נורות / 11 מ׳ / 60 נורות / 13 מ׳ / 100 נורות / 22 מ׳ / 200 נורות; צבע תאורה: צהוב / כחול / צבעוני / לבן

**power_source (proposed):** סולארי  — source: • טעינה סולארית

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | • עמידות IP65 |
| charge_time_hours |  |  |
| light_hours | כ־8–10 שעות לאחר טעינה מלאה | • כ־8–10 שעות עבודה לאחר טעינה מלאה |
| color_temp | צהוב, כחול, צבעוני או לבן | • צהוב, כחול, צבעוני או לבן |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions | אורך 5–22 מטר | • 5–22 מטר |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes | 8 | • 8 מצבי תאורה |

Stated facts with no matching metafield (stay in the description): 20–200 נורות LED

**direct_answer** (16 words): גרילנדת כדורי קריסטל סולארית — נצנוץ סביב אזור הישיבה, לאורך גדר או בתוך אוהל, בלי חיבור לחשמל.

**not_fit_for** (pair 3 · מרפסת ופינת ישיבה): צריך אור חזק — זו אינה מטרתה
  Why: מרפסת/פרגולה — ליצור אווירה (״רקע חגיגי״); הסעיף נכון מילולית.

**faq**:
- Q: מה שמונת המצבים?  
  A: בחרו אור קבוע לערב רגוע, גל או דעיכה לאפקט עדין, והבהוב למסיבה ואירוע.  
  source: «בחרו אור קבוע לערב רגוע, גל או דעיכה לאפקט עדין, והבהוב למסיבה ואירוע.»
- Q: כמה שעות עובדת?  
  A: כ־8–10 שעות עבודה לאחר טעינה מלאה.  
  source: «• כ־8–10 שעות עבודה לאחר טעינה מלאה»
- Q: נשארת בחוץ?  
  A: עמידות IP65 מאפשרת שימוש בגינה ובמרפסת בתנאי מזג אוויר משתנים.  
  source: «עמידות IP65 מאפשרת שימוש בגינה ובמרפסת בתנאי מזג אוויר משתנים.»
- Q: איזה אורך לבחור?  
  A: מדדו את אזור התלייה והוסיפו מרווח לקשתות ולליפוף. שרשרת מעט ארוכה יותר נראית מלאה ומעוצבת יותר משרשרת מתוחה מדי.  
  source: «מדדו את אזור התלייה והוסיפו מרווח לקשתות ולליפוף. שרשרת מעט ארוכה יותר נראית מלאה ומעוצבת יותר»

**home_card_line:** (empty — none exists)

**Flags:**
- Gallery slides ("22 מטר / 200 נורות LED", "עמיד למים IP65", "התקנה פשוטה") agree with the description — nothing image-only.
- No charge time stated.

---

## 23. `modern-led-bollard-light-5w-ip65`

**מנורת עמוד LED מודרנית לגינה ולחצר – 5W IP65** · collection: path · תאורת-שביל-סולארית (שביל) · variants 1 · ₪129.9–129.9

Options: צבע גוף: שחור; הספק: 5W; גוון אור: אור חם

**power_source (proposed):** חשמל 220V  — source: מתח: AC 85–265V — המתח 220V הוא תווית הקטגוריה; התיאור אומר AC 85–265V.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | דירוג אטימות: IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | גוון חם | גוון אור: חם |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | אלומיניום | גוף: אלומיניום |
| dimensions |  |  |
| power_watt | 5W | הספק: 5W |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): מתח: AC 85–265V · נורה כלולה · תקן CE · אחריות יצרן: שנתיים (ראו דגל)

**direct_answer** (15 words): מנורת עמוד LED מינימליסטית 5W (AC 85–265V) — להאיר שבילים, כניסות, מדשאות ופינות חוץ באור חם.

**not_fit_for:** EMPTY — מוצר מחווט (AC 85–265V): סעיף זוג 1 (״כמעט אינו מקבל אור יום״) לא חל; סעיף זוג 4 (״נדרשת התקנה מיוחדת או חיבור קבוע״) אינו ״לא מתאים״ למוצר שדורש חיבור קבוע בעצמו. אף אחד מארבעת הסעיפים אינו נכון מילולית — ריק.

**faq**:
- Q: מה מקור המתח?  
  A: מתח: AC 85–265V · נורה כלולה.  
  source: «הספק: 5W · מתח: AC 85–265V · … · נורה כלולה»
- Q: מתאימה לגשם?  
  A: דירוג IP65 מספק הגנה מפני אבק, גשם ולחות לשימוש שוטף בגינה.  
  source: «דירוג IP65 מספק הגנה מפני אבק, גשם ולחות לשימוש שוטף בגינה.»
- Q: ממה עשוי הגוף?  
  A: גוף אלומיניום עמיד.  
  source: «גוף אלומיניום עמיד ואחריות יצרן של שנתיים נועדו לשימוש ארוך טווח.»

**home_card_line:** (empty — none exists)

**Flags:**
- MAINS PRODUCT IN THE SOLAR PATH COLLECTION (`תאורת-שביל-סולארית`) — the collection name promises solar; the title does not say solar but a buyer landing from that collection will assume it.
- IMAGE CONTRADICTS THE DESCRIPTION: images[0] says "שנה אחריות" (1 year) and carries the third-party mark "LUMIÈRE OUTDOOR LIGHTING"; the description says "אחריות יצרן: שנתיים" (2 years). Warranty wording is under the owner ban (INVENTORY) — not put in any metafield.
- No dimensions (height) stated for a bollard; certification "תקן CE" unverifiable — not mapped.
- Description is the older plain format ("פרטים טכניים" line, no `.elms-sales` bullets).

---

## 24. `rechargeable-telescopic-camping-lantern`

**פנס קמפינג טלסקופי נטען 360° עם תאורת צד** · collection: spot · ספוטים-ופרוז-קטורים-סולאריים (גינה) · variants 1 · ₪189.9–189.9

Options: צבע: כסוף־שחור

**power_source (proposed):** נטען  — source: נטען ב־USB‑C: טעינה של כ־3 שעות באמצעות 5V/2A · טעינה: Type‑C

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours | כ־3 שעות (5V/2A) | טעינה של כ־3 שעות באמצעות 5V/2A, בלי להסתמך על סוללות חד־פעמיות. |
| light_hours | כ־3 שעות בפנס הקדמי וכ־5+ שעות בתאורת הצד | זמן עבודה מוצהר: כ־3 שעות בפנס הקדמי וכ־5+ שעות בתאורת הצד |
| color_temp |  |  |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | ABS | חומר: ABS עמיד לנפילות |
| dimensions | מקופל כ־25.2×10×4.2 ס״מ; נפתח עד גובה כ־51.8 ס״מ | מתקפל לגודל כ־25.2×10×4.2 ס״מ … נפתח עד גובה של כ־51.8 ס״מ |
| power_watt |  |  |
| lumens | עד כ־310 לומן (פנס קדמי) / עד כ־170 לומן (תאורת צד) | מצב קדמי ממוקד עד כ־310 לומן ותאורת צד עד כ־170 לומן. |
| battery |  |  |
| light_modes | פנס: חזק / חלש / הבהוב · תאורת צד: חזק / חלש | מצבי פנס: חזק / חלש / הבהוב · מצבי תאורת צד: חזק / חלש |

Stated facts with no matching metafield (stay in the description): מקור אור: ליבת אור לבנה + 54 LED · טעינה: Type‑C · צבע: כסוף־שחור · עמידות למים לשימוש יומיומי (ללא דירוג IP)

**direct_answer** (16 words): פנס קמפינג טלסקופי נטען עם פנס קדמי חזק ותאורת צד רחבה — לאוהל, לרכב או לאזור עבודה.

**not_fit_for:** EMPTY — פנס נייד לקמפינג — אינו שייך לאף אחד מארבעת המקומות (שביל/קיר/מרפסת/גינה) ואף סעיף אינו נכון מילולית. ריק.

**faq**:
- Q: כמה זמן עובד?  
  A: זמן עבודה מוצהר: כ־3 שעות בפנס הקדמי וכ־5+ שעות בתאורת הצד.  
  source: «זמן עבודה מוצהר: כ־3 שעות בפנס הקדמי וכ־5+ שעות בתאורת הצד»
- Q: איך טוענים?  
  A: טעינה של כ־3 שעות באמצעות 5V/2A, בלי להסתמך על סוללות חד־פעמיות.  
  source: «טעינה של כ־3 שעות באמצעות 5V/2A, בלי להסתמך על סוללות חד־פעמיות.»
- Q: מה הגודל?  
  A: מתקפל לגודל כ־25.2×10×4.2 ס״מ ונוח לאחסון ברכב או בציוד הקמפינג.  
  source: «מתקפל לגודל כ־25.2×10×4.2 ס״מ ונוח לאחסון ברכב או בציוד הקמפינג.»
- Q: עמיד למים?  
  A: עמידות למים לשימוש יומיומי.  
  source: «חומר: ABS עמיד לנפילות · צבע: כסוף־שחור · עמידות למים לשימוש יומיומי.»

**home_card_line:** (empty — none exists)

**Flags:**
- TITLE CONTRADICTS THE IMAGE: title says "360°", images[0] says "ראש מסתובב 270°"; the description states neither. No rotation number is written anywhere in the text — none used.
- No IP number ("עמידות למים לשימוש יומיומי" only) — ip_rating empty; "ABS עמיד לנפילות" is drop-resistance, not waterproofing.
- Non-solar portable lantern in collection `ספוטים-ופרוז-קטורים-סולאריים`.
- No battery capacity stated. Description is the older plain format.

---

## 25. `swaying-solar-path-lights-ip65`

**סט מנורות שביל סולאריות מתנדנדות ברוח – 2/6 יחידות IP65** · collection: path · תאורת-שביל-סולארית (שביל) · variants 2 · ₪189.9–329.9

Options: כמות: 2 יחידות / 6 יחידות

**power_source (proposed):** סולארי  — source: מקור מתח: סולארי

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | דירוג אטימות: IP65 |
| charge_time_hours |  |  |
| light_hours | עד כ־12 שעות, לאחר טעינה מלאה בשמש ובהתאם לתנאי מזג האוויר | עד כ־12 שעות תאורה: לאחר טעינה מלאה בשמש ובהתאם לתנאי מזג האוויר. |
| color_temp | לבן חם | גוון אור: לבן חם |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | ABS | חומר: ABS |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): מתח עבודה: 5V · נורות LED כלולות · התקנה בהרכבה פשוטה · תקנים: CE, RoHS, UL, FCC, LVD (לא אומת — לא ממופה)

**direct_answer** (15 words): מנורות שביל סולאריות שנעות בעדינות עם הרוח — לאורך שבילים, ערוגות, מדשאות ופינות ישיבה, ללא חיווט.

**not_fit_for** (pair 1 · שביל, מדרגות ומעברים): המקום כמעט אינו מקבל אור יום
  Why: שביל; סולארי (״מקור מתח: סולארי״) — הסעיף נכון מילולית.

**faq**:
- Q: כמה שעות מאירות?  
  A: עד כ־12 שעות תאורה: לאחר טעינה מלאה בשמש ובהתאם לתנאי מזג האוויר.  
  source: «עד כ־12 שעות תאורה: לאחר טעינה מלאה בשמש ובהתאם לתנאי מזג האוויר.»
- Q: צריך חיווט?  
  A: נטענות מהשמש במהלך היום ופועלות באופן אוטומטי בשעות החשכה.  
  source: «ללא חיווט: נטענות מהשמש במהלך היום ופועלות באופן אוטומטי בשעות החשכה.»
- Q: עמידות לגשם?  
  A: דירוג IP65 וגוף ABS מספקים הגנה מפני גשם, אבק ולחות.  
  source: «מוכנות לחוץ: דירוג IP65 וגוף ABS מספקים הגנה מפני גשם, אבק ולחות.»
- Q: 2 או 6 יחידות?  
  A: בחרו 2 יחידות לנקודת עניין — או 6 יחידות כדי ליצור אפקט גינה שלם.  
  source: «בחרו 2 יחידות לנקודת עניין — או 6 יחידות כדי ליצור אפקט גינה שלם.»

**home_card_line:** (empty — none exists)

**Flags:**
- IMAGE CONTRADICTS THE DESCRIPTION: images[0] ("פאנל סולארי מוגדל") claims "עד 14 שעות תאורה", "+30% יעילות טעינה", "50,000 שעות עבודה"; the description says "עד כ־12 שעות". Only the description value is used; never render images[0].
- Certification list (CE, RoHS, UL, FCC, LVD) is unverifiable from the store — not mapped to any metafield.
- Description is the older plain format.

---

## 26. `powerful-solar-garden-light`

**מנורת גינה סולארית עוצמתית LED – תאורה אוטומטית לחוץ** · collection: path · תאורת-שביל-סולארית (שביל) · variants 1 · ₪179.9–179.9

Options: כמות: יחידה אחת

**power_source (proposed):** סולארי  — source: מקור מתח: סולארי

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating |  |  |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp |  |  |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material |  |  |
| dimensions |  |  |
| power_watt |  |  |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): מקור אור: LED · התקנה בהרכבה פשוטה · יחידה אחת באריזה · חיישן יום/לילה

**direct_answer** (16 words): מנורת גינה סולארית שמוסיפה אור ברור לחצר, לשביל, למדשאה ולכניסה — נטענת ביום ונדלקת אוטומטית עם החשכה.

**not_fit_for** (pair 1 · שביל, מדרגות ומעברים): המקום כמעט אינו מקבל אור יום
  Why: שביל/חצר/כניסה; סולארי (״ממקמים באזור שמקבל שמש״) — הסעיף נכון מילולית.

**faq**:
- Q: צריך חיבור לחשמל?  
  A: פאנל סולארי טוען את המנורה ביום, כך שאין צורך בחיבור קבוע לחשמל.  
  source: «פאנל סולארי טוען את המנורה ביום, כך שאין צורך בחיבור קבוע לחשמל.»
- Q: נדלקת לבד?  
  A: חיישן יום/לילה מאפשר פעולה אוטומטית בשעות הערב.  
  source: «חיישן יום/לילה מאפשר פעולה אוטומטית בשעות הערב.»
- Q: מתאימה לגשם?  
  A: בנויה לעבודה בסביבה חיצונית ובתנאי גשם, לחות ומזג אוויר משתנה.  
  source: «בנויה לעבודה בסביבה חיצונית ובתנאי גשם, לחות ומזג אוויר משתנה.»
- Q: איפה למקם?  
  A: ממקמים באזור שמקבל שמש, נותנים לה להיטען — ומהערב היא מתחילה לעבוד בשבילכם.  
  source: «ממקמים באזור שמקבל שמש, נותנים לה להיטען — ומהערב היא מתחילה לעבוד בשבילכם.»

**home_card_line:** (empty — none exists)

**Flags:**
- NO NUMERIC SPEC AT ALL: no IP, hours, lumens, watt, battery, size. The title promises "עוצמתית" with nothing to back it; "מתאימה לחוץ … בתנאי גשם" without an IP rating. All 12 spec fields empty.
- images[0] is clean (no baked claims); images[2] has a small caption (ledger).
- Description is the older plain format.

---

## 27. `dual-head-garden-light-10w-ip65`

**מנורת גינה דו־ראשית מתכווננת 180° – ‏10W IP65** · collection: spot · ספוטים-ופרוז-קטורים-סולאריים (גינה) · variants 1 · ₪189.9–189.9

Options: צבע גוף: שחור; הספק: 10W; גוון אור: אור חם

**power_source (proposed):** חשמל 220V  — source: מתח: AC 85–265V — המתח 220V הוא תווית הקטגוריה; התיאור אומר AC 85–265V.

| field | value | source quote (description / option / title) |
|-------|-------|---------------------------------------------|
| ip_rating | IP65 | דירוג אטימות: IP65 |
| charge_time_hours |  |  |
| light_hours |  |  |
| color_temp | גוון חם | גוון אור: חם |
| sensor_range_m |  |  |
| sensor_angle_deg |  |  |
| material | אלומיניום | גוף: אלומיניום |
| dimensions |  |  |
| power_watt | 10W | הספק: 10W |
| lumens |  |  |
| battery |  |  |
| light_modes |  |  |

Stated facts with no matching metafield (stay in the description): סיבוב: עד 180° · נורות כלולות · תקן CE · אחריות יצרן: שנתיים (ראו דגל)

**direct_answer** (19 words): מנורת גינה דו־ראשית 10W עם סיבוב של עד 180° — שליטה על פיזור האור בחצר, בשביל, ליד קיר או בכניסה.

**not_fit_for:** EMPTY — מוצר מחווט (AC 85–265V): סעיף זוג 4 (״נדרשת התקנה מיוחדת או חיבור קבוע״) אינו ״לא מתאים״ למוצר שדורש חיבור קבוע; סעיפי הסולארי לא חלים. ריק.

**faq**:
- Q: אפשר לכוון כל ראש בנפרד?  
  A: סיבוב של עד 180° מאפשר להפנות את האור לשני אזורים שונים וליצור כיסוי מדויק יותר.  
  source: «סיבוב של עד 180° מאפשר להפנות את האור לשני אזורים שונים וליצור כיסוי מדויק יותר.»
- Q: מתאימה לחוץ?  
  A: דירוג IP65 מספק עמידות מפני אבק, גשם ולחות לשימוש שוטף.  
  source: «דירוג IP65 מספק עמידות מפני אבק, גשם ולחות לשימוש שוטף.»
- Q: מה מקור המתח?  
  A: מתח: AC 85–265V · נורות כלולות.  
  source: «הספק: 10W · גוון אור: חם · צבע גוף: שחור · מתח: AC 85–265V · … · נורות כלולות»

**home_card_line:** (empty — none exists)

**Flags:**
- MAINS PRODUCT in collection `ספוטים-ופרוז-קטורים-סולאריים` (solar spotlights) — a buyer from that collection expects solar.
- Warranty wording ("אחריות יצרן: שנתיים") is under the owner ban — not mapped. "תקן CE" unverifiable.
- images[1–3] are on the never-use list (baked "ראש מתכוונן 180°", "אור חם ונעים") — consistent with the description, no extra numbers.
- Description is the older plain format.

---
