# QUIET — copy

Concept: **the fewest images that make it real.** One photograph per page, only where a photograph
carries a fact; everything else is typography. Source of truth: `../../COPY-SOURCE.md`. Everything
not listed below is that file's copy, verbatim, character for character — including the flagged typo
«בצל כבוד רוב היום» (guide §03) and every `<bdi dir="ltr">` wrapper.

## 0. Kept copy, by section (nothing changed)

| page | section in this concept | kept verbatim from COPY-SOURCE |
|---|---|---|
| guide | h1, role line, TOC (4 links) | §1 band + TOC |
| guide | `01 · איפה צריך אור?` intro + the four row sub-lines | §1 intro, the four `<span>` sub-lines |
| guide | `02 · מה האור צריך לעשות?` — three terms and bodies | §1 `ol.en-doc__sched` rows א/ב/ג (titles + bodies) |
| guide | `03 · איזה מקור חשמל מתאים?` intro + the three bodies | §1 intro + rows 1–3 bodies |
| guide | `04 · מה בודקים לפני ההזמנה?` — the five labels | §1 rows 01–05 |
| guide | the note («פרט חשוב חסר…») with its contact link | §1 note |
| guide | the gold pill «לכל גופי התאורה» → `/collections/all` | §1 CTA, filled button |
| why-solar | h1, role line | §2 band |
| why-solar | «איך זה עובד בפועל» — the three beats 1/2/3, titles and bodies | §2 `ol.en-doc__sched` |
| why-solar | «יכול להתאים כאשר» — the four bullets | §2 panel 1 |
| why-solar | «שלוש בדיקות לפני שבוחרים» — the three questions | §2 third section |
| why-solar | the note («חלק מהמוצרים בחנות…») | §2 note |
| why-solar | the gold pill «איך בוחרים תאורה לגינה?» | §2 CTA, filled button |
| about | h1 «רק תאורת חוץ. וזה בכוונה.», role line | §3 band |
| about | «למה הקמנו את ElmsNest» + its paragraph | §3 h2 + intro |
| about | «העקרונות שמכוונים אותנו» — three titles + bodies | §3 rows 01–03 |
| about | «מה זה אומר בפועל» — three titles + bodies | §3 rows 1–3 |
| about | «מה תמצאו בחנות» heading | §3 h2 |
| about | the gold pill «לכל גופי התאורה» | §3 CTA, filled button |
| faq | h1, role line with «כתבו לנו», TOC (3 links) | §4 band + TOC |
| faq | the three group headings and all **ten** questions and answers, links included | §4 |
| faq | the gold pill «ליצירת קשר» | §4 CTA, filled button |
| processing · shipping · contact | every sentence, every number, every link | §5 · §6 · §7 |

The schedule numbers print byte-identically: «חינם», «<bdi dir="ltr">29.90</bdi> ₪»,
«<bdi dir="ltr">1–3</bdi>», «<bdi dir="ltr">7–14</bdi>», «<bdi dir="ltr">8–17</bdi>»,
«<bdi dir="ltr">14</bdi> ימים», «<bdi dir="ltr">5%</bdi> … או <bdi dir="ltr">100</bdi> ₪»,
«<bdi dir="ltr">17</bdi> ימי עסקים», «יום עסקים: ראשון עד חמישי…». The only counts are
`products_count` (8 / 6 / 6 / 7).

---

## 1. Changed sentences

### 1.1 The four collection names — now the titles used everywhere else (BRIEF §2)

Both lists print `collection.title` from Liquid, so they can never drift from the menu again.

**Guide, `01 · איפה צריך אור?` (row titles only; the sub-lines are untouched):**

| was | is |
|---|---|
| שביל, עמוד וגינה | תאורת שביל, עמוד וגינה |
| כניסה וקיר | תאורת קיר |
| הארה ממוקדת | ספוטים, פרוז׳קטורים ותאורה ניידת |
| מרפסת ואירוח | גרילנדות ותאורה דקורטיבית |

**About, «מה תמצאו בחנות»:**

| was | is |
|---|---|
| שביל, עמוד וגינה | תאורת שביל, עמוד וגינה |
| תאורת קיר | תאורת קיר *(unchanged)* |
| ספוטים ותאורה ניידת | ספוטים, פרוז׳קטורים ותאורה ניידת |
| אווירה ודקורציה | גרילנדות ותאורה דקורטיבית |

### 1.2 Why-solar — «עדיף פתרון אחר כאשר» becomes the four licensed pairs

The three general negatives are replaced by the four sentences of `snippets/elmsnest-s-place.liquid`
(`emit: 'no'`), each under its place word. Printed as two columns, so no dash is added to a sentence
that already carries one.

- שביל — לא מתאים כשהמקום כמעט אינו מקבל אור יום.
- קיר — לא מתאים כשנדרש אור חזק וקבוע לאורך כל הלילה.
- גינה — לא מתאים כשנדרשת התקנה מיוחדת או חיבור קבוע.
- מרפסת — לא מתאים אם צריך אור חזק — זו אינה מטרתה.

(was: «המקום כמעט ואינו מקבל אור יום — סולארי לא יספיק שם» · «נדרש אור חזק וקבוע לאורך כל הלילה —
תאורה סולארית לא תמיד מחליפה תאורה חשמלית חזקה» · «יש דרישות התקנה מיוחדות — אז חיבור קבוע עם בעל
מקצוע, או מוצר נטען ב־<bdi dir="ltr">USB</bdi>».)

### 1.3 Guide §03 — the em dash becomes the column split

The row title «X — Y» is set as a two-column row: the power source in the narrow column, the
condition beside it. No word changes, the dash is dropped because the layout now carries it.

| was (one line) | is (term column · value) |
|---|---|
| סולארי — למקום שמקבל שמש | סולארי · למקום שמקבל שמש |
| סוללה או <bdi dir="ltr">USB</bdi> — לשליטה בטעינה | סוללה או <bdi dir="ltr">USB</bdi> · לשליטה בטעינה |
| חיבור לחשמל — להתקנה קבועה | חיבור לחשמל · להתקנה קבועה |

### 1.4 Section numerals — kept only where the order is real

COPY-SOURCE lists these as «labels, not facts». Kept: the guide's `01`–`04` on the four h2s (the four
decisions are a sequence) and why-solar's `1 · 2 · 3` on ביום / בערב / מה זה אומר (a day is a
sequence). Dropped: guide א/ב/ג (§02, three alternatives), guide `1 · 2 · 3` (§03, three
alternatives), guide `01`–`05` (§04, a checklist), about `01`–`03` and `1 · 2 · 3` (principles are
not ranked), why-solar `1 · 2 · 3` on «שלוש בדיקות» (three questions, any order).

### 1.5 One gold pill per page — the second button becomes a link that already exists

| page | pill kept | ghost button removed | who carries it now |
|---|---|---|---|
| guide | לכל גופי התאורה | שאלה לפני הזמנה | the note's link «שלחו לנו את שם המוצר ואת השאלה» |
| why-solar | איך בוחרים תאורה לגינה? | לכל גופי התאורה | the foot nav |
| about | לכל גופי התאורה | איך בוחרים תאורה לגינה? | the foot nav («מדריך הבחירה») |
| faq | ליצירת קשר | למדיניות המלאה | the answer's own link «מדיניות הביטולים וההחזרים» |
| processing · shipping | ליצירת קשר | — | «למדיניות המשלוחים המלאה» / «מה קורה אחרי שהזמנתם» stay, **as text links, labels unchanged** |

### 1.6 The foot nav drops the link the page already gives

The four shared labels are unchanged. A page never prints a link to itself, and never repeats the
link its gold pill carries — so guide prints «לדף הבית · יצירת קשר», about «לדף הבית · מדריך הבחירה ·
יצירת קשר», why-solar «לדף הבית · לכל גופי התאורה · יצירת קשר», FAQ «לדף הבית · לכל גופי התאורה ·
מדריך הבחירה». (Today all five print all four, and the guide links to itself.)

---

## 2. New sentences (all of them)

Nine lines, and four of them are credits.

**Guide — the photograph after the places**

1. caption: **חצר אחת בשעת בין ערביים — ארבעת המקומות נמצאים בה.**
2. label: **שביל** · **החצץ שמוביל אל הדלת**
3. label: **קיר** · **החזית המוארת**
4. label: **גינה** · **העץ בעציץ**
5. label: **מרפסת** · **השולחן והכיסאות**
6. credit: **צילום: Jeremy Levine Design (CC BY <bdi dir="ltr">2.0</bdi>)**

**About — the photograph beside the h1**

7. caption: **קיר, שיח וחצץ באור צהריים**
8. credit: **צילום: Carol M Highsmith (CC0 <bdi dir="ltr">1.0</bdi>)**

**Why-solar — the mechanism beside the three beats**

9. caption: **תאים סולאריים באור יום**
10. credit: **צילום: Bastique (CC BY <bdi dir="ltr">4.0</bdi>)**

**Contact (planned, not in this render)**

11. caption: **גינה ים־תיכונית באור יום — תמונה כזאת מספיקה לנו**
12. credit: **צילום: Swphotouk (CC BY <bdi dir="ltr">4.0</bdi>)**

Every label ends without a period. Every caption is a description of what is in the frame, so no
photograph can be read as a product of the store. No «+», no «;», no claim, no count.

## 3. alt text (new, not visible copy)

- guide: «חצר עם חצץ, שולחן וכיסאות, עציץ וקיר מואר, בשעת בין ערביים»
- about: «קיר לבן, שיח בוגנוויליה וחצץ באור צהריים»
- why-solar: «תאים סולאריים ופסי מוליכים מאירים בשמש חזקה»
