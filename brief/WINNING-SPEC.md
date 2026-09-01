# ElmsNest homepage v2 — WINNING SPEC (build-ready)

Design lead decision, 2026-09-01. Read after `BRIEF.md`, before `THEME-NOTES.md`.
Winner: **dusk (השעה הכחולה)** with the honesty device rebuilt from **switch** + **one** + **map**.
Reference mockup: `/home/user/ElmsNest/brief/concepts/dusk/index.html` (lift CSS/JS from it; §8).

---

## 1. The one idea

**The page is dusk turning into night.** One sky gradient runs down the whole document — blue-hour
indigo behind the hero, true black behind the footer — and every lamp on the page (product photo,
collection scene, the "לא." in the headline, the string of bulbs, the garden in the footer) is dim
until you reach it, then lights. The honest positioning is the one place on the page where a lamp
is allowed to stay dark: a photo split by a draggable line — lit on one side with "מתאים כדי…", dark
on the other with "לא מתאים כש־…" — and dragging the line all the way puts the lamp out.

**Why dusk beats the others (judges split 1–2; this is the ruling and the reason):**

- Two judges ranked *switch* first because its rocker makes the brand position the page's mechanism.
  They are right about the mechanism and wrong about the page: switch's idea lives in an OFF state
  no still ever shows, its execution carries three things the brief bans outright (brown-on-cream
  WhatsApp panel, skeuomorphic beige rocker plate, seven equal shelf cards + default footer), and
  the owner judges from screenshots first. Dusk is the only concept whose idea is *visible in a
  still* (the full-page capture actually goes indigo → black), the only one with a colour idea
  rather than a palette, the best first screen of the five on both viewports (product + ₪ + buy
  inside the hero), and the most editorial typography (Frank Ruhl Libre at 150px against Heebo
  labels). Aggregate score also puts it first (141 vs 140).
- Dusk's one real flaw — the honesty section is eight identical SVG bollards in four identical
  rows, all rendering lit — is exactly the part switch/one/map do better. So the honesty section is
  **replaced**, not patched: one stage, one divider you drag, four places you pick. Everything else
  in dusk is kept and its listed defects are fixed in this spec (five-box shelf replaced, clipped
  mobile numerals fixed, v1 hero photo replaced, firefly caption cropped).

---

## 2. Grafts (what is absorbed from the other concepts, and exactly where)

| # | From | Device | Where it lands in the build |
|---|------|--------|-----------------------------|
| G1 | **switch** (place 01) | Draggable lit/unlit divider over one photograph (`clip-path: inset(0 0 0 var(--v))`, range input on top, knob) | §4.4 `elmsnest-v2-switch` — the entire honesty section is this one stage |
| G2 | **map** (switchboard) | Flipping a place OFF makes the "does not suit" reason physically replace the promise | §4.4 — the dark half carries "לא מתאים כש־ …"; drag to ≤12 % lit and the lamp goes out and the hint appears |
| G3 | **one** (chapter switch) | OFF rendering = photo at ~9 % brightness (not a grey filter); tiny tracked two-position label with a hairline gold underline on the active state | §4.4 — dark layer filter `brightness(.09) saturate(.3)`; the "דולק · כבוי" quick toggle above the stage |
| G4 | **dusk** (own device, kept as a detail) | The dark lamp refuses to light — "לא נדלק. זו הנקודה." | §4.4 — hint that fades in at the dark extreme; a 240 ms flicker on the halo when crossing the threshold |
| G5 | **lit** (statement) | "אנחנו נגיד לכם גם מתי לא." where the word "לא." switches on like a lamp | §4.4 — it is the section's h2; "לא." is outline-only until the section enters view, then lights gold with one flicker |
| G6 | **switch** (shelf captions) | One-line verdict attached to every buy row ("מתאים: לראות את הדרך") | §4.2 — the kicker above each of the four products is `place · approved suits-phrase`; no separate verdict row |
| G7 | **switch** (place 03) | The photo-filled headline word (`background-clip:text` over the string-light photo) | §4.6 `elmsnest-v2-atmosphere` — replaces dusk's five-box shelf |
| G8 | **map** (terrace) | The sagging string of bulbs that physically hangs over the terrace products | §4.6 — SVG catenary under the word; the three products hang from it at different heights |
| G9 | **one** (companion) | Caption-sized "גם ל…" companion product under the hero product (restrained upsell, no card grid) | §4.5 `elmsnest-v2-night-wall` — one line under the price |
| G10 | **lit** (hero) | The hero photo *is* product 01 | §4.1 — the hero background is the stainless path light's own night shot and the hero card sells that lamp ("המנורה שבתמונה") — this also retires the v1 pergola photo |
| G11 | **switch / map** (footer strip) | A single hairline line carrying the four consumer terms | §4.8 `elmsnest-v2-goodnight` — one line above the Kalles footer, so terms are findable twice (ledger + strip) |

Not grafted, deliberately: switch's rocker plate (skeuomorphic), map's plan/pills/toggles (UI-kit),
lit's Karantina volume and marquee, one's collapsed 27-row index, map's mobile chips.

---

## 3. Global design system

### 3.1 Palette (exact)

| Token | Hex | Use |
|-------|-----|-----|
| `--env2-sky-0` | `#4a6a9c` | blue hour — top of document (behind hero) |
| `--env2-sky-1` | `#1f3357` | early night — behind "מה שנדלק ראשון" |
| `--env2-sky-2` | `#0f1a2f` | night — behind places / switch |
| `--env2-sky-3` | `#070b15` | deep night — wall / atmosphere / terms |
| `--env2-sky-4` | `#020306` | full night — goodnight + Kalles footer + `html` background |
| `--env2-ink` | `#f4eee3` | primary text |
| `--env2-ink-2` | `#c9c4b8` | secondary text, leads |
| `--env2-mute` | `#8f95a3` | tertiary (≥ 4.5:1 on sky-2 and darker only — never on sky-0/1) |
| `--env2-gold` | `#e9b96e` | kickers, rules, active states |
| `--env2-glow` | `#ffd394` | prices, lit numerals, primary button fill, halos |
| `--env2-ember` | `#f7a24a` | halo core only (radial gradients), never text |
| `--env2-btn-ink` | `#1a1206` | text on glow buttons |
| hairline | `rgba(244,238,227,.12)` | all rules; `.25` for outlined buttons; `.45` for outlined numerals |
| scrim | `rgba(5,8,14,.55)` + `backdrop-filter: blur(10px)` | the only "card" surface (hero card, big-product caption) |

**Page ground (the idea):** one gradient on the document, not per section.
```css
html{background:#020306}
body.template-index{
  background:linear-gradient(180deg,#4a6a9c 0%,#1f3357 14%,#0f1a2f 34%,#070b15 58%,#020306 100%) no-repeat;
  background-size:100% 100%;
}
/* Kalles paints wrappers — make them transparent on the index template only */
.template-index #wrapper,.template-index .main-content,.template-index main{background:transparent}
```
All eight sections are background-transparent except `elmsnest-v2-night-wall` (its photo + veil) —
the sky must be visible between sections. Stars: static CSS radial-gradient layer (`.env2-stars`,
copy from dusk `.stars`) with per-section opacity: places .18 → switch .30 → atmosphere .45 →
terms .55 → goodnight .70. No stars on hero, first-lit, wall.

No brown, no beige, no cream anywhere. Gold is an accent, not a surface (max surface: the pill button).

### 3.2 Type

Loaded once, from `snippets/elmsnest-v2-fonts.liquid`, rendered only by the hero:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@500;700;900&family=Heebo:wght@300;400;500&display=swap">
<style>
@font-face{font-family:"FRL Fallback";src:local("David"),local("Times New Roman");size-adjust:94%;ascent-override:92%;descent-override:26%;line-gap-override:0%}
:root{--env2-serif:"Frank Ruhl Libre","FRL Fallback","Noto Serif Hebrew",serif;--env2-sans:"Heebo","Assistant",system-ui,sans-serif}
</style>
```
(Assistant is already loaded by the theme, so Heebo's fallback is metric-close; the serif fallback
carries `size-adjust` so the hero h1 does not jump on swap. Tune the override numbers once with a
fallback-font tool; do not skip them.)

| Role | Face / weight | 1440 px | 390 px | Notes |
|------|---------------|---------|--------|-------|
| h1 hero | Frank Ruhl Libre 700 | `clamp(54px,9.4vw,150px)` → 135 | `clamp(54px,15.5vw,72px)` → 60 | line-height .98, `letter-spacing:-.01em`, `text-wrap:balance`, second line in glow |
| h2 section | FRL 700 | `clamp(40px,5.6vw,84px)` → 80 | 40 | line-height .98 |
| h2 wall | FRL 700 | `clamp(46px,7.2vw,118px)` → 104 | `clamp(48px,14vw,64px)` → 55 | line-height .95 |
| "אווירה" word | FRL 900 | `clamp(96px,24vw,340px)` → 340 | 96 | line-height .9, photo-filled |
| place numerals 1–4 | FRL 900 | `clamp(90px,10vw,170px)` → 144 | 88 | outline → glow when lit |
| ledger numerals | FRL 500 | `clamp(52px,7vw,104px)` → 100 | 58 | tabular-nums, unit at .32em |
| "לילה טוב" | FRL 900 | `clamp(48px,9vw,140px)` → 130 | 48 | outline only, never filled |
| price | FRL 500 | 26 (hero card) · 30 (big) · 34 (wall) · 24 (item) · 19 (small) | −4 px each | `font-variant-numeric:tabular-nums`, colour glow, `white-space:nowrap` |
| quote | FRL 400 | `clamp(22px,2.4vw,32px)` | 22 | line-height 1.25 |
| lead | Heebo 300 | `clamp(17px,1.4vw,21px)` | 16 | max-width 38ch, colour ink-2 |
| body | Heebo 300/400 | 15–16 | 15 | line-height 1.55 |
| product title | Heebo 400 | 15–19 | 15 | never the display face |
| kicker / label | Heebo 500 | 11–12 | 11 | `letter-spacing:.16–.18em`, `text-transform:uppercase` (Latin only), gold |
| button | Heebo 500 | 15 | 14 | |
| nav (Kalles) | theme | | | leave |

Latin tokens inside Hebrew (`IP65`, `LED`, `6W`, `USB-C`) go inside `<bdi>` in authored copy;
Liquid-rendered product titles get `unicode-bidi:isolate` and an engineer eyeballs
"IP65 – 6W/12W" once. Prices render as `<bdi>{{ n }}</bdi> ₪` — number first, then the sign.

### 3.3 Spacing, width, radius

- `--env2-gut: clamp(20px,4vw,64px)`; container `.env2-wrap{width:min(1240px,100% - 2*var(--env2-gut));margin-inline:auto}`;
  the places strip is wider: `min(1500px,100% - 2*gut)`; the switch stage, wall and word are full-bleed.
- Section padding-block: desktop `120px / 80–120px`, mobile `72px / 56px`. Hero and wall are `min-height:100svh`.
- Vertical rhythm on an 8 px base; hairlines separate ledger rows; no boxes.
- **Radius policy:** `0` on every image, card, stage and input. `999px` only on pill buttons and the
  divider knob (a circle). Nothing in between. Theme radii stay 0.
- Logical properties everywhere (`inset-inline-start`, `margin-inline`, `padding-inline`) — Sense RTL flips physical ones.

### 3.4 Motion principles (what moves, and why)

1. **Lamps light on arrival.** Any `[data-lamp]` starts dim and lights once when 25 % of it is in view
   (IntersectionObserver, `rootMargin:'0px 0px -6% 0px'`); it never goes dark again on scroll-up.
   ```css
   .env2-js [data-lamp]{--lit:0} .env2-js [data-lamp].lit{--lit:1}
   [data-lamp] .env2-ph img{filter:brightness(calc(.22 + .78*var(--lit,1))) saturate(calc(.4 + .6*var(--lit,1)));transition:filter 1.6s cubic-bezier(.2,.7,.2,1)}
   [data-lamp] .env2-ph::after{/* warm halo, radial, mix-blend-mode:screen */opacity:var(--lit,1);transition:opacity 1.6s .2s}
   ```
   No-JS / JS-failed = everything lit (`--lit` defaults to 1; the dim rule only applies under `html.env2-js`,
   which the base snippet adds with an inline script before any section paints).
2. **The sun goes down.** A fixed hairline rail (desktop only, `inset-inline-end:22px`, vertically centred)
   with a 9 px glowing dot whose `top` = scroll progress `--p` (rAF on passive scroll). Labels שקיעה / לילה.
   The hero photo darkens with the same `--p`: `brightness(max(.45, 1 - 2.2*var(--p)))`.
3. **One thing switches on per section**, and it is the thing the section is about: the "לא." (switch),
   the numerals (places), the bulbs on the string (atmosphere), the garden (goodnight). Nothing else animates.
4. **The divider** follows the pointer with `transition:clip-path .12s linear`; place change crossfades .5 s.
5. **Hover:** buttons `translateY(-2px)` + glow shadow `.35s cubic-bezier(.2,.8,.2,1)`; links colour `.3s`. No scale, no bounce.
6. Nothing autoplays; no parallax; no fade-in-on-scroll for text.

**Reduced motion (`prefers-reduced-motion: reduce`):** all transitions/animations off; every lamp rendered
lit; hero brightness fixed at 1; sun rail hidden; "לא." rendered lit; divider still draggable (instant);
place change instant; string bulbs all on. Anchor scrolls use `behavior:'auto'`.

### 3.5 Shared plumbing (build once)

- `snippets/elmsnest-v2-fonts.liquid` — §3.2. Rendered by hero only.
- `snippets/elmsnest-v2-base.liquid` — rendered by hero only: `<script>document.documentElement.classList.add('env2-js')</script>`,
  the page gradient, tokens, `.env2-stars`, `[data-lamp]` rules, `.env2-btn` / `.env2-btn--ghost` / `.env2-link` /
  `.env2-eyebrow` (gold 34 px rule + tracked label), `.env2-price`, and `window.env2 = {observe(root), rm}`
  (the IO + sweep + `--p` scroll code from dusk lines 736–786). Every other section's JS ends with
  `window.env2 ? env2.observe(sectionEl) : sectionEl.querySelectorAll('[data-lamp]').forEach(l=>l.classList.add('lit'))`
  so a page without the hero still renders lit.
- `snippets/elmsnest-v2-price.liquid` — input `product`; prints `<span class="env2-price"><bdi>…</bdi> ₪</span>`.
  Rule: if `product.price_varies == false` → the price; else if `price_max <= price_min * 1.25` → `min–max ₪`;
  else → `מ־min ₪`. (Wall light 219.90–252.90 shows a range; crystal balls 89.90–179.90 shows מ־89.90.)
- `snippets/elmsnest-v2-buy.liquid` — input `product`, `label`: single variant → `<form method="post" action="{{ routes.cart_add_url }}">`
  with hidden `id`/`quantity=1` and a `.env2-btn` submit "הוספה לסל"; multi-variant → `<a class="env2-btn env2-btn--ghost" href="{{ product.url }}">{{ label | default: 'לבחירת דגם' }}</a>`.
- Anchors: every section root has `id="env2-<name>"` and `scroll-margin-top:90px`.
- WhatsApp: one `whatsapp_url` setting per section that needs it (default `https://wa.me/`; the lead fills the
  number from `snippets/elmsnest-whatsapp.liquid`), with prefilled text
  `שלום, אשמח לבדוק התאמה — מצרף/ת תמונה של המקום.` The floating snippet stays bottom-left; nothing fixed is placed there.

### 3.6 Image ledger (every slot, decided — indexes are 0-based `product.images[i]`; Shopify admin position = i+1)

| Slot | Source | Why / crop |
|------|--------|-----------|
| Hero bg desktop | `stainless-steel-solar-path-light-ip65` images[0] | three bollards along a brick path, dusk sky at top, text-free. `object-position:50% 40%`. **Replaces the v1 pergola webp.** |
| Hero bg mobile | same product images[0] | `object-position:22% 50%` (front bollard + hedge fill the portrait crop) |
| Hero card thumb | same product images[3] | bollard by brick wall + steps, text-free. aspect 1/1.1 |
| First-lit big | `outdoor-bidirectional-led-wall-light-ip65` images[0] | up/down wall light on a house at dusk, text-free. aspect 4/5 |
| First-lit small 1 | `powerful-solar-garden-light` images[2] | path lights along a walkway; tiny caption at bottom → aspect 1/.88 + `object-position:50% 0` crops it |
| First-lit small 2 | `solar-edison-string-lights` images[3] | Edison bulbs over a table with the solar panel, text-free. aspect 1/1.05 |
| First-lit small 3 | `solar-firefly-garden-lights` images[3] | fireflies close-up; aspect 1/.84 + `object-position:50% 0` crops the bottom 10 % (any residual tag) |
| Places 1–4 | `collection.featured_image` of path / wall / spot / decor | night scenes, text-free; aspects 5/4 · 3/4.6 · 4/3.2 · 3/4.1 |
| Switch stage 01 | `stainless-steel-solar-path-light-ip65` images[1] | single bollard in dark bushes — the dark state reads as "lamp off". aspect 4/3, `object-position:45% 50%` |
| Switch stage 02 | `modern-led-wall-light-6w-up-down` images[0] | two up/down cubes on a wall, text-free. aspect 4/3 |
| Switch stage 03 | `solar-crystal-ball-string-lights` images[2] | crystal balls on a wooden trellis, text-free. aspect 4/3 |
| Switch stage 04 | `solar-firefly-garden-lights` images[2] | fireflies in a flower bed in front of a cabin (= ערוגה); small caption bottom-right → aspect 4/3 + `object-position:50% 20%` |
| Wall (full viewport) | `waterproof-led-wall-light-ip65-6w-12w` images[3] | wide black wall light lit on plaster, text-free. `object-position:30% 50%` desktop / `45% 50%` mobile |
| "אווירה" fill | `collection.featured_image` of decor (string lights under a tree) | `background: … center 34% / cover` |
| Atmosphere hang 1 | `solar-crystal-ball-string-lights` images[0] | close-up, text-free. width 300, aspect 1/1.1 |
| Atmosphere hang 2 | `solar-rope-string-lights` images[2] | rope light on a tree; IP65 badge top-left → aspect 4/3 + `object-position:50% 100%` crops the top 25 % |
| Atmosphere hang 3 | `lighted-birch-branches-20-led` images[1] | birch branches in a white vase, text-free. width 200, aspect 1/1.4 |
| Goodnight garden | `collection.featured_image` of decor | at 80 % opacity under a sky-4 gradient, `object-position:50% 70%` |

Never use on this page (baked-in marketing text at any readable size): images of `retro-solar-path-lights-set`,
`warm-solar-step-deck-lights`, `waterproof-solar-deck-step-lights`, `solar-garden-lantern-9-led`,
`solar-garden-spotlight-52-led`, `solar-security-light-100-led`, `modern-solar-path-lights-set`,
`solar-floodlight-ip67-remote-timer`, `decorative-led-net-lights`, `led-globe-string-lights`,
`modern-led-bollard-light-5w-ip65`, `rechargeable-telescopic-camping-lantern`, `swaying-solar-path-lights-ip65`,
`magnetic-rechargeable-touch-wall-light`, and `dual-head-garden-light-10w-ip65` images[1–3]. They are still
sold — reach them through the collection links and "לכל 27 המוצרים".

Every image slot is a schema setting (product picker + `image_index` range 1–4, or `image_picker` override),
so the merchant can swap without code; the defaults above are what ships. Guard `product.images[i]` with
`| default: product.featured_image`.

---

## 4. Section-by-section build spec (final page order)

Legend for layout sketches: `▲` start side (right in RTL), `▼` end side (left).

### 4.1 `elmsnest-v2-hero` — the last minute of daylight

**Purpose.** Screen 1 on both viewports: the idea (dusk), the brand line, and a real product with ₪ and
add-to-cart. The header is transparent over it (THEME-NOTES); the hero runs under the bar.

**Copy (exact).**
- note (small caption, top-end): **השעה הכחולה** — `הדקות שבין השקיעה ללילה. הדף הזה מחשיך איתן, וכל מנורה נדלקת כשמגיעים אליה.`
- eyebrow: `תאורת חוץ, לפי המקום`
- h1: `כשהשמש יורדת,` / (glow) `הגינה נדלקת.`
- lead: `מנורות שביל, קיר, מרפסת וגינה. קטגוריה אחת בלבד — ואם מוצר לא מתאים למקום שלכם, נגיד את זה לפני שתזמינו.`
- primary button: `לארבע הקולקציות` → `#env2-places`
- ghost button: `לשלוח תמונה של המקום` → WhatsApp
- card kicker: `המנורה שבתמונה · שביל` · card title: product title (default override `מנורת שביל סולארית מנירוסטה, תאורה אוטומטית IP65`) · price via snippet (`169.90 ₪`) · button `הוספה לסל`
- sun rail labels: `שקיעה` / `לילה`

**Layout, desktop (1440).**
```
┌──────────────────────────────────────────────────────────────┐ ← transparent Kalles header (70px) over the photo
│  photo: three bollards on the path, full-bleed, darkening    │
│                                                   ▲ note 300px│
│                                          ▲ eyebrow           │
│                                   ▲ h1 135px, 2 lines        │
│                                   ▲ lead 38ch                │
│  ▼ card 360px (thumb 132px + kicker/title/price/buy)          │
│    sits 96px above the bottom, justify-self:start of col 2    │
│                                   ▲ [לארבע הקולקציות] [ghost] │
└──────────────────────────────────────────────────────────────┘
```
`min-height:100svh`; `.env2-wrap` is a 2-column grid `minmax(0,1.3fr) minmax(0,.9fr)`, `align-items:end`,
`padding-block:120px 96px`. The card is `justify-self:start` inside column 2 (not flush to the viewport edge —
the WhatsApp float lives bottom-left). Scrim (copy dusk `.hero .scrim`) blends the bottom 22 % into sky-1 and
darkens the end side 55 %. The hero eyebrow text is ink (not gold) for contrast over the photo; the rule is gold.

**Layout, mobile (390).** Single column, `padding-block:96px 84px`: note (one line, `b::after " — "`),
eyebrow, h1 60 px, lead 16 px, the two buttons (wrap), then the card full-width
(`grid-template-columns:104px 1fr`, thumb at the end side). Price + `הוספה לסל` must be inside 844 px;
the card's bottom edge stays ≥ 84 px above the viewport bottom so the WhatsApp float never covers it.
Verified against dusk's mobile fold, which already achieves this.

**Imagery.** Per §3.6. `<picture>`: source `(max-width:900px)` → images[0] `image_url: width: 1000`;
default images[0] `image_url: width: 1800`, `widths: '900,1400,1800,2400'`, `sizes:'100vw'`,
`loading:'eager'`, `fetchpriority:'high'`. Lead must also edit `layout/theme.liquid` so the index preload
points at these two URLs (or drop the old webp preloads) — otherwise the v1 photos are downloaded for nothing.

**Motion.** Card is `[data-lamp]` (lights ~1.6 s after paint; on screen 1 it is intersecting immediately, so
it is the first thing that switches on). Hero image brightness follows `--p`. Sun rail. Nothing else.

**Schema.** `product` (product) · `bg_image_index` (range 1–4, default 1) · `bg_image_index_mobile` (default 1) ·
`bg_image` / `bg_image_mobile` (image_picker overrides) · `card_image_index` (default 4) · `card_kicker` ·
`card_title_override` · `note_title` · `note_text` · `eyebrow` · `heading_line1` · `heading_line2` · `lead` ·
`cta_primary_label` · `cta_primary_link` (url, default `#env2-places`) · `cta_secondary_label` · `whatsapp_url` ·
`show_sun_rail` (checkbox, default true). Renders `elmsnest-v2-fonts` and `elmsnest-v2-base` at the top.

**Non-negotiables carried.** Real product, real price, buy in screen 1. "Send a photo" promise (ghost CTA).
Header: the one h1 on the page lives here.

---

### 4.2 `elmsnest-v2-first-lit` — מה שנדלק ראשון

**Purpose.** Screen 2: four real products from the four places, each lighting as it enters, each carrying
its place and the approved "suits" phrase as its kicker (G6). Sells before any positioning.

**Copy.**
- eyebrow `01 · נדלקים עכשיו` · h2 `מה שנדלק ראשון`
- intro (end side of the head): `ארבעה מוצרים מארבעת המקומות. כל אחד נדלק כשהוא נכנס למסך — כמו בגינה, כשמתחיל להחשיך.`
- kickers (defaults per block): big `קיר · להאיר נקודה מסוימת` · small 1 `שביל · לראות את הדרך` ·
  small 2 `מרפסת · ליצור אווירה` · small 3 `גינה · הארה ממוקדת של עץ או ערוגה`
- buttons: single-variant `הוספה לסל`; big → `לבחירת גוון`; edison → `לבחירת אורך` with variant note `5 או 8 מטר`

**Layout, desktop.**
```
▲ eyebrow + h2 (80px)                         ▼ intro 34ch, baseline-aligned
grid 1.15fr | 1fr, gap clamp(24px,5vw,80px)
▲ BIG: photo 4/5, its caption is a scrim card    ▼ STACK (padding-top 40px, gap 44px):
  overlapping the photo's bottom by 84px,           item1: thumb 220px | text     (margin-inline-start 0)
  width min(86%,440px), aligned to the start        item2: thumb 170px | text     (margin-inline-start 22%)
  edge. kicker · h3 · [price 30px  | ghost btn]     item3: thumb 260px | text     (margin-inline-end 8%)
```
Nothing is a box: thumbs sit on the sky; text is set beside them at `align-items:end`.

**Layout, mobile.** Head stacks. Big photo 4/5 with the caption card overlapping by 54 px at 92 % width.
Stack items alternate direction (item 2 is `direction:ltr` with children `rtl`, thumb 120 px, margin-inline-end 12 %)
— copy dusk lines 322–329.

**Imagery.** §3.6. Big `image_url: width: 1000`; thumbs 520. All lazy.

**Motion.** Each of the four is `[data-lamp]`; the big one also has the `.halo` (blurred radial behind the image).

**Schema.** `eyebrow`, `heading`, `intro`; blocks `product` (max 4, first = big): `product`, `image_index`
(1–4), `kicker`, `button_label` (multi-variant only), `variant_note`, `object_position` (text, default `50% 50%`).

**Non-negotiables.** Four real products, real ₪, buy/select. No labels other than place + approved phrase.

---

### 4.3 `elmsnest-v2-places` — ארבעה מקומות. קטגוריה אחת.

**Purpose.** The four collections as a staggered staircase of night scenes with oversized numerals —
a collections section that is not four equal boxes. All 27 products are one click away.

**Copy.** h2 `ארבעה מקומות. קטגוריה אחת.` · intro `אנחנו לא חנות תאורה. אנחנו חנות תאורת חוץ — ומתאימים כל מוצר למקום שבו הוא יעמוד.`
Captions: `1 שביל` / `שביל, עמוד וגינה` · `2 קיר` / `תאורת קיר` · `3 גינה` / `ספוטים, פרוז׳קטורים וניידים` ·
`4 מרפסת` / `גרילנדות ותאורה דקורטיבית`; count `{{ collection.products_count }} מוצרים`.
After-link: `לכל {{ collections.all.products_count }} המוצרים ←` → `/collections/all`.

**Layout, desktop.** Head: h2 (max-width 14ch) at start, intro at end, `align-items:baseline`.
Strip `width:min(1500px,100% - 2*gut)`, grid `1.55fr .95fr 1.3fr .85fr`, gap 14, `align-items:end`;
per step bottom offsets 0 / 60 / 24 / 100 px and aspects 5/4 · 3/4.6 · 4/3.2 · 3/4.1 (a staircase, not a row).
**Numeral fix:** the numeral sits *inside* the photo's top-start corner (`position:absolute; top:.04em;
inset-inline-start:.06em; z-index:2`), outline `1px rgba(244,238,227,.45)` until lit, then glow fill with
`text-shadow:0 2px 24px rgba(0,0,0,.6),0 0 30px rgba(255,211,148,.5)` so it reads over bright zones.
Caption under each photo: `b` 30 px serif + `small` 13 px, count in mute at the end.

**Layout, mobile.** Head stacks (intro start-aligned). Strip becomes a horizontal snap scroller
(`overflow-x:auto; scroll-snap-type:x mandatory; padding-inline:var(--env2-gut); scroll-padding-inline:var(--env2-gut)`)
with widths 76vw / 60vw / 80vw / 62vw and bottom offsets 0 / 40 / 16 / 60. Numerals 88 px inside the photo corner —
**nothing may overhang the viewport edge** (this fixes the clipped "1" the judges saw). After-link start-aligned.

**Imagery.** `collection.featured_image | image_url: width: 900`, lazy; `image_picker` override per block.

**Motion.** Each step is `[data-lamp]`; the numeral fills (`transition:color 1.2s,-webkit-text-stroke-color 1.2s`) as the photo lights.

**Schema.** `heading`, `intro`, `all_label`, `all_link`; blocks `place` (max 4): `collection`, `image` (override),
`title_short`, `subtitle`, `aspect` (select: 5/4 · 3/4.6 · 4/3.2 · 3/4.1), `lift` (range 0–120 px).

**Non-negotiables.** Real counts from Liquid; the "27" is computed, never typed.

---

### 4.4 `elmsnest-v2-switch` — אנחנו נגיד לכם גם מתי לא. (the honesty device)

**Purpose.** The brand position as a device you operate, visible in a still: one photograph split by a
draggable line — lit on the start side with the approved "מתאים כדי", dark on the end side with the approved
"לא מתאים כש־". Four places, one stage. Replaces dusk's four lamp rows entirely.

**Copy (exact; the four pairs are verbatim from BRIEF §3).**
- eyebrow `02 · לפני שקונים`
- h2 `אנחנו נגיד לכם גם מתי <span class="env2-no">לא.</span>`
- lead `לכל מקום יש מנורה שמתאימה לו, ומצב שבו היא לא תעבוד. גררו את הקו — וראו מתי האור נשאר כבוי.`
- quick toggle (tiny, tracked): `דולק` · `כבוי`
- place index (radio tabs): `01 שביל, מדרגות ומעברים` · `02 כניסה, קיר וחזית` · `03 מרפסת ופינת ישיבה` · `04 הדגשת אזור בגינה`
- stage labels: lit side `מתאים כדי` · dark side `לא מתאים כש־`
- pairs: 01 `לראות את הדרך` / `המקום כמעט אינו מקבל אור יום` · 02 `להאיר נקודה מסוימת` / `נדרש אור חזק וקבוע לאורך כל הלילה` ·
  03 `ליצור אווירה` / `צריך אור חזק — זו אינה מטרתה` · 04 `הארה ממוקדת של עץ או ערוגה` / `נדרשת התקנה מיוחדת או חיבור קבוע`
- hint at the dark extreme: `לא נדלק. זו הנקודה.`
- helper under the stage (mute, 12 px): `גררו את הקו · או בחרו מקום`
- closing quote: `«כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה.»` cite `מתוך «מי אנחנו», elmsnest.com`
- link: `למדריך המלא לבחירת תאורה לגינה ←` → `/pages/guide-garden-lighting`
- photo check line: `לא בטוחים איזה מקום זה? שלחו תמונה — נבדוק התאמה לפני שתזמינו.` + link `לשליחת תמונה בוואטסאפ`

**Layout, desktop.**
```
.env2-wrap grid 5fr | 7fr, gap clamp(32px,5vw,96px), min-height 100svh, align-items:center
▲ COLUMN A (start)                                    ▼ COLUMN B (end) — THE STAGE
  eyebrow                                                aspect 4/3, full column width, radius 0
  h2 80px: "אנחנו נגיד לכם גם מתי לא."                  ┌────────────────────┬──────────────────────┐
  lead 21px, 40ch                                        │  DARK layer (end)  │  LIT layer (start)   │
  ── hairline ──                                         │  brightness .09    │  photo + warm halo   │
  place index, vertical, 4 rows, 22px serif 500:         │                    ○ knob 44px, hairline │
    01 שביל, מדרגות ומעברים   ← active: gold + lit dot    │ ▼ "לא מתאים כש־"   │   "מתאים כדי" ▲      │
    02 כניסה, קיר וחזית        inactive: ink-2 55%        │   reason, 20px     │   promise, 24px      │
    03 מרפסת ופינת ישיבה                                 └────────────────────┴──────────────────────┘
    04 הדגשת אזור בגינה                                     default split: lit 62 % / dark 38 %
  ── hairline ──                                            helper line under the stage
  quick toggle: דולק · כבוי (hairline underline on active)
below both columns, full width, padding-top 40, hairline top:
▲ blockquote 32px, 26ch + cite            ▼ guide link · photo-check line + WhatsApp link
```
Stage DOM (per place, only one place visible):
```html
<div class="env2-stage" style="--v:38%" data-place="1">
  <figure class="env2-layer env2-layer--dark"><img …><figcaption><span class="k">לא מתאים כש־</span><p>…</p></figcaption></figure>
  <figure class="env2-layer env2-layer--lit"><img …><div class="halo"></div><figcaption><span class="k">מתאים כדי</span><p>…</p></figcaption></figure>
  <span class="env2-bar" aria-hidden="true"></span><span class="env2-knob" aria-hidden="true">‹ ›</span>
  <input class="env2-range" type="range" min="0" max="100" value="38" aria-label="מיקום קו האור">
  <span class="env2-hint" aria-live="polite">לא נדלק. זו הנקודה.</span>
</div>
```
CSS (lift from switch lines 181–194, restyled):
```css
.env2-layer{position:absolute;inset:0}
.env2-layer img{width:100%;height:100%;object-fit:cover}
.env2-layer--dark img{filter:brightness(.09) saturate(.3) contrast(1.05)}          /* G3 */
.env2-layer--lit{clip-path:inset(0 0 0 var(--v));transition:clip-path .12s linear} /* G1: lit occupies the start side */
.env2-bar{position:absolute;top:0;bottom:0;left:var(--v);width:1px;background:#f4eee3;opacity:.8}
.env2-knob{position:absolute;top:50%;left:var(--v);transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;
  background:#f4eee3;color:#1a1206;display:grid;place-items:center;box-shadow:0 10px 30px rgba(0,0,0,.6)}
.env2-range{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
figcaption{position:absolute;bottom:0;width:48%;padding:22px 24px;background:linear-gradient(0deg,rgba(2,3,6,.85),rgba(2,3,6,0))}
.env2-layer--lit figcaption{inset-inline-start:0}  .env2-layer--dark figcaption{inset-inline-end:0}
.env2-layer--lit .k{color:#e9b96e} .env2-layer--dark .k{color:#8f95a3} .env2-layer--dark p{color:#c9c4b8}
.env2-hint{position:absolute;bottom:22px;left:50%;transform:translateX(-50%);font-size:12px;letter-spacing:.14em;color:#8f95a3;opacity:0;transition:opacity .4s}
.env2-stage.is-dark .env2-hint{opacity:1}
.env2-stage.is-dark .env2-layer--lit .halo{animation:env2-flick .24s steps(1,end) 1}   /* G4 */
```
Captions are clipped *with* their layer, so dragging fully to the dark side leaves only the reason on screen,
fully to the lit side only the promise. Both captions are always in the DOM (screen readers read both).

**Interaction, precisely.**
- `input` on the range → `--v = value%`; `is-dark` toggled when `value ≥ 88` (lit ≤ 12 %); leaving that zone removes it.
  Pointer down anywhere on the stage sets the value (the range covers the stage). Keyboard: arrows step 2, PageUp/Down 10.
- Place index buttons (`role="tab"`, `aria-selected`): set `data-place`, crossfade layers `.5s` (opacity),
  swap captions, keep the current split. Keyboard: arrows move between tabs (roving tabindex).
- Quick toggle: `דולק` animates the range to 4 (`transition:clip-path .6s cubic-bezier(.2,.8,.2,1)` during the
  programmatic move, then back to .12s linear); `כבוי` to 96 (triggers `is-dark` → hint + flicker). Active label
  gets the 1 px gold underline; neither is active while the user is mid-way.
- "לא.": `.env2-no{color:transparent;-webkit-text-stroke:1px rgba(255,211,148,.45)}`; when the h2 is 40 % in view
  (IO, once), 300 ms later add `.on` → `color:#ffd394;-webkit-text-stroke-color:transparent;text-shadow:0 0 40px rgba(255,211,148,.45)`
  with keyframes `env2-lamp-on` (0 % .0 → 40 % 1 → 55 % .25 → 70 % 1 → 100 % 1, .55 s). Reduced motion: `.on` immediately, no keyframes.
- The stage's lit layer is also `[data-lamp]` (halo grows in when the section is reached).

**Layout, mobile.** Column A first: eyebrow, h2 40 px, lead 16 px, then the place index as **one text row**
(`01 שביל · 02 קיר · 03 מרפסת · 04 גינה`, 13 px, active gold with hairline underline — not chips), then the
stage at **aspect 4/5** full-bleed (`margin-inline:calc(-1*var(--env2-gut))`), captions at 13 px inside the stage
(48 % width each) over the bottom scrim, the helper line, the quick toggle centred. Then quote, guide link, photo-check line.
Default split on mobile: lit 58 %.

**Imagery.** §3.6 stages 01–04; `image_url: width: 1200`; place 1 eager-ish (`loading:'lazy'` is fine — it is below
the fold), 2–4 lazy. One `<img>` per place is enough: the dark layer may reference the same URL (browser cache).

**Schema.** `eyebrow`, `heading_before` (`אנחנו נגיד לכם גם מתי`), `heading_no` (`לא.`), `lead`, `label_yes`,
`label_no`, `hint_dark`, `helper`, `default_split` (range 20–80, default 62 = lit %), `toggle_on_label`,
`toggle_off_label`, `quote`, `quote_cite`, `guide_label`, `guide_link`, `photo_line`, `whatsapp_label`,
`whatsapp_url`; blocks `place` (max 4): `title`, `suits`, `not_suits`, `product` (image source), `image_index`,
`image` (override), `object_position`, `collection` (optional link under the caption: `לכל המוצרים ל{{title_short}} ←`).

**Non-negotiables carried.** The four approved pairs verbatim; the מי אנחנו quote verbatim; the "send a photo,
we check fit before you order" promise, right after the device. No other claims.

---

### 4.5 `elmsnest-v2-night-wall` — הלילה כבר כאן. קיר אחד מספיק.

**Purpose.** Night has fallen: one product photo fills the viewport, its own light is the only light.
Scale contrast against the sections around it. Sells the highest-ticket wall light with a companion line (G9).

**Copy.** eyebrow `03 · הלילה` · h2 `הלילה כבר כאן.` / (glow) `קיר אחד מספיק.` · kicker `קיר · LED` ·
h3 = product title (default override `מנורת קיר LED עמידה למים IP65, אור למעלה ולמטה`) · spec line generated from
`product.options_with_values` (e.g. `הספק: 6W / 12W · צבע: שחור / לבן` — only what Shopify holds; nothing typed) ·
price `219.90–252.90 ₪` · button `לבחירת הספק` → product page · companion line:
`גם לקיר: {{ companion.title }} · {{ price }} ←` (default companion `magnetic-rechargeable-touch-wall-light`, `159.90 ₪`, link to its page; no thumb).

**Layout, desktop.** `min-height:100svh; display:grid; align-items:center`. Background: the photo absolutely
positioned, `object-position:30% 50%` (the lamp sits in the end half), then a veil
`linear-gradient(90deg,rgba(7,11,21,0) 30%,rgba(7,11,21,.6) 62%,rgba(7,11,21,.94) 100%)` + top/bottom fades into
sky-2 / sky-3. Text column at the start (`grid-template-columns:.9fr 1.1fr`, text in column 1): eyebrow, h2 104 px,
hairline, kicker, h3 19 px, spec 13 px mute, `[price 34px] [button]`, companion 12.5 px mute with gold price.

**Layout, mobile.** Photo occupies the top 62vh (`object-position:45% 50%`), veil fades to sky-3 from 48 %;
text starts at 52vh: h2 55 px, product block, companion. `min-height:auto`.

**Motion.** The whole background is `[data-lamp]` — the wall light literally switches on as the section is reached
(this is the one place where the 1.6 s brightness curve is the section's event).

**Schema.** `product`, `image_index` (default 4), `image` (override), `object_position`, `object_position_mobile`,
`eyebrow`, `heading_line1`, `heading_line2`, `kicker`, `title_override`, `button_label`, `companion_product`,
`companion_prefix` (`גם לקיר:`).

**Non-negotiables.** Real price range from Liquid; option values from Liquid.

---

### 4.6 `elmsnest-v2-atmosphere` — אווירה (replaces the five-box shelf)

**Purpose.** The terrace place as one typographic moment: the word filled with the string-light photo (G7), a
string of bulbs hanging from it (G8), three decorative products hanging from the string at different heights.
Also the page's reach line (27 products, price range, link to all).

**Copy.** eyebrow `04 · מרפסת ופינת ישיבה` · word `אווירה` · sub (end side, 36ch):
`גרילנדות ותאורה דקורטיבית: אור חם בגובה העיניים — כדי לשבת, לא כדי לקרוא.` · products: crystal balls
`גרילנדת כדורי קריסטל סולארית, 20 עד 200 נורות` `מ־89.90 ₪` `לבחירת אורך`; rope `שרשרת חבל סולארית לחוץ, 50 עד 300 נורות`
`מ־89.90 ₪` `לבחירת אורך`; birch `ענפי ליבנה מוארים, 20 נורות LED` `89.90 ₪` `לבחירה` · reach line:
`{{ collections.all.products_count }} מוצרים · {{ min }}–{{ max }} ₪ · לכל המוצרים, לפי מקום ←` → `/collections/all`
(min/max computed from `collections.all.products` in Liquid — 89.90–999.90 today).

**Layout, desktop.**
```
▲ eyebrow                                                   ▼ sub 36ch (baseline of the word)
        א  ו  ו  י  ר  ה      ← 340px FRL 900, centred, full-bleed, photo-filled, gold hairline stroke
 ╲__●___●____●_____●_____●_____●____●___●__╱   ← SVG catenary from the word's baseline, 9 bulbs, full width
        │                      │                     │
   [rope 4/3 240px]      [crystal 1/1.1 300px]   [birch 1/1.4 200px]   ← hang offsets 60 / 0 / 120px
    title · price · link   title · price · link   title · price · link  (text under each, start-aligned)
                                                          reach line, end-aligned, hairline above
```
`.env2-word{font:900 clamp(96px,24vw,340px)/.9 var(--env2-serif);text-align:center;background:url({{ fill }}) center 34%/cover;
-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-stroke:1px rgba(233,185,110,.45);
filter:brightness(1.35) contrast(1.08) drop-shadow(0 0 40px rgba(255,179,71,calc(.35*var(--lit,1))))}` (from switch line 218).
The string: inline `<svg viewBox="0 0 1440 220" preserveAspectRatio="none">` — one `path` (quadratic, sag 120)
stroke `rgba(244,238,227,.35)` 1 px, 9 `circle r=5` bulbs (fill glow, `filter:url(#env2-soft)`), three 1 px
vertical `line`s down to the products at x = 15 % / 50 % / 82 %. Products are an absolutely positioned trio inside a
`position:relative; height:560px` band (`top` = hang offset, `inset-inline-start` = the line's x, `translateX(-50%)`).
Each product's photo casts dusk's pool of light (`.obj .ph::before`, blurred radial under the image).

**Layout, mobile.** Word at 96 px (fits 350 px with 5 letters). String SVG at `viewBox 0 0 390 120`, sag 60, 5 bulbs,
no drop-lines. Products become a horizontal snap scroller (`padding-inline:var(--env2-gut)`, widths 230 / 200 / 170,
`align-items:flex-end`) standing on a hairline "floor" (dusk `.floor::after`). Reach line start-aligned.

**Motion.** The word is `[data-lamp]` (its drop-shadow glow uses `--lit`). Bulbs: each `circle` has
`opacity:0; transition:opacity .4s` and lights in sequence with an 80 ms stagger when the string is 30 % in view.
Products are `[data-lamp]`. Reduced motion: all on.

**Schema.** `eyebrow`, `word` (text, default `אווירה`), `fill_collection` (collection → featured_image) / `fill_image`
(override), `sub`, `reach_label`, `reach_link`; blocks `product` (max 3): `product`, `image_index`, `button_label`,
`width` (range 160–320), `hang` (range 0–160), `x` (range 10–90 %), `aspect` (select 1/1.1 · 4/3 · 1/1.4), `object_position`.

**Non-negotiables.** Reach to all 27 with a real count and real price range; no "best-seller", no ratings.

---

### 4.7 `elmsnest-v2-terms` — ארבעה מספרים שכדאי לדעת

**Purpose.** The consumer-protection terms, findable on the homepage, set as a numeral ledger (rows on hairlines,
enormous numeral at the start, small text at the end) — not four boxes, not small print.

**Copy (exact).** eyebrow `05 · לפני שמזמינים` · h2 `ארבעה מספרים שכדאי לדעת` · intro `לא אותיות קטנות. אותיות גדולות, במקום גלוי, לפני שמשלמים.`
1. `0` unit `₪` — **`משלוח לנקודת איסוף — חינם.`** `משלוח עד הבית: 29.90 ₪.`
2. `8–17` unit `ימי עסקים` — **`מרגע ההזמנה עד הדלת.`** `1–3 ימי טיפול ועוד 7–14 ימי משלוח. חלק מהמוצרים נשלחים ממחסנים מחוץ לישראל — ולכן אנחנו כותבים את זה כאן, ולא מגלים אחרי.`
3. `14` unit `יום` — **`ביטול עסקה לפי חוק הגנת הצרכן.`** `עד 14 יום מקבלת המוצר. דמי ביטול עד 5% ממחיר העסקה או 100 ₪ — הנמוך מביניהם.`
4. `1` unit `תמונה` — **`שלחו תמונה של המקום בוואטסאפ.`** `נבדוק התאמה לפני שתזמינו — ואם המוצר לא מתאים, נגיד.` link `לשליחת תמונה` → WhatsApp
Foot links: `משלוחים ואספקה` → `/pages/shipping-delivery` · `זמני טיפול` → `/pages/processing-time` · `שאלות נפוצות` → `/pages/help-faq` · `למה תאורה סולארית` → `/pages/why-solar-lighting`.

**Layout, desktop.** Head: h2 at start, intro at end. Ledger rows: grid `minmax(200px,.5fr) minmax(0,1fr)`,
`padding-block:30px`, hairline top (last row also bottom), numeral 100 px glow with the unit at .32em ink-2,
text column: bold 19 px + 15 px ink-2, max 56ch. Foot links 12.5 px mute, hairline-underlined.
**Layout, mobile.** Head stacks; rows stack (numeral 58 px, then text), `padding-block:24px`.
**Motion.** None beyond the stars (`.55`). This is the quiet section before the garden.
**Schema.** `eyebrow`, `heading`, `intro`; blocks `line` (max 4): `number`, `unit`, `title`, `text`, `link_label`, `link_url`; blocks `link` (max 6): `label`, `url`.
**Non-negotiables carried.** All four terms verbatim in substance (free pickup / 29.90 door; 8–17 = 1–3 + 7–14, warehouses outside Israel; 14-day cancellation, ≤ 5 % or 100 ₪ whichever lower; photo check on WhatsApp).

---

### 4.8 `elmsnest-v2-goodnight` — לילה טוב (sits directly above the Kalles footer)

**Purpose.** Full night. The garden from section 3 reappears, lit, under stars; the outlined wordmark-line
"לילה טוב"; the photo-check promise with the WhatsApp button; a one-line terms strip (G11). Then the theme footer.

**Copy.** line: `שלחו תמונה של המקום — נבדוק התאמה לפני ההזמנה.` · button `וואטסאפ` (pill, outlined) · big word `לילה טוב`
(aria-hidden; the line is decorative) · strip: `משלוח חינם לנקודת איסוף · 8–17 ימי עסקים · ביטול תוך 14 יום לפי חוק הגנת הצרכן · לתנאים המלאים ←` → `#env2-terms` · socials: Instagram, TikTok (icons, outlined circles, from theme settings or two URL settings).

**Layout, desktop.** `padding-block:120px 40px; position:relative; isolation:isolate`. Garden image
absolutely positioned at the bottom 62 % of the section, `opacity:.8` when lit, under `linear-gradient(180deg,#020306 0,rgba(2,3,6,.35) 45%,rgba(2,3,6,.7) 100%)`.
Row 1 (`.env2-wrap`, grid `1fr auto`): the line + WhatsApp pill at start, socials at end. Row 2 (`margin-top:150px`,
`display:flex; justify-content:space-between; align-items:end`): `לילה טוב` outlined 130 px at end side (as in dusk),
the terms strip 12.5 px mute at start. No columns, no lists — those belong to the Kalles footer below.
**Layout, mobile.** `padding-block:64px 28px`; line + pill; socials; `לילה טוב` 48 px; strip wraps to 2 lines.
**Motion.** The section root is `[data-lamp]`: the garden fades in over 2.4 s (`.env2-garden{opacity:0;transition:opacity 2.4s}` → `.lit .env2-garden{opacity:.8}`); stars `.7`.
**Schema.** `collection` (garden image source) / `image` (override), `line`, `whatsapp_label`, `whatsapp_url`, `big_word`, `strip_text`, `strip_link`, `instagram_url`, `tiktok_url`.
**Non-negotiables.** Terms findable a second time in one line; the photo promise; real socials only.

---

## 5. Header + footer (configure, do not rebuild — per THEME-NOTES)

**Header (`sections/header-group.json` → `header-inline-blocks`).**
- `header_transparent: true` on index; `logo_transparent` = `ElmsNest_Logo_Night.png` (gold mark) — this *is* the
  wordmark; no text logo, no second logo. Logo height 44 px desktop / 36 px mobile.
- `header_height: 70`, `header_height_mb: 60`, `sticky_type: on_scroll_up`, `sticky_glass: true`. When stuck, the
  glass tint must be `rgba(2,3,6,.72)` + `blur(14px)` (override the theme's glass colour in the new scheme, not per section).
- Add a colour scheme in `config/settings_data.json` → `color_schemes`: **`scheme-env2-night`** = text `#f4eee3`, secondary `#c9c4b8`,
  background `#020306`, accent `#ffd394`, button text `#1a1206`. Header uses it (icons/text ink over the transparent hero — the hero
  scrim guarantees contrast at the top 28 %).
- Menu `main-menu`: `דף הבית` `/` · `קולקציות` `#env2-places` · `מדריך לבחירה` `/pages/guide-garden-lighting` · `מי אנחנו` `/pages/מי-אנחנו` · `יצירת קשר` `/pages/contact-us`. Cart + search icons on; no announcement bar; no promo strip.
- Sections that are link targets carry `scroll-margin-top:90px`.

**Footer (`sections/footer-group.json` → Kalles `footer`).**
- `colors_by_section: true`, `color_scheme: scheme-env2-night` on both footer sections (so it continues the black of `goodnight`, no seam).
- Blocks, in this order (drop the newsletter block — no popups, no "join us"): (1) logo + text
  `תאורת חוץ בלבד, לפי המקום: שביל, קיר, גינה, מרפסת. אם משהו לא מתאים לכם — נגיד לפני שתזמינו.`; (2) `קולקציות`: the four
  collection links (`שביל, עמוד וגינה` · `תאורת קיר` · `ספוטים ופרוז׳קטורים` · `גרילנדות ודקורטיבי`); (3) `מידע`:
  `מדריך לבחירת תאורה לגינה` · `למה תאורה סולארית` · `מי אנחנו` · `משלוחים ואספקה` · `זמני טיפול` · `שאלות נפוצות`; (4) `יצירת קשר`:
  contact page + WhatsApp link. Column headings in the theme's small caps style, gold (`#e9b96e`) if the scheme allows.
- Copyright line: `© ElmsNest 2026 · elmsnest.com · תנאי משלוח וביטול` (link → `#env2-terms`). Payment icons: theme default, monochrome.
- The footer is deliberately plain: the composed footer moment is `elmsnest-v2-goodnight` above it.

---

## 6. `templates/index.json` — section order and file names

```json
{
  "sections": {
    "env2_hero":       { "type": "elmsnest-v2-hero" },
    "env2_first_lit":  { "type": "elmsnest-v2-first-lit" },
    "env2_places":     { "type": "elmsnest-v2-places" },
    "env2_switch":     { "type": "elmsnest-v2-switch" },
    "env2_night_wall": { "type": "elmsnest-v2-night-wall" },
    "env2_atmosphere": { "type": "elmsnest-v2-atmosphere" },
    "env2_terms":      { "type": "elmsnest-v2-terms" },
    "env2_goodnight":  { "type": "elmsnest-v2-goodnight" }
  },
  "order": ["env2_hero","env2_first_lit","env2_places","env2_switch","env2_night_wall","env2_atmosphere","env2_terms","env2_goodnight"]
}
```
Files to create:
```
sections/elmsnest-v2-hero.liquid
sections/elmsnest-v2-first-lit.liquid
sections/elmsnest-v2-places.liquid
sections/elmsnest-v2-switch.liquid
sections/elmsnest-v2-night-wall.liquid
sections/elmsnest-v2-atmosphere.liquid
sections/elmsnest-v2-terms.liquid
sections/elmsnest-v2-goodnight.liquid
snippets/elmsnest-v2-fonts.liquid
snippets/elmsnest-v2-base.liquid
snippets/elmsnest-v2-price.liquid
snippets/elmsnest-v2-buy.liquid
templates/index.json   (above, with the default settings/blocks from §4 filled in)
config/settings_data.json (add scheme-env2-night) · sections/header-group.json · sections/footer-group.json (per §5)
layout/theme.liquid   (index preload → the new hero image URLs)
```
Each section: markup + `{% stylesheet %}` (all selectors prefixed `.env2-<section>__…`) + `{% javascript %}`
(init via `document.querySelectorAll('[data-env2-<section>]')`) + `{% schema %}` with one preset named `ElmsNest v2 — <Hebrew name>`.
Every block root carries `{{ block.shopify_attributes }}`.

Section anchors: `#env2-hero #env2-first #env2-places #env2-switch #env2-wall #env2-atmosphere #env2-terms #env2-goodnight`.

---

## 7. Do-not list for this build (what would drift it back to v1)

1. **Do not put four of anything in a row.** Places is a staircase (four different aspects, four different lifts);
   the ledger is rows on hairlines; the switch shows one place at a time. If a grid of equal cells appears anywhere, it is wrong.
2. **Do not reuse a layout.** Hero (photo + card) · first-lit (1 tall + 3 staggered) · places (staircase) · switch
   (5/7 split with a stage) · wall (full-viewport photo, text at start) · atmosphere (word + string + hanging trio) ·
   terms (numeral ledger) · goodnight (garden + outlined word). Do not "simplify" any of them into the previous one.
3. **Do not give any section its own background colour.** The gradient is the identity; sections are transparent
   (only the wall paints its photo). No panels, no cards except the two scrim captions, no rounded tiles.
4. **Do not ship the honesty device as text.** Both captions in the switch section live *inside the photo* and are
   clipped with their layer; the dark layer must be dark (`brightness(.09)`) in the default render, at the default split.
5. **Do not render lamps lit by default when JS is present.** If `[data-lamp]` starts lit, the idea is gone; if it
   starts dim without the `.env2-js` guard, no-JS users get a black page. Both rules are required.
6. **Do not use the v1 hero photos** (`elmsnest-hero-*-performance.webp`) anywhere on the page; fix the preload.
7. **Do not use any image from the "never use" list in §3.6**, and do not let a baked-in caption survive a crop
   (check firefly / powerful-solar / rope at 1× and 2×).
8. **Do not add** best-seller badges, ratings, counts of customers, quotes, countdowns, "free shipping" icon rows,
   newsletter popups, emoji, or a marquee. The only numbers on the page are prices, product counts from Liquid, and the four terms.
9. **Do not fill "לילה טוב" or the outlined numerals before they light**; do not make the gold a surface larger than a button.
10. **Do not use brown / beige / cream** (no `#2b2118` surfaces, no `#f7f0e6` backgrounds) — the theme's old scheme is not used on this page.
11. **Do not put anything fixed in the bottom-left corner** (WhatsApp float) and do not let the hero card sit under it.
12. **Do not bind to the 1200 px page width** for the hero, the switch stage, the wall, the word, the string or the garden — they are full-bleed.
13. **Do not use Assistant as a display face** and do not set headlines in Heebo; product titles are never in the serif.
14. **Do not add scroll-triggered fades to text.** Only lamps light.
15. **Do not type facts.** Counts, prices, ranges, option values come from Liquid objects; copy comes from the strings in §4.

---

## 8. Reference

- Winning mockup (lift CSS/JS): `/home/user/ElmsNest/brief/concepts/dusk/index.html`
  - tokens, gradient, `[data-lamp]`, stars, buttons: lines 14–71
  - hero: 97–119 (+ mobile 301–313); first-lit: 121–144 (+ 315–329); places: 146–164 (+ 331–343);
    wall: 198–213 (+ 356–362); shelf floor/pool (reused for the hanging trio): 215–235; terms ledger: 237–252;
    footer/garden/outlined word: 254–273; reduced motion: 276–283; JS (IO, sweep, `--p`, anchors): 735–807.
- Graft sources:
  - divider stage + knob + range: `/home/user/ElmsNest/brief/concepts/switch/index.html` lines 181–194; photo-filled word: line 218; JS slider: the `.cmp` block in its `<script>`.
  - dim-to-9 % + companion line: `/home/user/ElmsNest/brief/concepts/one/index.html` lines 80–81, 99–102, 324.
  - catenary string + hanging products: `/home/user/ElmsNest/brief/concepts/map/index.html` — CSS lines 204–209 (`.z3 .swag .wire`), SVG path at line 652 (`M0 10 Q 325 140 650 40 T 1300 30`).
- Screens the spec was checked against: `brief/concepts/dusk/shot-desktop.png`, `shot-mobile.png` (full page, both viewports)
  and the same for `switch`, `one`, `map`. Assets: `brief/assets/img/`, `brief/catalog.json`, `brief/assets/fonts.css`.
- Theme mechanics: `brief/THEME-NOTES.md` (read next).
