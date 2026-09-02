# "המתג" (switch) — self-critique

Files: `index.html` (A, crystal balls, 24 variants) · `path.html` (B, path light, 1 variant) · `wall.html` (C, wall light, 8 variants, mains) · `switch.css` · `switch.js`
Shots: `shot-*` / `shot-path-*` / `shot-wall-*` (`-desktop`, `-mobile`, `-desktop-fold`, `-mobile-fold`).
Heights — index 7882 / 8600 · path 5899 / 6531 · wall 6027 / 6832. No horizontal overflow, no JS errors on any of the six renders.

## The one idea

**The page is one stage the buyer operates: every choice is a switch that changes the product's own light in front of you** —
picking a length lights that many bulbs along a real string while the price counts up; picking watts and Kelvin resizes and
recolours the halo on the wall; picking quantity adds bollards along the path — and the same stage goes dark when you flip
it to the one thing the lamp is not for.

## The spine, answer by answer

| # | Lands on | How |
|---|---|---|
| 1 | Screen 1 — the stage (`#stage`) | Place kicker "מרפסת ופינת ישיבה · מתאים כדי ליצור אווירה" + editorial h1 "הערב מתחיל מהכדור הראשון." over the night photo; the string lights bulb-by-bulb on arrival; title in Heebo; price + הוספה לסל at y≈504 on 390 — inside the fold. |
| 2 | Screen 2 — the switch (`#fit`, starts at y=844 mobile, toggle at y=1136) | A real toggle knob between the two halves of the approved pair, verbatim: **ליצור אווירה** / **צריך אור חזק — זו אינה מטרתה**. Flipping it to "לא מתאים" darkens the string below and prints "לא נדלק. זו הנקודה." The negative is demonstrated, not claimed. Path uses the שביל pair ("המקום כמעט אינו מקבל אור יום"), wall the כניסה/קיר pair ("נדרש אור חזק וקבוע לאורך כל הלילה"). |
| 3 | Screen 3 — night gallery (`#night`) | Two staggered figures, no grid: the bulb close-up (what the crystal does to the light) and the trellis shot as the scale cue — "כל כדור מול עלה. 5 מטר מכסים פינה אחת; 22 מטר עוטפים חלל שלם." Both light on arrival; the product's light is the only light. |
| 4 | Screen 4 — the ledger (`#lengths`) | Six rows, each a string **drawn to scale** (5 m short, 22 m spanning the row) with its bulb count, its own price, its ₪-per-metre, and its own add-to-cart. Every price is readable before selecting. Colour is a separate quiet axis in the hero with the standing line "הצבע לא משנה את המחיר". Wall: four rows = W × K with 219.90 / 222.90 / 249.90 / 252.90 and a halo that grows/cools per row. Path: a 1–8 quantity rail with the running total — no one-value picker anywhere. |
| 5 | Screen 5 — the facts (`#facts`) | An enormous outlined **IP65** that fills with glow when lit, beside a hairline `<dl>` of only what the description states: solar charging (and therefore the panel needs sun), ~8–10 h, IP65, 8 modes, 5–22 m / 20–200 LED, the four light colours. Nothing about dimensions, because the description has none. |
| 6 | Screen 6 — four numbers (`#terms`) | 0 ₪ / 8–17 ימי עסקים / 14 יום / 1 תמונה as four enormous glow numerals with the full wording under each, including the ≤5 % or 100 ₪ cancellation fee and "נשלחים ממחסנים מחוץ לישראל". The sticky buy bar is on screen throughout, so it is always within one screen of a buy action. |
| 7 | Screen 7 — why here (`#ask`) | One quiet line plus the «מי אנחנו» quote *"כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה."* and one link. No table, no competitor. Device #2 already did the real work. |
| 8 | Screen 7 + footer | Two low-commitment steps side by side: **לשלוח תמונה של המקום** (mailto with a prefilled subject; the word "בוואטסאפ" appears nowhere) and **להתחיל מ־5 מטר — 89.90 ₪**, which snaps the stage back to the shortest string and submits it. |

Order note: I kept the default order but pulled #4 *forward into screen 1* as the length rail under the fold line — the
buyer sees all six prices before scrolling — and left the full ledger at position 4 for the decision itself.

## Where it sells hardest

The ledger. Twenty-four variants collapse into one decision because each row *is* the product at that size: a string you
can measure by eye, its bulb count, its price, its price per metre, and a button. Nothing is hidden behind a click, and
the two 89.90 rows make the 6.5 m the obvious first buy. Second hardest is screen 2: a store that hands you a switch
labelled "this is when I am wrong for you" earns the right to be believed on everything else — and it costs no honesty,
because the sentence is the owner's own approved one.

## Where it is weakest

**The colour axis is invisible in a still.** Colour is half of the 24 (6 lengths × 4 colours) and the page treats it
correctly — a quiet second row of dots that never touches the price — but its whole payoff is motion: the string
recolours to blue / multi / white when you pick. A judge reading PNGs sees only the yellow state, so the page looks
like a 6-variant page. Secondary: product A has only two usable local images, so screen 3 carries less evidence than
the path and wall pages do.

## With one more day

1. Give the colour axis a still-visible payoff: four short lit string fragments in the hero, one per colour, so the
   choice reads without interaction (and screenshots well).
2. Make the switch in screen 2 auto-demonstrate once on arrival — flick dark for 600 ms and back — so the device is
   discovered without a tap; keep it off under reduced motion.
3. On mobile the six-stop rail is legible but tight at 390; test a two-line stagger so the ₪-per-metre can ride along
   as it does on desktop.
4. Add the "לפני שימוש ראשון" note from the path description as a fifth `<dt>` on B, and re-check the wall facts list
   against the C bullets for anything I left on the floor.
5. Replace the wall page's shelf gap: C and B end at #7 with no related module — worth carrying the index shelf across
   so all three archetypes prove the card design.
