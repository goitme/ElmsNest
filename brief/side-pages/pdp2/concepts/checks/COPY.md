# Concept «checks» — every Hebrew sentence (new copy, for the owner's approval)

Two sections. Nothing below is printed anywhere else on the product page. Guillemets are notation. No «+», no «;».
Labels and headings carry no terminal period; a sentence keeps its period.

## 1. `elmsnest-s-pdp-scene` — the scene band (after `main-product`)

One sentence per family, on the photograph, in glow serif. It is about the *light in that place at night*, never a
spec, and it holds whether the frame shows this product (A, B) or the collection scene (C). Chosen by the product's
place collection through `elmsnest-s-place` (`emit: 'collection'`).

| family (collection) | sentence | note |
|---|---|---|
| שביל — `תאורת-שביל-סולארית` | «אור נמוך שמלווה את הדרך.» | archetype A |
| קיר — `solar-wall-lights` | «אור על הקיר, בדיוק בנקודה שבחרתם.» | archetype B. No «חם» — the wall light has a 6000K option, warmth would be a colour claim |
| גינה — `ספוטים-ופרוז-קטורים-סולאריים` | «אור מכוון אל מה שרוצים להראות.» | archetype C. True of an adjustable spot and of a floodlight alike |
| מרפסת — `גרילנדות-ותאורה-דקורטיבית` | «נורות קטנות, וערב שלם סביבן.» | not rendered in the mock (no decor archetype), listed for approval |

Honesty line, rendered ONLY when the frame shows another store product than the page's (rule §3-3):

- «בתמונה: {product title}» — label, 12.5 px muted, the title linked to that product. On C: «בתמונה: מנורת גינה
  דו־ראשית מתכווננת <bdi dir="ltr">180°</bdi> – <bdi dir="ltr">10W IP65</bdi>» (the other product's own title, verbatim).

## 2. `elmsnest-s-pdp-checks` — «לפני שמזמינים» (after `ens_pdp_facts`, before `ens_related`)

Heading: «לפני שמזמינים»

Lead (a label, no period), by the solar gate:
- solar → «שלוש בדיקות קטנות, במקום עצמו»
- not solar → «שתי בדיקות קטנות, במקום עצמו»

The questions (each a question the buyer answers at the spot; the section asks, it never warns — the not-for line
under the button already warns):

| # | gate | question | source of the fact |
|---|---|---|---|
| 1 | solar only | «כמה שמש מגיעה למקום במשך היום?» | the guide's first question; a question about the buyer's spot, no product claim |
| 2 | every product | «עד לאן האור צריך להגיע?» | the guide's second question |
| 3 | solar only | «בחורף היום קצר יותר. לקחתם בחשבון?» | «בחורף היום קצר יותר» is a fact about the sun (BRIEF §3 allows it as a category fact); the second sentence is the question |
| 2′ | not solar only | «מאיפה יגיע החשמל למקום?» | a question about the spot; true for a mains light (a cable) and for a rechargeable one (a socket somewhere) — no «220V», no «מתחבר לחשמל» claim |

Solar branch renders 1 · 2 · 3. Non-solar branch renders 2 · 2′ (numbered 1 · 2 on the page). The gate is the
`elmsnest-s-place` test copied verbatim (metafield `custom.power_source == 'סולארי'`, else title + description
contain «סולארי»).

Link (the licensed ל־ form, P4; the PDP has no other guide link): «למדריך לבחירת תאורה ←» → `/pages/guide-garden-lighting`

The numerals «1» «2» «3» are decorative (`aria-hidden`), a lone digit each, so no `<bdi>` is needed.

## Not said, on purpose

- No «לא מתאים כש…» (the not-for line says it once). No «מתאים כדי…» (the kicker). No IP code, no hours, no lumens,
  no watt (the facts). No price, no button, no terms, no contact line, no place list, no product grid.
