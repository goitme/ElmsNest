# NOTES — concept «band» (one band per page)

## 1. The idea, and the device per page

Every content page opens the same way — one full-bleed photograph band (the home band's skeleton: the `<img>` in flow, 520 px at 390 / 560 at ≥ 901 when the h1 sits on it, 400 / 480 when it sits under it), then ONE narrow reading column (640 px, centred) on the side-page ground gradient. Inside the column each idea gets exactly one device, and no device appears twice on a page:

| page | band (h1 on / under) | ideas → devices, in order | inline breaks (max 2) | CTA |
|---|---|---|---|---|
| guide | dusk sky, **h1 on** (18:1) | 01 places → **link list** (title · sub-line · count · ←) under the night-path photograph — one photograph, four links, not a photograph each · 02 purposes → **lettered spine** (א/ב/ג on a gold rail) · 03 power → **two-column dl** (term ┃ body; stacked at 390) under the cells photograph · 04 checks → **checklist** (hollow gold square + numeral, title only) · the note = the page's one contact line | night path (place) · solar cells (mechanism) | one gold pill «לכל גופי התאורה» |
| about | Haifa garden, **h1 under** (bright crop) | founding → prose · three principles → **numbered spine** (01–03) · «מה זה אומר בפועל» → **two-column dl** · the four collections → **plain link list** (title · ←) | the Jerusalem grove (place), before the collections | pill + text link «למדריך לבחירת תאורה ←» |
| why solar | sunrise, **h1 under** | how it works → **numbered spine** (1–3) · suits / does-not-suit → **pair** (two plain lists, side by side ≥ 600 px; the second list is the four licensed pairs of `elmsnest-s-place`) · three checks → **checklist** · the note = the contact line | the tilted panel (mechanism), between the spine and the pair | pill + guide link |
| FAQ | dusk path, **h1 on** (10.7:1) | role line with the contact link · three group links → **inline link row** · ten Q&A → **native `<details>`** in three groups (the first open) | none | text link «למדיניות המלאה ←» (no pill: the contact link is in the role line) |
| processing (not rendered) | a place band, h1 under | the three figures → the two-column dl (dt = label, dd = the `<bdi>` figure) · «מה קורה אחרי שהזמנתם» → numbered spine · the business-day note · the 17-day h2 + prose | none | pill «ליצירת קשר» + link «למדיניות המשלוחים המלאה ←» |
| shipping (not rendered) | a place band, h1 under | costs → two-column dl · times → numbered spine · returns → checklist-shaped rows (title + body) · the 17-day block | none | pill «ליצירת קשר» + link «מה קורה אחרי שהזמנתם ←» |
| contact (not rendered) | a courtyard band, h1 under | the two rich-text blocks verbatim → prose with one plain list · the photo/email line (`elmsnest-s-contact`) once · then the stock Kalles `contact-form` section | none | the form's own submit |

The vocabulary is the S pages': Frank Ruhl Libre 700 headings (h1 32 → 46 px, h2 24 → 30, row titles 20 → 22), Heebo 300/400/500 text (16 → 17), captions 13, credits 12, hairlines `#1f1e1d`, gold numerals, the one glow pill, the hairline-underlined text link with its 44 px `::before` belt, radius 0, logical properties, no boxes/cards/shadows (the spine's numeral square is a 1 px gold outline on the ground, not a box around content). No JS at all — the FAQ is `<details>`.

## 2. Plumbing — ONE section for seven handles

`sections/elmsnest-s-page.liquid`, `"enabled_on": {"templates": ["page"]}`, one preset «ElmsNest S — עמוד תוכן».

**Dispatch.** `case page.handle` → `when 'guide-garden-lighting' / 'why-solar-lighting' / 'מי-אנחנו' / 'help-faq' / 'processing-time' / 'shipping-delivery' / 'contact-us'`, `else` = the fallback. Each branch is literal Liquid holding that page's copy (as `elmsnest-content-page.liquid` holds it today) — the owner edits page copy in code, which the brief allows and which keeps the numbers in ONE reviewable file with the FAQ. **Shipping and processing are hard-coded too**, not read from `page.content`: their numbers must stay byte-identical to the policies and to the FAQ, and the shipping body in the admin carries the old `en-doc` classes; `main-page` leaves the template, so the Shopify body is no longer rendered anywhere and stays untouched as the rollback. The fallback branch prints `page.title` as the h1 on the ground and `{{ page.content }}` in the reading column (plain prose, the `.ens-page__col` type rules), so any new page the owner creates is dressed without code.

**Photographs.** Blocks of one type, `photo` («תמונה לעמוד»): `handle` (text — which page), `slot` (select: band / break-1 / break-2), `image` (image_picker), `caption` (text — the place or mechanism line), `credit` (text — «צילום: …», empty for CC0/own), `object_position` + `object_position_desktop` (text, as the home sections), `zoom` (text, «100%» default; «190%» keeps part of the width) + `keep` (select right/left), and for the band slot `h1_on_band` (checkbox). The section captures `ens_band`, `ens_break_1`, `ens_break_2` at the top: the first block matching this handle and slot wins; with no block, a Liquid map by handle names the theme asset (`assets/ens-page-<page>-<slot>.jpg`, IMAGES.md), its size, crop, caption, credit and the on-band default (guide + FAQ on, the rest under). The copy branch prints `{{ ens_break_1 }}` exactly where the break belongs (the guide: after 01's intro and after 03's intro). Srcset widths 600/900/1200/1400 capped to the file's width (the home2 R26 rule); band `loading="eager" fetchpriority="high"`, breaks lazy; `sizes="100vw"`. A photograph with neither block nor asset prints nothing, and the h1 sits on the ground — the honest state.

**Headings.** Section settings `h1_<handle>` (text) override each hard-coded h1 (empty = the copy's h1); the page's `page.title` stays the `<title>`.

**Templates.** `templates/page.json` → `{"sections":{"ens_page":{"type":"elmsnest-s-page","settings":{}}},"order":["ens_page"]}` — the Kalles `main-heading` (its `sr-only` duplicate h1 goes with it) and `main-page` leave; rollback = the old JSON. `templates/page.contact-us.json` → `["ens_page","contact_form"]`: the section's contact branch prints the band, the h1, the two rich-text blocks moved verbatim from the `_liquid` block, and the email promise once; the stock `contact-form` section follows untouched (P1). Header and footer groups untouched. Nothing deleted (P7): `elmsnest-content-page.liquid` stays as a file.

**Twice-guards in the section.** Per handle the contact line renders once (the guide's note, why-solar's note, the FAQ's role line, contact's `elmsnest-s-contact`; about/processing/shipping have none in the body — the footer's link suffices); the pill renders at most once; the foot nav of the old section is not rebuilt.

## 3. Measured at 390×844 (JS off — there is none; the shots are the measurements)

Page height = the `<article>` alone, without the 64 px header band and the 620 px footer band; screens = (page + 64 + 620) / 844.

| page | height at 390 | screens with header + footer | target | at 1366 (screens of 900) |
|---|---|---|---|---|
| guide | **3355 px** | **4.79** | ≤ 6 | 3808 px · 4.99 |
| about | **2433 px** | **3.69** | ≤ 5 | 2661 px · 3.72 |
| why solar | 2424 px | 3.68 | ≤ 5 | 2462 px · 3.50 |
| FAQ (answers collapsed but the first) | 1949 px | 3.12 | ≤ 6 | 2040 px · 3.03 |

Fold at 390: the guide's fold shows the whole band with the h1 on it, the caption and the role line, and the 01 heading; the About's fold shows the band, the h1 and role, and the first h2. No horizontal scroll at either width (`scrollWidth` = viewport; the two over-wide zoom images are clipped by their frames). Geometry and the contrast crops are in `measure/` (`shoot.js` reproduces them).

## 4. Is any of this twice? — honestly

- **On a page: no idea is drawn twice.** Each of the five list devices (link list, spine, two-column dl, checklist, pair) appears at most once per page; the contact line once; one pill; the four place words appear in the guide's kept copy (titles, sub-lines, the purposes) more than once — that is the guide's own copy naming places, not the fit pairs repeated; the licensed pairs themselves appear once (why-solar).
- **What does repeat on a page is the caption line under every photograph** — three on the guide. It is the licence's requirement (CC BY needs the credit) and the brief's (a photograph is captioned as place or mechanism); it is one line, not a section. If the lead wants fewer, the guide can drop the cells photograph and keep two.
- **Across pages the same skeleton recurs** — band, caption, role, column, the devices — once each; that is what «one section for seven handles» means and it is what the family resemblance to the home and the PDP rests on (the band is `elmsnest-s-home-band`'s skeleton; the caption and credit are `elmsnest-s-pdp-scene`'s credit line).
- **The collection names print on two pages** (guide with sub-lines and counts, about as plain links). Both are the question «which four places» on pages that ask it; on the home the same four are tiles. Not twice on any one page.
- Flags for the honesty guardian: the night-path photograph (guide) shows landscape lighting of another kind under a caption naming it as someone's garden; two Haifa balustrade globes and one far lamp post survive their crops at ≈ 3–6 px (IMAGES.md rows 4 and 8).
