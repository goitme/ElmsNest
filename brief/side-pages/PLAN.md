# Side pages — plan of record (2026-09-02, after the inventory)

Read after `HANDOFF.md`. Inputs: `brief/inventory/INVENTORY.md` (merged inventory, 20 owner questions),
`brief/inventory/AUDIT-*.md` (per-family visual audits from real JS-enabled renders), `brief/inventory/THEME-SRC.md`
(what every template/section is), `brief/side-pages/OWNER-NOTES.md` (owner directives, verbatim).
Nothing in this plan is built yet. Nothing is published. The homepage verdict is still pending.

## 0. What the inventory established (the facts that shape the order)

1. **Every side page is off-system.** All 30 mirrored side pages have `env2 base loaded: False`, the old cream/brown
   `scheme-1`, Assistant, boxes, and end in a hard cream→black cut into the night footer. The homepage is the only
   page on the design system.
2. **The header is unreadable on every side page.** `header_transparent: true` + `scheme-env2-night` + opacity 0 puts
   ink `#f4eee3` menu text on cream: menu, search and hamburger are invisible until the sticky bar appears on scroll-up.
   This is a site-level decision (dark ground under every template), not a per-page fix.
3. **The product page already had a pass ("PDP Design v2")** — ten `elms-pdp-*` sections, ~9.5k px, the same ~5,000 px
   of template copy on every product, solar-only copy on wired lamps, a comparison table against "מנורה גנרית זולה",
   a variant picker that never shows a price, and empty data blocks (spec/not-fit/FAQ metafields exist on 1 of 27).
   Its copy assets (`.elms-sales` description HTML on all 27 products, the licensed terms wording) are worth keeping;
   its composition and palette are not on-system.
4. **The catalogue is small and variant-heavy**: 27 products, 172 variants, 8 single-variant, four products with 16–30
   variants (length × colour matrices). 19 of 27 cards show a price range. Roughly two-thirds of `images[0]` are AI
   creatives with baked-in Hebrew claims (WINNING-SPEC §3.6 has the usable-index ledger and the never-use list).
5. **Kalles is a JS organism where it matters**: variant picker → price → gallery → sticky ATC → cart drawer; facets
   drawer; quick-add popup. New sections either keep those DOM contracts or rebuild the stack. The cart drawer is
   JS-injected, cream, and opens on every add-to-cart on every page.
6. **Honesty is already met by absence** (no ratings, counts, countdowns rendered), except: the PDP comparison table,
   the "-25%" badge + struck price on one product, "הנמכרים ביותר / פופולריות" sort entries, sr-only "מחיר מבצע" on
   regular prices, the fake blog, and the baked-in numeric claims in `images[0]`. Full ledger: INVENTORY §3.
7. **Tooling learned**: `file://` renders of Kalles pages hide every product grid (importmap never loaded). Use
   `brief/mirror.py` (now fetches the importmap) + `brief/shot-http.js` (serves the mirror on 127.0.0.1) —
   `brief/inventory/shot-all-http.sh` does all pages. The cart drawer, quick-add and facets still need an interactive
   Playwright session over the same server.

## 1. Owner directive that reorders the work

> اهم شيء في صفحة المنتج ان يكون هناك تسويق قوي بيع قوي … ليس صفحة بصرية فقط

The PDP is judged first as a selling page. So: (a) the PDP is the first page designed after the shared core, not the
collection; (b) its brief opens with a **persuasion spine** (§4) that every concept must implement; (c) its judging
panel gets a conversion judge with the heaviest weight; (d) the owner sees the five PDP concepts and the judges'
ruling before anything is built (an extra checkpoint only for this page).

## 2. Order of work (recommendation)

| # | Round | Why here | Reuses / produces |
|---|---|---|---|
| 0 | **Shared core** (engineering + one critique, no concept panel) | Nothing can be judged from a real render until the ground, header, type and cart drawer are on-system. | Produces `snippets/elmsnest-v2-core` (global) + index-only gradient split; per-template ground; Kalles bands removed; drawer scheme; back-to-top; Heebo for Kalles chrome; `--en-*` retargeted; sort/badge/sr-only fixes; `lint.py` per template. |
| 1 | **Product page** | Owner priority; where the money is; the hardest stack (variants, sticky ATC, gallery). | Produces the buy box, the variant/price ledger device, the suits/doesn't-suit device at product level, the "related" card → reused as the catalogue card. |
| 2 | **Collection** (+ `/collections/all`; decide `list-collections`) | The funnel entry from the homepage's four places; inherits the card from round 1. | Produces the browse composition, sort/filters decision, empty state, the ground rule for long pages. |
| 3 | **Cart drawer + cart page** | "The lamp goes into the basket" — the moment after every ATC; needs the interactive harness. | Drawer primary, page as fallback (pending Q15). Terms strip reused from the homepage ledger. |
| 4 | **Search (hits / none / blank) + 404** | Small; reuse the card; the 404 and zero-results get one device each (a lamp that did not light + the four places). | — |
| 5 | **Content pages** (guide, why-solar, about, faq, shipping, processing, contact) | One editorial family, one idea, per-page variation; contact depends on the WhatsApp answer (Q1). | Replaces the 37 KB hard-coded switch with per-page JSON templates + sections. |
| 6 | **Policies, password, customers** | Policies are locked markup (type + hairlines from `theme.liquid`); password matters while the plan is "Pause and Build"; customers only if Q9 says they are ours. | — |

Rounds 1 and 2 can overlap: the PDP concept panel starts while round 0 is being engineered (mockups are offline).

## 3. The process, per page (unchanged from the homepage, with two additions)

1. **Brief** (`brief/side-pages/<page>/BRIEF.md`): store facts for this template, data that exists (from INVENTORY §4),
   the design system (WINNING-SPEC §3 + CONTRACT), hard constraints (Kalles contracts, no-JS, RTL), the bar, the
   do-not list, the image ledger for this page. For the PDP: the persuasion spine (§4) first.
2. **Concept panel**: 5 designers, each forced to a radically different seed, each producing a complete offline HTML
   mockup with real products/prices/images/fonts (`brief/assets`), screenshotting (`brief/shot.js`) and self-critiquing
   from the PNGs. Renders are judged, never text.
3. **Judges**: creative director · Israeli mobile shopper/conversion · brand + Liquid feasibility. **PDP addition:** a
   conversion strategist who scores the persuasion spine step by step (weight 40 % of the total) and a Hebrew
   copy chief for the buy-box words. Then a lead synthesises the build spec (grafts from non-winners, image ledger,
   copy, schema, do-not list).
4. **Owner checkpoint (PDP only):** the five concept screenshots + the ruling, before build.
5. **Build**: shared plumbing first, one engineer per section, offline preview + `lint.py`, integrator reconciles
   schema ↔ template JSON, deploys to the dev theme (`brief/DEPLOY.md`), mirrors with `mirror.py`, shoots with
   `shot-http.js`.
6. **Adversarial critique**: creative director · Hebrew mobile shopper (executes the buy flow on the http-served
   mirror: variant → price → ATC → drawer) · Hebrew typographer · front-end QA (touch/keyboard/reduced-motion/no-JS).
   Triage → per-file fix packages → fix → redeploy → verify on a fresh mirror.
7. **Lead looks personally**, then the owner judges. Nothing is published without an explicit "publish".

## 4. PDP persuasion spine (the brief's first section; the owner's directive made concrete)

The page answers the buyer's questions in the order they arise, each with a device, each honest by construction:

| # | Buyer's question | Device on the page | Honest source |
|---|---|---|---|
| 1 | What is this, and is it for *my* place? | First screen: the lamp lit in its place (night photo), the place kicker (שביל/קיר/גינה/מרפסת) with the approved "מתאים כדי" phrase, price, buy. | `product.type`/collection, BRIEF §3 pairs |
| 2 | Will it work where I want to put it? | The suits / doesn't-suit device at product level (the homepage divider, or a place picker) — the *one* negative from the approved four, never a new one. | BRIEF §3, `custom.not_fit_for` when filled |
| 3 | What does it look like at night, really? | Night gallery that lights on arrival; a scale cue (height in cm, spacing between units). | `images[1..]`, description bullets |
| 4 | What exactly do I get, and what does the long one cost? | Variant ledger: each length/quantity with its own price and per-unit price; sets (2/4/6) as coverage ("שביל של 6 מטר = 4 יחידות"). | `product.variants`, `unit_price` |
| 5 | What could go wrong? | The facts that lower risk, stated plainly: power source, IP rating, hours after a full charge, winter note for solar; what is *not* known is not claimed. | description spec bullets, metafields (Q17) |
| 6 | What happens after I order? | The four numbers (0 ₪ pickup / 29.90 door · 8–17 days · 14-day cancellation · photo check) — the homepage ledger, compact. | policies, `elmsnest-pdp-trust` wording |
| 7 | Why buy here and not on a marketplace? | Not a comparison table: the specialist's promise as a device — "we tell you when not", Hebrew spec, a human to ask before ordering (WhatsApp when Q1 is answered). | «מי אנחנו» |
| 8 | Can I do something smaller than buying? | The low-commitment step: send a photo of the place; or add the single unit and decide the set later. | WhatsApp / contact |

Rules: no fabricated proof (reviews, counts, urgency), no comparison claims about others, no solar copy on wired
products (a power-source branch in Liquid), no typed facts (numbers from variants/metafields/description only).

## 5. Shared core — engineering spec outline (round 0)

- Split `snippets/elmsnest-v2-base.liquid` → `elmsnest-v2-core` (tokens, fonts, `.env2-*` helpers, `[data-lamp]`,
  `window.env2`, `html.env2-js`, reduced motion, back-to-top hide, footer type) rendered from `layout/theme.liquid`
  on every template; `elmsnest-v2-ground-index` (the dusk gradient) stays with the hero.
- Ground per template (decided in the PDP concept round, applied to all): a shorter sky (sky-2 → sky-4) or a flat
  sky-3 with stars — the same hairline/scrim vocabulary; Kalles `#wrapper/main` transparent on every `hdt-page-type-*`.
- Header stays as configured (transparent, night scheme) because every first section becomes dark; the first section
  of each template carries `section-allow-transparent hdt-section`.
- Remove `main-heading` and `top-list-collections` from collection/search/cart/list-collections/page/contact/customers
  templates (they are the cream bands + duplicate h1s).
- `system-group.json`: cart drawer → `scheme-env2-night`; back-to-top hidden.
- `settings_data.json` (minimal edit): drop the "best selling / popularity" sort labels where possible, badge policy
  per Q4/Q16, cart drawer strings in Hebrew.
- `snippets/css-variables.liquid` `--en-*` → env2 values (interim for the old custom sections until they are replaced).
- `brief/lint.py`: glob every template JSON we own; check `section-allow-transparent` on first sections.

## 6. Owner questions (full list: INVENTORY.md §5). The ones that block round 0–1

Q1 WhatsApp number · Q5 PDP v2 = base to restyle or replace (recommendation: replace the composition, keep the copy
assets) · Q6 baked-text images: regenerate or lock indexes 1–3 · Q17 fill spec/not-fit/FAQ metafields for 26 products
(recommendation: we extract them from the description bullets into a sheet the owner approves) · Q4/Q16 sale +
reference price · Q7 filters/sort (recommendation: no toolbar for 27 products; place links + price order) ·
Q13/Q14 canonical collection names and the taxonomy oddities · Q15 drawer vs page (recommendation: drawer) ·
Q20 homepage verdict, hero master, lockup (still pending from the homepage round).
Recommendations to close without design: Q8 retire the blog URL; Q9 accounts stay Shopify-hosted; Q10 publish the
accessibility statement; Q11/Q12 Hebrew policy titles + real business details; Q19 delete the Kalles demo templates.
