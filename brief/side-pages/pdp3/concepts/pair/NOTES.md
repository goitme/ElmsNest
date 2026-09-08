# Concept «pair» — notes

Two new sections for the product page: **`ens_pdp_pair`** («בין הצהריים לשקיעה») and
**`ens_pdp_checks`** («לפני שקונים»). Three photographs on the page, one credit line, no JS, no gate.

---

## 1. The device, and why it is a different look

**The pair.** Two photographs of *one kind of place* — a stone path beside a wall — at two hours of
the day, standing **side by side** inside the wrap at the same 4:5 crop, with a **1 px hairline of the
night ground between them**. That is the whole device: the juxtaposition does the work, so nothing has
to be written on a photograph. No scrim, no words over the image, no full-bleed edge, no rule under it.
Two small hour tags (**צהריים** in ink, **שקיעה** in gold) and one caption per frame sit below.

**The checks.** Three tiny square photographs in a row with one short statement under each, then the
guide link. The three squares are three **windows into one photograph** — a strip cut from one frame,
and the caption says so — which is why the section costs the page one file and not three.

**Why this is «not the same colour» (BRIEF §2).** The two round-2 sections are one device: a dark
night photograph edge to edge, words under it on the night ground, then a hairline row. Everything
here is the opposite of that, on purpose:

| round 2 | this concept |
|---|---|
| one photograph, full-bleed | two and three photographs, **framed inside the wrap**, never touching the edge |
| night, blue-black, artificial light | **noon green, sunset amber, hard-noon crimson and blue** — daylight, no lamp in any frame |
| photograph, then words under it | **words first, photographs under them**; on desktop, words in the right column and the pair in the wide left column |
| a hairline **rule** across the row | a hairline **gap** between two frames — a line of the night ground, not a border |
| one image at a time | the **pairing** and the **strip** — plural images are the form |

The night ground of the page is untouched. The sections bring light into it, in three tones the page
has never carried.

## 2. Order in the template (`templates/product.elmsnest.json`)

```
main-product → ens_pdp_scene → ens_pdp_dusk → [ens_pdp_pair] → ens_pdp_facts → [ens_pdp_checks] → ens_related
```

- **`ens_pdp_pair` right after `ens_pdp_dusk`.** The night story of round 2 ends at the dusk row; the
  pair opens the day immediately after it, so the page goes night → dusk → day/sunset instead of
  night → night. On archetype B there is no dusk row, so the pair follows the scene directly; on C the
  pair is the first photograph after the gallery, which is the archetype it helps most.
- **`ens_pdp_checks` after `ens_pdp_facts`, before `ens_related`.** You read the specs, then the three
  things to look at in your own place, then the guide link — the last thing before the related cards.
  Nothing sits between the gallery and the button, and nothing sits after `ens_related`.

Both files are `sections/elmsnest-s-pdp-{pair,checks}.liquid` with a Hebrew `{% schema %}` and
`enabled_on: templates: ["product"]`. The template edit is `product.elmsnest.json` only.

## 3. Measured heights at 390 (Playwright, `getBoundingClientRect`)

| | `ens_pdp_pair` | `ens_pdp_checks` | both | archetype block* |
|---|---|---|---|---|
| **A** stainless path light (solar, photo scene) | **411.1** | **301.7** | 712.8 | 4121.8 |
| **B** waterproof wall light (mains, no dusk row) | **411.1** | **301.7** | 712.8 | 3973.8 |
| **C** solar floodlight (text-only scene) | **411.1** | **301.7** | 712.8 | 3649.8 |

\* the block as rendered in `index.html`: a 60 px header stub, the grey bands at their true heights, the
two new sections, no footer.

Caps: each section ≤ 520 px ✔ (411 and 302) · both together ≤ 1500 px ✔ (713). Because neither section
is gated, the numbers are identical on all three archetypes — the page grows by the same 713 px
whatever the product is.

**Screens at 390 × 844.** Round 2 measured rope 4.85 · path 5.03 · deck 4.41 · wall 4.84 · flood 4.49.
Adding 713 px = 0.84 screens, and giving back ≈ 38 px where the scene's guide link is removed:
path **5.83** · rope 5.65 · wall 5.65 · flood 5.29 · deck 5.21. The worst page is 5.83 of the 7.5 cap ✔.

Desktop (1366): pair 716 px, checks 416 px.

## 4. The gate, per family

**There is none, and that is the design.** Both sections are family-agnostic and power-agnostic:

| family | `ens_pdp_pair` | `ens_pdp_checks` |
|---|---|---|
| שביל (path) | prints, same copy, same two photographs | prints, same three statements |
| קיר (wall) | prints | prints |
| גינה (spot) | prints | prints |
| מרפסת (decor) | prints | prints |
| solar / mains / USB / battery | no difference | no difference |

Why: the round-2 sections already carry all the per-product logic (the scene's photograph map, the
dusk row's solar gate, the facts' bullets). Adding two more gated sections would multiply the states an
engineer has to hold. Both new sections say something true of *any* outdoor light in *any* place — the
hour changes what you see, and these are the three things to look at in your own garden — so they need
no product data, no metafield and no per-family variant. The only Liquid conditions are `product !=
blank` and «is an image slot filled».

Available but **not shipped**: `image_picker` slots per family (four day/sunset pairs instead of one),
if the owner ever wants the path pair on path products and a wall pair on wall products. That is eight
settings and no new logic; the copy would not change.

## 5. Weight

Three files, all lazy, all sized, `asset_img_url` candidates never wider than the file
(1920 · 2047 · 3840 px).

| photograph | srcset | largest candidate | at 390 (1×) | at 1366 (2×) |
|---|---|---|---|---|
| alley, day (pair) | 400 · 600 · 900 | **213 KB** @ 900 w | 47 KB @ 400 w | 213 KB |
| stone path, sunset (pair) | 400 · 600 · 900 | **132 KB** @ 900 w | 27 KB @ 400 w | 132 KB |
| garden wall (checks, one file for three tiles) | 400 · 600 · 900 | **163 KB** @ 900 w | 73 KB @ 600 w | 163 KB |

Every candidate is ≤ 220 KB (measured at q80; the Shopify CDN encodes smaller). A phone at 390 loads
**≈ 147 KB** for all three new sections; a 1366 screen at 2× loads ≈ 508 KB, spread over two sections
that are both below the fold. The three tiles of `ens_pdp_checks` are three `<img>` with the same
`src`, so the row is **one** network fetch, not three.

No JS, no carousel, no parallax, no reveal, no second buy button, no second price, radius 0, logical
properties throughout. The only non-obvious CSS is the checks tile: the `<img>` sits at 260 % of the
tile inside `overflow:hidden` and is panned with two custom properties — a plain CSS crop, `dir="ltr"`
on the figure so the logical insets map to the photograph's own left and top.

## 6. Is any of this twice? — the honest answer

**One thing was, and it is fixed rather than argued away: the guide link.** `ens_pdp_scene` carries
«למדריך לבחירת תאורה ←» today, and `ens_pdp_checks` is exactly where a guide link belongs — under the
three checks it answers. So the scene's `link_label` setting is emptied in
`templates/product.elmsnest.json` (a settings value, no code change) and the link is drawn **once**, in
the new section. The grey scene band in `index.html` is labelled with that change, and the ≈ 38 px it
gives back is in the screen counts above.

Two smaller ones, weighed and kept:

- **A second and a third photograph of a place.** The scene already shows a place at night. The pair
  shows a place by day and at sunset. It is a photograph again — but of a *different* thing (a place
  the store does not sell, at hours the page has never shown, framed instead of full-bleed), and the
  captions say so. If the owner wants only one photographic idea on the page, the section to drop is
  `ens_pdp_checks`, not the pair.
- **«המקום נמצא בחוץ»** is adjacent to the not-for line on solar path and spot products
  («לא מתאים כשהמקום כמעט אינו מקבל אור יום») — both point at the shopper's own spot. They are not the
  same sentence and not the same fact: the not-for line is about daylight reaching the panel, this is
  about the light living outside. The sun check that the seed suggested — «המקום מקבל שמש» — *would*
  have been that line said twice, which is why it is not in this concept.

Everything else is new to the page: the two hours, the two captions, the three statements, and the
whole device.
