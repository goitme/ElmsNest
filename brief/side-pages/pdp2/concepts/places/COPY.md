# Concept «places» — every Hebrew sentence (new copy, for the owner's approval)

Guillemets are notation. No «+», no «;». Headings and tile words carry no terminal period; the one sentence keeps
its period. Nothing below is on the product page today: not the kicker's «מתאים כדי …», not the not-for line, not
the terms, not the specs, not the contact line.

## Section 1 — `ens_pdp_places` (`sections/elmsnest-s-pdp-places.liquid`)

### Heading (one setting per case, chosen by rule — NOTES.md)

| case | text | renders on | why this wording |
|---|---|---|---|
| every tile shows the page's own product | «אותו אור, מקומות אחרים» | A | true: the same product, photographed in three places |
| any tile shows a sibling product, 2–3 tiles | «מקומות לאור כזה» | B | «a light like this» — claims nothing about which product is pictured; the credit line says which |
| one tile, sibling product | «מקום לאור כזה» | C | singular of the same |

The heading is not a claim about the product: it names places. The licensed place words (שביל · קיר · גינה ·
מרפסת) are not used anywhere in this concept (P2 keeps them for the kicker, the home fit block and the collection
header).

### Tile words (one word or one short line, on the photograph)

| family | tile | word | frame | what the frame shows |
|---|---|---|---|---|
| path (A) | lead | «מדרגות» | own_stainless…_6 | three bollards on stone garden steps |
| path (A) | 2 | «כניסה» | own_stainless…_4 | two bollards along a brick house at dusk |
| path (A) | 3 | «בין השיחים» | own_stainless…_2 | one bollard beside shrubs on a stone path |
| wall (B) | lead | «פרגולה» | own_waterproof…_6 | the page's own white sconce on a stone pillar under a pergola |
| wall (B) | 2 | «חצר» | own_outdoor-bidirectional…_5 | sibling square up-down light, patio with dining chairs |
| wall (B) | 3 | «אבן צפחה» | own_outdoor-bidirectional…_6 | sibling cylinder up-down light on a slate wall |
| spot (C) | single | «ליד האדנית» | own_dual-head…_3 (clean slice) | sibling dual-head garden light on a dark terrace beside a planter |

Not written for decor in this round (no decor archetype in BRIEF §5); the same section would take, for the string
lights, «גדר» · «שולחן» · «שרכים» from own_solar-crystal-ball-string-lights_5 / own_solar-edison-string-lights_4 /
own_solar-firefly-garden-lights_4 — proposed, not rendered, so they are not in the approved set.

### Credit line (13 px, muted, only when a tile shows another store product — BRIEF §3 image rule 3)

Pattern: «{tile words} — בתמונה: {product title}», the title linked to `/products/{handle}`. With one tile the
prefix is dropped.

- B: «חצר, אבן צפחה — בתמונה: מנורת קיר LED חיצונית דו־כיוונית IP65» → `/products/outdoor-bidirectional-led-wall-light-ip65`
  (the title is the product's own; `LED` and `IP65` in `<bdi dir="ltr">`)
- C: «בתמונה: מנורת גינה דו־ראשית מתכווננת 180° – 10W IP65» → `/products/dual-head-garden-light-10w-ip65`
  (`180°` and `10W IP65` in `<bdi dir="ltr">`)
- A: no credit line (every tile is the product).

## Section 2 — `ens_pdp_winter` (`sections/elmsnest-s-pdp-winter.liquid`) — solar products only

One hairline row, label + value, in the facts' language:

- label (13 px): «בחורף»
- value (16 px): «היום קצר יותר, וגם האור בלילה.»

Source of the fact: the sun — a general fact about the category, not a product claim (BRIEF §3: «בחורף השמש קצרה
יותר» is the licensed kind of sentence). No hours, no percentage, no «פחות X». Gate: `custom.power_source ==
'סולארי'`, else title + description contain «סולארי» (the three-state test of `elmsnest-s-place`). Renders on A and
C, prints nothing on B (mains) and on the wall collection's five mains lights and the rechargeable one.

The home says the same fact in other words («בחורף השמש קצרה יותר, והפאנל נטען פחות.», `elmsnest-s-home-winter`).
This line is new wording, placed at the point of sale directly above the facts' «זמן עבודה» row — NOTES.md answers
«twice» honestly.

## Alt text

All seven `<img>` carry `alt=""`: the word on the tile carries the meaning, the credit line names the product.
