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
