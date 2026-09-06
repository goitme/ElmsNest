# Home, round 2 — two or three image-led sections (2026-09-06)

## 0. The owner's request (verbatim, Arabic)

«الان لا اريد العمل على السلة اريد العمل على الصفحة الرئيسية اريد منك ان تزيد محتوى لكن لا تزيد كثير زيد يعني 2-3 سكشنز
و اهم شيء ان اتصنع السكشن مع صور يعني ابحث عن صور مناسبة للنيش و قوم بوضعها في السكشن بشكل ابداعي جميل»

So: the cart is parked. The home page gets **2–3 more sections, not more**, with **content**, and the point of the
round is **images**: find images that fit the niche (solar outdoor lighting for Israeli gardens, balconies, paths and
walls) and set them in the sections **creatively and beautifully**. His standing verdict (SIMPLIFY §0) still binds:
simple to shop, nothing twice, the night look, the store's own product photos where a product is shown.

## 1. What the home page is today (SIMPLIFY, deployed on the dev theme, measured 2026-09-05)

hero (photo + two-line sentence + one button) → «איפה צריך אור?» four collection tiles → «מה שנדלק ראשון» four
product cards → «מתי כן, ומתי לא» four place rows with the approved suits / doesn't-suit pairs + guide link +
contact line → «שלושה מספרים שכדאי לדעת» terms strip → footer. **5.12 phone screens** (target was ≤ 6).
Everything in it answers one buyer question once (SIMPLIFY §3). The new sections must not answer any of those
questions again — no fifth place list, no second product grid, no second terms, no second contact line
(§11 counts «תמונה של המקום» in `<main>` = 1 per page and `mailto` = 1).

## 2. Constraints that bind every concept

- P1–P7 of `brief/side-pages/simplify/SPEC.md` §2. Night ground, gold, Frank Ruhl Libre + Heebo, radius 0 except
  pills, logical properties, `<bdi>` isolation of numbers/Latin inside Hebrew (P6).
- **Honesty (BRIEF §3):** no reviews, ratings, counts, ranks, urgency, «best», invented customer photos, no product
  claims the store cannot back (no hours-of-light numbers, no lumen numbers, no «all our lights are IP65»). A
  general fact about the sun is not a product claim («ביום נטען, בלילה נדלק»; «בחורף השמש קצרה יותר»). Every new
  Hebrew sentence is new copy the owner has not seen: keep it short, plain, claim-free, and list every sentence in
  the owner report for his approval. No «+», no «;», no terminal period on labels; a sentence keeps its period.
- **Images:** a photograph in a new section is *atmosphere*, never «our product» unless it IS the store's own product
  image. Allowed sources, in order of preference: (1) the store's own product images (`images/own/`, all 27 products,
  165 frames — some are real lifestyle shots); (2) commercial-safe Creative Commons photographs from Openverse /
  Wikimedia Commons (`images/candidates/`, manifest with license + author — CC0 / PDM need nothing; CC BY / BY-SA
  need one credit line, which goes in the section as a 11 px muted caption «צילום: Name (CC BY)» or in the footer);
  (3) generated imagery only as a last resort, capped, and labelled as generated in the owner report. No faces, no
  foreign brand marks or baked-in text, no daylight-only garden shots unless the concept is a day/night pair.
  Every image lands on the DEV theme as a theme asset (`assets/ens-home-*.jpg`, ≤ 220 KB, ≤ 1800 px wide, JPEG q78
  or WebP) via `themeFilesUpsert` BASE64 — proven on 2026-09-06 — and is rendered with `asset_img_url` sizes.
  Nothing goes into the store's Files library.
- **Length:** each new section ≤ 0.8 phone screen (≤ 675 px at 390×844); the page stays ≤ 7.5 screens with all
  additions (5.12 now). Images are `loading="lazy"` below the hero, with width/height attributes.
- **Stock patterns only** (P1): no carousels, no lamps that light on scroll, no parallax, no hover reveals that hide
  content. A gentle fade or none. Reduced-motion respected.
- Files: new sections are `sections/elmsnest-s-home-*.liquid` with a `{% schema %}` (settings for every text and
  image so the owner can edit them; images as `image_picker` with the theme asset as the *default rendering* when the
  picker is empty — so the section works the moment it is added and still lets him swap photos). Template edit =
  `templates/index.json` only. Nothing published to the live theme.

## 3. Idea seeds (the concept agents may take, combine or reject these)

1. **«ביום נטען. בלילה נדלק.»** — how solar lighting works, in two frames (day / night) and three plain steps:
   the panel charges by day · the light turns on by itself at dusk · no cable, no electrician. A fact about the
   category, not a claim about a product.
2. **«לפני שקונים» (before you buy)** — the three questions the guide asks (how much sun reaches the spot · how far
   must the light reach · indoors or out), each with a photograph, leading to the existing guide page
   `/pages/guide-garden-lighting`. If this section carries the guide link, the fit block's own guide link is
   turned off in the template (one guide link per page).
3. **«ובחורף?»** — the honest note the brand is built on: shorter days mean less charge; the store says so before
   you order. One moody image, three lines.
4. **A night editorial band** — one full-bleed photograph of a lit garden with one short sentence; the page's breath
   between two dense sections. (Watch the hero: it already does this once. Only if it is clearly different.)
5. **«מה מאיר מה»** — what kind of light each family gives (down-light on a path, wash on a wall, a beam on a tree,
   a string over a table) as four small photographs with one line each. Risk: the four collections a third time —
   only if it reads as *light kinds*, not as places.
6. **Materials & weather** — rain, dust, summer sun: only with facts every product shares. Probably no.

## 4. Deliverable of a concept

A folder `concepts/<name>/` with `index.html` (self-contained mockup of the 2–3 sections in place — the real home
page's neighbouring sections sketched as grey bands above/below so the rhythm is judged), `shots/` at 390×844 and
1366×900 (fold and full), `COPY.md` (every Hebrew sentence, with the source of any fact), `IMAGES.md` (each image:
manifest id, why, license/credit), and `NOTES.md` (what the concept is, what it refuses, estimated px per section
at 390). Judges see the shots, not the code.

## 5. Judging

Five judges from the screenshots: the owner (his verdict, his three complaints, «creative but simple»), a first-time
shopper on a phone, the honesty guardian (every sentence and image), a designer (craft, rhythm with the existing
sections, image treatment), and an engineer (feasibility inside P1–P7, weight, length). Shopper and owner ×1.5.
