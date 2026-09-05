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
