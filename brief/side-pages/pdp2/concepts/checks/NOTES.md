# Concept «checks» — לפני שמזמינים

## What it is

The store as the friend who says «check this first». Two sections, not three:

1. **`elmsnest-s-pdp-scene`** — right after the buy box: one edge-to-edge photograph of the product (or, for a
   product with no clean frame, the collection's scene, honestly captioned) *in place, at night*, with one family
   sentence in glow serif. 400 px tall at 390, 520 at 1366. The desire picture the gallery hides behind a swipe.
2. **`elmsnest-s-pdp-checks`** — «לפני שמזמינים», after the facts: the three checks that prevent a return, each ONE
   question on a photographic strip — how much sun reaches the spot · how far the light must reach · winter means
   a shorter day — then the one guide link «למדריך לבחירת תאורה ←». The three strips are three crops of ONE frame
   (top · middle · bottom), so the photograph is read as sliced, and the page loads one file for three tiles.
   Non-solar products get two checks (reach · where the power comes from). A product with no clean frame gets the
   typographic fallback: the outlined gold numerals of the facts section, on hairlines, no photograph.

## What it refuses

- No second price, button, terms, contact line, not-for line, place list, product grid (SIMPLIFY §3 stays one-to-one).
- No warning. The not-for line warns once; this section asks. No «לא מתאים» anywhere in it.
- No spec: no IP, hours, lumens, watt, 220V. No «מתאים כדי…».
- No frame with baked text, no gallery-1 frame, no CC photograph, no featured creative. Every frame is the store's own.
- No third section: the «כשמחשיך» day/night pair was dropped — the home already owns the big diptych, and the
  winter question carries the one solar honesty the PDP needs at the point of sale.
- No JS, no carousel, no parallax, no hover reveal, no motion (reduced-motion has nothing to reduce).

## Template order and why

`main-product → ens_pdp_scene → ens_pdp_facts → ens_pdp_checks → ens_related`

Desire before detail, detail before doubt. The band sits under the button because it is the one thing the carousel
cannot do (a wide night scene, no swipe) and it costs no reading. The checks sit after the facts because a shopper
who reads that far is the one still deciding: he has the specs, he now gets the three questions and the guide, and
the related grid stays last as the exit. The shopper who is sure never reaches the checks — the sticky bar has him.
`ens_related` stays last in the body.

## Measured heights (Playwright, real fonts, `getBoundingClientRect`)

| | A · path, solar | B · wall, mains | C · spot, solar, no frame |
|---|---|---|---|
| scene band @390 | 400 | 400 | 427.8 (400 + the 27.8 px «בתמונה» line) |
| checks @390 | 485.5 (3 tiles × 104) | 377.5 (2 tiles × 104) | 481.5 (3 fallback tiles × 105) |
| **total new @390** | **885.5** | **777.5** | **909.3** |
| scene band @1366 | 520 | 520 | 549.5 |
| checks @1366 | 580.4 | 593.4 | 538.4 |
| total new @1366 | 1100.4 | 1113.4 | 1087.9 |

Every section ≤ 520 at 390; every total ≤ 1500. The path PDP goes from 3498 to ≈ 4384 px = 5.2 screens (cap 6).
Nothing that must be read lives in the last 78 px of the page (the related grid is below the checks).

## The rule the Liquid follows (no product data changes)

- **Family (sentence, lead, defaults):** `{% render 'elmsnest-s-place', product: product, emit: 'collection' %}` →
  one of four handles → the family sentence setting (`line_path`, `line_wall`, `line_spot`, `line_decor`).
- **Solar gate:** copied from `elmsnest-s-place` (metafield `custom.power_source == 'סולארי'`, else title +
  description contain «סולארי»). Solar → questions 1·2·3 and lead «שלוש…»; else → 2·2′ and lead «שתי…».
  The wall collection's five mains lights and the rechargeable one therefore never see a sun or winter line.
- **Photographs, map first, collection fallback:** section blocks `product` + `image_picker` (+ an
  `object_position` text) matched on `product.handle`; when no block matches, the collection default asset
  (`ens-pdp-{path,wall,spot,decor}.jpg`) renders **with** the «בתמונה: {title}» line, whose product handle is a
  per-collection setting (`credit_product_path` …) — the caption is `all_products[handle].title`, linked. When a
  block matches, no caption. The checks section takes its tile file from a second block list (`tile_image`); when
  none matches, the typographic fallback renders (no collection default for the tiles — a second captioned frame
  of another product would be one honesty line too many).
- **Gallery-1 guard:** the map is owner-curated; the defaults chosen here are frames 4/6 (A), 6/4 (B) and the
  spot scene (C) — none is any product's featured image.
- Weight: ≤ 2 files per PDP, lazy, sized, `asset_img_url` capped at the rendered width (IMAGES.md).

## Is any of this twice? (honest answer)

Partly, in two places, and said here so the judges can weigh it:
1. The sun question («כמה שמש מגיעה למקום במשך היום?») and the path not-for line («לא מתאים כשהמקום כמעט אינו מקבל
   אור יום.») rest on the same fact. One asks at the spot, one warns under the button; the angle is that they are
   two different acts, but a strict judge can call the fact twice.
2. The winter line is on the home too (the fit block's honesty). Here it is a question at the point of sale, not a
   statement — still the same fact.
Also to weigh: the scene band is the home band's device (edge-to-edge photo + one glow sentence) on another page
with another photograph; and on B the band shows gallery frame 6, which the phone shopper never swiped to but the
desktop thumbnails do list. Nothing else on the page is repeated: no price, button, terms, contact, not-for, spec,
place word, grid or guide link exists twice.
