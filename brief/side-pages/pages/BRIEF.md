# Content pages — the SIMPLIFY look, with photographs (2026-09-07)

## 0. The owner's request (verbatim, Arabic — the second half of the round-3 request)

«و بعدها اذهب الى صفحات المتحوى و ايضا ضيف صور هناك — الصور اريد منك ان تبحث و تجيبها من الانترنت نت عادي»

Then the content pages, with images too; the images may come from the internet. The order the owner set: after the
product page's third round is deployed (`../pdp3/`). His standing verdict (SIMPLIFY §0) binds: simple, nothing twice,
the night identity, honest, email not WhatsApp.

## 1. What the content pages are today (audit `brief/inventory/AUDIT-content-pages.md`, 2026-09-02; unchanged since)

Seven pages, all on `templates/page.json` = `[editorial] elmsnest-content-page` → `[heading] main-heading` → `[main]
main-page` (contact: `page.contact-us.json` = `main-heading` + Kalles `contact-form`). `elmsnest-content-page.liquid`
(dev theme only; archived to `brief/inventory/theme-src/sections/elmsnest-content-page.liquid`) hard-codes the copy of
five pages — **guide** `/pages/guide-garden-lighting`, **why solar** `/pages/why-solar-lighting`, **about**
`/pages/מי-אנחנו`, **FAQ** `/pages/help-faq`, **processing time** `/pages/processing-time` — in the REJECTED cream
editorial (`#f7f0e6` page, brown ink, Assistant, an opaque `#12100e` band, bordered boxes, the same ruled list four times,
no images except a Pexels kerosene lantern on the About page, invisible header nav, duplicate h1). **Shipping**
`/pages/shipping-delivery` keeps its copy in the Shopify page body (en-doc classes) and renders on the Kalles path with
an invisible cream-on-cream title and no gutters. **Contact** is the Kalles form under the S-night heading.

The copy is good and honest (the audit's «worth keeping»: the four-decision spine of the guide, the day/evening/meaning
three-beat and the suits/does-not-suit pairing of why-solar, «רק תאורת חוץ. וזה בכוונה.» and the three principles of the
About page, the FAQ's answers, the schedule numbers that equal the policies). It is the *dress* that is wrong. Facts
already fixed elsewhere: the header nav is visible on every S page since SIMPLIFY (the header group is ours).

## 2. The task

Re-dress the seven pages in the SIMPLIFY vocabulary and give the five content pages photographs from the internet
(licence-filtered, credited) — the owner's «add images there too». Keep the copy (edit only where the audit flagged it:
the why-solar does-not-suit list must use the four licensed pairs of `elmsnest-s-place`, not three general negatives;
the four collection names must be the four titles used everywhere else). One template plumbing for all seven, so the
shipping page stops being «a different species».

Targets at 390×844 (JS on, footer included): guide ≤ 6 screens, why-solar ≤ 5, about ≤ 5, FAQ ≤ 6 (answers collapsed),
processing ≤ 4, shipping ≤ 5, contact ≤ 4. Desktop proportionally shorter.

## 3. Constraints that bind every concept

- **P1–P7 of `../simplify/SPEC.md` §2**, the tokens of §4 (night ground `#020306` with the sky gradient of
  `elmsnest-v2-core`, ink `#f4eee3`, ink-2 `#c9c4b8`, gold `#e9b96e`, glow `#ffd394`, hairline `#1f1e1d`, Frank Ruhl
  Libre 700 headings, Heebo 300/400 text, radius 0 except pills, logical properties, `<bdi dir="ltr">` on digits/Latin).
  The header, footer and the skin are shared files and stay untouched.
- **Nothing twice on a page, one device per idea.** The guide's four decisions may not be four copies of one ruled
  list: vary the device (a photograph row for the places, a numbered spine for the purposes, a two-column for the power
  sources, a checklist for the checks). Each page carries its terms/contact line at most once; the photo/email promise
  once; the four place words in the licensed forms. No boxes, no cards, no shadows, no pills except the store's one
  gold pill form («לכל המוצרים» style) for the page's single call to action.
- **Photographs — from the internet, honestly.** Sources and licences as `../pdp3/BRIEF.md` §4 (Openverse + Wikimedia
  Commons, CC0/PDM/CC BY/CC BY-SA, author + licence recorded, a credit caption where the licence needs one, no faces,
  no brand marks, no baked text, ≥ 1200 px, no heavy filters). The shortlist lives in `../pdp3/images/SHORTLIST.md`
  (roles «content: guide / about / why solar / contact» were requested) plus the home round's pool
  (`../home2/images/`). On a content page a photograph is a *place* or a *mechanism* (a garden at dusk, a panel in the
  sun, a courtyard), captioned or headed so it never reads as the store's product; the store's own frames may be used
  where the copy speaks of the store's products (`../pdp2/images/INVENTORY.md`). One top photograph per content page
  (a band with the h1 on it only where the crop measures ≥ 4.5:1; otherwise the h1 sits under it on the ground), and
  one or two more inside the page at section breaks — never a photograph per row. The Pexels kerosene lantern goes.
  Every photograph is a theme asset (`assets/ens-page-*.jpg`, ≤ 220 KB, ≤ 1800 px) with an `image_picker` override.
- **Template plumbing:** one new section `sections/elmsnest-s-page.liquid` (`enabled_on: templates: ["page"]`) renders
  the page by `page.handle`: the five hard-coded pages, shipping and processing (their copy from `page.content` or
  hard-coded — decide, say why), and a plain-prose fallback for any other page; `templates/page.json` order becomes
  `[ens_page]` only (the Kalles heading and main-page leave the template — rollback = the old JSON). The contact page
  keeps the Kalles `contact-form` section under a new `ens_page` entry in `page.contact-us.json` (the form is stock, P1);
  the section gives the contact page its photograph and the email promise once. Copy lives in the section (as now) with
  schema settings for every photograph and for the headings; long copy blocks may stay literal Liquid (the owner edits
  the page copy in code, as today) — say so.
- **Length and weight:** targets above; ≤ 3 photographs per page, lazy below the first, sized, ≤ 220 KB each.
- **Honesty:** BRIEF §3. The schedule numbers stay byte-identical to the policies (0 ₪ / 29.90 / 1–3 / 7–14 / 8–17 / 14
  days / 5% or 100 ₪). No counts except `products_count` (allowed catalogue fact), no reviews, no urgency.

## 4. Deliverable of a concept

`concepts/<name>/index.html` — the guide page and the About page rendered in full (the two most different pages), plus
the top of why-solar and of FAQ, with the real photographs from the shortlist by relative path and the credits drawn;
`shots/` at 390×844 (`guide-m-fold.png`, `guide-m-full.png`, `about-m-fold.png`, `about-m-full.png`, `why-m-fold.png`,
`faq-m-fold.png`) and 1366×900 (`guide-d-fold.png`, `about-d-fold.png`); `COPY.md` (any changed or new sentence; the
kept copy referenced by section), `IMAGES.md` (id, author, licence, credit, crop, role, and how it is framed so it does
not read as the product), `NOTES.md` (the device per idea, the template plumbing, measured heights at 390 per page,
the honest «is any of this twice?»).

## 5. Judging

Five judges from the shots: the owner (simple, my night store, nothing twice, the pages now have real pictures and read
as one family with the home and the product page), a first-time visitor who arrived on the guide from a search (does it
help me choose and send me to a collection, or is it a wall of text?), the honesty guardian (licences, credits, no
product implied, the numbers equal the policies, the four licensed pairs), a designer (the family resemblance to the
S pages, image treatment, rhythm, typography), an engineer (one section for seven handles, the template swap, the
contact form intact, weight, heights). Visitor and owner ×1.5.
