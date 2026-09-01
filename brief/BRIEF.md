# ElmsNest homepage — creative brief (v2, 2026-09-01)

Read this whole file before doing anything. Then read `catalog.json` (27 products,
4 images each) and look at `v1-rejected-desktop.jpg` — that is the design that was
rejected, and it is what you must NOT produce.

## 1. The verdict on v1 (owner's words, verbatim, translated from Arabic)

> "So far the design is very bad. I feel the site is from the nineties. Everything on
> the page is repeated, all of it is trivial text, and there is no creativity, no
> innovation, no creative visual design."

Diagnosis of why v1 failed — do not repeat any of these:

1. **Same layout four times.** Hero, then four consecutive sections each shaped
   "heading on the right, four equal boxes in a row". No rhythm, no scale contrast,
   no asymmetry, no surprise.
2. **Text problem solved by shortening text, not replacing it with visual ideas.**
   The guidance section is still a table of words. Terms are still words.
3. **Colour mistaken for identity.** Dark background + gold button is a palette,
   not a concept.
4. **Default typography.** One body font (Assistant) at 700 pretending to be a
   headline. No display face, no editorial scale, no typographic composition.
5. **Same container, same padding, every section.** No full-bleed moments after the
   hero, no overlap, no layering.
6. **Zero motion, zero interaction.** A store that sells *light* showed nothing
   turning on, glowing, revealing, or responding.
7. **Only one version was ever built** — no alternatives, no judging.

## 2. The store (facts — do not invent others)

- **elmsnest.com**, Shopify, theme Kalles v5.4.2, plan "Pause and Build".
- **Hebrew only, RTL.** Currency ₪ (ILS). Market: Israel.
- **27 active products, all outdoor lighting**, 89.90–999.90 ₪, typical 130–220 ₪.
- **4 collections** (handle → display name → count):
  - `תאורת-שביל-סולארית` → path / bollard / garden (8)
  - `solar-wall-lights` → wall lights (6)
  - `ספוטים-ופרוז-קטורים-סולאריים` → spotlights, floodlights, portable (6)
  - `גרילנדות-ותאורה-דקורטיבית` → string lights & decorative (7)
- **Sales history: one test order.** There are no best-sellers, no review counts,
  no "X families trust us". Any such number on the page is a lie. Do not write one.
- **Products are purchasable** (inventory untracked, `availableForSale: true`).
- Socials: instagram.com/elmsnest, tiktok.com/@elmsnest. WhatsApp exists (snippet
  `elmsnest-whatsapp` renders a floating button on every page).
- Pages: `/pages/guide-garden-lighting` (מדריך לבחירת תאורה לגינה),
  `/pages/why-solar-lighting`, `/pages/מי-אנחנו`, `/pages/shipping-delivery`,
  `/pages/help-faq`, `/pages/contact-us`, `/pages/processing-time`.

## 3. Brand position and non-negotiables

**Position:** "the narrow specialist who also tells you what does NOT suit you."
One category only — outdoor light — matched to the place: path, wall, garden, terrace.
From «מי אנחנו»: *"כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה"* — unverified
information is never presented as fact.

This is the one thing on the page a competitor cannot copy. It must survive the
redesign — **as a visual idea, not as a table of sentences.**

Non-negotiables:
- **No fabricated claims.** No best-seller labels, no review counts, no customer
  quotes, no "trusted by N". No fake urgency or countdowns.
- **The "not for" lines must be compressions of already-published guidance.** The
  four approved pairs (place → suits / does not suit) are:
  - שביל, מדרגות ומעברים → לראות את הדרך / המקום כמעט אינו מקבל אור יום
  - כניסה, קיר וחזית → להאיר נקודה מסוימת / נדרש אור חזק וקבוע לאורך כל הלילה
  - מרפסת ופינת ישיבה → ליצור אווירה / צריך אור חזק — זו אינה מטרתה
  - הדגשת אזור בגינה → הארה ממוקדת של עץ או ערוגה / נדרשת התקנה מיוחדת או חיבור קבוע
- **Consumer-protection terms must remain findable on the homepage** (they may be
  compact, collapsed, or footnoted — not removed): free shipping to pickup point
  (29.90 ₪ to door); delivery 8–17 business days (1–3 handling + 7–14 shipping,
  may ship from warehouses outside Israel); cancellation within 14 days of receipt
  per חוק הגנת הצרכן, fee up to 5% or 100 ₪ whichever is lower; "send a photo of
  the place on WhatsApp and we'll check fit before you order".
- **Hebrew copy, RTL.** Numbers and Latin tokens (IP65, LED, USB-C, 10W) inside
  `<bdi>` where they would otherwise flip.
- **Must sell.** Real products with real ₪ prices and a way to buy are visible
  early — not after four screens of positioning.

## 4. Assets you can use

- **Product images:** see `catalog.json`. All AI-generated 1254×1254 PNGs. Featured
  image (index 0) is often a marketing creative with Hebrew text baked in;
  indexes 1–3 are usually cleaner product / lifestyle / night shots. Choose the
  cleanest per product. Night scenes with warm light dominate — use that.
- **Hero webp assets (already preloaded by theme.liquid on the index template):**
  `{{ 'elmsnest-hero-desktop-performance.webp' | asset_url }}` (2000×1125) and
  `{{ 'elmsnest-hero-mobile-performance.webp' | asset_url }}` (750×900). Garden
  lantern at dusk, warm glow, dark foliage. Use them or replace them consciously.
- **Collection images** (Shopify `collection.featured_image`): night garden scenes,
  one per collection.
- **Logo:** `https://cdn.shopify.com/s/files/1/0689/4927/8894/files/ElmsNest_Logo_Night.png`
  (800×800, house-with-heart mark, gold on dark).
- **No video exists.** Motion must come from CSS/JS (scroll-driven reveals, glow,
  transitions, canvas, SVG animation) — not from a video file.
- **Fonts:** theme uses Shopify Fonts → Assistant. You may load Google Fonts with
  Hebrew subsets via a `<link>` in the section (storefront allows it). Hebrew-capable
  faces worth considering: **Heebo, Rubik, Frank Ruhl Libre (serif), Suez One
  (heavy slab display), Secular One (display), Karantina (condensed display),
  Bellefair (serif display), Miriam Libre, Alef, Noto Serif Hebrew, David Libre.**
  A display face for headlines paired with a clean text face is expected.

## 5. Technical constraints (hard)

- Deliverable is **Shopify Liquid sections** for Kalles 5.4.2 (Online Store 2.0):
  each section is one `.liquid` file with markup, `{% stylesheet %}…{% endstylesheet %}`
  (or `{% style %}`), optional `{% javascript %}…{% endjavascript %}`, and a
  `{% schema %}` JSON block with settings/blocks/presets. Plus `templates/index.json`.
- **No external JS libraries.** Vanilla JS only, inline in the section. CSS
  scroll-driven animations, IntersectionObserver, `<canvas>`, inline SVG, CSS
  `@property`, view-transitions — all fine. Respect `prefers-reduced-motion`.
- **Header is sticky, ~90px.** Use `scroll-margin-top: 90px` on anchored sections.
- **Page width token** is 1200px but you are NOT bound to it — full-bleed is
  encouraged. Theme radii are all 0; you may override inside your sections if
  the concept needs it, but be consistent within the page.
- **Existing colour tokens** (RGB triplets, use with fallbacks):
  `--en-night` 43 33 24 (#2b2118), `--en-ink` 247 240 230 (#f7f0e6),
  `--en-gold` 217 173 95 (#d9ad5f), `--en-paper` 255 253 247, sale red #91212a.
  These are a starting point, not a cage. A true black (#0b0906-ish) or a deeper
  night is allowed if the concept calls for it. Do NOT ship brown-on-cream.
- **RTL app (Sense RTL) is active** — it flips some theme CSS. Write your own CSS
  with logical properties (`inline-start/end`, `margin-inline`) so it is correct
  regardless.
- **Performance:** first screen must not wait on fonts or JS. Lazy-load below
  the fold. No layout shift on font load (use `font-display: swap` + size-adjust
  or a matching fallback).
- **Accessibility:** real headings hierarchy (one h1), focus states, contrast
  ≥ 4.5:1 for text, animation optional under reduced-motion.
- Add-to-cart for single-variant products may be a plain `<form method="post"
  action="{{ routes.cart_add_url }}">` with hidden `id` + `quantity`. Multi-variant
  products link to their page.

## 6. The bar

The owner should look at it and think *"this was made by a real designer for a
real lighting brand"*, not *"a Shopify template with Hebrew in it"*.

That means, concretely:
- **One idea** the whole page is built around, that only a *lighting* store could
  have. Light in darkness. The moment of switching on. The glow. Dusk. A garden
  revealing itself. Choose one and commit.
- **Every section is composed differently.** If two sections share a layout
  pattern, one of them is wrong.
- **Scale contrast.** Something enormous next to something small. A headline that
  is a wall. A product photo that fills the viewport.
- **Motion that means something.** Not "fade in on scroll" for everything —
  something that connects to the idea (a lamp lights as you reach it; the page
  gets brighter; a beam follows the cursor; the dusk sky shifts).
- **Editorial typography.** Display face, tight leading on big Hebrew, deliberate
  hierarchy, generous whitespace.
- **The honest positioning shown, not told.** The "suits / doesn't suit" idea
  should be a *device* (a toggle, a light that goes out, a comparison you can
  feel), not four cards of text.
- **It sells.** Product, price, buy — reachable within the first two screens.

Reference points for taste (do not copy, calibrate against): Apple product pages'
scale and restraint; Aesop's editorial calm; Flos / Louis Poulsen / Artemide
lighting sites; the way Stripe's homepage uses one gradient idea everywhere.

## 7. What we do NOT want

- Generic e-commerce template patterns: icon-row of "free shipping / guarantee",
  star ratings, "trusted by", countdown timers, popup discounts.
- Four equal boxes in a row, twice.
- Brown/beige/cream "cozy" palette. Gradients that look like 2012 Bootstrap.
- Stock-photo smiling families. Emoji as icons.
- Lorem-ipsum-grade Hebrew. Copy must be specific and short.
