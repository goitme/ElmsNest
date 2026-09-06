# Product page, round 2 — two or three image-led sections on a SALES page (2026-09-06)

## 0. The owner's request (verbatim, Arabic)

«بعدها ابداء في صفحة المنتج بنفس الطلب لكن زبطها اكثر لانه صفحة منتج صفحة بيع»

The same request as the home round (`../home2/BRIEF.md` §0: 2–3 more sections, not more; the point is images that
fit the niche, set creatively and beautifully), applied to the product page — and **tuned harder, because a
product page is a sales page.** His standing verdict (SIMPLIFY §0) binds: simple to shop, nothing twice, the night
look, the store's own product photos where a product is shown, email not WhatsApp.

## 1. What the product page is today (SIMPLIFY §8, deployed on the dev theme, measured 2026-09-06)

`templates/product.elmsnest.json` (every product carries `templateSuffix: elmsnest`):
`main-product` (Kalles gallery — one frame at a time on the phone with a «1/6» fraction, thumbnails on the left at
1366 — then kicker «{collection} · מתאים כדי {yes}», h1, price, per-unit caption, variant pills, quantity, the
button «הוסיפו להזמנה», the ONE terms line, the not-for line + contact line) → `ens_pdp_facts` (the outlined IP
numeral + a hairline `<dl>` from the listing's bullets + the description behind `<details>`) → `ens_related`
(«עוד לאותו מקום», four stock cards) → footer. Sticky buy bar on the phone (78 px reserved at the bottom).

Measured at 390×844 (JS on): rope 3.93 · path 4.14 · deck 4.07 screens (target ≤ 6, P5). Section heights at 390:
main-product 1085–1266 · facts 362–723 · related 781 · footer ≈ 850. At 1366×900: 2.6 screens. Shots:
`../simplify/verify-after/pdp-{path,rope,deck}-{m,d}-js-full.png`; mirrors (real HTML + assets) in
`../simplify/verify-after/mirrors/pdp-{path,rope,deck}/`.

Every buyer question is answered exactly once on this page (SIMPLIFY §3): where am I (kicker) · which product, price
(h1, price) · does it suit / when not (kicker «מתאים כדי…», not-for line) · choose (pills) · buy (form + sticky) ·
per unit (caption) · specs (facts) · terms (one line) · not sure (contact line) · where next (related). **The new
sections must not answer any of these again**: no second price, no second button, no second terms, no second
contact line, no second «לא מתאים», no product grid, no place list. What they may do is what the gallery and
the facts cannot: show the product — or its kind of light — *in a place, at night, page-wide*, and say the one or
two honest things a buyer wants to hear before pressing the button.

## 2. Why «sales page» changes the brief (the tuning)

1. **Nothing between the gallery and the button.** The first new section sits AFTER `main-product`. Candidates
   for the order: `main-product → A → ens_pdp_facts → B → ens_related` or `main-product → A → B →
   ens_pdp_facts → ens_related` or `… → ens_pdp_facts → A → B → ens_related`. A concept must say which and why
   (desire before detail? detail before doubt?). `ens_related` stays last in the body.
2. **Length is a hard cap:** PDP ≤ 6 screens at 390×844 (P5). The path PDP is 3498 px today → **≤ 1500 px of new
   sections in total at 390, each ≤ 520 px** (measured with the real fonts). Fewer, better sections beat three.
3. **Every section earns its place by helping the decision**, in this order of value: (a) *see it in place, at
   night* — the desire the carousel hides behind a swipe; (b) *what happens at dusk / how it charges* — the one
   fact a first-time solar buyer needs, gated to solar products; (c) *before you order* — the honest checks that
   prevent a return (sun at the spot, distance, winter), which is also the brand's voice. A section that is only
   decoration is cut by the judges.
4. **Per-product, without touching products.** No metafield, tag, product or collection may change. The sections
   therefore adapt by rule, in Liquid: the product's collection through `snippets/elmsnest-s-place.liquid`
   (`emit: 'collection'` / `'word'`), the solar gate copied from the same snippet (metafield
   `custom.power_source == 'סולארי'`, else title + description contain «סולארי»; 16 of 27 products are solar,
   see `images/INVENTORY.md`), and — for the photograph — either a **per-product map** (section blocks: a
   `product` setting + an `image_picker`, matched on `product.handle`, so the owner can add or swap a frame per
   product in the theme editor) or a **per-collection default** (four theme assets), or both (map first, collection
   fallback). A product with no clean frame (10 of 27) must still render a beautiful section: design the fallback.
5. **The sticky buy bar** covers the bottom 78 px of the phone viewport; nothing a section needs read may live
   only in the last 78 px of the page, and no section may add a button that competes with it.
6. **Weight:** a PDP loads ≤ 3 new photographs, all `loading="lazy"`, `decoding="async"`, width/height set,
   `asset_img_url` sizes ≤ the rendered width (no 1200w candidate where 900 is enough — the CDN re-encode is
   heavier than the original, home2 critique E7).

## 3. Constraints that bind every concept (unchanged from the home round, plus PDP specifics)

- P1–P7 of `../simplify/SPEC.md` §2. Night ground, gold, Frank Ruhl Libre + Heebo, radius 0 except pills,
  logical properties, `<bdi dir="ltr">` around digits/Latin inside Hebrew (P6), stock patterns only (no carousel,
  no scroll-lamps, no parallax, no hover reveal), reduced-motion respected.
- **Honesty (`../../BRIEF.md` §3):** no reviews, ratings, counts, ranks, urgency, «best», no product claims the
  store cannot back (no hours of light, no lumens, no «IP65» unless the product's own bullets say it — the facts
  section already prints those; do not print them twice). A general fact about the sun or the category is not a
  product claim («ביום נטען, בלילה נדלק», «בחורף השמש קצרה יותר»). Every new Hebrew sentence is new copy the owner
  has not seen: short, plain, claim-free, listed in COPY.md for his approval. No «+», no «;», no terminal period on
  labels/headings; a sentence keeps its period. Guillemets are notation.
- **Images — the PDP rule is stricter than the home's.** A photograph on a product page is read as *this
  product*. So: (1) the store's own frames only (`images/INVENTORY.md`: per product, which frames are clean, which
  need a baked pre-crop, which are unusable — baked claims, infographics, faces, foreign brand marks LUMIÈRE /
  LUMORA / KINFOLK…); the CC candidates of the home round are NOT available here (somebody else's lamps on a
  product page is a lie). (2) When the photograph shows the page's own product, nothing needs saying. (3) When it
  shows ANOTHER store product (a collection scene on a product that has no clean frame), the section must say
  so in a muted 12–13 px line — «בתמונה: {that product's title}», linked to it — or must not use it. Never imply.
  (4) No frame with baked text, badges, icons or a brand sign, unless the asset is pre-cropped so the text is
  outside the file (like `ens-home-night.jpg`); a pre-crop must leave ≥ 1000 px on the short side. (5) The
  featured frames (`../simplify/featured.json`) are marketing creatives with baked Hebrew on most products —
  never reuse them. (6) A frame that is already the page's gallery image 1 (what the phone shows) is not used
  again; a later gallery frame may be (the phone shopper never swiped to it) — say so in NOTES.md and let the
  judges weigh «twice». Assets land on the DEV theme as `assets/ens-pdp-<slug>.jpg` (≤ 220 KB, ≤ 1800 px, JPEG,
  progressive) via `themeFilesUpsert` (URL body from the public raw GitHub URL, as in `../home2/DEPLOY-LOG.md`),
  rendered with `asset_img_url` sizes; the owner can override any of them with an `image_picker`. Nothing goes
  into the Files library.
- **Copy for four families, one voice.** The place vocabulary is licensed (`elmsnest-s-place`): שביל «לראות את
  הדרך» · קיר «להאיר נקודה מסוימת» · גינה «להאיר עץ או ערוגה» · מרפסת «ליצור אווירה». The kicker already prints
  «מתאים כדי {yes}» — do not print it again. New family lines must be about the *light* (what it does in that
  place at night), never a spec. The wall collection holds five MAINS lights and one rechargeable (not solar):
  a solar sentence on them is a lie — gate it.
- **Files:** `sections/elmsnest-s-pdp-<name>.liquid` with `{% schema %}` in Hebrew (a setting for every text and
  image, `enabled_on: {templates: ["product"]}`), `class: "ens-pdp-section hdt-section"`; template edit =
  `templates/product.elmsnest.json` only (`order` + new entries). Nothing published to the live theme; no
  Kalles file, no core, no skin edited. Lint clean (`brief/lint.py theme`).

## 4. Idea seeds (the concept agents may take, combine or reject these)

1. **«ככה זה נראה בלילה»** — one page-wide night photograph of this product in place (own frame when the map
   has one, the collection scene otherwise, honestly captioned) with one sentence. The desire picture the
   carousel hides. Watch: the gallery's frame 1 is already a picture; this one must be *in place, at night, wide*.
2. **«כשמחשיך»** — the moment the light comes on: a small day/night pair (panel in the sun · the same light at
   night) with one line, solar products only; on mains/USB products it collapses to nothing or to one line about
   the connection the listing states («מתחבר לחשמל» only where the bullets say 220V). The home already has the
   big diptych — the PDP version must be smaller and differently framed (a detail, not a landscape), or the
   judges will call it twice.
3. **«לפני שמזמינים»** — three checks before ordering: how much sun reaches the spot · how far the light must
   reach · winter means less charge (solar) — each with a small photograph, then «למדריך לבחירת תאורה ←» to
   `/pages/guide-garden-lighting` (the PDP has no guide link today). The not-for line already says «לא מתאים
   כש…» — this section must not repeat that sentence; it asks, it does not warn.
4. **«אותו אור, מקומות אחרים»** — three frames of the same family in three places (steps · hedge · entrance for
   a path light; patio · slate wall · terrace for a wall light; fence · table · ferns for decor), one word each.
   Honest only where the frames show the same product or are captioned; the spot family has one clean frame.
5. **The winter note** on solar products, right where it matters (before the order): «בחורף השמש קצרה יותר…».
   The home says it too; on the PDP it is the honesty at the point of sale — a judge may still call it twice.
6. **Scale / size / what's in the box** — no clean images exist; probably no.

## 5. Deliverable of a concept

A folder `concepts/<name>/` with `index.html` — a self-contained mockup (dir="rtl" lang="he", the real fonts from
`brief/assets/fonts` via file:// @font-face, the real frames referenced from `../../../home2/images/own/…`) that
renders the 2–3 new sections **for three archetype products, one after the other, each in its PDP context**
(the existing sections as labelled grey bands of their true heights at 390: main-product 1085 / facts 723 /
related 781 for the path light; 1266 / 362 / 781 for the rope light; the wall light like the path light):

- **A — `stainless-steel-solar-path-light-ip65`** (path, solar, 1 variant, clean own frames 1/2/4/5/6),
- **B — `waterproof-led-wall-light-ip65-6w-12w`** (wall, MAINS, 8 variants, one clean own frame 6 + studio 2/4/5),
- **C — `solar-floodlight-ip67-remote-timer`** (spot, solar, 3 variants, NO clean own frame → the fallback).

Plus `shots/` at 390×844 and 1366×900: `<A|B|C>-m-fold.png` (the first new section at the top of the viewport),
`<A|B|C>-m-full.png`, `<A|B|C>-d-fold.png`, `<A|B|C>-d-full.png`; `COPY.md` (every Hebrew sentence per family,
with the source of any fact and the gate it renders under); `IMAGES.md` (each frame: manifest id, product, crop,
why, and the caption it needs); `NOTES.md` (what the concept is, what it refuses, the order it proposes in the
template and why, the measured height of each section at 390 for A/B/C, the per-product/per-collection rule the
Liquid would follow, and the honest answer to «is any of this twice?»). Judges see the shots, not the code.

## 6. Judging

Five judges from the screenshots: the owner (his verdict, his three complaints, «creative but simple», and now
«it is a sales page»), a first-time shopper on a phone who is about to decide, the honesty guardian (every
sentence, every image against §3 — a photograph implying a product it does not show is a 2), a designer
(craft, rhythm with the buy box and the facts, image treatment on the night ground, 390 and 1366), and an
engineer (feasibility inside P1–P7 with no product data changes, the gate logic, weight, length, the fallback
for the ten products without a clean frame). Shopper and owner ×1.5.
