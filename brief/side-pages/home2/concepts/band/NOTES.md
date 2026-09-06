# Concept «band» — the breath

## What it is

The page does not need more blocks. It needs air. Three sections, thirty-six words, the photographs carry it.

- **[A] `elmsnest-s-home-band`** — one full-bleed night photograph (the store's own crystal-ball string on a picket fence at blue hour) with one sentence: «חושך הוא לא סוף הערב.» Nothing else: no eyebrow, no button, no link. It sits **between the product cards and the fit rows** — after the two grids, before the text block — so the eye rests once before reading again. Different picture from the hero on purpose (a fence and bulbs, not bollards and a hedge).
- **[B] `elmsnest-s-home-solar`** — three plain solar facts, mostly type, each with a 64 px photograph window: the panel, a lit lamp head, a spike in the earth. Heading «ביום נטען. בלילה נדלק.» (BRIEF §2's own example of a category fact). The winter note is one line inside step 1 rather than a section of its own. **After the fit rows.**
- **[C] `elmsnest-s-home-daynight`** — the slim day/night pair the shortlist has (rows 1–2, the same bollards and hedge at two hours), two labels and one line: «אותה גינה, אותן מנורות.» It is the proof of B's heading, so it follows B, **before the terms strip**.

Order: hero → tiles → cards → **A** → fit → **B** → **C** → terms → footer. Photo, grid, grid, **photo**, text, **type**, **photo pair**, text.

## What it refuses

- A second product grid, a second place list, a second contact line, a second guide link (nothing twice, SIMPLIFY §3 / BRIEF §1).
- Reviews, counts, hours-of-light, lumens, «all our lights are…», any «best».
- CC imagery with credit lines: all six frames are the store's own, so no 11 px caption anywhere.
- Carousels, scroll-lit lamps, parallax, hover reveals, any JS. The three sections are plain HTML and CSS; reduced-motion is respected (there is nothing that moves).
- Rounded corners (radius 0 everywhere; the only pill on the page stays the hero button).

## Measured heights (playwright, `getBoundingClientRect`, fonts loaded)

| section | 390 px | ≤ 675? | 1366 px |
|---|---|---|---|
| [A] band | **520** | yes | 546 |
| [B] solar facts | **454** | yes | 325 |
| [C] day / night pair | **322** | yes | 541 |
| all three | 1296 | | 1412 |

Mock page at 390: 5301 px with the existing sections sketched at their measured heights (844 · 761 · 781 · 690 · 397) and a 520 px footer stand-in → **≈ 6.3 phone screens** (limit 7.5; the real page is 4321 now, so 4321 + 1296 = 5617 px = 6.66 screens with the real footer). The desktop grey bands are estimates from `home-d-js-full.png`, not measurements.

## Craft notes

- Type and spacing copy the neighbours: `padding-block:48px 40px` (72/56 on desktop), h2 `clamp(25px,3.4vw,44px)`, hairlines `#1f1e1d`, eyebrow and kicker from core. The band's sentence is `env2-h` at `clamp(30px,8.4vw,54px)` over a bottom scrim (`rgba(2,3,6)` 0 → .9), measured white-on-dark well above 7:1 at the text's position.
- The night frame of the pair carries a baked Hebrew caption bottom-left; it is cropped out in both viewports by CSS only (see IMAGES.md). The step-3 window sits far from the IP65 badge in its source frame.
- The three 64 px windows are `<img>` elements oversized inside `overflow:hidden` figures with `left/top` from three custom properties; in Liquid those become three section settings (`zoom`, `x`, `y`) next to each `image_picker`, defaults set to the theme assets, so the owner can swap a photo and still frame it.
- Weight on the theme: six JPEGs; the band at 1800 px and the pair at 1200 px each, the three squares at 600 px (they render at 64–72 px) — comfortably under 220 KB each; everything below the hero is `loading="lazy"` with width/height.
- Schema: every text above is a setting (`text` / `richtext`), every image an `image_picker` with the asset as the default rendering, so the section works the moment it is added.

## Risks the judges may raise

- The owner may want a product named under the pair (it is the powerful solar garden light). The concept deliberately keeps it wordless: the cards above already sell, and a link here would be the product grid a second time. Adding a `url` setting to [C] is a one-line change if he asks.
- Two of the three tiny windows show a solar panel (step 1 the panel face, step 3 the spike). They are different objects at different scales; if it reads as repetition, step 3 can take the firefly frame (`own_solar-firefly-garden-lights_4`, stems in the ground) with no copy change.
