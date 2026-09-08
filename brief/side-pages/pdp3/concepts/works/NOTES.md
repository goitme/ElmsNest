# Concept «works» — «how it works, in daylight» (PDP round 3, 2026-09-07)

## The device, and why it is a different look

**Prints on the night.** Both new sections are one idea: a cream mat (`--env2-ink`, `#f4eee3`, radius 0) inside the wrap,
with a photograph set into it and its words typed on the mat in dark ink (`--env2-btn-ink`) — a print laid on the night
page, the way a photograph lies on a table in the evening. The night ground never changes; the sections bring light
into it, as BRIEF §2 asks. Against the two round-2 sections (an edge-to-edge night photograph with words under it on
the night ground; a hairline row) this is the opposite in every axis the owner named: **framed, not full-bleed; cream and
daylight, not blue-black; words on the mat, never on the photograph; small pictures, not one big one; no hairline.** The
page keeps its serif heading scale (`clamp(25px,3.4vw,44px)`), its wrap, its two desktop columns (the facts' / scene's
grid: heading inline-start, print inline-end), so it is unmistakably the same store.

1. **`ens_pdp_works` — «איך זה עובד»** (solar only). One print holding three small tiles, read right to left: a real
   solar cell in hard sun (cool blue — the «different colour» in one frame), the sky at dusk (purple-amber), and the
   night — which is **not a photograph** but the page's own ground with one drawn glow, a light without a lamp. Each tile
   is named by a 12–13 px caption under it; the two credits sit on the mat. The section says nothing in sentences: the
   dusk row directly above already says the words, this print shows them. The third tile is the honest answer to two
   constraints at once — «≤ 3 photographs per page» and «an internet photograph never presented as this product»: the
   only night light on this page that could be mistaken for the product is the product's own, in the scene above.
2. **`ens_pdp_place`** (every family). One serif sentence («האור האחרון של היום.») in the heading column and one print:
   a real garden path and dry-stone wall at golden hour, captioned as a place («גינה בשעת בין ערביים»), credited. Warm
   amber on the night page; atmosphere, explicitly not the product.

On the **mains wall light (B)** the works section prints nothing — there is no daylight mechanism to show on a mains
lamp, and a «wall · bracket · beam» triptych would be decoration pretending to explain (the pool also has no bracket or
beam frame). Absence is the design: B keeps the scene, the facts, and gets the golden print before the related grid.

Type on photographs: **none** — so nothing to measure on a picture. Measured on the mat: caption ink 16.05:1, credit
4.83:1 (≥ 4.5:1); the serif headings on the ground: 15.0:1 (sky-2) to 17.0:1 (sky-3).

## Order in the template (`templates/product.elmsnest.json` → `order`)

```
main-product → ens_pdp_scene → ens_pdp_dusk → ens_pdp_works → ens_pdp_facts → ens_pdp_place → ens_related
```

- `ens_pdp_works` sits right after the dusk row so the row's two sentences and the print read as one thought (words, then
  pictures); on a text-only scene (C) the row and the print still follow each other.
- `ens_pdp_place` sits after the facts, before the related grid — a breath between the specs and the cards; never after
  `ens_related`. Nothing sits between the gallery and the button.

Files: `sections/elmsnest-s-pdp-works.liquid`, `sections/elmsnest-s-pdp-place.liquid` (Hebrew `{% schema %}`,
`enabled_on: templates: ["product"]`, presets), the template edit only. Stock patterns: no JS, no carousel, no parallax,
no reveal, no second buy button or price, radius 0, logical properties, `prefers-reduced-motion` guard.

## Measured heights at 390 (playwright, `getBoundingClientRect`, fonts loaded, images decoded)

| archetype | `ens_pdp_works` | `ens_pdp_place` | new together | cap check | page (round-2 doc height + new) | screens at 844 |
|---|---|---|---|---|---|---|
| A — stainless path light (solar, photo scene) | **337.75** | **397.59** | **735.34** | each ≤ 520 ✓ · together ≤ 1500 ✓ | 4246 + 735 = 4981 | **5.90** (cap 7.5) |
| B — waterproof wall light (mains) | 0 (prints nothing) | **397.59** | **397.59** | ✓ | 4081 + 398 = 4479 | **5.31** |
| C — solar floodlight (solar, text-only scene) | **337.75** | **397.59** | **735.34** | ✓ | 3791 + 735 = 4526 | **5.36** |

At 1366: works 453.88, place 540.77 (A, C); place 540.77 (B). No horizontal overflow at either width (`scrollWidth` =
viewport). Round-2 doc heights from `../../../pdp2/verify-after/verify.json`.

Budget of the works section at 390: 40 + h2 28 + 18 + mat (10 + tiles 140 + 8 + caption ≈ 16–32 + credit 10 + 17 + 2 + 10)
+ 40 ≈ 338. Place: 40 + line 28 + 18 + mat (10 + photo 220 + 10 + caption 22 + 10) + 40 ≈ 398.

## The gate, per family

| family (`elmsnest-s-place emit:'word'`) | `ens_pdp_works` | `ens_pdp_place` |
|---|---|---|
| שביל (path) — solar products | prints | prints |
| שביל — the mains bollard `modern-led-bollard-light-5w-ip65` | nothing | prints |
| קיר (wall) — `solar-wall-light-motion-sensor-ip65` | prints | prints |
| קיר — the mains / rechargeable wall lights (B) | nothing | prints |
| גינה (spot) — solar spots, lantern, floodlight (C), security light | prints | prints |
| גינה — dual-head (mains), camping lantern (rechargeable) | nothing | prints |
| מרפסת (decor) — solar strings, firefly, crystal | prints | prints |
| מרפסת — USB globe string, 220V net, battery birch | nothing | prints |
| no place collection (a product only in `sale`) | nothing | nothing |

The works gate is the dusk row's, copied verbatim from `snippets/elmsnest-s-place.liquid` (three states:
`custom.power_source == 'סולארי'`; when unwritten, title + description must contain «סולארי»; anything else is not
solar). No product data is read beyond that; no product, collection, page or metafield changes. The place section is
ungated: optional per-family `image_picker` slots (`image_path`, `image_wall`, `image_spot`, `image_decor`; empty = the one
default asset `ens-pdp-place-garden.jpg`) let the owner give the wall family its own place later without a code change;
the caption is a text setting per slot so an owner-picked photograph is always named.

## Weight

Images per page (deploy assets, `IMAGES.md`): A / C ≈ 190 KB (two 600x tiles ≈ 35 KB each, the garden at 1200x ≈ 120 KB),
B ≈ 120 KB; every `<img>` lazy, `width`/`height` set, `srcset` candidates capped at the file's width. CSS ≈ 2.4 KB (works)
+ 1.6 KB (place) inline per section, no JS, no font added (the page's Frank Ruhl Libre and Heebo). Three network
requests on A/C, one on B.

## Honest «is any of this twice?»

- **The triptych is the dusk row in pictures.** The row says «ביום הפאנל אוסף שמש, וזה מה שמאיר בלילה»; the print shows a
  cell in the sun, a dusk sky, a night glow. No sentence is repeated — the print has no sentence — but the *thought* is
  told twice, once in words and once in pictures, deliberately adjacent. If the owner counts that as twice, the honest
  cut is to drop the dusk row on solar products and let the print carry it (the row is 152 px; the print is 338).
- **«לילה»** is the page's word already (the scene's «בלילה, על השביל», the row's «בלילה»). Here it is a one-word caption
  naming a tile that is not a photograph; it cannot be named anything else.
- **«האור האחרון של היום.»** rhymes in meaning with the row's heading «כשמחשיך» — both are about the hour — but it is a
  different sentence about a different thing (the sun's last light, not what the panel does).
- **A path at golden hour under a path light's «בלילה, על השביל»** (A): the same kind of place at another hour, framed and
  captioned as someone else's garden. Not the same picture, not the same device.
- Nothing else: no second price, no second button, no second guide link, no specs, no terms, no contact, no place line.

## What I would still check before deploy

Re-fetch the Flickr original of `ov_42864d07` (1024 px as downloaded; fine at 390, soft at 2× on desktop); export the
three theme assets at the sizes in `IMAGES.md`; measure the real page in the theme preview at 390 — the print's height
depends on the caption wrapping in the store's rendered Heebo, which this concept loads from the same offline pack.
