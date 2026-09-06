# Concept «scene» — every Hebrew sentence (new copy, for the owner's approval)

Voice: short, plain, claim-free. Nothing here repeats the kicker («מתאים כדי …»), the not-for line, the terms, the
specs or the price. Digits / Latin inside Hebrew are wrapped in `<bdi dir="ltr">`. No «+», no «;». Labels carry no
terminal period; sentences keep theirs.

## Section 1 — `ens_pdp_night` («ככה זה נראה בלילה»): ONE sentence on the photograph, per place family

The family comes from `elmsnest-s-place` (`emit: 'collection'`). The sentence is about the *light in that place at
night* — never a spec, never the kicker's infinitive. Each is a theme setting (default below), so the owner can change
any of them without code.

| family (collection) | sentence | why it is honest |
|---|---|---|
| שביל — `תאורת-שביל-סולארית` | **בלילה השביל עוד שם.** | a path light keeps the path visible after dark; says nothing about reach, hours or brightness |
| קיר — `solar-wall-lights` | **בערב הקיר עצמו מאיר.** | a wall light washes the wall it sits on; «בערב» not «כשמחשיך», because five of the six wall products are mains and do not switch on by themselves |
| גינה — `ספוטים-ופרוז-קטורים-סולאריים` | **בלילה הגינה לא נעלמת.** | a spot picks a tree or a bed out of the dark; no claim about how far or how bright |
| מרפסת — `גרילנדות-ותאורה-דקורטיבית` | **הערב נשאר במרפסת.** | decor light is about staying outside longer; different words from the home's «חושך הוא לא סוף הערב.» (not rendered by an archetype — the three archetypes are path / wall / spot) |

Rendered in the mockup: A «בלילה השביל עוד שם.» · B «בערב הקיר עצמו מאיר.» · C «בלילה הגינה לא נעלמת.»

### The honesty line (only when the photograph shows another store product — BRIEF §3 image rule 3)

**בתמונה: {כותרת המוצר שבתמונה}** — 13 px, muted (`--env2-mute`), the title linked to that product's page.
Rendered on C: «בתמונה: מנורת גינה דו־ראשית מתכווננת <bdi dir="ltr">180°</bdi> – <bdi dir="ltr">10W IP65</bdi>»
(the title of `dual-head-garden-light-10w-ip65`, verbatim from the store). Not rendered on A and B: the frame shows
the page's own product, so nothing needs saying. `alt` of the photograph is empty (decorative; the sentence carries
the meaning) — a setting, like the home band.

## Section 2 — `ens_pdp_dusk` («כשמחשיך»): solar products only

Gate: the P4 solar test copied from `elmsnest-s-place` (`custom.power_source == 'סולארי'`, else title + description
contain «סולארי»). Renders on A and C (solar); prints nothing on B (mains) and on every other mains / USB / battery
product — no «מתחבר לחשמל» substitute, because the bullets already say the connection and the facts print them.

| element | text | source / why it is not a claim |
|---|---|---|
| label (h2, no period) | **כשמחשיך** | the moment, not a promise |
| sentence 1 | **ביום הפאנל אוסף שמש. כשמחשיך, האור נדלק.** | how every solar light of the category works (BRIEF §3: «ביום נטען, בלילה נדלק» is a general fact, not a product claim). Says «הפאנל», not where it sits — the floodlight's panel is on a cable, the bollard's is on the head, so the sentence is true of both |
| sentence 2 (muted) | **יותר שמש ביום, יותר אור בלילה.** | the one thing a first-time solar buyer needs to hear before pressing the button — the dependency on the spot's sun, as a general fact, with no number, no hours, no lumens. It states the positive of the not-for line without repeating its words |

## Not written on purpose

- No «ביום נטען. בלילה נדלק.» (the home diptych's headline) — the fact is restated in different words and in a
  detail, not a landscape (BRIEF §4 seed 2).
- No winter line («בחורף השמש קצרה יותר») — the home already says it; on the PDP it would be twice (seed 5).
- No «נדלק לבד» / «אוטומטי» — the title of A already says it; C has a remote and a timer, so a blanket «לבד» is not
  safe for every solar product.
- No hours, no lumens, no IP code, no «חזק», no «best», no reviews, no urgency.
