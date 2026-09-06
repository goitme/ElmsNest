# Product page, round 2 — SPEC (2026-09-06): two sections, one photograph, the store's own frames only

> **Amended after the critique of the deployed render** (`critique/LEAD-DECISIONS.md`, 2026-09-06): the rope frame is
> re-cut below its baked IP65 badge (y 380 → 1254×874 — the first pre-crop, read off a thumbnail, was wrong), the powerful
> bollard frame loses the legs at its top-right (y 90 → 1254×1040), the step-light frame its headline stroke (y 345 →
> 854×909); stainless and the path scene are 1100 px / ≤ 220 KB; lantern 9 crops at «0% 50%», edison at «50% 30%» on
> desktop; the spot line drops its «בלילה» («אור מכוון אל מה שרוצים לראות.»); the camping lantern is headed «בלילה, בשטח»
> (`heading_portable`); the text-only state renders as a hairline row (20/22 px heading, the facts' `<dl>` column at
> ≥ 901); the dusk row sets each sentence on its own line inside a closed row (hairline above and below, 16 px of air
> above, the facts' column at ≥ 901); the fallback option shows no photograph when its pictured product is not live; a
> file narrower than 1254 offers its own width as a srcset candidate. The amended text is inline below.

Lead's synthesis after five concepts and five judges (`concepts/`, ranking **one 49.75 · scene 49.25** · places 42.5 ·
checks 36.75 · dusk 36.25 — a tie at the top: the owner and the honesty judge put *scene* first, the shopper, the
designer and the engineer put *one* first, and every judge named the other as the thing to borrow from). Built:
**one's** layout (the photograph left alone, every word on the night ground under it, the place heading that is
true on every product, the guide link as the section's only link) with **scene's** photograph height and its split
into a scene section plus a small «כשמחשיך» row for solar products, and the rule every judge converged on for the
products that have no clean frame of their own: **no photograph rather than another product's photograph** (the
owner's «swapped product photos» complaint, SIMPLIFY §0/§1) — the collection scene with a credit line exists as an
owner option, off by default. The shopper's favourite sentence («יותר שמש ביום, יותר אור בלילה.») and the honesty
judge's two corrections (no «נדלק» on products with a remote, timer or sensor; no spot line that contradicts the
floodlight's «מאיר רחב») are in the copy. Dropped: the dusk detail square (a second device, fragile CSS), the
triptych, the checklist, the winter line (the home says it), text on the photograph (the home band already does
that once).

## 1. The sections and where they go

`templates/product.elmsnest.json` order becomes: `main-product` → **`ens_pdp_scene`** → **`ens_pdp_dusk`** →
`ens_pdp_facts` → `ens_related`. Desire before detail: the shopper who has just read the price, the button and the
not-for line gets the picture the carousel hides at gallery frame 4–6, then the one solar fact, then the specs;
the related grid stays last. Nothing existing changes.

| # | section file | template id | at 390 (cap) | what |
|---|---|---|---|---|
| A | `sections/elmsnest-s-pdp-scene.liquid` | `ens_pdp_scene` | ≤ 640 px with a photograph (440 photo + ≤ 200 text), ≤ 220 px without | one page-wide night photograph of THIS product in place (map), then on the night ground: the place heading, one family line, the guide link |
| B | `sections/elmsnest-s-pdp-dusk.liquid` | `ens_pdp_dusk` | ≤ 160 px | «כשמחשיך» — a hairline row with two sentences; solar products only, prints nothing on mains / USB / battery |

Page estimate at 390×844 (JS on): path 3498 + ≈ 620 + ≈ 120 = 4238 px ≈ **5.0 screens** (P5 cap 6); wall (mains,
photo, no dusk row) 3485 + 620 ≈ 4.9; floodlight (solar, no photo) 3500 + 220 + 120 ≈ 4.5; rope 3318 + 740 ≈ 4.8;
deck (solar, no photo) ≈ 4.5. At 1366: + 560 + ≈ 200 + ≈ 110.

### A — `elmsnest-s-pdp-scene` («ElmsNest S — בלילה»)

**Photograph.** In flow, edge to edge at every width (the home band's skeleton, `elmsnest-s-home-band.liquid`):
`<figure>` with the `<img>` `display:block; inline-size:100%; block-size:440px; object-fit:cover;
object-position:var(--ens-op,50% 50%)` at 390, `block-size:560px; object-position:var(--ens-op-lg,50% 50%)` at ≥ 901.
No scrim, no text on it, no border, radius 0, `loading="lazy" decoding="async"`, `width`/`height` from the real file,
`srcset` 600/900/1254 (never a candidate wider than the source — home2 critique E7), `sizes="100vw"`, `alt=""`
unless the map or block sets one.

**Which photograph — the rule (no product data changes):**
1. **Owner block first.** Section blocks of type `frame`: `product` (product picker), `image` (image_picker),
   `object_position` (text, default «50% 50%»), `object_position_desktop` (text, default «50% 50%»), `heading`
   (text, optional override of the place heading), `alt` (text, optional). The first block whose
   `block.settings.product.handle == product.handle` wins. Blocks are empty by default (the map below is the
   default rendering); the owner adds one to replace a frame for one product without touching code.
2. **The per-product map** (a `case product.handle` in the section; §3 lists the assets): a product with a clean
   frame of its own renders it. Twelve products have one today; four more are pre-crop candidates the lead
   confirms by eye at asset time (§3). The map carries the crops (`--ens-op`, `--ens-op-lg`) per frame and, for the
   indoor birch branches, the heading override «בערב, בבית».
3. **No frame** (the other products): **no photograph.** The section still renders its text block on the night
   ground (heading, family line, guide link) — the honest state, ≤ 220 px. Never another product's frame by default.
4. **Owner option `scene_fallback`** (checkbox, default **false**): when on, a product with no frame shows its
   collection's scene (`image_path` / `image_wall` / `image_spot` / `image_decor` pickers with the §3 scene assets
   as the empty-picker default) and a muted 13 px line under the photograph «{credit_prefix} {pictured product's
   title}» linked to that product (`credit_prefix` text setting, default «בתמונה:»; `pictured_path` / `_wall` /
   `_spot` / `_decor` product settings, defaults = the products in §3). The line is skipped when the pictured
   product IS the page's product. The whole state is off until the owner turns it on — the report says why.
5. **No collection match** (a product only in `sale`): the place word is blank → the section prints nothing.

**Text block** (inside `.env2-wrap`, on the night ground, `padding-block: 24px 28px` at 390):
- `<h2 class="env2-h ens-pdp-scene__h2">` — the place heading by `elmsnest-s-place … emit:'word'`: שביל → «בלילה, על
  השביל» · קיר → «בלילה, על הקיר» · גינה → «בלילה, בגינה» · מרפסת → «בלילה, במרפסת» (four text settings
  `heading_path/_wall/_spot/_decor`; the map/block override wins). Same scale as the related grid's heading
  (`clamp(25px,3.4vw,44px)`), no terminal period.
- one family line `<p class="ens-pdp-scene__line">`, Heebo 300, 16 px / 17 px at ≥ 901, ink, `max-inline-size:46ch`
  (four text settings `line_path/_wall/_spot/_decor`, defaults §2).
- the guide link `<a class="ens-pdp-scene__link">` «למדריך לבחירת תאורה ←» → `/pages/guide-garden-lighting`
  (`link_label` text, `link_url` url setting WITHOUT a default in the schema — Shopify rejects page-path defaults;
  the template entry sets `"link_url": "shopify://pages/guide-garden-lighting"`; empty label = no link). Same form
  as the page's «לכל התנאים ←» (`elmsnest-s-pdp-terms-line`: 44 px hit area via `::before`, hairline underline,
  glow on hover/focus, arrow in an `aria-hidden` span). ONE guide link per page: the PDP body has none today.
- At ≥ 901 the text block is two columns like the facts grid: heading in the inline-start column (right in RTL),
  line + link in the inline-end column, `align-items:start`, gap 48px 64px (the «one» desktop shot is the reference).

### B — `elmsnest-s-pdp-dusk` («ElmsNest S — כשמחשיך»)

Renders only when the product passes the **solar gate** copied verbatim from `snippets/elmsnest-s-place.liquid`
(`product.metafields.custom.power_source == 'סולארי'`; when that metafield is unwritten, `product.description |
strip_html` + `product.title` contain «סולארי»). 16 of 27 products pass (`images/INVENTORY.md` summary); the five
mains wall lights, the rechargeable spot, the mains bollard, the dual-head, the camping lantern, the USB globe
string, the 220V net and the battery birch branches get nothing — no substitute line (the facts print the
connection the bullets state).

Markup: `<section class="env2-section ens-pdp-dusk">` → `.env2-wrap` → a hairline row (`border-block-start:1px
solid #1f1e1d`, `padding-block:20px 22px`, the facts' `<dl>` rhythm): `<h2 class="ens-pdp-dusk__h">` «כשמחשיך»
(Frank Ruhl Libre 700, 20 px / 22 px, ink, no period) and `<p class="ens-pdp-dusk__p">` with the two sentences
(Heebo 300, 16 px, ink-2 `#c9c4b8`, `max-inline-size:52ch`): «ביום הפאנל אוסף שמש, וזה מה שמאיר בלילה.» «יותר שמש
ביום, יותר אור בלילה.» (settings `heading`, `line_1`, `line_2`). At ≥ 901: `grid-template-columns: 128px
minmax(0,1fr)` like a facts row (heading in the label column). No image, no link, no button. ≤ 160 px at 390.

## 2. Copy — every Hebrew sentence, verbatim (guillemets are notation)

| where | text | gate | source / why it is claim-free |
|---|---|---|---|
| A heading, path | «בלילה, על השביל» | collection שביל | the licensed place word; true with or without a photograph |
| A heading, wall | «בלילה, על הקיר» | collection קיר | idem |
| A heading, spot | «בלילה, בגינה» | collection גינה | idem |
| A heading, decor | «בלילה, במרפסת» | collection מרפסת | idem |
| A heading override | «בערב, בבית» | map: `lighted-birch-branches-20-led` (indoor) | the listing's «לעיצוב הבית» |
| A line, path | «אור נמוך, קרוב לאדמה, שמלווה את הדרך.» | שביל | what a bollard's light is by its form; no reach, no hours, no lumens |
| A line, wall | «אור על הקיר, בדיוק בנקודה שבחרתם.» | קיר | a wall light lights the wall it is mounted on; the shopper judges' clearest line |
| A line, spot | «אור מכוון אל מה שרוצים לראות.» | גינה | true of a spot, a floodlight and a security light alike (a beam or a flood is aimed) — the honesty judge's correction of «אלומה אחת ממוקדת»; the critique cut its «בלילה» (four in 290 px on the text-only pages: the heading already says when) |
| A heading override | «בלילה, בשטח» | map: `rechargeable-telescopic-camping-lantern` (spot family, no clean frame) | the listing's own word («בשטח»); it never mentions a garden (critique H3) |
| A line, decor | «הרבה נקודות אור קטנות במקום מנורה אחת. אור שיושבים בו.» | מרפסת | the nature of a string; no strength claim except by contrast |
| A link | «למדריך לבחירת תאורה ←» | all | the licensed ל־ infinitive form (P4); the PDP's first and only guide link |
| A credit (option) | «בתמונה: {title}» | `scene_fallback` on, pictured ≠ page product | the pictured product's own title, verbatim, linked |
| B heading | «כשמחשיך» | solar | the moment, not a promise |
| B line 1 | «ביום הפאנל אוסף שמש, וזה מה שמאיר בלילה.» | solar | how every solar light works; says nothing about switching on by itself (the floodlight has a remote and a timer, the security light a sensor) |
| B line 2 | «יותר שמש ביום, יותר אור בלילה.» | solar | the sun dependency as a general fact — no number, no hours; the positive of the not-for line without its words |

Rules: no «+», no «;», sentences keep their period, headings have none; digits/Latin inside Hebrew in `<bdi
dir="ltr">` (none in the defaults; the credit title may carry «180°», «10W IP65» — the credit renders the title
through the same token loop `elmsnest-s-pdp-facts` uses). `alt` empty by default (decorative; the heading carries
the meaning) — a setting per block. Not said: «ככה זה נראה» (a lie on a fallback), «נדלק לבד», «בלי כבל» (false on the
floodlight's cabled panel), hours, lumens, IP, «חזק», the winter line, «לא מתאים», the kicker's infinitive.

## 3. Images — theme assets on the DEV theme (`assets/ens-pdp-*.jpg`, ≤ 220 KB, progressive JPEG, store-owned)

Per-product map (gallery position ≠ 1 everywhere; the frame is the page's own product):

| handle | asset | source frame · crop (x,y,w,h in the 1254² source) | crops `--ens-op` / `--ens-op-lg` |
|---|---|---|---|
| `stainless-steel-solar-path-light-ip65` | `ens-pdp-stainless.jpg` | `_6` steps · none; 1100×1100 q70 (pass 2: the 1254 file was 304 KB and its 900w CDN derivative 281 KB) | 50% 55% / 50% 45% |
| `powerful-solar-garden-light` | `ens-pdp-powerful.jpg` | `_4` lit bollards, patterns · pre-crop 0,90,1254,1040 (the «מתאים לגינה» caption sat below y 1150 and a person's legs at the top-right edge above y 90 — pass 2) | 50% 50% / 50% 40% |
| `solar-rope-string-lights` | `ens-pdp-rope.jpg` | `_3` rope on the trunk, lantern, panel · pre-crop 0,380,1254,874 (the IP65 badge spans y ≈ 185–355; the first crop at y 210 left it in the file — the critique's blocker, pass 2) | 50% 50% / 50% 50% |
| `solar-crystal-ball-string-lights` | `ens-pdp-crystal.jpg` | `_3` trellis · none (`_5` is the home band) | 50% 50% / 50% 50% |
| `solar-edison-string-lights` | `ens-pdp-edison.jpg` | `_4` patio table, panel · none | 50% 50% / 50% 30% (pass 2: the first bulb kept its socket at 1366) |
| `solar-firefly-garden-lights` | `ens-pdp-firefly.jpg` | `_4` ferns · none | 50% 50% / 50% 50% |
| `lighted-birch-branches-20-led` | `ens-pdp-birch.jpg` | `_4` hallway, two vases · none (indoor; heading «בערב, בבית») | 50% 50% / 50% 55% |
| `outdoor-bidirectional-led-wall-light-ip65` | `ens-pdp-bidirectional.jpg` | `_6` slate wall · none | 50% 50% / 50% 45% |
| `waterproof-led-wall-light-ip65-6w-12w` | `ens-pdp-waterproof-wall.jpg` | `_6` dusk terrace, pillar · none | 62% 50% / 50% 34% (scene's measured crops) |
| `modern-led-wall-light-indoor-outdoor` | `ens-pdp-wall-indoor-outdoor.jpg` | `_5` six-beam sconce on the grey wall · none (a studio wall, but the product itself) | 50% 50% / 50% 50% |
| `modern-led-wall-light-6w-up-down` | `ens-pdp-wall-6w.jpg` | `_7` black cube on the dark wall · none (1000 px source — the 900 candidate is the largest; softness noted for the owner) | 50% 50% / 50% 50% |
| `dual-head-garden-light-10w-ip65` | `ens-pdp-dual-head.jpg` | `_5` bollard aiming into the planting · pre-crop 0,0,930,1254 (the LUMIÈRE sign is at x > 935 — the whole panel stays out of the file; 930 px wide, the short side, renders at 390 without upscaling and at 1366 like every other 1254 source, ×1.1–1.5) | 50% 50% / 50% 45% |
| `modern-solar-path-lights-set` | `ens-pdp-modern-path.jpg` | `_3` dusk path, three curved bollards, the house · pre-crop 0,380,1254,660 (the headline and subtitle above, the icon strip below; confirmed by eye) | 50% 60% / 50% 55% |
| `solar-garden-lantern-9-led` | `ens-pdp-lantern9.jpg` | `_6` the spot in the rain lighting the wet shrub · pre-crop 0,300,1254,680 (headline above, weather icons below; confirmed) | 0% 50% / 50% 50% (pass 2: the spot and its panel whole at 390/360) |
| `warm-solar-step-deck-lights` | `ens-pdp-warm-step.jpg` | `_2` the lit stairs · pre-crop 400,345,854,909 (the gold headline and the icon column are on the left; a stroke of the headline sat on the top edge at y 330 — pass 2) | 50% 50% / 50% 50% |
| ~~candidates~~ | `swaying-solar-path-lights-ip65_4` rejected (the «נטען ביום • מאיר בלילה» pill sits exactly where the far lamp heads are — no band is both clean and whole); `retro-solar-path-lights-set_6` rejected (four labelled quadrants) | a band ≥ 600 px tall from the full 1254 width is enough for a 440/560 px band (no vertical upscaling); rejected if any glyph, badge or icon survives |

Fifteen products carry their own frame. No frame (text-only A by default), twelve: `magnetic-rechargeable-touch-wall-light`,
`solar-wall-light-motion-sensor-ip65`, `waterproof-solar-deck-step-lights`, `retro-solar-path-lights-set`,
`swaying-solar-path-lights-ip65`, `modern-led-bollard-light-5w-ip65`, `solar-garden-spotlight-52-led`,
`solar-security-light-100-led`, `solar-floodlight-ip67-remote-timer`, `rechargeable-telescopic-camping-lantern`,
`led-globe-string-lights`, `decorative-led-net-lights`. These are the owner's open item #3 (clean frames): the
moment he uploads one, a `frame` block puts it on the page.

Collection scenes (the `scene_fallback` option, off by default; each shows a sibling product, hence the credit):

| collection | asset | source frame | pictured product (credit) |
|---|---|---|---|
| path | `ens-pdp-scene-path.jpg` (1100×1100 q70, pass 2) | `stainless-steel-solar-path-light-ip65_1` (hedge, wet pavers — not `_6`, so the stainless page and a fallback page never show the same frame) | `stainless-steel-solar-path-light-ip65` |
| wall | `ens-pdp-scene-wall.jpg` | `outdoor-bidirectional-led-wall-light-ip6_1` (dusk patio, cylinder — not `_6`) | `outdoor-bidirectional-led-wall-light-ip65` |
| spot | `ens-pdp-dual-head.jpg` (the same file as the dual-head's own) | `dual-head-garden-light-10w-ip65_5` pre-crop | `dual-head-garden-light-10w-ip65` |
| decor | `ens-pdp-scene-decor.jpg` | `solar-edison-string-lights_5` (pergola, lantern — not `_4`) | `solar-edison-string-lights` |

Prepared by `images/prepare-assets.py` (`<id>=<slug>[:x,y,w,h]`, ≤ 1800 px, JPEG ≤ 220 KB), ledger in
`images/CHOSEN.md`; uploaded with `themeFilesUpsert` `body: {type: URL}` from the public raw GitHub URL of the
committed file (as in `../home2/DEPLOY-LOG.md`), checksums compared. Nothing goes into the Files library.
Rendered with `asset_img_url` 600/900/1254 (900 only for the 1000 px source; a pre-cropped file's candidates stop at
its own width). ≤ 1 photograph per PDP.

## 4. File rules

- Both sections: `{% schema %}` in Hebrew, `"tag": "section"`, `"class": "ens-pdp-section hdt-section"`,
  `"enabled_on": {"templates": ["product"]}`, a `presets` entry, `"name"` ≤ 25 chars with the «ElmsNest S — »
  prefix. Section root `<section class="env2-section ens-pdp-scene" dir="rtl">` / `ens-pdp-dusk`; `<style>` inside
  the section (like `elmsnest-s-fit`); logical properties only; radius 0; no JS; a reduced-motion rule; every
  digit/Latin token inside Hebrew in `<bdi dir="ltr">`; no `text` setting with an empty default (omit the default);
  no `url` setting with a page-path default; no `"""`. A `frame` block type in A's schema with the settings of §1.2.
  Focus-visible outline `2px solid #ffd394` on the link.
- `templates/product.elmsnest.json`: two new entries after `main-product` — `"ens_pdp_scene": {"type":
  "elmsnest-s-pdp-scene", "settings": {"link_url": "shopify://pages/guide-garden-lighting"}}` (every other default
  lives in the schema; `blocks` omitted) and `"ens_pdp_dusk": {"type": "elmsnest-s-pdp-dusk", "settings": {}}` — and
  the new order. Keep the /* */ header; nothing else in the file changes.
- No edit to `elmsnest-s-place`, the skin, core, `elmsnest-s-pdp-facts`, `elmsnest-s-products` or any Kalles file.
  Lint clean (`python3 brief/lint.py theme`).

## 5. Acceptance (`simplify/verify-mirror.js` on the re-mirrored PDPs, 390×844 / 360×640 / 1366×900, JS on and off)

- PDP ≤ 6 screens at 390×844 on `pdp-path`, `pdp-rope`, `pdp-deck`, `pdp-wall`, `pdp-flood`; A ≤ 640 px at 390 with
  a photograph, ≤ 220 without; B ≤ 160.
- The gate: B present on path, rope, deck, flood (solar); **absent on wall** (mains). A's photograph present on path
  (stainless), rope, wall; absent on deck and flood (no map entry) unless a candidate is confirmed; the credit line
  absent on every page (option off).
- Every §11 PDP check unchanged: `form.hdt-main-product-form` 1, sticky form 1, terms line 1, «תמונה של המקום» in
  main 1, `mailto` in main 1, 0 WhatsApp, 0 glyph plates, 0 Liquid errors, no overflow-x, en-dash ranges in bdi;
  `main a[href*="guide-garden-lighting"]` = 1.
- Copy on the page byte-identical to §2 per family (grep the mirror). No new count, rank, claim, no spec repeated.
- Images: `img` in `.ens-pdp-scene` = 1 or 0 by the map, with width/height, `loading="lazy"`, `decoding="async"`,
  candidates ≤ the source width; the asset served from the theme (request log).
- Shots at 390 and 1366 of A and B on path, wall, flood (`pdp2/shoot-sections.js --sections=ens-pdp-scene,ens-pdp-dusk`),
  the heading legible on the night ground (no text over the photograph — no contrast probe needed beyond the
  ground's known ≥ 12:1).
