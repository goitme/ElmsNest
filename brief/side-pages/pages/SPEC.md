# Content pages — the spec (lead synthesis, 2026-09-08)

## 0. What is built

The seven content pages leave the rejected cream editorial and are re-dressed in the SIMPLIFY night vocabulary by
**one new section** rendering all seven handles, **one photo snippet**, and **ten licensed photographs**. The copy is
the one in `COPY-SOURCE.md`, kept sentence for sentence except where §4 lists a change.

## 1. The five concepts, the judges, and the lead's rulings

Concepts in `concepts/{atlas,letter,field,band,quiet}/`; five judges from the real shots (owner and visitor ×1.5):
**atlas 46.5 · quiet 42.5 · letter 41.5 · band 41.0 · field 38.0**. The panel split — visitor, designer and engineer
for atlas; the owner for band; the honesty guardian for field — so the build takes the structure of the winner and
the opening grammar of the owner's choice:

| # | Ruling | Why |
|---|---|---|
| R1 | **Structure = atlas.** Devices vary with the content: an image atlas for the places, a lettered spine for the purposes, a two-column definition list for the power sources, a hollow-square checklist for the checks, a run-in trio and a link run on About. No TOC, no foot nav, one gold pill per page. | Visitor 9 («choosing is a look and a tap rather than a read»), designer 8 («no page reads as one ruled list repeated four times»), engineer 9 (lightest and most completely specified: 3.87 / 3.35 / 3.02 / 2.54 screens). |
| R2 | **Opening grammar = band.** Every one of the seven pages opens with one photograph band; the h1 sits **on** the photograph only where the crop measures ≥ 4.5:1 against the ink (measured, recorded), otherwise directly under it on the night ground. | Owner 9: «the only one where the content pages open the way my home and my product page open… a customer knows without thinking that this is the same shop». |
| R3 | **The band is short.** ≤ 220 px at 390 and ≤ 300 px at ≥ 901, so the page's first decision is at the fold. | Visitor 5 on band («spends the most screen on the least information»), and on letter/field («a hero that eats the fold»). |
| R4 | **The guide's four tiles become one frame with four labels** (quiet's device) — a single real courtyard at dusk, four labels under it naming what שביל · קיר · גינה · מרפסת are *in that frame*, each label carrying its collection's live Shopify title and `products_count` and linking to it (atlas's tile content). | Owner: «the smartest [idea]»; honesty and engineer both flag atlas's four photograph files against the ≤ 3-per-page cap; this keeps the visitor's point-and-tap and obeys the cap. |
| R5 | **Caption grammar = field.** Every caption opens with a kicker naming the kind of picture — «מקום» or «מנגנון» — then the subject and the hour, then the credit on its own line. | Honesty 8 for field, and its winner: «all nine say what they are before they say anything else». |
| R6 | **About ends signed** (letter): «כתבו לנו.» then ElmsNest, ישראל and the store's email address as text. | Owner 8 («turns the email promise from a policy line into a person»), visitor «the only one I would actually finish reading». |
| R7 | **No noon panorama owns a fold.** The Haifa terraces, the desert cactus park, the Kew borders and the yellow bougainvillea wall never sit in a band; where they are used at all they are inline and cropped. | Owner on atlas and field («midday bougainvillea, blue-sky Haifa… a Haifa panorama owning the entire desktop fold»), designer «the loudest of the five on the darkest ground». |
| R8 | **Every page gets a photograph, including the two policy pages** — one quiet band each, captioned as a place, no claim — so the seven pages open alike. | Owner's «one family»; engineer's objection to quiet («FAQ and processing get no photograph at all… under-delivers the owner's request»). |
| R9 | Desktop is a designed layout, not a phone column centred in 1366: the reading measure is 62–68 ch on its own column with the captions in the margin where the device has one. | Designer on band («there is no desktop design — a 640 px column centred in 1366»). |

## 2. Plumbing

- **`sections/elmsnest-s-page.liquid`** — `enabled_on: templates: ["page"]`, one `{% case page.handle %}` with seven
  `when` branches (`guide-garden-lighting`, `why-solar-lighting`, `מי-אנחנו`, `help-faq`, `processing-time`,
  `shipping-delivery`, `contact-us`) and an `else` that prints `page.title` + `page.content` in the plain prose style
  (so any future page renders correctly). Copy lives as literal Liquid inside each branch, as it does today, with the
  h1 and the lead of every page exposed as schema text settings. The shipping page's numbers move into the section so
  all seven pages share one source and one `<bdi>` discipline; a `shipping_from_body` checkbox prints `page.content`
  instead (rollback without touching Shopify — the Shopify page body is never edited).
- **`snippets/elmsnest-s-page-photo.liquid`** — one photograph slot: `image` (picker, empty → the theme asset),
  `asset`, `kicker`, `caption`, `credit`, `alt`, `pos` / `pos_d` (`object-position` per breakpoint), `band` (boolean:
  full-bleed band vs. inline frame), `h1_on` (boolean: the h1 is set on this photograph). Ten slots are used.
- **`templates/page.json`** — order becomes `["ens_page"]` only (the Kalles `main-heading` and `main-page` leave the
  template; the old JSON is the rollback). **`templates/page.contact-us.json`** — `["ens_page", "contact_form"]`, the
  stock Kalles contact form untouched (P1) under the contact page's own h1, photograph and email line.
- Live data only: `collections[handle].title`, `products_count`, `pages[…].url`, `shop.shipping_policy.url`,
  `shop.refund_policy.url`, and the four licensed pairs from `snippets/elmsnest-s-place.liquid`.
- No JS beyond native `<details>`; radius 0 except the one gold pill; logical properties; tokens by name.

## 3. The photographs (ten, ≤ 3 per page, all from `../pdp3/images/`)

| page | slot | id | licence / credit | kicker + caption |
|---|---|---|---|---|
| guide | band | `ov_30d8e75d…` | CC BY 2.0 → צילום: aenigmatēs (CC BY 2.0) | מקום · שמיים בין ערביים, מעל גינה |
| guide | places frame (4 labels) | `ov_b59b37d7…` | CC BY 2.0 → צילום: Jeremy Levine Design (CC BY 2.0) | מקום · חצר אחת בשעת בין ערביים |
| why-solar | band | `wm_51200569f7` | CC BY-SA 4.0 → צילום: Dietmar Rabich (CC BY-SA 4.0) | מקום · זריחה בין עצים |
| why-solar | mechanism | `wm_5869e6ea3a` | CC BY 2.0 → צילום: Guilhem Vellut (CC BY 2.0) | מנגנון · תא סולארי מקרוב, באור יום |
| about | band | `wm_d5e6fd1fe6` | CC BY 2.5 → צילום: זאב שטיין (CC BY 2.5) | מקום · חורשה בירושלים, בצל של צהריים |
| about | inline | `ov_f33051a3…` | CC BY 2.0 → צילום: RonAlmog (CC BY 2.0) | מקום · חצר בירושלים, בצל |
| help-faq | band | `wm_a17b65ac2a` | CC BY-SA 3.0 → צילום: PumpkinSky (CC BY-SA 3.0) | מקום · שביל בגינה, בין ערביים |
| processing-time | band | `wm_51c75f4f98` | CC BY 4.0 → צילום: Swphotouk (CC BY 4.0) | מקום · גינה ים-תיכונית, אחר הצהריים |
| shipping-delivery | band | `ov_8bc79722…` | CC BY 2.0 → צילום: Dimitry B (CC BY 2.0) | מקום · מטע זיתים, יום מעונן |
| contact-us | band | `wm_98c063e839` | CC BY-SA 2.0 → צילום: Josh Evnin (CC BY-SA 2.0) | מקום · חצר בחיפה, בצהריים (crop on gravel and palm) |

Assets `assets/ens-page-<slug>.jpg`, ≤ 1600 px, ≤ 210 KB, `loading="lazy"` below the first, `width`/`height`,
`sizes` matching the rendered width, `srcset` candidates ≤ the file. No frame shows a lamp that could read as a store
product; the two frames that contain a fixture (the courtyard's doorway light, the Haifa lamppost) are captioned as
places and are never under a heading about lighting products. The Pexels kerosene lantern of the old About page goes.

## 4. Copy changes (everything else stays byte-identical to `COPY-SOURCE.md`)

1. **The four collection names** become the live Shopify titles everywhere (guide §01, About): «תאורת שביל, עמוד וגינה»,
   «תאורת קיר», «ספוטים, פרוז׳קטורים ותאורה ניידת», «גרילנדות ותאורה דקורטיבית».
2. **why-solar's «does not suit»** becomes the four licensed pairs of `elmsnest-s-place`, place word + sentence,
   replacing the three general negatives.
3. **Dropped:** the guide's and the FAQ's TOC, the five-page foot nav, the guide's second button (the note above it
   already links to contact), the duplicate `main-heading` h1 (the template swap removes it).
4. **Added:** the ten captions and credits of §3, the four labels of the guide's places frame, and About's signature
   line (R6). Nothing else is written.
5. The typo in guide §03 row 1 («בצל כבוד» for «בצל כבד») is **left as it is** and recorded as an owner item — the copy
   is his.

## 5. Budgets and verification

- Screens at 390×844 (JS on, footer included): guide ≤ 5, why-solar ≤ 4.5, about ≤ 4.5, FAQ ≤ 5, processing ≤ 4,
  shipping ≤ 5, contact ≤ 4. Desktop proportionally shorter (measured, not assumed).
- `verify-mirror.js` already carries the seven pages (`page-guide`, `page-why`, `page-about`, `page-faq`,
  `page-processing`, `page-shipping`, `page-contact`); add copy probes for the h1 of each page, the four collection
  titles, the seven policy numbers and the ten captions.
- Contrast measured on the real render: the h1 on a band ≥ 4.5:1 (otherwise the h1 moves under the band), captions and
  credits ≥ 4.5:1 on their real ground.
- Weight per page ≤ 3 photographs, ≤ 420 KB of images.

## 6. Owner items this round records

1. The «בצל כבוד» typo in the guide (§4.5).
2. An Israeli photograph at dusk or golden hour — every Israeli frame in the pool is midday; the golden-hour places
   are Mediterranean-looking but photographed elsewhere. One own photograph replaces any band in a picker.
3. The contact page's Shopify body is never rendered by the template today; if it holds copy the owner wants shown,
   it goes into the section's contact branch.
