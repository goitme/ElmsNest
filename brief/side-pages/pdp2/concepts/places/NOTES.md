# Concept «places» — «the same light, three places»

## What it is

Two sections, both after the buy box; nothing between the gallery and the button.

1. **`ens_pdp_places`** — `sections/elmsnest-s-pdp-places.liquid`. A triptych of the family's clean frames in three
   places, one word (or one short line) on each tile at the bottom inline-start on a short scrim — «מדרגות · כניסה ·
   בין השיחים» for the path light, «פרגולה · חצר · אבן צפחה» for the wall light. A heading in the facts' scale (24 px
   serif, 30 at ≥ 901). At 390 a 1 + 2 mosaic (lead tile 390×220 edge to edge, two 193×160 tiles, 4 px gutters —
   the home-solar grid gutter); at ≥ 901 three equal 4:5 tiles inside the wrap. Tight, consistent crops: every tile
   is a lit lamp low in the frame and its place around it. The desire the carousel hides behind a swipe, three times,
   in one screen.
2. **`ens_pdp_winter`** — `sections/elmsnest-s-pdp-winter.liquid`, solar products only. One hairline row in the
   facts' own language (label «בחורף» 13 px muted · value «היום קצר יותר, וגם האור בלילה.» 16 px), inside the wrap,
   directly above the facts so it sits over the «זמן עבודה» row it qualifies. Mains / USB products: nothing.

Editorial and graphic: three photographs, three words, one heading, one honest row. No sentence about the product.

## What it refuses

- A second price, button, terms, contact line, «לא מתאים», product grid, place list (BRIEF §1). The only link is the
  13 px credit to the sibling product, which the honesty rule requires.
- The licensed place words (שביל · קיר · גינה · מרפסת) — P2 keeps them for the kicker and the home / collection
  header; the tiles use other nouns («בין השיחים» instead of «שביל», «פרגולה» instead of «מרפסת»).
- Gallery frame 1 of the product (the phone already shows it): A uses 6 / 4 / 2, B uses its frame 6.
- Any frame with baked text unless the dev asset is a baked pre-crop — only C's one frame needs it (IMAGES.md).
- The CC lamps of the home round, the featured creatives, faces, foreign brand marks (dual-head frame 5 with its
  LUMIÈRE sign is out even though the scene is the best in the spot family: its clean slice is 930 px wide).
- A studio frame as a «place» (the wall light's own 2 / 4 / 5, the dual-head's 1 / 6).
- A third section. The day/night pair (seed 2) is the home's diptych; «לפני שמזמינים» (seed 3) overlaps the not-for
  line; scale / box (seed 6) has no clean images. The winter row is the one honest thing worth saying at the point of
  sale, and it is 81 px.
- Decoration: no stars, no lamp device, no motion, no carousel, no hover, no parallax.

## Order in `templates/product.elmsnest.json`, and why

`main-product → ens_pdp_places → ens_pdp_winter → ens_pdp_facts → ens_related`

Desire before detail: the shopper has just seen one frame, the price and the button. The next screen answers «will
it look like that at my place?» — three places, three words, no reading. Then the one doubt a first-time solar buyer
should meet before the specs (winter), on the same hairline as the facts' rows, so the eye reads «בחורף … / IP65 /
זמן עבודה …» as one list. On a mains product the page is places → facts, one row shorter. `ens_related` stays last.

## Measured heights at 390 (playwright, `getBoundingClientRect`, real fonts) — cap 520 per section, 1500 total

| archetype | ens_pdp_places | ens_pdp_winter | total new | PDP after (main 1085 + new + facts 723 + related 781) |
|---|---|---|---|---|
| A path · solar · own frames (1 + 2) | **476.4** | **81.3** | **557.7** | 3147 px body ≈ 3.7 screens (+ footer) |
| B wall · mains · own + 2 siblings (1 + 2 + credit) | **505.2** | 0 (gated off) | **505.2** | 3094 px |
| C spot · solar · one credited frame | **421.2** | **81.3** | **502.5** | 3092 px |

At 1366×900: A 652.3 + 72.3 · B 685.2 · C 685.2 + 72.3 (the single 4:5 tile keeps the row's height). The mosaic's
words sit ≥ 10 px above each tile's bottom edge and the credit / winter rows are in flow above the facts, so nothing
that must be read lives only in the bottom 78 px of a phone viewport; the fold shots draw the sticky bar.

## The rule the Liquid follows (no metafield, tag, product or collection changes)

- **Family / gate** → `render 'elmsnest-s-place', product: product, emit: 'collection'` for the collection handle;
  the solar test copied from the same snippet (`custom.power_source == 'סולארי'`, else title + description contain
  «סולארי») gates `ens_pdp_winter` — 16 of 27 products pass; the wall collection's five mains lights and the
  rechargeable one print nothing.
- **Tiles** → section blocks `tile` (`product` + `image_picker` + `text` word + two `text` object-positions), each
  block also carrying a `product` «shown in the frame» (`pictured`). The section collects the blocks whose
  `product.handle == product.handle` (the per-product map, up to three, in block order); if none, the blocks whose
  `collection` setting equals the place collection (the per-collection default, up to three). Zero tiles → the
  section prints nothing (camping lantern, security light, net lights…).
- **Degrade by count** → 3 tiles: 1 + 2 · 2 tiles: 1 + 1 (the second tile spans the row) · 1 tile: one 390×300 tile
  at 390, one 4:5 column of three at ≥ 901 (C).
- **Heading** → three text settings; `heading_own` when every tile's `pictured` is the page's product, else
  `heading_family` (plural) or `heading_family_one` (one tile).
- **Credit** → for every distinct `pictured` product that is not the page's product, one 13 px line «{words} —
  בתמונה: {pictured.title}» linked to `pictured.url` (the words prefix dropped when there is one tile). Never
  implied, never omitted.
- **Weight** → ≤ 3 photographs, `loading="lazy" decoding="async"`, width/height, `asset_img_url` widths capped at
  the rendered size (IMAGES.md), the owner's `image_picker` srcset capped against the source width (the hero's R26
  rule).
- Files: `class: "ens-pdp-section hdt-section"`, `enabled_on: {templates: ["product"]}`, Hebrew schema, a setting for
  every text and image; `templates/product.elmsnest.json` gets two entries and the order above; nothing published to
  the live theme.

## Is any of this twice?

Honest answer: **the winter fact is on the home in other words** («בחורף השמש קצרה יותר, והפאנל נטען פחות.»); here it
is a new sentence, gated to solar products and placed above the «זמן עבודה» row it qualifies — a judge who counts
facts rather than sentences will call that one twice, and the row costs 81 px to drop. The triptych is not twice:
its frames are gallery frames the phone shopper never swiped to (A: 6 / 4 / 2, B: 6) or frames from another
product's gallery, credited (B: two, C: one), and the heading, the words and the credit are all new. Nothing else
on the page — price, button, terms, not-for, contact, specs, related, the kicker's place sentence — is repeated.
