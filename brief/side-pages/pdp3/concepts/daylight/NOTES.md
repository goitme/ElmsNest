# Concept «daylight» — «the same garden by day» (PDP round 3, 2026-09-07)

## The device, and why it is a different look

**A window of day let into the night page.** One idea across the three sections: a **sand-coloured card** (`#ead9b3`, a warm
amber-cream, radius 0) inset in the wrap, with the photograph set into the card and bleeding to the card's edges, and the
words typed in dark ink (`#1a1206`) **on the sand — never on the photograph**. The night ground of the page stays (the card
sits on sky-3/sky-4); the card is the daylight, framed. Against the two round-2 sections (an edge-to-edge night photograph
with words under it on the night ground; a hairline row) it is the opposite on every axis the owner named:

- **Framed, not full-bleed** — the card is inside the wrap; no photograph touches the page edge.
- **Day, golden hour and noon, not blue-black** — a sunset path, a noon wall, a noon terrace garden, a solar cell in hard sun.
- **Sand and dark ink, not night and cream** — the only light-ground surface on the page, deliberately the opposite tonality.
- **Beside, not under** — at ≥ 901 the words stand beside the photograph (photo on the inline-start, words on the inline-end);
  at 390 the photograph is the card's top and the words its foot, all on the sand.
- **No hairline, no text on a picture** — so nothing to measure on a photograph. Measured on the sand: ink 13.3:1, muted
  captions and credits 6.38:1; the checks note on the night ground (ink-2 on sky-3) 11.31:1.

The three sections and their place in the page (the «same garden» thought):

1. **`ens_pdp_day` — «ביום»** (every family). After the scene's night photograph of THIS product and the dusk row, a real
   place by day: a path at sunset for the path family, a house wall at noon for the wall family, a terraced garden at noon
   for the spot family, a balcony at golden hour for decor (four `image_picker` slots, one theme asset each as the empty
   default, the caption a text setting per slot so an owner-picked photograph is always named). One line in two variants
   by the solar gate: solar — «מה שהפאנל רואה בצהריים, ה{place} רואה בלילה.»; not solar — «ביום הוא רק חלק מה{place}. האור
   מחכה לערב.» The naming caption («שביל בגן קקטוסים, לפנות ערב» …) sits on the same card, 12 px, with the credit beside it
   when one is owed.
2. **`ens_pdp_cell` — «מקרוב»** (solar only). A second, low sand card hung 4 px under the first — two panes of one window —
   with a 1:1 detail of a real solar cell in the sun at its inline-start, the word «מקרוב», one line («תא סולארי. הצד שפונה
   לשמיים.») and the credit. On a mains / USB / battery product the section prints nothing: no root, no style, no substitute.
3. **`ens_pdp_checks` — «לפני שקונים»** (after the facts, before the related grid). Three small tiles on one sand card — each
   a **detail crop of the same «ביום» photograph** (the same asset, another `object-position` and a zoom: no fourth file on
   any page) — with one word and one statement, never a question: «שמש» (solar only), «מרחק» (always), «בחוץ» (when the
   listing carries an IP code). A note under the card says so («שלושה פרטים מתוך תמונת היום») and repeats the credit. On B
   the sun tile fails the gate and the card is a two-up; fewer than two tiles → nothing prints.

No device already on the page is repeated: no second full-bleed band, no second hairline row, no words on a photograph;
the home's two-frame figure (words on scrims) is not repeated either. The page keeps its wrap, its serif heading scale for
«לפני שקונים» (`clamp(25px,3.4vw,44px)`), its Heebo body — the same store.

## Order in the template (`templates/product.elmsnest.json` → `order`)

```
main-product → ens_pdp_scene → ens_pdp_dusk → ens_pdp_day → ens_pdp_cell → ens_pdp_facts → ens_pdp_checks → ens_related
```

- `ens_pdp_day` right after the dusk row: night (scene) → the sun (row) → the same kind of place by day (card).
- `ens_pdp_cell` immediately under it (4 px gap): the material the row talks about, up close. On B both the row and the cell
  are empty, so the day card follows the scene directly.
- `ens_pdp_checks` after the facts and before `ens_related`: the last thing before «more for the same place». Nothing between
  the gallery and the button; nothing after `ens_related`.

Files: `sections/elmsnest-s-pdp-day.liquid`, `sections/elmsnest-s-pdp-cell.liquid`, `sections/elmsnest-s-pdp-checks.liquid`
(Hebrew `{% schema %}`, `enabled_on: templates: ["product"]`, presets), the template edit only. Stock patterns: no JS, no
carousel, no parallax, no reveal, no second buy button or price, radius 0, logical properties (the crop point is a physical
`object-position` — a fact about the photograph, not about reading direction), `prefers-reduced-motion` guard.

## Measured heights at 390 (playwright, `getBoundingClientRect`, DPR 1, fonts loaded, images decoded — `shots/measure.json`)

| archetype | `ens_pdp_day` | `ens_pdp_cell` | `ens_pdp_checks` | new together | caps | page (round-2 doc height + new) | screens at 844 |
|---|---|---|---|---|---|---|---|
| A — stainless path light (solar, photo scene) | **411.55** | **160.00** | **324.16** | **895.71** | each ≤ 520 ✓ · together ≤ 1500 ✓ | 4246 + 896 = 5142 | **6.09** (cap 7.5) |
| B — waterproof wall light (mains) | **387.55** | 0 (prints nothing) | **361.97** (two-up) | **749.52** | ✓ | 4081 + 750 = 4831 | **5.72** |
| C — solar floodlight (solar, text-only scene) | **407.64** | **160.00** | **324.16** | **891.80** | ✓ | 3791 + 892 = 4683 | **5.55** |

The day card's photograph is 350×219 at 390 (16:10); the checks tiles 102×102 (three-up) / 158×158 (two-up).
At 1366: day 546.78 / 606.67 / 544.33 (A / B / C; the photograph column 723×483–543), cell 236, checks 526.27 (A, C) /
502.20 (B); tiles 392×245. `scrollWidth` = viewport at both widths (no horizontal overflow). Round-2 doc heights from
`../../../pdp2/verify-after/verify.json` (path 4246 · wall 4081 · flood 3791).

Budget of the day card at 390: 36 (section) + 219 (photo) + 18 + 34 (h2) + 10 + 48 (line, two rows) + 10 + 4 + 17 (caption)
+ 16 ≈ 412; C adds a second caption row for the credit (≈ +17, offset by a one-row line). Cell: 4 + 12 + 132 + 12 = 160.
Checks: 36 + 27.5 (h2) + 14 + card (12 + 102 + 6 + 4 + 18 + 6 + 55 + 12) + 8 + 16 + 8 ≈ 324.

## The gate, per family (by rule, no product data beyond the place word and the dusk row's solar test)

| family (`elmsnest-s-place emit:'word'`) | `ens_pdp_day` (slot · line) | `ens_pdp_cell` | `ens_pdp_checks` (tiles) |
|---|---|---|---|
| שביל (path) — solar products (A: stainless, retro set, powerful garden light, swaying set, step/deck lights…) | path slot · solar line | prints | שמש · מרחק · בחוץ |
| שביל — the mains bollard `modern-led-bollard-light-5w-ip65` | path slot · mains line | nothing | מרחק · בחוץ |
| קיר (wall) — `solar-wall-light-motion-sensor-ip65` | wall slot · solar line | prints | שמש · מרחק · בחוץ |
| קיר — the mains / rechargeable wall lights (B and its siblings) | wall slot · mains line | nothing | מרחק · בחוץ (IP in the bullets) |
| קיר — the magnetic indoor touch light (no IP code) | wall slot · mains line | nothing | **nothing** (one tile only) |
| גינה (spot) — solar spots, lantern, floodlight (C), security light | spot slot · solar line | prints | שמש · מרחק · בחוץ |
| גינה — dual-head (mains, IP65), camping lantern (rechargeable, no IP) | spot slot · mains line | nothing | dual-head: מרחק · בחוץ; lantern: nothing |
| מרפסת (decor) — solar strings, firefly, crystal | decor slot · solar line | prints | שמש · מרחק · (בחוץ when IP is in the bullets) |
| מרפסת — USB globe string, 220V net, battery birch branches | decor slot · mains line | nothing | nothing (no sun tile, no IP → one tile) |
| no place collection (a product only in `sale`) | nothing | nothing | nothing |

The solar test is the dusk row's, copied verbatim from `snippets/elmsnest-s-place.liquid` (three states:
`custom.power_source == 'סולארי'`; when that metafield is unwritten, title + description must contain «סולארי»; anything
else is not solar). The «בחוץ» tile reads the listing's own outdoor claim (title + description `contains 'IP'`), the
facts section's technique. The indoor birch branches keep their «בערב, בבית» scene and get a balcony-at-dusk card with
the mains line — honest, if a little generous; the owner can empty the decor picker and the section prints text-only.

## Weight

Deploy assets (`IMAGES.md`): per page never more than two files — the day photograph (≤ 220 KB at its largest candidate,
≈ 100–115 KB at the `800x` a 390 phone takes) and the cell tile (91 KB at 600, 45 KB at 400). A ≈ 160 KB on a phone /
≈ 300 KB max; B ≈ 100 / 205 KB; C ≈ 100 + 45 / 219 + 91 KB. The checks tiles cost no request (same asset). CSS ≈ 1.9 KB
(day) + 0.9 KB (cell) + 1.4 KB (checks) inline per section; no JS; no font added.

## Honest «is any of this twice?»

- **The sun, three times on a solar page.** The dusk row («ביום הפאנל אוסף שמש…», «יותר שמש ביום, יותר אור בלילה»), the day
  card's line («מה שהפאנל רואה בצהריים, השביל רואה בלילה») and the «שמש» tile («שמש ישירה על הפאנל, לא מבעד לענפים») are
  three sentences about one dependency. No sentence repeats another — the row says what the panel does, the card says what
  the place gets, the tile says where to put the panel — but a strict owner may read the *thought* as told twice. The honest
  cut, in order: drop the «שמש» tile (the checks become a two-up everywhere: −0 px on B, −0 px on A/C — the tile row keeps
  its height); then, if still twice, drop the day card's line and let the heading «ביום» and the caption carry the card.
- **«בחוץ» beside a page that prints an IP numeral.** The tile says a general thing (under the sky, rain and sun) and never
  the code; the facts say the code. Two registers of one fact — the brief's seed 3 allows exactly this; flagged anyway.
- **«לפני שקונים» as a checklist.** The round-2 judges rejected the guide's three checks *under the price*; here they sit
  after the facts, as three pictures with one statement each, no questions, no link. If the owner still reads them as the
  guide again, the section is the one to cut — the concept stands on the two cards.
- **A path at sunset under a page whose scene is a path at night** (A): the same kind of place at the other hour, framed,
  captioned as a cactus garden — not the same picture, not the same device; that adjacency is the point of the concept.
- Nothing else: no second price, no button, no guide link, no specs, no terms, no contact, no place line, no «כשמחשיך».

## What I would still check before deploy

Export the four day assets and the cell tile at the sizes in `IMAGES.md` (the cactus band lands at ≈ 205 KB at 1100 / q78;
1200 / q80 is 258 KB, over the cap); measure the real page in the theme preview at 390 — the card's height moves with the
line's wrapping in the store's rendered Heebo (this concept loads the same offline pack); confirm the Haifa crop on a 2×
desktop (the balustrade's globe finials must stay outside the right edge — they do at ×2.3 on 1366); the decor slot's
balcony frame is 2048 px and soft — re-fetch the Flickr original or swap in the purple sage before the decor family ships.
