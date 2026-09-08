# COPY — concept «band» (content pages, 2026-09-07)

Everything not listed here is the verbatim copy of `../../COPY-SOURCE.md`, printed in the same order, with every `<bdi dir="ltr">` wrapper of the source kept (and «ElmsNest» — unwrapped in the source — now wrapped too). The numbers are byte-identical to the source's «Facts that must stay byte-identical» table (29.90 · 1–3 · 7–14 · 8–17 · 14 · 5% · 100 · 17; «חינם»). No «+», no «;», no terminal period on a label; the two h1 sentences that carry periods in the source («רק תאורת חוץ. וזה בכוונה.») are the source's own h1, kept as the hero sentence is kept by SIMPLIFY §6.1.

## Guide — `/pages/guide-garden-lighting` (rendered in full)

Kept, by section: h1 · role line · 01 intro · the four sub-lines and counts of the collection rows (`products_count`, 8 / 6 / 6 / 7 as on 2026-09-02) · 02 the three purposes (א/ב/ג) · 03 intro and the three power rows (the typo «בצל כבוד» kept as the source has it) · 04 the five checks · the note («פרט חשוב חסר…», the contact link inside it) · the filled button label «לכל גופי התאורה».

Changed:

| # | Where | Was | Now | Why |
|---|---|---|---|---|
| 1 | 01, row 1 title | שביל, עמוד וגינה | **תאורת שביל, עמוד וגינה** | BRIEF §2: the four collection names are the four Shopify titles used everywhere else (SPEC §1 answer 4) |
| 2 | 01, row 2 title | כניסה וקיר | **תאורת קיר** | same |
| 3 | 01, row 3 title | הארה ממוקדת | **ספוטים, פרוז׳קטורים ותאורה ניידת** | same (the string as `footer-group.json` prints it, geresh U+05F3) |
| 4 | 01, row 4 title | מרפסת ואירוח | **גרילנדות ותאורה דקורטיבית** | same |
| 5 | h2 01–04 | «`01` · איפה צריך אור?» (numeral inside the h2 text) | the numeral is a gold serif label above the h2; the h2 text is the question alone | one device for the numeral (the «·» separator goes) |

New sentences (captions — a photograph is captioned as a place or a mechanism):

- «שמיים אחרי השקיעה, מעל גינה» (top band)
- «שביל בגינה פרטית, בלילה. כל גוף תאורה מאיר כמה מטרים» (break before the collection links)
- «תאים סולאריים באור יום מלא» (break before the power rows)
- credit lines: «צילום: aenigmatēs (CC BY 2.0)», «צילום: Asaph441 (CC BY-SA 4.0)», «צילום: Bastique (CC BY 4.0)»

Removed (nothing twice): the TOC (four links «לפי מקום / לפי מטרה / מקור חשמל / לפני ההזמנה» — the four numbered headings and the photographs carry the structure); the outlined button «שאלה לפני הזמנה» (the note above it is the page's one contact line); the foot nav (four links — the footer follows).

## About — `/pages/מי-אנחנו` (rendered in full)

Kept: h1 · role line · «למה הקמנו את ElmsNest» and its paragraph · the three principles (01–03) · «מה זה אומר בפועל» and its three rows (1–3, the numerals dropped as labels: the two-column list carries no numeral) · «מה תמצאו בחנות» · the filled button label «לכל גופי התאורה».

Changed:

| # | Where | Was | Now | Why |
|---|---|---|---|---|
| 1 | store row 1 | שביל, עמוד וגינה | **תאורת שביל, עמוד וגינה** | the four Shopify titles |
| 2 | store row 3 | ספוטים ותאורה ניידת | **ספוטים, פרוז׳קטורים ותאורה ניידת** | same |
| 3 | store row 4 | אווירה ודקורציה | **גרילנדות ותאורה דקורטיבית** | same («תאורת קיר» already was the title) |
| 4 | second button | outlined «איך בוחרים תאורה לגינה?» | text link **«למדריך לבחירת תאורה ←»** | P4: one gold pill per page, text links in the ל־ form; the label is the store's own (`elmsnest-s-guide-strip`, `elmsnest-s-pdp-scene`) |
| 5 | band image | the Pexels kerosene lantern, no caption | a licensed place photograph with a caption and credit | BRIEF §3 |

New sentences: «מדרגות גן בחיפה, בצהריים» (band) · «חורשה בירושלים, בצל של צהריים» (break) · credits «צילום: Josh Evnin (CC BY-SA 2.0)», «צילום: זאב שטיין (CC BY 2.5)».

Removed: the foot nav.

## Why solar — `/pages/why-solar-lighting` (top rendered; the whole page is in index.html)

Kept: h1 · role · «איך זה עובד בפועל» (1–3) · «מתי זה מתאים — ומתי עדיף פתרון אחר» · the h3 «יכול להתאים כאשר» and its four items · «שלוש בדיקות לפני שבוחרים» (1–3) · the note, word for word · the button label «לכל גופי התאורה».

Changed:

| # | Where | Was | Now | Why |
|---|---|---|---|---|
| 1 | second h3 | עדיף פתרון אחר כאשר | **מתי לא, לפי המקום** | the list under it is now the four place pairs, so the heading names them |
| 2 | its list | three general negatives («המקום כמעט ואינו מקבל אור יום — סולארי לא יספיק שם», «נדרש אור חזק וקבוע לאורך כל הלילה — תאורה סולארית לא תמיד מחליפה…», «יש דרישות התקנה מיוחדות — אז חיבור קבוע…») | the four licensed pairs exactly as `snippets/elmsnest-s-place.liquid` prints them (emit `word` + emit `no`): **שביל** לא מתאים כשהמקום כמעט אינו מקבל אור יום. · **קיר** לא מתאים כשנדרש אור חזק וקבוע לאורך כל הלילה. · **גינה** לא מתאים כשנדרשת התקנה מיוחדת או חיבור קבוע. · **מרפסת** לא מתאים אם צריך אור חזק — זו אינה מטרתה. | BRIEF §2 (the audit's flag) |
| 3 | note | «…שאלו אותנו לפני ההזמנה.» plain | the same words, «שאלו אותנו לפני ההזמנה» now the link to `/pages/contact-us` | the page's one contact line needs the link |
| 4 | buttons | filled «איך בוחרים תאורה לגינה?» + outlined «לכל גופי התאורה» | pill **«לכל גופי התאורה»** + text link **«למדריך לבחירת תאורה ←»** | P4 |

New sentences: «זריחה בין עצים, מעל בריכה» (band) · «פאנל סולארי מוטה אל השמש, על עמוד תאורה עירוני» (break) · credits «צילום: Dietmar Rabich (CC BY-SA 4.0)», «צילום: Isaacvp (CC BY-SA 4.0)».

Removed: the foot nav.

## FAQ — `/pages/help-faq` (top rendered; the whole page is in index.html)

Kept: h1 · role line with its «כתבו לנו» link · the three group links (as an inline row) · the ten questions and answers verbatim, links included · the first `<details>` open.

Changed:

| # | Where | Was | Now | Why |
|---|---|---|---|---|
| 1 | end buttons | filled «ליצירת קשר» + outlined «למדיניות המלאה» | text link **«למדיניות המלאה ←»** only | the role line already carries the page's contact link — a contact pill would be the second |

New sentences: «שביל בגן ציבורי, בשעת בין ערביים» (band) · credit «צילום: PumpkinSky (CC BY-SA 3.0)».

Removed: the foot nav.

## Processing time · Shipping · Contact (not rendered — NOTES.md §2 says how the section prints them)

Copy verbatim from COPY-SOURCE §5–§7. The only planned edits of the same kind as above: the second button of each becomes a text link in the ל־ form (processing: pill «ליצירת קשר», link «למדיניות המשלוחים המלאה ←»; shipping: pill «ליצירת קשר», link «מה קורה אחרי שהזמנתם ←»); the contact page prints the two rich-text blocks of `page.contact-us.json` verbatim above the stock form, plus one photo/email line (`snippets/elmsnest-s-contact`) — the page's only promise.
