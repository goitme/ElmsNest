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
