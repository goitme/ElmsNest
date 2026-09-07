# Product page, round 3 — two or three more image sections, a different look, internet photographs (2026-09-07)

## 0. The owner's request (verbatim, Arabic)

«اريد ان تضيف محتوى اكثر في صفحة المنتج و يعني كمان صورتان او ثلاث مع ابتكار ليس بنفس الون
و بعدها اذهب الى صفحات المتحوى و ايضا ضيف صور هناك
الصور اريد منك ان تبحث و تجيبها من الانترنت نت عادي»

Three things, in order: (1) **more content on the product page — two or three more sections with images, creative,
«not the same look»** (`ليس بنفس اللون` — not the same colour/tone/device as what is there); (2) **then the content pages,
with images too** (a separate brief, `../pages/BRIEF.md`, after this round is deployed); (3) **the images may come from the
internet** — search and bring them. The owner's standing verdict (SIMPLIFY §0) still binds where it does not conflict with
this request: simple to shop, nothing twice, the night identity of the store, honest.

## 1. What the product page is today (round 2, pass 3, deployed 2026-09-07)

`main-product` (gallery + buy box, the terms line, the not-for line + contact) → `ens_pdp_scene` (**one night photograph of
THIS product** from its own gallery, 440/560 px, then the place heading, one family line, the guide link; text-only on
12 of 27 products) → `ens_pdp_dusk` («כשמחשיך», solar only) → `ens_pdp_facts` (IP numeral + `<dl>` + description) →
`ens_related` (four cards) → footer. Measured at 390×844: rope 4.85 · path 5.03 · deck 4.41 · wall 4.84 · flood 4.49
screens. Files: `theme/sections/elmsnest-s-pdp-{scene,dusk,facts}.liquid`, `theme/templates/product.elmsnest.json`;
shots `../pdp2/verify-after/pdp-{path,rope,deck,wall,flood}-{m,d}-js-full.png`; the round-2 record `../pdp2/SPEC.md`.

What the page already says once (SIMPLIFY §3 + round 2): where am I (kicker), price, suits/not-for, choose, buy, per-unit,
**how it looks at night in its place (scene)**, **what happens at dusk / the sun dependency (dusk row)**, specs (facts),
terms, contact, related. The new sections must not say any of these again.

## 2. What «a different look» means for this round (the lead's reading — stated, not asked)

The two round-2 sections are one device: a dark night photograph, edge to edge, words under it on the night ground, and a
hairline row. «Not the same colour» is read as: **different devices and different tonalities**, still inside the store's
identity — for example a **daylight** or **golden-hour** photograph (the panel in the sun, a Mediterranean garden at noon,
dusk with a warm sky), **detail** photographs (a solar cell surface, rain on a lamp head, a stake in soil, hands installing),
**framed** images instead of full-bleed (a photograph inside the wrap with a caption, a two-up or three-up of small
photographs, a photograph beside text), **warm amber or cream tones** on a photograph rather than the blue-black night —
and typography that sits on the photograph only where the crop is dark enough (≥ 4.5:1, measured). The night ground of the
page stays; the sections bring light into it. No device already on the page (no second full-bleed night band with a
sentence, no second hairline row under a photograph).

## 3. What the sections may be about (seeds; concepts may combine or reject)

1. **«איך זה עובד»** — the solar mechanism in three images: the cell in daylight (a real solar cell / panel close-up in the
   sun), the light at dusk, the light at night — as a framed triptych with one word each. Gated to solar products; on
   mains/USB products the section shows a different triptych or nothing (design it).
2. **«התקנה»** — what installing looks like: a stake pushed into soil, a wall bracket and two screws, a string hung on a hook
   — real photographs of hands and tools (faces never), one line each, by family (path: stake; wall: bracket; decor: hook;
   spot: stake or bracket). Facts the listings state («נעיצה באדמה», «ברגים») only.
3. **«מזג אוויר»** — rain on a lamp, sun on a panel, dust — detail photographs with one honest line each (the IP code
   stays in the facts; here only the general: outdoor lights live outside). Careful: no claim the product cannot back.
4. **«מקומות»** — a warm-tone dusk photograph of a real garden, balcony or path (a licensed internet photograph), framed
   inside the wrap with a caption naming what it is («גינה בשעת בין ערביים») — atmosphere, explicitly not the product.
5. **«לפני שקונים»** — the guide's three checks with three small photographs (sun on the spot · distance · indoors/out) —
   rejected by the round-2 judges as a checklist under the price; may return only as an image-led, non-question form.
6. **A day/dusk pair of one real place** (a licensed photograph pair or a single photograph at golden hour).

## 4. Constraints that bind every concept

- **Images from the internet: licence and honesty.** Sources: Openverse and Wikimedia Commons, commercial-safe licences
  only (CC0, public domain, CC BY, CC BY-SA); every photograph's author, licence and source page recorded in
  `images/manifest.jsonl`; CC BY / BY-SA photographs carry a credit («צילום: Name (CC BY 2.0)») as an 11–12 px muted
  caption inside the section — never omitted; CC0/PDM need none. No faces (a person from behind or hands are fine),
  no foreign brand marks, no baked-in text, no watermark, ≥ 1200 px on the long side (a detail crop from a larger
  photograph is fine), no heavy colour filters. **On a product page an internet photograph is never presented as the
  product**: a caption or heading names what it is (a place, a mechanism, a material); no photograph of another brand's
  lamp sits under a heading that could read as this product. The store's own frames remain available (`../pdp2/images/
  INVENTORY.md`), but the round-2 sections already use the clean ones — new sections should bring new images.
  Generated imagery only as a last resort, labelled as generated in the report.
- **Copy:** Hebrew, short, claim-free (BRIEF §3 honesty: no hours, lumens, IP, «best», reviews, counts, urgency); general
  facts about sun, weather, installation as the listings state them; every new sentence listed for the owner. No «+», no
  «;», no terminal period on labels. Digits/Latin in `<bdi dir="ltr">`.
- **Length:** the P5 cap for the product page rises for this round from 6 to **7.5 screens at 390×844** (the home went
  6 → 7.5 in its image round); each new section ≤ 520 px at 390; all new sections together ≤ 1500 px. Nothing between the
  gallery and the button; the new sections sit after `ens_pdp_dusk` and before or after `ens_pdp_facts`, never after
  `ens_related`. ≤ 3 new photographs per page, lazy, sized, ≤ 220 KB each, `asset_img_url` candidates ≤ the file.
- **Per-product behaviour by rule, no product data:** family by `elmsnest-s-place emit:'word'`, the solar gate as in
  `elmsnest-s-pdp-dusk`, image slots as settings (image_picker with a theme asset as the empty default), optional
  per-family variants. Stock patterns only (P1): no carousel, no parallax, no reveal; radius 0; logical properties; no JS.
- **Files:** `sections/elmsnest-s-pdp-<name>.liquid` with a Hebrew `{% schema %}`, `enabled_on: templates: ["product"]`;
  the template edit = `templates/product.elmsnest.json` only. Nothing published to the live theme; no product, collection,
  page or metafield changed; no Kalles, core or skin file edited.

## 5. Deliverable of a concept

`concepts/<name>/index.html` — the 2–3 new sections rendered for the three round-2 archetypes (A stainless path light:
solar, photo; B waterproof wall light: mains; C solar floodlight: text-only scene), each inside its current page context
(grey bands of true heights at 390: main-product 1085 / scene 596 / dusk 152 / facts 723 / related 781 for A; for B scene
596, no dusk; for C scene 135, dusk 135), with the real photographs referenced from `../../images/candidates/…` and the
credits drawn; `shots/` (`<A|B|C>-m-fold.png` 390×844 with the first new section at the top, `<A|B|C>-m-full.png`,
`<A|B|C>-d-fold.png` 1366×900, `<A|B|C>-d-full.png`); `COPY.md`, `IMAGES.md` (id, author, licence, credit line, crop, why,
and the sentence that says what it is), `NOTES.md` (the device and why it is a different look, the order in the template,
the measured heights at 390 per archetype, the gate per family, the honest «is any of this twice?»).

## 6. Judging

Five judges from the shots: the owner (simple, nothing twice, my store's night identity, «creative, a different look», the
photographs are not pretending to be my products), a first-time phone shopper about to decide (help or delay?), the honesty
guardian (licence + credit on every internet photograph, no baked text, no claim, nothing implying the product), a designer
(is the new look one clear idea, how the daylight/warm images sit on the night page, crops, type on photographs measured),
an engineer (feasibility, gate logic, weight, heights, ≤ 3 photographs per page). Shopper and owner ×1.5.
