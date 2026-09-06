# Concept «one» — every Hebrew sentence (new copy, for the owner's approval)

One section, `sections/elmsnest-s-pdp-scene.liquid`. Every line is a schema setting; the family lines are four
settings each (one per licensed place), picked by `elmsnest-s-place … emit:'collection'`. Nothing here repeats the
kicker («מתאים כדי …»), the not-for line, the terms, the specs or the contact line.

## 1. Heading — one per family (no terminal period: a heading)

| family (place word from `elmsnest-s-place`) | heading | source |
|---|---|---|
| path — שביל | בלילה, על השביל | the licensed place word, nothing else |
| wall — קיר | בלילה, על הקיר | idem |
| spot — גינה | בלילה, בגינה | idem |
| decor — מרפסת | בלילה, במרפסת | idem |

Rendered in the mockup: A «בלילה, על השביל» · B «בלילה, על הקיר» · C «בלילה, בגינה».

## 2. The night line — one per family, about the *light* in that place (never a spec, never a product claim)

| family | sentence | why it is claim-free |
|---|---|---|
| path | אור נמוך, קרוב לאדמה. השביל מואר, הגינה נשארת בחושך. | what a bollard's light does by its form (low source, pool on the ground); no reach, no hours, no lumens |
| wall | כתם אור על הקיר. הכניסה נראית, השאר נשאר בצל. | what a wall light does (a wash on the wall); no distance, no brightness |
| spot | אלומה אחת ממוקדת. מה שמואר בולט, מה שמסביב נעלם בחושך. | the nature of a spot beam; no angle, no lumens |
| decor | הרבה נקודות אור קטנות במקום מנורה אחת. אור שיושבים בו. | the nature of a string; says nothing about strength except by contrast with «מנורה אחת» |

Rendered: A path line · B wall line · C spot line. Gate: none (every product in a mapped collection gets its family line).

## 3. The dusk line — solar products only

| sentence | gate | source of the fact |
|---|---|---|
| ביום הפאנל אוסף שמש. כשמחשיך, האור נדלק. | renders only when the product passes the solar test copied from `elmsnest-s-place` (`custom.power_source == 'סולארי'`, else title + description contain «סולארי»); on the 11 mains / USB / battery products the setting is skipped entirely | a general fact about solar lighting (BRIEF §3: «ביום נטען, בלילה נדלק» is not a product claim); no hours, no charge time |

Rendered on A and C. On B (mains) the line is absent — the section shows heading, night line, link.
No connection line on mains products either: the section does not quote bullets (the facts section prints them).

## 4. The link

| text | href | note |
|---|---|---|
| למדריך לבחירת תאורה ← | /pages/guide-garden-lighting | the arrow is a separate `aria-hidden` span; same form as the page's «לכל התנאים ←». The PDP body has no guide link today (the footer's «מדריך לבחירת תאורה לגינה» is a menu entry, not a sentence) |

## 5. The honesty line — only when the frame shows another store product

| text | when | markup |
|---|---|---|
| בתמונה: מנורת גינה דו־ראשית מתכווננת <bdi dir="ltr">180°</bdi> – <bdi dir="ltr">10W IP65</bdi> | the per-product map has no frame for this product and the collection default is used (C) | `«בתמונה: »` is a setting (`credit_prefix`), the title is `{{ credit_product.title }}` from the block's `product` setting, linked to `credit_product.url`; 12 px (13 at ≥ 901) in `--env2-mute`, the title in `--env2-ink-2` |

Rendered on C only. A and B show their own product → no line.

## 6. What is deliberately NOT said

- No «ככה זה נראה בלילה» heading: on a fallback frame that sentence would be a lie; the place heading is true on every product.
- No winter sentence (the home says it; the guide link is where the winter question goes).
- No «לא מתאים …», no second contact line, no «בלי חשמלאי» (home), no «חושך הוא לא סוף הערב» (home band).
- No «+», no «;», no digits outside `<bdi dir="ltr">`.
