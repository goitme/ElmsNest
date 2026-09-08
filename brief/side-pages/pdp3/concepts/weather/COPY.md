# Concept «weather» — every Hebrew sentence, per section, with the gate it lives under

Rules applied: Hebrew only, every sentence short, no hours / lumens / IP / «best» / reviews / counts / urgency, no «+»,
no «;», no terminal period on labels and headings, Latin (the credit lines) inside `<bdi dir="ltr">`. Nothing the page
already says: not the kicker, the price, suits / not-for, the scene's place heading and line, the dusk row's two
sentences, the specs, the terms, the contact.

## Section 1 — `ens_pdp_weather` («בחוץ, כל השנה»)

Gate: the product's own bullets carry an outdoor IP code (IP65 / IP66 / IP67 / IP68 — the facts' numeral loop, same
tokens). Without one the section prints nothing. Which PAIR: the dusk row's solar test — solar → the panel pair;
not solar → the garden pair. The four lines are the same on both pairs; only the captions differ.

| # | text | role | where |
|---|---|---|---|
| 1 | בחוץ, כל השנה | heading (h2), no period | every page that passes the gate |
| 2 | גשם של ינואר. התאורה נשארת בחוץ. | the line under the rain tile — two short sentences | both pairs (A, B, C) |
| 3 | שמש של אוגוסט. אותו הדבר. | the line under the sun tile | both pairs (A, B, C) |
| 4 | טיפות גשם על פאנל סולארי גדול · צילום: `h080 (CC BY-SA 2.0)` | caption + credit, rain tile, SOLAR pair | A, C |
| 5 | תא סולארי מקרוב, בשמש · צילום: `Guilhem Vellut (CC BY 2.0)` | caption + credit, sun tile, SOLAR pair | A, C |
| 6 | טיפות על גבעול, אחרי הגשם · צילום: `jenny downing (CC BY 2.0)` | caption + credit, rain tile, GARDEN pair | B |
| 7 | קיר לבן בשמש של צהריים | caption, sun tile, GARDEN pair (CC0 — no credit owed) | B |

What the lines claim: only the general fact the listings state — an outdoor light stays outdoors, in rain and in
sun. No number, no «waterproof», no code (the IP code is the facts' numeral, directly under this section). The
month names (ינואר, אוגוסט) are Hebrew words, not digits.

## Section 2 — `ens_pdp_hour` («בין ערביים»)

Gate: the place word from `elmsnest-s-place emit:'word'` (שביל / קיר / גינה / מרפסת) is not blank. The two products
the scene treats as exceptions (the indoor birch branches, the camping lantern — their place is not a courtyard)
print nothing. ONE photograph for all four families; the line changes with the word.

| # | text | role | where |
|---|---|---|---|
| 8 | בין ערביים | heading (h2), no period | every page that passes the gate |
| 9 | השביל, רגע לפני שצריך אור. | the family line — path (word שביל) | A |
| 10 | הקיר, רגע לפני שצריך אור. | the family line — wall (word קיר) | B |
| 11 | הגינה, רגע לפני שצריך אור. | the family line — spot (word גינה) | C |
| 12 | המרפסת, רגע לפני שצריך אור. | the family line — decor (word מרפסת) | decor pages (not an archetype this round) |
| 13 | חצר של בית במקסיקו, בשקיעה · צילום: `Dago Gonzalez (CC BY 4.0)` | caption + credit under the photograph | A, B, C |

What the line claims: nothing about the product — it names the hour before a light is needed and the place the
family is for. The caption names the photograph as a house courtyard in Mexico at sunset, so it never reads as
this product's place or as this product.

## Owner-editable (schema text settings, defaults = the rows above)

heading (both sections), line_rain, line_sun, caption_rain_solar, caption_sun_solar, caption_rain_garden,
caption_sun_garden, line_path / line_wall / line_spot / line_decor, caption_hour. Every setting runs through the
facts' Latin/number `<bdi dir="ltr">` token loop (P6) so a typed credit never flips.
