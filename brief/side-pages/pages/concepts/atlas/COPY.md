# COPY — concept «atlas» (content pages, 2026-09-07)

Every sentence on the four rendered pages is the verbatim copy of `../../COPY-SOURCE.md` unless it is listed below. The rule applied: change only what BRIEF §2 allows (the four collection names → the Shopify titles everywhere; the why-solar does-not-suit list → the four licensed pairs of `elmsnest-s-place`), add only captions and credits (a photograph must be captioned as a place or a mechanism), and remove only navigation chrome that the S template already provides once (foot nav, TOC) or that the concept's «one device per idea» rule makes twice (numerals inside a checklist, a second button). Numbers: every figure prints byte-identical to COPY-SOURCE «Facts that must stay byte-identical» (29.90 / 1–3 / 7–14 / 8–17 / 14 / 5% / 100 ₪ / 17 / חינם), each in its `<bdi dir="ltr">`.

## Kept verbatim (referenced by section)

- **Guide** — h1, role line; §01 heading + intro + the four sub-lines + «N מוצרים ←» meta (counts 8 / 6 / 6 / 7 as rendered 2026-09-02; live `products_count` in Liquid); §02 heading + א/ב/ג titles and bodies (the `<bdi dir="ltr">` on the letters kept as in the source); §03 heading + intro + the three titles and bodies (incl. the source's «בצל כבוד רוב היום», kept as flagged); §04 heading + the five check titles + the note with its contact link; the filled button label «לכל גופי התאורה».
- **About** — h1 «רק תאורת חוץ. וזה בכוונה.» (the audit's strongest line; its two terminal periods are the source's), role line; «למה הקמנו את ElmsNest» + intro (ElmsNest unwrapped, as the source); «העקרונות שמכוונים אותנו» 01–03 titles + bodies; «מה זה אומר בפועל» three titles + bodies; «מה תמצאו בחנות» heading; the filled button label «לכל גופי התאורה» and the second label «איך בוחרים תאורה לגינה?».
- **Why solar** — h1, role; «איך זה עובד בפועל» 1–3 titles + bodies; «מתי זה מתאים — ומתי עדיף פתרון אחר» h2 + both h3 + the four «יכול להתאים כאשר» items; «שלוש בדיקות לפני שבוחרים» + the three questions; the note; both button labels.
- **FAQ** — h1, role with its «כתבו לנו» link; the three group headings; the ten questions and answers word for word, links included (the «ב» prefix attached to «מדיניות המשלוחים» / «מדיניות הביטולים וההחזרים» as in the source); both button labels.
- **Processing, shipping, contact** (not rendered in this concept; the section renders them with the same skin): all copy verbatim, nothing changed.

## Changed sentences (the two edits BRIEF §2 allows)

| page · place | was | now | why |
|---|---|---|---|
| guide §01 tile 1 title | שביל, עמוד וגינה | תאורת שביל, עמוד וגינה | the Shopify collection title (SPEC §1 answer 4: label = the Shopify title, one order everywhere); Liquid prints `collections['תאורת-שביל-סולארית'].title` |
| guide §01 tile 2 title | כניסה וקיר | תאורת קיר | idem, `collections['solar-wall-lights'].title` |
| guide §01 tile 3 title | הארה ממוקדת | ספוטים, פרוז׳קטורים ותאורה ניידת | idem, `collections['ספוטים-ופרוז-קטורים-סולאריים'].title` |
| guide §01 tile 4 title | מרפסת ואירוח | גרילנדות ותאורה דקורטיבית | idem, `collections['גרילנדות-ותאורה-דקורטיבית'].title` |
| about «מה תמצאו בחנות» rows 1–4 | שביל, עמוד וגינה · תאורת קיר · ספוטים ותאורה ניידת · אווירה ודקורציה | תאורת שביל, עמוד וגינה · תאורת קיר · ספוטים, פרוז׳קטורים ותאורה ניידת · גרילנדות ותאורה דקורטיבית | the same four titles (the audit's flag «two name sets for one handle» closes) |
| why-solar «עדיף פתרון אחר כאשר» item 1 | המקום כמעט ואינו מקבל אור יום — סולארי לא יספיק שם | **שביל** לא מתאים כשהמקום כמעט אינו מקבל אור יום. | the licensed pair, `render 'elmsnest-s-place', collection: collections['תאורת-שביל-סולארית'], emit: 'no'` (word from `emit: 'word'`) |
| why-solar item 2 | נדרש אור חזק וקבוע לאורך כל הלילה — תאורה סולארית לא תמיד מחליפה תאורה חשמלית חזקה | **קיר** לא מתאים כשנדרש אור חזק וקבוע לאורך כל הלילה. | idem, `solar-wall-lights` |
| why-solar item 3 | יש דרישות התקנה מיוחדות — אז חיבור קבוע עם בעל מקצוע, או מוצר נטען ב־USB | **גינה** לא מתאים כשנדרשת התקנה מיוחדת או חיבור קבוע. | idem, `ספוטים-ופרוז-קטורים-סולאריים` |
| why-solar item 4 (new row) | — | **מרפסת** לא מתאים אם צריך אור חזק — זו אינה מטרתה. | the fourth licensed pair; the list now has four rows, one per place, in the menu order |

## New sentences (captions and credits only — nothing else was written)

Captions name the photograph as a place or a mechanism, never as a product (BRIEF §3). They are `text` settings of the section (empty = no caption).

| page | caption (13 px, ink-2) | credit (11.5 px, muted, drawn only where the licence needs one) |
|---|---|---|
| guide tile 1 | שביל | צילום: Corey Leopold (CC BY 2.0) |
| guide tile 2 | קיר | none (CC0) |
| guide tile 3 | גינה | צילום: Josh Evnin (CC BY-SA 2.0) |
| guide tile 4 | מרפסת | צילום: Jeremy Levine Design (CC BY 2.0) |
| about, top | ספסל בגינה, לפנות ערב | צילום: Basile Morin (CC BY-SA 4.0) |
| about, before «מה תמצאו בחנות» | חורשה בירושלים, בצהריים | צילום: זאב שטיין (CC BY 2.5) |
| why solar, top | פאנל סולארי באור יום | צילום: Bastique (CC BY 4.0) |
| FAQ, top | חצר בשעת בין ערביים | צילום: Dago Gonzalez (CC BY 4.0) |

The four tile captions are the four place words in the licensed forms of `elmsnest-s-place` (`emit: 'word'`): שביל · קיר · גינה · מרפסת — the only place they appear in the guide body besides the collection titles themselves. The credit lines are copied verbatim from `../../../pdp3/images/SHORTLIST.md` «Credit lines».

## Removed (navigation and labels, not copy)

- The five-page **foot nav** («לדף הבית · לכל גופי התאורה · מדריך הבחירה · יצירת קשר») — the footer group prints the same four links on every page; a second copy above the footer is the same thing twice.
- The guide **TOC** (לפי מקום · לפי מטרה · מקור חשמל · לפני ההזמנה) and the FAQ **TOC** (מוצרים והתאמה · הזמנות ומשלוח · ביטול והחזרות): the pages are 3–4 screens with numbered h2s; the atlas row is the guide's wayfinding. The section ids (`#guide-place` … `#faq-policies`) stay so external links keep working.
- The guide's second button «שאלה לפני הזמנה» — the note directly above it already links «שלחו לנו את שם המוצר ואת השאלה» to the contact page; one gold pill per page (BRIEF §3). On About, why-solar and FAQ the second button becomes a text link with the same label (no copy change).
- Row numerals that are labels, not facts (COPY-SOURCE «Section numerals (labels, not facts)»): guide §03 «1/2/3» (the two-column carries the titles), guide §04 «01–05» and why-solar «1–3» (the checklist carries a square), About «מה זה אומר בפועל» «1/2/3» (the trio carries run-in titles). The h2 numerals «01–04» of the guide stay (the role line promises «ארבע החלטות»), and so do א/ב/ג and 01–03 on the two spines.
- The About media band's Pexels kerosene lantern (`images['pexels-taryn-elliott-4112233.jpg']`, alt '') — replaced by the licensed bench photograph with a caption.

## Checks run on the file

- no «+», no «;», no «וואטסאפ» in storefront text; headings carry no terminal period (the About h1 is the source's sentence and keeps its periods, like the hero's);
- every digit / Latin token in `<bdi dir="ltr">` (01–04, א/ב/ג, 01–03, 1–3, USB, 29.90, 8–17, 1–3, 7–14, 14, 5%, 100, the product counts, the credit names) — the unwrapped «ElmsNest» stays unwrapped as in the source;
- links use the ל־ / infinitive form the source already has; the arrows are `<span aria-hidden="true">←</span>`.
