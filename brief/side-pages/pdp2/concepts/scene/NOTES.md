# Concept «scene» — «see it at night»

## What it is

Two sections, both after the buy box, nothing between the gallery and the button:

1. **`ens_pdp_night`** — `sections/elmsnest-s-pdp-night.liquid` («ככה זה נראה בלילה»). ONE page-wide night photograph
   of this product in its place (in flow, 480 px tall at 390, 560 px at ≥ 901, edge to edge) with ONE sentence in glow
   serif at the bottom inline-start, inside the wrap, on a 34 % bottom fade. The desire the carousel hides behind a
   swipe. Own frame when the product has one (map), the collection scene with the muted linked «בתמונה: …» line
   otherwise. No heading, no eyebrow, no link, no button, no motion, no carousel.
2. **`ens_pdp_dusk`** — `sections/elmsnest-s-pdp-dusk.liquid` («כשמחשיך»), solar products only (P4 gate copied from
   `elmsnest-s-place`). A detail, not a landscape: one small square (132 px at 390 / 200 px at ≥ 901) — a tight crop of
   the product's own frame at the moment the light comes on — with the label and two short sentences beside it, on a
   hairline row that rhymes with the facts' `<dl>` under it. No detail frame → text row. Mains / USB → nothing.

Cinematic and quiet: big type on the photograph, then a small honest row, then the facts.

## What it refuses

- A second price, button, terms, contact, «לא מתאים», product grid, place list (BRIEF §1).
- Any frame with baked text unless the asset is a baked pre-crop (only C's spot fallback needs one — IMAGES.md).
- Gallery frame 1 of the product (the phone already shows it): A uses frame 6, B uses frame 6.
- The CC lamps of the home round, the featured creatives, faces, foreign brand marks.
- The home's two-landscape diptych and its headline words; the winter line (home already says it); hours, lumens,
  IP codes, «חזק», «אוטומטי», «לבד».
- A third section. «לפני שמזמינים» (seed 3) was left out on purpose: its three checks overlap the not-for line and the
  facts, and the sentence «יותר שמש ביום, יותר אור בלילה.» already carries the one check that prevents a return.

## Order in `templates/product.elmsnest.json`, and why

`main-product → ens_pdp_night → ens_pdp_dusk → ens_pdp_facts → ens_related`

Desire before detail: the shopper has just seen the price and the button; the next screen answers «what will it look
like at my place at night?» — the question the gallery's one-frame-at-a-time cannot. The dusk row sits right under the
scene because it is the second half of the same thought (at night it is on — and why), and because on the phone the
scene's bottom edge + the row make one 668 px screen before the facts begin. Then the facts (specs, description),
then `ens_related` last in the body. On a mains product the page is scene → facts, one section shorter.

## Measured heights at 390 (playwright, `getBoundingClientRect`, real fonts) — cap 520 per section, 1500 total

| archetype | ens_pdp_night | ens_pdp_dusk | total new | PDP after (main 1085 + new + facts 723 + related 781) |
|---|---|---|---|---|
| A path · solar · own frames | 480.0 | 188.3 | **668.3** | 3257 px body ≈ 3.9 screens (+ footer) |
| B wall · mains · own frame | 480.0 | 0 (gated off) | **480.0** | 3069 px |
| C spot · solar · fallback | 509.5 (480 photo + 29.5 «בתמונה» line) | 140.3 (text row) | **649.8** | 3239 px |

At 1366×900: A 560 + 287 = 847 · B 560 · C 593.5 + 244.7 = 838.2. Nothing that must be read lives in the bottom 78 px
of any phone viewport: the sentence ends 34 px above the photo's bottom edge, and the fold shots draw the sticky bar.

## The rule the Liquid follows (no metafield, tag, product or collection changes)

- **Family** → `render 'elmsnest-s-place', product: product, emit: 'collection'` picks the sentence (four text
  settings, one per collection handle; the decor one is never gated).
- **Photograph** → section blocks (`product` + `image_picker` scene + `image_picker` detail + two `object_position`
  texts), matched on `product.handle`; else the collection's `image_picker` + `product` pair (four of each in the
  section settings); the «בתמונה: {title}» line prints whenever the frame's product is not the page's product, linked
  with `fallback_product.url`. Nothing → the section prints nothing.
- **Solar gate** (section 2 only) → `custom.power_source == 'סולארי'`, else `product.title + description contains
  'סולארי'` — the same three-state test as `elmsnest-s-place`. 16 of 27 products pass; the wall collection's five mains
  lights and the rechargeable one do not.
- **Crops** → the scene: `object-fit:cover` + `object-position` per breakpoint (two settings, as the home band); the
  fallback that needs a slice (spot) and the detail square: an oversized image anchored with logical insets
  (`inset-inline-start` / `inset-block-start`), three custom properties per breakpoint — no physical `left`/`right`
  (lint PHYS rule), radius 0, no transform, no JS.
- **Images** → `asset_img_url` 600 / 900 / 1254 candidates, `sizes="100vw"` for the scene and `200px` for the detail,
  lazy + async + width/height. ≤ 2 new files per PDP.
- **Files** → `sections/elmsnest-s-pdp-night.liquid`, `sections/elmsnest-s-pdp-dusk.liquid`, Hebrew `{% schema %}`,
  `enabled_on: {templates: ["product"]}`, `class: "ens-pdp-section hdt-section"`; `templates/product.elmsnest.json`
  gets two entries and the order above. No Kalles, core or skin file touched.

## Is any of this twice? (the honest one line)

Yes, one thing: the dusk row restates the home's «ביום נטען. בלילה נדלק.» fact — in a detail and other words, plus
the sun dependency the home does not say — and A's and B's scene frames are gallery frames the phone shopper never
swiped to (6 and 6); nothing else on the page is said or shown a second time.

## Shots

`shots/{A,B,C}-m-fold.png` (390×844, the scene at the top of the viewport, sticky bar drawn) · `-m-full.png` (the
archetype's whole block at 390) · `-d-fold.png` (1366×900) · `-d-full.png`. Mockup: `index.html` (each archetype has
its own id `#arch-a` / `#arch-b` / `#arch-c`; the new sections `#ens-night-x`, `#ens-dusk-x`).
