# Concept «dusk» — every Hebrew sentence (new copy, for the owner's approval)

Rules kept: short, plain, claim-free; no «+», no «;»; labels without a terminal period, sentences with one; digits and
Latin inside Hebrew in `<bdi dir="ltr">`; nothing the page already says (kicker «מתאים כדי…», the not-for line, the
terms, the specs, the price, the button).

## Section 1 — `ens_pdp_dusk` («כשמחשיך»)

Gate: renders the pair + lines only when the product is solar (the `elmsnest-s-place` test: metafield
`custom.power_source == 'סולארי'`, else title + description contain «סולארי»). Not solar → the one-row state.

| # | text | kind | gate | source of the fact |
|---|---|---|---|---|
| 1 | כשמחשיך | h2 (label, no period) | solar | — |
| 2 | בין ערביים | corner tag on the first tile | solar, photo pair | — |
| 3 | לילה | corner tag on the second tile | solar, photo pair | — |
| 4 | יום | the word in the first tile of the TYPE pair | solar, no mapped frame | — |
| 5 | לילה | the word in the second tile of the TYPE pair | solar, no mapped frame | — |
| 6 | הפאנל אוסף אור שמש כל היום. | line 1 | solar | a general fact about the category (BRIEF §3: not a product claim) |
| 7 | כשמחשיך, המנורה נדלקת מעצמה. | line 2 | solar | category fact; on A the title itself says «תאורה אוטומטית» |
| 8 | בחורף הימים קצרים יותר, ויש פחות טעינה. | line 3 | solar | a fact about the sun (the home says it in other words — NOTES «twice») |
| 9 | בלי כבל, בלי חשמלאי. | the sales line, once, glow serif | solar | category fact — no mains connection on a solar light |
| 10 | כשמחשיך | the row label in the collapsed state (13 px, muted) | NOT solar | — |
| 11 | המנורה הזו אינה סולארית. | the one row of the collapsed state | NOT solar | the same gate the page already uses to hide the not-for line; the listing's connection (220V / USB / סוללות), when a bullet states one, is printed by `ens_pdp_facts` and is therefore NOT repeated here |

## Section 2 — `ens_pdp_scene` (the scene band)

One sentence per family, about the *light* in that place at night — never a spec, never the kicker's «מתאים כדי…».
The family comes from `elmsnest-s-place` (`emit: 'collection'`); each is a section setting.

| family | text | gate |
|---|---|---|
| שביל (path) | אחרי השקיעה, השביל עדיין שם. | collection = תאורת-שביל-סולארית |
| קיר (wall) | אור אחד על הקיר, והכניסה כבר לא חשוכה. | collection = solar-wall-lights (solar or mains — the sentence says nothing about power) |
| גינה (spot) | אלומה אחת על מה שרוצים לראות בלילה. | collection = ספוטים-ופרוז-קטורים-סולאריים |
| מרפסת (decor) | כמה נורות קטנות, והערב נמשך עוד קצת. | collection = גרילנדות-ותאורה-דקורטיבית (not rendered in the three archetypes) |

The honesty line (only when the frame shows ANOTHER store product — BRIEF §3 (3)), 13 px muted, linked to that product:

| text | where |
|---|---|
| בתמונה: <a>מנורת גינה דו־ראשית מתכווננת <bdi dir="ltr">180°</bdi> – <bdi dir="ltr">10W IP65</bdi></a> | C (the spot collection's default scene = `dual-head-garden-light-10w-ip65` frame 3). The title is quoted verbatim, as the rule requires; in the Liquid it is `{{ credit_product.title }}` linked to `{{ credit_product.url }}`. |

## Words deliberately not used

hours, lumens, IP codes, «חזק», «אוטומטי» (the title's word), «לבד» (the home hero's word), «ביום נטען.» / «בלילה נדלק.»
(the home diptych), «בלי חיבור לחשמל, בלי חשמלאי.» (the home line), «בחורף השמש קצרה יותר, והפאנל נטען פחות.» (the home
winter line), «לא מתאים», «מתאים כדי», any price, any button label.
