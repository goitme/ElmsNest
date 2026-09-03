# Collection page — the integrator's fix round (2026-09-03)

Input: `CRITIQUE-lead.md` (LEAD-01 closed, two corrections), `CRITIQUE-creative.md` (14),
`CRITIQUE-typographer.md` (13), `CRITIQUE-qa.md` (15). All four read in full before anything was
touched. Nothing settled by the lead was re-litigated: the narrow row was not moved, CREATIVE-06 was
not "fixed" (it is refuted — `env2-coll-scene__narrowlink` = 1 on all five mirrors after this round
too), and the scene's narrow label is still unit-neutral.

Everything below was **measured on the deployed dev-theme render**, re-mirrored after the last deploy,
with the real Frank Ruhl Libre and Heebo faces injected. Scripts are in
`brief/side-pages/collection/fix/`; the renders they produced are in `fix/after-sl/` (1440 viewport
slices, no 16,384 px ceiling), `fix/after-fold/` (five URLs × four phone sizes), `fix/before-sl/`
(the same slices shot before the round) and `fix/base-sl/` (the homepage and product-page baselines).

---

## 1. Deploy log

Seven files, one `themeFilesUpsert` call each, into
`gid://shopify/OnlineStoreTheme/154726400174` (UNPUBLISHED). `userErrors` was empty on every call.
Verified by **checksum, not by byte count**: Shopify's GraphQL block string strips the file's final
newline, so the deployed `checksumMd5` is compared against `md5(local file with the trailing newline
removed)` — the two agree exactly on all seven.

| # | file | size | deployed `checksumMd5` = local md5 |
|---|---|---|---|
| 1 | `snippets/elmsnest-v2-coll-glyph.liquid` | 10,471 | `844240540c7c3bcf75b70e188417e23c` |
| 2 | `snippets/elmsnest-v2-coll-rail.liquid` | 23,161 | `0b6560887d5542ae65e07d4419b160e9` |
| 3 | `snippets/elmsnest-v2-ground-collection.liquid` | 11,778 | `7188b3aacc829c6b331524c9bd349eb8` |
| 4 | `snippets/elmsnest-v2-pdp-card.liquid` | 14,559 | `6c9b71671c6317c9bab1af4c55ebf924` |
| 5 | `sections/elmsnest-v2-coll-scene.liquid` | 51,429 | `4ed6cb5b06fc1d5bfb8ae21e816c355d` |
| 6 | `sections/elmsnest-v2-coll-ruler.liquid` | 58,806 | `13cf430c68b456a26e8fbae7c8b86b9d` |
| 7 | `sections/elmsnest-v2-coll-bands.liquid` | 69,492 | `62f1b048bd5a453ca90c84dcc38fd56c` |

`templates/collection.json` was **not** changed: every fix is in a section, a snippet or a schema
default, so a merchant's saved settings survive. `python3 brief/lint.py` → **LINT OK (0 issues)**.
`git status` shows the seven theme files plus the five re-mirrored `index.html` — no commit was made.

Three of the seven were upserted more than once during the round (rail 2×, ruler 2×, bands 3×) as
findings were verified and corrected on the live render; the table gives the final state, and the
local repo is byte-identical to it.

**Follow-up deploy (QA-02, same day, one file).** `sections/elmsnest-v2-coll-scene.liquid` was upserted
twice more while QA-02 below was worked: once with the lead's prescribed `.8` photograph scale
(`ca74f152e15b6e2a19db98d07874979e`, 52,664 bytes) and once with the measured replacement that shipped —
the 472 px cap — at **`0787eea1023baacc782ddb3dc53d7f5b`, 53,929 bytes**, `userErrors` empty, checksum
verified against `md5(local file with the trailing newline removed)`. No other file was touched; the
inline style, the schema and `templates/collection.json` are unchanged, so merchant settings survive.
`python3 brief/lint.py` → **LINT OK (0 issues)**. All five URLs re-mirrored and re-shot after it.

---

## 2. Finding by finding

Severity is the critic's own. "Closed" means measured on the deployed render with the critic's own
method, at the critic's own viewport.

### The blocker

| id | sev | what changed | evidence it is closed |
|---|---|---|---|
| **QA-01** | blocker | `elmsnest-v2-coll-scene`. The tag was pinned at a per-cent of the **photograph** while the type block's content is bottom-set inside `photo − 84px` and rises as the viewport shortens; a constant reserve could not close it either, because the tag's own height is what varies (44 px on wall, 78 px on spot at 320). The two blocks are now coupled by **one number**: `--env2-scene-tagtop` (the tag's block-start, in px, resolved from the merchant's `pin_y_m` per-cent of `--env2-scene-hm`, floored at 72 px so it rises as the photograph shortens, ceilinged at `photo − 400px`), and `.env2-coll-scene--pinned .env2-coll-scene__type{padding-block-start:max(76px, tagtop + 72px)}`. contentTop ≥ tagTop + reserve **by construction**, at any viewport height and any per-cent. A `env2-coll-scene--pinned` class is emitted only when all four of the pin's facts are real, so a page with no pin pays nothing. | `fix/measure.js`, `getBoundingClientRect` on `.env2-coll-scene__tag` vs `.env2-coll-scene__h1` and vs the eyebrow, **5 URLs × 4 viewports = 20 combinations**: `tagOverH1:false` and `tagOverEyebrow:false` in all 20. Smallest clearances: **h1 +24.3 px** (spot 390×664), **eyebrow +8.7 px** (spot 390×664). Before: decor −1.9 / −17.5 at 664, spot −46.7 / −62.3, and at 320×568 four of five URLs overlapped the h1 (decor −68, spot −92). Folds: `fix/after-fold/coll-{decor,spot,…}-{390x844,390x664,360x640,320x568}.png`. |

**What QA-01 cost.** At **390×844 the fold is unchanged** — buy-control bottoms 717.6 / 717.6 / 741.3 /
671.7 / 717.6 px, the same numbers as before the round, and the LEAD-01 row still at top 515.3, height
44.0. At 390×664 and 360×640 the buy control moves down 25–55 px and stays inside the fold on all five
URLs (max 613.5 at 640). At **320×568 it now lands 26–68 px below the fold on decor, path, wall and
spot** (611 / 611 / 594 / 599 against 568); on `/collections/all` it is still inside (524).
That is a deliberate trade and it is the only regression in this round: at 320×568 the photograph
(78 svh = 443 px), the type block (310–359 px of content) and the card (162–208 px) cannot all fit
above 568 px at **any** tag position — before this round spot's buy control landed at exactly 568.0,
i.e. on the fold line, and only because the tag was printed across the h1. The binding fold
measurement in `WINNING-SPEC` §4.1 n-n 1 and §7 check 1 is 390×844 (`< 800 px`), and it is met with
59–128 px to spare. Reported to the lead as an open item, not hidden.

### QA-02 — the regression QA-01 left, and what actually moved it

| id | sev | what changed | evidence |
|---|---|---|---|
| **QA-02** | blocker (partly closed) | `elmsnest-v2-coll-scene`. The photograph's mobile height is no longer consumed raw: `--env2-scene-h` is derived once (`.env2-coll-scene{--env2-scene-h:var(--env2-scene-hm,78svh)}`) and **all four** consumers in the mobile block read it — the media box, the type block's `min-block-size`, and both arms of `--env2-scene-tagtop`. At ≤360 px it is **capped, not scaled**: `@media (max-width:360px){.env2-coll-scene{--env2-scene-h:min(var(--env2-scene-hm,78svh),472px)}}`. `min()` means the merchant's `image_height_mobile` is still the number in charge and is never exceeded. | 5 URLs × 4 viewports on the deployed render. **360×640 gains 27.2 px on all five** (decor 613.5 → 586.3, path 588.0 → 560.8, wall 582.1 → 554.9, spot 563.7 → 536.5, `/all` 558.5 → 531.3), all inside the fold. **390×844 and 390×664 are byte-identical to pre-round** (718 / 718 / 741 / 672 / 718 and 607 / 577 / 601 / 557 / 577; photograph still 658.3 and 517.9 px). **320×568 is untouched** — photograph back at its original 443 px. `tagOverH1` / `tagOverEyebrow` **false in all 20**; narrow row **44 px and in fold in all 20**; no horizontal overflow; `Liquid error` = 0 in all five mirrors. |

**Why the lead's first prescription was replaced.** The ruling was to shrink the photograph by `.8` at
≤360 px, on the arithmetic that 78 svh → 62.4 svh returns ~89 px at 568. Measured, it returned **zero**:
the buy control sat at the *same pixel* at 320×568 with the photograph at 443, 416, 399, 354 **and
221 px**. The photograph is not in the chain at that height. `--env2-scene-tagtop`'s ceiling is
`max(72px, photo − 400px)`, so below a 472 px photograph the ceiling *is* the 72 px floor, the tag band
is a constant `72 + 72 = 144 px`, and `min-block-size: photo − 84px` (270 px at `.8`) is far under the
type block's real 468–480 px of content — the block is content-sized, not photograph-sized. At 320×568
the photograph is already 443 px before anything is done to it, so any scale there only slides the copy
off the picture onto the veil and buys nothing. **472 px is the exact height at which the ceiling
reaches the floor** — the last pixel that is still load-bearing — which is why the shipped rule caps
there instead of scaling. It is scoped to ≤360 px because 78 svh is over 472 px on a 390 phone too
(658 px at 390×844, 518 px at 390×664), where the ceiling is genuinely above the floor: an
unconditional cap was measured and would have collapsed the 390×844 photograph to 472 px and moved the
buy control 718 → 561 on decor, 741 → 555 on wall and 672 → 515 on spot — rewriting the fold the lead
and the creative director signed off.

### Majors

| id | sev | what changed | evidence |
|---|---|---|---|
| **CREATIVE-01** | major | **Ruling: keep `הכול` as the default and print the per-unit figure there** (the critic's second option), not "default to the median stop". Reasons: (a) a page that arrives pre-narrowed answers a question the visitor never asked, and every share and search snapshot would then show prices at one stop rather than the catalogue; (b) `/collections/all` has no stops at all, so a default-stop fix cannot reach the URL the critic also cites; (c) the per-unit figure is the column no competitor prints — printing it at `הכול` puts the page's one idea in the still instead of behind a tap. In `elmsnest-v2-coll-rail`, the `v--all` answer now also prints `≈X ₪ למטר ב־N מ׳`, derived from the **same variant whose price is printed** (the lowest-priced record, field 11), with the entry measure named so it cannot be read as a rate across the range. The rail cursor no longer parks at 0 when nothing is chosen (`opacity:0` at `#env2-stop-all`), so the default still no longer reads "zero metres". | Deployed render, `fix/after-sl/coll-decor-03.png`: the three rows that all read `מ־89.90 ₪` now read `1.5–12 מ׳ · מ־89.90 ₪ · ≈59.93 ₪ למטר ב־1.5 מ׳`, `7–32 מ׳ · מ־89.90 ₪ · ≈12.84 ₪ למטר ב־7 מ׳`, `5–8 מ׳ · מ־139.90 ₪ · ≈27.98 ₪ למטר ב־5 מ׳` — three distinct per-metre figures. `env2-coll-rail__per--entry` = 4 on decor, 5 on path, 0 where the rail is a price ladder (correct: there is no unit to divide by). |
| **CREATIVE-02** | major | **Ruling: authored copy, and the band ships only where a human wrote a line.** The generated sentence is deleted from the source — there is no code path left that assembles a quote from `min`/`max`. `§4.3`'s two authored quotes ship: decor gets `עשר נורות שמתנדנדות ברוח, ובוקעות מתוך הפרחים.` verbatim; path gets `בין המנורה הזולה ליקרה יש פי {ratio}. ההבדל הוא כמה מנורות מקבלים.` with **the ratio derived** from the collection's own `price_max / price_min` (§6.19 forbids a typed number, and §4.4's ladder deck prints the same figure two screens below, so the two can never disagree). Where no line exists — wall, spot, `/all` — the quote composition leaves the rotation and those bands take another composition. The box is gone: Kalles paints `<blockquote>` as a filled panel with a decorative mark, and the reset is explicit (`background:none`, `::before/::after{content:none}`, one gold hairline on the start edge). | `grep -c env2-coll-bands__quote`: **1 on decor, 1 on path, 0 on wall / spot / all**. Rendered quote HTML on path: `בין המנורה הזולה ליקרה יש פי <bdi>14</bdi>. ההבדל…` — and the span deck on the same page reads `פי 14` from its own derivation. Computed `background-color` on `.env2-coll-bands__quote` = `rgba(0,0,0,0)` at 1440 and 390. Composition sets after the change: decor `pair·scene·quote·dip`, path `pair·quote·dip·scene`, wall `pair·dip·scene`, spot `pair·scene·dip`, all `pair·scene·dip·wide` — **no repeat on any URL** (§4.3 n-n 1 re-verified; removing the quote had briefly produced two `pair` bands on path, which is why path's authored line was restored rather than dropped). |
| **CREATIVE-03** | major | **Root cause found, and it was not what the critic could see.** The §3.6.4 veil this section already wrote for the off-scale band was on `.env2-pdp-card__ph::after` — and `elmsnest-v2-core` owns `[data-lamp] .env2-ph::after` for the warm halo at the same specificity, later in the cascade. The veil had **never painted a pixel**. It is now on `::before` (which keeps the core's halo, painted above it in tree order), it covers **every** card photograph in every band, at `.46` and `.56` on the off-scale/area bands. The lit floor was also trimmed to `.90 / .92` by the CREATIVE-07 rule. | Pixel statistics over every band card photo box on wall / all / decor, `fix/cream.js`. wall band 01 right card: **(218,201,184) 69.4 % cream → (204,189,173) 36.7 % (veil still not painting) → (111,104,96) 0.00 %**. `/collections/all` band 04: (207,192,176) 38.7 % → **0.00 %**; (173,158,140) 22.1 % → 0.00 %; the 691 px birch (181,162,138) 26.1 % → 0.00 %. **Worst cream fraction anywhere on the three URLs: 0.51 %** (threshold r>200 ∧ g>190 ∧ b>170), against 38.7 % before. |
| **CREATIVE-04** | major | Judged from the renders first, then fixed the critic's own way — **removing what holds too little, not adding decoration**. (a) The named weakest screen is gone: an area band with a single lamp is now folded into the off-scale band, whose label *"not measured in metres"* is exactly as true of it (decor 5 bands → 4; `data-kind="off"` now carries 3 cards, and the §4.3 n-n 5 assertion still prints). (b) The generated-quote bands are gone from three URLs (above). (c) The vertical spend is cut about a third at every section boundary — 216 px → 148 px — and between bands, 132 px → 88 px. | Per-900 px-screen ink density (share of pixels above luminance 34/255), same script before and after, viewport-by-viewport so no screen is missed: **decor** median 5.3 → 5.3, worst screen **1.3 → 1.9**; **path** 5.2 → 3.8, worst 2.4 → 2.6; **wall** 13.4 → 14.0; **spot** 5.0 → **8.9**, worst 1.7 → 2.4; **all** 8.4 → **12.3**, worst 1.9 → 2.1. Heights: 10,673→10,870 · 12,803→12,447 · 8,776→8,385 · 9,856→9,470 · 18,697→**16,623**; five URLs together 60,805 → 57,795 px (−5.0 %). Decor's weakest screen (`before-sl/coll-decor-08.png`: a 95 px numeral, a 60 px heading and one card on a black field) no longer exists. **Partly closed — see §5.** |
| **CREATIVE-05** | major | The ground ramp was spent by 5,000 px, so from there down every collection was one flat near-black field (5,700 px of it on decor, 13,700 px on `/all`). It now runs to **9,800 px** with seven stops. It starts at `--env2-sky-2` (`#0f1a2f`), **not** at sky-1 as the critic asked: the scene's veil's own last stop is `#0f1a2f`, so sky-1 at the top would put a visible step across the foot of the hero on all five URLs. The descent the critic wanted is delivered by the length of the ramp, not by its first stop. | `snippets/elmsnest-v2-ground-collection.liquid`, deployed; `background-size:100% 9800px`. Visible in the slice sets: the ground still moves at screens 8–12 on decor and 10–16 on `/all`, where before it was `#020306` from screen 6 down. |
| **CREATIVE-06** | major | **Refuted by the lead; nothing done.** Re-verified anyway after this round's re-mirror. | `env2-coll-scene__narrowlink` = **1 on each of the five** mirrors; the narrow row measures top 515.3 / height 44.0 / inside the fold at 390×844 on all five. |
| **CREATIVE-07** | major | The core's dim floor (`brightness .22 / saturate .4`) is raised **on the collection page only** to `brightness(calc(.52 + .38·--lit)) saturate(calc(.72 + .2·--lit))`, in the page-scoped ground snippet, so the homepage and the product page keep the core's own value. The switch-on gesture survives (.52 → .90 is still a visible lighting) and the halo, pool and glow layers are untouched. | Computed filter on `[data-lamp] .env2-ph img` on all five URLs. The unlit state is no longer the "featureless brown blur": the same firefly frame that measured mean luminance 18/255 now sits at .52 of its own value with its saturation at .72. The **reduced-motion branch is intact** — measured separately: under `prefers-reduced-motion: reduce`, 15 lamps, `notLit:0`, **0** transitioning elements inside `[id^=env2-coll]`; under `no-preference`, 13 of 15 unlit on arrival and 142 transitioning. |
| **TYPOGRAPHER-01** | major | `.env2-coll-scene__h1b{display:block}` → `display:inline`. The two-tone headline is a colour change, not a line break; `text-wrap:balance` on `.env2-h` starts working again. | Line boxes measured with the real faces, 1440 in a 640 px measure (critic's own method): **wall `תאורת קיר` 208/107 → one line, 441 px**; path 583/158 → 413/486; **spot 250/627/165 → 250/378/579**; decor 529/332 → 529/664. At 390 in a 350 px measure: wall 95/49 → one line, 201; spot 114/286/75 → 294/264. On all four titled URLs `glowAlone:false` — **the glow word is never alone on its line any more**, which is the `ניידת` orphan the lead referred to the typographer and the typographer ruled must not ship. |
| **TYPOGRAPHER-02** | major | The critic's prescribed fix (`max-width:62ch`) was already in the file — what they measured at `max-width:none` was the `__desc` wrapper, not the paragraph. The real defect (76 Hebrew characters to the line, because Hebrew glyphs are far narrower than the `ch` unit's zero) is fixed at the value that produces the effect they asked for: `max-inline-size:50ch`. | `.env2-coll-scene__p` box width **1053 px container / 529 px line → 461 px** at 1440 and 350 px at 390, on all five URLs; the measure now sits inside the 640 px h1 column above it instead of jumping outward. |
| **TYPOGRAPHER-03 / QA-02** | major | Both pin labels are product **names**, so both leave the tracked kicker style: scene tag and band pin name → **13 px Heebo 400, letter-spacing .02em, `text-transform:none`**, and the band name drops the `env2-kicker` class entirely. The band tag also stopped collapsing (a zero-width pin plus a wrapping name shrank the tag to min-content — `inline-size:max-content` restores the intent), and the name is now the product's **first three words**, the same rule the scene tag has always used, instead of a 54-character title clipped with an ellipsis. | Computed: `.env2-coll-scene__tagname` 11.5 px/1.84 px → **13 px / 0.26 px / none**. `.env2-coll-bands__pinname` 11 px + `text-overflow:ellipsis` + 31 % shown → **13 px, `clipped:false` on all ten tags across five URLs at 1440, 390 and 320**. Rendered names: `גרילנדת כדורי קריסטל`, `מנורת שביל סולארית`, `מנורת קיר LED`, `מנורת גינה דו־ראשית`, `פנס קמפינג טלסקופי`, `מנורות סולאריות למדרגות` — whole phrases, no `…`. |
| **TYPOGRAPHER-04** | major | In `price` mode both labels that point at the rail now say what the rail is: eyebrow → `המקום — והתקציב` (new `eyebrow_price` setting, so a merchant can still override), and the h2 defaults to `מה נכנס לתקציב?` on **spot** as well as wall, because spot's rail is the same budget ladder and the beam data does not exist (§4.2's own conditional). The second label the critic quoted — `אל הסרגל — לפי מידה ←` — is retired altogether (QA-05). | Read from the deployed DOM: wall **and** spot now carry eyebrow `המקום — והתקציב`, h2 `מה נכנס לתקציב?`; decor and path unchanged (`המקום — והמידה` / `כמה מטרים של אור?` / `כמה נקודות אור לאורך הדרך?`). |
| **QA-03** | major | Evidence gap, not a page defect. All five mirrors were re-taken after the last deploy of this round. | `stat` on the five `index.html`: all five written after the final upsert; `Liquid error` = **0** on every one. |
| **QA-07** | major | `elmsnest-v2-pdp-card` gains an optional `heading_level` (default 3, so the PDP related row and every band are untouched); the scene passes `heading_level: 2`, and the scene card's title is the section's `h2`. | Heading dump inside `[id^=env2-coll]`, all five URLs at 1440 and 390: `jumps: []`. The old `1 → 3` is gone; one `<h1>` per URL, zero `sr-only` h1s. **The product page is byte-identical**: fresh mirror + shot of `/products/solar-crystal-ball-string-lights` against the pre-round render — desktop 2880×16984 and mobile 780×17976, `ImageChops` bbox `None`, MAD `0.000000`, **0 of 48,913,920 and 0 of 14,021,280 pixels** differ. |

### Minors and nits fixed

| id | sev | what changed | evidence |
|---|---|---|---|
| **CREATIVE-08** | minor | The scene tag takes the scrim the page already owns (`rgba(5,8,14,.55)` + 8 px blur) instead of a second opaque chip; the band pin tag takes the same surface; both print a short name, never a cut one. | Computed background on both tags; the ellipsis is gone from all ten band tags (above). |
| **CREATIVE-14** | nit | `.env2-coll-glyph__cap` 11.5 px → **13 px** (tracking eased to .1em so the line still reads as a caption). | Computed `font-size:13px` on all five URLs. |
| **TYPOGRAPHER-05** | minor | The ledger measure takes a fixed cell aligned on its end edge (`display:grid; clamp(46px,4.6vw,68px) auto`) so `9.5` and `10` no longer put a 9 and a 1 at the same x, and `מ׳` forms its own column. | `fix/after-sl/coll-decor-10.png`: the 10 · 11 · 12 · 13 · 22 · 32 column is right-aligned with the unit stacked beneath a single x. |
| **TYPOGRAPHER-06** | minor | The ledger rows are capped at `min(100%,960px)` and the terms ledger + its head at `min(100%,1120px)`, so the ~710 px void between a name and its price inside one 56 px row is gone. | Same crop; the price now sits within ~300 px of the name at 1440. |
| **TYPOGRAPHER-07** | minor | On the phone the rail price takes the end column the desktop row already has (`margin-inline-start:auto`) and the per-unit line takes its own row. | The four prices in a decor rail row now share one inline-end edge at 390 instead of scattering across 19 px. |
| **TYPOGRAPHER-09** | minor | The three lamp names under a `/collections/all` place entry are three block lines, not a middot list whose separator is weaker than the en dashes inside the names. | `.env2-coll-ruler__placename{display:block}`, three per entry in the deployed markup. |
| **TYPOGRAPHER-13** | nit | The ruler caption stops repeating the numeral 40 px above it: `7 דגמים בקולקציה…` → `דגמים בקולקציה · 4 מהם נמדדים במטרים`. | Read from the deployed DOM on all five. |
| **QA-04** | minor | Both pin anchors have a collapsed border box, so the ring is moved onto the tag (`:focus-visible .env2-coll-scene__tag` / `.env2-coll-bands__pintag`, `outline:none` on the anchors). | Two rules per section, deployed; the ring now paints round the 204×44 tag instead of an 8 px square beside it. |
| **QA-05 / TYPOGRAPHER-08** | minor | The scene offers **one** door to the ruler: the older `אל הסרגל — לפי מידה ←` renders only when the LEAD-01 row is switched off (`narrow_label` blank). | `a[href="#env2-coll-ruler"]` inside `#env2-coll-scene` = **1** on all five URLs at 1440 and 390 (was 2). |
| **QA-06** | minor | The `role="group"` accessible name is a name again: in price mode `מחיר כניסה — עד כמה?` (new `question_aria` setting); the twelve-word instruction stays as the visible copy. | `aria-label` read on all five: decor `כמה מטרים צריך להאיר?`, path `כמה נקודות אור צריך השביל?`, wall = spot = `מחיר כניסה — עד כמה?`, all = none (correct — no radios there). |
| **QA-09** | nit | `aria-hidden="true"` on `.env2-coll-glyph__cap`; the svg's `aria-label` already carries the fact. | Attribute present on all five URLs. |

### Deliberately left, with the reason and the owner

| id | sev | why it is not fixed here | who takes it |
|---|---|---|---|
| **CREATIVE-03 (the deeper half)** | major | The critic's first choice was to route the six frames through the glyph plate. That means adding them to the never-use ledger in `snippets/elmsnest-v2-pdp-image.liquid`, which is **shared with the product page** — and this round's contract is that the PDP render does not move a pixel (it does not: MAD 0.000000). A second, collection-only image ledger would be a second source of truth for the same six pictures. So this round takes the frames to night by measurement (0.00–0.51 % cream) and hands the "should these products show a photograph at all" question to the owner with the PDP. | lead + owner |
| **CREATIVE-09** | minor | `/collections/ספוטים` has no photographic anchor: six of six cards are the glyph plate and the band-02 scene is a studio render. Using the collection's own `featured_image` as that band's scene is a `scene_image` picker on a band block — a template/content decision, and the same photograph is already the URL's hero, so the page would show it twice within two screens. Needs an art decision, not a code change. | lead |
| **CREATIVE-10** | minor | `/collections/all` opens with decor's photograph because it owns none of its own; the fix is to give the catalogue its own hero image (an `image_picker` setting that already exists — `image`). It is a content decision and one upload. | owner |
| **CREATIVE-11 / TYPOGRAPHER-10** | minor | Real, and it was blocking this round's own judgement, so it is fixed **in the tooling rather than the page**: `fix/slices.js` shoots viewport-by-viewport and has no 16,384 px ceiling, and every density and ink number in this report comes from it. `brief/shot-http.js` still writes a DPR-2 full-page PNG that goes white below 8,192 logical px; changing the shared shooter is the lead's call because every other page's evidence was taken with it. | lead |
| **CREATIVE-12** | minor | The middle of the page has no scale peak; the terms numerals render 66 px here against 101 px on the homepage. Restoring them is a shared-section decision (the same component renders on the homepage), and giving one band a genuinely enormous element is composition work, not a fix. | creative + lead |
| **CREATIVE-13** | minor | The wall price stops are 99.90 / 109.90 / 129.90 / 159.90 / 219.90 — two of them ten shekels apart — because the stop set is the union of the collection's **real entry prices**, thinned by index (§4.2: never a typed budget). Rounding them to `עד 120 · עד 160 · עד 220` would be four typed numbers, which §6.19 forbids; drawing each row's full range as a bar is already what price mode does. The right fix is a thinning rule that spaces stops by value rather than by index, which changes the rail on two URLs and wants the creative director's eye on the result. | lead |
| **TYPOGRAPHER-11** | nit | `כ־` instead of `≈` would have to change `.env2-pdp-card__unitprice`, which renders on the **product page**; that render is frozen this round (and is now proven identical). The `≈` stays inside the `<bdi>`, which the lead already ruled correct. | lead, with the PDP round |
| **TYPOGRAPHER-12** | nit | Normalising the en dash inside merchant titles (`| replace: ' – ', ' — '`) rewrites Shopify data at render time in seven places; it is a house-voice decision that should be taken once, for every template, not introduced on one page. | lead |
| **QA-08** | nit | Announcing the *consequence* of a stop change needs either JS (which §3.4 forbids for the narrowing) or an `aria-describedby` on every label pointing at the rail foot — which makes a screen reader read a 25-word sentence on each of seven stops. Worse than the silence. | lead |
| **QA-10** | nit | The goodnight photograph's `alt=""` is correct as it stands: the outline word `לילה טוב` carries the meaning and the image is decoration behind it. Recorded as a deliberate decision rather than a default. | closed by decision |

### Rulings where two critics pulled opposite ways

1. **CREATIVE-02 (keep an authored quote) vs CREATIVE-04 (kill the quote band for density).** The quote
   ships where §4.3 authored a line and nowhere else. It costs path 1.4 points of median ink; it buys
   the page its only "tiny vs huge" scale contrast — which is the thing CREATIVE-12 says the middle of
   the page lacks — and the only human sentence anywhere on it. Deleting it everywhere would have left
   decor and path with no authored voice at all, which is the round-0 charge in another form.
2. **CREATIVE-04's "pull the ledger up above the bands".** Not done. §4 fixes the page order (gate →
   instrument → desire → the fourteen-times screen → the measure → terms → close); putting the measure
   table straight after the ruler stacks two hairline-row screens and delays the only photographic
   screens on the page. The density complaint is answered by removing empty ground and empty bands,
   not by reshuffling the spec's order.
3. **CREATIVE-01's two options.** Ruled above: `הכול` stays the default and gains the per-unit column.
   The "all" state stays honest — nothing is pre-narrowed, nothing is hidden, and the figure printed
   belongs to the same variant as the price printed beside it.

---

## 3. The five URLs, final measurements

Deployed render, re-mirrored after the last upsert. Heights from `brief/shot-http.js`; `Liquid error`
by grep on the mirrored `index.html`.

| URL | height (1440) | height (390) | Liquid errors | h1 / sr-only h1 | heading jumps | horizontal overflow @390 / @320 | tap targets < 44 px in our sections |
|---|---|---|---|---|---|---|---|
| `coll-decor` | 10,870 | 11,313 | 0 | 1 / 0 | none | none / none | 0 |
| `coll-path` | 12,447 | 15,173 | 0 | 1 / 0 | none | none / none | 0 |
| `coll-wall` | 8,385 | 8,716 | 0 | 1 / 0 | none | none / none | 0 |
| `coll-spot` | 9,470 | 9,820 | 0 | 1 / 0 | none | none / none | 0 |
| `coll-all` | 16,623 | 21,743 | 0 | 1 / 0 | none | none / none | 0 |

**The fold at 390×844**, all five: the eyebrow, the collection's own `h1` in two tones, the deck, the
approved suits/doesn't-suit pair, the counts hairline, the LEAD-01 narrow row (top 515.3, height 44.0,
inside the fold on all five) and the pinned card with a real price and a live buy control — bottom
edge **717.6 / 717.6 / 741.3 / 671.7 / 717.6 px**, all under §4.1's 800 px, all unchanged by this
round. The pinned lamp's tag clears the eyebrow by 87–174 px. `fix/after-fold/*-390x844.png`.

**Ink density per 900 px screen** (share of pixels above luminance 34/255), viewport-by-viewport, same
script for the baselines:

| page | median before → after | worst screen before → after | height before → after |
|---|---|---|---|
| homepage (approved baseline) | 28.9 | — | 8,506 |
| product page (approved baseline) | 12.6 | — | 8,492 |
| `coll-decor` | 5.3 → 5.3 | 1.3 → **1.9** | 10,673 → 10,870 |
| `coll-path` | 5.2 → **3.8** | 2.4 → 2.6 | 12,803 → 12,447 |
| `coll-wall` | 13.4 → 14.0 | 2.4 → 2.1 | 8,776 → 8,385 |
| `coll-spot` | 5.0 → **8.9** | 1.7 → 2.4 | 9,856 → 9,470 |
| `coll-all` | 8.4 → **12.3** | 1.9 → 2.1 | 18,697 → 16,623 |

**No-JS, re-run because QA asked for it.** `coll-decor` at 390×844 under reduced motion, JavaScript
disabled vs enabled, at three scroll depths: `ImageChops` bbox `None`, **MAD 0.000000, 0 pixels
differing by more than 8/255** at every depth. With scripting off: 12 prices rendered, 0 empty, 1
`POST /cart/add` form, 7 stop radios, 4 sort anchors, no horizontal overflow. The property that makes
the CSS-only ruler defensible survived every change in this round.

---

## 4. What this round did not touch

- `templates/collection.json` — unchanged; every fix is a section, a snippet or a schema default.
- `elmsnest-v2-core` — unchanged. The one core behaviour this round overrides (the `[data-lamp]` dim
  floor) is overridden **only** under `body.hdt-page-type-collection`.
- The product page — proven byte-identical, desktop and mobile.
- The homepage — it renders none of the seven files (`grep` for `env2-pdp-card`,
  `env2-ground-collection`, `env2-coll-` on `inventory/home/index.html` = 0).
- The three open core bugs in `core/REPORT.md` §9 — not this round's, not touched.

**One structural note the lead should see.** Four sections needed nothing but a padding value
(`-span`, `-ledger`, `-terms`, `-goodnight`) plus two row measures. Those six declarations were put in
`snippets/elmsnest-v2-ground-collection.liquid`, page-scoped at (0,3,1), beside the four belts that
already live there — one place to read the page's spacing decision and one place to revert it — rather
than re-upserting 137 KB of Liquid for one declaration each. The ruler and the bands carry the
identical values inside their own stylesheets because those two files were being rewritten anyway.
The values are the finding; the location is a call the lead may reverse.

---

## 5. Open items

**For the lead**

1. **320×568 — OPEN, accepted at ≤320 px, held at 360 px.** Ruled by the lead, not a bug and not a
   pending fix. The buy control lands **43 / 43 / 26 / 31 px** below a 568 px fold on decor, path, wall
   and spot; `/collections/all` is inside at 524.

   **The arithmetic.** At 320×568 the stack above the buy control is a **144 px tag band** (72 px tag
   floor, clear of the 60 px header, + 72 px reserve) + **310 px of copy** (eyebrow top 143 → narrow-row
   bottom 453) + **14 px** type padding-bottom, and then the card, whose button ends 144 px in — 611 px
   against 568. **The photograph contributes nothing to it**: proven by measuring the same pixel with
   the photograph at 443, 416, 399, 354 and 221 px (see QA-02). There is no slack in this file to find.

   **The four levers, and why each was rejected.**
   - *Tighten the tag reserve* (`--env2-scene-tagres` 72 → ~64 px): only ~9 px is available before
     spot's 63.2 px tag touches the eyebrow. It trades a blocker for a blocker, and does not reach 43.
   - *Drop the pin band at ≤360 px*: reclaims the full 144 px and closes all four — but that **is**
     QA-01's fix removed at that width. The same trade in another dress.
   - *Trim the scene card at ≤360 px* (axis caption + per-unit line, ≈40 px on decor): the per-metre
     figure is the strongest selling device on the page and the one no competitor prints. Losing it on
     every ≤360 px phone to buy 40 px against a 43 px deficit would **not even close decor**.
   - *Shrink the photograph* (the lead's first ruling): measured inert at this viewport for any factor.

   **What the visitor gets at 320.** The photograph, the title, the counts, the narrow row, the product,
   the price and the per-metre figure — and a 43 px scroll for the button. That is a scroll, not a
   failure. Note for the record that the **pre-round page only passed at 320 because the tag was
   printing across the h1** — spot sat at exactly 568.0 by virtue of the QA-01 bug, not despite it, so
   there is no earlier state to restore.

   **Acceptance boundary — treat as a contract.** **360×640 must stay inside the fold** (currently
   586.3 / 560.8 / 554.9 / 536.5 / 531.3 against 640, with 27 px returned by the QA-02 cap). Any future
   change that pushes 360×640 out of the fold is a **regression**, not a new trade. 320×568 is accepted
   as-is; 390×844 and 390×664 remain the signed-off measurements and are unchanged.
2. **CREATIVE-04 is partly closed.** The empty screens are gone and four of five URLs are shorter, but
   `coll-path`'s median ink fell 5.2 → 3.8 because it regained the authored quote band. Two things the
   metric cannot see: a hairline table (the ledger, the span ladder, the terms) scores 2–3 % however
   good it is, and this page is a night page — it will never reach the homepage's 28.9 %. If the lead
   wants a like-for-like target, it should be "no screen under 2 %", which is now met on 4 of 5 URLs
   (wall has one screen at 2.1 %, `/all` one at 2.1 %).
3. **The six cream frames.** Measured to 0.00–0.51 % cream by veil and grade. The critic's preferred
   answer — the glyph plate — needs the never-use ledger, which is shared with the frozen PDP.
4. **The shared shooter.** `brief/shot-http.js` still writes DPR-2 full-page PNGs that go white below
   8,192 logical px. Everything below that on every page in this project has been judged from renders
   that do not contain it. `fix/slices.js` is the replacement; adopting it is a project-wide call.
5. **CREATIVE-09, -10, -12, -13, TYPOGRAPHER-11, -12, QA-08** — listed above with reasons.

**For the owner**

1. `/collections/all` opens with the decor photograph because the catalogue owns no image of its own.
   One upload closes CREATIVE-10.
2. Six wall and spot products have only studio cut-outs on a cream ground. The page now takes them to
   night, but a night photograph of the lamp in place would sell them better than a graded cut-out —
   and the same six frames are what the product page shows.
3. `/collections/ספוטים` still has no photograph of a product anywhere on it: six of six cards are the
   honest illustration plate. That is a photography decision, not a design one.

---

## 6. The two questions

**Does this page let a phone visitor narrow the catalogue and buy?**
Yes. On a 390×844 phone the first screen carries the place, the collection's own name, a lit lamp
pinned in the photograph with its name and its real measure, a real price, a live buy control ending
at 672–741 px, and — since LEAD-01 — the question that leads to the ruler, at top 515 with a 44 px
target. One tap on a stop turns four ranges into four priced answers with a ₪-per-unit figure beside
each, and since this round the same figure is already printed **before** the tap, so the instrument
says something in the state the visitor arrives in. It all works with JavaScript disabled — proven
this round again at zero pixels of difference — and at 390×664 and 360×640, the sizes a real phone
with browser chrome actually reports, nothing overlaps and the buy control is still inside the fold.
At 320×568 the buy control is a short scroll away.

**Does it belong to the same store as the homepage and the product page?**
Yes, and more so than before this round. It uses the store's ground (now a sky that keeps descending
for 9,800 px instead of going flat at 5,000), the store's card (the very same file the product page
renders — proven pixel-identical), the store's price rule, its hairlines, its radius-0 discipline, its
gold-on-night palette and its Hebrew punctuation system. The two things that made it look like a
different shop are gone: the only opaque box on the page (a `<blockquote>` panel Kalles painted, which
held a sentence generated from `min` and `max`), and the cream studio cut-outs that sat on a `#070b15`
ground at 36 % cream pixels and now measure zero. What still separates it from the homepage is not
identity but density — this page is mostly hairlines and night, and it reads quieter than a page whose
second screen is a full-bleed photograph. That is the page's nature, and it is the one thing in the
creative director's list this round could only half answer.
