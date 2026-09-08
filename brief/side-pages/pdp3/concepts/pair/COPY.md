# Concept «pair» — every Hebrew sentence, per section

Two new sections. **Neither is gated**: the same words print on every product, in every family, solar
or not. Nothing here is per-product data, so there is one copy set and nothing to write per product.

Rules kept: short, claim-free (no hours, lumens, IP, «best», reviews, counts, urgency), no «+», no «;»,
no terminal period on a label, Latin/digits inside `<bdi dir="ltr">`.

---

## 1. `ens_pdp_pair` — «בין הצהריים לשקיעה»

Gate: **none** (prints on every product page, path · wall · spot · decor, solar and mains).

| # | role | Hebrew | note |
|---|---|---|---|
| 1 | heading (h2) | בין הצהריים לשקיעה | no period, it is a label |
| 2 | the one line | השעה משנה את מה שרואים בחוץ. | the only full sentence in the section |
| 3 | hour tag, right frame | צהריים | 10.5 px, letterspaced, ink-2 |
| 4 | caption, right frame | סמטת אבן בין קירות | names the place, not the product |
| 5 | hour tag, left frame | שקיעה | same tag, in gold — the two-tone |
| 6 | caption, left frame | שביל אבן וקיר אבנים | names the place, not the product |
| 7 | credit, left frame | צילום: <bdi dir="ltr">Corey Leopold (CC BY 2.0)</bdi> | 11 px muted, verbatim from `images/SHORTLIST.md` |

The right frame is CC0 and carries no credit line, so only one credit is drawn in the section.

## 2. `ens_pdp_checks` — «לפני שקונים»

Gate: **none**.

| # | role | Hebrew | note |
|---|---|---|---|
| 8 | heading (h2) | לפני שקונים | row scale, 20 px serif |
| 9 | statement, tile 1 (right) | המקום נמצא בחוץ | statement, not a question, no period |
| 10 | statement, tile 2 | הגובה שבו מתקינים | |
| 11 | statement, tile 3 (left) | המרחק בין הנקודות | |
| 12 | caption under the row | שלושה חלונות בתמונה אחת של קיר גינה | says the three squares are one photograph |
| 13 | guide link | למדריך לבחירת תאורה ← | the arrow is an `aria-hidden` span, as in the scene |

The link is the page's **only** guide link: `ens_pdp_scene`'s `link_label` setting is emptied in
`templates/product.elmsnest.json` so it is not said twice (see NOTES §6).

---

## Alt text (read by screen readers, never drawn)

| image | alt |
|---|---|
| right pair frame | סמטת אבן צרה בין קירות אבן, כד חרס וצמחייה, בשמש של צהריים |
| left pair frame | שביל אבן מתעקל לצד קיר אבנים, שמי שקיעה כתומים מעל העצים |
| checks tile 1 | שמי תכלת מעל שפת קיר לבן ובוגנוויליה |
| checks tile 2 | קיר טיח לבן ושפתו, בשמש חזקה |
| checks tile 3 | חצץ וצל חד לרגלי הקיר |

---

## What the page already says, and is not said again here

kicker · price · «מתאים כדי…» / «לא מתאים כש…» · variant choice · buy · per-unit · the scene's place
heading and family line · the dusk row's two sentences about the sun · the IP numeral · the specs `dl` ·
the terms line · the contact line · the related cards. None of the thirteen sentences above repeats any
of them. The one adjacency is the guide link, resolved by emptying the scene's setting.
