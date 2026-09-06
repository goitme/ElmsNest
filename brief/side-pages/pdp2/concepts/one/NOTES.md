# Concept «one» — one section, done

## What it is

**One** new section, `sections/elmsnest-s-pdp-scene.liquid` (`class: "ens-pdp-section hdt-section"`,
`enabled_on: {templates: ["product"]}`), inserted **directly after the buy box**:

```
"order": ["main-product", "ens_pdp_scene", "ens_pdp_facts", "ens_related"]
```

It is the home band's device on the product page, tuned for a sale: one page-wide photograph of the product — or
its kind of light — in a place, at night, in flow (300 px tall at 390, 520 at ≥ 901, full-bleed at every width like
the phone's gallery), then, **on the night ground under it, not on the photo**: the place heading
(«בלילה, על השביל» — the licensed place word), the family's night line (what the light does in that place), the
dusk line on solar products only («ביום הפאנל אוסף שמש. כשמחשיך, האור נדלק.»), and the guide link
(«למדריך לבחירת תאורה ←», the PDP's first). When the frame shows another store product, a muted 12–13 px
«בתמונה: {title}» line, linked, sits between the photo and the heading. No scrim, no headline-on-photo, no card
chrome, no motion, no JS.

## What it refuses

- A second section. The round allows two or three; a sales page is shorter with one that does the three jobs
  (see it in place at night · what happens at dusk · where to check before ordering) in ≤ 520 px.
- Any text on the photograph (the crops are not uniformly dark; B has a blue-hour sky) — the typography sits on
  the night ground, the photograph is left alone.
- A day/night pair (the home has it), a winter line (the home has it), a checklist (the guide is one tap away),
  a second «לא מתאים», a second contact line, a second button, a second price, a place list, a product grid.
- Any frame that is not the store's own; any frame with baked text unless the asset is pre-cropped; the gallery's
  frame 1; the featured creatives; the home band's fence frame.
- Copy about specs: the night lines describe the *form* of the light (low pool · wash on a wall · one beam ·
  many small points), never reach, hours, lumens or IP.

## The order, and why

`main-product → scene → facts → related`. Desire before detail: the shopper who has just read the price and the
not-for line gets, in one screen, the picture the carousel hid at position 6 and the one solar fact and the way
out to the guide — then the facts answer the spec question for the one who is still reading, and `ens_related`
stays last. Putting the scene after the facts would separate the photograph from the button by 362–723 px and
leave the shopper who stops at the facts without ever seeing the light in place.

## Measured heights (Playwright, real faces, `getBoundingClientRect` on `#X-scene`)

| archetype | 390 wide (cap 520 / total cap 1500) | of which photo · text | 1366 wide |
|---|---|---|---|
| A — stainless path light (own frame, solar) | **481 px** | 300 · 157 (+24 padding) | 735 px |
| B — waterproof wall light (own frame, mains → no dusk line) | **453 px** | 300 · 129 | 676 px |
| C — solar floodlight (fallback frame + credit line, solar) | **504 px** | 323 (300 + 23 credit) · 157 | 763 px |

All new sections together = the one section: 453–504 px at 390 (the cap is 1500). The path PDP goes from
3498 px to ≈ 3979 px at 390 = 4.7 screens (P5 ≤ 6). Nothing the section needs read lives in the last 78 px of the
page (the sticky bar); the section adds no button. No horizontal overflow at 390 or 1366 (`scrollWidth` = viewport).

Mockup bands: A and B use the path light's true heights (main-product 1085 / facts 723 / related 781, BRIEF §5,
«the wall light like the path light»); C uses the same path numbers — the floodlight PDP was not measured in
SIMPLIFY. Desktop band heights are approximations read off `pdp-path-d-js-full.png` (590 / 470 / 620 / footer 420).

## The rule the Liquid follows (no product data changes)

1. **Photograph — map first, collection fallback.** Section blocks of type `frame`: `product` (product picker),
   `image` (image_picker), `object_position` / `object_position_desktop` (text). The first block whose
   `block.settings.product.handle == product.handle` wins → no credit line. Otherwise the collection handle from
   `{% render 'elmsnest-s-place', product: product, emit: 'collection' %}` picks one of four section settings
   (`image_path` / `image_wall` / `image_spot` / `image_decor`, each an image_picker with the theme asset
   `ens-pdp-<slug>.jpg` as the empty-picker default) and its `credit_<slug>` product setting; the credit line renders
   unless `credit_product.handle == product.handle`. No collection match (a product only in `sale`) → the section renders **nothing** (the place word is blank),
   so a stray product never shows a foreign frame.
2. **Heading and night line — by place word.** `emit:'word'` → שביל / קיר / גינה / מרפסת selects `heading_<slug>`
   and `line_<slug>` (eight text settings with the defaults in COPY.md).
3. **Dusk line — the solar gate**, copied verbatim from `elmsnest-s-place` lines 96–108 (`custom.power_source ==
   'סולארי'`, else title + description contain «סולארי»). 16 of 27 products pass; the five mains wall lights, the
   rechargeable one, the mains bollard, the dual-head, the camping lantern, the net and globe strings and the birch
   branches get no dusk sentence. The decor pair is NOT exempt here: the string lights that are solar get the
   line, the USB ones do not.
4. **Link** — `link_label` + `link_url` settings (default `/pages/guide-garden-lighting`); empty label = no link.
5. **Weight** — one `<img>`, `loading="lazy" decoding="async"`, width/height, `sizes="100vw"`, candidates
   600/900/1254 from `asset_img_url` (or the picker's `image_url` capped at the source width). ≤ 220 KB each,
   progressive JPEG, uploaded to the DEV theme via `themeFilesUpsert`.
6. **Products with no clean frame (10 of 27)** render the collection default with the credit line; the spot
   collection's default is the baked pre-crop described in IMAGES.md (measured clean at 1214×1014).

## Craft notes

- Same skeleton as `elmsnest-s-home-band` (figure in flow, `object-position` per breakpoint as settings) and the
  facts section's text scale (24–26 serif heading at 390, 16 px Heebo 300 lines, 40 serif at 1366), so it reads
  as the same page between the buy box and the facts. Two-column body at ≥ 901 (heading start, lines end)
  mirrors the facts grid.
- Contrast: every glyph is on `#0f1a2f → #070b15` (the page ground), ink `#f4eee3` ≥ 15:1, ink-2 `#c9c4b8`
  ≥ 10:1, the credit line `#8f95a3` 12 px ≈ 5.6:1.
- `<bdi dir="ltr">` around `180°` and `10W IP65` in the credit line; the arrow of the link is `aria-hidden`.

## Is any of this twice? (honest)

Nearly not: the photograph of A and B is the product's own **gallery frame 6**, which the phone shopper never
swipes to but which does exist in the gallery (the judges may weigh that); the dusk sentence says, in new words,
the same solar fact as the home's «ביום נטען. בלילה נדלק.» — deliberate, because on the PDP it sits at the point of
sale; everything else (place heading, night lines, credit line, guide link) is new to the store.
