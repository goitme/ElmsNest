# Concept «questions» — before you buy

## What it is
The store as the friend who says «ask this first». Two sections, no new answers to old questions:

- **[A] «שלוש שאלות לפני שקונים»** — the guide's three questions as three photographic cards, one line each, then the page's single guide link. Inserted **after the four product cards and before «מתי כן, ומתי לא»**: the shopper has just looked at a product; before the fit block tells him where it does not belong, this tells him what to check. The three photos are the same garden at three hours — noon (sun on the panels), night (the steps), dusk (the threshold) — so the daylight frame is read as part of a day-to-night set, not a daylight garden shot on its own.
- **[B] «ובחורף?»** — one cool image, a heading and three lines. Inserted **after the fit block and before the terms strip**: the last honest note before the numbers. On the phone the band runs edge to edge; on desktop it is a 4:3 photo beside the text.

Page order becomes: hero → tiles → cards → **[A]** → fit → **[B]** → terms → footer.

## Measured (playwright, `getBoundingClientRect`, real fonts from the offline pack)
| | 390 wide | 1366 wide |
|---|---|---|
| [A] ens-ask | **629 px** (cap 675) | 853 px |
| [B] ens-winter | **409 px** (cap 675) | 633 px |
| whole mock page | 5370 px = **6.36 screens** of 844 (cap 7.5) | 5114 px |

The mock page keeps the existing bands at their measured heights (hero 844, tiles 761, cards 781, fit 690, terms 397, footer 848 = the remainder of the 4321 px current page). With the guide link switched off, the fit block will lose roughly 40 px, so the real total is ≈ 6.3 screens. Desktop band heights are read off `home-d-js-full.png` (905 / 655 / 600 / 540 / 400 / 518) and are approximate.

## What it refuses
- No fifth place list, no product grid, no second terms, no second contact line. [A] names no collection and shows no price; [B] sells nothing.
- No claim: no hours of light, no lumens, no metres, no «IP65 on everything». Every line is a fact about the sun, the season or light in general (COPY.md lists the source of each).
- Only one guide link on the page. The cards are not links, so the guide link count stays at one (BRIEF §3 seed 2). If judges want the cards tappable, the foot link goes and the three cards link to the guide instead — still one destination, but three anchors; the safer reading of «one guide link per page» is the one built.
- No credit caption anywhere (three store frames, one CC0), so no 11 px muted line competes with the copy.
- No JS, no carousel, no parallax, no lamps, no hover reveal. Hover only recolours the link. Reduced motion respected.
- Nothing twice: the night twin of the day frame (`own_powerful…_2`) is deliberately left unused.

## Craft notes
- Same skeleton as the existing sections: `env2-section` + `env2-wrap`, the same h2 size (`clamp(25px,3.4vw,44px)`), card ground `#05070c` on the `#1f1e1d` hairline, radius 0, logical properties, Frank Ruhl Libre for questions and numerals, Heebo 300 for lines.
- Cards on the phone are rows (124 px square photo on the inline-start side, text beside it) so three photographic cards fit in 0.75 screen; on desktop they are three columns with square photos, question and line beneath.
- The winter band is the one cold-blue image on a gold page — deliberate, it is what the heading says. It is the section the owner is most likely to swap for his own rainy-day photo, so the image is the block's `image_picker` with the asset as default.
- The numeral rides in gold Frank Ruhl 500 at 13–14 px, like the terms strip's numbers, so the two sections rhyme across the fit block.

## Theme files (for the build, not part of this mockup)
- `sections/elmsnest-s-home-ask.liquid` — settings: heading, lead, guide_label, guide_link; 3 blocks `question` with `image_picker`, `object_position`, `question`, `line`; default rendering from `assets/ens-home-ask-{1,2,3}.jpg`.
- `sections/elmsnest-s-home-winter.liquid` — settings: heading, line_1, line_2, line_3, `image_picker`, `object_position`; default `assets/ens-home-winter.jpg` (pre-cropped band).
- `templates/index.json`: add `ens_ask` after `ens_products`, `ens_winter` after `ens_fit`; set `ens_fit.settings.guide_label` to `""`.
