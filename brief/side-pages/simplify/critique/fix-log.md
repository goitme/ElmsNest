# SIMPLIFY critique — fixer log (2026-09-05, deployed-render round)

Inputs: the skeptic-confirmed findings (shopper / qa / honesty / owner lenses), `review/LEAD-DECISIONS.md` (followed
wherever it names a finding; deviations are marked **DEVIATION** with the reason), `SPEC.md`. Every edit is an exact-match
replacement (each old string asserted unique before writing); `snippets/elmsnest-v2-core.liquid` and every Kalles file
untouched. JSON templates re-parsed after the edit; `python3 brief/lint.py theme` → `LINT OK (0 issues)`.

## Files changed (9)

| file | edit |
|---|---|
| `theme/templates/product.elmsnest.json` | `main-product-medias.mobile_media_layout` `"thumbnails"` → `"fraction"` (shopper 0 / owner 3, lead's ruling). `ens_noscript.text` wrapped in `{% if product.variants.size > 1 %}…{% endif %}` and its `form=` attribute corrected to `product-form-{{ section.id }}{{ product.id }}` (see qa 4 / qa 6 below). |
| `theme/sections/elmsnest-s-coll-header.liquid` | sort chevron `border-inline-end` → `border-inline-start` (down in RTL; geometry in a comment); visible `<label for>` «מיון» before the select (+ `id` on the select, + `.ens-ch__sort-label` rule); manual option relabelled «סדר החנות»; `@media (max-width:400px)` `.ens-ch__hero{min-block-size:calc(30svh + …)}` (+ vh fallback); header comment updated. |
| `theme/snippets/elmsnest-s-skin.liquid` | card title `--line-clamp-count:3` + `font-size:16px` (line 16); `hdt-price.hdt-price > .sr-only{display:none}` after the compare-at rule; no-JS thumbnail rail rule `.hdt-product-media .hdt-product-media__thumb hdt-slider-thumb:not(:defined) .hdt-slider__container{max-height:none;flex-wrap:wrap}` at the end of section 3. |
| `theme/templates/index.json` | hero `lead` → «מנורות שביל, קיר, גינה ומרפסת. אם מוצר לא מתאים למקום שלכם, נגיד את זה לפני שתזמינו.» |
| `theme/sections/elmsnest-v2-hero.liquid` | ≤900 px `.env2-hero__h1{font-size:clamp(40px,11.5vw,56px)}` (was 54/15.5vw/72); schema `lead` default = the same sentence as index.json (place order fixed: שביל, קיר, גינה ומרפסת). |
| `theme/snippets/elmsnest-s-pdp-terms-line.liquid` | line text gains «· עד הבית <bdi dir="ltr">29.90</bdi> ₪» after «משלוח חינם לנקודת איסוף»; sync script resolves the main form by class inside its own `.shopify-section` (fallback: the sticky bar's `form=` id); header comment updated. |
| `theme/templates/collection.json` | `main-collection.image_ratio` `"portrait"` → `"square"` (`image_size` stays `true`). |
| `theme/sections/elmsnest-s-products.liquid` | both `image_ratio: 'portrait'` → `'square'`; grid wrapper `hdt-ratio--portrait` → `hdt-ratio--square` (the class is what sets the box ratio; the render param alone was a no-op — skeptic). `hdt-ratio--square{--ratio-percent:100%}` confirmed in Kalles' CSS. |
| `theme/sections/elmsnest-s-pdp-facts.liquid` | (a) build loop skips a bullet that equals an option value or names ≥2 values of the same option (whole tokens); (b) caption = bullet minus the code token, omitted when empty; giant loses `aria-hidden` (it is now the only accessible «IP65»); (c) chevron `rotate(-45deg)`→`rotate(45deg)` closed, `rotate(135deg)`→`rotate(-135deg)` open (geometry in a comment); header comment updated. |

## Finding by finding

| finding | applied | notes |
|---|---|---|
| shopper 0 / owner 3 — buy button below the fold (`product.elmsnest.json:214`) | **yes**, lead's lever only: `mobile_media_layout: "fraction"` | `image_ratio` untouched (never read by product-media.liquid; owner answer 2). `hdt_show_sticky_atc: hdt_show_always` (skeptic's option a) **not** applied — no lead ruling, and it is a P1/§8.2.9 change. Skeptic's option b (hide the single-variant picker) is Admin work. Honest target per the lead: price + pills in the first screen at 390×844; **re-measure `atcTop`** after deploy, do not promise `atcInFold`. |
| shopper 1 + qa 2 + qa (coll-header:147) — sort chevron points LEFT | **yes**: `border-inline-start` + `border-block-end` + `rotate(45deg)` | Logical properties kept (lint PHYS rule + Sense RTL app). Bottom-right corner (+1,+1) rotated 45° clockwise → (0,+1.41) = down. |
| shopper 1 (visible label) — revised by owner 7 / honesty 2 | **yes**: visible `<label>` «מיון» before the select; **no** «מיון: » prefix (the lead's revised ruling) | The `aria-label="מיון"` stays (SPEC §7.1 names it; same text as the label). No-JS: the page shows «מיון [select] [מיון button]» — the noscript button text is the SPEC's; left as is. |
| honesty 2 — «מומלץ» on /all names an order nobody made (`coll-header:100`) | **yes**, lead's version: relabel «סדר החנות» on every collection | Not the skeptic's `unless ens_all` wrap: the lead ruled the relabel (true on the manual collections AND the automatic /all), and the wrap needed a `sort_by=manual` redirect on top. Still four options → §11 unaffected. |
| shopper 3 + owner 5 — 2-line clamp swallows «10» → «0…» (`skin:16`) | **yes**: `--line-clamp-count:3;font-size:16px` | Per the lead's revised ruling (clamp experiment: square + clamp3 + 16px = 7.51 screens, 0 clipped). Line-height stays 1.3. |
| shopper 5 — hero lead «קטגוריה אחת בלבד» (`index.json:24`, hero:241) | **yes**, lead's smallest edit | Only «קטגוריה אחת בלבד — ו» removed; the four place names keep the menu order for §11. |
| shopper 6 — hero h1 three lines at 390 (`hero:194`) | **yes**, lead's size: `clamp(40px,11.5vw,56px)` (≈45 px at 390, ≈41 px at 360) | **DEVIATION from the skeptic** (30–34 px per SPEC §4): the lead ruled 40/11.5vw/56 explicitly. No `min-height` change (lead). «כשהשמש יורדת,» ≈ 230 px at 45 px → two lines again. |
| shopper 7 — PDP terms line lacks the door price (`terms-line:24`) | **yes** | Wrap = digits only (`<bdi dir="ltr">29.90</bdi> ₪`), matching the home strip / coll-header meta convention the skeptic asked to stay consistent with; the lead's variant put «₪» inside the bdi — same render. Comment cites `elmsnest-s-terms.liquid` ens_s1 + BRIEF §3 (not "coll_terms"). The drawer renders the same snippet → picks it up. |
| shopper 8 — 360×640 collection header fills the fold (`coll-header:118`) | **yes**, lead's version: 30svh at ≤400 px only | Skeptic's spacing trims and the 26svh idea not applied (lead: 30svh, nothing else). Expect ~38 px, not a full card row (skeptic's arithmetic); 360×640 is informational per §11. |
| shopper 9 — facts chevron points RIGHT (`facts:200`) | **yes**: logical pair, `rotate(45deg)` closed / `rotate(-135deg)` open | Kept logical borders (lint PHYS rule), not the skeptic's physical `border-right/bottom`; same geometry result, verified in the comment. `margin-block-end` nudges and transitions kept. |
| qa 4 — sticky sync never observed (`terms-line:27`) | **yes** — **DEVIATION from LEAD-DECISIONS ("no theme change")** | The lead's ruling predates the skeptic's proof: the deployed main form id is `product-form-template--…__main-product<id>` (mirror pdp-path line: `id="product-form-template--21567616745646__main-product9197362413742"`), so `document.forms['product-form-main-product…']` is `undefined` and the listener never attached — the live sticky button adds the initial variant whatever pill is chosen. Fixed the lookup only (by class inside the block's own section, the elmsnest-s-pdp-unit pattern; fallback = the sticky bar's `form=` attribute); listener body and the sticky id (`form-product-sticky<id>`, correct) untouched. **Same wrong id was in the `ens_noscript` select's `form=`** (mirror: `<noscript><select name="id" form="product-form-main-product9197362413742">` vs the real id) → the no-JS select was orphaned and its choice never posted; corrected to `product-form-{{ section.id }}{{ product.id }}` in the same string. Post-deploy: confirm `section.id` resolved inside the `_liquid` block (grep the mirror for `form="product-form-template--`), then run the live pill-click check the critic describes. |
| qa 3 — no-JS desktop thumbnail rail collapses (`skin:73`) | **yes** | Hook = `hdt-slider-thumb:not(:defined)` (lead); declarations = the skeptic's `max-height:none;flex-wrap:wrap` (the real clamp is `max-height:10rem`; `display:grid` / `transform:none` were inert). Also unclips media 5–6 on phones. Placed in skin section 3, not under the sticky-bar comment. |
| shopper 4 + qa 6 — one-variant picker / one-option no-JS select (`product.elmsnest.json:112`) | **yes**, theme half | Guard is `product.variants.size > 1` (skeptic's betterFix) rather than the lead's `has_only_default_variant`: it subsumes it (a default-variant product has one variant) and removes the one-option select **now**, before the owner removes «צבע אור». Admin half → owner report. **Consequence:** `verify.json` `noscriptSelect` will be `false` on pdp-path; SPEC line 347 must read "present when variants.size > 1". |
| honesty 1 — sr-only «sale price» on every non-sale price (`skin:23`) | **yes**, skeptic's single unscoped rule | Covers cards, PDP price block, related cards and the cart-drawer line (the lead's card+PDP scope missed the drawer). The CSS comment avoids the Hebrew word (lint's sale-token rule). |
| owner 0 — portrait crop cuts the owner's square images (`collection.json:23`) | **yes**: square in the template, both render params and the wrapper class | Not `adapt` (invalid value) and no `object-fit:contain` CSS (letterboxes). |
| owner 1 — facts `<dl>` repeats the variant options (`facts:225`) | **yes**, in the build loop as the skeptic advised | Checked after the label split and the trailing-period trim, so «אורך: 7 מ׳ / 50 נורות» matches by `val`; ≥2 hits counted per option (so «לבן חם 3000K» survives, «לבן חם, לבן קר, כחול או צבעוני» drops); whole-token match on space-padded text with «,» and «·» → spaces; one-value options skipped. `prev_label` dedup handles a `<dt>` whose rows all drop. **Render-check the rope light after deploy**: expected rows = «הפעלה | אוטומטית בחושך» only; path and deck unchanged. |
| owner 6 — «IP65» numeral + caption «עמידות IP65» (`facts:218`) | **yes** | `gcap = gsub \| remove: giant \| strip` (computed after the row loop so the `t == gsub` row suppression still works); caption omitted when empty; `aria-hidden` dropped from the giant so screen readers still get the rating. |
| owner 8 — two «הוסיפו להזמנה» (`product.elmsnest.json:241`) | **no change** (lead: keep; P1 / §8.2.9 / §9 test) | Report wording: one submit that follows the customer; hidden until the main form scrolls out; no second quantity control; same variant id (now actually synced — see qa 4). |
| owner 4 — sticky bar painted over the pills in full-page PNGs (`shoot.js:47`) | **not a theme file** | The lead already applied the hide-for-fullPage rule in `verify-mirror.js` (commit 7be2997); the pdp-* PNGs on disk pre-date it. Needs the re-shoot (`verify-mirror.js --pages=pdp-rope,pdp-path,pdp-deck`) before `build-owner-page.py`, not an edit. |

## For the lead — SPEC.md lines the applied edits put out of contract (not edited by the fixer)

- line 121 (§5.1): card title «17/1.3 … clamped 2 lines» → 16/1.3, clamped 3 lines.
- lines 183–184 (§5.5) and 232 (§7.2): `hdt-ratio--portrait` / `image_ratio: 'portrait'` / `"image_ratio":"portrait"` → square.
- line 193 (§6.1): the `lead` string → «מנורות שביל, קיר, גינה ומרפסת. אם מוצר לא מתאים למקום שלכם, נגיד את זה לפני שתזמינו.»
- line 227 (§7.1): `manual` «מומלץ» → «סדר החנות»; add the visible «מיון» label.
- lines 251, 277, 284 (§8): the main form id is `product-form-{{ section.id }}{{ product.id }}`; the noscript block is guarded by `variants.size > 1`; the sync script resolves the form by class.
- line 260 (§8.1): `"mobile_media_layout":"thumbnails"` → `"fraction"`.
- line 282 (§8.2.8): the terms line gains «· עד הבית <bdi dir="ltr">29.90</bdi> ₪ ·».
- §8.2.2: caption = the bullet with the code token removed (omitted if empty); the `<dl>` skips option-value rows.
- line 347 (§11): `noscript select[name=id]` present **when variants.size > 1**.
- §4 «Mobile display 30–34 px»: the hero h1 is now ≈45 px at 390 (lead's 40/11.5vw/56); either amend the number or keep the exemption the lead chose.

## Post-deploy checks to run

1. `atcTop` on the three PDPs at 390×844 / 360×640 (target: price + first pill row in the fold).
2. Mirror grep: `form="product-form-template--` in the noscript select (proves `section.id` resolved in the `_liquid` block) and the live pill-click → sticky `input[name=id]` check from the qa finding.
3. Rope PDP facts: `<dl>` rows and the caption («עמידות» under IP65, no «IP65» twice).
4. /all: screens ≤ 8 (clamp experiment predicts 7.51 with square + clamp3 + 16px), 0 clipped titles, no cut slogans.
5. Sort pill: chevron down; the «מיון» label before it; facts summary chevron down/up.
6. JS-off desktop PDP: six thumbnails in the rail; JS-off mobile: 6 thumbs on rope/path (two rows).

## Lint (last lines of `python3 brief/lint.py theme`)

```
  .. templates/index.json: section "ens_products" type elmsnest-s-products: no schema dumped in theme-src — settings not checked
  .. templates/index.json: section "ens_fit" type elmsnest-s-fit: no schema dumped in theme-src — settings not checked
  .. templates/index.json: section "ens_terms" type elmsnest-s-terms: no schema dumped in theme-src — settings not checked
  .. templates/product.elmsnest.json: section "ens_pdp_facts" type elmsnest-s-pdp-facts: no schema dumped in theme-src — settings not checked
  .. templates/product.elmsnest.json: section "ens_related" type elmsnest-s-products: no schema dumped in theme-src — settings not checked
LINT OK (0 issues)
```
