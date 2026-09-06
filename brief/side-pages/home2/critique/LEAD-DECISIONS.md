# Lead decisions on the home round 2 critique (2026-09-06, written before the fixer runs)

Inputs: the five lenses' findings in `critique/*.jsonl` (shopper 7.5 · owner 6.5 · designer 7 · honesty 8 · engineer —
see the file), two skeptics per finding (evidence, scope), the real per-section shots in `verify/`, and the contrast
experiment in `verify/exp/` (`contrast.py` with the text made transparent, so the number is the true background):
base → candidate 1 (tags backed .85 in ink, night scrim .84, band fade .72) → candidate 2 (tags off, band desktop crop
50% 40%) → candidate 3 (tags off, band fade .72). Numbers below are p90 (the brightest tenth behind the glyphs).

| # | finding (lenses) | decision | why / measured |
|---|---|---|---|
| 1 | «יום» corner tag unreadable on the day frame — 1.19–1.76:1 (shopper blocker, owner blocker, designer major, honesty major) | **Tags OFF by default** (`label_day`/`label_night` default empty, info «ריק = בלי תווית»); the tag CSS stays and gets an `.85` night backing in ink so a label the owner types is legible on any photograph (14:1 measured, c1). | P2: the two headlines already say day and night; the label was the one thing on the frames that said something twice. A backing on a 12 px word is a chip on the photograph; off is cleaner. |
| 2 | band sentence over the lower string of bulbs at 1366 — 3.50:1 (owner blocker, designer blocker, shopper minor) | **`object_position_desktop` default 50% 60% → 50% 40%.** No extra fade. | Measured 6.62:1 (c2) with the photograph untouched; a heavier fade (c3) only reaches 4.57:1 and dirties the frame. The c2 shot: bulbs along the top, city bokeh in the middle, the sentence on the dark boards. Also settles the owner's minor (half-bulbs sliced at the top edge with 60%). |
| 3 | steps 1–2 repeat the frame headlines (owner major, shopper major) | **One line under the frames instead of three numbered steps: «בלי חיבור לחשמל, בלי חשמלאי.»** Settings `line_1` (that default), `line_2`, `line_3` (empty; «ריק = בלי שורה»); hairlines kept, gold numerals dropped (two facts are not a sequence). | The owner's rule. «ביום נטען.» = step 1; «בלילה נדלק.» + the hero's «כשהשמש יורדת, הגינה נדלקת.» = step 2 (the automatic fact is on the page twice already). Only step 3 was new. |
| 4 | «בלי כבל» not true of the separate-panel products (honesty minor) | **«בלי חיבור לחשמל, בלי חשמלאי.»** — the listings' own phrase. Folded into #3. | A solar floodlight has a lead from its panel; it has no mains connection. |
| 5 | the 13 px eyebrow does not scope the facts to solar (honesty major) | **Heading instead of eyebrow: `<h2 class="env2-h">` «איך עובדת תאורה סולארית?»** at the section's top, the neighbours' scale. Setting `heading` replaces `eyebrow`. | The scope word is in the heading at heading weight; the question form matches «ובחורף?» right after it (how does it work? → day/night → and in winter?). |
| 6 | night headline 4.43:1 at 360 (shopper minor, owner minor, designer major) | **Apply the deeper night scrim** `rgba(5,8,14,0) 36% → rgba(5,8,14,.84) 100%` (night frame only; the day frame keeps its own rule). | With the exact measurement it already passes (4.79:1 at 360, 5.03 at 390, 5.99 at 1366); c1 lifts it to 6.4–7.9:1 and is invisible on an already dark frame. Cheap insurance for an owner-picked photo. |
| 7 | winter figure's 1 px hairline border (owner minor, designer minor) | **Drop the border.** | Photographs on this page carry no frame; only product cards do. |
| 8 | day/night desktop crops cut the nearest panel crown / the far lamp heads (designer minor ×2) | **Add `object_position_day_desktop` (default 50% 40%) and `object_position_night_desktop` (default 50% 30%)** applied at ≥ 901, like the band. | Same mechanism the band has; the owner gets one field per frame per breakpoint. |
| 9 | step hairlines hug the frames at ≥ 901 (designer minor) | **`margin-block-start: 28px` at ≥ 901** on the lines list. | Applies to the one-line list too. |
| 10 | winter heading 34 px vs the neighbours' 44 (designer minor) | **Drop the section's font-size overrides on `.ens-hw__h2`; let `env2-h`'s clamp scale it** (the neighbours' `clamp(25px,3.4vw,44px)` via the same class the fit block uses — check what the fit heading uses and copy it). | One scale for consecutive h2s. |
| 11 | card 2 of «מה שנדלק ראשון» is the diptych's product (owner major) | **Keep. Put it to the owner as a question on the page**, with the one-line change (another product in `product_list`). | Card = the product shot, diptych = the same product in its place by day and by night: the ordinary product → scene pair, not a repeat of a fact. Changing the SIMPLIFY product list is the owner's call, not the round's. |
| 12 | band sentence vs the hero headline (owner major, shopper minor) | **Keep «חושך הוא לא סוף הערב.»; list it for approval with the alternative the owner lens asked for.** | The hero says the garden lights up when the sun sets (a fact about the lamps); the band says the evening goes on (a sentence about people). The setting is one field if he wants another. |
| 13 | winter frame is a fourth bollard scene (owner minor) | **Keep; note on the owner page.** | No store frame has rain or a winter dusk with a wall or spot product (`images/SHORTLIST.md` §gaps); the picker swaps it in one click. |
| 14 | a `link` setting on the band (shopper minor) | **Not now.** | SPEC §1 C: no link, no button; a setting that does nothing by default is one more field. If the owner asks, it is ten lines. |
| 15 | the band's absolutely positioned img (the blank full-page capture; engineer lens pending) | **Put the img in flow** (`display:block; inline-size:100%; block-size:520/560px; object-fit:cover`), figcaption stays absolute. | Simpler box, no min-block-size trick, and the harness's full-page shot shows it — the render on phones was always fine. |

Copy after these rulings (SPEC §2 is amended to match; the owner page lists it for approval):
A heading «איך עובדת תאורה סולארית?» · A headlines «ביום נטען.» / «בלילה נדלק.» · A line «בלי חיבור לחשמל, בלי חשמלאי.» ·
B «ובחורף?» + the three lines unchanged · C «חושך הוא לא סוף הערב.». Labels «יום»/«לילה» are gone from the page.

## Engineer lens (returned after the table above was written; score 7)

| # | finding | decision | why |
|---|---|---|---|
| E1 | the `1200w` srcset candidate is a CDN re-encode heavier than the 1254-px original (347 KB vs 249 KB on the fence) and exactly what a DPR-3 phone picks for the band (major) | **Apply: delete the `1200w` candidate from the three asset srcsets** (day, night, fence); the browser steps 900w → 1254w. | Measured on the mirror. Winter's top candidate is already its 1100-px original. |
| E2 | three assets over the brief's 220 KB (day 294, night 291, fence 249 KB) (major) | **Keep the sources; record the accepted overage** in SPEC §3 and on the owner page with the phone figure. | A phone never downloads the originals for the diptych (600w ≈ 145 KB each) or winter (1100w = 165 KB); for the band a DPR-3 phone takes the 1254w original (249 KB) — ≈ 700 KB lazy-loaded for three sections. Re-encoding the day frame at 220 KB cost visible foliage detail (q54); the owner page says so. |
| E3–E5 | tag, band caption, night scrim | already ruled (#1, #2, #6). | |
| E6 | `<ol>` list semantics / aria-hidden numerals (minor) | **Moot after #3; `role="list"` added to the one-line `<ul>`** (list-style none). | |
| E7 | no alt setting, `alt: ''` discards an Admin alt (minor) | **Apply: `alt_day`, `alt_night`, `alt`, `alt` text settings (no default) rendered on both branches.** | SPEC §2 promised it. |
| E8 | band img absolute (minor) | already ruled (#15). | |
| E9 | `decoding: 'async'` missing on the picker `image_tag` (minor) | **Apply.** | The two branches are meant to be interchangeable. |
| E10 | `aria-label="נשימה"` when the sentence is blank names a landmark after the file (minor) | **Apply: no label when the sentence is blank.** | |

## Post-fix re-review (contract + render lenses over the pass-2 render, one skeptic each; `critique/REREVIEW.json`)

Contract: every «Apply» present, every «Keep» untouched, copy byte-identical, no empty text default, 0 Liquid errors. Four minors, all confirmed:

| # | finding | decision | why |
|---|---|---|---|
| R1 | the picker branch hands an already-escaped alt to `image_tag`, which escapes again (solar only) | **Apply**: raw value to `image_tag`, escaped value only on the hand-written asset `<img>`. | The hero already does it that way; the reviewer's «house style» framing was wrong, the skeptic corrected it. |
| R2 | one bulb of the top string still cut by the band's top edge at 1366 with «50% 40%» | **Apply «50% 35%»** and re-measure the sentence (expect ≥ 6.65:1). | Measured on band-d.png rows 0–5. |
| R3 | the day frame's second and third heads cut at the top edge at 1366 with «50% 40%» while the night frame («50% 30%») shows every head | **Apply «50% 30%» on the day frame too** (not the reviewer's 35%: at 16:10 the overflow is 232 px, 30% gives the second disc ≈ 23 px of sky and the nearest crown ≈ 50 px); re-measure the day headline at d. | Same value on both frames; the pavement under the headline moves ≈ 23 px, contrast re-measured. |
| R4 | at 360/390 the on-frame words (28 px) outrank the section heading (clamp floor 25 px) | **Accept.** | The heading leads by position and colour; the words are the section's payload; the SPEC set both numbers and the neighbours share the clamp. |
