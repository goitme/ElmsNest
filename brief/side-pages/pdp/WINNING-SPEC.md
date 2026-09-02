# ElmsNest product page (PDP) v2 — WINNING SPEC (build-ready)

Winner: **`switch`** (`brief/side-pages/pdp/concepts/switch/`), with six grafts.
Binding parents: `brief/side-pages/pdp/BRIEF.md` · `brief/WINNING-SPEC.md` §3 (design system — inherited whole)
· `brief/build-preview/CONTRACT.md` (shared plumbing — inherited whole) · `brief/side-pages/OWNER-NOTES.md`
· `brief/inventory/AUDIT-product.md` · data: `brief/side-pages/pdp/products.json`, `metafields.json`, `METAFIELD-SHEET.md`.

Everything below is decided. Where this spec and a concept mock differ, this spec wins.

---

## 1. The one idea, and the ruling

### The idea

**The page is one stage the buyer operates.** Every choice she makes changes the product's own light in
front of her: a length lights that many bulbs along a real string while the price moves; watts and Kelvin
resize and recolour the halo on the wall; quantity draws more bollards receding down the path. And the same
stage **goes dark** when she flips it to the one thing this lamp is not for. The store's position — "we also
tell you when not" — stops being a sentence and becomes a mechanism: the lamp refuses to light.

The selling logic follows from it. A 24-variant matrix is not a picker, it is a **ledger of six lit rows** —
metres, bulbs, ₪, ≈₪ per metre, and *what that length is for* — every price visible before you choose,
every row its own add-to-cart. The buyer decides in ten seconds and the page never hides the range.

### Why this concept

I opened all sixty renders before reading a judge. Three things settle it:

1. **The phone fold.** `switch/shot-mobile-fold.png` is the only screen 1 of the five that carries, above
   844 px: a night photograph *of the actual product*, the place kicker with the approved «מתאים כדי ליצור
   אווירה», an editorial h1, the Heebo product title, the colour axis, `89.90 ₪`, `הוספה לסל`, the four
   consumer terms in one line, the photo-check link, **and** a six-stop rail with all six prices. `place`
   bottoms its button out at ~808 of 844 px; `walk` offers no add-to-cart at all on A and C; `ledger` opens
   on a spreadsheet with no photograph anywhere in screen 1; `dialogue` is complete but stops at the price —
   its ledger is a scroll and a link away. The owner's directive is a selling page. This is the selling fold.
2. **The device survives a still.** `switch/shot-path-desktop-fold.png` draws additional bollards receding
   down the real brick path as quantity rises, each stop carrying its running total (169.90 → 1,359.20 ₪).
   Nobody else answered "how many units" with anything but a number. And slice 2 of the desktop capture flips
   the approved pair from `ליצור אווירה` to `צריך אור חזק — זו אינה מטרתה` and puts the string out.
3. **It is already the Liquid shape.** `switch/index.html` lines 121–160: six `<li>` rows, each with a
   to-scale glowing string, bulb count, price, ≈₪/metre **and its own `<form method="post" action="/cart/add">`
   with the colour as a `<select name="id">`**. That is exactly what BRIEF §9 asks for — full ledger with
   per-variant forms without JS, JS enhances to a selector — built, not promised.

### Where the judges were right

- Creative director: the hero **dot-grid** (unlit bulbs drawn as a field over the photograph) reads as a
  screen-door artefact at 1×. Killed in §4.1 — unlit bulbs exist only on the cord path.
- Creative director: the **~350 px dead band** under the toggle (desktop slice 2, and worse on mobile). That
  band is exactly where `place`'s second question goes (§2, graft B).
- Creative director + copy chief: `switch`'s **wall hero is the weakest of the three** — a dim plate on grey.
  Replaced by `walk`'s diptych (§2, graft D).
- Copy chief: `«5 מטר מכסים פינה אחת; 22 מטר עוטפים חלל שלם»` is an authored coverage claim. Removed; the
  ledger's per-row meanings are quoted from the product's own description instead (§4.4).
- Copy chief: `ששה אורכים` → **`שישה אורכים`**.
- Conversion + creative + copy: the **colour axis renders as four items on one line**. Fixed globally by the
  option-axis rule in §3.6 — four values is never four in a row.

### Where the judges were wrong (I checked the pixels)

- **Conversion judge, graft "place's real string of bulbs per ledger row":** `switch` already has it.
  Desktop slice 2 and mobile slice 3 show every row carrying a to-scale lit string (`svg.mini`,
  `data-m`/`data-b`). Rejected as a graft — it is the incumbent.
- **Conversion judge, "switch's bollard slider hides the money until you stop dragging":** false. The path
  fold prints all eight running totals before the buyer touches anything. What is missing is *meaning*, not
  money — hence graft C.
- **Conversion judge, "the six-column rail pushes captions under 13 px":** true only of the fold rail, not
  the ledger; on mobile the ledger is full-width rows at legible sizes. Fixed narrowly in §4.1 (the rail
  becomes a snap-scrolling single line at 26/13/14 px) rather than by importing another concept's ledger.
- **Creative director, graft "place's scrim card with a product thumbnail in the hero":** rejected on A and B.
  `place` needs a thumbnail because its hero photograph is the *decor collection scene*, not the product;
  `switch`'s hero **is** the product (`solar-crystal-ball-string-lights` images[2]). Adding a thumb would
  clutter the one fold that is already complete. The thumbnail survives only where it belongs: 46 px, in the
  sticky mobile bar.
- **Copy chief ranked `switch` 4th on writing and `dialogue` 1st.** Correct, and irrelevant to the ruling:
  copy is the one thing that grafts losslessly. Two of the six grafts are `dialogue`'s sentences.
- **Nobody caught the honesty landmine that will actually ship.** `METAFIELD-SHEET.md` §2: product C
  (`waterproof-led-wall-light-ip65-6w-12w`) has **no stated power source** — "לא צוין". BRIEF §5 calls it
  mains, and `switch/wall.html` prints `חיבור לחשמל` in the fold. That is a typed fact. §3.7 makes the power
  branch three-state; when unstated the page says *nothing* about power. Same for the not-for device: C has
  no true approved negative (`METAFIELD-SHEET` §5), so §4.2 renders the product's own choosing sentence and
  never invents one.

**Ranking:** `switch` · `dialogue` · `place` · `ledger` · `walk`.

---

## 2. Grafts (device → where it lands)

| # | From | Device (as rendered in the source) | Lands in |
|---|------|-----------------------------------|----------|
| A | `dialogue` | A use-meaning caption on every ledger row — `20 נורות · לפינת ישיבה קטנה או לשולחן אחד` … `200 נורות · קישוט של חלל שלם` (`dialogue/index.html` beat 04) | §4.4 ledger, the `__use` column. Turns a price list into the specialist's advice; pure copy, all of it quoted from the product's own description. It is the only thing on the page that decides 9.5 vs 11 metres. |
| B | `place` | The second place question — `כמה שמש המקום מקבל ביום?` → `שמש במשך היום` (lit) / `כמעט אינו מקבל אור יום` (dark) (`place/index.html` screen 02) | §4.2, directly under the toggle — it fills the dead band. Makes the solar limitation the buyer's own answer instead of a disclaimer. Solar branch only (§3.7). |
| C | `ledger` | Quantity rows labelled by what the quantity buys — `2 יח׳ משני צידי כניסה · 3 שורה קצרה · 4 לאורך שביל · 6 מהשער אל הדלת` (`ledger/path.html` fold) | §4.4 on product B: each stop of the bollard rail gets its meaning. Becomes the catalogue pattern for every quantity product. |
| D | `walk` | The wall diptych fold — product close-up beside a lit façade, the headline riding the seam (`walk/shot-wall-desktop-fold.png`, `walk/wall.html` lines 414 + 441) | §4.1 on product C only. Fixes the weakest of the three heroes and gives C a place at night while keeping the halo stage. The façade half is the **collection scene**, so it carries the place kicker, never `המנורה שבתמונה`. |
| E | `dialogue` | The hesitation as the section head — the buyer's own question set large in Frank Ruhl Libre inside guillemets (`dialogue` beats 01–08) | §4.2 and §4.5 headings: `«זה יתאים למרפסת שלי?»` and `«ומה יכול להשתבש?»`. States the hesitation before the device answers it — literally the owner's directive — and puts an editorial line where `switch` had empty space. |
| F | `ledger` | Two pieces of micro-copy: the one-line terms strip **under** the ATC, and `למי זה לא מתאים ←` **beside** the ATC (`ledger/index.html` screen 1) | §4.1 buy box. The negative offered at the moment of commitment is the store's whole position in three words; the terms strip puts the four numbers inside the mobile fold in eleven. |
| G | `place` | The related-module deck `בלי כוכבים ובלי «נמכר ביותר» — אין לנו עדיין מה למדוד.` | §4.8. Converts an absence into evidence of the position. Best sentence written for this brief. |
| H | `ledger` | The section head `ארבעה מספרים, לפני שמשלמים.` + deck `לא אותיות קטנות. אותיות גדולות, במקום גלוי, ליד הכפתור.` | §4.6. Sells the terms as a virtue instead of burying them. |

Rejected grafts, with reasons, are in §1 ("Where the judges were wrong").

---

## 3. Global decisions for the PDP

### 3.1 The ground — photo, then a short sky

The homepage is a sunset: `sky-0 → sky-4` over eight sections. **The PDP is already night.** The buyer arrives
from a collection card or an ad, not from daylight; there is no dusk to narrate, and starting on `#4a6a9c`
would make the product photograph look like a daytime catalogue shot.

- **Screen 1 is a photo ground:** a full-bleed night photograph at `min-height:100svh`, its bottom ~26 %
  blended into `--env2-sky-2` by a two-stop veil (lift `.stage__veil`, `switch/switch.css:104`).
- **The document below it is a short sky**, one gradient on the body, never per section:

```css
html{background:#020306}
body.template-product{
  background:linear-gradient(180deg,#0f1a2f 0%,#0f1a2f 20%,#070b15 56%,#020306 100%) no-repeat;
  background-size:100% 100%;
}
.template-product #wrapper,.template-product .main-content,.template-product main{background:transparent}
```

- `elmsnest-v2-base.liquid` currently guards on `body.hdt-page-type-index` (AUDIT §3). **Widen the guard to
  `body.hdt-page-type-product` and move the gradient into a new snippet `elmsnest-v2-ground-product.liquid`**,
  mirroring the existing `elmsnest-v2-ground-index.liquid`. Do not fork the tokens.
- Stars (`.env2-stars`) per section: fit `.22` → night `0` (photo) → ledger `.34` → facts `.45` → terms `.55`
  → ask `.62` → related `.70`. None on the stage.
- No section paints a background. The only card surface anywhere is the scrim
  `rgba(5,8,14,.55)` + `backdrop-filter:blur(10px)` — used exactly twice: the mobile sticky bar and the
  C diptych caption. No brown, beige or cream. Kalles' breadcrumb section is removed from the template
  (§5), so its colour scheme cannot paint cream above the stage.
- The header is transparent over the stage. This also fixes AUDIT §176 bug (a): the PDP's first screen is
  dark, so the `scheme-env2-night` header is legible without a per-template scheme.

### 3.2 Type sizes per role

Faces and tokens are inherited from `brief/WINNING-SPEC.md` §3.2 (`--env2-serif` Frank Ruhl Libre 500/700/900,
`--env2-sans` Heebo 300/400/500). **Product titles are never in the serif.** Hebrew display leading `.98`,
`letter-spacing:-.01em`, `text-wrap:balance`.

| Role | Face / weight | 1440 | 390 | CSS |
|------|---------------|------|-----|-----|
| h1 (stage) | FRL 700 | 84 | 38 | `clamp(38px,5.8vw,84px)`, lh .98, line 2 in `--env2-glow` |
| h2 (section) | FRL 700 | 72 | 34 | `clamp(34px,4.9vw,72px)`, lh .98 |
| h2 (fit, guillemet question) | FRL 700 | 86 | 36 | `clamp(36px,5.8vw,86px)`, lh .98 |
| toggle half (the approved pair) | FRL 700 | 46 | 24 | `clamp(24px,3.2vw,46px)`, lh 1.0 |
| giant fact numeral (`IP65`, `8–10`) | FRL 900 | 230 | 96 | `clamp(96px,16vw,240px)`, outline `1px rgba(244,238,227,.45)` → glow fill when lit |
| terms numeral | FRL 500 | 72 | 48 | `clamp(48px,5vw,72px)`, tabular |
| ledger metre numeral | FRL 500 | 44 | 34 | `clamp(34px,3vw,44px)`, tabular; unit at `.32em` |
| rail stop numeral | FRL 500 | 32 | 26 | tabular |
| price — stage | FRL 500 | 46 | 38 | tabular, glow, `white-space:nowrap` |
| price — ledger row / related card | FRL 500 | 22 / 21 | 20 / 19 | |
| price — sticky bar | FRL 500 | — | 22 | |
| quote (ask) | FRL 400 | 32 | 22 | `clamp(22px,2.4vw,32px)`, lh 1.25 |
| lead | Heebo 300 | 17–20 | 16 | `clamp(16px,1.4vw,20px)`, 38–44ch, `--env2-ink-2` |
| body / fact `dd` | Heebo 300/400 | 16 | 15 | lh 1.55 |
| product title | Heebo 400 | 19 | 16 | `clamp(16px,1.3vw,19px)`, `unicode-bidi:isolate` |
| ledger use-caption (graft A) | Heebo 300 | 15 | 14 | `--env2-ink-2` |
| any information-bearing caption | Heebo 300 | ≥14 | **≥13** | hard floor — no exceptions |
| kicker / axis label | Heebo 500 | 11.5 | 11.5 | `letter-spacing:.16em`, gold; labels only, never data |
| button | Heebo 500 | 15 | 14 | min tap target 48 px (44 px minimum) |

`<bdi>` on every Latin token (`IP65`, `LED`, `6W`, `3000K`) and every price: `<bdi>179.90</bdi> ₪`.
**A slash-joined pair goes inside ONE `<bdi>`** — `<bdi>6W/12W</bdi>`, never `<bdi>6W</bdi>/<bdi>12W</bdi>`,
which renders `12W/6W` under RTL (the bug visible on both of `walk`'s wall folds).

### 3.3 Motion rules

Inherited: `[data-lamp]` lights once at 25 % visibility and never re-dims; no-JS/reduced-motion = everything lit;
no text fades, no parallax, no autoplay (`CONTRACT.md` "The lamp device").

PDP-specific — **exactly one thing switches on per section, and it is the thing the section is about:**

| Section | What lights | Timing |
|---|---|---|
| stage | the string/halo on the photograph, bulb by bulb | 40 ms stagger, capped at 1.1 s total; starts on paint (screen 1 intersects immediately) |
| stage — variant change | bulbs added or removed to the new count; price counts to the new value | same 40 ms stagger; count-up ≤ 400 ms, tabular, off under reduced motion |
| fit | nothing lights — the toggle **puts the string out**: `.dark`, a 240 ms flicker (`@keyframes env2-flick`), then off, and the verbatim negative prints | 240 ms + .35 s knob travel |
| night | the two photographs, staggered | on arrival |
| ledger | the chosen row's string; the previous row's string dims to cord only | .55 s per bulb group |
| facts | the outlined giant numeral fills with glow | 1.4 s `color` + `-webkit-text-stroke-color` |
| terms | the four numerals, in reading order | 120 ms stagger |
| ask / related | the product photographs (`[data-lamp]`) | on arrival |

Product-specific stage motion: **C** — `6W → 12W` grows the halo radius and opacity, `3000K → 6000K` shifts the
halo hue `#ffd394 → #cfe0ff`, both `.5s`; **B** — quantity draws bollards receding down the path, 60 ms stagger.
Hover: buttons `translateY(-2px)` + glow shadow `.35s`. No scale, no bounce, no marquee.

### 3.4 The Kalles strategy — **rebuild the buy stack in our own sections**

Decision: **rebuild.** `main-product` and every `_product-*` block are removed from the product template
(§5). Variant state, price, add-to-cart, `?variant=` sync and the sticky bar are ours.

Why, in order of weight:

1. **The idea is not expressible inside the contracts.** `hdt-variant-picker → hdt-price → hdt-sticky-btn-atc`
   is one buy box in one place. Our buy state is spread over the whole page: the stage rail, six ledger rows
   each with its own form, the sticky bar, and a "start at 5 m" button in §4.7 that selects a row from two
   screens away. Keeping the contracts means keeping Kalles' picker markup — the brown rectangles that never
   show a price — which is precisely what the owner ordered replaced ("استبدل").
2. **The no-JS requirement is cheaper our way.** The ledger already *is* eleven `<form method="post"
   action="{{ routes.cart_add_url }}">` elements; without JS the buyer sees every price and can buy any
   variant. Wrapping Kalles' JS-bound picker to do that is more work, not less.
3. AUDIT §180 says either is possible; the custom price snippet already had to clone the `hdt-price` DOM and
   re-attach `form=` in an inline script at DOMContentLoaded. That fragility goes away with the rebuild.

**What we keep from Kalles — exactly two things:**

- **The cart drawer.** `POST /cart/add.js` (fetch), then re-render `/cart.js` into the theme's drawer and
  dispatch the theme's open event. *Verify the event name on the live preview before writing the section*
  (`OWNER-NOTES` §6: the drawer is primary, the cart page is the no-JS fallback). If the event cannot be
  resolved, fall back to `window.location = routes.cart_url` — never a silent failure.
- **`?variant=` URL sync**, via `history.replaceState`, so shared links and Meta catalogue deep links land on
  the right row.

Everything else — `hdt-*` classes, `product-form-<section>-<product>`, `variant:change`, `.hdt-money`,
`hdt-media-gallery` — is not referenced by any section we write.

### 3.5 The image ledger rule

Per-product, per-slot, merchant-editable, and it can never render a baked-text slide.

- Every image slot is **two schema settings**: `<slot>_image_index` (`range`, 1–6, **1-based = Shopify admin
  position**) and `<slot>_image` (`image_picker`, wins when set). Resolution in Liquid:
  `{%- assign img = section.settings.hero_image | default: product.images[section.settings.hero_image_index | minus: 1] | default: product.featured_image -%}`
- **Never index 0** for the fifteen products on the `brief/WINNING-SPEC.md` §3.6 never-use list. Enforced in
  Liquid, not by discipline: `elmsnest-v2-pdp-image.liquid` holds the handle list in one `assign`; if the
  resolved index is 0 **and** the handle is on the list, it silently steps to index 1. Log nothing, render
  the right picture.
- **Defaults that ship** (0-based `product.images[i]`; admin position = i+1):

| Product | stage hero | close-up | night gallery | diptych partner | sticky thumb |
|---|---|---|---|---|---|
| A `solar-crystal-ball-string-lights` | `[2]` string on the wooden trellis | `[0]` bulb close-up | `[2]` + `[0]` | — | `[0]` |
| B `stainless-steel-solar-path-light-ip65` | `[0]` three bollards on the brick path | `[3]` bollard by wall + steps | `[3]` + `[1]` (dark, the "lamp off" candidate) | — | `[3]` |
| C `waterproof-led-wall-light-ip65-6w-12w` | `[1]` black cube lit on plaster | `[3]` wide wall light lit | `[3]` + `[2]` (studio colour pairs) | `collection-wall` featured image | `[1]` |

- The C diptych partner is a **collection scene**, not this product. Its kicker is the place
  (`כניסה, קיר וחזית`), never `המנורה שבתמונה`. That single rule is what separates graft D from `walk`'s
  honesty breach.
- Loading: stage hero `loading="eager" fetchpriority="high"`, `widths:'900,1400,1800,2400'`, `sizes:'100vw'`,
  plus a `<source media="(max-width:900px)">` at `width:1000`. Everything below the fold `loading="lazy"`
  with explicit `width`/`height`. Gallery tiles get eager loading for the first tile only (AUDIT §182: the
  current lazy tiles render blank in captures).
- Variant images: A and B have none; C has `variant.image` on 5 of 8. When `variant.image` exists, the stage
  photograph cross-fades to it on selection (.5 s), otherwise the stage photograph never changes.

### 3.6 The option-axis rule (this is how "no four in a row" dies)

All five concepts broke §11 the same way: four colour swatches on one line. One rule, applied everywhere,
kills it and generalises to the whole catalogue:

- **An axis with 2–3 values** renders as an **inline hairline radio line** (label · value · value), tap target
  ≥ 44 px, selected value underlined in `--env2-glow`. (C: `לבן/שחור`, `6W/12W`, `3000K/6000K`.)
- **An axis with ≥ 4 values** renders as a **hairline `<select>`** — `border:0; border-bottom:1px solid
  var(--env2-hair-btn); border-radius:0; background:transparent; color:var(--env2-ink); font:15px Heebo`
  — with the label above it in the axis-label style and a note beneath. (A: `צבע האור`, four values, note
  `אותו מחיר לכל צבע`.)
- **An axis with 1 value never renders at all** (BRIEF §11 "no one-value picker"). B's `צבע אור: צהוב חם`
  is printed as a *fact* in the selection mirror and the facts ledger, never as a control.
- **The price-bearing axis is never a select.** It is the ledger (§4.4) — rows on hairlines, one per value,
  every price visible before choosing.

### 3.7 The power-source branch

`custom.power_source` (proposed new `single_line_text` definition, `metafields.json`). **Three states, not two.**

```liquid
{%- assign pwr = product.metafields.custom.power_source | default: '' -%}
{%- if pwr == 'סולארי' -%}   … solar sentences …
{%- elsif pwr == 'חשמל' -%}  … mains sentences …
{%- else -%}                 … nothing about power at all …
{%- endif -%}
```

- **Solar only:** the panel sentence, charge hours, the winter note, the `#env2-pdp-fit` second question
  (graft B), and the approved clause `המקום כמעט אינו מקבל אור יום`. A and B are `סולארי`.
- **Mains only:** the electrician note. Nothing else.
- **Unstated (`''`):** the page says **nothing** about power. No "חיבור לחשמל", no "סולארי", no panel, no
  charge time, and the fit device drops its second question. **Product C is in this state today**
  (`METAFIELD-SHEET.md` §2) — the BRIEF's "mains" is an inference, and an inference is not a fact.
  A tag fallback is *not* acceptable: `waterproof-led-wall-light-ip65-6w-12w` is tagged `תאורת קיר סולארית`
  and is not solar (`METAFIELD-SHEET.md` §11).
- The owner can flip C to `חשמל` by approving that one metafield value. Until then the branch stays silent.
- Same three-state discipline for the negative: `custom.not_fit_for` renders **verbatim** when present (it is
  always one of the four approved pairs); when empty — 7 of 27 products, C included — §4.2 renders the
  product's own choosing sentence and **never invents a negative**.

---

## 4. Section-by-section build spec (page order)

Sketch legend: `▲` = start side (right in RTL), `▼` = end side (left).
All copy below is exact. Product facts are Liquid or quoted from `description_text`; brand lines are authored.

---

### 4.1 `elmsnest-v2-pdp-stage` — screen 1 + the buy box · `#env2-pdp-stage`

**Purpose.** Spine #1 and the whole buy decision, inside the fold on 1440×900 **and** 390×844: the lamp lit
in its place at night, the place word + approved "suits" phrase, the title, the price with its range, the
add-to-cart, the four numbers in one line, the small step, and a preview of the full ledger.
Renders `elmsnest-v2-fonts` and `elmsnest-v2-base` at the very top of its markup, then
`elmsnest-v2-ground-product`.

**Copy (A — crystal balls).**
- kicker: `מרפסת ופינת ישיבה · מתאים כדי ליצור אווירה`
- h1: `הערב מתחיל` / *(glow)* `מהכדור הראשון.`
- title: `{{ product.title }}` (Heebo, `unicode-bidi:isolate`)
- axis label + select: `צבע האור` → `צהוב · כחול · צבעוני · לבן` · note `אותו מחיר לכל צבע`
- price: `<bdi>89.90</bdi> ₪` · selection mirror: `5 מ׳ / 20 נורות · צהוב`
- range line (graft F/dialogue): `מ־89.90 עד 179.90 ₪, לפי האורך. הצבע לא משנה את המחיר.`
- primary: `הוספה לסל` · beside it (graft F): `למי זה לא מתאים ←` → `#env2-pdp-fit`
- terms strip under the button (graft F): `משלוח לנקודת איסוף חינם · אספקה 8–17 ימי עסקים · ביטול עד 14 יום
  מקבלת המוצר.` + link `כל המספרים` → `#env2-pdp-terms`
- small step: `לפני שמזמינים אפשר לשלוח תמונה של המקום` → mailto (§4.7)
- rail label: `אורך ומספר נורות — המחיר לפי האורך בלבד`

**Copy (B — path light).** kicker `שביל, מדרגות ומעברים · מתאים כדי לראות את הדרך`; h1 `הדרך הביתה` /
`נדלקת לבד.`; price `<bdi>169.90</bdi> ₪`, mirror `יחידה אחת · אור צהוב חם` (a fact, not a picker — §3.6);
rail label `כמה יחידות? — יחידה אחת מאירה נקודה, שורה של יחידות יוצרת אפקט` *(quoted from the description)*.

**Copy (C — wall light).** kicker `כניסה, קיר וחזית · מתאים כדי להאיר נקודה מסוימת`; h1 `קיר אחד.` /
`שתי אלומות.`; title carries `<bdi>IP65</bdi> – <bdi>6W/12W</bdi>` from `product.title`; three radio lines
(§3.6) `עוצמה 6W · 12W` / `גוון אור 3000K · 6000K` / `צבע גוף לבן · שחור`; price `<bdi>219.90</bdi> ₪`, range
line `219.90–252.90 ₪, לפי העוצמה והגוון. צבע הגוף אינו משנה את המחיר.` No power sentence (§3.7).

**Layout, desktop 1440.**
```
┌───────────────────────────────────────────────────────────────┐ ← transparent Kalles header (70px) over the photo
│  full-bleed night photograph of the product, 100svh            │
│  the string / halo lights bulb-by-bulb on paint                │
│                                                                │
│                                    ▲ kicker                    │
│                                    ▲ h1 84px, 2 lines          │
│   ▼ price 46px                     ▲ product title 19px        │
│   ▼ mirror + range line            ▲ colour axis (select)      │
│   ▼ [הוספה לסל]  למי זה לא מתאים ←                              │
│   ▼ terms strip · photo-check link                             │
├───────────────────────────────────────────────────────────────┤
│  rail: 6 stops on one hairline — 5 · 6.5 · 9.5 · 11 · 13 · 22  │
│  each with bulbs + price; fill hairline runs to the chosen stop│
└───────────────────────────────────────────────────────────────┘
```
`.env2-pdp-stage__body` is `grid-template-columns:minmax(0,1fr) auto; align-items:end; gap:40px 56px`,
`padding-block:min(34vh,330px) 4px`. **The price and the button are in the same column, 12 px apart** — never
the desktop split that stranded `dialogue`'s price 700 px from its button.

**Layout, mobile 390 (the fold that wins the brief).** Single column, `padding-block:96px 0`:
kicker (2 lines) → h1 38 px → title → colour axis → price 38 px + mirror → range line → full-width
`הוספה לסל` (min-height 52 px) → `למי זה לא מתאים ←` → terms strip (2 lines, 13 px) → rail.
**`הוספה לסל` must have its bottom edge above 700 px** so that browser chrome cannot eat it — `place` failed
here at ~808 px. Verify with `node brief/shot.js` at 390×844 before sign-off.

**The rail (mobile fix).** One line, `display:flex; overflow-x:auto; scroll-snap-type:x mandatory;
scrollbar-width:none`, stop `min-width:92px; scroll-snap-align:center`, numeral 26 px, `נורות` caption 13 px,
price 14 px, fade mask on the end side. Never a 2×3 grid — that is four-of-a-thing in a box.

**Imagery.** §3.5. `.env2-pdp-stage__veil` = the two-stop gradient at `switch/switch.css:104` (bottom 26 %
→ `--env2-sky-2`, top 24 % → 60 % black for header legibility).

**Motion.** The string is an inline SVG built by JS along a catenary across the photograph
(`switch/switch.js` `makeString`, lines 41–126). **Unlit bulbs are drawn only on the cord path** — the
hero-wide dot field is deleted (see §1). C uses a halo instead of a string; B uses `makePath` (lines 127–186).

**Schema (`elmsnest-v2-pdp-stage`).**
`kicker` (text) · `heading_line1` · `heading_line2` · `hero_image_index` (range 1–6, default per §3.5) ·
`hero_image` (image_picker) · `hero_image_mobile` · `object_position_desktop` · `object_position_mobile` ·
`stage_device` (select: `string` / `halo` / `path`, default `string`) · `price_axis_option` (select:
`option1|option2|option3`, default `option1` — which option the ledger/rail is built from) ·
`quiet_axis_note` (text, default `אותו מחיר לכל צבע`) · `show_rail` (checkbox, default true) ·
`terms_strip` (text) · `photo_link_label` (text, default `לשלוח תמונה של המקום`) · `mailto_subject`.

**Non-negotiables.** Product photograph, place kicker with the approved suits phrase, resolved price (never
only `מ־`), a real `הוספה לסל`, the range disclosed, and the negative link — all inside both folds.

---

### 4.2 `elmsnest-v2-pdp-fit` — the not-for device · `#env2-pdp-fit`

**Purpose.** Spine #2, inside the second screen. The approved pair rendered as a physical switch: flipping it
puts the product's own light out. Then the buyer's second question (graft B), which disqualifies her before
she pays.

**Copy (A).**
- eyebrow: `02 · מתי כן, ומתי לא`
- h2 (graft E): `«זה יתאים למרפסת שלי?»`
- lead: `לכל מקום יש מטרה שהגרילנדה ממלאת — ומצב שבו היא לא. העבירו את המתג ותראו.`
- toggle, start side (on): tag `מתאים כדי` · `ליצור אווירה`
- toggle, end side (off): tag `לא מתאים כש־` · `צריך אור חזק — זו אינה מטרתה` **(verbatim, never edited)**
- on flip: `לא נדלק. זו הנקודה.`
- redirect, keeps the sale: `לאור חזק על קיר או בכניסה יש אצלנו מקום אחר — תאורת קיר. לאווירה, זו.`
  (`תאורת קיר` links to the collection)
- **graft B, second question:** `כמה שמש המקום מקבל ביום?` → `שמש במשך היום` (lit) / `כמעט אינו מקבל אור יום`
  (dark). Answering the second: `הפאנל נטען מהשמש והשרשרת נדלקת עם החשכה. אם המקום כמעט אינו מקבל אור יום —
  זה לא המוצר.`
- closing: `לא בטוחים? לשלוח תמונה של המקום ←` (mailto)

**Copy (B).** Same structure. Pair: `מתאים כדי` `לראות את הדרך` / `לא מתאים כש־` `המקום כמעט אינו מקבל אור
יום`. Note that for B the approved negative *is* the solar clause, so graft B's second question becomes
`מה האור צריך לעשות שם?` → `לראות את הדרך` / `להאיר את כל החצר` — **only if** a true source exists; if not,
the second question is omitted. Default: omitted on B.

**Copy (C).** `custom.not_fit_for` is empty (§3.7). The toggle renders the *suits* half plus the product's own
choosing sentences, verbatim from the description, and **no negative**:
`6W לאפקט עדין וממוקד; 12W לנוכחות חזקה יותר על שטח גדול.` and
`בכניסה צרה אפשר להסתפק ביחידה. על חזית רחבה או לאורך מעבר, התקנה סימטרית או רציפה תיצור אפקט שלם ומרשים יותר.`
Section eyebrow becomes `02 · איך בוחרים נכון`.

**Layout, desktop.** `padding-block:110px 90px`. Centred head (max 780 px). Then the toggle as a 3-column grid
`1fr auto 1fr`, `width:min(1100px,100% - 2*gut)`, the 96×48 knob in the middle, the two halves at 46 px FRL.
Below it the **string spanning the full width** (this is what goes dark). Then — in what was `switch`'s dead
band — graft B: the question as a 32 px serif line at the start side, its two answers as a hairline pair at
the end side, `margin-block-start:96px`.

**Layout, mobile.** Head; toggle stacked as `1fr auto 1fr` collapsing to `auto auto auto` rows (suits · knob ·
not-suits) with the halves at 24 px; string full-bleed beneath; graft B as two stacked hairline answers.
The toggle must sit **inside the second screen** — target `y ≈ 1,100–1,250 px`.

**Motion.** The only section where nothing lights. Flip → `.dark` on the string (`switch/switch.css:92–94`),
240 ms flicker, then off; the negative and `לא נדלק. זו הנקודה.` print at the same moment. Flipping back
re-lights (this is the one permitted re-light on the page, because the buyer asked for it). Reduced motion:
both states legible, no flicker, the negative always visible.

**Schema.** `eyebrow` · `question` (text, the guillemet head) · `lead` · `suits_label` / `suits_text` ·
`notfit_label` / `notfit_text` (**default from `product.metafields.custom.not_fit_for`; the section must not
render a negative when that is blank**) · `refusal_line` · `redirect_html` (richtext, one link) ·
`show_solar_question` (checkbox, **auto-off unless `power_source == 'סולארי'`**) · `solar_question` ·
`solar_yes` · `solar_no` · `solar_answer` · `photo_link_label`.

**Non-negotiables.** The pair verbatim. Never a fifth negative. Never a negative on a product whose
`not_fit_for` is empty. The dark state must be genuinely dark in a static screenshot.

---

### 4.3 `elmsnest-v2-pdp-night` — the night gallery · `#env2-pdp-night`

**Purpose.** Spine #3. What it actually looks like at night, at two distances, with a scale cue — and the
product's own light is the only light in both frames.

**Copy (A).** eyebrow `03 · בלילה` · h2 `מקרוב, הכדור הוא האור.` ·
lead *(quoted)*: `תולים סביב אזור הישיבה, לאורך גדר או בתוך אוהל. האור משתקף בתוך כל כדור — ולכן חלל פשוט
נראה חגיגי.` · caption 1 `מקרוב` · caption 2, the scale cue *(quoted, not authored)*:
`על הפרגולה. מ־5 ועד 22 מטר — לפי גודל האזור שמדדתם.` · honesty note `התמונות להמחשה.`

**Layout, desktop.** Two staggered figures, **no grid**: the trellis shot at `width:min(58%,720px)` on the end
side, `aspect-ratio:4/3`; the close-up overlapping it by 8 % on the start side at `width:38%`,
`aspect-ratio:1/1.15`, offset `translateY(22%)`. Head at the start side, baseline-aligned to the big figure's
top edge. `padding-block:110px 100px`. Full-bleed on the end side (the big figure runs to the viewport edge).

**Layout, mobile.** Big figure full-bleed edge to edge; the close-up beneath it inset `margin-inline-start:24px;
width:70%`, pulled up `-14%`; captions under each, 13 px.

**Motion.** Both `[data-lamp]`, staggered 220 ms. Nothing else.

**Schema.** `eyebrow` · `heading` · `lead` · `big_image_index` / `big_image` · `small_image_index` /
`small_image` · `caption_big` · `caption_small` · `note` · `big_aspect` / `small_aspect` (text, default
`4/3` and `1/1.15`).

---

### 4.4 `elmsnest-v2-pdp-ledger` — the variant / price ledger · `#env2-pdp-ledger`

**Purpose.** Spine #4, and the technical heart of the page. Every length / quantity / wattage with its own
price **before** selecting, ≈ price per metre or per unit, what that row is *for* (graft A), and its own
add-to-cart. 24 variants become one decision.

**Copy (A).**
- eyebrow `04 · מה מקבלים` · h2 `שישה אורכים.` / `הצבע לא משנה את המחיר.`
- lead *(verbatim from the description)*: `מדדו את אזור התלייה והוסיפו מרווח לקשתות ולליפוף. שרשרת מעט ארוכה
  יותר נראית מלאה ומעוצבת יותר משרשרת מתוחה מדי.`
- the six rows — **numerals and prices from Liquid; the `__use` column is graft A, every phrase quoted from
  the product's own description:**

| מ׳ | נורות | ₪ | ≈ ₪ למטר | `__use` |
|---|---|---|---|---|
| 5 | 20 | 89.90 | 17.98 | `לפינת ישיבה קטנה או לשולחן אחד` |
| 6.5 | 30 | 89.90 | 13.83 | `אותו מחיר, מטר וחצי יותר` |
| 9.5 | 50 | 99.90 | 10.52 | `לאורך גדר או מעקה` |
| 11 | 60 | 109.90 | 9.99 | `מסגרת לפרגולה` |
| 13 | 100 | 129.90 | 9.99 | `כמעט פי שניים נורות לאותו מרחק` |
| 22 | 200 | 179.90 | 8.18 | `קישוט של חלל שלם` |

- colour axis beneath the table (§3.6 select): label `צבע האור`, note `אותו מחיר לכל צבע`, description line
  `צהוב לאווירה חמה, לבן למראה נקי, כחול לאפקט קריר או צבעוני למסיבה.`
- after: `לחיצה על שורה מדליקה אותה בבמה למעלה.`

**Copy (B) — quantity, graft C.** h2 `כמה נקודות אור בדרך הביתה.` · rail/rows `1 · 2 · 3 · 4 · 6 · 8` at
169.90 ₪ each, running totals from Liquid (`169.90 · 339.80 · 509.70 · 679.60 · 1,019.40 · 1,359.20`), and the
meanings: `יחידה אחת מאירה נקודה` · `משני צידי כניסה` · `שורה קצרה` · `לאורך שביל` · `מהשער אל הדלת` ·
`מסביב למדשאה` *(all quoted from the description)*. Quantity posts as `quantity=N` on the single variant.
Footnote *(verbatim)*: `למראה מרשים באמת, מקמו מספר מנורות במרווחים אחידים לאורך שביל, מסביב למדשאה או בכניסה.`

**Copy (C) — two price-bearing axes.** Four rows (`6W/3000K` 219.90 · `6W/6000K` 222.90 · `12W/3000K` 249.90 ·
`12W/6000K` 252.90) with `__use` from the description: `אפקט עדין וממוקד` · `עדין, בגוון לבן וחד` ·
`נוכחות חזקה יותר על שטח גדול` · `חזק, בגוון לבן וחד`. Body colour is the quiet axis (§3.6 radio line, note
`צבע הגוף אינו משנה את המחיר`).

**Markup (this is the contract — copy the shape from `switch/index.html:132–157`).**
```liquid
<ol class="env2-pdp-ledger__rows">
{%- for v in price_axis_values -%}   {%- comment -%} one row per value of the price-bearing option {%- endcomment -%}
  <li class="env2-pdp-ledger__row" data-i="{{ forloop.index0 }}" data-value="{{ v.value | escape }}">
    <button type="button" class="env2-pdp-ledger__pick" aria-pressed="false"
            aria-label="{{ v.label }}, {{ v.price | money_without_currency }} ₪">
      <span class="n"><bdi>{{ v.number }}</bdi><small>{{ v.unit }}</small></span>
      <svg class="mini" data-m="{{ v.number }}" data-b="{{ v.bulbs }}" aria-hidden="true"></svg>
      <span class="b">{{ v.bulbs }} נורות</span>
      <span class="use">{{ v.use }}</span>                      <!-- graft A -->
      <span class="env2-price"><bdi>{{ v.price }}</bdi> ₪</span>
      <span class="pm">≈ <bdi>{{ v.per_unit }}</bdi> ₪ למטר</span>
    </button>
    <form method="post" action="{{ routes.cart_add_url }}" class="env2-pdp-ledger__form">
      <input type="hidden" name="quantity" value="1">
      <select name="id" aria-label="צבע האור">                   <!-- quiet axis inside the row -->
      {%- for q in v.quiet_variants -%}<option value="{{ q.id }}">{{ q.label }}</option>{%- endfor -%}
      </select>
      <button class="env2-btn env2-btn--ghost env2-btn--sm" type="submit">הוספה לסל</button>
    </form>
  </li>
{%- endfor -%}
</ol>
```
- **No JS:** all six rows visible with all six prices; every row buyable; the quiet axis is a native select.
- **With JS:** `html.env2-js` hides the per-row forms (`.env2-pdp-ledger__form{display:none}`), the row button
  becomes the selector, the stage price/mirror/string update, `?variant=` syncs, and the single stage
  `הוספה לסל` posts to `/cart/add.js`. This is exactly the CONTRACT's dim/lit inversion pattern applied to
  forms — the enhanced state is the *reduced* state.
- `per_unit` is computed in Liquid (`price | divided_by: metres`), rounded to 2 dp, prefixed `≈`. **Never use
  a 1-decimal figure** (`place` printed `≈ 18.0` beside `switch`'s `17.98`; on a page this precise that reads
  as carelessness).

**Layout, desktop.** Head as a 2-column grid (`h2` start / lead end, baseline-aligned). Rows are
`grid-template-columns: 88px 200px 1fr max-content 96px 132px` separated by `border-top:1px solid var(--env2-hair)`,
`padding-block:18px`, no boxes. The chosen row's numeral goes `--env2-ink`, its string lights, its price
brightens.

**Layout, mobile.** Rows become two lines each — line 1: numeral · string · bulbs · price; line 2: `__use` ·
`≈ ₪ למטר` · the row's own ATC pill. `padding-block:20px`, hairline between. **Never a horizontal 6-column
squeeze on 390** — that is where every fold-rail legibility complaint came from.

**Motion.** Choosing a row lights its string (40 ms per bulb) and dims the previous one to cord. The stage
price counts to the new value ≤ 400 ms.

**Schema.** `eyebrow` · `heading_line1` / `heading_line2` · `lead` (default: the description's advice
paragraph, parsed — §5) · blocks `row` (max 12) with `label` · `use_caption` · `unit_label` (`מ׳` / `יח׳` /
`W`) · `bulbs_label`; plus `show_per_unit` (checkbox) · `per_unit_suffix` (text, `₪ למטר` / `₪ ליחידה`) ·
`quiet_axis_note`. The row values themselves come from `product.variants` — the blocks only carry the
authored captions, keyed by option value.

**Non-negotiables.** Every price visible before selecting. Per-unit price on every row. The `__use` caption is
quoted, never invented. Colour never changes the price, and the page says so.

---

### 4.5 `elmsnest-v2-pdp-facts` — what could go wrong · `#env2-pdp-facts`

**Purpose.** Spine #5. The risk-lowering facts, only from the product's own bullets, and an explicit row for
what is *not* known.

**Copy (A).**
- eyebrow `05 · מה שכדאי לדעת` · h2 (graft E, as the section's question) `«ומה יכול להשתבש?»`
- deck: `מה שכתוב כאן — נכון. מה שלא ידוע — לא כתוב.`
- the giant: `IP65` (FRL 900, outline → glow) · sub `מיועדת להישאר בחוץ — בגינה ובמרפסת, בתנאי מזג אוויר משתנים.`
- the `dl`, parsed from `פרטים שכדאי לדעת` (§5):

| dt | dd |
|---|---|
| `מקור אנרגיה` | `טעינה סולארית. הפאנל נטען מהשמש, והשרשרת נדלקת עם החשכה במצב התאורה שבחרתם.` *(solar branch only)* |
| `זמן עבודה` | `כ־8–10 שעות עבודה לאחר טעינה מלאה.` |
| `עמידות` | `<bdi>IP65</bdi>.` |
| `מצבי תאורה` | `8 מצבים.` |
| `אורך ונורות` | `5–22 מטר · 20–200 נורות <bdi>LED</bdi>.` |
| `צבע האור` | `צהוב, כחול, צבעוני או לבן.` |
| **`מה שלא כתוב`** | `מידות מדויקות, לומן ואחריות אינם מופיעים בנתוני המוצר — ולכן אינם מופיעים כאן.` |

- the preserved description: `<details><summary>כל מה שכתוב על המוצר</summary>` → `{{ product.description }}`,
  restyled by scoped CSS (§5). Hairline summary, no box, no chevron icon rows.

**Copy (B).** giant `8–10` (`שעות עבודה לאחר טעינה טובה בשמש`); rows: `גוף נירוסטה` · `גוון אור צהוב חם` ·
`טעינה ממוצעת כ־6 שעות` · `זמן עבודה כ־8–10 שעות` · `<bdi>IP65</bdi>` · `נעיצה באדמה בעומק כ־5–10 ס״מ` ·
`לפני שימוש ראשון: מצב ON וטעינה של לפחות 3 שעות` + the `מה שלא כתוב` row (`המידות המדויקות מופיעות רק
בתמונת היצרן ולכן אינן מצוטטות כאן.` — accurate per `METAFIELD-SHEET` §12).

**Copy (C).** giant `<bdi>IP65</bdi>`; rows: `גוף אלומיניום` · `<bdi>IP65</bdi>` · `עוצמה <bdi>6W</bdi> או
<bdi>12W</bdi>` · `אור חם <bdi>3000K</bdi> או קר <bdi>6000K</bdi>` · `צבע שחור או לבן` · `תאורה דו־כיוונית` ·
`מתאימה לפנים ולחוץ` + `מה שלא כתוב`: `מקור החשמל, המידות והלומן אינם מופיעים בנתוני המוצר — ולכן אינם
מופיעים כאן.` **No power row** (§3.7).

**Layout, desktop.** `grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:clamp(30px,5vw,80px);
align-items:center` — giant numeral at the end side, the `dl` at the start side; `dl>div` is
`grid-template-columns:128px minmax(0,1fr)` on hairlines. `padding-block:110px 100px`.
**Mobile:** giant first at 96 px, then the `dl` as label-above-value pairs on hairlines.

**Motion.** The giant is `[data-lamp="manual"]`, lit at a 40 % threshold: `color:transparent;
-webkit-text-stroke:1px rgba(244,238,227,.45)` → `color:var(--env2-glow); text-shadow:0 0 50px
rgba(255,211,148,.4)` over 1.4 s. (`switch/switch.css:206–209`.)

**Schema.** `eyebrow` · `question` · `deck` · `giant_text` · `giant_sub` · `source` (select:
`description_bullets` / `metafields` / `blocks`, default `description_bullets`) · blocks `fact` (`label`,
`value`, `power_gate`: select `always|solar|mains`) · `unknown_row_label` (default `מה שלא כתוב`) ·
`unknown_row_text` · `show_full_description` (checkbox, default true).

---

### 4.6 `elmsnest-v2-pdp-terms` — the four numbers · `#env2-pdp-terms`

**Purpose.** Spine #6. The licensed consumer-terms wording, sold as a virtue. A compact version already sits
under the ATC (§4.1); this is the full ledger.

**Copy (graft H, all four verbatim from the licensed wording).**
- eyebrow `06 · אחרי הלחיצה` · h2 `ארבעה מספרים, לפני שמשלמים.`
- deck: `לא אותיות קטנות. אותיות גדולות, במקום גלוי, ליד הכפתור.`
- `0 ₪` — `משלוח לנקודת איסוף — חינם.` / `שליח עד הבית: 29.90 ₪.`
- `8–17` — `ימי עסקים מרגע ההזמנה ועד הדלת.` / `1–3 ימי טיפול ועוד 7–14 ימי משלוח. חלק מהמוצרים נשלחים
  ממחסנים מחוץ לישראל.`
- `14 יום` — `ביטול עסקה לפי חוק הגנת הצרכן.` / `עד 14 יום מקבלת המוצר. דמי ביטול עד 5% ממחיר העסקה או
  100 ₪ — הנמוך מביניהם.`
- `1 תמונה` — `שלחו תמונה של המקום — נבדוק התאמה לפני שתזמינו.` / `ואם המוצר לא מתאים, נגיד את זה.` +
  link `לשלוח תמונה של המקום` (mailto)
- foot links: `משלוחים ואספקה · זמני טיפול · מדיניות ביטולים · שאלות נפוצות`

**Layout.** A **2-column hairline ledger** (`grid-template-columns:1fr 1fr; column-gap:64px`), each cell
`numeral · headline · sub`, rows separated by hairlines. **Never four across** — that is the v1 trust strip
that is being deleted. Mobile: one column, four rows, numeral 48 px.

**Motion.** The four numerals light in reading order, 120 ms apart.

**Schema.** `eyebrow` · `heading` · `deck` · blocks `number` (max 4: `numeral`, `unit`, `headline`, `sub`,
`link_label`, `link_url`) · `foot_links` (richtext).

---

### 4.7 `elmsnest-v2-pdp-ask` — the specialist line + the small step · `#env2-pdp-ask`

**Purpose.** Spine #7 and #8 in one screen. One quiet line, one link, no table, no competitor — and the two
ways to not-buy-yet.

**Copy.**
- eyebrow `07 · למה כאן`
- h2: `עוד לא בטוחים?` / *(glow)* `לא צריך להיות.`
- lead: `אמרנו למעלה מתי היא לא מתאימה. המפרט בעברית, ומה שלא ידוע — לא כתוב. ולפני שמזמינים יש למי לשלוח
  תמונה, או להתחיל מהאורך הקצר.`
- quote (FRL 400, on a hairline): `«כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה.»`
  cite: `מתוך «מי אנחנו»` + link `מי אנחנו ←` → `/pages/about-us`
- ghost CTA: `לשלוח תמונה של המקום` →
  `mailto:info@elmsnest.com?subject=בדיקת%20התאמה%20למקום&body=שלום%2C%20אשמח%20לבדוק%20התאמה%20—%20מצרפ%2Fת%20תמונה%20של%20המקום.`
- primary CTA (A): `להתחיל מ־5 מטר — 89.90 ₪` → selects ledger row 1 and scrolls to `#env2-pdp-stage`
  (no-JS: it is an `<a href="#env2-pdp-ledger">`). B: `להתחיל מיחידה אחת — 169.90 ₪`. C: `להתחיל מ־6W — 219.90 ₪`.

**The mailto rule (binding until a number exists).** `settings.whatsapp_number` stays the switch. While it is
empty **every** photo-check CTA is the mailto above, and no string on the page may contain `וואטסאפ`. When the
number is filled, the same snippet swaps to the `wa.me` URL from `CONTRACT.md` without touching any section.
One snippet: `snippets/elmsnest-v2-pdp-photo-cta.liquid`.

**Layout.** `grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr); align-items:end;
gap:clamp(30px,6vw,100px)`: h2 + lead + the two CTAs at the start side, the quote at the end side.
`padding-block:100px`. Mobile: stacked, quote last, CTAs full width.

**Schema.** `eyebrow` · `heading_line1` / `heading_line2` · `lead` · `quote` · `quote_cite` · `quote_link_label`
/ `quote_link_url` · `photo_cta_label` · `mailto_subject` · `mailto_body` · `start_small_label` ·
`start_small_target` (select: `first_row` / `url`).

---

### 4.8 `elmsnest-v2-pdp-related` — the related module + the product card · `#env2-pdp-related`

**Purpose.** Spine follow-through, and **this card becomes the catalogue card in round 2.** Design it once,
here.

**Copy.** eyebrow `08 · עוד למרפסת` (place-driven) · h2 `עוד שלושה שיוצרים אווירה` ·
deck (graft G): `מאותו מקום — מרפסת ופינת ישיבה. מחיר אחד לכל אחד. בלי כוכבים ובלי «נמכר ביותר» — אין לנו
עדיין מה למדוד.` · closing link `לכל הגרילנדות והתאורה הדקורטיבית ←`

**The card spec (binding).**
```
figure  [data-lamp]  radius 0, aspect from the block (staggered, never equal cells)
        pool glow under the photo (switch/switch.css:254)
kicker  11.5px tracked gold — "<place> · <approved suits phrase>"
h3      Heebo 400 15px/1.35, unicode-bidi:isolate      ← never the serif
row2    price (FRL 500 21px glow, via elmsnest-v2-price)   ·   action
action  1 available variant → <form> ATC "הוספה לסל"
        else                → ghost link "לבחירת אורך" / "לבחירת דגם" / "לבחירת גוון"
```
- **Price rule** (`elmsnest-v2-price.liquid`, unchanged): single → `169.90 ₪`; narrow range
  (`max ≤ min×1.25`) → `219.90–252.90 ₪`; else → `מ־89.90 ₪`.
- **Forbidden on the card:** badges, sale flags, strikethrough, stars, review counts, swatch rows, quick-add
  icons, hover-swap second image, "N נמכרו", countdowns, rounded corners.
- **Widths are staggered, not equal:** `300px / 210px / 260px` at aspects `1/1.05`, `1/1.4`, `1/.9`
  (`switch/switch.css:255–258`). Three cards, never four — §11.
- **Image index per card** = `card_image_index` (1-based, default 2 for a never-use handle, else 1), resolved
  through `elmsnest-v2-pdp-image.liquid` (§3.5).

**Layout.** Head as a `space-between` flex row; the three cards on a baseline-staggered flex line with
`align-items:flex-end` and per-card `--ow`/`--ar`. Mobile: horizontal scroll-snap row, card width 62vw.

**Schema.** `eyebrow` · `heading` · `deck` · `collection` (collection picker, default = the product's place
collection) · `product_1..3` (product pickers, empty = auto-fill from the collection excluding the current
product) · per-card `card_image_index` · `card_action_label` · `link_label` / `link_url`.

---

### 4.9 `snippets/elmsnest-v2-pdp-buybar.liquid` — the sticky mobile bar

Rendered by §4.1, `<= 900px` only, `position:fixed; inset-inline:0; bottom:0; z-index:60`,
`background:rgba(4,6,11,.84) + backdrop-filter:blur(14px)`, hairline top, `transform:translateY(105%)` →
`.show` when the stage buy line leaves the viewport (`switch/switch.js` `stickyBar`, lines 201–219).

Contents, in RTL order: 46 px product thumb (§3.5) · title (one line, ellipsis, 14 px) + selection mirror
(13 px) · price 22 px · `הוספה לסל` pill. It **mirrors the selected variant** — the one place a thumbnail
belongs (§1). `body{padding-block-end:var(--env2-pdp-bar-h,0)}` so it never covers the footer. It is full
width, so it does not collide with the WhatsApp float's bottom-left corner. Hidden on desktop; hidden when
`#env2-pdp-stage`'s buy line or `#env2-pdp-ledger` is on screen (no double button).

---

## 5. `templates/product.json` — sections, order, and what dies

**New template** `templates/product.json` (the default; `product.elmsnest.json` is deleted, not orphaned):

```json
{
  "sections": {
    "pdp_stage":   { "type": "elmsnest-v2-pdp-stage" },
    "pdp_fit":     { "type": "elmsnest-v2-pdp-fit" },
    "pdp_night":   { "type": "elmsnest-v2-pdp-night" },
    "pdp_ledger":  { "type": "elmsnest-v2-pdp-ledger" },
    "pdp_facts":   { "type": "elmsnest-v2-pdp-facts" },
    "pdp_terms":   { "type": "elmsnest-v2-pdp-terms" },
    "pdp_ask":     { "type": "elmsnest-v2-pdp-ask" },
    "pdp_related": { "type": "elmsnest-v2-pdp-related" }
  },
  "order": ["pdp_stage","pdp_fit","pdp_night","pdp_ledger","pdp_facts","pdp_terms","pdp_ask","pdp_related"]
}
```

**Spine order note (required by BRIEF §4).** The spine's #6 is answered twice on purpose: a one-line terms
strip **inside the buy box** (§4.1, graft F) and the full ledger at position 6. The compact answer must be
next to the button; the full one must not push the ledger below 6,000 px.

**Files to create.**
```
sections/elmsnest-v2-pdp-stage.liquid
sections/elmsnest-v2-pdp-fit.liquid
sections/elmsnest-v2-pdp-night.liquid
sections/elmsnest-v2-pdp-ledger.liquid
sections/elmsnest-v2-pdp-facts.liquid
sections/elmsnest-v2-pdp-terms.liquid
sections/elmsnest-v2-pdp-ask.liquid
sections/elmsnest-v2-pdp-related.liquid
snippets/elmsnest-v2-ground-product.liquid   (the §3.1 gradient, mirrors elmsnest-v2-ground-index)
snippets/elmsnest-v2-pdp-image.liquid        (§3.5 index resolver + never-use guard)
snippets/elmsnest-v2-pdp-variants.liquid     (builds the ledger model from product.variants, once)
snippets/elmsnest-v2-pdp-buybar.liquid       (§4.9)
snippets/elmsnest-v2-pdp-photo-cta.liquid    (mailto now, wa.me when settings.whatsapp_number fills)
snippets/elmsnest-v2-pdp-card.liquid         (§4.8 — reused by the collection template in round 2)
templates/product.json
```
Reused unchanged: `elmsnest-v2-fonts` · `elmsnest-v2-base` (guard widened to `hdt-page-type-product`) ·
`elmsnest-v2-price` · `elmsnest-v2-buy`.

**Retire (delete from the template; delete the files once the preview is signed off).**

| What | Action |
|---|---|
| `templates/product.elmsnest.json` | delete |
| `main-product` + every `_product-*` / `_group-product` / `_product_sidebar` block | removed from the template (§3.4) |
| `breadcrumb` (`brc-nav-product`) | removed — it carries its own colour scheme and paints above the stage |
| `elms-pdp-trust-strip` | delete — 4-boxes-in-a-row; its wording lives on in §4.6 |
| `elms-pdp-description` | delete — cream, 2×2 card grid; replaced by §4.5 |
| `elms-pdp-night-gallery` (`elms_showcase`) | delete — replaced by §4.3 |
| `elms-pdp-installation` | delete — solar-only copy on mains products |
| `elms-pdp-comparison` | delete — **the comparison table is dead** (BRIEF §11) |
| `elmsnest-product-guidance` | delete — template copy identical on 27 products |
| `elms-pdp-faq` | delete — renders empty; the three authored Q&As move to `custom.faq` for a later round |
| `elms-pdp-warranty-shipping` (`elms_policy`) | delete — wording preserved in §4.6 |
| `related-products` (Kalles) | replaced by §4.8 |
| `elms-pdp-reviews` (theme-src, unused) | **do not revive** |
| `snippets/elmsnest-pdp-facts.liquid`, `-trust.liquid` | **copy the licensed wording into §4.6 first**, then delete; they also load `assets/elmsnest-pdp.css`, which must stop loading (it paints `.elms-pdp-section` cream / `#12100e`) |
| `snippets/elmsnest-pdp-price.liquid` | delete — the `hdt-price` DOM clone is obsolete under §3.4 |
| `snippets/elmsnest-pdp-specs.liquid`, `-not-fit.liquid`, `-direct-answer.liquid` | delete the snippets, keep the **metafield keys** — §4.2 and §4.5 read them directly |
| `assets/elmsnest-pdp.css` | delete after confirming nothing else loads it |

**The description (`.elms-sales` HTML) — decision: parse, and preserve the original behind a hairline
`<details>`.**

Not "restyle in place": the description's own marketing headings ("הפכו את החלל מרגיל לחגיגי…") duplicate our
headlines in the old voice, and its 2×2 bordered card grid is one of the four-in-a-row violations we are
deleting. Not "discard" either — the owner's instruction is to keep the copy asset.

So, in `elmsnest-v2-pdp-facts.liquid`:
```liquid
{%- assign raw = product.description | strip_html | strip -%}
{%- assign parts = raw | split: 'פרטים שכדאי לדעת' -%}
{%- if parts.size > 1 -%}
  {%- assign bullets = parts[1] | split: '•' -%}   {%- comment -%} → the dl rows, trimmed, empty dropped {%- endcomment -%}
{%- endif -%}
```
- The bullets become the `<dl>` in §4.5. Trim, drop empties, drop the trailing CTA sentence (the text after
  the last bullet with no `•`).
- The **advice paragraph** — the one immediately before `פרטים שכדאי לדעת` — becomes the §4.4 ledger lead
  ("מדדו את אזור התלייה…", "יחידה אחת מאירה נקודה…", "בכניסה צרה אפשר להסתפק ביחידה…"). It is the specialist
  speaking; it is the best sales copy the owner already owns.
- **Fallback chain** for the five products with no `.elms-sales` bullet list (`METAFIELD-SHEET` §8):
  bullets → `custom.*` spec metafields → nothing (the `dl` drops; the giant numeral and the `מה שלא כתוב`
  row still render).
- The full original renders inside `<details><summary>כל מה שכתוב על המוצר</summary>{{ product.description }}`,
  with CSS scoped to `.env2-pdp-facts__more` overriding `.elms-sales`: colours → `--env2-ink`/`--env2-ink-2`,
  every background → `transparent`, every border → the hairline, every radius → `0`, headings → Heebo (never
  the serif), the black "פרטים" panel → hairline rows. ~30 lines of CSS, no Liquid inside `{% stylesheet %}`.
- **Nothing on the visible page is typed.** Every number in §4.4 and §4.5 comes from `product.variants` or the
  parsed bullets.

**Metafields.** `METAFIELD-SHEET.md` is approved-and-then-written, per `OWNER-NOTES` §4 — writing is a
separate task and nothing here writes it. The sections must render correctly with every `custom.*` field
empty (that is the state today on 26 of 27 products): `not_fit_for` empty → no negative (§3.7);
`power_source` empty → no power sentence; `direct_answer` empty → the authored lead; `faq` empty → no FAQ.

---

## 6. The do-not list for this build

1. **No cream, beige or brown anywhere** — including anything `assets/elmsnest-pdp.css` used to paint
   (`#fffdf7`, `#12100e` as a "night" surface). Grounds are §3.1's two values only.
2. **No four of anything in a row.** The colour axis is a select (§3.6); the terms are a 2-column ledger; the
   related module is three staggered cards. If a grid of equal cells appears, it is wrong.
3. **No comparison table, no competitor claim, ever.** The v1 "מנורה גנרית זולה" table is deleted, not moved.
4. **No reviews, stars, counts, "נמכר ביותר", countdowns, "נותרו N", urgency, or fake scarcity.** One test
   order exists in the store's history.
5. **No sale UI:** no badges, no strikethrough, no `-N%`, no `compare_at` rendering.
6. **No typed facts.** Numbers come from `product.variants` or the parsed bullets. **No coverage claim** —
   `5 מטר מכסים פינה אחת` is deleted; the ledger's `__use` captions are quoted from the description.
7. **No solar copy on a product whose `power_source` is not `סולארי`**, and **no mains copy on a product
   whose `power_source` is empty** (§3.7 — this is C today).
8. **Never write a new negative.** Only the four approved pairs, verbatim, and only where literally true.
9. **No "בוואטסאפ"** in any string while `settings.whatsapp_number` is empty. The label is
   `לשלוח תמונה של המקום`.
10. **No one-value picker.** B's single `צבע אור` is a printed fact, not a control.
11. **No price that hides the range.** A resolved price plus the honest range line, in the fold, on both
    viewports. `מ־89.90 ₪` alone is not a fold.
12. **No product title in the serif**, no headline in Heebo, no Assistant as a display face.
13. **No `[data-lamp]` that starts lit under `html.env2-js`**, and none that stays dim without the guard.
    No-JS = everything lit and every ledger row buyable.
14. **No box, no rounded tile, no card grid.** Radius 0 everywhere except pill buttons (999 px) and the
    toggle knob. The scrim is the only card surface, used twice.
15. **Nothing fixed bottom-left** (the WhatsApp float lives there). The sticky bar is full-width bottom.
16. **No image at index 0 for a never-use handle**, and no crop that lets a baked caption survive — check
    every gallery tile at 1× and 2×.
17. **No `<bdi>` split across a slash pair.** `<bdi>6W/12W</bdi>`, one element.
18. **No caption under 13 px**, no tap target under 44 px, no horizontal page scroll at 360 px.
19. **No text fade-ins, no parallax, no autoplay, no marquee, no emoji, no English UI strings, no lorem.**
20. **Do not reuse a layout.** Stage (photo + buy) · fit (toggle + question) · night (two staggered figures) ·
    ledger (rows on hairlines) · facts (giant numeral + `dl`) · terms (2-column ledger) · ask (quote split) ·
    related (staggered cards). Eight compositions, eight shapes.

---

## 7. References — what to lift, and from where

**Primary source: `brief/side-pages/pdp/concepts/switch/`**

| What | File : lines |
|---|---|
| Tokens, `.wrap`, `.eyebrow`, `.kicker`, `.h`, `.lead`, `.ptitle`, `.price`, `.btn*`, `.link`, `.hair` | `switch.css:1–48` |
| `[data-lamp]` dim→lit (photo brightness + halo) | `switch.css:50–56` |
| Stars layer | `switch.css:58–72` |
| Transparent header strip over the stage | `switch.css:74–83` |
| The drawn string (cord, bulb halo/core, `.dark`, `.try` flicker) | `switch.css:85–95` |
| Stage grid, veil, buy column, colour axis | `switch.css:97–124` |
| **The rail** (stops, fill hairline, per-stop price) | `switch.css:125–139` — rebuild the mobile case per §4.1 |
| **The toggle** (3-col grid, knob, `.off` state) | `switch.css:141–161` |
| Night gallery | `switch.css:162–175` |
| **The ledger rows** | `switch.css:176–201` + markup `index.html:121–160` (the per-variant forms are the contract) |
| Facts: giant outline→glow numeral + `dl` | `switch.css:202–216` |
| Terms 2-column ledger | `switch.css:218–232` |
| Ask: quote, CTA pair | `switch.css:234–244` |
| Related: staggered `.obj` cards + pool glow | `switch.css:245–265` |
| Sticky buy bar | `switch.css:280–288` |
| Reduced motion | `switch.css:290–297` |
| Mobile recomposition (not a collapsed grid) | `switch.css:302–400` |
| Wall halo stage (6W/12W, 3000K/6000K) | `switch.css:444–466` |
| SVG string builder | `switch.js:41–126` (`makeString`) |
| SVG receding-path builder (product B) | `switch.js:127–186` (`makePath`) |
| Price count-up | `switch.js:187–200` (`fmt`, `countTo`) |
| Sticky bar controller | `switch.js:201–219` |
| No-JS form handling / anchors | `switch.js:220–243` |

**Graft sources**

| Graft | File : lines |
|---|---|
| A — ledger use-captions | `concepts/dialogue/index.html`, beat 04 rows (`shot-desktop.png` slice 4) |
| B — the solar place question | `concepts/place/index.html` screen 02 (`shot-desktop.png` slice 2) |
| C — quantity meanings | `concepts/ledger/path.html` fold rows (`shot-path-desktop.png` slice 1) |
| D — the wall diptych | `concepts/walk/wall.html:414` (collection scene) + `:441` (product close-up); `shot-wall-desktop-fold.png` |
| E — guillemet section heads | `concepts/dialogue/index.html` beats 01–08 |
| F — terms strip + `למי זה לא מתאים` | `concepts/ledger/index.html` screen 1 (`shot-mobile-fold.png`) |
| G — related deck | `concepts/place/index.html` screen 05 |
| H — terms head + deck | `concepts/ledger/index.html` screen 5 |

**Data and plumbing**

- `brief/side-pages/pdp/products.json` — variants, prices, option names/values, `description_text`.
- `brief/side-pages/pdp/metafields.json` + `METAFIELD-SHEET.md` — `custom.*` proposals; **read §2, §5, §8,
  §11, §12 before writing §3.7's branch or §4.5's fallback chain.**
- `brief/build-preview/CONTRACT.md` — section root, tokens, shared classes, `[data-lamp]`, `window.env2`,
  snippet signatures. Do not restyle a shared class.
- `brief/WINNING-SPEC.md` §3 — palette, type, spacing, motion, the never-use image list.
- `brief/inventory/AUDIT-product.md` §§3, 5–11, 175–182 — what is being replaced, the two global bugs, and
  the three hardest constraints.
- Screens this spec was checked against: all twelve PNGs of `switch`, plus the folds and desktop slices of
  `place`, `dialogue`, `ledger`, `walk`.

**Before sign-off, re-shoot and check:** `node brief/shot.js <file> <prefix>` at 1440×900 and 390×844 for
index / path / wall, and confirm (1) `הוספה לסל` bottom edge < 700 px on 390, (2) the toggle inside the
second screen, (3) no caption under 13 px, (4) the dark state genuinely dark in the still, (5) no horizontal
scroll at 360 px, (6) `6W/12W` renders in that order.

---

## 8. Addendum — corrections issued by the lead before the build (2026-09-02)

**8.1 The template file is `templates/product.elmsnest.json`, not `templates/product.json`.**
All 27 products carry `templateSuffix: "elmsnest"` (verified read-only against the Admin API on 2026-09-02).
`templateSuffix` is a property of the **product**, shared by every theme, so changing it would immediately change
which template the **published** theme renders — a live-store change this round is forbidden from making. Therefore:

- Write the new section list into `templates/product.elmsnest.json` on the dev theme (replace its contents).
- Do **not** create `templates/product.json`, do **not** delete `product.elmsnest.json`, and do **not** touch any
  product's `templateSuffix`.
- §5's JSON body is otherwise correct (same eight sections, same order, same ids).
- The old sections (`elms-pdp-*`, `elmsnest-product-guidance`, `brc-nav-product`, `main-product`) leave the template
  but their **files stay on the theme** until the owner signs off the preview; nothing is deleted this round.

**8.2 The base guard.** §5 says `elmsnest-v2-base` is reused "guard widened to `hdt-page-type-product`". That snippet
is now a 344-byte deprecation stub — round 0 replaced it with `snippets/elmsnest-v2-core.liquid`, which is rendered
from `layout/theme.liquid` on **every** template and already carries the tokens, the fonts, `[data-lamp]`,
`window.env2`, the buttons and the side-page ground. So: render nothing global from the PDP sections; assume the core.
`snippets/elmsnest-v2-ground-product.liquid` (§5) is still needed for the PDP's own §3.1 ground and must be rendered
by `elmsnest-v2-pdp-stage` only, exactly as the hero renders `elmsnest-v2-ground-index`.

**8.3 Known core bug the stage must not inherit.** `.env2-section a{color:inherit}` outranks
`.env2-btn{color:var(--env2-btn-ink)}`, so an **anchor** styled as a primary button renders ink-on-glow at 1.21:1
(REPORT §9.1). Until the lead approves the one-line core fix, every primary call to action in the PDP sections must be
a `<button>` inside a form, or must set its own colour explicitly (`.env2-pdp-…__btn{color:var(--env2-btn-ink)}`).
Check the computed colour in the render; do not assume.

**8.4 Notice colours.** `--en-warning-text` / `-success-` / `-error-` / `-info-` are still cream-era on the night
ground (REPORT §9.2). No PDP section may use them; write your own state colours from the env2 palette.
