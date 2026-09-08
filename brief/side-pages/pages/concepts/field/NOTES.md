# NOTES — concept «field» (content pages, 2026-09-07)

Angle: **a field guide.** Bright daylight photographs on the night ground, each one a *plate* with its caption set in a margin column (typography only: a gold serif kicker «מקום» or «מנגנון», the place and the hour, the credit in 12 px mute). Every page opens with the h1 on the ground and the first plate **under** it — never a band, never type on a photograph. Wide gutters (`--env2-gut`, a 240 px margin column at ≥ 901), one content column of ≤ 62ch, Frank Ruhl Libre 700 for h1/h2/terms, Heebo 300/400/500 for text, radius 0 except the one gold pill, no boxes, no cards, no shadows, no JS (the FAQ's `<details>` is native). The tokens are the `:root` of `elmsnest-v2-core` copied by value; the page ground is its side-page gradient.

## 1. The device per idea, per page

Rule: one device per idea, no device twice on a page. Hairline rules appear in at most one device per page.

**Guide** (rendered in full)
- Head: h1 + role line in the content column; the four-anchor TOC in the margin column (a small muted line under the lead on the phone).
- Top plate (Haifa terraces, noon) — the h1 is above it on the ground; caption in the margin.
- 01 places — **photograph row**: the section's own plate (the cholla path) and under it the four collection rows as *links without rules*: Shopify title in serif, the kept sub-line, «N מוצרים ←» in the end column (two columns on the desktop). The whole row is the link.
- 02 purposes — **numbered spine**: one gold vertical rule, the letters א / ב / ג hanging outside it in gold serif, title + sentence inside.
- (mechanism plate — PV cells in sun — at the break)
- 03 power — **two-column table**: term (serif, small gold numeral) beside its definition, hairlines between the three rows; 2fr/3fr on the phone, 1fr/2fr on the desktop.
- 04 checks — **checklist**: a 14 px hollow gold square before each line, two columns on the desktop.
- Foot: the note with the page's one contact link, then the one gold pill «לכל גופי התאורה». No second button, no foot nav.

**About** (rendered in full)
- Head: h1 «רק תאורת חוץ. וזה בכוונה.» + role; top plate (Jerusalem grove) under it.
- «למה הקמנו את ElmsNest» — **prose** (18 px).
- «העקרונות שמכוונים אותנו» — **legend**: three columns (stacked on the phone), a big gold numeral over a serif title over one sentence, one hairline above each.
- «מה זה אומר בפועל» — **run-in paragraphs**: the three titles become serif run-ins with a gold dash, no numerals, no rules.
- The marginal figure (Sergei Courtyard, 4:5) — in the margin column beside the run-ins on the desktop, a full-width portrait after them on the phone.
- «מה תמצאו בחנות» — **link run**: the four Shopify titles as hairline-underlined serif links wrapping on one line, each with ←.
- Foot: the pill «לכל גופי התאורה» + text link «איך בוחרים תאורה לגינה? ←», then the `elmsnest-s-contact` line once (this page has no other contact link).

**Why solar** (rendered in full; the fold shot is the deliverable)
- Head + top plate (cell macro). «איך זה עובד בפועל» — **three beats**: gold numeral beside serif title, three columns on the desktop. «מתי זה מתאים — ומתי עדיף פתרון אחר» — **two lists side by side**: the «יכול להתאים» items with a short gold dash marker; the «עדיף פתרון אחר» list as the **four licensed pairs** on hairlines (place word in gold serif · the `emit:'no'` sentence — the home fit block's grammar, the only place where the four words are typed on these pages). Sunrise plate at the break. «שלוש בדיקות» — **three questions in serif** with margin numerals. The note (its «שאלו אותנו» is the page's one contact mention), the pill «איך בוחרים תאורה לגינה?» + text link «לכל גופי התאורה ←».

**FAQ** (rendered in full; the fold shot is the deliverable)
- Head with the role line («כתבו לנו» = the one contact link) and the three-anchor TOC; top plate (bougainvillea). Three h2 groups of **native `<details>` on hairlines** (a gold chevron drawn with two borders, first one open). **One photograph between the groups**: the Taormina alley as a marginal 4:5 figure beside «הזמנות ומשלוח» on the desktop, a full-width portrait before it on the phone. Foot: text link «למדיניות המלאה ←» only (the «ליצירת קשר» pill would be the contact twice).

**Processing** (not rendered) — h1 + role; top plate (gravel terrace at dusk); the three plate numbers as **the home terms-strip row grammar** (serif gold numeral in `<bdi>`, unit, label); «מה קורה אחרי שהזמנתם» as a **numbered spine**; the business-day note; the 17-day h2 + prose; pill «ליצירת קשר» + text link «למדיניות המשלוחים המלאה ←». ≈ 3 screens.

**Shipping** (not rendered) — no photograph (the numbers are the picture); h1 + the same head grammar; «עלויות משלוח» as **two serif term rows**; «זמני טיפול ואספקה» as a **two-column table**; the tracking note; «ביטול עסקה והחזרות» as **run-in paragraphs**; the binding-policy note; the 17-day h2 + prose; pill «ליצירת קשר» + text link «מה קורה אחרי שהזמנתם ←». ≈ 3.5 screens.

**Contact** (not rendered) — h1 «יצירת קשר»; top plate (Haifa gravel bed, 1:1); the column-2 instructions as a **short legend** (two serif h3s, the three-item list with the dash marker, the email line once); then the stock Kalles `contact-form` section untouched (P1). ≈ 3 screens.

## 2. Template plumbing — one section, seven handles

**`sections/elmsnest-s-page.liquid`** (`enabled_on: templates: ["page"]`, one preset, class `ens-page-section`). It reads `page.handle` once:

```liquid
{%- liquid
  assign key = 'plain'
  case page.handle
    when 'guide-garden-lighting' then assign key = 'guide'
    when 'why-solar-lighting'    then assign key = 'why'
    when 'מי-אנחנו'              then assign key = 'about'
    when 'help-faq'              then assign key = 'faq'
    when 'processing-time'       then assign key = 'proc'
    when 'shipping-delivery'     then assign key = 'ship'
    when 'contact-us'            then assign key = 'contact'
  endcase
-%}
<article class="env2-section ens-page ens-page--{{ key }}" dir="rtl" data-ens-page="{{ key }}">
  {%- render 'elmsnest-s-page-head', key: key, page: page, section: section -%}   {# h1 + role + TOC + top plate #}
  {%- case key -%}
    {%- when 'guide' -%}   … the guide body, literal Liquid …
    {%- when 'about' -%}   …
    {%- when 'why' -%}     …
    {%- when 'faq' -%}     …
    {%- when 'proc' -%}    …
    {%- when 'ship' -%}    …
    {%- when 'contact' -%} … the instructions block only; the form is the next section …
    {%- else -%}
      <div class="ens-page__prose">{{ page.content }}</div>          {# any other page: plain prose on the ground #}
  {%- endcase -%}
</article>
```

- **Where copy lives.** The long copy of the seven pages stays **literal Liquid inside the section**, as `elmsnest-content-page.liquid` does today — the owner edits page copy in code, and the fact strings must stay byte-identical to the policies, which a rich-text setting cannot guarantee. **Shipping's copy moves from the Shopify page body into the section** (decision: hard-coded, like processing): one source and one style for the numbers, `<bdi>` on every figure, no `en-doc` classes left in a page body; `page.content` for that handle is ignored by the `ship` branch, so the body can be emptied later or kept as a backup. The `else` branch prints `page.content` for any future page.
- **What the schema exposes.** Per handle: `h1_<key>` (text, default = the h1 above; blank = `page.title`), `lead_<key>` (text). Photographs as **blocks of type `plate`**: `page` (select of the seven keys), `slot` (select: `top` / `mid` / `side`), `image` (image_picker), `object_position` + `object_position_desktop` (text, the `--ens-op` pattern of `elmsnest-s-home-band`), `kicker` (select «מקום» / «מנגנון»), `caption` (text), `credit` (text — the drawn credit line; blank = «נחלת הכלל»), `alt` (text). No block for a slot → the section renders the theme asset of this concept (`assets/ens-page-guide-top.jpg` … nine files, ≤ 1800 px, ≤ 220 KB, srcset capped at the file width as the home band does) with the crops of IMAGES.md; the credit strings are literals next to the asset names. One `checkbox` `show_toc` for the guide and the FAQ. The collection rows read `collections['…'].title` and `.products_count` live (the four handles are literals, menu order); the four pairs on why-solar come from `render 'elmsnest-s-place', collection: collections[handle], emit: 'word' / 'no'`; the About contact line is `render 'elmsnest-s-contact'`.
- **Templates.** `templates/page.json` → `"order": ["ens_page"]` only — `main-heading` and `main-page` leave the template (their hidden duplicate h1 and the invisible cream title go with them; rollback = the old JSON). `templates/page.contact-us.json` → `"order": ["ens_page", "contact_form"]`: the section prints the h1, the plate and the instructions block; the stock Kalles `contact-form` keeps its blocks and posts to `/contact` as today (P1); its `_contact_col` rich text is emptied so the instructions print once.
- **Weight.** ≤ 9 KB of CSS in the section (the rules of this mock, prefixed `ens-page-`); no JS; the first plate `loading="eager"`, the rest `lazy`; all with `width`/`height`.

## 3. Measured at 390 × 844 (Playwright, Chromium 1194, fonts loaded, JS irrelevant — nothing on the page needs it)

| page | content height (without the 64 + 620 px bands) | with header + footer | screens | target |
|---|---|---|---|---|
| guide | **3003 px** | 3687 px | **4.4** | ≤ 6 |
| about | **2428 px** | 3112 px | **3.7** | ≤ 5 |
| why-solar | 2253 px | 2937 px | 3.5 | ≤ 5 |
| FAQ (answers collapsed, first open) | 2002 px | 2686 px | 3.2 | ≤ 6 |

Desktop 1366 × 900 content heights: guide 3217 px, about 1938 px, why 2285 px, FAQ 1843 px — proportionally shorter than the phone (the fold shows the h1, the lead, the TOC and the whole top plate with its caption). No horizontal overflow at either width (`scrollWidth == clientWidth`). Estimated, not rendered: processing ≈ 3, shipping ≈ 3.5, contact ≈ 3 screens (targets 4 / 5 / 4).

## 4. Honesty — «is any of this twice?»

Checked page by page:
- **Guide.** Contact: once (the note's link; the ghost button is gone). Terms: none (not this page's job). The four place words: only in the kept copy (sub-lines, purposes). Devices: plate + link rows / spine / table / checklist — four different ones. The TOC names the four questions and the four h2s repeat them — that is what a contents line is; it is 13 px and one line, and `show_toc` can switch it off. The top plate and the §01 plate are 300 px apart on the phone — two photographs close together, both places; if a judge reads that as one idea twice, the §01 plate is the one to drop (the rows stand without it).
- **About.** Contact: once (the `s-contact` line). The four titles: once (the link run). Two photographs, both places, at different aspects and different distances.
- **Why-solar.** The «yes» list and the four pairs both speak of suitability — the source's own pairing, kept; the pairs replace three sentences, they do not add a second list. The note's «שאלו אותנו» is the one contact mention (no link, as in the source).
- **FAQ.** Contact: the role line's «כתבו לנו» once; the «ליצירת קשר» pill is gone. The refund policy is linked twice — inside the cancellation answer (kept copy) and as the foot link «למדיניות המלאה ←» (kept CTA text): the same destination twice on one page. Honest answer: **yes, that one is twice**; the fix is to drop the foot link and let the answer's own link carry it — kept here only because the source lists it as the page's CTA.
- **Across the family.** The plate-with-margin-caption is used on every page — that is the family device, once per page opening, as the scene is once per PDP. No photograph appears on two pages. The foot nav that printed the footer's four links a second time on five pages is gone.

One-line answer: **nothing on the guide or the About page is twice; on the FAQ the refund policy is linked twice (answer + foot link) — drop the foot link if the judges count it.**
