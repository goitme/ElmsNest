# Lead decisions on the review's "lead's call" items (2026-09-05, before the fixer ran)

Written from the five group files on disk (home 5, pdp 5, collection 4, templates 2, edited 4; interfaces pending)
so the fixer's diff can be checked against a decision made before it, not rationalised after it.

| finding | decision | why |
|---|---|---|
| index.json:23 «הגינה נדלקת.» — drop the terminal period (P4) | **KEEP the period. Add an exemption to P4/§6.1.** If the fixer drops it, restore it. | The hero headline is a two-line *sentence* («כשהשמש יורדת, / הגינה נדלקת.»), not a label; P4's rule is for section headings. The owner has seen this line on every version of the homepage since round 0. Changing the homepage's one sentence to satisfy a rule written for labels is the kind of self-imposed constraint the owner told us not to apply («ما اتحط قيود لنفسك»). |
| hero schema label «כפתור משני — טקסט (וואטסאפ)» (editor-only) | **Apply the one-word label edit** (line 245 → «כפתור משני — טקסט»; line 246 → «קישור חיצוני לכפתור המשני (ריק = עמוד יצירת קשר)»). Record the hero diff as "one setting + two labels". | The word never reaches the storefront, but the owner's answer was «فش رقم واتس، خلي البريد» and an editor label that still calls the button a WhatsApp button will mislead whoever edits the theme next. Zero storefront risk. |
| layout/theme.liquid: the comment line above the skin render | **Delete the comment line** so the diff is the single render line §10 names. | The exact-edit rule exists so a rollback is one line; keep it exact. |
| footer-group.json: `info@elmsnest.com` without `<bdi>` | **Apply** the `<bdi dir="ltr">` wrap and amend §10's "unchanged" note to "unchanged except P6 bdi". | P6 is a hard rule; the footer is our file and "held to the same rules" (P2). |
| pdp-facts heading «מה שכדאי לדעת» | **Remove** (`"heading": ""`). | §8.2 licenses no heading; P2 answers each question once; it near-duplicates the bullets marker «פרטים שכדאי לדעת». |
| elmsnest-s-collections: `default: col.featured_image` fallback | **Remove.** | P3: the store's own image, no silent substitution of a product photo for a collection image. |
| elmsnest-s-products: fallback to `collections.all.products` when nothing is picked | **Remove.** | An unlabelled best-selling order is exactly what P4 forbids («הנמכרים ביותר must not render»). |
| elmsnest-s-pdp-kicker: `collections[handle]` → loop over `product.collections` | **Apply.** | Keeps the snippet inside the object list §10 allows; same result. |
| skin file 12,254 bytes vs "≤ 12 KB" | **Apply** the header-comment trim. | Cheap; removes an ambiguity. |
| pdp-facts `<dd>` bidi tokenisation (the one MAJOR) | **Apply the whole-token wrap**, then LINT and render-check the two products the reviewer named (`waterproof-solar-deck-step-lights` 800mAh, `magnetic-rechargeable-touch-wall-light` 1200mAh) after deploy. | A Liquid rewrite of ~10 lines is the one fix that can break the file; it gets its own check. |

Everything else in the five files is mechanical and is applied as written.

## Added after the interfaces reviewer returned (7 findings, 1 major)

| finding | decision | why |
|---|---|---|
| footer «קולקציות» links carry no `data-ens-place` (MAJOR) | **Apply**: add `data-ens-place="<handle>"` to the four anchors in `footer-group.json`. | §11's order test names the footer as the fifth place; without the attribute the footer is invisible to the test and "the same order everywhere" cannot be proven. Labels and order are already right. |
| header-group.json `note_mobile` «אימייל: info@elmsnest.com» without `<bdi>`; footer_bottom «ElmsNest © 2026» | **Apply** the `<bdi dir="ltr">` wraps in both group files. | Same P6 rule as the footer_about line; the header group is ours (P2). |
| elmsnest-s-collections: `alt` escaped twice (`| escape` then `image_tag`) | **Apply**: drop the `| escape`. | Latent double-escaping; one-token fix. |
| pdp-facts `{{ heading }}` / `{{ more_label }}` output unescaped | **Apply** `| escape` on both, AND set the template heading to `""` (already decided above). | Both halves: the heading goes, and the code path stays safe for any future value. |
| pdp-facts bidi: the fixed code list misses 3000K, 6W, 120°, AA, Up/Down … (11 products) | Same as the major above: **whole-token wrap**, using the `elmsnest-v2-terms.liquid` word loop as the model. | Two reviewers, same root cause; one fix. |
| coll-header «כל המוצרים» pill `data-ens-place="all"` | **Apply**: drop the attribute from that pill. | Two reviewers agree; the four collection pills keep it. |

## After the fixer and the re-review (2026-09-05)

- The three `<bdi>` wraps (footer_about, footer_bottom, header note_mobile) were approved above and not applied by the fixer; **applied by the lead**, `header-group.json` added to the deploy order and to SPEC §10.
- The contact line's raw `&` in the mailto: the re-reviewer listed it as lead-approved. It was not — the skeptic **refuted** it (a bare `&body=` is not an ambiguous ampersand; every sibling caller of the same builder prints it the same way). Left as is.
- `elmsnest-s-pdp-facts.liquid` at 13,293 bytes after the bidi rewrite (the token loop written twice): **accepted** — "≤ 12 KB" is a smallness guideline with no runtime meaning, and a de-duplicating refactor before the first deploy is a risk the round does not need. The nested-`<bdi>` note on digit-led ranges is checked on the real render (§11 bdi count), not in the abstract.

## Learned at deploy time (2026-09-05): what Kalles' rich-text settings refuse

Shopify validated `sections/footer-group.json` on upsert and refused it twice: *"Tag '<bdi>' is not permitted"* and
*"Attribute 'data-ens-place=…' is not permitted on tag '<a>'"*. A `richtext` setting admits only a fixed tag/attribute
list. So, **reversed by the lead**: the two footer `<bdi>` wraps and the four `data-ens-place` markers on the footer
collection links. The bidi algorithm resolves a trailing LTR run (`info@elmsnest.com`, `ElmsNest © 2026`) correctly on
its own, so P6 loses nothing visible; the §11 order test reads the footer's order from the collection links' `href`s
in DOM order (`footerOrder` in verify-mirror.js) instead of from `data-ens-place`. The header's `note_mobile` is an HTML
setting and **kept its `<bdi>`** (accepted by the same validator). Also learned: a `url` setting may not carry a page
path as default, and a `text` setting may not carry an empty default — three sections bounced on those and were fixed.

## Critique of the deployed render (2026-09-05 evening): decisions written BEFORE the fixer runs

Read from `critique/shopper.jsonl` (12 findings) and `critique/qa.jsonl` (7) as they landed; the honesty and owner
lenses are added below when they land. The fixer must follow this table where it names a finding; everything else
that the skeptics confirm is applied as written. `lint.py` and the three stock levers of `/all` (7.94 screens,
50 px of margin under the 8-screen target) are the two constraints every fix here is checked against.

| finding | decision | why |
|---|---|---|
| shopper 0 (major): buy button below the fold on every phone; fix = mobile media layout | **Apply the stock lever only**: `templates/product.elmsnest.json` → `main-product-medias.mobile_media_layout: "fraction"` (Kalles' other option: a «1 / N» counter instead of the thumbnail strip). **Do not** change `image_ratio` — the featured photo keeps its own frame (owner answer 2). Re-measure `atcTop` after deploy; no hard fold target is set, the aim is the price and the pills inside the first screen at 390×844. | The only two values Kalles offers are `thumbnails` and `fraction` (block schema fetched from the dev theme). The strip costs ~100 px on every PDP; the counter is the pattern Dawn uses (P1). |
| shopper 1 + qa 2: sort chevron points LEFT in RTL (`border-inline-end` rotated 45°) | **Apply** `border-inline-start` (keeps `border-block-end` and `rotate(45deg)`); and prefix ONLY the default option: «מיון: מומלץ». | Two lenses, same geometry. A closed select shows the selected label, so the prefix is needed only on the resting state; the price options already say what they are. |
| shopper 2 (major, owner-admin): 7 of 8 path cards are marketplace collages | **Owner report**, not theme. SPEC §9 image sheet (5 products with a clean frame at images[1..4]; 14 without any). | The store's own featured image is the rule (owner answer 2, P3); reordering media is an Admin action the owner must approve. |
| shopper 3: card titles clamped to 2 lines → «– 0…» ellipses; fix = 3 lines | **Refuse the 3-line clamp.** Owner report: a list of the 27 titles with their length on a 2-line card, for the owner to shorten (his answer 4 makes the Shopify title the card's name). | 14 rows × ~22 px would put `/all` back over 8 screens (7.94 now, 50 px of margin). The title is the owner's text; cutting it differently is not ours to invent. |
| shopper 4 + qa 6: the one-variant path light shows a picker with one pill and a one-option no-JS select | **Apply the theme half**: wrap the `ens_noscript` block's `<select>` in `{% unless product.has_only_default_variant %}…{% endunless %}`. **Owner report** for the Admin half (remove the option «צבע אור» from that product; Kalles then omits the picker — no setting controls this, it is hard-coded on `has_only_default_variant`). | The picker block cannot be wrapped from a template; the noscript guard is ours and cheap. |
| shopper 5: hero lead «קטגוריה אחת בלבד» reads as "only one category" above four collections | **Apply the smallest edit**: delete «קטגוריה אחת בלבד — » so the lead reads «מנורות שביל, קיר, גינה ומרפסת. אם מוצר לא מתאים למקום שלכם, נגיד את זה לפני שתזמינו.» in `templates/index.json`; fix the schema `default` in `elmsnest-v2-hero.liquid` line 241 to the same sentence (its place order was wrong: «שביל, קיר, מרפסת וגינה»). | The lead is spec-authored copy (§6.1), not the owner's; §11 reads the four place names from it in menu order, which the edit preserves. |
| shopper 6: hero h1 breaks into three lines at 390 (`clamp(54px,15.5vw,72px)`) | **Apply a size change only**: `.env2-hero__h1{font-size:clamp(40px,11.5vw,56px)}` in the ≤900 px block (line 194). Nothing else in the hero moves; no `min-height` change. | The fold shot confirms «כשהשמש / יורדת, / הגינה נדלקת.» — the two-line sentence the owner has seen since round 0 is broken mid-clause. The size is the defect, the sentence is not. |
| shopper 7: PDP terms line lacks the home-delivery price | **Apply**, one line still: «משלוח חינם לנקודת איסוף · עד הבית <bdi dir="ltr">29.90 ₪</bdi> · אספקה משוערת <bdi dir="ltr">8–17</bdi> ימי עסקים · ביטול עד <bdi>14</bdi> יום מקבלת המוצר». | «עד הבית 29.90 ₪» is the home strip's own licensed wording (`elmsnest-s-terms.liquid` line 19, BRIEF §3). The moment before the button is where the door price is asked. |
| shopper 8: at 360×640 the collection header fills the whole fold | **Apply at ≤400 px only**: `.ens-ch__hero{min-block-size:calc(30svh + var(--header-height,60px))}` (and the vh fallback). Not the ≤900 px block. | 390×844 is already right (36svh after the /all trim); only the small phone needs the extra 40 px. |
| shopper 9: the facts «כל מה שכתוב על המוצר» chevron points right (= back, in RTL) | **Apply**: closed = down (`border-inline-start` + `border-block-end`, `rotate(-45deg)` → use `rotate(45deg)` with `border-inline-end`… the fixer picks the pair that yields DOWN and verifies the geometry in a comment), open = up. | Same class of defect as the sort chevron. |
| shopper 10: sticky bar painted over the main form in full-page captures | **Refuse.** Record as a capture artefact: the fold captures do not show it; Kalles offers only «Always» and «Scrolls outside the scope of the form», and the template already uses the second. | The full-page capture makes the viewport as tall as the page, so "outside the scope of the form" is never true there. |
| shopper 11 (owner-admin): no wordmark above the footer | **Owner report**: a logo file that carries the name, set as `logo` / `logo_mobile` (~120 px). No theme edit now. | The icon-only logo is the owner's asset choice; we ask, we do not swap. |
| qa 0 (major): /all 8.15 screens | **Refuted by the current numbers**: `verify.json` `collection-all-m-js` = 7.94, `overTarget:false` (commit 9a6970a; the lens read the file before the subset run rewrote it). **Do not** apply the 28vh header or the card-padding trim. | The three stock levers already did this; a fourth trim of the header photo has no defect behind it. |
| qa 1: 360×640 `overTarget` for home and /all | **No theme change.** SPEC §11 gets one sentence: the screen targets bind at 390×844; 360×640 and 1366×900 are recorded for information. | P5 defines the targets at 390×844. |
| qa 3: no-JS desktop thumbnail rail collapses to one thumbnail | **Apply** in the skin, keyed on `hdt-slider-thumb:not(:defined)` (Kalles sets no `html.no-js` hook we can rely on): the thumb container becomes a grid with the transform cleared. | JS-off is a §11 surface; one rule, no JS-on effect because a defined element never matches. |
| qa 4: the JS price swap / sticky sync has no positive evidence | **No theme change; open verification item in HANDOFF §7.6**: run `verify.js` against the live preview from a machine whose browser can reach the store (this sandbox's Chromium cannot). The server side is proven (variant 2 renders 99.90 with its own form id; the drawer received the live add). | Already a documented §11 exemption; the fix is a measurement, not an edit. |
| qa 5: no drawer screenshot | **Done** after the lens ran: `verify-after/drawer-rope-{mobile,desktop}.png` (rope light in the drawer, 89.90 ₪, checkout). Goes into the owner artifact. | — |

### Owner and honesty lenses (landed 16:21 / 16:2x) — and two rulings above revised by a measurement

`critique/clamp-experiment.js` served the /all mirror at 390×844 and injected CSS overrides (`critique/clamp-experiment.txt`):

```
clamp2 (now)          docH 6702  7.94 screens  26 of 27 titles clipped
clamp3 (portrait)     docH 7011  8.31          2 clipped   ← over target: why shopper 3 was refused above
square only           docH 6087  7.21          26 clipped
square+clamp3+16px    docH 6342  7.51          0 clipped   ← chosen
```

All 27 featured images are 1:1 (mirror `width`/`height`), so Kalles' `square` ratio shows the owner's frames whole
(owner 0: the portrait cover-crop slices his baked-in captions) and is 44 px shorter per row than `portrait`.

| finding | decision | why |
|---|---|---|
| owner 0 (major): portrait crop cuts the owner's images | **Apply** `templates/collection.json` `image_ratio: "square"` and `sections/elmsnest-s-products.liquid` lines 23/30 `image_ratio: 'square'` (not `adapt`: uniform grid, P1; a future landscape upload still gets a stable card). | 27/27 square sources; no crop; −616 px on /all. |
| owner 5 + shopper 3 (REVISED): 2-line clamp swallows «10» → «0…» | **Apply** in the skin line 16: `--line-clamp-count:3` and `font-size:16px` (line-height 1.3). Owner-admin note on titles stays as advice, no longer as the fix. | With square cards the page lands at 7.51 screens with 0 clipped titles (measured above). |
| owner 1 (major): PDP facts `<dl>` repeats the variant options (lengths, colours) | **Apply** in `elmsnest-s-pdp-facts.liquid` dl loop: skip a `<dd>` whose stripped text equals any `product.variants[].option1/2/3` value or contains two or more of `product.options_with_values[].values`; drop a `<dt>` left without rows. Render-check the rope light after deploy. | Complaint 2 in his own words; the picker already answers the question (P2). |
| owner 2 (major): the four places three times on the home (lead, tiles, fit rows) | **Refuse the merge; put the question to the owner in the artifact.** The tiles answer «which four places»; the fit rows answer «does it suit / when not» with the four approved pairs — the honesty device he approved. Folding «yes» into the tiles and dropping «no» would remove the pairs from the home. The lead is a sentence, not a section. | P2 maps two questions to two blocks. If he says it is still «twice», the fold is a one-block change (remove `ens_fit` from the order). |
| owner 3 (major): buy button below the fold | Same as shopper 0: `mobile_media_layout: "fraction"` (Kalles has no `dots`). The 28 px mobile title stays. | — |
| owner 4 (major): the sticky bar painted over the pills in every full-page PNG | **Harness fix, applied by the lead** (`verify-mirror.js`: the bar is hidden for the full-page capture only, restored for the fold). The PDP PNGs are re-shot with the re-verify after deploy; the owner sees clean captures. | Capture artefact of a page-tall viewport, not the live page. |
| owner 6: «IP65» numeral + caption «עמידות IP65» | **Apply**: caption = the bullet with the code token removed; when nothing but the code remains, no caption. | Literally the same thing twice, where he will look. |
| owner 7 (owner-admin) + honesty 2: /all is Shopify's automatic collection, sorted alphabetically; «מומלץ» names an order that does not exist there | **Theme**: relabel the manual option «סדר החנות» (the store's order — true on every collection, including the automatic one) and — REVISING shopper 1 — no «מיון: » prefix; instead a visible `<label>` «מיון» before the select in `.ens-ch__sort` (the stock Shopify pattern). **Owner-admin**: create an «all» collection (handle `all`, manual sort) if he wants his own order on /collections/all. | Honest label + visible affordance; two lenses. |
| owner 8: two «הוסיפו להזמנה» per PDP (main + sticky) | **Keep** (P1: one button that follows the customer; the bar shows only when the main button has scrolled away). Explained in the artifact. | — |
| honesty 0 (major, owner-admin): deck light `compare_at_price` 199.90 in the DOM | **Owner-admin** (clear compare-at on the 4 variants); the skin keeps hiding it. | Store data, SPEC §9. |
| honesty 1: Kalles' sr-only «מחיר מבצע» on every non-sale price | **Apply** the skin rule that hides the sr-only label inside `hdt-price` on cards and the PDP price block. | A sale claim for screen readers on 26 non-sale products. |
| honesty 3: «מה שנדלק ראשון» reads as a rank | **Apply**: heading «ארבעה לפתיחה» in `templates/index.json` and the section default. | P4: no popularity claims; the four are an owner pick. |
| honesty 4 (major, owner-admin): featured frames with a foreign brand (LUMIÈRE) and unbacked numbers | **Owner content task** (the §9 image sheet flags them first). No theme change (P3). | — |
| honesty 5 (major, owner-admin): `info@elmsnest.com` has no MX record | **Owner action before publishing** (a mailbox for info@). The line stays as the owner chose (answer 3: email). Top of the admin list. | The promise is his to make good; the theme cannot. |
