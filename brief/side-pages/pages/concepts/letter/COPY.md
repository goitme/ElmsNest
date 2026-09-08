# COPY — concept «letter» (content pages, 2026-09-07)

Source of every kept sentence: `../../COPY-SOURCE.md`. Nothing below was paraphrased; where a sentence changed it is quoted in full with the reason. «Kept» means byte-identical (including the `<bdi dir="ltr">` wrappers, which the concept prints exactly where the source has them, plus the two places the source left Latin unwrapped — «ElmsNest» on About and in the first FAQ answer — now wrapped, P6). Rendered in `index.html`: guide, about, why-solar, FAQ (all four in full). Processing, shipping and contact are not rendered; their copy plan is in `NOTES.md` §2 and they change nothing except what §5 below says.

## 1. Guide — `/pages/guide-garden-lighting`

| unit | status |
|---|---|
| h1 «בוחרים תאורת גינה לפי המקום — לא לפי התמונה» | kept |
| role line «ארבע החלטות קצרות: …» | kept, as the lead under the h1 |
| TOC (4 anchor links) | **removed** — the four numbered h2s are the spine; printing the spine a second time as a link row is the page's one idea twice. The page is 4.4 screens, the h2s are reachable by scrolling; the ids `#guide-place` … `#guide-check` stay for deep links |
| 01 intro «בחרו את האזור הקרוב ביותר …» | kept |
| 01 collection rows — sub-lines, counts, arrows, hrefs | kept; the counts are `products_count` (8 / 6 / 6 / 7 as measured 2026-09-02), hidden when 0 |
| 01 row titles | **changed** to the four Shopify collection titles in menu order (SIMPLIFY §1 answer 4, BRIEF §2 «the four collection names must be the four titles used everywhere else»); in Liquid they are `collection.title`, nothing typed: |
| | «שביל, עמוד וגינה» → **«תאורת שביל, עמוד וגינה»** |
| | «כניסה וקיר» → **«תאורת קיר»** |
| | «הארה ממוקדת» → **«ספוטים, פרוז׳קטורים ותאורה ניידת»** |
| | «מרפסת ואירוח» → **«גרילנדות ותאורה דקורטיבית»** |
| 02 letters א / ב / ג, titles and bodies | kept (letters still inside `<bdi dir="ltr">`, as the source) |
| 03 intro «הנתונים משתנים בין מוצרים. …» | kept |
| 03 three sources, titles and bodies (incl. «בצל כבוד רוב היום», verbatim) | kept; the numerals 1 / 2 / 3 are **not printed** — the three-column device carries no order mark (labels, not facts) |
| 04 five checks | kept; the numerals 01–05 are **not printed** — the checklist square replaces them |
| note «פרט חשוב חסר בעמוד המוצר? אל תנחשו. שלחו לנו את שם המוצר ואת השאלה — נבדוק לפני שתזמינו.» | kept; the link → `/pages/contact-us`. This is the page's one contact promise |
| CTA filled «לכל גופי התאורה» → `/collections/all` | kept as the page's one gold pill |
| CTA outlined «שאלה לפני הזמנה» → contact | **removed** — the note directly above already links to the contact page; a second link to the same place is the promise twice |
| foot nav (4 links) | **removed** on every page — the header menu and the footer carry the same four links (the footer is ours and unchanged) |

Photograph captions (new sentences, mine):

- «גינה בשעת בין ערביים, רגע לפני שהאור נדלק»
- «פאנל סולארי בצהריים. ככה נראה מקום שמקבל שמש»
- «שביל בגינה פרטית, בלילה — לא מוצר מהחנות. כל נקודת אור מכסה כמה מטרים בלבד»

Credit lines (drawn, from `../../../pdp3/images/SHORTLIST.md`): «צילום: PumpkinSky (CC BY-SA 3.0)», «צילום: Bastique (CC BY 4.0)», «צילום: Asaph441 (CC BY-SA 4.0)».

## 2. About — `/pages/מי-אנחנו`

| unit | status |
|---|---|
| h1 «רק תאורת חוץ. וזה בכוונה.» | kept, periods included (the audit's «strongest line»; P4's no-period rule is for labels) |
| role line «אנחנו עוזרים להתאים גוף תאורה למקום שלכם — וגם אומרים כשמשהו לא מתאים.» | kept, the letter's opening line |
| h2 «למה הקמנו את ElmsNest» + the intro paragraph | kept («ElmsNest» now in `<bdi dir="ltr">`) |
| h2 «העקרונות שמכוונים אותנו», 01–03 titles and lines | kept |
| h2 «מה זה אומר בפועל», rows 1–3 | kept word for word, **re-set as three prose paragraphs**: each row's title becomes the run-in lead of its paragraph, with a period after it («אין אצלנו קטגוריה אחרת.» / «המפרט לפני הקנייה.» / «וכשמשהו לא מתאים — אומרים.»); the numerals 1–3 are not printed |
| h2 «מה תמצאו בחנות» + four links | kept as links; the four titles **changed** to the Shopify titles (same rule as the guide): «תאורת קיר» (unchanged), «ספוטים ותאורה ניידת» → **«ספוטים, פרוז׳קטורים ותאורה ניידת»**, «אווירה ודקורציה» → **«גרילנדות ותאורה דקורטיבית»**, «שביל, עמוד וגינה» → **«תאורת שביל, עמוד וגינה»**; the «←» glyphs are dropped (an inline link run, not rows) |
| sign-off | **new**: «כתבו לנו.» then «ElmsNest, ישראל» and «info@elmsnest.com» (mailto) — the two lines are the contact page's own «**ElmsNest**, ישראל» / «דוא״ל: info@elmsnest.com», re-used as a signature; the email is the page's one contact promise |
| CTA filled «לכל גופי התאורה» | kept, the gold pill |
| CTA outlined «איך בוחרים תאורה לגינה?» → guide | **changed** to the house link form «למדריך לבחירת תאורה ←» (P4: text links in the ל־ infinitive; label = `elmsnest-s-guide-strip` default), a text link beside the pill |
| foot nav | removed (see guide) |

Caption (new): «חורשה בירושלים, בצל של צהריים». Credit: «צילום: זאב שטיין (CC BY 2.5)».

## 3. Why solar — `/pages/why-solar-lighting`

| unit | status |
|---|---|
| h1 «למה תאורה סולארית — ומתי לא», role line | kept |
| h2 «איך זה עובד בפועל», beats 1–3 | kept (numerals printed, gold serif) |
| h2 «מתי זה מתאים — ומתי עדיף פתרון אחר» | kept |
| h3 «יכול להתאים כאשר» + 4 bullets · h3 «עדיף פתרון אחר כאשר» + 3 bullets | **replaced** by the four licensed place pairs of `snippets/elmsnest-s-place.liquid` (BRIEF §2: «the does-not-suit list must use the four licensed pairs, not three general negatives»). Both panels go: printing the general list next to the pairs would say «suits» twice. In Liquid the rows are `render 'elmsnest-s-place', collection: c, emit: 'word' / 'yes' / 'no'` over the four collections in menu order; the concept prints their exact output: |
| | שביל · «מתאים כדי לראות את הדרך» · «לא מתאים כשהמקום כמעט אינו מקבל אור יום.» |
| | קיר · «מתאים כדי להאיר נקודה מסוימת» · «לא מתאים כשנדרש אור חזק וקבוע לאורך כל הלילה.» |
| | גינה · «מתאים כדי להאיר עץ או ערוגה» · «לא מתאים כשנדרשת התקנה מיוחדת או חיבור קבוע.» |
| | מרפסת · «מתאים כדי ליצור אווירה» · «לא מתאים אם צריך אור חזק — זו אינה מטרתה.» |
| h2 «שלוש בדיקות לפני שבוחרים», 3 questions | kept (numerals not printed — checklist squares) |
| note «חלק מהמוצרים בחנות מיועדים בעיקר לאווירה ולא לאור חזק. אם הנתון שחשוב לכם לא מופיע בעמוד המוצר — שאלו אותנו לפני ההזמנה.» | kept; «שאלו אותנו» is now the link → `/pages/contact-us` (the page's one contact promise) |
| CTA filled «איך בוחרים תאורה לגינה?» → guide | **changed** to the pill «למדריך לבחירת תאורה» (ל־ form, the guide stays the primary action) |
| CTA outlined «לכל גופי התאורה» → all | **changed** to the text link «לכל גופי התאורה ←» |
| foot nav | removed |

Captions (new): «זריחה בין עצים», «תא סולארי מקרוב, באור יום». Credits: «צילום: Dietmar Rabich (CC BY-SA 4.0)», «צילום: Guilhem Vellut (CC BY 2.0)».

## 4. FAQ — `/pages/help-faq`

| unit | status |
|---|---|
| h1 «שאלות נפוצות» | kept |
| role line «תשובות קצרות לפני ואחרי ההזמנה. לא מצאתם תשובה? כתבו לנו.» | **split**: «תשובות קצרות לפני ואחרי ההזמנה.» stays the lead; «לא מצאתם תשובה? כתבו לנו.» moves to the foot, above the pill, so the contact promise is printed once |
| TOC (3 links) | removed (see guide) |
| three h2s, ten questions and answers, links, `<details>` with only the first open | kept byte for byte — all numbers (29.90 ₪ · 8–17 · 1–3 · 7–14 · 14 · 5% · 100 ₪) in their source `<bdi>` form |
| CTA filled «ליצירת קשר», outlined «למדיניות המלאה» | kept: the pill «ליצירת קשר» and the text link «למדיניות המלאה ←» |
| foot nav | removed |

Caption (new): «מרפסת בשעת בין ערביים». Credit: «צילום: Jeremy Levine Design (CC BY 2.0)».

## 5. Not rendered — processing, shipping, contact

All copy kept verbatim (plan in `NOTES.md` §2). The only changes: the foot nav goes (processing); the CTA pair becomes pill + text link with the source labels (processing: «ליצירת קשר» / «למדיניות המשלוחים המלאה ←»; shipping: «ליצירת קשר» / «מה קורה אחרי שהזמנתם ←»); on contact the column-2 rich text («שאלה לפני הזמנה? …», the three bullets, «ואם משהו לא מתאים למקום — נגיד את זה מראש.», «פנייה על הזמנה קיימת? …», the email line) prints once from the section, above the untouched stock form. New caption sentences there: processing «שביל במדבר, לפני שקיעה»; contact «חצר בירושלים, בצל».

## 6. Every new or changed Hebrew sentence, in one list

1. «תאורת שביל, עמוד וגינה» (row title, guide and About — the Shopify title)
2. «תאורת קיר» (row title, guide — the Shopify title)
3. «ספוטים, פרוז׳קטורים ותאורה ניידת» (row title, guide and About)
4. «גרילנדות ותאורה דקורטיבית» (row title, guide and About)
5. «גינה בשעת בין ערביים, רגע לפני שהאור נדלק»
6. «פאנל סולארי בצהריים. ככה נראה מקום שמקבל שמש»
7. «שביל בגינה פרטית, בלילה — לא מוצר מהחנות. כל נקודת אור מכסה כמה מטרים בלבד»
8. «חורשה בירושלים, בצל של צהריים»
9. «כתבו לנו.» (About sign-off)
10. «למדריך לבחירת תאורה ←» / «למדריך לבחירת תאורה» (About link, why-solar pill — the house label)
11. «לכל גופי התאורה ←» (why-solar link — the source label in link form)
12. «זריחה בין עצים»
13. «תא סולארי מקרוב, באור יום»
14. «מתאים כדי לראות את הדרך» · «מתאים כדי להאיר נקודה מסוימת» · «מתאים כדי להאיר עץ או ערוגה» · «מתאים כדי ליצור אווירה» (why-solar pairs — `elmsnest-s-place` output after «מתאים כדי»)
15. «מרפסת בשעת בין ערביים»
16. «למדיניות המלאה ←» (FAQ link — the source label in link form)
17. «שביל במדבר, לפני שקיעה» · «חצר בירושלים, בצל» (processing / contact captions, not rendered)

Removed sentences: the seven general bullets of why-solar's two panels; the guide's «שאלה לפני הזמנה» button label; the About button label «איך בוחרים תאורה לגינה?». Everything else in the seven pages is untouched.
