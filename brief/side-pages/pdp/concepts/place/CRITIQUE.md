# CRITIQUE — concept "place" (המקום קודם), designer 1 of 5

Read from the PNGs (`shot-*.png`, `shot-path-*.png`, `shot-wall-*.png`), then the HTML.
Heights (shot.js): A `index.html` 7310 / 8015 px · B `path.html` 4038 / 4847 · C `wall.html` 3186 / 3740 (desktop / mobile). No horizontal overflow, no JS errors, on any of the six renders.

## The one idea

The page opens on the buyer's own place at night — a terrace, a path, an entrance — and the product is the only thing that lights it; every screen after that is one of the place's own questions (does it get sun? how many metres to go round? how many units along the path? how wide is the wall?), and the answer to each is the buy decision.

## The spine, answer by answer (A = crystal-ball string; B/C where they differ)

| # | Hesitation | Where it lands | Device |
|---|---|---|---|
| 1 | Is this for my place? | **Screen 1** (hero, `#place`) | Full-bleed collection scene of the terrace at night, dim → lit on arrival (`[data-lamp]`); eyebrow = place + approved "מתאים כדי ליצור אווירה"; serif line "המרפסת שלכם, אחרי השקיעה."; a scrim with the product close-up, Heebo title, the live variant mirror (`5 מ׳ / 20 נורות · צהוב`), price and **הוספה לסל** — inside the 1440×900 fold and inside the 390×844 fold (mobile fold shows title, price, button). B: the product's own three-bollard path is the place; C: the cube on plaster at dusk. |
| 2 | Will it work where I want it? | **Screen 2** (`#fit`) | "שתי שאלות על המקום שלכם": two segmented questions whose answers are the approved pair itself — [ליצור אווירה / צריך אור חזק] and [שמש במשך היום / כמעט אינו מקבל אור יום]. Both default to "fits", so the crystal-ball string lights on arrival; any wrong answer flickers it dark and prints the verbatim negative ("צריך אור חזק — זו אינה מטרתה" or the solar clause). B has one question (the sun), and its dark-bushes photo is the lamp that goes dark. C carries its pair as a quiet line under the ledger (screen 1 + ledger were the brief's minimum for C). |
| 3 | What does it look like at night? | **Screen 3** (`#night`) | Full-bleed trellis photo, lit on arrival, with the close-up inset overlapping the corner; captions from the description ("האור משתקף בתוך כל כדור"). Scale cue is the trellis slats and, on screen 4, the bulbs-per-metre density drawn from the real variant values. |
| 4 | What do I get, what does the long one cost? | **Screen 4** (`#tape`) | "כמה מטר להקיף?" — six hairline rows, each a wire whose length is proportional to the metres (5 → 22.7 %, 22 → 100 %) carrying its bulb count as dots, with **its own price and ≈ ₪/metre visible before selecting** (18.0 → 8.2 ₪/מ׳ — the long one sells itself). Selecting lights that wire; colour is an inline radio line "לא משנה את המחיר" that recolours the bulbs. The buy line under the tape and the hero scrim and the sticky bar all mirror one state. C: four rows (6W/12W × 3000K/6000K) with the halo growing with the wattage and the tint following the Kelvin; body colour quiet; "יחידה אחת / זוג, סימטרי" from the description doubles the quantity. B: no picker at all — a quantity stepper as "units along the path", eight bollards light up as you add, total = n × 169.90. |
| 5 | What could go wrong? | **Screen 6** (`#facts`) | "לילה אחד, מהשקיעה ועד הבוקר": the enormous outline numeral 8–10 fills with glow on arrival; hairline list of only what the description states (dusk auto-on, 8 modes, IP65, 5–22 m); an explicit "מה שלא כתוב" row saying charging time, ball size and spacing are not in the description. B adds the first-use ON + 3 h and the 6 h charge; C has no solar sentence anywhere (grep: 0 "סולאר", 0 "חשכה"). |
| 6 | What happens after I click? | **Screen 5** (`#terms`), directly under the buy line | The four numbers as a compact two-column hairline ledger: 0 ₪ / 29.90, 8–17, 14 days (≤5 % / 100 ₪), 1 photo. Reordered before the facts because the buy line is the moment the numbers are needed — the buyer reads them without leaving the ledger. |
| 7 | Why here? | **Screen 7** (`#step`, right column) | The «מי אנחנו» quote in the serif, one line ("אמרנו כבר למעלה מתי זה לא מתאים"), one link: info@elmsnest.com. No table. |
| 8 | Something smaller than buying? | **Screen 7** (`#step`, left column) | Two hairline options: "לשלוח תמונה של המקום" (mailto with prefilled subject + body; never "בוואטסאפ") and "או להתחיל ב־5 מטר — 89.90" with its own add form. The same mailto also sits under the two questions and in the 1-photo number. |

Related module (screen 8, `#more`): three terrace products on a lit floor, uneven widths (330 / 240 / 280), photo → place kicker → Heebo title → price by the rule (מ־139.90 · מ־89.90 · 99.90) → "לבחירת אורך" or a real add form. The rope light is cropped 4/3 from the bottom to drop its baked IP65 badge.

## Where it sells hardest

- The tape (screen 4). Twenty-four variants collapse into "how many metres" — one row per length with the price and the per-metre price already printed, so 22 m at 8.2 ₪/מ׳ against 5 m at 18.0 ₪/מ׳ is an argument the page makes without a word. The description's own advice ("שרשרת מעט ארוכה יותר נראית מלאה") sits next to it. Colour is demoted to a sentence, which is what "never changes the price" deserves.
- The fold on the phone: place, kicker, serif line, title, price, button, all in 844 px; the sticky bar takes over the moment the hero button scrolls off and always shows the chosen length + colour + price.
- Screen 2 is honest and still sells: the lamp lights by default, and the only way to turn it off is to describe a place this product is not for — the two negatives are the approved sentences, verbatim.

## Where it is weakest

- The place scene on A is the collection photo (globe bulbs over a sofa), not this product; the product appears in the scrim and from screen 3 on. It is labelled as the place, not the product, but a buyer could read the hero bulbs as the product. B and C use the product's own context photo and do not have this gap.
- The "8–10" numeral device repeats the homepage's outline → glow trick (the places numerals); it is the same family, but a stricter judge may count it as borrowed rather than new.
- Screen 5 (the four numbers) is a 2 × 2 of hairline lines — not boxes, but the most conventional composition on the page.
- The mobile ledger is six rows tall (≈ 1,150 px); it is not rectangles, but the buyer scrolls past four prices to reach the 22 m row. A "מהאורך הארוך" toggle or reversing the order would put the best value first.
- No spacing-between-units cue on B beyond the description's "במרווחים אחידים" — the description gives no distance, so the bollard row shows count, not metres.

## With one more day

1. Replace A's hero scene with a real photo of this product over a seating area (the trellis image is the closest, but it has no furniture for scale); until then, add a one-word "המקום" tag on the photo so it cannot be read as the product.
2. Make the tape interactive as a tape: drag a handle along one wire and have the price snap to the next length up ("measured 8 m → 9.5 m"), with the bulbs filling behind the handle.
3. On mobile, collapse the ledger to the selected row + "עוד אורכים" and let the sticky bar's price open the row list — keeps screen 4 in one phone screen.
4. Liquid: the rows are already a list of variants with per-row `/cart/add` forms under `html:not(.js)` (a `<select>` of colours per length); `?variant=` URL sync and the Kalles drawer hook (`/cart/add.js`) are the remaining plumbing. The two-question device is two radio groups reading a `power_source` metafield for the solar clause.
5. Wall: light the plaster photo itself with the chosen wattage (a second halo layer on the hero at 12 W) instead of only the ledger swatch.
