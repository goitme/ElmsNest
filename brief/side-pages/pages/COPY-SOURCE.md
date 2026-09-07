# COPY-SOURCE — the seven content pages, verbatim Hebrew copy as rendered on the dev theme (2026-09-07)

Sources: `brief/inventory/theme-src/sections/elmsnest-content-page.liquid` (the five hard-coded pages; unchanged in git since commit `fa74cb5`, and word-for-word identical to the 2026-09-02 mirrors) · `brief/inventory/page-shipping/index.html` (mirror of `/pages/shipping-delivery`, page body) · `brief/inventory/page-contact/index.html` (mirror of `/pages/contact-us`, Kalles form) · `brief/inventory/theme-src/templates/page.json`, `page.contact-us.json` (plumbing) · `brief/inventory/AUDIT-content-pages.md` (cross-check, «Worth keeping»). Page titles come from each mirror's `<title>` / `og:title`.

## Conventions of this file (not copy)

- Copy is verbatim. Nothing was corrected, translated or paraphrased — including anything that looks like a typo (see «Unsure» at the end).
- `<bdi dir="ltr">…</bdi>` wrappers are kept **literally, in code spans**, exactly where the source has them: `` `<bdi dir="ltr">1–3</bdi>` ``. Every digit and Latin token in the five Liquid pages and in the shipping body is wrapped this way; where a Latin token is **not** wrapped (the brand name «ElmsNest» on About and in the FAQ, everything on the contact page) it is noted.
- Links are written `[visible text](<href>)` with the href **exactly as in the source**, Liquid filters included; for Liquid hrefs, «→ renders as …» gives the path the 2026-09-02 mirror printed.
- Liquid variables of the section's `assign` block (l.18–23): `path_collection` = `collections['תאורת-שביל-סולארית']`, `wall_collection` = `collections['solar-wall-lights']`, `spot_collection` = `collections['ספוטים-ופרוז-קטורים-סולאריים']`, `decor_collection` = `collections['גרילנדות-ותאורה-דקורטיבית']`, `brand_image` = `images['pexels-taryn-elliott-4112233.jpg']`.
- Labels in parentheses such as (`.en-doc__role`), «Intro», «Note», «Row», «CTA» name the source element; they are mine. In a ruled row the printed numeral (`.en-doc__num`) comes first, then the `<strong>` title, then the `<p>` body on the next line. A colon or line break I put between a term and its value is layout, not copy; the source's own dashes (—, –, ־) are copy.
- «←» at the end of a collection row is a `<span aria-hidden="true">←</span>` in the source.
- The foot nav `nav.en-doc__foot` (`aria-label="ניווט משלים"`) sits outside the `case` but inside `{%- if editorial_page -%}`, so it prints on all five Liquid pages and on neither shipping nor contact. It is quoted under each of the five for document order.
- Each of the five Liquid pages also carries a hidden duplicate `<h1 class="sr-only hdt-pe-none">{{ page_title }}</h1>` from the `main-heading` section (the Shopify title), which the section hides with injected CSS. Listed once per page as «Shopify page title».

### Heading census (h1 / h2 / h3 printed by the section, plus the other copy units)

| page | h1 | h2 | h3 | other copy units |
|---|---|---|---|---|
| guide | 1 | 4 | 0 | role 1, TOC 4, collection rows 4, ruled rows 3 + 3 + 5, intro 2, note 1, buttons 2, foot nav 4 |
| why-solar | 1 | 3 | 2 | role 1, ruled rows 3 + 3, panel items 4 + 3, note 1, buttons 2, foot nav 4 |
| about | 1 | 4 | 0 | role 1, intro 1, ruled rows 3 + 3, collection rows 4, buttons 2, foot nav 4 |
| help-faq | 1 | 3 | 0 | role 1, TOC 3, Q&A 4 + 4 + 2 = 10, buttons 2, foot nav 4 |
| processing-time | 1 | 2 | 0 | role 1, plate cells 3, ruled rows 3, note 1, intro 1, buttons 2, foot nav 4 |
| shipping-delivery | 1 | 4 | 0 | ruled rows 2 + 3 + 3, notes 2, intro 1, buttons 2 |
| contact-us | 1 | 0 | 2 | 4 field labels + 1 submit, paragraphs 4, list items 3 |

---

## 1. Guide — `/pages/guide-garden-lighting`

- Path: `/pages/guide-garden-lighting` (canonical `https://elmsnest.com/pages/guide-garden-lighting`)
- Shopify page title: «מדריך לבחירת תאורה לגינה» — browser tab «מדריך לבחירת תאורה לגינה – ElmsNest»
- h1 the section prints: «בוחרים תאורת גינה לפי המקום — לא לפי התמונה»
- Source: `elmsnest-content-page.liquid` l.39–113, `{%- when 'guide-garden-lighting' -%}`

**Band (`header.en-doc__band`)**

h1: בוחרים תאורת גינה לפי המקום — לא לפי התמונה

Role (`p.en-doc__role`): ארבע החלטות קצרות: איפה צריך אור, מה הוא צריך לעשות, איזה מקור חשמל מתאים, ומה בודקים לפני שמזמינים.

**TOC (`nav.en-doc__toc`, `aria-label="תוכן המדריך"`)**

- [לפי מקום](#guide-place)
- [לפי מטרה](#guide-purpose)
- [מקור חשמל](#guide-power)
- [לפני ההזמנה](#guide-check)

### `<bdi dir="ltr">01</bdi>` · איפה צריך אור?

(`section#guide-place.en-doc__sec`)

Intro (`p.en-doc__intro`): בחרו את האזור הקרוב ביותר לצורך שלכם והמשיכו לקולקציה המתאימה. כל קולקציה מכילה רק מוצרים לאותו מקום.

Collection rows (`div.en-doc__links` → four `a.en-doc__link`; title `<strong>`, sub-line `<span>`, meta `span.en-doc__link-m`):

- **שביל, עמוד וגינה**
  לסימון הדרך, לערוגות ולפינות הגינה
  meta: `{% if path_collection.products_count > 0 %}` `<bdi dir="ltr">{{ path_collection.products_count }}</bdi>` מוצרים `{% endif %}` ←
  href `{{ path_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/תאורת-שביל-סולארית`; meta rendered «8 מוצרים ←» on 2026-09-02
- **כניסה וקיר**
  לדלת, לחזית ולאזורי מעבר
  meta: `{% if wall_collection.products_count > 0 %}` `<bdi dir="ltr">{{ wall_collection.products_count }}</bdi>` מוצרים `{% endif %}` ←
  href `{{ wall_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/solar-wall-lights`; meta rendered «6 מוצרים ←»
- **הארה ממוקדת**
  לעץ, לקיר, לפינה חשוכה או לשטח
  meta: `{% if spot_collection.products_count > 0 %}` `<bdi dir="ltr">{{ spot_collection.products_count }}</bdi>` מוצרים `{% endif %}` ←
  href `{{ spot_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/ספוטים-ופרוז-קטורים-סולאריים`; meta rendered «6 מוצרים ←»
- **מרפסת ואירוח**
  לאור חם ולאווירה בפינת הישיבה
  meta: `{% if decor_collection.products_count > 0 %}` `<bdi dir="ltr">{{ decor_collection.products_count }}</bdi>` מוצרים `{% endif %}` ←
  href `{{ decor_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/גרילנדות-ותאורה-דקורטיבית`; meta rendered «7 מוצרים ←»

### `<bdi dir="ltr">02</bdi>` · מה האור צריך לעשות?

(`section#guide-purpose.en-doc__sec`; `ol.en-doc__sched` — the numerals here are the Hebrew letters א / ב / ג, each still wrapped in `<bdi dir="ltr">`)

- `<bdi dir="ltr">א</bdi>` **לעזור להתמצא**
  לשביל, למדרגות ולאזורי מעבר שבהם חשוב לראות את הדרך.
- `<bdi dir="ltr">ב</bdi>` **להאיר נקודה**
  לכניסה, לקיר, לעץ או לאזור שרוצים להדגיש בצורה ברורה.
- `<bdi dir="ltr">ג</bdi>` **ליצור אווירה**
  למרפסת, לפרגולה ולפינת ישיבה שבהן האור הוא חלק מהחוויה. תאורת אווירה אינה מיועדת להאיר חזק — וזה בסדר, זה תפקידה.

### `<bdi dir="ltr">03</bdi>` · איזה מקור חשמל מתאים?

(`section#guide-power.en-doc__sec`)

Intro (`p.en-doc__intro`): הנתונים משתנים בין מוצרים. בדקו תמיד את עמוד המוצר, ואל תניחו שמפרט של מוצר אחד נכון גם לאחר.

- `<bdi dir="ltr">1</bdi>` **סולארי — למקום שמקבל שמש**
  מתאים כשרוצים להימנע מחיבור קבוע. הפאנל צריך אור יום של ממש: בצל כבוד רוב היום, ובימים מעוננים או בחורף, הביצועים יורדים. אם המקום כמעט לא מקבל שמש — אל תבחרו סולארי, יש פתרון מתאים יותר.
- `<bdi dir="ltr">2</bdi>` **סוללה או `<bdi dir="ltr">USB</bdi>` — לשליטה בטעינה**
  לא תלוי בשמש. בדקו איך טוענים או מחליפים סוללה, והאם שגרת התחזוקה מתאימה לכם.
- `<bdi dir="ltr">3</bdi>` **חיבור לחשמל — להתקנה קבועה**
  לעוצמה קבועה בלי תלות בטעינה. כשנדרשת עבודת חשמל — היעזרו בבעל מקצוע מוסמך.

### `<bdi dir="ltr">04</bdi>` · מה בודקים לפני ההזמנה?

(`section#guide-check.en-doc__sec`; five rows, title only, no body)

- `<bdi dir="ltr">01</bdi>` **מידות המוצר והשטח הזמין**
- `<bdi dir="ltr">02</bdi>` **מקור החשמל ואופן ההתקנה**
- `<bdi dir="ltr">03</bdi>` **מה כלול באריזה**
- `<bdi dir="ltr">04</bdi>` **נתוני אור ועמידות שמופיעים במפורש**
- `<bdi dir="ltr">05</bdi>` **התאמה למיקום המתוכנן**

Note (`p.en-doc__note`): פרט חשוב חסר בעמוד המוצר? אל תנחשו. [שלחו לנו את שם המוצר ואת השאלה](<{{ pages['contact-us'].url | default: routes.root_url }}>) — נבדוק לפני שתזמינו.
(link → renders as `/pages/contact-us`)

CTA (`div.en-doc__cta`):

- filled `a.en-doc__btn`: **לכל גופי התאורה** — href `{{ routes.all_products_collection_url }}` → renders as `/collections/all`
- outlined `a.en-doc__btn.en-doc__btn--ghost`: **שאלה לפני הזמנה** — href `{{ pages['contact-us'].url | default: routes.root_url }}` → renders as `/pages/contact-us`

Foot nav (`nav.en-doc__foot`, shared by the five Liquid pages):

- [לדף הבית](<{{ routes.root_url }}>) → `/`
- [לכל גופי התאורה](<{{ routes.all_products_collection_url }}>) → `/collections/all`
- [מדריך הבחירה](<{{ pages['guide-garden-lighting'].url | default: routes.root_url }}>) → `/pages/guide-garden-lighting` (on this page it links to itself)
- [יצירת קשר](<{{ pages['contact-us'].url | default: routes.root_url }}>) → `/pages/contact-us`

---

## 2. Why solar — `/pages/why-solar-lighting`

- Path: `/pages/why-solar-lighting` (canonical `https://elmsnest.com/pages/why-solar-lighting`)
- Shopify page title: «למה תאורה סולארית?» — browser tab «למה תאורה סולארית? – ElmsNest»
- h1 the section prints: «למה תאורה סולארית — ומתי לא»
- Source: `elmsnest-content-page.liquid` l.114–169, `{%- when 'why-solar-lighting' -%}`. No TOC on this page.

**Band (`header.en-doc__band`)**

h1: למה תאורה סולארית — ומתי לא

Role (`p.en-doc__role`): היתרון: פחות תלות בחיבור קבוע לחשמל. ההתאמה תלויה בשמש שהמקום מקבל, במטרת האור ובנתוני המוצר הספציפי.

### איך זה עובד בפועל

(`section.en-doc__sec`, `ol.en-doc__sched`)

- `<bdi dir="ltr">1</bdi>` **ביום**
  הפאנל הסולארי נטען מאור היום. צל, כיוון הפאנל ועונת השנה משפיעים על הטעינה.
- `<bdi dir="ltr">2</bdi>` **בערב**
  התאורה נדלקת ועובדת על האנרגיה שנאגרה, בהתאם למוצר ולתנאי הטעינה.
- `<bdi dir="ltr">3</bdi>` **מה זה אומר**
  השמש היא חלק מהמפרט. בימים מעוננים או בחורף הביצועים עשויים להיות חלשים יותר — זו לא תקלה, זה אופי הפתרון.

### מתי זה מתאים — ומתי עדיף פתרון אחר

(`section.en-doc__sec` → `div.en-doc__grid2` with two `div.en-doc__panel`, each an h3 + `ul.en-doc__list`)

#### יכול להתאים כאשר

- המיקום מקבל חשיפה טובה לאור יום
- לא רוצים חיבור קבוע לחשמל או שאין נקודה קרובה
- המטרה היא אווירה, סימון דרך או הארה נקודתית
- נתוני המוצר תואמים לשימוש המתוכנן

#### עדיף פתרון אחר כאשר

- המקום כמעט ואינו מקבל אור יום — סולארי לא יספיק שם
- נדרש אור חזק וקבוע לאורך כל הלילה — תאורה סולארית לא תמיד מחליפה תאורה חשמלית חזקה
- יש דרישות התקנה מיוחדות — אז חיבור קבוע עם בעל מקצוע, או מוצר נטען ב־`<bdi dir="ltr">USB</bdi>`

### שלוש בדיקות לפני שבוחרים

(`section.en-doc__sec`, `ol.en-doc__sched`; three rows, title only)

- `<bdi dir="ltr">1</bdi>` **כמה אור יום מגיע למקום?**
- `<bdi dir="ltr">2</bdi>` **האם המטרה היא אווירה, התמצאות או הארה ממוקדת?**
- `<bdi dir="ltr">3</bdi>` **אילו נתונים מופיעים במפורש בעמוד המוצר?**

Note (`p.en-doc__note`): חלק מהמוצרים בחנות מיועדים בעיקר לאווירה ולא לאור חזק. אם הנתון שחשוב לכם לא מופיע בעמוד המוצר — שאלו אותנו לפני ההזמנה.

CTA (`div.en-doc__cta`):

- filled: **איך בוחרים תאורה לגינה?** — href `{{ pages['guide-garden-lighting'].url | default: routes.root_url }}` → renders as `/pages/guide-garden-lighting`
- outlined: **לכל גופי התאורה** — href `{{ routes.all_products_collection_url }}` → renders as `/collections/all`

Foot nav (`nav.en-doc__foot`, shared):

- [לדף הבית](<{{ routes.root_url }}>) → `/`
- [לכל גופי התאורה](<{{ routes.all_products_collection_url }}>) → `/collections/all`
- [מדריך הבחירה](<{{ pages['guide-garden-lighting'].url | default: routes.root_url }}>) → `/pages/guide-garden-lighting`
- [יצירת קשר](<{{ pages['contact-us'].url | default: routes.root_url }}>) → `/pages/contact-us`

---

## 3. About — `/pages/מי-אנחנו`

- Path: `/pages/מי-אנחנו` (canonical `https://elmsnest.com/pages/%d7%9e%d7%99-%d7%90%d7%a0%d7%97%d7%a0%d7%95`)
- Shopify page title: «מי אנחנו» — browser tab «מי אנחנו – ElmsNest»
- h1 the section prints: «רק תאורת חוץ. וזה בכוונה.»
- Source: `elmsnest-content-page.liquid` l.204–254, `{%- when 'מי-אנחנו' -%}`. No TOC on this page.

**Band (`header.en-doc__band.en-doc__band--media`)** — carries the only image in the family, with **no copy** (`alt: ''`):
`{{ brand_image | image_url: width: 2200 | image_tag: class: 'en-doc__band-img', loading: 'eager', fetchpriority: 'high', widths: '800,1200,1600,2200', sizes: '100vw', alt: '' }}` (inside `{%- if brand_image != blank -%}`), then `span.en-doc__band-shade` (`aria-hidden="true"`).

h1: רק תאורת חוץ. וזה בכוונה.

Role (`p.en-doc__role`): אנחנו עוזרים להתאים גוף תאורה למקום שלכם — וגם אומרים כשמשהו לא מתאים.

### למה הקמנו את ElmsNest

(`section.en-doc__sec`; «ElmsNest» in this h2 and in the paragraph below is **not** wrapped in `<bdi>` — the only unwrapped Latin in the five Liquid pages, together with «ElmsNest» in the first FAQ answer)

Intro (`p.en-doc__intro`): בחירת תאורה באינטרנט יכולה להיות מבלבלת: מקורות חשמל שונים, דרכי התקנה שונות ומוצרים שנראים דומים אך מיועדים לצרכים אחרים. ElmsNest עוסקת בתחום אחד — תאורת חוץ — ומארגנת את הבחירה לפי מקום, מטרה ואופן שימוש, כדי שיהיה ברור מה מתאים לפני שקונים.

### העקרונות שמכוונים אותנו

(`section.en-doc__sec`, `ol.en-doc__sched`)

- `<bdi dir="ltr">01</bdi>` **בהירות לפני הבטחות**
  כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה.
- `<bdi dir="ltr">02</bdi>` **בחירה לפי צורך**
  העיצוב חשוב, אך ההתאמה למקום ולאופן ההתקנה חשובה לא פחות.
- `<bdi dir="ltr">03</bdi>` **שאלה לפני הזמנה**
  אם פרט חיוני חסר, עדיף לעצור ולבדוק לפני שקונים.

### מה זה אומר בפועל

(`section.en-doc__sec`, `ol.en-doc__sched`)

- `<bdi dir="ltr">1</bdi>` **אין אצלנו קטגוריה אחרת**
  לא מוצרי בית, לא גאדג׳טים — תאורת חוץ בלבד: סולארית, נטענת, בסוללה או בחיבור לחשמל.
- `<bdi dir="ltr">2</bdi>` **המפרט לפני הקנייה**
  בכל עמוד מוצר: מקור החשמל, המידות ואופן ההתקנה. נתון שלא מופיע — לא ממציאים.
- `<bdi dir="ltr">3</bdi>` **וכשמשהו לא מתאים — אומרים**
  במדריכים שלנו כתוב גם מתי תאורה סולארית היא לא הבחירה הנכונה. עדיף לקוח שקנה נכון מלקוח שהתאכזב.

### מה תמצאו בחנות

(`section.en-doc__sec` → `div.en-doc__links`; four rows with a `<strong>` title and «←» only — no sub-line, no count)

- **שביל, עמוד וגינה** ← — href `{{ path_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/תאורת-שביל-סולארית`
- **תאורת קיר** ← — href `{{ wall_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/solar-wall-lights`
- **ספוטים ותאורה ניידת** ← — href `{{ spot_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/ספוטים-ופרוז-קטורים-סולאריים`
- **אווירה ודקורציה** ← — href `{{ decor_collection.url | default: routes.all_products_collection_url }}` → renders as `/collections/גרילנדות-ותאורה-דקורטיבית`

CTA (`div.en-doc__cta`):

- filled: **לכל גופי התאורה** — href `{{ routes.all_products_collection_url }}` → renders as `/collections/all`
- outlined: **איך בוחרים תאורה לגינה?** — href `{{ pages['guide-garden-lighting'].url | default: routes.root_url }}` → renders as `/pages/guide-garden-lighting`

Foot nav (`nav.en-doc__foot`, shared):

- [לדף הבית](<{{ routes.root_url }}>) → `/`
- [לכל גופי התאורה](<{{ routes.all_products_collection_url }}>) → `/collections/all`
- [מדריך הבחירה](<{{ pages['guide-garden-lighting'].url | default: routes.root_url }}>) → `/pages/guide-garden-lighting`
- [יצירת קשר](<{{ pages['contact-us'].url | default: routes.root_url }}>) → `/pages/contact-us`

---

## 4. FAQ — `/pages/help-faq`

- Path: `/pages/help-faq` (canonical `https://elmsnest.com/pages/help-faq`)
- Shopify page title: «שאלות נפוצות» — browser tab «שאלות נפוצות – ElmsNest»
- h1 the section prints: «שאלות נפוצות» (same text as the Shopify title)
- Source: `elmsnest-content-page.liquid` l.255–332, `{%- when 'help-faq' -%}`. Ten native `<details>` in three groups; only the first is `open`.

**Band (`header.en-doc__band`)**

h1: שאלות נפוצות

Role (`p.en-doc__role`): תשובות קצרות לפני ואחרי ההזמנה. לא מצאתם תשובה? [כתבו לנו](<{{ pages['contact-us'].url | default: routes.root_url }}>).
(link → renders as `/pages/contact-us`)

**TOC (`nav.en-doc__toc`, `aria-label="נושאי השאלות"`)**

- [מוצרים והתאמה](#faq-products)
- [הזמנות ומשלוח](#faq-orders)
- [ביטול והחזרות](#faq-policies)

### מוצרים והתאמה

(`section#faq-products.en-doc__sec` → `div.en-doc__faq`)

- **Q:** האם כל המוצרים בחנות סולאריים? (`<details open>`)
  A: לא. ElmsNest מציעה תאורת חוץ בלבד, אבל מקורות החשמל שונים: סולארי, נטען ב־`<bdi dir="ltr">USB</bdi>`, סוללות או חיבור לחשמל. בדקו בכל עמוד מוצר את מקור החשמל ואופן ההתקנה.
  («ElmsNest» here is not wrapped in `<bdi>`; «USB» is.)
- **Q:** האם תאורה סולארית עובדת גם בחורף?
  A: היא עובדת, אבל חלש יותר: בימים מעוננים ובחורף הפאנל נטען פחות. אם המקום כמעט לא מקבל שמש — עדיף פתרון אחר, ואנחנו אומרים את זה גם כשזה אומר לוותר על מכירה. [מתי תאורה סולארית מתאימה ומתי לא](<{{ pages['why-solar-lighting'].url | default: routes.root_url }}>).
  (link → renders as `/pages/why-solar-lighting`)
- **Q:** איך בוחרים תאורה שמתאימה למקום?
  A: מתחילים במקום ובמטרת האור, ורק אז בודקים מקור חשמל, מידות ואופן התקנה. [מדריך הבחירה המלא](<{{ pages['guide-garden-lighting'].url | default: routes.root_url }}>) עובר על זה בארבעה צעדים.
  (link → renders as `/pages/guide-garden-lighting`)
- **Q:** נתון שחשוב לי לא מופיע בעמוד המוצר. מה עושים?
  A: לא מנחשים. שלחו לנו את שם המוצר ואת השאלה לפני ההזמנה — נבדוק את המידע הזמין ונחזור אליכם. אם נתון אינו מופיע, איננו מציגים אותו כעובדה.

### הזמנות ומשלוח

(`section#faq-orders.en-doc__sec` → `div.en-doc__faq`)

- **Q:** כמה עולה המשלוח?
  A: משלוח לנקודת איסוף בישראל — חינם. שליח עד הבית — `<bdi dir="ltr">29.90</bdi>` ₪. המחיר הסופי מוצג בקופה לפני התשלום.
- **Q:** תוך כמה זמן ההזמנה מגיעה?
  A: הזמן הכולל המשוער הוא `<bdi dir="ltr">8–17</bdi>` ימי עסקים: `<bdi dir="ltr">1–3</bdi>` ימי טיפול ועוד `<bdi dir="ltr">7–14</bdi>` ימי משלוח. הפירוט המלא ב[מדיניות המשלוחים](<{{ shop.shipping_policy.url | default: routes.root_url }}>).
  (link → renders as `/policies/shipping-policy`; the prefix «ב» is attached directly to the link text)
- **Q:** איך עוקבים אחרי ההזמנה?
  A: כשמספר מעקב זמין, הוא נשלח לאימייל או לטלפון שנמסרו בהזמנה. לפעמים נדרשים כמה ימים עד שהמעקב מתעדכן אצל חברת השילוח.
- **Q:** איך פונים לגבי הזמנה קיימת?
  A: דרך [עמוד יצירת הקשר](<{{ pages['contact-us'].url | default: routes.root_url }}>), עם מספר ההזמנה והאימייל ששימש לרכישה.
  (link → renders as `/pages/contact-us`)

### ביטול והחזרות

(`section#faq-policies.en-doc__sec` → `div.en-doc__faq`)

- **Q:** אפשר לבטל עסקה אחרי שהזמנתי?
  A: כן. בעסקת מכר מרחוק אפשר למסור הודעת ביטול עד `<bdi dir="ltr">14</bdi>` ימים מקבלת המוצר, לפי חוק הגנת הצרכן. כאשר הדין מאפשר גביית דמי ביטול, שיעורם `<bdi dir="ltr">5%</bdi>` ממחיר העסקה או `<bdi dir="ltr">100</bdi>` ₪ — הנמוך מביניהם. הפרטים המלאים ב[מדיניות הביטולים וההחזרים](<{{ shop.refund_policy.url | default: routes.root_url }}>).
  (link → renders as `/policies/refund-policy`; prefix «ב» attached to the link text)
- **Q:** קיבלתי מוצר פגום או שגוי. מה עושים?
  A: פנו אלינו בהקדם עם מספר ההזמנה ותמונות של הבעיה. בביטול שנובע מפגם, מאי־התאמה או מאי־אספקה במועד — לא נגבים דמי ביטול. אל תשלחו מוצר חזרה לפני שקיבלתם מאיתנו הנחיות כתובות.

CTA (`div.en-doc__cta`, inside `#faq-policies`):

- filled: **ליצירת קשר** — href `{{ pages['contact-us'].url | default: routes.root_url }}` → renders as `/pages/contact-us`
- outlined: **למדיניות המלאה** — href `{{ shop.refund_policy.url | default: routes.root_url }}` → renders as `/policies/refund-policy`

Foot nav (`nav.en-doc__foot`, shared):

- [לדף הבית](<{{ routes.root_url }}>) → `/`
- [לכל גופי התאורה](<{{ routes.all_products_collection_url }}>) → `/collections/all`
- [מדריך הבחירה](<{{ pages['guide-garden-lighting'].url | default: routes.root_url }}>) → `/pages/guide-garden-lighting`
- [יצירת קשר](<{{ pages['contact-us'].url | default: routes.root_url }}>) → `/pages/contact-us`

---

## 5. Processing time — `/pages/processing-time`

- Path: `/pages/processing-time` (canonical `https://elmsnest.com/pages/processing-time`)
- Shopify page title: «זמני טיפול בהזמנה» — browser tab «זמני טיפול בהזמנה – ElmsNest»
- h1 the section prints: «זמני טיפול בהזמנה» (same text as the Shopify title)
- Source: `elmsnest-content-page.liquid` l.170–203, `{%- when 'processing-time' -%}`. No TOC on this page.

**Band (`header.en-doc__band`)**

h1: זמני טיפול בהזמנה

Role (`p.en-doc__role`): המספרים כאן זהים למדיניות המשלוחים המלאה — אין הבטחות נפרדות.

Plate (`dl.en-doc__plate`, `aria-label="זמני טיפול ואספקה"`; three `div.en-doc__cell`, each `<dt>` then `<dd>`):

- טיפול בהזמנה: `<bdi dir="ltr">1–3</bdi>` ימי עסקים
- זמן הובלה: `<bdi dir="ltr">7–14</bdi>` ימי עסקים
- סה״כ משוער: `<bdi dir="ltr">8–17</bdi>` ימי עסקים

### מה קורה אחרי שהזמנתם

(`section.en-doc__sec`, `ol.en-doc__sched`)

- `<bdi dir="ltr">1</bdi>` **ההזמנה נקלטת**
  אישור נשלח לאימייל שהוזן ברכישה. בדקו שהשם, הטלפון והכתובת נכונים — ואם יש טעות, פנו אלינו מיד.
- `<bdi dir="ltr">2</bdi>` **ההזמנה מטופלת ונמסרת לשילוח**
  עד `<bdi dir="ltr">3</bdi>` ימי עסקים. כשמספר מעקב זמין — נשלח לכם אותו.
- `<bdi dir="ltr">3</bdi>` **ההזמנה בדרך**
  זמן ההובלה המשוער הוא `<bdi dir="ltr">7–14</bdi>` ימי עסקים. הזמנה עם כמה פריטים עשויה להגיע בחבילות נפרדות, בלי חיוב נוסף.

Note (`p.en-doc__note`): יום עסקים: ראשון עד חמישי, למעט ערבי חג, חגים וימי שבתון.

### עברו `<bdi dir="ltr">17</bdi>` ימי עסקים והחבילה לא הגיעה?

(`section.en-doc__sec`)

Intro (`p.en-doc__intro`): פנו אלינו עם מספר ההזמנה והאימייל ששימש לרכישה — נבדוק את המשלוח מול חברת השילוח ונחזור אליכם עם תשובה.

CTA (`div.en-doc__cta`):

- filled: **ליצירת קשר** — href `{{ pages['contact-us'].url | default: routes.root_url }}` → renders as `/pages/contact-us`
- outlined: **למדיניות המשלוחים המלאה** — href `{{ shop.shipping_policy.url | default: routes.root_url }}` → renders as `/policies/shipping-policy`

Foot nav (`nav.en-doc__foot`, shared):

- [לדף הבית](<{{ routes.root_url }}>) → `/`
- [לכל גופי התאורה](<{{ routes.all_products_collection_url }}>) → `/collections/all`
- [מדריך הבחירה](<{{ pages['guide-garden-lighting'].url | default: routes.root_url }}>) → `/pages/guide-garden-lighting`
- [יצירת קשר](<{{ pages['contact-us'].url | default: routes.root_url }}>) → `/pages/contact-us`

---

## 6. Shipping & returns — `/pages/shipping-delivery`

- Path: `/pages/shipping-delivery` (canonical `https://elmsnest.com/pages/shipping-delivery`)
- Shopify page title: «משלוחים והחזרות» — browser tab «משלוחים והחזרות – ElmsNest»
- h1 the template prints: «משלוחים והחזרות» — by `main-heading` (`templates/page.json` → block `_heading_liquid`, text `{{ page_title }}`, 4xl): `<h1 class="sr-only hdt-pe-none">משלוחים והחזרות</h1>` plus the visible heading block «משלוחים והחזרות» (the audit measured it invisible, cream on cream). The `elmsnest-content-page` section prints **nothing** for this handle (the mirror's `__editorial` section is empty).
- Source of the copy: the **Shopify page body** (`{{ page.content }}` printed by `main-page`, `full_width: true`), mirrored in `page-shipping/index.html` → `section#shopify-section-template--21567616352430__main` → `div.en-doc[dir="rtl"]`. The hrefs here are literal paths (page body HTML, not Liquid). No band, no role line, no TOC, no shell, no foot nav.

### עלויות משלוח

(`section.en-doc__sec` with inline `style="border-block-start:0"`, `ol.en-doc__sched`)

- `<bdi dir="ltr">1</bdi>` **משלוח לנקודת איסוף בישראל — חינם**
  לכל הזמנה, בלי מינימום.
- `<bdi dir="ltr">2</bdi>` **שליח עד הבית — `<bdi dir="ltr">29.90</bdi>` ₪**
  אפשרות המשלוח והמחיר הסופי מוצגים בקופה לפני התשלום.

### זמני טיפול ואספקה

(`section.en-doc__sec`, `ol.en-doc__sched`)

- `<bdi dir="ltr">1</bdi>` **טיפול בהזמנה: `<bdi dir="ltr">1–3</bdi>` ימי עסקים**
  מרגע ההזמנה ועד המסירה לחברת השילוח.
- `<bdi dir="ltr">2</bdi>` **זמן הובלה משוער: `<bdi dir="ltr">7–14</bdi>` ימי עסקים**
  מוצרים עשויים להישלח ממחסנים מחוץ לישראל. הזמנה עם כמה פריטים עשויה להגיע בחבילות נפרדות, בלי חיוב נוסף.
- `<bdi dir="ltr">3</bdi>` **סה״כ משוער: `<bdi dir="ltr">8–17</bdi>` ימי עסקים**
  ממועד ההזמנה ועד קבלתה. יום עסקים: ראשון עד חמישי, למעט ערבי חג, חגים וימי שבתון.

Note (`p.en-doc__note`): כשמספר מעקב זמין, נשלח אותו לאימייל או לטלפון שנמסרו בהזמנה. לעיתים נדרשים כמה ימים עד שהמעקב מתעדכן אצל חברת השילוח. המספרים כאן זהים ל[מדיניות המשלוחים המלאה](/policies/shipping-policy).
(prefix «ל» attached to the link text)

### ביטול עסקה והחזרות

(`section.en-doc__sec`, `ol.en-doc__sched`)

- `<bdi dir="ltr">1</bdi>` **ביטול עד `<bdi dir="ltr">14</bdi>` ימים מקבלת המוצר**
  לפי חוק הגנת הצרכן. כאשר הדין מאפשר דמי ביטול — `<bdi dir="ltr">5%</bdi>` ממחיר העסקה או `<bdi dir="ltr">100</bdi>` ₪, הנמוך מביניהם.
- `<bdi dir="ltr">2</bdi>` **מוצר פגום, חסר או שגוי**
  פנו אלינו בהקדם עם מספר ההזמנה ותמונות ברורות של הבעיה. בביטול שנובע מפגם, מאי־התאמה או מאי־אספקה במועד — לא נגבים דמי ביטול.
- `<bdi dir="ltr">3</bdi>` **אל תשלחו מוצר לפני קבלת הנחיות**
  פתחו בקשת החזרה וקבלו מאיתנו הנחיות כתובות. כתובת ההחזרה נמסרת בהתאם למוצר ולמסלול המשלוח.

Note (`p.en-doc__note`): הנוסח המחייב: [מדיניות הביטולים, ההחזרות וההחזרים](/policies/refund-policy).

### עברו `<bdi dir="ltr">17</bdi>` ימי עסקים והחבילה לא הגיעה?

(`section.en-doc__sec`)

Intro (`p.en-doc__intro`): פנו אלינו עם מספר ההזמנה, האימייל ששימש לרכישה ותיאור קצר — נבדוק מול חברת השילוח ונחזור אליכם עם תשובה.

CTA (`div.en-doc__cta`):

- filled `a.en-doc__btn`: **ליצירת קשר** — href `/pages/contact-us`
- outlined `a.en-doc__btn.en-doc__btn--ghost`: **מה קורה אחרי שהזמנתם** — href `/pages/processing-time`

(No foot nav; the night footer follows directly.)

---

## 7. Contact — `/pages/contact-us`

- Path: `/pages/contact-us` (canonical `https://elmsnest.com/pages/contact-us`)
- Shopify page title: «יצירת קשר» — browser tab «יצירת קשר – ElmsNest»
- h1 the template prints: «יצירת קשר» — `templates/page.contact-us.json` → `main-heading` (`use_dynamic_source: true`, block text `{{ page.title }}`, 2xl, `uppercase: true` → class `hdt-uppercase`, no effect on Hebrew): `<h1 class="sr-only hdt-pe-none">יצירת קשר</h1>` plus the visible heading block «יצירת קשר» (the audit measured it invisible, cream on cream).
- Page body (`{{ page.content }}`): this template has **no** `main-page` section, so the Shopify page body — whatever it holds — is not rendered and does not appear in the mirror. Nothing to quote.
- Source of the copy: `contact-form` section, two `_contact_col` blocks (`page-contact/index.html` → `div#shopify-section-template--21567616221358__contact_form_zzPDf3`; the rich text is also verbatim in `page.contact-us.json` → `liquid_XznGcy.settings.text`). **No `<bdi>` wrappers anywhere on this page.**

### Column 1 — the Kalles contact form (`_contact_col` `contact_col_39rTtM`)

Blocks in order: spacer 20 px → text block (setting `text: ""`, prints an empty `div`) → spacer 20 px → `_contact-form` block (`success_message: ""`).

Form: `{% form 'contact' %}` → `<form method="post" action="/contact#…" class="contact-form">`, hidden `form_type=contact`, `utf8=✓`. Four fields, each `div.hdt-form-input_wrap` with a `<label>` above the input; **no placeholder on any field**:

| # | Label (visible) | Control | Attributes |
|---|---|---|---|
| 1 | שם מלא | `<input type="text" name="contact[name]">` | `required` |
| 2 | כתובת מייל | `<input type="email" name="contact[email]">` | `required`, `aria-required="true"`, `autocorrect="off"`, `autocapitalize="off"` |
| 3 | מספר טלפון | `<input type="tel" name="contact[phone]">` | `required`, `pattern="[0-9\-]*"` |
| 4 | הודעה (נדרשת) | `<textarea rows="20" name="contact[body]" class="hdt-input-textarea">` | `required` |

Submit: `<input type="submit" value="שליחה">` — classes `hdt-btn hdt-btn-outline hdt-btn-full-width hdt-contact-form_btn hdt-font-semibold` (outlined, full width).

Success / error text after posting: not in the mirror; the block's `success_message` setting is empty, so whatever prints comes from the Kalles block + theme locale (neither archived in `theme-src`).

### Column 2 — rich text (`_contact_col` `contact_col_gcMnTL`, `_liquid` block `liquid_XznGcy`)

Blocks in order: spacer 20 px → text block (empty) → spacer 20 px → `_liquid` block, `text_size: base`, `font_weight: medium`, `ffamily: --f_family_1`, wrapped in `<div dir="rtl" style="text-align: right; line-height: 1.8;">`:

#### שאלה לפני הזמנה?

(`<h3 style="font-size: 20px; font-weight: 700; margin: 0 0 14px;">`)

זה בדיוק בשבילנו. כדי שנוכל לבדוק התאמה למקום שלכם, צרפו להודעה:

(`<ul style="margin: 0 0 18px; padding-inline-start: 20px;">`)

- תמונה של המקום שרוצים להאיר
- קישור למוצר ששוקלים
- השאלה עצמה — למשל כמה שמש המקום מקבל, או אילו מידות דרושות

ואם משהו לא מתאים למקום — נגיד את זה מראש.

#### פנייה על הזמנה קיימת?

(`<h3 style="font-size: 20px; font-weight: 700; margin: 22px 0 14px;">`)

ציינו מספר הזמנה ואת האימייל ששימש לרכישה, ונבדוק את הפנייה.

(`<p style="margin-top: 18px;">`, one paragraph with a `<br>`)

**דוא״ל:** info@elmsnest.com
**ElmsNest**, ישראל

(No foot nav; the night footer follows directly.)

---

## What the audit said to keep

Verbatim from `brief/inventory/AUDIT-content-pages.md` (dev theme 154726400174, mirrored 2026-09-02), the «Worth keeping» bullets of each page section, attributed to the audit:

### 1. page-guide — «Worth keeping» (audit §1)

- The four-decision spine (place → purpose → power → checks) and all of its copy — `elmsnest-content-page.liquid` l.39–113.
- `.en-doc__links` rows fed by `collections['תאורת-שביל-סולארית'|'solar-wall-lights'|'ספוטים-ופרוז-קטורים-סולאריים'|'גרילנדות-ותאורה-דקורטיבית'].products_count` — the only live data in the family.
- The "missing spec → ask before ordering" fallback (`pages['contact-us'].url`) and `<bdi dir="ltr">` on every Latin token / numeral.
- Radius 0, hairline tokens `--rule/--rule-strong/--rule-night` (values must change, the idea stays).

### 2. page-why-solar — «Worth keeping» (audit §2)

- The honest "sun is part of the spec" framing and the suits / does-not-suit pairing (`elmsnest-content-page.liquid` l.114–169) — content, not the box.
- Day/evening/meaning three-beat (it is a storyboard for the lamp-lights-on motion).
- Cross-links to the guide and the collections.

### 3. page-about — «Worth keeping» (audit §3)

- The h1 "רק תאורת חוץ. וזה בכוונה." — the strongest line in the family — and the role line.
- The three principles and "עדיף לקוח שקנה נכון מלקוח שהתאכזב" (`elmsnest-content-page.liquid` l.204–254).
- The media-band mechanics (`images[...] | image_url: width: 2200 | image_tag: loading:'eager', fetchpriority:'high'`, l.207) — swap the image for a real lamp that lights on arrival.

### 4. page-shipping — «Worth keeping» (audit §4)

- All of the copy, verbatim (it mirrors the legal policies; `shop.shipping_policy.url` / `shop.refund_policy.url` links included).
- The "17 business days passed?" escalation block and the cross-link to `processing-time`.
- The numbered-row markup with `<bdi>` — reusable data, needs a real ground and a column.

### 5. page-faq — «Worth keeping» (audit §5)

- The 10 Q&A texts — accurate, link-rich, consistent with the policies (`elmsnest-content-page.liquid` l.255–332).
- Native `<details>/<summary>` (no JS, keyboard-accessible, works when the theme JS fails as it does in the mirror).
- The three-group order (fit → order/ship → cancel/return).

### 6. page-contact — «Worth keeping» (audit §6)

- The instruction copy (photo / product link / the question; order-number + email for existing orders) — `templates/page.contact-us.json` `_contact_col` rich text.
- Shopify form mechanics (`contact[name]/[email]/[phone]/[body]`, `/contact` POST) and `info@elmsnest.com`.
- `sections/contact-form.liquid` as a schema reference for a rebuilt section (blocks, spacing settings).

### 7. page-processing — «Worth keeping» (audit §7)

- The plate data as `<dl>` with `<bdi>` numerals (`elmsnest-content-page.liquid` l.170–203) — the data, not the box.
- The three-step "what happens after you order" copy and the 17-day escalation block.
- Strict consistency with the shipping policy (one source of numbers).

(The audit's family summary, point 4, adds: «The copy is honest, complete and reusable verbatim — every consumer term is present with `<bdi>` numerals: all of them on shipping-delivery; 1–3 / 7–14 / 8–17 on processing; prices, days, 14-day / 5 % or 100 ₪ inside FAQ accordions; "ask before ordering" on the guide.» Its one shipping-page caveat: the page body has «no shell, band or foot nav» and runs «flush to the viewport edge with zero gutter» — a dress problem, not a copy problem.)

---

## Facts that must stay byte-identical

The figures below are the only numbers in the seven pages. Each is quoted in its exact source form (with its `<bdi>` wrapper where the source has one) and the page(s) it appears on. Any redesign must print these strings unchanged; the pages themselves say the numbers «זהים למדיניות המשלוחים המלאה — אין הבטחות נפרדות».

| Fact | Exact source string(s) | Appears on |
|---|---|---|
| Pickup point in Israel is free («0 ₪» is never written — the word is «חינם») | «משלוח לנקודת איסוף בישראל — חינם» | shipping-delivery (row 1 title, + «לכל הזמנה, בלי מינימום.»), help-faq («כמה עולה המשלוח?») |
| Courier to the door 29.90 ₪ | «שליח עד הבית — `<bdi dir="ltr">29.90</bdi>` ₪» | shipping-delivery (row 2 title), help-faq («כמה עולה המשלוח?») |
| Processing 1–3 business days | «`<bdi dir="ltr">1–3</bdi>` ימי עסקים» / «`<bdi dir="ltr">1–3</bdi>` ימי טיפול» | processing-time (plate «טיפול בהזמנה»), shipping-delivery («טיפול בהזמנה: … ימי עסקים»), help-faq («תוך כמה זמן ההזמנה מגיעה?») |
| …and its «up to 3» form | «עד `<bdi dir="ltr">3</bdi>` ימי עסקים» | processing-time (row 2 «ההזמנה מטופלת ונמסרת לשילוח») |
| Transit 7–14 business days | «`<bdi dir="ltr">7–14</bdi>` ימי עסקים» / «`<bdi dir="ltr">7–14</bdi>` ימי משלוח» | processing-time (plate «זמן הובלה» + row 3 «ההזמנה בדרך»), shipping-delivery («זמן הובלה משוער: …»), help-faq («תוך כמה זמן ההזמנה מגיעה?») |
| Total 8–17 business days | «`<bdi dir="ltr">8–17</bdi>` ימי עסקים» | processing-time (plate «סה״כ משוער»), shipping-delivery («סה״כ משוער: …»), help-faq («תוך כמה זמן ההזמנה מגיעה?») |
| 14 days to cancel from receipt | «עד `<bdi dir="ltr">14</bdi>` ימים מקבלת המוצר» | shipping-delivery (row 1 «ביטול עד … ימים מקבלת המוצר»), help-faq («אפשר לבטל עסקה אחרי שהזמנתי?») |
| Cancellation fee 5 % or 100 ₪, the lower | «`<bdi dir="ltr">5%</bdi>` ממחיר העסקה או `<bdi dir="ltr">100</bdi>` ₪» (shipping: «, הנמוך מביניהם»; FAQ: « — הנמוך מביניהם») | shipping-delivery (row 1 body), help-faq («אפשר לבטל עסקה אחרי שהזמנתי?») |
| 17 business days → escalate | «עברו `<bdi dir="ltr">17</bdi>` ימי עסקים והחבילה לא הגיעה?» | processing-time (h2), shipping-delivery (h2) |
| Business-day definition | «יום עסקים: ראשון עד חמישי, למעט ערבי חג, חגים וימי שבתון.» | processing-time (note), shipping-delivery (row 3 body) |
| Warehouses outside Israel | «מוצרים עשויים להישלח ממחסנים מחוץ לישראל.» | shipping-delivery only |
| No cancellation fee on defect / mismatch / late delivery | «בביטול שנובע מפגם, מאי־התאמה או מאי־אספקה במועד — לא נגבים דמי ביטול.» | shipping-delivery (row 2), help-faq («קיבלתי מוצר פגום או שגוי. מה עושים?») |
| Live product counts (the only live numbers) | `<bdi dir="ltr">{{ path_collection.products_count }}</bdi>` etc. — 8 / 6 / 6 / 7 on 2026-09-02 | guide (four collection rows) |
| Contact email | «info@elmsnest.com» | contact-us (column 2) |
| Section numerals (labels, not facts) | 01–04 (guide h2s), א/ב/ג, 1–3, 01–05 (rows) — every one in `<bdi dir="ltr">` | guide, why-solar, about, processing-time, shipping-delivery |

---

## Unsure / flagged while extracting (nothing was changed)

1. Guide, section 03, row 1: the source reads «בצל כבוד רוב היום» — probably a typo for «כבד»; kept verbatim as the task requires.
2. Guide, section 02: the Hebrew letters א / ב / ג are wrapped in `<bdi dir="ltr">` like digits; reported as-is.
3. Contact form labels («שם מלא», «כתובת מייל», «מספר טלפון», «הודעה (נדרשת)», «שליחה») are quoted from the rendered mirror; their source (Kalles `blocks/contact-form.liquid` + the theme's Hebrew locale) is not in `theme-src`, and neither is any post-submit success/error string.
4. Contact page body (`page.content`): not rendered by `page.contact-us.json`, so the mirror cannot say whether the Shopify body is empty or holds hidden copy.
5. The mirrors (14:31) print `color-scheme="scheme-env2-night"` on shipping's `main-heading` / `main-page` and on contact's `main-heading`, where the audit (07:51 the same day) names `S-night77` / `scheme-1`; a styling difference, no effect on the copy.
6. The four collection names differ between the guide («הארה ממוקדת», «כניסה וקיר», «מרפסת ואירוח») and About («ספוטים ותאורה ניידת», «תאורת קיר», «אווירה ודקורציה») for the same four collection handles; both sets are copied as they are — the audit already flags this.
