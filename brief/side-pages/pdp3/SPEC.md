# Product page, round 3 — the spec (lead synthesis, 2026-09-08)

## 0. What was asked, and what this spec builds

The owner asked (Arabic, verbatim in `BRIEF.md` §0): more content on the product page — two or three more image
sections, creative, **«not the same look/colour»** — and the photographs may come from the internet.

This spec builds **two new sections and three photographs per page** (the BRIEF §4 cap of three photographs is what
stops a third section: a third would need a fourth file). Both use the device the round-2 sections do not: a
photograph **framed inside the wrap**, never full-bleed; **no word on any photograph**; a 12 px muted caption under
each frame naming what it is and carrying the credit; and **daylight and cream tones** — wet grey, hard noon sun, a
golden-hour print on a cream mat — brought onto the night ground.

## 1. The five concepts, the judges, and the lead's rulings

Concepts in `concepts/{works,install,weather,daylight,pair}/`. Five judges scored from the real shots (owner and
shopper ×1.5): **works 43.2 · weather 41.0 · daylight 39.8 · pair 37.0 · install 33.5**.

The build is not the top-ranked folder as drawn. The owner's verdict was explicit — *«The winner is weather, on one
condition: I approve its first section and reject its second… In its place I take works's golden-hour print»* — and
the honesty guardian independently scored weather 3 for that same second section. The lead follows the owner:

| # | Ruling | Why (judge, evidence) |
|---|---|---|
| R1 | **Build weather's first section** «בחוץ, כל השנה» as `ens_pdp_weather`. | Owner 8 («exactly what I asked for — a different colour, a different device»), shopper 8 («the only copy that answers, in one read and in my own weather»), designer «the cleanest, most restrained thing in the round» at 1366, honesty «exemplary… materials, never places with someone else's lamps». |
| R2 | **Reject weather's second section** «בין ערביים» (the Cuernavaca courtyard). | Honesty 3: the frame carries at least three glowing lantern fixtures and two planter uplights under a heading about the hour a light is needed — BRIEF §4 forbids it outright; the caption also called a hotel a house. Owner: «one Mexican hotel courtyard printed on every family». Shopper: honest caption, still reads as lamps. |
| R3 | **Build works's cream print** in its place as `ens_pdp_print` — one golden-hour photograph of a real place on a cream mat, one serif line «האור האחרון של היום.», the caption and credit at the mat's foot. | Owner takes it by name; shopper «the most convincing different look of the five»; designer «words on the mat and never on the photograph»; engineer 9 for works's plumbing. |
| R4 | **Do not build works's triptych** «איך זה עובד». | Honesty 8 but: «the triptych is the dusk row told a second time in pictures» (its own NOTES concede it); owner «the thinnest answer»; designer «a near-black rectangle with a fuzzy orange dot reads as a failed image». SIMPLIFY §0: nothing twice. |
| R5 | **Do not build an installation section** (`install`). | Honesty 5: on the MAINS wall light the page would print «מתחברת לקיר… דיבל, בורג, וזהו» — a mounting claim the listings do not state. Owner and designer both reject the photographs («a snapshot of dirty hands in weeds», «a red wall plug on a white studio ground»). The copy the shopper loved («בלי חפירה, בלי חיווט») is recorded as an **owner item** (§6.1): it can return per product once the owner confirms each product's mounting. |
| R6 | **Do not build the sand card** (`daylight`) or the diptych (`pair`). | daylight: owner «the identical bougainvillea wall appears three times on one page», designer «a loud manila-yellow that competes with the amber buy button», engineer «three sections, five assets for a round that asked for two or three». pair: honesty «the comparison the photographs do not support» (two different places sold as one), engineer 5 («there is no gate, and that is the design» misses §4's per-product rule). |
| R7 | **Fix the flagship pair's two blue panels.** In `ens_pdp_weather` the sun tile is the **white wall in noon sun** (CC0) on **every** product; only the rain tile is gated (solar → rain on a panel; everything else → drops on a stem). | Designer: «on the flagship solar page the pair is two solar panels side by side, cold blue twice». This also keeps the section off the dusk row's subject: the pair is about weather, not about charging. |
| R8 | **No Haifa frame on a product page.** | Honesty on daylight: «three pale bollard-shaped fixtures stand along the path» in the Haifa crop. It stays available for the content pages, cropped. |
| R9 | Keep the round-2 sections untouched (`ens_pdp_scene`, `ens_pdp_dusk`, `ens_pdp_facts`), keep the page's single guide link in the scene, add no second button, price, link or claim. | SIMPLIFY P1–P7; BRIEF §4. |

## 2. `sections/elmsnest-s-pdp-weather.liquid` — «בחוץ, כל השנה»

**Device.** Two framed detail tiles side by side inside the wrap: 1:1 at 390 (two columns, 12 px gap), 3:2 at ≥ 901.
Under each tile: one short line (Heebo 400, `--env2-fs-body`), then a 12 px muted caption + credit
(`#8f8b83`, one `<bdi dir="ltr">` around the Latin credit). Heading above the pair (`env2-h`, Frank Ruhl Libre 700).
No text on a photograph, no scrim, no hairline row, radius 0, logical properties, no JS.

**Gate (by rule, no product data).**
1. *Prints at all* — only when the product's own description carries an outdoor IP token: `IP65`, `IP66`, `IP67`,
   `IP68` (the same token list the facts section already scans). No token, or `IP44` and lower → the section prints
   nothing (the birch branches, the camping lantern, the USB globe string, the net lights).
2. *Which rain tile* — the dusk row's solar test copied verbatim (`product.metafields.custom.power_source == 'סולארי'`,
   else the stripped title + description contain «סולארי») → the panel tile; anything else → the stem tile.

**Copy** (settings with these defaults):

| setting | default |
|---|---|
| `heading` | בחוץ, כל השנה |
| `line_rain` | גשם של ינואר. התאורה נשארת בחוץ. |
| `line_sun` | שמש של אוגוסט. אותו הדבר. |
| `cap_rain_solar` | טיפות גשם על פאנל סולארי |
| `cap_rain_plain` | טיפות על גבעול, אחרי הגשם |
| `cap_sun` | קיר לבן בשמש של צהריים |
| `credit_rain_solar` | צילום: h080 (CC BY-SA 2.0) |
| `credit_rain_plain` | צילום: jenny downing (CC BY 2.0) |
| `credit_sun` | *(empty — CC0 needs none)* |

**Images** (theme assets, `image_picker` override per slot, empty picker → the asset):

| slot | asset | source id | licence | crop (`object-position` phone / desktop) |
|---|---|---|---|---|
| rain, solar | `ens-pdp-rain-panel.jpg` (1066×1600, 188 KB) | `ov_dbe4a3f1…` | CC BY-SA 2.0 h080 | 50% 50% / 50% 45% |
| rain, other | `ens-pdp-rain-stem.jpg` (1600×1067, 152 KB) | `ov_5795ed8a…` | CC BY 2.0 jenny downing | 50% 50% |
| sun, all | `ens-pdp-sun-wall.jpg` (1200×900, 196 KB) | `ov_7379ba54…` | CC0 Carol M Highsmith | 50% 50% / 55% 50% |

## 3. `sections/elmsnest-s-pdp-print.liquid` — the cream print

**Device.** A cream mat (`#efe7d8`) inset in the wrap with 14 px padding: one photograph at 3:2 (390) / 16:9 (≥ 901)
bleeding to the mat's inner edge, then on the mat itself — never on the photograph — the caption naming the place and
the credit (11 px, `#6b6558`), and above the mat one serif sentence on the night ground. This is the one cream surface
on the page; it is a *print lying on the night page*, and it is the round's answer to «not the same colour».

**Gate.** Prints when `elmsnest-s-place emit:'word'` is not blank; the two scene overrides
(`lighted-birch-branches-20-led`, `rechargeable-telescopic-camping-lantern`) print nothing — an evening garden is not
their place. The photograph and the caption are chosen by the place word.

**Copy.** `line` (default «האור האחרון של היום.», Frank Ruhl Libre 400, `--env2-fs-h3`), plus per-family captions:

| place word | asset | source id | licence / credit | caption |
|---|---|---|---|---|
| שביל | `ens-pdp-print-path.jpg` (1200×781, 188 KB) | `ov_42864d07…` | CC BY 2.0 → צילום: Corey Leopold (CC BY 2.0) | שביל אבן בשעת בין ערביים |
| קיר | `ens-pdp-print-wall.jpg` (1600×1063, 189 KB) | `ov_93506e94…` | CC BY 2.0 → צילום: BPPrice (CC BY 2.0) | גינה של בית, באור אחרון |
| גינה | `ens-pdp-print-garden.jpg` (1000×667, 197 KB) | `wm_faf95922bd` | CC BY-SA 4.0 → צילום: Basile Morin (CC BY-SA 4.0) | ספסל בגינה, לפנות ערב |
| מרפסת | `ens-pdp-print-balcony.jpg` (1600×1067, 166 KB) | `ov_c3ee8ae1…` | CC BY-SA 2.0 → צילום: tillwe (CC BY-SA 2.0) | מרפסת בשעת בין ערביים |
| *(fallback picker)* | `ens-pdp-print-path.jpg` | — | — | — |

No frame in this set contains an artificial light fixture (R8). All seven assets are prepared and on disk (`images/CHOSEN.md`): ≤ 1600 px, ≤ 202 KB, `loading="lazy"`,
`width`/`height` set, `srcset` candidates capped at the file width, `sizes` matching the rendered width.

## 4. Template order (`templates/product.elmsnest.json`, the only template edit)

`main-product` → `ens_pdp_scene` → `ens_pdp_dusk` (solar only) → **`ens_pdp_weather`** → `ens_pdp_facts` →
**`ens_pdp_print`** → `ens_related`.

The weather pair sits directly above the facts so the IP numeral answers the pictures without a word; the print is the
warm breath between the numbers and the related grid. Nothing between the gallery and the button; nothing after
`ens_related`.

## 5. Budgets and verification

- Heights at 390: `ens_pdp_weather` ≤ 430 px, `ens_pdp_print` ≤ 420 px, both together ≤ 850 px (cap 1500).
- Pages at 390×844 (deployed today → expected): path 5.03 → ≤ 6.1 · rope 4.85 → ≤ 6.0 · deck 4.41 → ≤ 5.5 ·
  wall 4.84 → ≤ 6.0 · flood 4.49 → ≤ 5.6 screens. **Cap 7.5** (BRIEF §4).
- `verify-mirror.js` probes: add `ens-pdp-weather` / `ens-pdp-print` to the `pdpSections` selector, and the new
  sentences to the copy table; every image `sized`, `lazy`, `loaded`, `srcset` ≤ file width; contrast of caption and
  credit on the mat and on the night ground ≥ 4.5:1 (`pdp2/verify/contrast.py`).
- Weight added per page ≤ 260 KB (three JPEGs).

## 6. Owner items this round records (not built)

1. **An installation line per product** («בלי חפירה, בלי חיווט» / «דיבל, בורג, וזהו») — the shopper's favourite
   sentence in the round. It needs the owner to confirm each product's mounting; the store cannot claim it from the
   listings alone (R5).
2. **A real Israeli place at dusk.** Every Israeli frame in the pool is midday; the golden-hour places are
   Mediterranean-looking but photographed elsewhere (a Californian stone wall, a Singapore bench, a German balcony).
   The captions say what each place is, honestly — but the owner's own dusk photograph of a garden here would replace
   any of them in one picker.
3. **The dusk row's second sentence** and the twelve products without a clean night frame remain open from round 2.
