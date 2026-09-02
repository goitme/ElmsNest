# ElmsNest product page (PDP) — creative brief (round 1, 2026-09-02)

Read everything here, then: `HANDOFF.md` §1–§3, `brief/WINNING-SPEC.md` §3 (the design system — binding), `brief/build-preview/CONTRACT.md`,
`brief/inventory/AUDIT-product.md` (what the current PDP does and why it fails), `brief/inventory/INVENTORY.md` §4 (data facts),
`brief/side-pages/OWNER-NOTES.md` (owner decisions), `brief/side-pages/PLAN.md` §4, and the data pack `brief/side-pages/pdp/products.json`.
Look at the homepage renders (`brief/inventory/home/http-desktop.png`, `http-mobile.png`) — that is the level and the system every
concept must belong to. Look at `brief/inventory/pdp-single/http-desktop.png` — that is the current PDP the owner has decided to REPLACE.

## 1. The owner's directive (verbatim) and what it means

> اهم شيء في صفحة المنتج ان يكون هناك تسويق قوي بيع قوي يعني نعرف كيف ندخل راس الزبون و نجعله يشتري ليس صفحة بصرية فقط

"The most important thing on the product page is strong marketing, strong selling — we know how to get into the customer's head and
make them buy; not just a visual page." The PDP is judged **first as a selling page**, then as a visual one. Selling here is not
pressure: the store's position (§3) forbids fake proof and urgency. Selling is: answering the buyer's hesitations before they are
spoken, in the order they arise, with specifics, and lowering the risk of saying yes. The conversion judge carries 40 % of the score.

## 2. What is being replaced, and why (do not repeat)

The current PDP ("PDP Design v2", `templates/product.elmsnest.json`): Kalles buy box (Assistant, cream, brown rectangles, a picker that
never shows a price) followed by ten sections of template copy identical on every product (~5,000 px), solar copy on wired lamps, a
comparison table against "מנורה גנרית זולה", a spec table that renders empty on 26 of 27 products, four-boxes-in-a-row twice, nothing
that lights. Owner: "استبدل" (replace). Keep only the copy assets: the owner-authored `.elms-sales` description of every product
(`products.json → description_text`, ~1,300 chars each, with a "פרטים שכדאי לדעת" bullet list) and the licensed consumer-terms wording.

## 3. Store facts and honesty rules (unchanged from the homepage brief; binding)

- elmsnest.com, Shopify (Kalles 5.4.2), Hebrew-only RTL, ₪, Israel. 27 products, 172 variants, 8 single-variant. One test order in
  history: **no reviews, no ratings, no "bought N times", no "trusted by", no countdowns, no "only N left", no "best seller"**.
- **Position:** the narrow specialist who also tells you what does NOT suit you. From «מי אנחנו»: *"כאשר מידע אינו מאומת, איננו
  צריכים להציג אותו כעובדה"*. The only negatives allowed on any page are the four approved pairs (place → suits / does not suit):
  - שביל, מדרגות ומעברים → לראות את הדרך / המקום כמעט אינו מקבל אור יום
  - כניסה, קיר וחזית → להאיר נקודה מסוימת / נדרש אור חזק וקבוע לאורך כל הלילה
  - מרפסת ופינת ישיבה → ליצור אווירה / צריך אור חזק — זו אינה מטרתה
  - הדגשת אזור בגינה → הארה ממוקדת של עץ או ערוגה / נדרשת התקנה מיוחדת או חיבור קבוע
  A product page uses the ONE pair of its place. Never write a new negative. The solar clause ("כמעט אינו מקבל אור יום") applies to
  solar products only.
- **No claims about competitors** (the comparison table is dead). No typed facts: every number comes from `products.json`
  (variants, prices, description bullets). What the description does not state is not stated.
- **Consumer terms, findable on the PDP:** free shipping to a pickup point (29.90 ₪ to the door); delivery 8–17 business days
  (1–3 handling + 7–14 shipping; may ship from warehouses outside Israel); cancellation within 14 days of receipt per חוק הגנת הצרכן,
  fee ≤ 5 % or 100 ₪ whichever is lower; "send a photo of the place, we check fit before you order".
- **No WhatsApp number exists yet.** The photo-check promise is real but its channel is email until the number is set:
  `mailto:info@elmsnest.com` with a prefilled subject. Never write "בוואטסאפ" on the page. Label the action "לשלוח תמונה של המקום".
- **No sales exist:** no badges, no strikethrough, no "-N%", no "מבצע".
- Latin tokens (`IP65`, `LED`, `6W`, `3000K`, `USB`) in `<bdi>`; prices `<bdi>169.90</bdi> ₪`.

## 4. The persuasion spine (mandatory; every concept renders all eight answers)

Default order = the order hesitations arise. A designer may reorder (e.g. put #6 next to the buy button) but must say why in the
self-critique. Each answer is a *device*, not a paragraph.

| # | The buyer is thinking | The page answers with | Honest source |
|---|---|---|---|
| 1 | "What is this — and is it for *my* place?" | Screen 1: the lamp lit in its place at night; the place word (שביל / קיר / גינה / מרפסת) + the approved "מתאים כדי …" phrase; the product title (Heebo); price; buy. | collection → pair; title |
| 2 | "Will it actually work where I want it?" | The suits / doesn't-suit device at product level — the homepage's divider idea or a place picker — showing the ONE approved negative for this place. Solar: "המקום כמעט אינו מקבל אור יום". | BRIEF pair; power source from description |
| 3 | "What does it really look like at night?" | Night gallery that lights on arrival (lamps); a scale cue (a person / a door / metres) and the spacing between units; the product's own light is the only light. | images (ledger §6) |
| 4 | "What exactly do I get, and what does the long / big one cost?" | The variant ledger: every length / quantity / wattage with its own price visible BEFORE selecting; per-unit or per-metre price; sets as coverage ("שביל של 6 מטר ≈ 4 יחידות" only if the description supports spacing — otherwise "כמה יחידות?" as a question with the set sizes). Colour/K options that do not change price are presented as a quiet second axis. | `products.json → variants` |
| 5 | "What could go wrong?" | The risk-lowering facts stated plainly: power source, IP rating, hours after a full charge, charging time, "לפני שימוש ראשון" note, winter note for solar; what is unknown is absent (no dimensions if the description has none). | description bullets |
| 6 | "What happens after I click?" | The four numbers (0 ₪ pickup / 29.90 door · 8–17 days · 14-day cancellation · photo check) as a compact ledger, within one screen of the buy button. | terms |
| 7 | "Why here and not a marketplace?" | Not a table: the specialist's promise as a device — "we tell you when not" (device #2 already did), spec in Hebrew, a human to ask before ordering. One quiet line, one link. | «מי אנחנו» |
| 8 | "Can I do something smaller than buying?" | The low-commitment step: send a photo of the place (email); or add one unit now, decide the set later (single unit is a variant on set products). | mailto |

The buy action must be reachable **inside the first screen on 390×844** (price + "הוספה לסל" or the variant selector that leads to it),
and answer #2 within the second screen. A sticky buy bar on mobile is expected (mirror of the selected variant + price).

## 5. The three archetypes every concept must handle (mock A fully; B and C as the first two screens)

| | A — `solar-crystal-ball-string-lights` | B — `stainless-steel-solar-path-light-ip65` | C — `waterproof-led-wall-light-ip65-6w-12w` |
|---|---|---|---|
| Place | מרפסת ופינת ישיבה (decor) | שביל, מדרגות ומעברים | כניסה, קיר וחזית |
| Variants | 24 = 6 lengths × 4 colours; price by length only: 5 מ׳/20 → 89.90 · 6.5/30 → 89.90 · 9.5/50 → 99.90 · 11/60 → 109.90 · 13/100 → 129.90 · 22/200 → 179.90 (verified from products.json; colour never changes the price); colours צהוב / כחול / צבעוני / לבן | 1 variant, 169.90 (option "צבע אור: צהוב חם" is a single value — never show a one-button picker) | 8 = לבן/שחור × 6W/12W × 3000K/6000K; price by W and K (219.90 / 222.90 / 249.90 / 252.90) |
| Power | solar (panel), 8 modes, IP65, ~8–10 h | solar, sensor auto on/off, IP65, ~6 h charge, ~8–10 h | **mains** (no solar copy!), IP65, 6W/12W, aluminium, indoor + outdoor |
| Description | 1,306 chars + 7 bullets | 1,366 chars + 7 bullets | 1,272 chars + 7 bullets |
| Sets / coverage | metres + bulbs per length | "הוסיפו את הכמות המתאימה לאורך הדרך" (quantity, not a set) | "בכניסה צרה יחידה אחת; חזית רחבה — סימטרי" |

The full copy for each is in `products.json` → `description_text` (use it; do not invent product facts; you may write new brand
headlines, kickers and micro-copy in the brand voice — short, specific, Hebrew).

## 6. Image ledger (local files `brief/assets/img/<handle>-<i>.jpg`; the Shopify product has 6 images, the local pack has 0–3)

| Product | Usable | Never (baked text) |
|---|---|---|
| A crystal | `-0` close-up bulbs (hero-grade), `-2` string on a wooden trellis (context) | `-1` (22 מטר / 200 LED slide), `-3` (installation infographic) |
| B path | `-0` three bollards on a brick path (hero), `-1` single bollard in bushes (dark, "lamp off" candidate), `-3` bollard by brick wall + steps | `-2` (dimensions slide) |
| C wall | `-1` black cube lit on plaster (hero), `-3` wide black wall light lit (hero alt), `-2` 4-up black/white pairs (colour axis, studio) | `-0` (slogan slide) |
| Header logo | `brief/assets/img/logo.png` | |
| Collection scenes (place context) | `brief/assets/img/collection-{path,wall,spot,decor}.jpg` | |

Any other product may be used for the "related" module (see §7) — obey WINNING-SPEC §3.6's never-use list (15 products whose `-0`
carries text; use their `-1..-3`).

## 7. What the concept must contain (so it can become the template)

1. Screen 1 (hero) with #1 and the buy action. 2. The variant/price ledger device (#4). 3. The place / not-for device (#2).
4. The night gallery (#3). 5. The facts (#5). 6. The four numbers (#6). 7. The specialist line (#7) and the small step (#8).
8. **A "related" module** (3–4 products of the same place) — design the product card here; it becomes the catalogue card in round 2:
   photo (ledger index), place kicker, title (Heebo), price by the rule (single / `min–max` / `מ־min`), no badges, no swatches, no
   quick-add icon; single-variant → "הוספה לסל", else → "לבחירת אורך / דגם".
9. The Kalles header (mock it as a static 70 px transparent strip: centred gold logo, menu דף הבית · קולקציות · מדריך לבחירה ·
   מי אנחנו · יצירת קשר, search + cart icons) and the night footer (mock as one dark block) — do not design them.
10. Mobile: the sticky buy bar; the ledger must not become 3–4 rows of rectangles; captions ≥ 13 px; tap targets ≥ 44 px.

## 8. Design system constraints (binding — WINNING-SPEC §3 + CONTRACT)

- **Ground:** sky, not cream. The PDP ground is yours to decide within the system: a shorter sky (sky-2 `#0f1a2f` → sky-4 `#020306`),
  or a photo ground for screen 1 fading into sky-3. Sections transparent; hairlines separate; the only card surface is the scrim.
  No brown, beige or cream anywhere.
- **Type:** Frank Ruhl Libre 500/700/900 for display lines; Heebo 300/400/500 for text; **product titles never in the serif**
  (the serif carries the editorial line, e.g. "המנורה לשביל שלכם."). Prices FRL 500 tabular in glow. Kickers 11–12 px tracked gold.
  Hebrew display leading .98, `text-wrap: balance`.
- **Colour:** ink `#f4eee3`, ink-2 `#c9c4b8`, mute `#8f95a3` (on sky-2 or darker only), gold `#e9b96e`, glow `#ffd394`, ember `#f7a24a`
  (halo cores only), hairline `rgba(244,238,227,.12)`, scrim `rgba(5,8,14,.55)` + blur.
- **Radius:** 0 everywhere except pill buttons (999px). No boxes, no rounded tiles, no card grids of equal cells.
- **Motion:** lamps light on arrival (`[data-lamp]`, once, never re-dim); exactly one thing switches on per section; the variant
  device may light the product (e.g. selecting a length lights more bulbs; 6W vs 12W changes the halo); no fade-in on text, no
  parallax, no autoplay; reduced motion = everything lit; no JS = everything lit and the single-variant form still posts.
- **Layout:** `.env2-wrap` = min(1240px, 100% − 2×gutter); full-bleed for screen 1 and the gallery; logical properties only;
  every screen composed differently; scale contrast (one enormous thing per screen).
- **Fonts offline:** `<link rel="stylesheet" href="../../../../assets/fonts.css">` (from `brief/side-pages/pdp/concepts/<key>/`).

## 9. Technical reality (the feasibility judge scores against this; designers should know it)

Kalles' buy stack is JS-bound (`hdt-variant-picker` → `hdt-price` → gallery → `hdt-sticky-btn-atc` → cart drawer, `form="product-form-…"`).
The build will either keep those contracts inside a restyled `main-product` or rebuild variant selection + price + ATC + sticky bar
in our own section with `product.variants` JSON and `/cart/add.js` (the base already opens the drawer). Either is possible; the
ledger device must be expressible as: a list of variants with prices from Liquid (no-JS shows the full ledger with per-variant
`/cart/add` forms), JS enhances to a selector. Images come from `product.images[i]` with a per-product index ledger (schema setting
or metafield). A power-source branch in Liquid (`custom.power_source` metafield, or a tag) gates every solar sentence.

## 10. The bar

The owner should feel: *"this page knows my customer's hesitations and answers them before they are asked — and it is unmistakably
the same store as the new homepage."* Concretely: buy inside screen 1 on a phone; the not-for answer inside screen 2; a variant
device that makes 24 choices feel like one decision; every screen composed differently; one idea only a lighting store could have;
editorial Hebrew type; motion that means something; nothing that could not be true.

## 11. Do-not list

No cream/beige/brown; no boxes or equal-card grids; no comparison table; no reviews/stars/counts/urgency; no typed facts; no solar copy
on C; no "בוואטסאפ"; no one-value picker; no price that hides the range; no product title in the serif; no emoji; no icon rows of
"free shipping / guarantee"; no marquee; nothing fixed bottom-left; no four of anything in a row; no lorem; no English UI strings.

## 12. Deliverables per designer

`brief/side-pages/pdp/concepts/<key>/index.html` — product A, complete page, desktop + mobile responsive, RTL, real copy from
`products.json`, local images/fonts, vanilla JS for the variant device and lamps (offline, no network).
`brief/side-pages/pdp/concepts/<key>/path.html` — product B, the first two screens (hero + not-for device) at minimum.
`brief/side-pages/pdp/concepts/<key>/wall.html` — product C, screen 1 + the variant ledger (8 variants, mains copy).
Screenshots: `node brief/shot.js <file> <prefix>` for each (desktop 1440 / mobile 390, full + fold).
`brief/side-pages/pdp/concepts/<key>/CRITIQUE.md` — self-critique from the PNGs: the one idea in one sentence; the spine, answer
by answer, with the screen it lands on; where the page sells hardest and where it is weakest; what you would fix with one more day.

## 13. Judging (from the screenshots; the text is read after the images)

| Criterion | Weight |
|---|---|
| **Sells** — spine answered in order, buy reachable, hesitation handling, variant decision made easy, risk lowered, small step offered | 40 |
| One idea only a lighting store could have; screen 1 states it | 15 |
| Composition: every screen different, scale contrast, full-bleed moments, no boxes | 15 |
| Typography: editorial Hebrew, hierarchy, `<bdi>` discipline, mobile legibility | 10 |
| Honesty + brand: the pair verbatim, no claims, terms findable, same store as the homepage | 10 |
| Feasibility: expressible in Liquid + vanilla JS with Kalles contracts or a clean rebuild; no-JS path | 10 |
