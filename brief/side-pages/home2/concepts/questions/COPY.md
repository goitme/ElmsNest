# Concept «questions» — every Hebrew sentence (new copy, for the owner's approval)

Rules kept: short, plain, claim-free, no «+», no «;», labels without a terminal period, sentences keep theirs.
Numbers sit inside `<bdi dir="ltr">`. No product claim (no hours, no lumens, no IP for «all products»).

## [A] «שלוש שאלות לפני שקונים» — after the product cards, before «מתי כן, ומתי לא»

| # | where | text | note / source of fact |
|---|---|---|---|
| 1 | h2 | שלוש שאלות לפני שקונים | heading, no period |
| 2 | lead | השאלות שהמדריך שואל ראשון. | points at the existing guide page |
| 3 | card 1 · question (h3) | כמה שמש מגיעה לנקודה? | the guide's first question (BRIEF §3 seed 2); same question the PDP fit block asks («כמה שמש המקום מקבל ביום?») |
| 4 | card 1 · line | הפאנל נטען מהשמש ביום. פינה מוצלת רוב היום תיתן פחות אור בלילה. | general fact about solar charging (BRIEF §2: «a general fact about the sun is not a product claim») |
| 5 | card 2 · question (h3) | עד כמה רחוק האור צריך להגיע? | the guide's second question |
| 6 | card 2 · line | מנורה אחת מאירה את סביבתה הקרובה. שביל ארוך צריך כמה מנורות. | general fact about any point light, no distance number |
| 7 | card 3 · question (h3) | בפנים או בחוץ? | the guide's third question |
| 8 | card 3 · line | בחוץ יש גשם, אבק ושמש. לא כל מנורה בנויה לזה. | general fact about outdoors; «not every lamp» is not a claim about ours |
| 9 | link | למדריך לבחירת תאורה ← | the licensed form (SPEC P4), moved here from the fit block — one guide link per page |

Numerals on the cards: `1` `2` `3` (in `<bdi dir="ltr">`).

Alt texts (labels, no period):
- מנורות גינה סולאריות בשמש, הפאנל על כל ראש
- שלוש מנורות שביל לאורך מדרגות אבן בלילה
- מנורת קיר על עמוד בין חלון מואר לגינה בדמדומים

## [B] «ובחורף?» — after «מתי כן, ומתי לא», before the terms strip

| # | where | text | note / source of fact |
|---|---|---|---|
| 10 | h2 | ובחורף? | BRIEF §3 seed 3, heading as given |
| 11 | line 1 | בחורף השמש קצרה יותר, והפאנל נטען פחות. | fact about the season (BRIEF §2 example «בחורף השמש קצרה יותר») |
| 12 | line 2 | פחות טעינה ביום, פחות שעות אור בלילה. | consequence of line 1, no number |
| 13 | line 3 (muted) | זה נכון לכל תאורה סולארית, גם שלנו. | the honest note; says it applies to us too, promises nothing |

Alt text: עמודי תאורה על דשא בדמדומים כחולים של חורף

## Band labels (mockup only, not storefront copy)
The grey bands repeat the existing headings («כשהשמש יורדת, הגינה נדלקת.», «איפה צריך אור?», «מה שנדלק ראשון», «מתי כן, ומתי לא», «שלושה מספרים שכדאי לדעת») plus «קיים», the section kind and its height. They are not new copy.

## What changes in existing copy
Nothing is rewritten. `ens_fit.settings.guide_label` becomes `""` in `templates/index.json` so the guide link appears once, in [A]. The fit block keeps its contact line.
