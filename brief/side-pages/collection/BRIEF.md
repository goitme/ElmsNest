# ElmsNest collection page — creative brief (round 2, 2026-09-03)

Read in this order: this file · `brief/side-pages/PLAN.md` §2 · `brief/WINNING-SPEC.md` §3 (the design system — binding)
· `brief/build-preview/CONTRACT.md` · `brief/side-pages/pdp/WINNING-SPEC.md` §3.5–§3.6 and §4.8 (the image ledger, the
option-axis rule and the product card that already exists) · `brief/inventory/AUDIT-collection.md` (what you are
replacing, with measurements) · `brief/inventory/INVENTORY.md` §4 (data) · `brief/side-pages/OWNER-NOTES.md` (owner
decisions) · `brief/side-pages/core/REPORT.md` §9 (known core bugs — do not inherit them).
Data pack: `brief/side-pages/collection/data.json`. Look at the real renders: the finished product page
(`brief/inventory/pdp-multi/http-desktop.png`, `http-mobile-fold.png`) and the homepage
(`brief/inventory/home/http-desktop.png`) — the level and the system. And at `brief/inventory/coll-all/http-desktop.png`
— the Kalles catalogue page you are replacing (it is now night-grounded by round 0, but the composition is untouched).

## 1. The job

The collection page is the **path from the homepage's four places to a product**. The homepage says "four places, one
category" and sends the visitor here; the product page then sells. This page's only job is to make the right lamp
findable and desirable in a store with **27 products** — a number small enough that a supermarket toolbar is an insult
and large enough that a single undifferentiated grid is boring.

Five URLs must work: the four real collections and `/collections/all`.

| handle | title | products | variants | price span |
|---|---|---|---|---|
| `תאורת-שביל-סולארית` | תאורת שביל, עמוד וגינה | 8 | 22 | 69.90–999.90 |
| `solar-wall-lights` | תאורת קיר | 6 | 34 | 99.90–252.90 |
| `ספוטים-ופרוז-קטורים-סולאריים` | ספוטים, פרוז׳קטורים ותאורה ניידת | 6 | 11 | 99.90–499.90 |
| `גרילנדות-ותאורה-דקורטיבית` | גרילנדות ותאורה דקורטיבית | 7 | 105 | 89.90–469.90 |
| `all` | קטלוג | 27 | 172 | 69.90–999.90 |

## 2. Owner decisions that bound this round (`OWNER-NOTES.md`)

- **No sales exist.** No badge, no strikethrough, no "-N%", no `/collections/sale` link anywhere. The one compare-at
  price in the catalogue must not render as a discount.
- **No toolbar** (the owner accepted the recommendation): the only facets Shopify holds are availability and price,
  there is no wattage / IP / zone / power-source data, and "best selling" and "popularity" imply sales rank the store
  cannot support. Replace the toolbar with something that actually helps in a 27-product store — but *some* ordering
  must exist (price, at least) and it must work server-side without JS (`?sort_by=price-ascending`).
- **The image ledger is locked**: never render `images[0]` of the products on the never-use list
  (`brief/WINNING-SPEC.md` §3.6) — roughly 15 of 27 carry baked-in Hebrew marketing text; one carries a third-party
  "LUMIÈRE" mark. `snippets/elmsnest-v2-pdp-image.liquid` already resolves this per product and per slot.
- **No WhatsApp number**: the photo-check step is a `mailto:` via `snippets/elmsnest-v2-pdp-photo-cta.liquid`.
  Never write "בוואטסאפ".
- **Honesty**: no ratings, no review counts, no "trusted by", no urgency, no invented facts. The four approved
  suits/doesn't-suit pairs (`brief/BRIEF.md` §3) are the only negatives that may appear anywhere.

## 3. What already exists and must be reused, not redesigned

- **The product card**: `snippets/elmsnest-v2-pdp-card.liquid`, designed and shipped inside the product page
  (`pdp/WINNING-SPEC.md` §4.8). Image via the resolver, place kicker, title in Heebo, price by the
  `elmsnest-v2-price` rule (single / `min–max` / `מ־`), single-variant → an add-to-cart form, multi → a link. No badge,
  no swatch dots, no quick-add icon, no stars. **Extend it if the concept needs a variant (a wider card, a caption, a
  per-unit line) — do not fork it**; whatever you change must still render correctly on the product page's related row.
- **The shared core**: `snippets/elmsnest-v2-core.liquid` is rendered on every template and already provides the
  tokens, Frank Ruhl Libre + Heebo, `.env2-*` helpers, `[data-lamp]`, `window.env2`, the pill buttons and the night
  ground. The header is legible on every side page (round 0). Do not re-render it, do not redefine its tokens.
- **The PDP ground** pattern: `snippets/elmsnest-v2-ground-product.liquid` shows how a template gets its own gradient
  scoped to its `body.hdt-page-type-*`. The collection needs its own (`-ground-collection`), and its ground must work
  for a page that can be 1 screen (6 products) or 4 screens (27, paginated).
- **The buy plumbing**: `elmsnest-v2-buy`, `elmsnest-v2-price`, `elmsnest-v2-bdi-range`, and the core's
  `form[data-env2-buy]` handler that adds to cart and opens the night drawer.

## 4. What is wrong with the page today (from the audit — do not repeat)

1. The first screen of the four real collections shows **no price and no product** — a banner, a paragraph and a
   toolbar; only the tops of two photos. On `/collections/all` products do reach the fold.
2. Four equal cards in a row, four times: the exact shape the owner rejected on the homepage.
3. The `<h1>` is the SEO string ("… | ElmsNest") and it is `sr-only`; the visible title is a 32 px `div`.
4. `collection.description` — two honest, specific paragraphs per collection — is printed as a grey slab and then
   contradicted: it says "choose by light output / installation area / beam angle" and the page offers no such choice.
5. Nothing lights. No lamp device, no motion that means anything.
6. The consumer terms appear on none of the five pages.
7. The 12-per-page pagination on `/collections/all` breaks the catalogue into three arbitrary pages.

## 5. The data you may use (all real, all in `data.json`)

- `collection.title`, `collection.description` (two paragraphs, quoted in the audit), `collection.image`
  (four clean night photographs; the wall one is landscape 1456×816 and needs a deliberate crop).
- Per product: title, price range, variant count, **the first option axis with its price per value** (this is what
  makes "מ־89.90" honest and what a length/quantity/wattage caption can be built from), `productType`,
  `custom.home_card_line` on 12 of 27 (a one-line merchant description), and the description's first sentences.
- Counts: `collection.products_count`, `collections.all.products_count` — always from Liquid, never typed.
- The four places and their approved "suits" phrases (`brief/BRIEF.md` §3) — the vocabulary that ties this page to the
  homepage and the product page.

## 6. The bar

A visitor arriving from the homepage's "ארבעה מקומות" must, **within the first screen on a phone**, see: which place
they are in, at least one real product with a real price, and a way to narrow 6–27 lamps to the two or three that suit
them. Then:

- **One idea only a lighting store could have.** Browsing lamps is browsing *light*: how much of it, what colour,
  how far it reaches, what it is for. The catalogue's own axes (metres, units, watts, Kelvin, beam) are richer than
  any generic filter — a concept that uses them beats a concept that decorates a grid.
- **Every screen composed differently.** If the page is one grid scrolled four times, it is wrong. Scale contrast:
  something enormous next to something small.
- **The place, not the SKU, is the organising idea.** The store sells by place; the collection page should too.
- **Editorial Hebrew type**, the sky ground, hairlines instead of boxes, lamps that light on arrival, radius 0 except
  pills — the system of `brief/WINNING-SPEC.md` §3, no exceptions.
- **It must sell**: price and a route to buy on every card; the single-variant products (8 of 27) can be added to the
  cart from this page; the terms strip is reachable.
- **It must be honest**: real counts, real ranges, no badge, no invented claim.

## 7. Hard constraints

- Kalles' `main-collection.liquid` is an 85 KB JS organism (facets drawer re-rendered by AJAX, grid-density selector,
  reveal-on-scroll). The build will **replace it** with our own section, exactly as the product page replaced
  `main-product`. That means re-implementing, in Liquid: `paginate collection.products by N`, server-side `?sort_by=`
  (plain links, no JS), the description, and the pagination control. Everything must work with JS disabled.
- `templates/collection.json` is the file to write (there is no per-collection template suffix in use).
- `/collections/all` must not feel like a different page from a real collection — but it may be composed differently
  (it is the whole catalogue, not one place).
- RTL: logical properties only. Latin tokens and prices in `<bdi>`. Radius 0 except pills. No Liquid inside
  `{% stylesheet %}` / `{% javascript %}`. Schema `name` max 25 chars. No `"""` in any file.
- Mobile first screen is 390×844 and the sticky header is 60 px.

## 8. Deliverables per designer (offline mockups, judged from the renders)

`brief/side-pages/collection/concepts/<key>/index.html` — **`/collections/גרילנדות-ותאורה-דקורטיבית`** (7 products,
105 variants — the hardest: every product is a range), complete page, desktop + mobile, RTL, real titles/prices/images
from `data.json`, local assets (`brief/assets/img/<handle>-<i>.jpg`, `brief/assets/fonts.css`), vanilla JS only,
lamps on arrival, works with JS off.
`.../path.html` — **`/collections/תאורת-שביל-סולארית`** (8 products, the widest price span 69.90–999.90): the same
system proving it holds when one product costs fourteen times another.
`.../all.html` — **`/collections/all`** (27 products): the first screen and the first ~2 screens at minimum — how the
whole catalogue is composed and how pagination or its replacement works.
Screenshot each with `node brief/shot.js <file> <prefix>`; **read your own PNGs** and fix what they show.
`.../CRITIQUE.md` — the one idea in a sentence; how a visitor narrows 7 / 8 / 27 lamps to a choice; where it sells
hardest and weakest; what you would fix with one more day.

## 9. Judging (from the screenshots first)

| Criterion | Weight |
|---|---|
| **Findability + selling** — place clear, product and price in the fold, a real way to narrow the set, a route to buy, works on a phone | 35 |
| One idea only a lighting store could have, visible in a still | 20 |
| Composition: every screen different, scale contrast, no four-equal-boxes, no toolbar | 15 |
| Typography and RTL craft | 10 |
| Honesty + system fidelity (same store as the homepage and the PDP) | 10 |
| Feasibility: Liquid + `paginate` + server-side sort, no-JS path, reuses the card | 10 |
