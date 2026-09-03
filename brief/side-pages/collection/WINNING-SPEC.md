# ElmsNest collection page v2 — WINNING SPEC (build-ready)

Design-lead decision, 2026-09-03. Read after `BRIEF.md`, before any Liquid is written.
Winner: **evening (ערב אחד)** — its staging, its ground, its card-in-the-scene fold — with the **narrowing
mechanism rebuilt from `howmuch`**, the **price ladder from `switchboard`**, the **14× sentence from `index`**,
and the **place question from `places`**.

Reference mockups: `concepts/evening/{index,path,all}.html` + `evening.css` + `evening.js` (lift; §7).
Binding upstream: `brief/WINNING-SPEC.md` §3 · `brief/side-pages/pdp/WINNING-SPEC.md` §3.5, §3.6, §4.8 ·
`brief/build-preview/CONTRACT.md` · `brief/side-pages/core/REPORT.md` §9 · `brief/side-pages/OWNER-NOTES.md`.

---

## 1. The one idea, and the ruling

### The idea

**The collection page is one evening in one garden, and the evening is measured.**

You scroll from the gate to the table. Every lamp appears *pinned* — a lit dot, a hairline stem, a gold tag —
to the place in the photograph where it would actually stand, and its card rises out of that photograph.
That is `evening`, and it is the only device in the round that a lighting shop could invent and that a judge
can read in a still with nothing clicked.

But a picture of an evening does not narrow seven lamps to two. So the evening is laid on **one ruler**, in
the unit the buyer already owns — **metres of string, points of light along a path, a price rung** — and a
row of unit pills drops a **glowing cursor** on that ruler. Tap `10 מ׳` and five ranges collapse into four
comparable, priced offers; the garland that cannot reach dims and prints `האורך המרבי: 8 מ׳` instead of
vanishing. That is `howmuch`, and it is the only mechanism in the round that produces an **answer** rather
than a shortlist.

The evening is the desire. The ruler is the decision. Neither ships alone.

### The ruling, and why

Both panels ranked **evening** first (8.48 / 8.45 aggregate over `howmuch`), and the pixels agree with them
on the thing that carries 35 of 100 points: **`shot-mobile-fold.png`, `shot-path-mobile-fold.png` and
`shot-all-mobile-fold.png` each put a full-bleed lit scene, the collection name, one named lamp, a real price
and a live buy control inside 844 px — on all three URLs, on both viewports.** No other concept does that on
even two URLs. `howmuch`'s `shot-all-mobile-fold.png` opens the whole catalogue with three numerals and no
product photograph at all — the exact audit fault (§4.1) this round exists to kill, transplanted to `/all`.

But the instruction is explicit: *a page that does not let a phone visitor narrow the set cannot win.*
Evening, as mocked up, narrows by **anchor-jumping to a station** — that is navigation, not narrowing — and
its one real narrowing instrument, the 14-row metre ledger, sits at ~5,500 px on desktop and ~5,000 px on a
6,944 px phone page, with the `?sort_by=` line stranded below it at line 236 of 287. **So evening does not
win as drawn.** It wins with `howmuch`'s cursor moved into the second screen and made the page's spine
(§3.4, §4.2). That is the ruling: evening's staging, howmuch's instrument, and the ledger promoted from
footnote to destination.

### Where I disagree with the panel (I checked the pixels and the assets)

1. **The image problem is far worse than any concept or judge assumed, and it changes the build.**
   I built contact sheets of `brief/assets/img/<handle>-{0,1,2,3}.jpg` for all 27 products.
   **Fifteen products have no clean photograph at *any* of indexes 0–3** — every one is a full marketing
   poster with baked Hebrew headlines, spec icon rows and cream/beige grounds. The whole
   `ספוטים-ופרוז-קטורים-סולאריים` collection is in this state except one product.
   `modern-led-bollard-light-5w-ip65` carries **three different third-party wordmarks across its four
   images** — `LUMIÈRE` [0], `LUMORA` [1], `LUMIRA` [2] — which is worse than the homepage ledger records.
   The PDP spec's "silently step to index 1" resolver (`pdp/WINNING-SPEC.md` §3.5) is therefore **not
   sufficient here**: the PDP needs one clean image for one product; the collection page needs one for
   twenty-seven. §3.6 makes `howmuch`'s drawn glyph plate the house rule, not a fallback.
2. **The merchandiser judge's `dual-head-garden-light-10w-ip65` violation against evening is wrong on the
   ledger's own wording** — `brief/WINNING-SPEC.md` §3.6 bars *images[1–3]* for that handle, so `[0]` is
   permitted. But `[0]` is a black bollard on a **cream studio ground**, which §3.1 does bar. The right
   index is `[2]` (the same lamp, at night, warm). Ruled: `[2]`.
3. **A breach on evening that the panel missed.** `all.html`'s terrace band renders
   `decorative-led-net-lights` with its baked caption strip legible along the top edge
   (`shot-all-desktop.png`, terrace band; "מתאימה לעיצוב גינה, שבילים ופינות ישיבה…"). Do-not #7. Fixed by
   §3.6 — that handle gets the glyph plate, not a crop.
4. **`howmuch` puts `decorative-led-net-lights` on the metre rail at `12×2 מ׳`.** That product is sold by
   **area**, not by length; a row that says "reaches 12 m" for a net is a false row. Evening's ledger
   footnote is the honest treatment and the graft must carry it (§4.5, non-negotiable 3).
5. **Evening's five/four station names are the one thing that must not ship.** `מעל השולחן`, `בערוגה`,
   `על הגדר ברוחב` exist in no Shopify field; shipping them means a new per-product metafield and a merchant
   who hand-places every new lamp. **They are replaced by the ruler's own bands** (§4.3) — measurements, which
   the store *does* hold, in the same numbered, full-bleed, scene-per-band composition. The poetry moves to
   the **pin tag**, which prints the lamp it points at and its real value (`כדורי קריסטל · 5 מ׳`) — already
   real data, already drawn in evening's `02` scene. Zero new data dependencies. This is the single change
   that turns the winner from a mockup into a template.
6. **The panel treated "one ruler per collection" as universal. It is not.** For `decor` and `path` the first
   option axis is a real measured scale. For `wall` and `spot` it is **colour** — and there is no shared
   numeric axis in either collection (verified: wall's price-bearing axis is `עוצמה` on one product, `כמות`
   on two, `סוג גוף` on one; spot has none at all). `places` printed wall and spot questions it could not
   answer; this spec refuses to. §3.4 gives the ruler **four unit modes, the fourth of which is the price
   rung ladder**, and wall and spot ship in that mode.

### One line per concept, as it goes to the owner

- **evening** — the winner: the only page whose first screen is a lit garden with a lamp, a price and a
  buy button, on all three URLs and both viewports; its weakness is that it looks rather than answers.
- **howmuch** — the best instrument in the round and the coldest shop; its cursor is grafted in whole.
- **index** — the most intelligent document, the least desirable page; it explains the 14× gap better than
  anyone, in one sentence, and we take the sentence.
- **places** — the sharpest opening line (the place asks its own question) attached to the worst first
  screens; we take the question and refuse the two questions it could not answer.
- **switchboard** — one superb screen (the price ladder) inside a settings panel; the ladder is grafted, the
  rockers are not, and it renders images[0] of five never-use products.

---

## 2. Grafts (device → where it lands)

| # | From | Device | Lands in |
|---|------|--------|----------|
| **C1** | `howmuch` | The **unit pill row** (`הכול · 3 · 6 · 10 · 15 · 22 · 30 מ׳`) that drops a glowing cursor on the rail and collapses every row from a range to one real priced answer; the lamp that cannot reach **dims to .4 and prints `האורך המרבי: 8 מ׳`** rather than disappearing | §4.2 `elmsnest-v2-coll-ruler` — the page's second screen and its spine |
| **C2** | `howmuch` | The **derived per-unit line** at the chosen stop — `≈37.48 ₪ לנקודת אור`, `≈29.16 ₪ ליחידה` — labelled as derived | §4.2 row 3, §4.4, §4.5 |
| **C3** | `howmuch` | The drawn **light-glyph plate** captioned `איור · אין תצלום נקי` for a product with no text-free photograph at any index | §3.6 — promoted to **house rule** |
| **C4** | `index` | The **14× sentence**, verbatim: `המוצר היקר בקולקציה עולה פי 14 מהזול — לא כי הוא מנורה טובה יותר, אלא כי הוא סט של 8 יחידות.` | §4.4 deck, inside the path fold's second screen |
| **C5** | `index` | The **high table of contents** on `/collections/all` — entries with count, price span and first three product names, anchored — **with the `?sort_by=` line on the same hairline** | §4.2 `/all` variant; fixes evening's stranded ordering |
| **C6** | `switchboard` | `path.html`'s **one-screen price ladder**: one rung per product, bar solid to `price_min`, hairline onward to `price_max`, banded | §4.4 `elmsnest-v2-coll-span` |
| **C7** | `places` | **The place's own question as the display headline** — `כמה נקודות אור צריך השביל?` / `כמה מטר צריך לכסות?` — and the four questions as the four doors of `/all` | §4.2 h2; §4.3 `/all` variant |
| **C8** | `places` | The homepage's own place phrase + the **approved suits/doesn't-suit pair** immediately under the h1 | §4.1 |
| **C9** | `switchboard` | The `לא צוין` bucket **carried with a real count** rather than hidden | §4.2 rail foot |
| **C10** | `evening` (own, kept) | The **pin**: lit dot + hairline stem + gold tag on the photograph, tag = the lamp and its real value | §4.1, §4.3 |

**Not grafted, deliberately:** switchboard's rocker glyphs and pip matrices (skeuomorphic UI kit — the
homepage spec already refused them, `brief/WINNING-SPEC.md` §2 closing line); index's 56–120 px photo slivers;
places' photo-left/boxed-ladder-right repetition; evening's invented station taxonomy; howmuch's
starting-price budget stops (§6.7).

---

## 3. Global decisions for the collection page

### 3.1 The ground — a photo, then a sky that does not care how long the page is

The homepage is a sunset over eight fixed sections. The PDP is already night. **The collection page is night
too, but its length is unknown** — 6 products (1 screen) to 27 (4 screens). A percentage-stop gradient would
put "deep night" at 30 % of a short page and at 78 % of a long one.

**Decision: the gradient is measured in `px`, not `%`, so every page reaches full night at the same distance
and then stays there.**

```css
html{background:#020306}
body.hdt-page-type-collection{
  background:
    linear-gradient(180deg,
      #0b1526 0px,
      #0a1120 620px,
      #080e1c 1500px,
      #060a14 2600px,
      #04070e 3800px,
      #020306 5000px) no-repeat,
    #020306;
  background-size:100% 100%;
}
.hdt-page-type-collection #wrapper,
.hdt-page-type-collection .main-content,
.hdt-page-type-collection main{background:transparent}
```

- Lives in a **new snippet `snippets/elmsnest-v2-ground-collection.liquid`**, mirroring
  `elmsnest-v2-ground-product.liquid`, rendered **only by `elmsnest-v2-coll-scene`** (§4.1). Do not re-render
  the core, do not redefine its tokens (`core/REPORT.md` §9 and PDP §8.2 — `elmsnest-v2-base` is a 344-byte
  deprecation stub; assume `elmsnest-v2-core.liquid`, which `layout/theme.liquid` renders on every template).
- **Screen 1 is a photo ground**, not the gradient: full-bleed `collection.image` at `min-height:100svh`
  desktop / `78svh` mobile, bottom ~26 % blended into `--env2-sky-2` by the two-stop veil.
- No section paints a background. The only card surface anywhere is the scrim
  `rgba(5,8,14,.55)` + `backdrop-filter:blur(10px)` — used exactly twice: the pinned card on the scene (§4.1)
  and the card riding a band photo (§4.3).
- Stars (`.env2-stars`, per-section `--st`): scene `0` (photo) → ruler `.28` → bands `.34` → span `.42` →
  ledger `.48` → terms `.55` → goodnight `.70`.
- **Palette is `brief/WINNING-SPEC.md` §3.1 verbatim.** `--env2-sky-2 #0f1a2f`, `--env2-sky-4 #020306`,
  `--env2-ink #f4eee3`, `--env2-ink-2 #c9c4b8`, `--env2-mute #8f95a3`, `--env2-gold #e9b96e`,
  `--env2-glow #ffd394`, `--env2-btn-ink #1a1206`, hairline `rgba(244,238,227,.12)`, button hairline `.25`,
  numeral outline `.45`. **No brown, no beige, no cream, on any surface, including a photograph's own ground
  (§3.6).** Gold is an accent; its maximum surface is a pill button.
- Radius `0` on every image, plate, rail, row and input. `999px` only on pill buttons and the cursor knob.
  Logical properties only (`inset-inline-*`, `margin-inline`, `padding-inline`) — the Sense RTL app flips
  physical ones.
- Container `.env2-wrap{width:min(1240px,100% - 2*var(--env2-gut))}`; band scenes and the scene are
  full-bleed; the ruler rail is `min(1500px,100% - 2*gut)`.
- Section padding-block: desktop `120px / 96px`, mobile `72px / 56px`. Every section root carries
  `id="env2-coll-<name>"` and `scroll-margin-top:90px`.

### 3.2 Type

Faces and tokens inherited (`brief/WINNING-SPEC.md` §3.2): `--env2-serif` Frank Ruhl Libre 500/700/900,
`--env2-sans` Heebo 300/400/500. **Product titles are never in the serif. Headlines are never in Heebo.**
Hebrew display leading `.98`, `letter-spacing:-.01em`, `text-wrap:balance`.

| Role | Face / weight | 1440 | 390 | CSS |
|---|---|---|---|---|
| h1 — collection title (scene) | FRL 700 | 84 | 38 | `clamp(38px,5.8vw,84px)`, lh .98, line 2 in `--env2-glow` |
| h2 — the place's question (ruler) | FRL 700 | 72 | 34 | `clamp(34px,4.9vw,72px)`, lh .98 |
| h2 — band headline | FRL 700 | 60 | 30 | `clamp(30px,4.2vw,60px)`, lh 1.0 |
| pull quote (band 03) | FRL 400 | 46 | 26 | `clamp(26px,3.4vw,46px)`, lh 1.2 |
| count numeral (ruler) | FRL 900 | 150 | 88 | `clamp(88px,10vw,150px)`, tabular, outline `1px rgba(244,238,227,.45)` → glow fill when lit |
| band numeral `01`–`05` | FRL 900 | 96 | 56 | `clamp(56px,6.6vw,96px)`, tabular, `--env2-gold` |
| ledger row numeral (`10 מ׳`) | FRL 500 | 44 | 32 | `clamp(32px,3vw,44px)`, tabular; unit at `.32em` |
| rail stop numeral | FRL 500 | 15 | 13 | tabular, `--env2-mute` |
| price — pinned card | FRL 500 | 34 | 30 | tabular, glow, `white-space:nowrap` |
| price — ruler row / band card | FRL 500 | 22 | 20 | tabular, glow |
| price — ledger cell | FRL 500 | 17 | 16 | tabular, glow |
| lead / deck | Heebo 300 | 17–20 | 16 | `clamp(16px,1.4vw,20px)`, 38–44ch, `--env2-ink-2` |
| product title | Heebo 400 | 19 | 16 | `clamp(16px,1.3vw,19px)`, `unicode-bidi:isolate` |
| axis caption / per-unit line | Heebo 300 | 15 | 14 | `--env2-ink-2` |
| any information-bearing caption | Heebo 300 | ≥14 | **≥13** | hard floor, no exceptions |
| kicker / axis label / pin tag | Heebo 500 | 11.5 | 11.5 | `letter-spacing:.16em`, gold; labels only, never data |
| button | Heebo 500 | 15 | 14 | min tap target 48 px (44 px absolute floor) |

`<bdi>` on every Latin token and every price: `<bdi>179.90</bdi> ₪`, `<bdi>IP65</bdi>`, `<bdi>3000K</bdi>`.
**A slash-joined pair goes inside ONE `<bdi>`** — `<bdi>6W/12W</bdi>`, `<bdi>1/4/8/12</bdi>`, never split
(under RTL a split pair renders reversed; this is a live bug in the current theme's card titles, AUDIT §2e).

### 3.3 Motion

Inherited: `[data-lamp]` starts dim under `html.env2-js`, lights once at 25 % visibility
(`rootMargin:'0px 0px -6% 0px'`), never re-dims. **No-JS / JS-failed / reduced-motion = everything lit and
every row buyable.** Lift `evening.js` whole (22 lines: IO + `load`/`scroll` sweep) — it is already the
CONTRACT's shape; it must end with
`window.env2 ? env2.observe(root) : root.querySelectorAll('[data-lamp]').forEach(l=>l.classList.add('lit'))`.

**Exactly one thing switches on per section, and it is the thing the section is about:**

| Section | What lights | Timing |
|---|---|---|
| scene | the pin — dot, then the stem draws from the dot to the tag | dot `.5s`, stem `scaleY` `.45s` `.15s` delay |
| ruler | the cursor travels to the chosen stop; the matching dot on each row scales to 1.5 and takes the glow halo | `inset-inline-start .32s cubic-bezier(.2,.7,.2,1)`; dot `.25s` |
| ruler — unreachable row | opacity to `.4` and the `האורך המרבי` line fades in | `.28s`; **never `display:none`** |
| bands | the band's scene photograph, then its card | photo on arrival, card `+.2s` |
| span (14×) | the rungs fill right-to-left, cheapest first | 70 ms stagger, capped 900 ms |
| ledger | the row under the cursor keeps its glow; the rest are hairline only | no animation — it is a table |
| terms | the four numerals, in reading order | 120 ms stagger |
| goodnight | the garden | on arrival |

Hover: buttons `translateY(-2px)` + glow shadow `.35s cubic-bezier(.2,.8,.2,1)`; links colour `.3s`.
**No scale, no bounce, no parallax, no autoplay, no marquee, no `hdt-reveal` slide-ins, no fade-in on text.**
`prefers-reduced-motion: reduce`: all transitions off, every lamp lit, cursor jumps instantly, anchor scrolls
`behavior:'auto'`.

### 3.4 The narrowing device — the ruler (this is the section that wins or loses the page)

One instrument, four unit modes, chosen per collection by a schema setting and **defaulted honestly**.

| mode | unit | collections | source |
|---|---|---|---|
| `length` | `מ׳` | `גרילנדות-ותאורה-דקורטיבית` | first option value parsed for a leading number before `מ׳` |
| `count` | `נקודות אור` | `תאורת-שביל-סולארית` | first option value parsed for a leading number before `יח׳ / יחידה / יחידות` |
| `price` | `₪` | `solar-wall-lights`, `ספוטים-ופרוז-קטורים-סולאריים` | `product.price_min` / `price_max` |
| `mixed` | three sub-rulers | `all` | §3.8 |

**Why `price` for wall and spot, and not a wattage ruler:** wall's first option axis is `צבע גוף` on four of
six products; its price-bearing axis is `עוצמה` on one, `כמות` on two, `סוג גוף` on one. Spot has no shared
axis at all — one product's `דגם` axis happens to be watts (`72 LED / 100W` → `200 LED / 300W`, 199.90 →
499.90 ₪) and no other product has it. **There is no honest wattage/Kelvin/beam ruler in this catalogue.**
`places` printed those questions anyway; we do not. Wall's and spot's ruler is the price rung ladder (§4.4's
composition, reused as the narrowing screen) plus a two-state `גוון אור` line where 4 of 6 wall products
actually carry `3000K / 6000K`.

#### The mechanism (exact)

```
[ 7 ]  ← count numeral, from collection.products_count, never typed
כמה מטרים צריך להאיר?                       ← h2, the place's question (C7)
( הכול )( 3 מ׳ )( 6 מ׳ )( 10 מ׳ )( 15 מ׳ )( 22 מ׳ )( 30 מ׳ )   ← the stops
סדר: [לפי אורך] מחיר עולה  מחיר יורד  א־ב                      ← plain ?sort_by= links, same hairline
├─0──────5──────10──────15──────20──────25──────30 מ׳──────────┤   ← the rail + cursor
  <row per product: title · axis caption · dot rail · price · action>
```

- **State lives in radio inputs, not JS.** `<input type="radio" name="env2-stop" id="env2-stop-10" class="env2-sr">`
  before the wrapper, `<label for="env2-stop-10" class="env2-pill">` inside it, and every consequence is a
  `#env2-stop-10:checked ~ .env2-wrap …` sibling rule. This is `howmuch/index.html:229–262` and it is the
  right answer: **it narrows with JavaScript disabled, and it does not scroll-jump the way `:target` does.**
- **The stops are generated, never typed.** Liquid walks `collection.products`, reads
  `product.options_with_values[0].values`, extracts the leading number of each value, and unions them into a
  sorted set; the section then keeps at most **seven** stops (`הכול` + six), chosen as the evenly-spaced
  members of that set. For decor the set is `1.5 3 5 6 6.5 7 8 9.5 10 11 12 13 22 32` and the six that ship
  are `3 · 6 · 10 · 15 · 22 · 30`. For path the set is `1 2 4 6 8 12` and all six ship.
- **A row never disappears.** At a stop, each row renders one of three states:
  - **hits** — the row prints the exact variant at or immediately above the stop and its exact price
    (`10 מ׳`: rope `12 מ׳ / 100 נורות — 99.90 ₪`, crystal `11 מ׳ / 60 נורות — 109.90 ₪`,
    globe `10 מ׳ / 80 נורות — 169.90 ₪`);
  - **short** — dims to `.4` and prints `האורך המרבי: <max> מ׳` (Edison at `10 מ׳`: `האורך המרבי: 8 מ׳`);
  - **off-scale** — a product whose axis is not in this unit is **not on the rail at all**; it is lifted into
    its own band (§4.3, band `לא נמדד במטרים`) with a real photograph and a real card. Decor's two are
    `solar-firefly-garden-lights` and `lighted-birch-branches-20-led`; path's three single-unit lamps
    (`stainless-steel-solar-path-light-ip65`, `modern-led-bollard-light-5w-ip65`,
    `powerful-solar-garden-light`) get their own band with three add-to-cart forms.
  - **area, not length** — `decorative-led-net-lights` is sold by area (`1.5×1.5` → `12×2` or `6×4 מ׳`) and
    **is never drawn as a span on a length rail**. It sits in the off-scale band with its own caption
    `נמדדת לפי שטח, לא לפי אורך`. (`howmuch` got this wrong; the ledger footnote in `evening` got it right.)
- **The derived per-unit line (C2)** prints under the price at every stop where a quantity exists, as
  `≈<price ÷ units> ₪ לנקודת אור` / `≈… ₪ ליחידה`, in `--env2-ink-2` at 14 px, always prefixed `≈` and always
  carrying the word the maths came from. It is computed in Liquid (`divided_by` on integers ×100 then
  `money_without_currency`-style rounding to two places) — never typed, never a claim.
- **`לא צוין` is carried, not hidden (C9).** When a product's first axis yields no number, the rail foot
  prints `<n> מוצרים בקולקציה אינם נמדדים ביחידה הזאת` with `<n>` from Liquid and an anchor to that band.

#### The URL / no-JS contract (binding)

| capability | with JS | without JS |
|---|---|---|
| narrow to a stop | works (radio) | **works** (radio) |
| shareable narrowed URL | **yes** — `#len-10`, written by `history.replaceState` on `change`, read on load | no — the page opens at `הכול`, fully usable |
| ordering | works | **works** — plain `<a href="?sort_by=price-ascending">`, server-side |
| add a single-variant product to cart | fetch → theme drawer | **works** — the form posts to `{{ routes.cart_add_url }}` and lands on `/cart` |
| every price visible | yes | **yes** — all stop states are rendered in the DOM; CSS chooses |

The JS enhancement is **eleven lines** and does nothing else:

```js
/* elmsnest-v2-coll-ruler: make the chosen stop shareable. No other behaviour. */
(function(){
  var f=document.getElementById('env2-coll-ruler'); if(!f) return;
  var pick=function(h){var el=h&&document.getElementById('env2-stop-'+h.replace(/^#(len|qty|band)-/,''));if(el)el.checked=true;};
  pick(location.hash);
  f.addEventListener('change',function(e){
    if(e.target.name!=='env2-stop') return;
    var v=e.target.id.replace('env2-stop-','');
    history.replaceState(null,'', v==='all' ? location.pathname+location.search : '#'+f.dataset.unitKey+'-'+v);
  });
})();
```

**Ordering is never a `<select>` and never a toolbar.** It is one hairline line of plain anchors inside the
ruler head, active state underlined in `--env2-glow`:
`סדר: לפי אורך · מחיר עולה · מחיר יורד · א־ב` → `?sort_by=manual|price-ascending|price-descending|title-ascending`.
Default label is honest: `לפי סדר הערב` on `/all` (= `manual`), `לפי אורך`/`לפי כמות` on decor/path.
**Never render `best-selling` or `popularity`** — one test order exists in the store's history.

### 3.5 The card — extend `elmsnest-v2-pdp-card.liquid`, do not fork it

The card was designed inside the PDP (`pdp/WINNING-SPEC.md` §4.8) precisely so this page could reuse it.
Its contract is unchanged: photo `[data-lamp]` radius 0 with pool glow · gold 11.5 px tracked kicker
(`<place> · <approved suits phrase>`) · `h3` **Heebo 400**, never the serif · price via
`elmsnest-v2-price.liquid` (`single` / `min–max` when `max ≤ min×1.25` / `מ־min`) · single available variant →
`<form>` add-to-cart `הוספה לסל`, else ghost link `לבחירת אורך` / `לבחירת כמות` / `לבחירת דגם` / `לבחירת גוון`.

**Three additive parameters, all optional, all defaulting to today's rendering** (so the PDP related row
renders byte-identically):

| param | type | effect |
|---|---|---|
| `variant: 'scene'` | string | the scrim card that rides a photograph (§4.1, §4.3): `background:var(--env2-scrim)`, `backdrop-filter:blur(10px)`, `padding:22px 26px`, price and action on one `space-between` row |
| `axis_caption` | string | one 14 px `--env2-ink-2` line under the title — the option axis and how far it reaches (`5 מ׳ / 10 נורות · 8 מ׳ / 20 נורות`) |
| `unit_price_line` | string | one 14 px `--env2-ink-2` line under the price — the derived per-unit figure (C2), always `≈`-prefixed |

**Forbidden on the card, here as on the PDP:** badge, sale flag, strikethrough, `-N%`, stars, review count,
swatch row, quick-add icon, hover-swap second image, `N נמכרו`, countdown, rounded corners.
**The kicker must not repeat identically down a column** — when two adjacent cards would print the same
`<place> · <suits>` string, the second prints the place alone. (`places` degraded the approved phrase to
wallpaper across seven cards; `evening`'s all.html terrace band does it across five.)

### 3.6 The image ledger — and the house rule for the fifteen products that have no photograph

**Verified finding (contact sheets over `brief/assets/img/`, indexes 0–3, all 27 products):** fifteen products
have **no** text-free image at any index in 0–3. Every one is a marketing poster — baked Hebrew headline,
spec icon strip, cream or beige ground. Whole-collection worst case:
`ספוטים-ופרוז-קטורים-סולאריים`, where five of six products have nothing usable and the sixth
(`dual-head-garden-light-10w-ip65`) is clean only at `[0]` (cream) and `[2]` (night).

Therefore:

1. **Resolution order** — every product thumbnail on this page goes through
   `snippets/elmsnest-v2-pdp-image.liquid` (already built, §3.5 of the PDP spec), called with
   `slot: 'card'`. Order: `section.settings.<block>_image` (image_picker override) →
   `product.images[card_image_index - 1]` (1-based schema range 1–6) → the never-use guard → the glyph plate.
2. **The never-use guard is widened.** The snippet already holds the fifteen handles from
   `brief/WINNING-SPEC.md` §3.6 in one `assign` and steps index 0 → 1. Add a second `assign`,
   `env2_no_clean_image`, holding the handles for which **no index is clean**, and for those the snippet
   renders **the glyph plate instead of an `<img>`**:

   | ships as a glyph plate | why |
   |---|---|
   | `solar-security-light-100-led`, `solar-garden-lantern-9-led`, `rechargeable-telescopic-camping-lantern`, `solar-floodlight-ip67-remote-timer`, `solar-garden-spotlight-52-led` | every index 0–3 is a poster |
   | `warm-solar-step-deck-lights`, `waterproof-solar-deck-step-lights`, `retro-solar-path-lights-set`, `modern-solar-path-lights-set`, `swaying-solar-path-lights-ip65` | every index 0–3 is a poster |
   | `modern-led-bollard-light-5w-ip65` | posters **and** three conflicting third-party wordmarks (`LUMIÈRE`/`LUMORA`/`LUMIRA`) |
   | `led-globe-string-lights`, `decorative-led-net-lights` | every index 0–3 is a poster on a cream ground |
   | `magnetic-rechargeable-touch-wall-light`, `solar-wall-light-motion-sensor-ip65` | every index 0–3 is a poster or a white studio cut-out |

3. **The glyph plate (C3), exact.** Same aspect and radius 0 as the photograph it replaces, ground
   `#080d18`, an inline SVG drawn from the product's own shape family (bollard / cube / string / net / spot —
   five glyphs, one `<symbol>` sprite in the section), stroke `rgba(244,238,227,.45)` 1 px, a warm radial halo
   `--env2-ember` at 22 % where the light source is, and a bottom-start caption in the kicker style:
   **`איור · אין תצלום נקי`**. It is a `[data-lamp]` like any photograph — its halo is what lights.
   It is **not** a grey placeholder and it never says "coming soon".
4. **Photographs that do ship** (verified clean and night-toned; 1-based admin position in brackets):
   `collection.image` ×4 (the only four images in the family with no baked text — path, wall, spot, decor) ·
   `stainless-steel-solar-path-light-ip65` [1] · `powerful-solar-garden-light` [2] ·
   `solar-crystal-ball-string-lights` [1] and [3] · `solar-rope-string-lights` [3] ·
   `solar-edison-string-lights` [1] and [4] · `solar-firefly-garden-lights` [3] ·
   `outdoor-bidirectional-led-wall-light-ip65` [1] · `waterproof-led-wall-light-ip65-6w-12w` [2] and [4] ·
   `modern-led-wall-light-6w-up-down` [4] · `modern-led-wall-light-indoor-outdoor` [4] ·
   `dual-head-garden-light-10w-ip65` **[3]** (not [1] — [1] is a cream studio ground, §1 disagreement 2) ·
   `lighted-birch-branches-20-led` [2] **only inside the off-scale band with a `--env2-sky-4` multiply veil**,
   because it is a bright cream interior and §3.1 bans cream as a surface.
5. **Every crop is checked at 1× and 2× before sign-off.** A caption that survives a crop is a breach whether
   or not the index was permitted (`evening`'s `all.html` terrace band fails this today with
   `decorative-led-net-lights`; that product is now a glyph plate, so it cannot).
6. Loading: the scene photograph `loading="eager" fetchpriority="high"`, `widths:'900,1400,1800,2400'`,
   `sizes:'100vw'`, plus `<source media="(max-width:900px)">` at `width:1000`. Everything below the first
   screen `loading="lazy"` with explicit `width`/`height`. The first band photograph is eager (AUDIT §182:
   lazy tiles render blank in captures).

### 3.7 Pagination — and why there isn't any

`paginate collection.products by 50`. **The pagination control renders only when `paginate.pages > 1`**, which
at 27 products is never — so the catalogue is one page and the page says so, in Liquid, not as a slogan:
`{{ collection.all_products_count }} מנורות בעמוד אחד. אין עמוד 2.`

The reason is printed once, in §4.5's foot, because it is a design decision the owner should be able to read:
a 12-per-page break cuts the ruler in half and destroys the only comparison the page exists to enable — and
today's `/collections/all` paginates 12/12/3 into three arbitrary alphabetical pages (AUDIT §1). The
`paginate` tag and the control are still **built** (`snippets/elmsnest-v2-coll-paginate.liquid`), because the
catalogue will grow and because `?sort_by=` must survive a page boundary: the control appends the current
`sort_by` to every page link.

Any `?sort_by=` **drops the band grouping to one flat ruler** — a page ordered by price cannot also be
grouped by distance without lying about the order. The ruler head says so:
`ממוין לפי מחיר — הקיבוץ לפי מרחק בוטל.`

### 3.8 How `/collections/all` differs

It is the whole catalogue, not one place, so it is composed differently — but it is the same store: same
ground, same pin, same card, same terms, same `לילה טוב`.

1. **Scene** (§4.1) — `collection.image` of the catalogue (or a merchant-set image), the pin, h1 `קטלוג`,
   deck `עשרים ושבע מנורות, לפי הסדר שבו נדלק הערב.` and one pinned product card with a live buy control
   (today: `dual-head-garden-light-10w-ip65`, `189.90 ₪`, `הוספה לסל`, image index `[3]`).
2. **The ruler becomes the table of contents (C5)** — the catalogue admits it has three units and says so as
   three numerals that are also jump links, **with the `?sort_by=` line on the same hairline** (this is the
   graft that fixes evening's ordering stranded at ~5,900 px):
   `17 · מנורה אחת, מקום אחד — הסרגל: מחיר` · `5 · שורה של נקודות — הסרגל: יחידות` ·
   `5 · קו רצוף של אור — הסרגל: מטרים`. Under it, four place entries — count, price span, first three product
   names, each an anchor.
3. **The bands become the four doors (C7)** — four places, each with its numeral, its scene, its own question,
   its count, its span and one named product with a price:
   `01 שביל, מדרגות ומעברים — כמה נקודות אור צריך השביל? · 8 מנורות · 69.90–999.90 ₪`
   `02 כניסה, קיר וחזית — כמה חזק האור צריך להיות? · 6 מנורות · 99.90–252.90 ₪`
   `03 הדגשת אזור בגינה — מה בדיוק צריך להאיר? · 6 מנורות · 99.90–499.90 ₪`
   `04 מרפסת ופינת ישיבה — כמה מטר צריך לכסות? · 7 מנורות · 89.90–469.90 ₪`
   Wall and spot questions are the two the *catalogue can answer by price and by named model*; they are not
   the beam/Kelvin questions `places` promised and could not draw (§3.4).
4. **The span screen (§4.4) runs on the whole catalogue** — 27 rungs, `69.90 → 999.90`, banded
   `עד 120 ₪ ⟨10⟩ · 121–250 ₪ ⟨16⟩ · מעל 250 ₪ ⟨1⟩`, counts from Liquid.
5. **No metre ledger** on `/all` (three units cannot share one column). It closes on the terms and
   `לילה טוב` instead.
6. **The four bands are ordered as an evening** — path, wall, spot, terrace — so the page reads as one
   sequence, not four sections. The band ordering is a schema `collection_1..4` picker list, not a hard-code.

---

## 4. Section-by-section build spec (page order)

Sketch legend: `▲` = start side (right in RTL), `▼` = end side (left). All Hebrew below is exact copy.
Every number is Liquid or a real variant value; nothing is typed.

---

### 4.1 `elmsnest-v2-coll-scene` — the gate · `#env2-coll-scene`

**Purpose.** In one screen, on a phone: which place you are in, what it looks like at night, one real lamp,
its real price, and a live route to buy. This is the section that answers AUDIT §4.1.

**Copy.**
- eyebrow (gold rule + tracked): `ערב אחד בחצר · קולקציה` — on `/all`: `ערב אחד · כל החנות`
- `h1` = `{{ collection.title }}`, real `<h1>`, visible, in Frank Ruhl Libre. **The `sr-only` SEO `h1` dies**
  (AUDIT §4.3). Line 2 in `--env2-glow`.
- deck, per collection, one authored line under the h1, and **the approved suits/doesn't-suit pair from
  `brief/BRIEF.md` §3 immediately under it (C8)** — the words the visitor tapped on the homepage:
  - decor: `מהשולחן, דרך העצים והערוגה, עד הגדר בסוף החצר.` / `מתאים כדי ליצור אווירה. לא מתאים אם צריך אור חזק — זו אינה מטרתה.`
  - path: `מהשער עד הדלת, בלי לנחש איפה המדרגה.` / `מתאים כדי לראות את הדרך. לא מתאים כשהמקום כמעט אינו מקבל אור יום.`
  - wall: `קיר אחד, וכל מה שלידו נראה אחרת.` / (the collection's own approved pair)
  - spot: `אור אחד, מכוון בדיוק לאן שצריך.` / (the collection's own approved pair)
  - all: `עשרים ושבע מנורות, לפי הסדר שבו נדלק הערב.`
- the counts line, all Liquid, on one hairline:
  `{{ collection.products_count }} מנורות · {{ variant_total }} וריאציות · {{ min }}–{{ max }} ₪`
- **`collection.description` paragraph 1** prints in the band below the veil, right column. **Paragraph 2
  prints only when the page delivers the choice it names** — decor and path deliver it (the ruler), so it
  prints as the ruler's deck (§4.2); wall's and spot's paragraph 2 (`בחרו לפי עוצמת האור, אזור ההתקנה וזווית
  ההארה`) **is suppressed**, because no such chooser exists in the data (§3.4). This is the fix for AUDIT §4.4
  and it is a one-line Liquid split: `{% assign dp = collection.description | split: '</p>' %}`.

**Desktop (1440).** Full-bleed `collection.image`, `min-height:100svh`, `object-position` per collection
(wall's is landscape 1456×816 → `50% 38%`). Header transparent over it (`scheme-env2-night` is already
legible on a dark first screen — this also closes AUDIT §0's cream-on-cream header bug for this template).
- The **pin** at a merchant-set `pin_x` / `pin_y` (`range`, 0–100, default 42/28): a 9 px `--env2-glow` dot
  with a 34 px radial halo, a 1 px hairline stem falling `--pin-stem` px (default 120) to a gold tracked tag.
  **The tag prints the lamp and its real value** — `כדורי קריסטל · 5 מ׳`, `01 · בתחילת השביל` is retired —
  and links to that product.
- Type block `▼` bottom-start, `max-width:22ch`.
- The **pinned card** `▲` bottom-end, `variant:'scene'` (§3.5), 420 px wide, riding the veil.
- Two-stop veil over the bottom 26 %: `linear-gradient(180deg,transparent 0%,rgba(15,26,47,.72) 62%,#0f1a2f 100%)`.

**Mobile (390×844, header 60 px).** Photo `78svh`; pin at `pin_x_m`/`pin_y_m`; the h1 + deck sit on the photo
at its foot; the **card is below the veil, full width, and its `הוספה לסל` / `לבחירת אורך` bottom edge must
land above 800 px**. Then the description paragraph, then the counts line, and the ruler's first stop row
must be visible at the fold edge. This is proven in `evening/shot-mobile-fold.png`,
`shot-path-mobile-fold.png` and `shot-all-mobile-fold.png` — hold the measurement.

**Motion.** The dot lights, then the stem draws (§3.3). Nothing else moves in screen 1.

**Schema.** `eyebrow` · `deck` · `suits_line` · `image` (image_picker, default `collection.image`) ·
`image_position_desktop` / `_mobile` (select of 5) · `pin_product` (product picker) · `pin_x` · `pin_y` ·
`pin_x_m` · `pin_y_m` · `pin_stem` · `card_image_index` (range 1–6) · `card_action_label` ·
`show_description_p1` (checkbox, default true) · `show_description_p2` (checkbox, **default false**).
Schema `name`: `"מסך פתיחה"` (≤25 chars).

**Non-negotiables.** (1) A product, a price and a buy control inside 844 px on 390 — on all five URLs.
(2) The `h1` is `collection.title`, visible, serif. (3) No banner band, no breadcrumb strip, no toolbar.
(4) The pin tag is real data or the pin is not drawn.

---

### 4.2 `elmsnest-v2-coll-ruler` — the instrument · `#env2-coll-ruler`

**Purpose.** Turn N ranges into N comparable priced answers in one tap, on a phone, with JS off.
This is the section the ruling exists for.

**Copy.**
- eyebrow: `המקום — והמידה`
- `h2` = the place's question (C7): decor `כמה מטרים של אור?` · path `כמה נקודות אור לאורך הדרך?` ·
  wall `כמה חזק, ובאיזה גוון?` **only if the גוון line ships**, else `מה נכנס לתקציב?` ·
  spot `מה בדיוק צריך להאיר?` · all `כמה אור? שלוש יחידות מידה.`
- deck = `collection.description` paragraph 2 where it is delivered (decor, path); else an authored line.
- count numeral: `{{ collection.products_count }}` at 150/88 px, with
  `דגמים בקולקציה · {{ n_on_rail }} מהם נמדדים ב{{ unit_word }}` under it.
- stop question: `כמה מטרים צריך להאיר?` / `כמה נקודות אור צריך השביל?` / `עד כמה לנקודת אור אחת?`
- order line: `סדר:` + four anchors (§3.4).
- rail foot: `האורך והמחיר בכל שורה הם וריאציה קיימת. כשהמקום ארוך מהדגם — כתוב עד כמה הוא מגיע, ולא מוסתר.`
  and, when applicable, `{{ n_off }} מוצרים בקולקציה אינם נמדדים ביחידה הזאת →` (anchor to the off-scale band).

**Desktop.** Numeral `▲` far start, question + stops centre, order line `▼`; then the full-width rail
(`min(1500px,…)`) with `0 … max` ticks; then one row per product on hairlines:
`▲ title + axis caption` · `centre: the product's own dot rail` (one dot per real option value, positioned by
its number; the dot at the chosen stop scales 1.5 and takes the halo) · `▼ price + per-unit line + action`.
Row height 96 px desktop.

**Mobile.** Numeral inline with its caption at 88 px; stops wrap to two rows of pills (48 px tall, `999px`
radius — the only radius on the page besides buttons); the order line on its own hairline; the rail spans the
gutter width; each row becomes: title (2 lines max) → axis caption → dot rail full width → price row with the
action pill `▼`. **The dot rail must not clip at the inline edge** — this is `index`'s live defect
(`index/shot-mobile-fold.png`: `179.90` and `129.90` half-cut). Give the row `overflow-x:auto;
overscroll-behavior-inline:contain` and a fading mask, and never let the page itself scroll horizontally at
360 px.

**`/collections/all` variant.** The ruler becomes the TOC of §3.8.2 — three unit numerals as jump links, the
sort line on the same hairline, then the four place entries with count, span and first three product names.

**Motion.** §3.3 ruler row. **The cursor's travel is the only thing that animates in this section.**

**Schema.** `unit_mode` (select: `length` / `count` / `price` / `mixed`, default resolved from the collection
handle) · `unit_word` · `unit_short` · `question` · `stops_max` (range 4–7, default 6) · `rail_max` (range,
default = computed) · `show_unit_price` (checkbox, default true) · `sort_default` (select) ·
`off_scale_anchor`. Blocks: none — the rows are `collection.products`.
Schema `name`: `"הסרגל"`.

**Non-negotiables.** (1) The stops work with JS disabled. (2) A product that cannot reach the stop **dims and
prints its maximum**; `display:none` on a product row is a breach. (3) Every price shown at a stop is a real
variant price at that value. (4) The order line is inside this section, above the fold on desktop and inside
the second screen on mobile — **not at 5,900 px** (evening's one real findability failure). (5) No `<select>`,
no funnel icon, no drawer, no grid-density control, anywhere on the page.

---

### 4.3 `elmsnest-v2-coll-bands` — the walk · `#env2-coll-bands`

**Purpose.** The desire. Each band is one differently-composed screen, so the page is never one grid scrolled
four times. **The bands are the ruler's bands, not invented places** (§1 disagreement 5).

**Band set, decor (5 bands, from the rail):** `01 עד 6 מ׳` · `02 6–12 מ׳` · `03 13 מ׳ ומעלה` ·
`04 לא נמדד במטרים` · `05 נמדדת לפי שטח`.
**Band set, path (4):** `01 מנורה אחת` · `02 2–4 נקודות` · `03 6–12 נקודות` · `04 נמכרות ביחידה`.
**Band set, wall / spot (3):** the three price bands of §4.4.
**Band set, `/all` (4):** the four places (§3.8.3).

Each band prints: numeral `01`–`05` (96/56 px gold) · the band label · a Liquid line
`{{ n }} מנורות · מ־{{ min }} ₪` · then its own composition. **The five compositions are different by rule:**

| band | composition | scale contrast |
|---|---|---|
| 01 | two cards on a hairline, no photo band — the quiet opening | small |
| 02 | **one full-bleed scene photograph with two pins**, the two cards `▼` riding its bottom edge | enormous |
| 03 | **a pull quote at 46 px** (`עשר נורות שמתנדנדות ברוח, ובוקעות מתוך הפרחים.`) `▼`, one small 260 px card `▲` — 3 : 1 | tiny vs huge |
| 04 | a photographic **diptych**, unequal (`1/1.05` and `1/1.4`), the off-scale products with real cards | medium |
| 05 | a wide low band, the card overlaid at its start edge | wide vs short |

Quote copy is authored per band via schema (default for decor 03 above; path 03:
`בין המנורה הזולה ליקרה יש פי 14. ההבדל הוא כמה מנורות מקבלים.`). Quotes are **never** claims about
performance.

**The wall band is recomposed** — `evening`'s `all.html` wall band is six near-equal cards on a 3×2 line and
is the one screen in the winner that is not "one evening" (the creative director is right). It ships as
**two + a wide one + three on a staggered baseline** at widths `300 / 210 / 260 / 300 / 210 / 260` and
aspects `1/1.05 · 1/1.4 · 1/.9`, `align-items:flex-end`. **Never four equal cells in a row.**

**Mobile.** Bands stack; the scene bands keep their photograph at `52svh` with the card below the veil; the
diptych becomes a 2-column asymmetric grid (`1.15fr .85fr`), never two equal squares; the pull quote is full
width at 26 px with the card under it.

**Schema.** Blocks of type `band`: `numeral` (auto) · `label` · `composition` (select of the five) ·
`scene_image` (image_picker) · `pin_1_product` / `pin_1_x` / `pin_1_y` · `pin_2_*` · `quote` · `product_1..3`
(pickers; empty = auto-fill from the band's computed set) · per-card `card_image_index` · `card_action_label`.
Max 5 blocks. Schema `name`: `"תחנות הערב"`.

**Non-negotiables.** (1) No band repeats another band's composition. (2) Every card carries a price and a
route to buy. (3) The kicker does not repeat identically on adjacent cards (§3.5). (4) No band is four equal
boxes. (5) Every product in the collection appears in exactly one band — `collection.products_count` must
equal the sum of the band counts, asserted in Liquid and printed in the last band's foot.

---

### 4.4 `elmsnest-v2-coll-span` — the fourteen-times screen · `#env2-coll-span`

**Purpose.** Dissolve a 69.90 → 999.90 ₪ span in one screen. Ships on `path`, `spot` and `all`
(schema-toggled off on `decor` and `wall`, whose spans are narrow).

**Copy.**
- eyebrow: `אותה קולקציה, פי ארבעה־עשר`
- `h2`: `כמה מנורות צריך?`
- deck **(C4, verbatim from `index` — the one sentence that does the work):**
  `המוצר היקר בקולקציה עולה פי 14 מהזול — לא כי הוא מנורה טובה יותר, אלא כי הוא סט של 8 יחידות.`
- the resolution line, all derived: `שמונה מנורות לאורך הדרך, 124.99 ₪ כל אחת.`
- foot: `המחיר ליחידה מחושב מהמחיר של הווריאציה חלקי מספר היחידות שבה. אינו מחיר קטלוגי.`

**The ladder (C6, from `switchboard/path.html`).** One rung per product, ordered by `price_min`:
`▲ product title + axis caption` · a **bar solid from 0 to `price_min` and a hairline onward to `price_max`**
on a shared linear scale to the collection's `price_max` · `▼ מ־69.90 ₪` and, where the axis is a quantity,
the per-unit figure at the largest and smallest stop. Rungs are grouped under three band headers that are
**not controls, just headers** — `עד 150 ₪ ⟨3⟩ · 150–350 ₪ ⟨4⟩ · מעל 350 ₪ ⟨1⟩`, counts from Liquid.
(The rockers and pip matrices of `switchboard` are **not** grafted; the ladder is.)

**The closing column** is the per-unit column alone, at 4 and 8 points, verified against `data.json`:

| at 4 נקודות | price | ₪ לנקודה |
|---|---|---|
| `waterproof-solar-deck-step-lights` | 149.90 | ≈37.48 |
| `warm-solar-step-deck-lights` | 159.90 | ≈39.98 |
| `retro-solar-path-lights-set` | 389.90 | ≈97.48 |
| `modern-solar-path-lights-set` | 549.90 | ≈137.48 |

| at 8 נקודות | price | ₪ לנקודה |
|---|---|---|
| `waterproof-solar-deck-step-lights` | 149.90 | ≈18.74 |
| `warm-solar-step-deck-lights` | 269.90 | ≈33.74 |
| `modern-solar-path-lights-set` | 999.90 | ≈124.99 |

`swaying-solar-path-lights-ip65` sells 2 or 6 only and is **absent from both columns** — it appears in the
ladder with its own stops and the note `נמכרת ב־2 או ב־6 בלבד`. (The panel's "at 4 points: 329.90" line mixed
that product's 6-unit price into a 4-unit column; it is wrong and does not ship.)

**Layout.** Desktop: eyebrow + h2 + deck `▲` in a 34ch column, the ladder full width beneath, the closing
column as a hairline table `▼`. Mobile: the ladder rungs stack, each 72 px, bar full width under the title;
the closing column is a 3-row hairline table. **No horizontal scroll at 360 px.**

**Motion.** Rungs fill cheapest-first, 70 ms stagger, capped 900 ms.

**Schema.** `enabled` (checkbox) · `eyebrow` · `heading` · `deck` · `resolution_line` ·
`band_1_max` / `band_2_max` (range) · `unit_stops` (text, comma list, default `4,8`) · `foot_note`.
Schema `name`: `"פער המחירים"`.

**Non-negotiables.** (1) Every per-unit figure is derived in Liquid and prefixed `≈`. (2) No product appears
in a per-unit column at a quantity it does not sell. (3) The bars are a shared linear scale — a log scale
would flatter the expensive set.

---

### 4.5 `elmsnest-v2-coll-ledger` — the measure · `#env2-coll-ledger`

**Purpose.** Answer "I have a six-metre pergola" with one row. This is `evening`'s best screen; it is promoted
from the page's foot to a destination the ruler links to.

**Copy.** eyebrow `אחרי המקום — המידה` · `h2` `כמה מטר צריך?` (path: `כמה מנורות צריך?`) ·
deck `ארבע מהגרילנדות נמכרות לפי אורך. אלה כל האורכים שיש בקולקציה, עם המחיר של כל אחד — לפני שבוחרים.`

**Decor — 14 rows**, one per real length in the union of the first option axes, each naming every garland
available at that length with its exact price:

| מ׳ | products at that length |
|---|---|
| 1.5 | כדורי `LED` 10 נורות — 89.90 ₪ |
| 3 | כדורי `LED` 20 נורות — 99.90 ₪ |
| 5 | כדורי קריסטל 20 נורות — 89.90 ₪ · נורות אדיסון 10 נורות — 139.90 ₪ |
| 6 | כדורי `LED` 40 נורות — 119.90 ₪ |
| 6.5 | כדורי קריסטל 30 נורות — 89.90 ₪ |
| 7 | שרשרת חבל 50 נורות — 89.90 ₪ |
| 8 | נורות אדיסון 20 נורות — 179.90 ₪ |
| 9.5 | כדורי קריסטל 50 נורות — 99.90 ₪ |
| 10 | כדורי `LED` 80 נורות — 169.90 ₪ |
| 11 | כדורי קריסטל 60 נורות — 109.90 ₪ |
| 12 | שרשרת חבל 100 נורות — 99.90 ₪ · כדורי `LED` 100 נורות — 179.90 ₪ |
| 13 | כדורי קריסטל 100 נורות — 129.90 ₪ |
| 22 | שרשרת חבל 200 נורות — 119.90 ₪ · כדורי קריסטל 200 נורות — 179.90 ₪ |
| 32 | שרשרת חבל 300 נורות — 159.90 ₪ |

**Path — 6 rows** (`1 · 2 · 4 · 6 · 8 · 12`), each printing the price **and** the per-unit figure (C2).

**Foot, exact and binding (this is the honesty fix `howmuch` failed):**
`שלוש הנותרות נמדדות אחרת: הרשת נמדדת לפי שטח — מ־1.5×1.5 מ׳ ועד 12×2 מ׳ או 6×4 מ׳; הגחליליות מגיעות בדגם אחד של 10 נורות; ענפי הליבנה בגובה כ־72 ס״מ.`
Then the pagination decision, in Liquid: `{{ collection.all_products_count }} מנורות בעמוד אחד. אין עמוד 2.`

**Layout.** Desktop: numeral `▲` at 44 px tabular with the unit at `.32em`, then a hairline row carrying one
to three named products with their prices, `▼`-aligned. Row 56 px, hairline between. Mobile: numeral on its
own line, products stacked beneath at 15 px — **never a horizontally scrolling table**.

**Every row is a link** to the ruler at that stop (`#len-10`), so the ledger and the ruler are one instrument
seen twice.

**Motion.** None. It is a table and it should read like one.

**Schema.** `enabled` · `eyebrow` · `heading` · `deck` · `foot_note` · `link_rows` (checkbox, default true).
Schema `name`: `"טבלת המידות"`.

**Non-negotiables.** (1) Every length and every price comes from `product.options_with_values[0]` and
`variant.price` — nothing typed. (2) A product measured in another unit is named in the foot, never given a
row. (3) `decorative-led-net-lights` never appears as a length.

---

### 4.6 `elmsnest-v2-coll-terms` — the four numbers · `#env2-coll-terms`

Lifted from the PDP's §4.6 as a **2-column hairline ledger, never four boxes** (this is the shape `evening`
gets wrong on mobile, `shot-mobile.png` slice 4: a 2×2 bordered grid).

`0 ₪ משלוח לנקודת איסוף — חינם. עד הבית 29.90 ₪.` · `8–17 ימי עסקים לאספקה: 1–3 ימי טיפול ו־7–14 ימי משלוח.
ייתכן משלוח ממחסן מחוץ לישראל.` · `14 יום לביטול מקבלת המוצר, לפי חוק הגנת הצרכן. דמי ביטול עד 5% או 100 ₪ —
הנמוך מביניהם.` · `1 תמונה — שולחים תמונה של המקום ואנחנו בודקים התאמה לפני ההזמנה.`

CTA: `<a>` styled ghost, `לשלוח תמונה של המקום` → `mailto:info@elmsnest.com` with a prefilled subject and
body (`snippets/elmsnest-v2-pdp-photo-cta.liquid`). **Never the word `בוואטסאפ`** while
`settings.whatsapp_number` is empty. Note beside it: `כאשר מידע אינו מאומת, איננו מציגים אותו כעובדה.`

**This section appears on all five URLs** — the terms currently appear on none of the eight collection pages
(AUDIT §4.6).

Schema `name`: `"לפני שקונים"`.

---

### 4.7 `elmsnest-v2-coll-goodnight` — the way out · `#env2-coll-goodnight`

The homepage's closing gesture, reused so the two pages rhyme: `לילה טוב` in FRL 900, **outline only, never
filled**, over `collection.image` at 80 % opacity under a `--env2-sky-4` gradient, `object-position:50% 70%`.
Under it, the cross-links as plain anchors on one hairline — the other three collections by name, then
`לכל {{ collections.all.products_count }} המוצרים ←`. On `/all`, the four places instead.

Sits **directly above the Kalles footer**. Schema `name`: `"לילה טוב"`.

---

## 5. `templates/collection.json`, the file list, and what is retired

### 5.1 The template

There is **no per-collection template suffix in use** (BRIEF §7), so the file is `templates/collection.json`
and it serves all five URLs; the sections branch on `collection.handle` through their `unit_mode` defaults.

```json
{
  "sections": {
    "coll_scene":     { "type": "elmsnest-v2-coll-scene" },
    "coll_ruler":     { "type": "elmsnest-v2-coll-ruler" },
    "coll_bands":     { "type": "elmsnest-v2-coll-bands" },
    "coll_span":      { "type": "elmsnest-v2-coll-span" },
    "coll_ledger":    { "type": "elmsnest-v2-coll-ledger" },
    "coll_terms":     { "type": "elmsnest-v2-coll-terms" },
    "coll_goodnight": { "type": "elmsnest-v2-coll-goodnight" }
  },
  "order": ["coll_scene","coll_ruler","coll_bands","coll_span","coll_ledger","coll_terms","coll_goodnight"]
}
```

`coll_span` and `coll_ledger` carry an `enabled` checkbox and render nothing when off, so `wall` (narrow span,
no shared unit) and `spot` ship six sections and `decor` ships six (span off, ledger on).

### 5.2 New files

| file | what |
|---|---|
| `sections/elmsnest-v2-coll-scene.liquid` | §4.1 — renders `elmsnest-v2-ground-collection` and nothing else global |
| `sections/elmsnest-v2-coll-ruler.liquid` | §4.2 — the radios, the stops, the rail, the rows, the sort line |
| `sections/elmsnest-v2-coll-bands.liquid` | §4.3 — five compositions, blocks |
| `sections/elmsnest-v2-coll-span.liquid` | §4.4 — the ladder + per-unit columns |
| `sections/elmsnest-v2-coll-ledger.liquid` | §4.5 — the measure table |
| `sections/elmsnest-v2-coll-terms.liquid` | §4.6 |
| `sections/elmsnest-v2-coll-goodnight.liquid` | §4.7 |
| `snippets/elmsnest-v2-ground-collection.liquid` | §3.1, mirrors `-ground-product` |
| `snippets/elmsnest-v2-coll-axis.liquid` | parses `options_with_values[0]` → `{value, number, unit, price, variant_id}` array; the single source of every number on this page |
| `snippets/elmsnest-v2-coll-rail.liquid` | one product's dot rail + its three stop states |
| `snippets/elmsnest-v2-coll-paginate.liquid` | §3.7 — renders only when `paginate.pages > 1`, carries `sort_by` |
| `snippets/elmsnest-v2-coll-glyph.liquid` | §3.6.3 — the five-glyph sprite + `איור · אין תצלום נקי` plate |

### 5.3 Edited, not forked

- `snippets/elmsnest-v2-pdp-card.liquid` — three additive optional params (§3.5). **After the edit, re-shoot
  the PDP's related row and diff it: it must render byte-identically.**
- `snippets/elmsnest-v2-pdp-image.liquid` — add the `env2_no_clean_image` handle list and the glyph branch
  (§3.6.2). Same signature.
- `snippets/elmsnest-v2-core.liquid` — **no change this round.** The `<a class="env2-btn">` ink bug
  (`core/REPORT.md` §9.1, 1.21:1) is still open, so **every primary call to action on this page is a
  `<button>` inside a form, or sets its own colour: `.env2-coll a.env2-btn{color:var(--env2-btn-ink)}`.**
  Check the computed colour in the render; do not assume. Do not use `--en-warning-text` / `-success-` /
  `-error-` / `-info-` (`REPORT` §9.2) — they are cream-era.

### 5.4 Retired from the collection template

Removed from `templates/collection.json` (files stay on the theme until the owner signs off the preview;
nothing is deleted this round, exactly as the PDP round did it):

| section | why |
|---|---|
| `main-collection` | the 85 KB JS organism: facets drawer re-rendered by AJAX, grid-density selector, `hdt-price-range`, `readmore-less`, `hdt-reveal`, `toolbar-mobile`. Replaced wholesale (BRIEF §7) |
| `main-heading` (`_heading_liquid`, `_heading_brc`) | the taupe banner and the duplicated breadcrumb title; the real `h1` is now §4.1's |
| `top-list-collections` (`collections_list_simple_4yRUED`) | the 45 px cream strip with four brown links, no active state, clipped on mobile |
| `snippets/facets.liquid` + the filter drawer | the only facets Shopify holds are availability and an untranslated English `Price`; the owner rejected the toolbar |

**Kept from Kalles — exactly three things:** the `collection` object with `paginate`; server-side `?sort_by=`
and `collection.sort_options`; and the `/cart/add` → cart-drawer mechanic. `card-price.liquid` is **not**
kept — `elmsnest-v2-price.liquid` owns the price rule.

`body.hdt-page-type-collection` hooks stay on the body (Kalles JS expects them); no section relies on them.

---

## 6. The do-not list for this build

1. **No toolbar.** No sort `<select>`, no funnel icon, no filter drawer, no grid-density toggles, no "מיין"
   button. Ordering is four plain anchors on a hairline inside §4.2.
2. **No skeuomorphic controls.** No rocker plates, no pip matrices, no dot-matrix rows. The homepage spec
   already refused them once.
3. **No four of anything in a row**, and no band that repeats another band's composition. If a grid of equal
   cells appears, it is wrong.
4. **No sale UI**: no badge, no strikethrough, no `-N%`, no `compare_at` rendering, no `/collections/sale`
   link. The one compare-at price in the catalogue (`waterproof-solar-deck-step-lights`, 199.90 → 149.90)
   renders as **149.90 ₪ and nothing else**.
5. **No ratings, review counts, "נמכר ביותר", "פופולריות", countdowns, "נותרו N", or any urgency.** Never
   render `best-selling` or `popularity` in the sort list.
6. **No product row is hidden by narrowing.** A lamp that cannot reach the stop dims and says how far it does
   reach. `display:none` on a product is a breach.
7. **No filter that answers a question it cannot answer.** A budget stop that narrows on `price_min` puts a
   199.90–499.90 ₪ floodlight under `עד 220 ₪`; a footnote is not a mechanism. On `price` mode the stop reads
   `מחיר כניסה עד N ₪` and the row prints its full range beside it.
8. **No invented taxonomy.** No station, zone, room or place that has no Shopify field behind it. No new
   per-product metafield is introduced by this round.
9. **No image at index 0 for a never-use handle, and no crop that lets a baked caption survive.** Fifteen
   products get the glyph plate (§3.6.2). Check every thumbnail at 1× and 2×.
10. **No cream, beige or brown on any surface** — including a photograph whose own ground is cream. That is
    what disqualifies the birch and the wall studio cut-outs from the open page.
11. **No product title in the serif, no headline in Heebo, no Assistant as a display face.**
12. **No `<bdi>` split across a slash pair.** `<bdi>6W/12W</bdi>`, `<bdi>1/4/8/12</bdi>`, one element.
13. **No caption under 13 px, no tap target under 44 px, no horizontal page scroll at 360 px**, and no dot
    rail that clips at the inline edge.
14. **No box, no rounded tile, no card grid.** Radius 0 everywhere except pill buttons and the cursor knob.
    The scrim is the only card surface, used twice.
15. **No `[data-lamp]` that starts lit under `html.env2-js`**, and none that stays dim without the guard.
    No-JS = everything lit, every stop usable, every single-variant product buyable.
16. **No `hdt-reveal`, no slide-in, no fade-in on text, no parallax, no autoplay, no marquee, no emoji, no
    English UI strings.**
17. **No "בוואטסאפ"** while `settings.whatsapp_number` is empty. The label is `לשלוח תמונה של המקום`.
18. **Never write a new negative.** Only the four approved suits/doesn't-suit pairs, verbatim, and only where
    literally true. **Never print `collection.description` paragraph 2 on a page that does not deliver the
    choice it names** (wall, spot).
19. **No typed number anywhere.** Counts, spans, variant totals, lengths, quantities and per-unit figures all
    come from `collection.products_count`, `collection.all_products_count`, `product.price_min/max`,
    `product.options_with_values[0]` and `variant.price`.
20. **Do not reuse a layout.** Scene (photo + pinned card) · ruler (numeral + stops + rail + rows) · bands
    (five different compositions) · span (rungs) · ledger (numbered rows) · terms (2-column) · goodnight
    (outline word over a photo). Seven sections, seven shapes.

---

## 7. References — what to lift, and from where

**Primary source: `brief/side-pages/collection/concepts/evening/`**

| What | File : lines |
|---|---|
| Tokens, `.wrap`, `.eyebrow`, `.kicker`, `.lead`, `.h`, `.price`, `.btn*`, `.link`, `.hair`, `.sr` | `evening.css:1–56` |
| `[data-lamp]` dim → lit, photo brightness + halo | `evening.css:58–72` |
| **The pin** — dot, hairline stem, gold tag | `evening.css:73–86` |
| Transparent header over the scene | `evening.css:87–106` |
| **The opening scene** + veil + the card sold from inside it | `evening.css:107–149` |
| Station bands → **re-target to the ruler's bands** (§4.3) | `evening.css:170–250` |
| The price ladder under a card (`§4.3`, per-value stops) | `evening.css:222–239` |
| **The measure ledger** (numeral + named products per row) | `evening.css:251–271` |
| Order line + all-link (**move it into §4.2**) | `evening.css:272–280` |
| Terms strip (**rebuild as 2-column, not 2×2 boxes**) | `evening.css:281–289` |
| Footer / `לילה טוב` | `evening.css:290–305` |
| `all.html` four-hours composition | `evening.css:336–358` |
| Hairline product rows (the walk) | `evening.css:359–378` |
| Pagination note | `evening.css:395–400` |
| Lamps-on-arrival IO + sweep (lift whole, 22 lines) | `evening.js:1–22` |
| Fold proof to hold | `shot-mobile-fold.png`, `shot-path-mobile-fold.png`, `shot-all-mobile-fold.png` |

**Graft sources**

| Graft | File : lines |
|---|---|
| C1 — the stops, the cursor, the three row states, **all in pure CSS `:checked ~` (no JS)** | `concepts/howmuch/index.html:229–262` (the `:checked ~` rule set), `:301–307` (the seven radios), `:355–380` (a row's per-stop `.v` spans), `:395–507` (the two honest miss states — `האורך המרבי: <n> מ׳` on the row, `לא מגיעה ל־<n> מ׳` on the rail) |
| C2 — the derived per-unit line | `concepts/howmuch/path.html` closing column; `concepts/evening/path.html` station 05 (`shot-path-desktop.png` slice 4: `124.99 ₪` / `137.48 ₪`) |
| C3 — the glyph plate | `concepts/howmuch/` `איור · אין תצלום נקי` plates |
| C4 — the 14× sentence + compressed price scale | `concepts/index/path.html` fold (`shot-path-mobile-fold.png`) |
| C5 — high TOC with the sort line beside it | `concepts/index/all.html` head (`shot-all-mobile-fold.png`) |
| C6 — the one-screen price ladder | `concepts/switchboard/path.html` (`shot-path-desktop-fold.png`) — the ladder only, none of the toggles |
| C7 — the place's own question as the headline | `concepts/places/all.html` four doors (`shot-all-desktop-fold.png`) |
| C8 — homepage place phrase + approved pair under the h1 | `concepts/places/index.html` fold (`shot-mobile-fold.png`) |
| C9 — the `לא צוין` bucket carried with a real count | `concepts/switchboard/index.html` power-source bank |

**Data and plumbing**

- `brief/side-pages/collection/data.json` — the only source for counts, spans, option axes and prices.
- `brief/WINNING-SPEC.md` §3.1–§3.6 — palette, type, spacing, motion, the never-use image list.
- `brief/side-pages/pdp/WINNING-SPEC.md` §3.5 (image resolver), §3.6 (option-axis rule), §4.8 (the card),
  §6 (the do-not list this one extends), §8.2–§8.4 (the core is `elmsnest-v2-core`; the anchor-button and
  notice-colour bugs).
- `brief/build-preview/CONTRACT.md` — section root, tokens, shared classes, `[data-lamp]`, `window.env2`,
  snippet signatures. **Do not restyle a shared class.**
- `brief/inventory/AUDIT-collection.md` §§0, 4, 5, 7 — what is being replaced, with measurements.
- `brief/side-pages/core/REPORT.md` §9.1–§9.2 — the two open core bugs this page must not inherit.
- `brief/side-pages/OWNER-NOTES.md` — no sales, no toolbar, no WhatsApp number, locked image ledger.

**Before sign-off, re-shoot and check** (`node brief/shot.js <file> <prefix>` at 1440×900 and 390×844, on
**all five** URLs — decor, path, wall, spot, all):

1. A product photograph (or glyph plate), a real price and a buy control **inside 844 px on 390** — five for
   five. Measure the `הוספה לסל` / `לבחירת אורך` bottom edge; it must be `< 800 px`.
2. The **stops are inside the second screen on mobile** and the sort line is with them — not at 5,900 px.
3. **Disable JavaScript and re-shoot**: the stops still narrow, every price is visible, the sort links still
   work, and every single-variant product still adds to cart.
4. Tap `10 מ׳` on decor: rope `99.90`, crystal `109.90`, globe `169.90`, and Edison **dimmed and printing
   `האורך המרבי: 8 מ׳`**.
5. No caption under 13 px; no tap target under 44 px; **no horizontal page scroll at 360 px**; no dot rail
   clipped at the inline edge.
6. Zero cream pixels above the Kalles footer; zero legible baked Hebrew in any thumbnail at 1× **and** 2×.
7. `<bdi>6W/12W</bdi>` and `<bdi>1/4/8/12</bdi>` render in that order.
8. The PDP related row is byte-identical to its pre-edit render.
