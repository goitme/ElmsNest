# COPY — concept «field» (content pages, 2026-09-07)

Source of truth: `../../COPY-SOURCE.md`. Everything not listed under «changed / new» is kept **verbatim**, `<bdi dir="ltr">` wrappers included. Section numerals that the source treats as labels («Section numerals (labels, not facts)») are dropped where the device no longer needs them; that is layout, not copy, and is listed under «dropped» for honesty.

## Kept, by section

| page | kept verbatim (COPY-SOURCE section) |
|---|---|
| guide | h1, role line, TOC (4 anchors), §01 intro + the four sub-lines and the `products_count` meta («<bdi>8</bdi> מוצרים ←» etc.), §02 rows א/ב/ג, §03 intro + rows 1–3 (including «בצל כבוד רוב היום», kept as flagged), §04 the five check titles, the note with its contact link, the filled CTA «לכל גופי התאורה» |
| about | h1 «רק תאורת חוץ. וזה בכוונה.», role line, «למה הקמנו את ElmsNest» + intro paragraph, «העקרונות שמכוונים אותנו» rows 01–03, «מה זה אומר בפועל» rows (titles + bodies), «מה תמצאו בחנות», the filled CTA «לכל גופי התאורה», the outlined CTA text «איך בוחרים תאורה לגינה?» (now a text link) |
| why-solar | h1, role line, «איך זה עובד בפועל» rows 1–3, «מתי זה מתאים — ומתי עדיף פתרון אחר», «יכול להתאים כאשר» (4 items verbatim), «שלוש בדיקות לפני שבוחרים» (3 questions), the note, both CTA texts (filled «איך בוחרים תאורה לגינה?», outlined «לכל גופי התאורה» now a text link) |
| FAQ | h1, role line with «כתבו לנו» link, TOC (3 anchors), the three h2s, all ten Q&A verbatim with their links (`/pages/why-solar-lighting`, `/pages/guide-garden-lighting`, `/policies/shipping-policy`, `/policies/refund-policy`, `/pages/contact-us`), the outlined CTA text «למדיניות המלאה» (now a text link) |
| processing, shipping, contact | not rendered in this concept; all copy kept verbatim (see NOTES §1 for the devices) |

Every fact string of «Facts that must stay byte-identical» that appears on the rendered pages is printed unchanged: «משלוח לנקודת איסוף בישראל — חינם», «<bdi dir="ltr">29.90</bdi> ₪», «<bdi dir="ltr">8–17</bdi> ימי עסקים», «<bdi dir="ltr">1–3</bdi> ימי טיפול», «<bdi dir="ltr">7–14</bdi> ימי משלוח», «עד <bdi dir="ltr">14</bdi> ימים מקבלת המוצר», «<bdi dir="ltr">5%</bdi> ממחיר העסקה או <bdi dir="ltr">100</bdi> ₪ — הנמוך מביניהם», «בביטול שנובע מפגם, מאי־התאמה או מאי־אספקה במועד — לא נגבים דמי ביטול.», the live counts 8 / 6 / 6 / 7 (typed here; `products_count` in Liquid).

## Changed (the two edits BRIEF §2 allows)

1. **Guide §01 — the four collection titles** are now the Shopify titles, in the main-menu order, as the header, the home tiles, the collection filter row and the footer print them (the sub-lines and counts are unchanged):
   - «שביל, עמוד וגינה» → **תאורת שביל, עמוד וגינה**
   - «כניסה וקיר» → **תאורת קיר**
   - «הארה ממוקדת» → **ספוטים, פרוז׳קטורים ותאורה ניידת**
   - «מרפסת ואירוח» → **גרילנדות ותאורה דקורטיבית**
2. **About «מה תמצאו בחנות» — the same four titles** replace «שביל, עמוד וגינה» / «תאורת קיר» / «ספוטים ותאורה ניידת» / «אווירה ודקורציה» (the audit's «two name sets for one handle» flag closes).
3. **Why-solar «עדיף פתרון אחר כאשר»** — the three general negatives are replaced by the four licensed pairs of `snippets/elmsnest-s-place` (`emit:'word'` + `emit:'no'`), byte-for-byte:
   - **שביל** — לא מתאים כשהמקום כמעט אינו מקבל אור יום.
   - **קיר** — לא מתאים כשנדרש אור חזק וקבוע לאורך כל הלילה.
   - **גינה** — לא מתאים כשנדרשת התקנה מיוחדת או חיבור קבוע.
   - **מרפסת** — לא מתאים אם צריך אור חזק — זו אינה מטרתה.
   Removed sentences: «המקום כמעט ואינו מקבל אור יום — סולארי לא יספיק שם», «נדרש אור חזק וקבוע לאורך כל הלילה — תאורה סולארית לא תמיד מחליפה תאורה חשמלית חזקה», «יש דרישות התקנה מיוחדות — אז חיבור קבוע עם בעל מקצוע, או מוצר נטען ב־USB».

## New sentences (all Hebrew, all mine)

Captions — one per photograph, a kicker naming the kind («מקום» / «מנגנון») then the place or the mechanism and the hour; the credit line follows in the licence's form:

- «טרסות מגוננות בחיפה, בצהריים» (guide, top)
- «דרך חצץ בין קקטוסים, בשמש נמוכה» (guide, §01)
- «תאים סולאריים בשמש מלאה, ביום» (guide, before §03)
- «חורשה בירושלים, בצל הצהריים» (about, top)
- «חצר סרגיי בירושלים, בצל» (about, margin)
- «תא סולארי מקרוב, בשמש» (why-solar, top)
- «זריחה בין עצים, מעל בריכת מים» (why-solar, break)
- «בוגנוויליה בשמש הצהריים» (FAQ, top)
- «סמטה בטאורמינה, בצל» (FAQ, between groups)
- «מקום» and «מנגנון» (the caption kickers)
- «נחלת הכלל» (the line printed under a CC0 / public-domain photograph, where no credit is owed)
- «צילום: …» (the credit prefix, as `../pdp3/images/SHORTLIST.md` prescribes)

The contact line on the About page is the sentence of `snippets/elmsnest-s-contact` (SIMPLIFY §5.4), not new: «לא בטוחים? נבדוק התאמה לפני שתזמינו.» + «לשלוח תמונה של המקום ←» (mailto, body «שלום, מצרף/ת תמונה של המקום שרוצים להאיר.»). It appears once, on the one rendered page that has no other contact link.

The header/footer band labels («header group · 64 px», «footer group · 620 px») are mock-up labels, not storefront copy.

## Dropped (nothing twice — each is a duplicate of something the page or the shared groups already carry)

- **The foot nav** («לדף הבית · לכל גופי התאורה · מדריך הבחירה · יצירת קשר») on all five Liquid pages: the footer group prints the same four links 200 px lower, and on the guide the third link pointed at itself.
- **The second button** of each CTA pair: the guide's ghost «שאלה לפני הזמנה» (the note above it is already the page's one contact link); the FAQ's filled «ליצירת קשר» (the role line's «כתבו לנו» is the page's one contact link — «למדיניות המלאה ←» stays as a text link). On About and why-solar the second text is kept as a text link beside the one pill (P4's «one gold pill»).
- **Row numerals that were labels**: the guide's checklist 01–05 (a hollow square replaces them), About's «מה זה אומר בפועל» 1–3 (run-in titles replace them). Kept: the guide's 01–04 section numerals, א/ב/ג on the spine, 1–3 on the power table, 01–03 on the principles, 1–3 on the beats and the three checks.
- **The hidden duplicate `sr-only` h1** of `main-heading` — gone with the template swap (NOTES §2).

## Markup only (not copy)

- «ElmsNest» on About (h2 + paragraph) and in the first FAQ answer is now inside `<bdi dir="ltr">` like every other Latin token (P6); the text is unchanged.
- The guide h2s print the numeral in the margin column («01») and the question in the content column; the source's « · » separator is layout and is not printed.
