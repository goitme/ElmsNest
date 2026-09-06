# Concept «dusk» — «what happens when it gets dark»

## What it is

Two sections, both after the buy box; nothing between the gallery and the button.

1. **`ens_pdp_dusk`** — `sections/elmsnest-s-pdp-dusk.liquid`, «כשמחשיך». On a **solar** product: a compact pair of two
   square details (173 px each at 390, 260 px at ≥ 901, a 4 px night gap) — the page's own frame at dusk («בין ערביים»)
   and the same lamp at night («לילה») — then three short lines on hairlines (charges by day · comes on by itself at
   dusk · less charge in winter) and the one sales line in glow serif, said once: «בלי כבל, בלי חשמלאי.». A solar
   product with no mapped frame gets the same two squares in type («יום» outlined gold on the day sky, «לילה» in glow
   on the night sky with the house stars) — no photograph, no other product. On a **mains / USB / battery** product the
   whole section collapses to ONE hairline row: «כשמחשיך · המנורה הזו אינה סולארית.» (79 px).
2. **`ens_pdp_scene`** — `sections/elmsnest-s-pdp-scene.liquid`. One wide photograph in flow (300 px at 390, 480 px at
   ≥ 901, edge to edge, a 34 % bottom fade) with one family sentence in glow serif at the bottom inline-start, inside
   the wrap. Own frame when the map has one; the collection's default scene with the muted linked «בתמונה: …» line
   under the picture otherwise.

The angle is explanatory, not decorative: the pair answers the first-time solar buyer's question (what happens at
dusk, what it needs by day, what winter does), and the band gives the desire picture the carousel hides — in that
order, because the shopper has just read a price and is deciding.

## What it refuses

- A second price, button, terms, contact, «לא מתאים», product grid, place list (BRIEF §1). No link anywhere except
  the honesty line's link to the pictured product.
- Any photograph in the dusk pair that is not the page's own product. The pair has no collection fallback on purpose:
  a day/night pair of a different lamp implies «this is your lamp's panel» even with a caption — so it shows the page's
  product or shows type.
- A frame with baked text unless the asset is a baked pre-crop (only the spot default needs one — IMAGES.md).
- The product's gallery frame 1 (the phone already shows it).
- The home's diptych headlines («ביום נטען.» / «בלילה נדלק.») and its landscape framing: here the two tiles are details,
  square, small, dusk · night rather than day · night, and the words sit in lines under them, not on the photographs.
- Hours, lumens, IP codes, «אוטומטי», «לבד», «חזק»; a solar sentence on a mains light (the wall collection holds five).
- A third section: «לפני שמזמינים» (seed 3) overlaps the not-for line and the dusk lines; «אותו אור, מקומות אחרים» (seed 4)
  needs three honest frames most products do not have.
- Carousel, parallax, scroll-lamps, hover reveals, JS.

## Order in `templates/product.elmsnest.json`, and why

`main-product → ens_pdp_dusk → ens_pdp_facts → ens_pdp_scene → ens_related`

Detail before doubt, then desire before «where next». The dusk pair sits directly under the buy box because it is the
sentence a first-time solar buyer needs before pressing the button («does it need an electrician, what happens at
night, what about winter») — and on a mains light it is a 79 px row that quietly removes a wrong assumption. The
facts follow, in the same hairline rhythm (the three lines are drawn like the facts' `<dl>`, so the two read as one
column of plain truths). The scene band comes after the facts as the exhale: one wide night picture, one sentence,
then the four related cards. `ens_related` stays last in the body. On a mains product the page is row → facts → band.

Template entries: `"ens_pdp_dusk": {"type": "elmsnest-s-pdp-dusk", "blocks": {…map…}, "settings": {…}}` and
`"ens_pdp_scene": {"type": "elmsnest-s-pdp-scene", "blocks": {…map…}, "settings": {…}}`; `order` as above.

## Measured heights at 390 (playwright, `getBoundingClientRect`, the real Frank Ruhl Libre + Heebo) — caps 520 / 1500

| archetype | ens_pdp_dusk | ens_pdp_scene | new total | block (header 59 + main 1085 + new + facts 723 + related 781 + footer 850) |
|---|---|---|---|---|
| A — stainless path light (solar, photo pair) | **498.05** | **300** | **798.05** | 4306 |
| B — waterproof wall light (mains, one row) | **79.3** | **300** | **379.3** | 3893 |
| C — solar floodlight (solar, type pair · captioned default scene) | **498.05** | **329.5** (300 picture + the credit line) | **827.55** | 4342 |

At 1366 × 900: A 444 / 480 · B 68.8 / 480 · C 444 / 511.5. No horizontal overflow at either width (`scrollWidth` =
viewport). The path PDP would go from 3498 px to ≈ 4296 px at 390 ≈ 5.1 screens (cap 6). Nothing a section needs read
sits in the last 78 px of the page (the sticky bar's strip): the band's sentence ends 22 px above the picture's foot,
which is followed by `ens_related`.

Shots: `shots/<A|B|C>-m-fold.png` (390 × 844, `ens_pdp_dusk` at the top of the viewport), `-m-full.png` (the whole
archetype block at 390), `-d-fold.png` (1366 × 900), `-d-full.png`.

## The rule the Liquid would follow (no product data changes)

```
gate      = elmsnest-s-place solar test (custom.power_source == 'סולארי', else title+description contain 'סולארי')
family    = render 'elmsnest-s-place', product: product, emit: 'collection'   (path / wall / spot / decor)
map       = the section's blocks: {product, image_dusk_1, image_dusk_2, image_scene, zoom_1, focal_1, zoom_2, focal_2, op, op_lg}
            matched on product.handle (the owner adds or swaps frames in the theme editor)

ens_pdp_dusk:
  not gate                      → one row: label «כשמחשיך», text «המנורה הזו אינה סולארית.»   (the facts print any stated 220V/USB — not repeated)
  gate and map.image_dusk_1/2   → the photo pair (tags «בין ערביים» / «לילה») + 3 lines + the sales line
  gate, no map                  → the type pair («יום» / «לילה») + 3 lines + the sales line
ens_pdp_scene:
  map.image_scene               → own frame, family sentence, no credit line
  else                          → assets/ens-pdp-{family}.jpg (image_picker override per collection in settings),
                                   family sentence, and — unless the default's product IS this product — the line
                                   «בתמונה: {{ credit.title }}» linked to credit.url (credit = the product setting beside each default)
  no family                     → nothing
```

Schema: every text is a setting (h2, two tags, two words, three lines, sales line, the mains row label + text, four
family sentences, the credit prefix); every image an `image_picker`; zoom (range 1–3) and focal (text «72% 47%») per
tile; `object_position` / `object_position_desktop` per band; `enabled_on: {templates: ["product"]}`;
`class: "ens-pdp-section hdt-section"`. Weight: 2 photographs on A (tiles 900 w max, the band `asset_img_url` 600/900/1254
with `sizes="100vw"`), 1 on B, 1 on C; all `loading="lazy" decoding="async"` with width/height. `asset_img_url` never
asks for a width above the source. Lint: logical properties only (the tile figure is `direction:ltr` so its
inset-inline-start equals the photo's left — a photograph has no reading direction); radius 0; reduced-motion has
nothing to switch off (no transitions are used).

## Is any of this twice? — the honest answer

Yes, three things, and each is a choice:

1. **The winter line and the sales line say what the home says**, in other words («בחורף הימים קצרים יותר, ויש פחות
   טעינה.» / «בלי כבל, בלי חשמלאי.» against the home's «בחורף השמש קצרה יותר…» / «בלי חיבור לחשמל, בלי חשמלאי.»). On the
   PDP each is said once, at the point of sale; a shopper who lands on the product from an ad never saw the home.
2. **Line 2 («כשמחשיך, המנורה נדלקת מעצמה.») is the title's «תאורה אוטומטית» in a sentence**, and on products whose
   bullet prints «הפעלה: אוטומטית בחושך» the facts say it too. It stays because it is the angle's one fact and the title
   word is not a sentence; the judges may still count it.
3. **A's three frames (2, 4, 6) are later gallery frames** the phone shopper never swiped to (the phone shows frame 1
   with a «1/6»); B's band is its gallery frame 6. Frame 1 is never reused.

Not twice: the pair's framing (square details, dusk · night, words under the pictures) is not the home diptych; the
mains row names no connection because the facts do; the band sentence for path was changed from «כשמחשיך, …» to «אחרי
השקיעה, …» so the section heading's word is not repeated two screens down.

## Trade-offs the judges should weigh

- C's band shows a MAINS lamp on a solar page. It is the collection's only clean night frame, the caption names and
  links it, the sentence speaks of a beam and not of power, and the dusk section above it shows no photograph at all —
  but the owner may prefer the type-only fallback for the band too (one checkbox: «בלי תמונת קולקציה»), or a mapped frame.
- The «יום» / «לילה» type pair is calmer than a photograph; it is the honest floor for the 10 products with no clean frame,
  and the map raises any of them the day the owner picks a frame.
