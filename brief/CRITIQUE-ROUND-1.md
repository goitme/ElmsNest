# ElmsNest v2 — critique round 1, merged fix list

Design lead ruling on the four critiques of the deployed dev theme (creative director, mobile shopper /
conversion, Hebrew typographer, front-end QA + a11y), checked against the live crops in
`brief/build-preview/live/`, the dusk mockup and WINNING-SPEC §1 / §3 / §7, and the source in
`theme/sections/elmsnest-v2-*.liquid`, `theme/snippets/elmsnest-v2-*.liquid`, `theme/templates/index.json`.

## 0. Ruling

**Would the owner still say "nineties"? No.** The page has one idea (dusk → night on one gradient), one
device you can drag, editorial Frank Ruhl Libre at 135/104/340 px against Heebo labels, a numeral ledger and
an outlined word; on both viewports it reads as designed, not templated. **What he would say instead is
"dark, unfinished and slightly broken"**, for five reasons that are all visible in the screenshots he will
judge from first: a white Kalles back-to-top square floating over Hebrew text on every scrolled screen; every
"send a photo on WhatsApp" promise landing on a contact form (and a dead `wa.me/` in the footer); the honesty
stage showing the lamp OFF on the lit side at its default split; a muddy brown finale where the mockup had a lit
garden; and the delivered full-page PNGs showing five sections black because the QA scroll never lit them. On a
phone he adds "beautiful, but where do I buy?" (the buy button sits under the Safari fold; three of four
collections are behind swipes) and "everything is repeated" is still half true (the photo promise five times,
nine pill buttons, the footer paragraph restating the hero lead).

All of those are fixable in one round without touching the idea. Nothing below reintroduces a grid of equal
boxes, a cream surface, a typed fact, or a second layout.

## 1. Dedupe table (merged items → critic ids)

| # | Merged defect | Raised by | Severity | Decision |
|---|---|---|---|---|
| R01 | Kalles back-to-top = white 32/40 px square bottom-right over text (terms "1", places caption, switch lead, atmosphere CTA) | F01 · M1 · Q1 (+ visible in crop-m-env2-terms / crop-d-env2-places / crop-d-env2-atmosphere) — **4 critics** | blocker | **MUST** — base |
| R02 | Photo-check promise has no WhatsApp target: 6 CTAs → `/pages/contact-us`, footer link is bare `https://wa.me/` | F02 · M2 · M5 · Q3 — **4 critics** | blocker | **MUST** — config + label guards |
| R03 | A vertical swipe that starts on the switch stage snaps the divider to the finger (range takes touchstart) | Q2 (executed) | major | **MUST** — switch JS |
| R04 | Switch default split shows the bollard inside the dark clip; the lit side is leaves and spill, caption "לראות את הדרך" next to a black lamp | F03 (confirmed: bollard x≈180–300 of 781, lit clip starts x=297; source image has the bollard in its left third) | major | **MUST** — switch (mirror block 1) |
| R05 | Mobile first screen: at 390×664 (iPhone Safari small viewport) "הוספה לסל" is below the fold; the first text is a 12 px three-line footnote about the page | M3 · M4 · T5 — **3 critics** | major | **MUST** — hero |
| R06 | Goodnight finale: garden at .8 under a .55/.28/.66 veil in a 479 px strip, outlined word a .45 hairline — reads as a brown smear vs the mockup's lit garden | F09 (confirmed vs `concepts/dusk` bottom; mobile bulbs read as grey discs) | major | **MUST** — goodnight |
| R07 | Wall: h2 wraps to three lines ("קיר אחד / מספיק." orphan at 104 px); studio-grey backdrop reads as fog top-left; on mobile the photo box (62svh) ends in a hard seam through the h2 | F06 · T2 — **2 critics** (seam confirmed at y≈523 CSS in crop-m-env2-wall) | major | **MUST** — night-wall |
| R08 | String bulbs ring themselves with dark banded discs (60 px/.14 box-shadow composites darker than the sky) | F08 · Q8 — **2 critics** (visible at 1× in crop-d-env2-atmosphere) | major | **MUST** — atmosphere |
| R09 | Mobile hanging trio: bulbs at y≈300, products 150 px lower with no drop-lines, a black band between; card 2 guillotined at x=0 mid-word; card 3 off-screen; no affordance | F10 · M11 · Q4 — **3 critics** | major | **MUST** — atmosphere |
| R10 | Terms: "100 / ₪" split across lines (currency torn from its number); h2 stacks "ארבעה / מספרים / שכדאי לדעת" at max-width 11ch | T1 · T3 · F12 — **2 critics** | major | **MUST** — terms |
| R11 | Repetition: photo promise ×5 (hero, switch line + link, terms row 4, goodnight, footer), goodnight strip restates the ledger 470 px above, footer paragraph = hero lead, nine pill buttons | M10 · F15 (+ F02 count) — **2 critics** | major | **MUST** (copy/settings) + SHOULD (pills) |
| R12 | Delivered shot-desktop/mobile.png show five sections unlit: `html{scroll-behavior:smooth}` defeats shot.js's rapid `scrollTo` | F20 | nit for the site, blocker for the review | **MUST** — shot.js |
| R13 | Three Hebrew paragraphs set `text-align:end` → ragged on the reading edge (places intro, terms intro, atmosphere sub) | T4 (confirmed: terms intro line 2 hangs at the far left) | major | **SHOULD** — places / terms / atmosphere |
| R14 | Mobile thumb targets: `.env2-btn--sm` 36 px, `.env2-link` 21 px, wall companion 20 px, strip/foot links 21 px | M7 | major | **SHOULD** — base + wall/terms/goodnight |
| R15 | "הוספה לסל" is a bare POST: Kalles binds ajax only inside `hdt-product-form`, so the tap leaves the page for `/cart` | M14 · Q12 — **2 critics** | major/minor | **SHOULD** — base JS (verify on the dev theme) |
| R16 | Nine pills; button sizes mixed inside first-lit (15 vs 13.5 px) and atmosphere | F15 · T11 | minor | **SHOULD** — buy snippet + atmosphere + first-lit |
| R17 | Birch branches = bright cream INDOOR styling shot (white vase, framed print) — the one bright rectangle on a night page about outdoor lighting | F07 (all four product images are indoor; images[0] is the darkest, grey wall) | major | **SHOULD** — atmosphere + index.json |
| R18 | Mobile places: headline says four, screen shows one; 58 px sliver of #2; no index | M6 | major | **SHOULD** — places |
| R19 | Places step 2 (קיר): landscape collection image, wall light sliced at the frame's left edge, numeral on it | F13 (known open item) | minor | **SHOULD** — places + index.json |
| R20 | Rhythm: ~330 px empty sky between the places link and the switch eyebrow; terms 1365 px for four rows | F14 | minor | **SHOULD** — places / switch / terms |
| R21 | Switch details: inactive tabs 3.9:1, lit kicker 3.97:1 (Q6); dark caption 10/13.5 px (M9, T10); "לא." outline invisible before it lights (F11); mobile collection link a 13 px hairline, toggle decorative (M8); inactive panels not hidden from AT (Q10) | Q6 · M9 · T10 · F11 · M8 · Q10 | minor | **SHOULD** — switch |
| R22 | Wall spec line: separator dot opens the wrapped second line | T7 · Q9 — **2 critics** | minor | **SHOULD** — night-wall |
| R23 | "מ־139.90 ₪": maqaf in FRL reads as a macron on the digits; prefix same size as the number | T6 | minor | **SHOULD** — price snippet + base |
| R24 | Sticky Kalles bar returns as .7 glass over the sky, headlines show through it | F16 · M13 — **2 critics** | minor | **SHOULD** — header-group.json |
| R25 | Kalles footer: Assistant not Heebo, underlined links, copyright "© elmsnest.com · ElmsNest 2026 …" reads out of order; intro paragraph = hero lead | F17 · T13 (+ M10) | minor | **SHOULD** — base CSS + footer-group.json |
| R26 | Hero LCP preload never matches the `<img>` srcset (filtered vs unfiltered widths) | Q5 | major (perf) | **SHOULD** — hero + theme.liquid |
| R27 | Hero small copy: note/eyebrow 3.2–3.4:1 over lit grass (Q15); sun-rail "שקיעה" touches step-4 photo (F19); mobile ghost button over the white bollard (F18); card title is an `<h2>` peer of section h2s (T8, Q11); five sections without an accessible name (Q11) | Q15 · F19 · F18 · T8 · Q11 | minor/nit | **SHOULD** — hero (+ one line per section) |
| R28 | Typed facts / settings: `card_title_override`, `title_override`, hard-coded social URLs (Q18); reach link says "לפי מקום" but goes to `/collections/all` (M12); guillemets + "elmsnest.com" in the self-cite (T14, M16) | Q18 · M12 · T14 · M16 | minor/nit | **SHOULD** — index.json + switch schema |
| R29 | `.env2-first__var` mute on sky-1 (forbidden by §3.1), 4.45:1 | Q7 | minor | **SHOULD** — first-lit |
| R30 | Reach range computed from `collections.all.products` (50-item page) | Q17 | nit | **SHOULD** — atmosphere |
| S01 | Hero master 1003/1254 px stretched to 1440 CSS @2×; card covers the front bollard | F04 · Q5 (softness) | major | **SKIP** — needs a ≥2400 px master from the merchant; the card cannot move right inside its grid column (it is already at column 2's start edge), and card-over-photo matches the mockup |
| S02 | No brand wordmark on the first screen (icon only) | F05 | major | **SKIP** — a lockup asset does not exist (`ElmsNest_Logo_Night.png` is the icon; the footer "ElmsNest" is Kalles' shop-name text). Ask the owner for a lockup PNG/SVG (icon + "ElmsNest", FRL 700, ink #f4eee3), then set `logo`/`logo_transparent`/`logo_mobile` + `logo_width` 150/120 |
| S03 | Letter-spacing .16–.22em + uppercase on Hebrew labels | T9 | minor | **SKIP** — §3.2 mandates it; the winning mockup used it; only the garden kicker wraps and its text is the approved phrase. (Toggle .22em is hidden on mobile by R21.) |
| S04 | Display leading .98 → 1.03 | T12 | minor | **SKIP** — §3.2 says .98; critic confirms no collision |
| S05 | Metric fallback faces for Android/iOS | T15 · Q16 | nit | **SKIP** — the override numbers are tuned for David/Times; adding Noto Serif Hebrew under the same overrides needs re-measurement; the Google Fonts CSS is already preconnected. Revisit with a fallback-font tool. |
| S06 | `label_no` ends in a maqaf | T10 (part) | nit | **SKIP** — §1/§4.4 copy "לא מתאים כש־ …": the maqaf is the join to the next line |
| S07 | "8–17" is the biggest number on the page; reorder rows | M15 | nit | **SKIP** — §4.7 mandates the four numbers; owner decision, not engineering |
| S08 | `innerHTML of null` console error | Q13 | minor | **SKIP** — Kalles `lazySubmenu` fetching `/search?section_id=`; not in env2 files. Confirm once on the dev-theme URL. |
| S09 | Hero empty-state when the product is unpublished | Q14 | minor | **SKIP** — editor-only; product is set; `bg_image` picker already exists |
| S10 | Footer accordion on mobile | F17 (part) | minor | **SKIP** — `collapse` is already `true` in footer-group.json and no accordion setting is exposed; Kalles admin |
| S11 | Quote 19 px on mobile | M16 (part) | nit | **SKIP** — §3.2 quote 22 on mobile |
| S12 | Hide the ₪ range on mobile | M12 (part) | nit | **SKIP** — §4.6 reach line = real count + real range |
| S13 | Move the דולק/כבוי toggle after the range in DOM | Q10 (part) · M8 (part) | nit | **SKIP** — G3 puts the toggle beside the index; hidden on mobile by R21; `aria-describedby` on the range instead |

Rulings where critics disagreed, after looking at the crops myself:

- **Hero note on mobile** — M4 (hide) vs T5 (keep, move after the CTAs). Hiding wins: the fold at 390×664 is
  the reason dusk won ("product + ₪ + buy inside the hero") and the note's device explanation is self-evident
  once the first lamp lights. Desktop keeps the note.
- **Photo promise repetition** — M10 (cut to hero + goodnight) vs the spec (hero, switch, terms, goodnight).
  Keep three: hero ghost CTA, terms row 4 (it is a term), goodnight (the closing ask). The switch's photo line +
  WhatsApp link go (settings, no code); the footer paragraph is rewritten; the goodnight strip keeps only its link
  on mobile and stays whole on desktop (G11 composition).
- **Mobile ghost button over the bollard** — F18 proposes re-ordering the CTAs; a re-order demotes the primary
  CTA. Give the ghost a scrim tint instead (`rgba(5,8,14,.35)` + blur), the page's one card surface.
- **Birch branches** — F07 proposes replacing with the Edison string (already in first-lit = a repeated product)
  or a filter. All four birch images are indoor; images[0] (grey wall, glass vases) is the darkest. Use it +
  a mild dim. Product stays (it is the only decor product not already on the page).
- **Wall spec separator** — Q9 (hairline or one-per-line) vs T7 (`::after` on the preceding item). `::after`:
  keeps the look, a trailing dot at a line end is normal.
- **Terms ₪** — T1's glue-before-split would put a trailing "." inside a `<bdi>` that resolves LTR
  ("₪ 29.90." misordered). Glue after the loop instead (`</bdi> ₪` → `</bdi>&nbsp;₪`), so the bdi stays
  digits-only and the sign cannot start a line.
- **Back-to-top** — Q1's fallback of restyling it bottom-left violates §7.11 (nothing fixed bottom-left). Hide.
- **Switch place-01** — the block's `object_position` cannot move a square source inside a 4/3 stage
  (width fills); mirroring is the only CSS fix; expose it as a per-block checkbox rather than a hard-coded
  `nth-child`.

## 2. Ranked list

**MUST (fix now):** R01 · R02 · R03 · R04 · R05 · R06 · R07 · R08 · R09 · R10 · R11 · R12
**SHOULD (fix now, contained):** R13 · R14 · R15 · R16 · R17 · R18 · R19 · R20 · R21 · R22 · R23 · R24 · R25 · R26 · R27 · R28 · R29 · R30
**SKIP:** S01–S13 (reasons in the table)

## 3. Work packages (one file = one package; ordered edits; acceptance = what the verifier checks)

Conventions: line numbers are from the current files; "mobile block" = the file's `@media (max-width:900px)`
block; contrast checks use the qa4-style method (screenshot the background patch with the text hidden, WCAG
luminance). Regenerate the screenshots with package P11 first, then verify the rest against fresh crops.

---

### P01 — `/home/user/ElmsNest/theme/snippets/elmsnest-v2-base.liquid` (+ `elmsnest-v2-buy.liquid`, `elmsnest-v2-price.liquid`)  — section: base

1. **[R01 MUST]** After line 39 add
   `body.hdt-page-type-index .hdt-back-to-top,body.template-index .hdt-back-to-top,body.hdt-page-type-index back-to-top{display:none!important}`
   (the element is `<back-to-top class="hdt-back-to-top hdt-back-to-top__design1 …">`, body class is `hdt-page-type-index`).
2. **[R14 SHOULD]** Replace line 75 with
   `@media (max-width:900px){.env2-btn{font-size:14px;padding:13px 20px}.env2-btn--sm{font-size:14px;padding:13px 18px}.env2-link{position:relative}.env2-link::before{content:"";position:absolute;inset:-11px -6px}}`
   (hit area 44 px without moving the hairline underline).
3. **[R25 SHOULD]** After line 39 add
   `body.hdt-page-type-index .shopify-section-group-footer-group{font-family:var(--env2-sans)}`
   `body.hdt-page-type-index .shopify-section-group-footer-group a{text-decoration:none}`
   `body.hdt-page-type-index .shopify-section-group-footer-group a:hover,body.hdt-page-type-index .shopify-section-group-footer-group a:focus-visible{text-decoration:underline}`
   (class confirmed in index.html: `shopify-section shopify-section-group-footer-group`).
4. **[R23 SHOULD]** In `elmsnest-v2-price.liquid` line 20 (wide-range branch) change `מ־<bdi>` to
   `<span class="env2-price__from">מ־</span><bdi>`; in base after line 60 add
   `.env2-price__from{font-family:var(--env2-sans);font-weight:400;font-size:.62em;color:var(--env2-ink-2);margin-inline-end:.15em;letter-spacing:0}`.
5. **[R16 SHOULD]** In `elmsnest-v2-buy.liquid` add a `link` parameter: when `link` is truthy and the product is
   not single-variant (both the `product.available` and sold-out branches), output
   `<a class="env2-link env2-buy__link" href="{{ product.url }}">{{ label | default: 'לבחירת דגם' }} <span aria-hidden="true">←</span></a>`
   instead of the ghost pill. Document it in the header comment (`link: true` → text link, used by the hanging trio).
6. **[R15 SHOULD]** In the base JS after the anchors block (line 188) add the ajax add-to-cart, mirroring Kalles'
   `ProductForm` (events verified in the bundle: `cart:update` with `detail{resource,sourceId,cartData,actionAfterATC,source,data}`; `hdt-cart-drawer[section-id][ref="hdt-cart"]` listens on `document` and calls `open()` when `source === 'product-form-component'`):
   ```js
   document.addEventListener('submit', function(e){
     var form = e.target && e.target.closest ? e.target.closest('form[data-env2-buy]') : null;
     var drawer = document.querySelector('hdt-cart-drawer[section-id]');
     if (!form || !drawer || !window.fetch || !window.FormData) return;           // no drawer / old browser → native POST
     e.preventDefault();
     var btn = form.querySelector('[type="submit"]'), fd = new FormData(form);
     fd.append('sections', drawer.getAttribute('section-id')); fd.append('sections_url', location.pathname);
     if (btn) { btn.disabled = true; btn.setAttribute('aria-busy', 'true'); }
     var root = (window.Shopify && Shopify.routes && Shopify.routes.root) || '/';
     fetch(root + 'cart/add.js', { method: 'POST', body: fd, headers: { 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/javascript' } })
       .then(function(r){ return r.json(); })
       .then(function(j){
         if (j.status) throw new Error(j.message || 'cart');
         document.dispatchEvent(new CustomEvent('cart:update', { bubbles: true, detail: {
           resource: {}, sourceId: String(fd.get('id')), cartData: j, actionAfterATC: 'open_cart_drawer',
           source: 'product-form-component', data: { itemCount: 1, sections: j.sections } } }));
       })
       .catch(function(){ form.submit(); })
       .then(function(){ if (btn) { btn.disabled = false; btn.removeAttribute('aria-busy'); } });
   });
   ```
   (Keep the plain form as the no-JS path. Do not add `return_to`.)

**Acceptance P01**
- After `window.scrollTo(0,3000)` at 1440 and 390, `getComputedStyle(document.querySelector('.hdt-back-to-top')).display === 'none'`; no pure-white rectangle in any regenerated crop (pixel scan for ≥ 30×30 px of #fff outside product photos).
- At 390: every `.env2-btn--sm` `getBoundingClientRect().height ≥ 44`; `document.elementFromPoint(x, linkTop-8)` returns the `.env2-link` for the places "לכל 27 המוצרים" link and the switch collection link.
- Footer computed `font-family` starts with "Heebo"; footer links `text-decoration-line: none`.
- crop-d-env2-first: the "מ־" prefix is visibly smaller than the digits and set in Heebo; the maqaf sits at x-height, not above the digits.
- `document.querySelectorAll('#env2-atmosphere .env2-btn').length === 0` after P07 uses `link: true`.
- Ajax cart: on the dev theme (online), tap "הוספה לסל" in the hero → the Kalles cart drawer opens with the item, `location.pathname` unchanged. Offline (file://) the fetch fails → the form submits natively (unchanged behaviour).

---

### P02 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-hero.liquid` — section: env2-hero

1. **[R05 MUST]** Mobile block (lines 146–166): replace lines 153–159 with
   `.env2-hero__wrap{grid-template-columns:1fr;gap:18px;padding-block:80px 48px}`
   `.env2-hero__note{display:none}`
   `.env2-hero__h1{font-size:clamp(54px,15.5vw,72px);margin:8px 0 12px}`
   `.env2-hero__lead{font-size:16px}`
   `.env2-hero__ctas{margin-top:16px;gap:10px}`
   and delete the mobile `.env2-hero__note-title` / `::after` rules (lines 155–156). Desktop note untouched.
2. **[R27/F18 SHOULD]** In the mobile block add `.env2-hero__ctas .env2-btn--ghost{background:rgba(5,8,14,.35);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}`.
3. **[R27/Q15 SHOULD]** Line 116–120 desktop scrim: prepend the layer `radial-gradient(40% 32% at 16% 24%,rgba(8,13,26,.5),rgba(8,13,26,0) 72%),` (darkens the lit grass under the note).
4. **[R27/F19 SHOULD]** Line 143: `inset-inline-end:22px` → `inset-inline-end:14px` and `font-size:10.5px` → `font-size:10px`.
5. **[R27/T8+Q11 SHOULD]** Line 96: `<h2 class="env2-hero__title">` → `<h3 class="env2-hero__title">` (closing tag too); line 135 add `text-wrap:pretty`.
6. **[R26 SHOULD]** In the liquid block (after line 30) compute capped width lists so the section and the preload agree by construction:
   ```liquid
   assign hero_widths = ''
   assign hero_want = '900,1400,1800,2400' | split: ','
   for w in hero_want
     assign wn = w | plus: 0
     if bg_desktop != blank and wn <= bg_desktop.width
       if hero_widths == '' ; assign hero_widths = w ; else ; assign hero_widths = hero_widths | append: ',' | append: w ; endif
     endif
   endfor
   if hero_widths == '' ; assign hero_widths = '900' ; endif
   ```
   and line 49 `widths: '900,1400,1800,2400'` → `widths: hero_widths`. Same capping for the mobile `<source>` (1000/1400 vs `bg_mobile.width`), and mirror the cap in `layout/theme.liquid`'s mobile preload (P10 item 9).

**Acceptance P02**
- Playwright 390×664 (hasTouch, real fonts): `#env2-hero` height ≤ 664 and the card's `button[name=add]` bottom ≤ 640; at 390×844 the card bottom is ≥ 44 px above the viewport bottom; `.env2-hero__note` display none at 390, visible at 1440 (unchanged position).
- crop-m-env2-hero: the ghost button's label is legible over the bollard (sampled contrast ≥ 4.5:1 against the tinted button background).
- crop-d-env2-hero: the note's p99 contrast ≥ 4.5:1 (qa4 method).
- crop-d-env2-places: the "שקיעה" label's right edge < the step-4 photo's left edge (57 px).
- Heading outline: `h1` → `h2 מה שנדלק ראשון` (no h2 between them); hero card title is an `h3`.
- On the dev theme HTML: the `<link rel="preload" media="(min-width: 901px)">` `imagesrcset` string equals the hero `<img srcset>` string byte-for-byte; same for the mobile pair.

---

### P03 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-first-lit.liquid` — section: env2-first

1. **[R29 SHOULD]** Line 140: `color:var(--env2-mute)` → `color:var(--env2-ink-2)`.
2. **[R16/T11 SHOULD]** Line 56: add `, small: true` to the big-card buy render so the section has one button size.
3. **[R27/Q11 SHOULD]** Line 8: add `aria-labelledby="env2-first-h2"`; line 15: add `id="env2-first-h2"`.

**Acceptance P03** — computed color of `.env2-first__var` is `rgb(201,196,184)`; all `.env2-btn` inside `#env2-first` have font-size 13.5 px at 1440 (14 px at 390); `document.getElementById('env2-first').getAttribute('aria-labelledby')` resolves to the h2.

---

### P04 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-places.liquid` — section: env2-places

1. **[R13 SHOULD]** Line 75: remove `text-align:end` (keep `justify-self:end`).
2. **[R19 SHOULD]** Add block setting `{ "type": "text", "id": "object_position", "label": "מיקום החיתוך בתמונה (object-position)", "default": "50% 50%", "info": "0% 50% = להצמיד לשמאל התמונה. נקודת מיקוד שנקבעה בממשק הניהול גוברת." }`; in the block liquid (line 29–38) `assign op = block.settings.object_position | default: '50% 50%' | strip | escape`, add `--env2-places-op:{{ op }}` to the inline style on line 39; CSS after line 81: `.env2-places__place .env2-places__ph img{object-position:var(--env2-places-op,50% 50%)}`. (index.json sets `0% 50%` for `place_wall` — P10.)
3. **[R18 SHOULD]** Mobile: replace lines 108–115 widths with `.env2-places__place{width:62vw}` / `:nth-child(2){width:50vw}` / `:nth-child(3){width:64vw}` / `:nth-child(4){width:52vw}` (aspects unchanged); after the strip (before line 63) render a mobile-only index row:
   `<nav class="env2-places__idx" aria-label="ארבעת המקומות">{% for block in section.blocks %}{% if block.settings.collection != blank %}<a href="{{ block.settings.collection.url }}"><bdi class="env2-places__idx-n">{{ forloop.index | prepend: '0' | slice: -2, 2 }}</bdi> {{ block.settings.title_short | default: block.settings.collection.title }}</a>{% endif %}{% endfor %}</nav>`
   CSS: `.env2-places__idx{display:none}` desktop; mobile `.env2-places__idx{display:flex;flex-wrap:wrap;gap:0 18px;padding:10px var(--env2-gut) 0;font-size:14px;color:var(--env2-ink-2)} .env2-places__idx a{padding-block:10px} .env2-places__idx-n{font-size:11px;letter-spacing:.16em;color:var(--env2-gold);margin-inline-end:4px}`. A text row (same pattern as the switch index), not a grid.
4. **[R20 SHOULD]** Line 72: `padding-block:120px 64px`; line 97: `margin-top:40px`; mobile line 119: `margin-top:20px`.
5. **[R27/Q11 SHOULD]** Line 17: `aria-labelledby="env2-places-h2"`; line 21: `id="env2-places-h2"`.

**Acceptance P04** — crop-d-env2-places: the intro's second line is flush with the first line's right edge; step-2 wall light fully inside its frame with the numeral clear of it; at 390 the first place and ≥ 40 % of the second are visible without scrolling and the index row lists four links (`.env2-places__idx a` count 4, each ≥ 44 px tall); at 1440 `.env2-places__idx` is display none; section height at 1440 ≤ 1000 px (was 1044).

---

### P05 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-switch.liquid` — section: env2-switch

1. **[R03 MUST]** Replace lines 343–344 (the `input`/`change` listeners) with a gesture guard for touch/pen (mouse and keyboard unchanged):
   ```js
   var g = null; // touch gesture: 0 undecided, 1 horizontal (drag the line), 2 vertical (page scroll)
   range.addEventListener('pointerdown', function(e){ if (e.pointerType === 'mouse') return; g = { x: e.clientX, y: e.clientY, v: +range.value, mode: 0 }; });
   range.addEventListener('pointermove', function(e){
     if (!g || g.mode) return;
     var dx = Math.abs(e.clientX - g.x), dy = Math.abs(e.clientY - g.y);
     if (dx < 6 && dy < 6) return;
     g.mode = dy > dx ? 2 : 1;
     if (g.mode === 2) { range.value = g.v; setV(g.v, false); } else { setV(range.value, false); }
   });
   function endGesture(e){
     if (!g) return;
     if (g.mode === 2 || e.type === 'pointercancel') { range.value = g.v; setV(g.v, false); }
     else if (g.mode === 0) { setV(range.value, false); }   // a tap: jump to the finger
     g = null;
   }
   range.addEventListener('pointerup', endGesture);
   range.addEventListener('pointercancel', endGesture);
   range.addEventListener('input', function(){ if (g && g.mode !== 1) return; setV(range.value, false); });
   range.addEventListener('change', function(){ if (g) return; setV(range.value, false); });
   ```
   Keep `touch-action:pan-y` on the range (line 231).
2. **[R04 MUST]** Per-block mirror: schema block setting `{ "type": "checkbox", "id": "mirror", "label": "להפוך את התמונה (ימין↔שמאל)", "default": false, "info": "כשהמנורה יושבת בצד החשוך בברירת המחדל." }`; line 77 add class `{% if block.settings.mirror %} is-mirrored{% endif %}` on `.env2-switch__place`; CSS after line 213: `.env2-switch__stage .env2-switch__place.is-mirrored .env2-switch__layer img{transform:scaleX(-1)}` (specificity (0,4,1) beats line 212's `transform:none`). Preset + index.json: `mirror: true` for the path block (P10).
3. **[R21/F11 SHOULD]** Line 170: `-webkit-text-stroke:1px rgba(255,211,148,.45)` → `1.5px rgba(255,211,148,.7)`.
4. **[R21/Q6 SHOULD]** Line 175: `opacity:.55` → `opacity:.78`; line 225: `.env2-switch__cap--lit .env2-switch__k{color:var(--env2-gold);font-size:12px;text-shadow:0 1px 10px rgba(0,0,0,.85)}`.
5. **[R21/M9+T10 SHOULD]** Line 228: `color:var(--env2-ink-2)` → `color:var(--env2-ink)`; mobile lines 280–282 → `.env2-switch__k{font-size:11px}` `.env2-switch__cap--dark .env2-switch__k{color:var(--env2-ink-2)}` `.env2-switch__p{font-size:15px;line-height:1.25}` `.env2-switch__cap--dark .env2-switch__p{font-size:15px;color:var(--env2-ink)}`; line 284 `.env2-switch__hint{font-size:12px}`.
6. **[R21/M8 SHOULD]** Mobile block: replace line 286 with `.env2-switch__toggle{display:none}`; add `.env2-switch__under{flex-wrap:wrap;gap:12px 20px}` and `.env2-switch__plink.env2-link{font-size:14px;color:var(--env2-ink);padding:12px 18px;border:0;box-shadow:inset 0 0 0 1px var(--env2-hair-btn);border-radius:999px}` (the knob is the switch on a phone; desktop toggle unchanged — G3).
7. **[R21/Q10 SHOULD]** In `select()` line 370:
   `places.forEach(function(p, j){ var on = j === i; if (on) { p.hidden = false; } p.setAttribute('aria-hidden', on ? 'false' : 'true'); requestAnimationFrame(function(){ p.classList.toggle('is-active', on); }); clearTimeout(p.__hideT); if (!on) p.__hideT = setTimeout(function(){ if (!p.classList.contains('is-active')) p.hidden = true; }, 520); });`
   and on line 106 add `aria-describedby="env2-switch-helper-{{ sid }}"` to the range with that id on the helper `<p>` (line 114).
8. **[R02 guard SHOULD]** Line 142–145: render the glyph and the label only when `wa_href contains 'wa.me'`; otherwise `<a class="env2-link env2-switch__wa" href="{{ wa_href }}">לשליחת תמונה</a>` (no glyph, no "וואטסאפ").
9. **[R20 SHOULD]** Line 157: `padding-block:100px 90px` → `padding-block:64px 90px`.
10. **[R28/T14 SHOULD]** Schema defaults line 447–448: quote `"כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה."` (straight double quotes), cite `מתוך "מי אנחנו"` (drop `elmsnest.com`).
11. **[R27/Q11 SHOULD]** Line 23: `aria-labelledby="env2-switch-h2"`; line 33: `id="env2-switch-h2"`.

**Acceptance P05**
- Playwright 390×844 hasTouch, CDP touch: (a) touchStart at the stage centre, six touchMoves straight up 150 px, touchEnd → `scrollY` increases and `--v` on the stage is unchanged (58 %); (b) touchStart centre, moves −120 px in x → `--v` changes; (c) a tap at 25 % of the stage width → `--v` ≈ 25 %. Mouse drag and keyboard (Arrow/Home/End) unchanged.
- crop-d-env2-switch at the default split: the bollard (place 01) sits inside the lit right side (its body between 55 % and 85 % of the stage width); at 390 (split 42) also inside the lit side; dragging to ≥ 88 % puts it out.
- Screenshot the section before it lights (block the IO by capturing with the section 60 % below the fold): "לא." outline visible (stroke pixels ≥ 45 % ink luminance on sky-2).
- Contrast: inactive `.env2-switch__tt` ≥ 4.5:1; `.env2-switch__cap--lit .env2-switch__k` p90 ≥ 4.5:1; dark caption 15 px ink on both viewports.
- At 390: `.env2-switch__toggle` display none; the collection link is a pill ≥ 44 px tall; the inactive `[role=tabpanel]`s have `hidden` and `aria-hidden="true"` 600 ms after a tab change; the range has `aria-describedby` resolving.
- Page has no "וואטסאפ" label whose href lacks `wa.me/` (after P10).
- Places link → switch eyebrow gap at 1440 ≤ 260 px (was ~330).

---

### P06 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-night-wall.liquid` — section: env2-wall

1. **[R07 MUST — headline]** Line 131: `grid-template-columns:minmax(0,1fr) minmax(0,.85fr)` → `minmax(0,1.15fr) minmax(0,.85fr)`; after line 134 add `@media (min-width:901px){.env2-wall__h2 .env2-wall__glow{white-space:nowrap}}` (desktop only — at 320 px nowrap would overflow).
2. **[R07 MUST — mobile seam]** Mobile block: add `.env2-wall__bg{-webkit-mask-image:linear-gradient(180deg,#000 55%,transparent 100%);mask-image:linear-gradient(180deg,#000 55%,transparent 100%)}` and change line 165 to `linear-gradient(0deg,var(--env2-sky-3) 0,rgba(7,11,21,.92) 34%,rgba(7,11,21,.55) 50%,rgba(7,11,21,.15) 70%,transparent 100%)` (the photo box ended in a hard edge at 62svh under the h2).
3. **[R07 SHOULD — grey haze]** Line 117 img rule: add `filter:brightness(calc(.17 + .61*var(--lit,1))) contrast(1.15) saturate(calc(.4 + .5*var(--lit,1)))` (keeps the dim→lit ramp; lit = .78/1.15/.9); line 126 veil: prepend `radial-gradient(42% 40% at 8% 10%,rgba(7,11,21,.45),rgba(7,11,21,0) 70%),` (corner haze only — do not dim the lamp's up-light).
4. **[R22 SHOULD]** Line 142 → `.env2-wall__opt:not(:last-child)::after{content:"·";margin-inline-start:14px;color:var(--env2-mute)}` and drop the `+ ::before` rule.
5. **[R14 SHOULD]** Mobile block: `.env2-wall__also{font-size:14px;padding-block:8px}`.
6. **[R27/Q11 SHOULD]** Line 33: `aria-labelledby="env2-wall-h2"`; line 53: `id="env2-wall-h2"`.

**Acceptance P06** — at 1440, 1280, 1024 and 901 the h2 renders exactly two lines ("הלילה כבר כאן." / "קיר אחד מספיק.") with no horizontal overflow (`scrollWidth === clientWidth`); at 390 and 320 two lines, no overflow. crop-m-env2-wall: no horizontal luminance step between y 480–560 CSS (max adjacent-row mean-L delta < 6). crop-d-env2-wall: mean luminance of x0–400,y0–200 lower than the current render by ≥ 20 %, lamp edge highlight still visible. No line of `.env2-wall__spec` begins with "·" at either viewport. Companion link ≥ 36 px tall at 390.

---

### P07 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-atmosphere.liquid` — section: env2-atmosphere

1. **[R08 MUST]** Line 164: `box-shadow:0 0 6px 1px rgba(255,211,148,.95),0 0 22px 7px rgba(247,162,74,.38),0 0 60px 18px rgba(247,162,74,.14)` → `box-shadow:0 0 6px 1px rgba(255,211,148,.95),0 0 18px 6px rgba(247,162,74,.35);mix-blend-mode:screen` (screen cannot go darker than the sky).
2. **[R09 MUST]** Mobile block, replace lines 206–211 with:
   `.env2-atm__band{height:auto;margin-top:-30px;display:flex;align-items:flex-end;gap:18px;padding:44px var(--env2-gut) 36px;padding-inline-end:56px;overflow-x:auto;scroll-snap-type:x proximity;scroll-padding-inline:var(--env2-gut);scrollbar-width:none;-webkit-overflow-scrolling:touch;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 48px,#000 100%);mask-image:linear-gradient(90deg,transparent 0,#000 48px,#000 100%)}`
   `.env2-atm__hang{position:relative;flex:0 0 var(--env2-atm-mw,200px);width:var(--env2-atm-mw,200px);margin:0;scroll-snap-align:start}`
   `.env2-atm__hang::before{display:block;top:-44px;bottom:auto;height:44px;inset-inline-start:50%}`
   (drop-lines back, band pulled up under the string, end edge fades instead of chopping). Add after the band (inside `.env2-atm__stage`) `<p class="env2-atm__helper" aria-hidden="true">גללו ←</p>` with `.env2-atm__helper{display:none}` desktop / mobile `display:block;margin:-24px var(--env2-gut) 0;font-size:12px;letter-spacing:.04em;color:var(--env2-mute)`. Widths 230/200/170 stay.
3. **[R17 SHOULD]** Block schema: `{ "type": "checkbox", "id": "tone_down", "label": "להכהות מעט (לתמונות בהירות)", "default": false }`; line 97 add class `{% if block.settings.tone_down %} env2-atm__hang--dim{% endif %}`; CSS after line 174: `.env2-atm__hang--dim .env2-atm__ph img{filter:brightness(calc(.18 + .62*var(--lit,1))) saturate(calc(.4 + .5*var(--lit,1)))}` (lit = .8/.9). index.json (P10): birch `image_index: 1` (images[0], grey wall) + `tone_down: true`.
4. **[R16 SHOULD]** Line 112: `{% render 'elmsnest-v2-buy', product: product, label: block.settings.button_label, link: true %}`; CSS `.env2-atm__buy .env2-link{font-size:13.5px}`.
5. **[R13 SHOULD]** Line 141: remove `text-align:end`.
6. **[R22/T7 SHOULD]** Line 127: `<span class="env2-atm__dot env2-atm__dot--link">·</span>`; mobile `.env2-atm__dot--link{display:none}`.
7. **[R30 SHOULD]** Wrap lines 15–20 in `{% paginate collections.all.products by 250 %} … {% endpaginate %}` (the `map`s then see up to 250 products).
8. **[R27/Q11 SHOULD]** Line 23: `aria-labelledby="env2-atmosphere-h2"`; line 37: `id="env2-atmosphere-h2"` on the word.

**Acceptance P07** — luminance profile around a lit bulb centre in crop-d-env2-atmosphere is monotonically non-increasing from r=10 to r=100 (no dip below the sky value; the current profile is 34→25→23→28→32). crop-m-env2-atmosphere: each card has a drop-line reaching the string (no black band > 30 px between the wire's low point and the card tops); the left edge fades over ~48 px; "גללו ←" visible under the band; the crystal card's title starts inside the viewport or is visibly faded, not chopped. Birch card mean luminance ≤ the crystal card's; no cream rectangle. `#env2-atmosphere .env2-btn` count 0, three `.env2-link` buy links. Sub line ragged on the left, flush right. Reach line unchanged in content (27 · 69.90–999.90 ₪).

---

### P08 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-terms.liquid` — section: env2-terms

1. **[R10 MUST — ₪]** After the word loop (line 59) add `assign line_text = line_text | replace: '</bdi> ₪', '</bdi>&nbsp;₪' | replace: '</bdi> %', '</bdi>&nbsp;%'` (the bdi stays digits-only; the sign can no longer start a line).
2. **[R10 MUST — h2]** Line 106: `max-width:11ch` → `max-width:15ch`.
3. **[R13 SHOULD]** Line 107: remove `text-align:end`.
4. **[R20 SHOULD]** Line 99: `padding-block:110px 90px`; line 111: `padding:30px 0` → `padding:24px 0`.
5. **[R14 SHOULD]** Mobile block: `.env2-terms__foot{font-size:13.5px}` `.env2-terms__foot-a{padding-block:8px}` `.env2-terms__a{padding-block:8px}`.

**Acceptance P08** — at 1440 and 390 no line in `.env2-terms__p` begins with "₪" (Range-rect check per text node); row 1 still reads "משלוח עד הבית: 29.90 ₪." in order; h2 is exactly two lines ("ארבעה מספרים" / "שכדאי לדעת") at 1440; the intro's line 2 is flush with line 1's right edge; section height at 1440 ≤ 1250 px (was 1365).

---

### P09 — `/home/user/ElmsNest/theme/sections/elmsnest-v2-goodnight.liquid` — section: env2-goodnight

1. **[R06 MUST]** Line 117: `padding-block:120px 40px` → `padding-block:150px 40px`; line 121: `height:62%` → `height:78%`, `opacity:calc(.8*var(--lit,1))` → `opacity:calc(.95*var(--lit,1))`; line 122 veil → `linear-gradient(180deg,rgba(2,3,6,.45) 0,rgba(2,3,6,.08) 40%,rgba(2,3,6,.5) 100%)`; line 123 add `filter:saturate(1.1) contrast(1.06)`; line 148 stroke → `-webkit-text-stroke:1.5px rgba(244,238,227,calc(.3 + .35*var(--lit,1)))` (still outline-only, never filled — §7.9). Mobile line 153: `height:72%`.
2. **[R02 guard SHOULD]** Lines 55–58: when `wa_href contains 'wa.me'` render the glyph + `whatsapp_label`; else render `<span>לשליחת תמונה</span>` with no glyph.
3. **[R11 SHOULD]** Mobile block: `.env2-goodnight__strip-i,.env2-goodnight__dot{display:none}` (the strip keeps only "לתנאים המלאים ←" on phones; desktop keeps the whole G11 line).
4. **[R14 SHOULD]** Mobile block: `.env2-goodnight__strip{font-size:13.5px}` `.env2-goodnight__strip-a{padding-block:8px}`.

**Acceptance P09** — crop-d-env2-goodnight: mean luminance of the bottom 60 % band ≥ 1.6× the current render; string bulbs read as warm points (local maxima with R > G > B), not grey discs; "לילה טוב" stroke clearly visible (stroke pixels ≥ 55 % of ink luminance); the word is not filled. With `settings.whatsapp_number` blank the pill reads "לשליחת תמונה" without an icon; with a number it reads "וואטסאפ" with the icon and `target=_blank`. At 390 the strip shows only the link.

---

### P10 — template / config: `/home/user/ElmsNest/theme/templates/index.json` (+ `config/settings_data.json`, `sections/header-group.json`, `sections/footer-group.json`, `layout/theme.liquid`) — section: template

1. **[R02 MUST]** `config/settings_data.json` → `whatsapp_number`: **needs the owner's number (E.164, 9725XXXXXXXX)** — request it in the hand-off; do not invent one. Until it exists, make every label honest: `footer-group.json` line 203 → `<p><a href="/pages/contact-us">עמוד יצירת קשר</a></p><p><a href="/pages/contact-us">לשלוח תמונה של המקום</a></p>` (no bare `wa.me/`, no "וואטסאפ"); `index.json` `env2_terms.blocks.line_photo.settings.title` → `"שלחו תמונה של המקום."` (restore "בוואטסאפ" when the number is set); `env2_switch.settings.whatsapp_url` and `env2_goodnight.settings.whatsapp_url` → `""` (fall back to the theme setting, not the `https://wa.me/` sentinel). When the number arrives, set it once in settings and revert the two label edits.
2. **[R11 MUST]** `index.json` `env2_switch.settings.photo_line` → `""`, `whatsapp_label` → `""` (the promise stays in hero, terms, goodnight). `footer-group.json` line 49 intro text → `<p>שאלות על מוצר או על התאמה למקום? כתבו לנו: info@elmsnest.com</p>` (the address already ships in the header's mobile note; no new facts). Line 276 copyright → `<p>ElmsNest © 2026 · <a href="/#env2-terms">תנאי משלוח וביטול</a></p>`.
3. **[R24 SHOULD]** `header-group.json` lines 60–61: `background_opacity_sticky: 0.92`, `sticky_glass: false`.
4. **[R28/Q18 SHOULD]** `index.json`: `env2_hero.settings.card_title_override` → `""`, `env2_night_wall.settings.title_override` → `""`, `env2_goodnight.settings.instagram_url` / `tiktok_url` → `""` (they resolve from `settings.social_instagram_link` / `social_tiktok_link`, which hold the same URLs).
5. **[R28/M12 SHOULD]** `env2_atmosphere.settings.reach_link` → `"#env2-places"`.
6. **[R28/T14 SHOULD]** `env2_switch.settings.quote` → `"כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה."` (straight double quotes), `quote_cite` → `מתוך "מי אנחנו"`.
7. **[R04]** `env2_switch.blocks.sw_path.settings.mirror` → `true`.
8. **[R17]** `env2_atmosphere.blocks.hang_birch.settings.image_index` → `1`, `tone_down` → `true`.
9. **[R19]** `env2_places.blocks.place_wall.settings.object_position` → `"0% 50%"`; other three `"50% 50%"`.
10. **[R26]** `layout/theme.liquid` lines 76–80: cap the mobile preload's widths with the same `<= en_hero_mob.width` rule the desktop one uses (so both pairs match the hero's capped lists from P02).

**Acceptance P10** — rendered HTML: `grep -c 'wa.me/"'` = 0; every anchor whose text contains "וואטסאפ" has an href containing `wa.me/972` (if no number: zero anchors contain "וואטסאפ"); the switch foot shows quote + guide link only; footer intro paragraph is not the hero lead; copyright starts "ElmsNest © 2026"; scrolling up mid-page the sticky bar is near-opaque (no headline visible through it in crop-*-env2-switch/terms); hero card title equals `product.title` from Liquid ("מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65"); socials still render; reach link href `#env2-places`; the quote renders with straight quotes and the cite has no domain.

---

### P11 — `/home/user/ElmsNest/brief/shot.js` — section: template (QA harness)

1. **[R12 MUST]** Before the scroll walk (line 20) set `document.documentElement.style.scrollBehavior = 'auto'` inside the evaluate, or use `window.scrollTo({ top: y, behavior: 'instant' })`; after returning to the top wait ≥ 2600 ms (line 23: 1800 → 2600) so the 1.6–2.4 s lamp transitions finish; then capture. Regenerate `shot-desktop.png`, `shot-mobile.png`, both folds and all `crop-*.png`, and use the fresh crops for the verification of P01–P10.

**Acceptance P11** — in the regenerated full-page PNGs every lamp is lit: places numerals gold (not outlined), switch bollard lit, wall photo bright, string bulbs on, goodnight garden visible (sample: mean luminance of the wall crop's lamp region ≥ 3× the unlit render).

## 4. Skipped (with reasons) — see S01–S13 in the table

The two that the owner will notice and that need him: a ≥ 2400 px hero master (S01) and a brand lockup for the
header (S02). Ask for both in the same message as the WhatsApp number.

## 5. Verification order

1. P11 (regenerate screenshots) → 2. P01 base → 3. P10 config → 4. P02 hero → 5. P05 switch → 6. P06 wall →
7. P07 atmosphere → 8. P09 goodnight → 9. P08 terms → 10. P04 places → 11. P03 first-lit → regenerate again and
re-run the acceptance checks above; then the 390×664 fold run, the touch-gesture run, and the contrast table.
