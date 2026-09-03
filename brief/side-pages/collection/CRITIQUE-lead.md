# Collection page — the design lead's own verification (2026-09-03)

**Why this file exists.** The four adversarial critics (creative director, mobile shopper, Hebrew typographer,
front-end QA) could not run: three attempts returned API 500 and then 529 Overloaded from the model service, once
with the four in parallel and once strictly sequential, so the cause is service capacity and not our workflow.
The adversarial round for this page is therefore **still owed**. What follows is what I verified myself on the
deployed dev-theme render — it is a floor, not a substitute.

## What I checked, and how

| Check | Method | Result |
|---|---|---|
| First screen carries place + product + price + a route to buy, on all five URLs, both viewports | read the fold PNGs; the integrator's measured buy-bottom values (790/814 px desktop, 672–741 px mobile against 844) | **pass** — this is the audit's worst defect (four of five URLs had no price and no product in the fold) and it is closed |
| One real `<h1>` per URL, not an `sr-only` SEO string | grep `<h1` and `sr-only` on all five mirrors | **pass** — 1 h1, 0 sr-only |
| No sale devices | grep for `-N%`, `%N-`, `<s>`, `line-through`, `compare_at` inside our sections on all five | **pass** — the five "percent" hits per page were URL-encoded Hebrew handles (`%D7%90…`), not badges |
| No fabricated proof | grep for stars, ratings, "best selling", "פופולריות", "נמכר ביותר" | **pass** — 0 on every URL |
| No WhatsApp claim while the number is empty | grep `בוואטסאפ` | **pass** — 0 |
| No cream/brown surface | grep `#f7f0e6`, `#fffdf7`, `#2b2118` inside our sections | **pass** — 0 |
| `<bdi>` discipline on prices and measures | 191 `<bdi>` on the decor page; sampled every price form | **pass** — `<bdi>89.90</bdi> ₪`, `<bdi>89.90–469.90</bdi> ₪`, and the `≈` correctly **inside** the bdi (`<bdi>≈17.98</bdi> ₪`) so RTL does not throw it to the far edge |
| The narrowing device has an accessible name and real controls | inspected the markup | **pass** — `role="group"` + `aria-label="כמה מטרים צריך להאיר?"` around seven native `<input type="radio">` with seven `<label>`s and per-stop `aria-label`s. `role="radiogroup"` would be more precise ARIA but is wrong here: with native radios the browser already forms the group, and `radiogroup` would oblige us to manage `aria-checked` on `role="radio"` children. Not a defect. |
| No horizontal overflow at 390 and 320 | Playwright measurement on the served mirror | **pass** — `scrollWidth === clientWidth` at both; the only elements crossing the viewport edge are `env2-pool`, the decorative blurred glow layers, clipped by their container |
| The pinned-lamp tag is not flush to the screen edge | I suspected it was, from the screenshot; measured it | **my suspicion was wrong** — 18 px gap at both 390 and 320 |
| Counts and spans are computed, not typed | compared every fold against `data.json` | **pass** on all five |
| The narrowing works with JavaScript disabled | the integrator's `javaScriptEnabled:false` run (the `html` class never gained `env2-js`): at 10 מ׳ rope 12 מ׳/99.90, crystal 11 מ׳/109.90, globe 10 מ׳/169.90, Edison dimmed printing "האורך המרבי: 8 מ׳" | **pass** — the device is pure CSS `:checked`, state in the URL |
| The product page did not change | the integrator's PIL diff of the related row and the whole page | **pass** — MAD 0.000000, 0 of 48,913,920 pixels |
| The glyph plate reads as a choice, not a missing image | read the spot page fold, where six of six products use it | **pass** — an outlined lamp in a glow with «איור · אין תצלום נקי» beneath. Honest, and it does not pretend to be a photograph. It still sells worse than a photograph would (see §Owner). |

## Rulings I owe as the lead

1. **`coll-wall` ships five sections, not the six §5.1 names — this is correct, and the spec is amended.**
   The measure ledger ranks products along one shared unit. Every wall lamp is priced by wattage and colour
   temperature, not by metres or points of light, so a ledger there would have had to invent a ranking. A section
   that gates itself off when its data does not exist is the honesty rule working, not a gap. `WINNING-SPEC.md`
   §5.1's headline count is amended: wall ships five, spot and decor six, path seven, all six.
2. **The spot collection's h1 orphan.** "ספוטים, פרוז׳קטורים ותאורה ניידת" breaks to three lines at 1440 and leaves
   "ניידת" alone in glow on the third. It reads deliberately enough that I am not spending a fix on it before the
   typographer has seen it; it goes to the critics' list.

## What is genuinely good (do not break it in the fix round)

1. The first screen. On five URLs and two viewports it does the three things at once — where you are, a lit lamp
   pinned in the place it would stand, and a real price with a route to buy.
2. The ruler as pure CSS. The one device this page exists for works with scripts disabled, and the garland that
   cannot reach ten metres dims and says so instead of vanishing.
3. The glyph plate. Fifteen products have no clean photograph; the page says so in Hebrew rather than shipping a
   marketing poster with baked-in claims.

## Still owed

The adversarial round: four lenses on the deployed render, the shopper executing the purchase on a phone, the QA
engineer testing keyboard, reduced motion and 320 px, the typographer reading every mixed-direction number, and the
creative director trying to prove the page is not world-class. Re-run `brief/side-pages/workflows/collection-critique.js`
when the model service recovers. Until then this page is **verified, not critiqued**.

---

## The shopper journey, executed (added after the critics failed a third time)

The four critic agents failed on three attempts (500, then 529 twice, parallel and sequential), so I drove the
purchase myself with Playwright on the served `coll-decor` mirror at 390×844, with and without JavaScript.
Screenshots: `brief/side-pages/collection/shopper/decor-6m-js{true,false}.png`.

**The task:** I want string lights for a six-metre pergola. Seven garlands, 105 variants, prices 89.90–469.90.

| Step | What happened | Verdict |
|---|---|---|
| Land | The fold gives the place, one lit garland pinned in the photograph, `מ־89.90 ₪`, `≈17.98 ₪ למטר` and `לבחירת אורך` | pass |
| Find the instrument | The ruler's first pixel is at **943 px — 1.12 screens down**. I had to scroll past a full screen to reach the one device this page exists for | **LEAD-01, major** |
| Choose 6 מ׳ | Every row collapsed from a range to one real answer: crystal `6.5 מ׳ · 89.90 ₪ · ≈13.83 ₪/מ׳`, globe `6 מ׳ · 119.90 ₪ · ≈19.98`, rope `7 מ׳ · 89.90 ₪ · ≈12.84`, Edison `8 מ׳ · 179.90 ₪ · ≈22.49` | pass — and this is the best conversion device in the whole project: four comparable offers, and the cheapest per metre is visible without arithmetic |
| Same with JavaScript disabled | **Byte-identical output.** The stop is a label over a native radio and the narrowing is pure CSS `:checked` | pass |
| Reach a product | Every row's title is a 50 px link to the product page and carries a 45 px `לבחירת אורך`; the stops are 48 px | pass — above the 44 px floor |
| The three garlands not measured in metres | fireflies, birch and the net are **not dropped** — they appear elsewhere on the page (2, 3 and 3 links respectively) rather than being forced onto a metre rail | pass |

### LEAD-01 · major · `elmsnest-v2-coll-scene` + `-ruler`

**What.** The narrowing device sits 943 px down on a phone — 1.12 screens. `BRIEF.md` §6 sets the bar as: within
the first screen on a phone the visitor must see the place, a real product with a real price, **and a way to narrow
the set**. The first two are there; the third is one full scroll away, so the page's own instrument is invisible at
the moment of arrival.

**Evidence.** Measured `getBoundingClientRect().top + scrollY` on `#env2-coll-ruler` at 390×844 = 943 px.

**Fix (one iteration, no redesign).** Put the question in the scene, not just the section: a single hairline line
under the counts reading `כמה מטרים צריך להאיר?` followed by the six stop values as anchors to `#env2-coll-ruler`
(they are already `<a>`-able ids). It costs about 60 px in the fold, it uses copy that already exists, and it makes
the instrument discoverable without moving the ruler above the bands — which would cost the page its opening
photograph, the reason this concept won.

## Corrected verdict

The page is **verified and now partly critiqued**: the buy path, the narrowing device, the no-JS contract, the
honesty rules, the RTL numerals and the tap targets are measured and sound; one major finding (LEAD-01) is open;
the creative, typographic and full-QA lenses are still owed and must run when the model service recovers.

## LEAD-01 — CLOSED (deployed 2026-09-03 20:01 UTC)

**The fix.** One hairline row in `elmsnest-v2-coll-scene`, between the counts and the product card:
the question in ink, then `לסרגל המידה ←` in gold, anchored to `#env2-coll-ruler`. Two new schema settings
(`narrow_label`, `narrow_link_label`) so a merchant can reword it.

**Why the wording is unit-neutral (`כמה אור צריך המקום?`) and not the ruler's own question.** The ruler resolves
its unit from the data — length, count or price — in about a hundred lines that walk every product in the
collection. Printing "כמה מטרים צריך להאיר?" in the scene would mean either duplicating that resolution (two
sources, and the fold starts lying the day a collection's unit changes) or refactoring the ruler to publish it
(a hundred working lines touched across five URLs, for one line of copy). A question that is true whether the
rail measures metres, points of light or shekels is correct by construction on all five URLs including
`/collections/all`, where the ruler is a table of contents and no unit applies. The `info` string in the schema
records the reason so the next engineer does not "improve" it into a lie.

**Verified on the deployed render** (Playwright, served mirror, 390×844):

| | coll-decor | coll-all |
|---|---|---|
| row top (page coords) | 515.3 | 515.3 |
| row height | **44.0** (the floor exactly) | 44.0 |
| inside the 844 px fold | **yes**, bottom 559.3 | yes |
| clear space to the card | 14 px | 14 px |
| buy control | 672.8–717.6, still inside the fold | inside |
| `#env2-coll-ruler` top | **943.4 — unchanged** | 735.6 |
| click → ruler in view | scrollY 0→853, ruler at y=90 | 0→646, y=90 |
| horizontal overflow @390 / @320 | none / none | none / none |
| `Liquid error` | 0 | 0 |

**The row costs nothing.** The ruler did not move: the scene's mobile type block is a flex column with
`justify-content:flex-end`, so the new row consumed existing slack instead of pushing the page taller.
Deploy verified by checksum, not by length — `checksumMd5 0ea1f284b2befc8dcea5db70d3acf1e0` equals the md5 of
the local file, so the live section is byte-identical to the repo copy. (The byte count I gave the deploying
engineer was stale; it caught that and verified harder instead of trusting my number.)
