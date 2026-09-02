# dialogue · «השיחה» — self-critique (designer 4, round 1)

Files: `index.html` (A · crystal balls, 24 variants) · `path.html` (B · path light, 1 variant) ·
`wall.html` (C · wall light, 8 variants, mains).
Shots: `shot-*.png`, `shot-path-*.png`, `shot-wall-*.png` (1440 / 390, full + fold).
Heights: A 9103 / 9013 · B 7047 / 7467 · C 5224 / 6058. No horizontal overflow, no JS errors on any of the six captures.

## 1. The one idea

**The page is the conversation you would have with the specialist, transcribed** — eight numbered beats, each one the
buyer's own hesitation set in Frank Ruhl Libre inside guillemets («ואם אני צריך *אור חזק* במרפסת?»), answered in Heebo
in the brand's voice, and then *proved by a device that lights* rather than by a paragraph.

## 2. The spine, answer by answer

| # | Screen / device | How it lands |
|---|---|---|
| 1 | **b1 hero** — full-bleed `-0` bulbs, place line `מרפסת ופינת ישיבה — מתאים כדי ליצור אווירה`, title in **Heebo**, `89.90 ₪` + range, `הוספה לסל` | The question *is* the H-line: «זה יתאים למרפסת שלי?». Price + buy sit **inside the 390×844 fold** (see `shot-mobile-fold.png`) and inside the 1440×900 fold. |
| 2 | **b2 fit** — enormous `מרפסת.` + a **lit / dark pair of the same SVG string**: right lit with halos `מתאים כדי / ליצור אווירה`, left genuinely dark `לא מתאים כש־ / צריך אור חזק — זו אינה מטרתה`; clicking the dark one flickers and refuses, `לא נדלקת. זו הנקודה.` Solar clause below as its own gold-labelled line. | The whole approved pair, verbatim, **inside screen 2**. The negative is not typography — it is a lamp that will not switch on. |
| 3 | **b3 night** — asymmetric two-figure gallery (`-2` trellis big, `-0` close-up overlapping), both `[data-lamp]`, the only light in frame is the product's; honest caption `התמונות להמחשה`. | Answers "what does it look like, really" without a scale claim the description cannot support. |
| 4 | **b4 ledger** — a **metre ruler** (5 · 6.5 · 9.5 · 11 · 13 · 22) over an SVG string that grows and lights with the choice, then six hairline rows: metres (FRL) · bulb count + a use sentence · price · `≈ ₪ למטר`. Colour is a **quiet second axis** underneath, one line, with `אותו מחיר לכל צבע`. | 24 variants become **one decision** (length) plus a footnote (colour). Every price is visible before selecting; `179.90` is shown to cost less than half per metre of `89.90`. |
| 5 | **b5 risk** — `8–10` as an enormous numeral, then facts as hairline rows (power source, `IP65`, 8 modes, first-use, winter) and the honesty note: what the description does not state is not stated. | Nothing typed; every row traces to a description bullet. |
| 6 | **b6 after** — the four numbers on a **vertical rail**, staggered left/right: `0 ₪` · `8–17` · `14` · `1 תמונה`. | Deliberately **not** four across (§11). A compact buy view sits immediately under it. |
| 7 | **b7 why** — the «מי אנחנו» line as a serif pull-quote, one lead, one link. No table, no competitor. | One quiet line, as the brief asks. |
| 8 | **b8 small** — enormous `שלחו תמונה של המקום.`, `mailto:` with prefilled subject/body, and the smaller alternative `להתחיל ב־5 מ׳ / 20 נורות — 89.90 ₪`. | Two sizes of "yes", the smallest one first. Never "בוואטסאפ". |

Ordering note: I kept the brief's default order and did **not** move #6 next to the buy button — instead the buy box
recurs. `data-buyview` appears **four times** (hero, ledger, after-the-numbers, small-step) and a full-width sticky bar
(top on desktop, bottom on mobile) shows whenever none of them is in view. So #6 is always within one screen of a buy.

**Related module** (`#more`): three products of the same place, staggered heights — photo, place kicker, Heebo title,
price by the rule (`מ־89.90` / `99.90` / `מ־139.90`), single-variant → `הוספה לסל`, multi → `לבחירת אורך`. No badges,
no swatches, no quick-add.

**B and C.** `path.html` carries beats 1–2 plus its own third beat — the **quantity device**: six bollards along a rule,
`כמה?` lights 1 / 2 / 3 / 4 / 6 of them, so a set becomes a picture instead of a number (no one-value picker anywhere;
`צבע אור: צהוב חם` is printed as a fact, not an option). `wall.html` carries beat 1 plus the ledger: four W×K price rows
(`219.90 / 222.90 / 249.90 / 252.90`) with שחור/לבן as the same quiet second axis, and a preview photo whose caption
follows the choice. **No solar sentence exists on C** — its hero lead says `מחוברת לחשמל הבית`.

## 3. Where it sells hardest

- **Beat 2.** A dark lamp that refuses to light is the strongest honesty device I could find that is also a *sales* device:
  it buys the credibility that the rest of the page spends. It is the same gesture on all three products.
- **Beat 4.** The ruler plus the `≈ ₪ למטר` column reframes the expensive variant as the cheap one. That is the single
  highest-leverage number on the page and it is not a discount.
- **The mobile fold.** Question, title, price, range and a 44 px+ `הוספה לסל` all above 844 px on all three pages.

## 4. Where it is weakest

1. **The colour axis is four items on one line** (צהוב · כחול · צבעוני · לבן). It is a radio group, not four boxes, but
   a judge reading §11 literally could flag it. I chose it over a 2×2 grid, which would have been worse.
2. **Beat 2 has a dead column.** The lamp pair is shorter than the text column, leaving ~200 px of empty sky on desktop
   (and a similar gap before beat 4 on mobile). It reads as air, not as rhythm.
3. **The ruler labels crowd on 390** — `13 · 11 · 9.5` nearly touch at the short end of the scale.
4. **Beat 3 is the least inventive screen.** Two photographs and a caption; it is the one beat where the answer is not a
   mechanism, only a picture.
5. **The recurring buy view is text-identical each time.** Four appearances of the same block risks reading as a repeat
   rather than as the conversation returning to the offer.

## 5. What I would fix with one more day

- Pull the beat-2 pair down to sit on the text baseline and let the enormous `מרפסת.` bleed off the inline edge, killing
  the dead column and gaining a full-bleed moment the page currently lacks between b1 and b3.
- Re-space the ruler logarithmically on mobile, or drop to 5 / 11 / 22 with the rest as unlabelled ticks.
- Give beat 3 a real device: a spacing cue driven by the ledger — choosing 22 מ׳ draws the string longer across the
  photograph — so #3 and #4 become one continuous mechanism instead of two sections.
- Vary the recurring buy view: hero = full, mid-page = one line, end = the small step only.
- Move the colour axis into the selected ledger row (it appears where the length is chosen) so the second axis is
  literally subordinate to the first, and the four-in-a-line question disappears.
