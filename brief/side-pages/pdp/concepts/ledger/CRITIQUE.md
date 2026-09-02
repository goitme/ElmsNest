# הפנקס — THE LEDGER · self-critique (designer 2 of 5)

Files: `index.html` (A, crystal balls, 24 variants) · `path.html` (B, path light, 1 variant) · `wall.html` (C, wall light, 8 variants, mains).
Renders: `shot-*.png`, `shot-path-*.png`, `shot-wall-*.png` (desktop 1440 / mobile 390, full + fold). Heights: A 7190 / 8219 · B 5643 / 6639 · C 5511 / 6443 px. No horizontal overflow, no JS errors.

## The one idea

The variant matrix *is* the hero: every length is a row on a hairline — an enormous metre numeral, its bulb count, its price-per-metre and its price in glow — so 24 choices read as one table you can decide in ten seconds, and the row you choose is the only thing on the page that lights.

Screen 1 states it in the serif ("כמה מטרים של ערב.") and in the device: the ledger is not a picker that hides the price behind a click; the price sits in every row before you touch anything, colour is a quiet axis under the table with "לא משנה את המחיר" written next to it, and the chosen row lights its numeral, the price, the tape under the photograph (0–22 m) and the halo on the photo (the 22 m halo is bigger than the 5 m halo). Numerals arrive as outlines and fill on arrival, staggered by row — the ledger "switches on" as you reach it.

## The spine, answer by answer

| # | Hesitation | Where it lands | Device |
|---|---|---|---|
| 1 | What is this, for my place? | Screen 1, top | Eyebrow with the place word and the approved phrase verbatim ("מרפסת ופינת ישיבה · מתאים כדי ליצור אווירה"), serif line, product title in Heebo, the ledger with prices, "השורה שבחרתם" + price + הוספה לסל. On 390 the price and the button sit above the ledger inside the first 844 px; the sticky bar mirrors the row once the button scrolls away. |
| 2 | Will it work where I want it? | Screen 2 (`#fit`, y≈1250 desktop / y≈1400 mobile — inside the second screen) | Two lines of the pair: "ליצור אווירה." at wall scale, FRL 900, lights on arrival; "צריך אור חזק — זו אינה מטרתה." stays an outline and never fills ("השורה הזאת לא נדלקת. זו הנקודה."). The solar sentence from the description under a hairline. On B the pair is two photographs: the bollard by the wall lights, the bollard in the bushes (`-1`) is `data-lamp="off"` and never lights. |
| 3 | What does it look like at night? | Screen 3 (`#night`), full-bleed | The decor collection scene (seating = human scale) as a 100svh lamp, the trellis inset, and the spacing rule: one metre of *the row you chose* drawn as N glowing dots (20/5 → 4, 200/22 → 9 — arithmetic on the option values, nothing typed). |
| 4 | What do I get, what does the long one cost? | Screen 1 | The ledger: 6 rows × (metres, bulbs, ₪ per metre, price). The per-metre column is the honest argument for the long string (17.98 → 8.18 ₪/m). Colour under the table, four dots, no price change. C: two wattage rows, each holding two Kelvin lines with their own price; body colour as two photo swatches. B: the ledger becomes "כמה יחידות" with unit multiples (1 → 6) and the description's own line "יחידה אחת מאירה נקודה — שורה של יחידות יוצרת אפקט". |
| 5 | What could go wrong? | Screen 4 (`#facts`) | The seven description bullets as a column of numerals (8–10 hours as the enormous one; 8 modes; IP65; 5–22 m; solar; 4 colours) beside the description's own sentences; a closing line saying the dimensions are not in the spec we received, so they are not here. |
| 6 | What happens after I click? | Screen 5 (`#after`) — and a one-line version under the buy button in screen 1 | A receipt: the chosen row mirrored with price and a second הוספה לסל (submits the same form), then the four numbers as a ledger (0 ₪ · 8–17 · 14 · 1 תמונה). Reordered: the compact line lives next to the button on screen 1 ("משלוח לנקודת איסוף חינם · 8–17 · ביטול 14 · כל המספרים"), the full numbers sit one screen from the *second* button. |
| 7 | Why here? | Screen 6 (`#why`) | The «מי אנחנו» quote in the serif, one line ("we said when not — that was screen 2"), one link. |
| 8 | Something smaller than buying? | Screen 6, right beside #7 | "לא חייבים להחליט על 22 מטר הערב." — a ghost pill "לשלוח תמונה של המקום" (mailto with prefilled subject; no WhatsApp word anywhere) *or* "להתחיל מ־5 מטר · 89.90 ₪" which selects row 1 and returns to the ledger. B: "להתחיל מיחידה אחת". C: "להתחיל מ־6W אור חם". |

Related module (screen 7): three decor products on a shelf line with different widths and one raised — the card is photo / place kicker / Heebo title / price by the rule (מ־139.90, מ־89.90, 99.90) / "לבחירת אורך" or a real `הוספה לסל` form for the single-variant firefly. Header: static 70 px transparent strip, gold logo centred, five menu items split around it, search + cart. Footer: one sky-4 block.

## Where it sells hardest

- Screen 1 on both viewports: the buyer sees all six prices, the per-metre price and the bulb count before touching anything. The "24 choices" become "which row" — the decision the brief asked for.
- The chosen row lights, the tape fills, the halo grows: the interaction *means* "more metres, more light".
- The not-for answer is inside screen 2 and is the second-largest thing on the page; the dark outlined line is more persuasive than any table.
- The receipt at the end re-offers the button next to the four numbers, and the small step is concrete ("start from 5 m · 89.90") rather than a vague "contact us".

## Where it is weakest

- Screen 1 is typographic, not photographic: the winning homepage opens on a night garden, this opens on numerals. The photo is there (close-up, lit, with the tape) but it is the second thing you see on desktop and below the fold on mobile. A judge who wants the lamp *in its place* on screen 1 will dock this.
- The evidence for A is thin — only two usable photos — so the trellis picture appears twice (fit + night inset). B and C have better photo pairs.
- The wall light's studio photos (grey ground) sit awkwardly on the sky; the quadrant crops for the body-colour swatches are a workaround, not a design.
- The four numbers repeat once (compact line + full ledger). Deliberate, but a purist may read it as "terms twice".
- The "1 תמונה" line, the mailto and the small step all point at the same email — honest (no WhatsApp yet) but three doors to one room.

## With one more day

1. Draw the string: an SVG catenary above the ledger whose lit bulbs scale with the chosen row (20 → 200) — the product's own light as the hero's motion, so screen 1 is a lamp *and* a table.
2. A photo ground for screen 1 on mobile only (the close-up at 22 % brightness behind the ledger, lighting with the first row) so the phone opens on light, not on sky.
3. Ask the owner for one more night photograph of A on a balcony to replace the second use of the trellis, and a night exterior for C.
4. Build the Liquid: rows from `product.variants` grouped by option 1 with `<bdi>` prices, the per-metre column computed in Liquid from the option string, `?variant=` sync, `/cart/add.js` + drawer; the no-JS path already exists (a `<select name="id">` inside `<noscript>`; B's quantity radios post natively).
5. Tighten the mobile eyebrow (one line) and test the tape labels at 320 px.
