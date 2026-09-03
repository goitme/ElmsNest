# PDP v2 — integration, fix pass (2026-09-03)

Theme `gid://shopify/OnlineStoreTheme/154726400174` — **UNPUBLISHED**. Nothing was published, no product,
collection, page or metafield was written, and `templateSuffix` was not touched on any product (§8.1).
Four critiques were read in full: `CRITIQUE-creative.md` (3 blockers · 7 majors · 3 minors),
`CRITIQUE-shopper.md` (2 · 6 · 4 · 1), `CRITIQUE-typographer.md` (0 · 7 · 4 · 4), `CRITIQUE-qa.md` (0 · 4 · 5 · 1).

---

## 1. What was built

Every finding was reproduced first — on the served mirrors, with Playwright, with the two brand faces
served locally (see TYPOGRAPHER-01) — before anything was changed. Files below are the **deployed**
sizes reported by `themeFilesUpsert`.

| file | bytes | what changed |
|---|---:|---|
| `snippets/elmsnest-v2-bdi-range.liquid` | 2,995 | **new.** Wraps a `number–number` range in ONE `<bdi>`. ASCII digits are bidi class EN, so the en dash between two of them resolves RTL and `5–22 מטר` printed as `22–5 מטר`. |
| `snippets/elmsnest-v2-core.liquid` | 22,598 | the buy handler acknowledges a successful `/cart/add.js` on the page itself (label → `נוסף לסל`, control disabled 1.6 s) instead of leaving every visible response to the theme's drawer. |
| `snippets/elmsnest-v2-pdp-image.liquid` | 7,827 | new `ask` slot for §4.7's closing photograph (A 0 · B 1 · C 3 — never the hero's own frame); wall `small` moved 2 → 1 and index 2 (a supplier 2×2 contact sheet) added to the deny list. |
| `snippets/elmsnest-v2-pdp-card.liquid` | 9,270 | `kicker: 'none'` suppresses the card's place line when the caller already said it; `.env2-price__from` floored at 13 px (scoped, not on the shared class). |
| `snippets/elmsnest-v2-pdp-buybar.liquid` | 7,430 | ≤430 px: the thumbnail goes, the price steps down, the text column grows 96.8 → 168 px, so the selection mirror never truncates. |
| `sections/elmsnest-v2-pdp-stage.liquid` | 66,190 | authored h1 (`heading_map` + per-place pairs); the negative link decided like §4.2 decides; ATC floor at (0,2,0); 44 px radios; `role=radiogroup`; veil + local kicker scrim; 14 px desktop floor; paired-rail caption; `env2:pdp:stage` broadcast. |
| `sections/elmsnest-v2-pdp-fit.liquid` | 42,423 | the negative falls back to the place's own approved pair when the metafield is blank (gated on solar for the three that are only true on a battery); solar read from the product's own words; three bands — catenary / receding path / two beams. |
| `sections/elmsnest-v2-pdp-ledger.liquid` | 50,339 | receives the stage's picks (two-way binding); `role=radiogroup` + `role=radio`/`aria-checked`; per-unit column suppressed on a quantity ledger; price column pinned so the figures align; 14 px desktop floor. |
| `sections/elmsnest-v2-pdp-facts.liquid` | 37,141 | power source read from the description when the metafield is blank; ranges through the new isolator; a row that only repeats the giant numeral is dropped; the merchant description's h2/h3 demoted to h4/h5; giant at §3.2's own `clamp(96px,16vw,240px)`; `unicode-bidi:isolate` on the giant sub; 14 px `dt`. |
| `sections/elmsnest-v2-pdp-terms.liquid` | 18,675 | `text-align:end` removed from the deck. |
| `sections/elmsnest-v2-pdp-ask.liquid` | 32,061 | the closing screen is a full-bleed photograph on the §3.1 veil; CTA floors at (0,2,x); the §4.2 agreement re-derived the same way §4.2 now derives it. |
| `sections/elmsnest-v2-pdp-related.liquid` | 24,667 | `text-align:end` removed from the deck; passes `kicker: 'none'` to same-place cards. |
| `templates/product.elmsnest.json` | 13,260 | 16 ledger `row` blocks (graft A, handle-scoped); `heading_map` for the three archetypes; the `fit_link_label` override dropped; two calqued Hebrew lines rewritten. |
| `brief/shot-http.js` | — | harness: serves the real Frank Ruhl Libre and Heebo `.woff2` and fulfils the Google stylesheet request with `@font-face` rules for them. |

`python3 brief/lint.py` → **LINT OK (0 issues)** after every schema/template change.

## 2. Deploy log

Order: snippets → sections → template (DEPLOY.md). One file per call, GraphQL block string. Every call
returned `userErrors: []` except one, noted below.

```
snippets/elmsnest-v2-bdi-range.liquid    2995   ok
snippets/elmsnest-v2-pdp-buybar.liquid   7430   ok
snippets/elmsnest-v2-pdp-image.liquid    7488   ok   (7827 on the second pass, ask slot)
snippets/elmsnest-v2-pdp-card.liquid     9270   ok
snippets/elmsnest-v2-core.liquid        22598   ok
sections/elmsnest-v2-pdp-terms.liquid   18675   ok
sections/elmsnest-v2-pdp-related.liquid 24667   ok
sections/elmsnest-v2-pdp-ask.liquid     31942   ok   (32061 on the second pass, ask slot)
sections/elmsnest-v2-pdp-facts.liquid   37141   ok
sections/elmsnest-v2-pdp-fit.liquid     42423   ok
sections/elmsnest-v2-pdp-ledger.liquid  50189   ok   (50339 on the second pass, price column)
sections/elmsnest-v2-pdp-stage.liquid   65447   ok   (65558, then 66190 — kicker scrim, paired rail)
templates/product.elmsnest.json         FAILED  FILE_VALIDATION_ERROR "Invalid JSON"
templates/product.elmsnest.json         13260   ok
```

The one failure was mine and is worth recording: inside a GraphQL **block string** (`"""…"""`) no escape
is processed except `\"""`, so a JSON `\"` must be typed as `\"` and a JSON `\n` as `\n` — I had doubled
both, which produced a stray backslash before a quote and invalid JSON. Retyped with single backslashes;
accepted. Nothing was written by the failed call.

Then, for each of the three archetypes: `brief/mirror.py` against the dev preview, `brief/shot-http.js`
for the four PNGs, and the two Playwright probes re-run with the same method each critic used.

## 3. Finding by finding

Severities are the critics' own. "closed" means re-measured after the redeploy with the critic's method.

### Blockers

| id | sev | what changed | evidence it is closed |
|---|---|---|---|
| SHOPPER-01 | blocker | The stage↔ledger binding is now two-way. `apply()` in the stage broadcasts `env2:pdp:stage` on `document`; §4.4 listens, re-selects its quiet option and calls `paint(i,false)`, which never calls `driveStage` — so the two directions cannot loop. | Tapping rail stop 3 at 390: **A** stage `11 מ׳ / 60 נורות · צהוב` 109.90 → ledger `11 מ׳ / 60 נורות · צהוב` 109.90, `ledgerId 48880938614958 == barId`. **B** stage `4 יחידות` 679.60 → ledger `4 יחידות` 679.60. **C** stage `12W / אור קר 6000K · לבן` 252.90 → ledger identical, id `48675431776430`. Before: 5 מ׳/89.90, 1 יחידה/169.90, 6W/219.90. |
| SHOPPER-05 · CREATIVE-02 · QA-01 | blocker / major | Spine #2 has a device again. `custom.not_fit_for` stays the FIRST source; when it is blank the place's own approved pair (BRIEF §3) stands in — and only where it is literally true. The decor pair is a statement about purpose and needs no power test; the path, wall and spot pairs are only true on a battery charged by the sun, so all three are gated on solar, which is read from the product's own word `סולארי` when `custom.power_source` is empty (BRIEF §4 row 2: "power source from description"). Never a fifth negative: whatever the source, the string must match one of the four exactly or it is dropped. | `#env2-pdp-fit` innerText, A: `02 · מתי כן, ומתי לא … מתאים כדי ליצור אווירה — [knob] — לא מתאים כש־ צריך אור חזק — זו אינה מטרתה … לא נדלק. זו הנקודה. … כמה שמש המקום מקבל ביום?` B: the same shape with `המקום כמעט אינו מקבל אור יום`. C: still **choose** mode, no negative, no solar question — which is what §4.2 (C) demands of a mains wall light. `.env2-pdp-fit__half--no` present on A and B, absent on C, with and without JavaScript. |
| CREATIVE-01 · SHOPPER-11 | blocker / minor | The `<h1>` is authored. `heading_map` in the template carries §4.1's three lines; a product not in the map gets an authored pair for its place; only a product with no place at all falls back to `מתאים כדי …`. The suits phrase moved back to the kicker, where §4.1 puts it. | A `הערב מתחיל / מהכדור הראשון.` · B `הדרך הביתה / נדלקת לבד.` · C `קיר אחד. / שתי אלומות.` Kicker: `מרפסת ופינת ישיבה · מתאים כדי ליצור אווירה`. |
| CREATIVE-03 | blocker | **Partly closed, and partly refused with evidence.** What the archetype now changes: the h1, the fold's negative link, the fit band (catenary / receding path / two beams), the ledger's captions and its per-unit column, the wall's gallery frames, the rail's caption weight, and the closing photograph. What it cannot change is the *section order*: §8.1 fixes one shared `product.elmsnest.json` for all 27 products because `templateSuffix` is a property of the product and this round may not touch it. Reordering per archetype is therefore impossible without a live-store change. Section tops at 390 are no longer identical either — night starts at 1950 / 1901 / 1707 and the ledger at 2996 / 2953 / 2759. | offsets above; `env2-pdp-fit__band--hang` / `--path` / `--halo`, one per archetype. |

### Majors

| id | what changed | evidence |
|---|---|---|
| CREATIVE-08 · SHOPPER-02 · QA-03 · TYPOGRAPHER-06 | `.env2-btn{min-height:0}` in the layout's inline `<style>` is (0,1,0) and later in the cascade, so the floor is now stated at (0,2,x) in both sections. | `.env2-pdp-stage__atc` **52.0 px** at 390 and at 1440 on all three; `.env2-pdp-ask__start` and `.env2-pdp-ask__photo` **52.0**. Was 42.8. |
| SHOPPER-03 | The template's `fit_link_label` override is gone; the stage decides the label the same way §4.2 decides whether it has a negative. | fold link: A/B `למי זה לא מתאים ←`, C `איך בוחרים נכון ←`. |
| CREATIVE-04 · SHOPPER-04 · QA-02 | 16 handle-scoped `row` blocks in the template with §4.4's quoted captions. | `.env2-pdp-ledger__use` non-empty on 6/6 (A), 6/6 (B), 4/4 (C). |
| SHOPPER-06 | The facts section reads the power source from the product's own words when the metafield is blank, so a solar product's own bullets print. C stays silent about power (§3.7 / §6.7). | A's `dl` now carries `טעינה · סולארית`; C unchanged, and its `מה שלא כתוב` still names `מקור החשמל`. |
| SHOPPER-07 | The core acknowledges the add itself, before and regardless of the drawer. | after a stubbed `/cart/add.js`: label `הוספה לסל` → **`נוסף לסל`, `disabled: true`** → restored after 1.6 s, on all three. |
| SHOPPER-08 | `min-inline-size:44px` + inline padding on the radio. | wall body-colour radios **44 × 47.3** each. Was 21.3 and 33.0. |
| TYPOGRAPHER-01 | Harness fix, not a theme fix: `shot-http.js` serves `brief/assets/fonts/{FrankRuhlLibre,Heebo}-*.woff2` and fulfils the Google stylesheet request. Every render in this report is in the real faces. | 100 px probe: FRL 763.4 / Heebo 841.8 / monospace 902 (unequal ⇒ resolved). The `FRL Fallback` **metrics** are left alone — see §7, and the refutation there. |
| TYPOGRAPHER-02 | New `elmsnest-v2-bdi-range` snippet, applied to every `dd` value and every merchant fact block. | per-character reconstruction: `5–22 מטר` now prints `5–22`, `20–200 נורות LED` prints `20–200`, `כ־8–10 שעות` prints `8–10`, `כ־5–10 ס״מ` prints `5–10`. Was reversed in all four. |
| TYPOGRAPHER-03 | `text-align:end` deleted from `.env2-pdp-related__deck` and `.env2-pdp-terms__deck`. | computed `text-align: start` at 1440 on both, all three products. |
| TYPOGRAPHER-04 | A `@media (min-width:901px)` block raises the stage's caption/mirror/range/terms/photo-link to 14 px; ledger `__b`, `__pm`, `__jsnote` and facts `__dt` to 14 px. | text nodes under 14 px at 1440 fell from **80 → 47** (multi), 63 → 35 (single), 64 → 37 (wall). The remainder are the 11–11.5 px tracked kicker/eyebrow roles §4.8 itself specifies — QA-05's spec conflict, still the lead's to rule. |
| TYPOGRAPHER-05 | `.env2-pdp-card__price .env2-price__from{font-size:max(13px,.62em)}` — scoped to the PDP card, so the shared class and the homepage are untouched. | 11.78 → **13.0 px** at 390. |
| TYPOGRAPHER-07 · SHOPPER-10 | Under 430 px the bar drops its thumbnail and steps the price down; the text column goes 96.8 → **168 px**. | after picking stop 3: mirror `11 מ׳ / 60 נורות · צהוב` / `4 יחידות · צהוב חם` / `12W / אור קר 6000K · לבן`, `scrollWidth == clientWidth` on all three — the mirror never truncates. The title still clips, which is what the critic asked for ("if a clip is unavoidable, clip the title"). |
| QA-04 | The veil got one more stop (which also makes the wall's studio hero read as night — CREATIVE-05), and the kicker got a local scrim: the box is shrunk to its own words and the gradient reaches zero alpha inside that box, so it is a shadow and not an edge (§6.14). | same method — stage re-rendered with the copy transparent, background sampled inside the kicker's own box: **10.95 / 11.10 / 10.52 : 1** at the 95th percentile, **9.65 / 10.96 / 9.72** at the single brightest pixel. Was 3.71 / 4.00 / 2.75. |
| CREATIVE-05 | Wall image 2 (a supplier 2×2 contact sheet — four equal cells, §6.2) banned from every slot; `small` falls to 1. The strengthened veil takes the warm-grey studio hero to night. | `close`/`small` resolve to 1; the fold now reads night (see the desktop fold PNG). |
| CREATIVE-06 | Three bands, one per archetype: A the hung catenary, B a receding line of stops each smaller and dimmer, C two beams up and down. | `env2-pdp-fit__band--hang` / `--path` / `--halo`; crops in the scratchpad. |
| CREATIVE-07 · TYPOGRAPHER-15 | The suits phrase left the h1 (it is the kicker's, once) and the related cards no longer repeat the place kicker when they come from the same place. | `מתאים כדי` on multi: **5 → 2** occurrences in the body (the kicker and section 02's tag). Three identical gold card kickers: gone. |
| CREATIVE-10 | §4.7 now closes the page on a full-bleed photograph of the product's own light, on the §3.1 veil — the same device the page opens with, and never the same frame (a dedicated `ask` image slot). | `.env2-pdp-ask__bg img` present on all three, lit with and without JS. Lit-pixel fraction by quarter, multi: `.054 / .163 / .032 / .077`; wall: `.137 / .243 / .031 / .115` (was `.153/.238/.027/.094`). **Honest note: the metric barely moved** — the veil that keeps the copy legible also keeps the pixels dark. What changed is visible rather than measurable: see §6. |
| CREATIVE-09 | **Refuted.** The ask quote is not a filled box and carries no Latin ornament. | computed `background-color: rgba(0, 0, 0, 0)` on `.env2-pdp-ask__quote`; the CSS is a 1 px gradient hairline (`::before`, `inline-size:1px`); `grep` for `“` / `&ldquo;` in all three mirrors → **0**. The critique was written in an earlier run against an earlier build. |
| QA-06 | **Refuted in part, and fixed anyway.** The pair was never unnamed: the wrapper already carried `role="group" aria-labelledby` pointing at `צבע גוף` — the critic queried only for `fieldset,[role=radiogroup]`. But `group` never announces "1 of 2", so it is now `role="radiogroup"`. | `#env2-pdp-stage [role=radiogroup]` → 1, labelled by `env2-pdp-stage-quiet-label`. |

### Minors and nits fixed (one-line fixes, per the brief)

| id | change | evidence |
|---|---|---|
| TYPOGRAPHER-08 | The real cause was not the ₪: every row is its **own** grid, so a `max-content` column is sized per row. Flooring the last two columns pins the price column. | decimal-point x on every row of every product: **335.3 px**, identical. Was 267.1 vs 275.9 (and 12.5 px apart before the pass). |
| TYPOGRAPHER-09 | `לא צריך להיות.` → `לא חייבים.`; `מטרה שהתאורה ממלאת` → `תפקיד שהתאורה ממלאת` (both `lead` and `lead_choose`). | rendered h2 `עוד לא בטוחים? / לא חייבים.`; fit lead `לכל מקום יש תפקיד שהתאורה ממלאת…`. |
| TYPOGRAPHER-10 | `unicode-bidi:isolate` on `.env2-pdp-facts__giantsub`. | computed `isolate`. (`.env2-pdp-stage__cap` is a plain option value with no Latin tail on any of the 27; left as the lead's call — see §7.) |
| TYPOGRAPHER-14 | giant numeral `clamp(96px,13vw,230px)` → §3.2's own `clamp(96px,16vw,240px)`. | 187.2 → 230.4 px at 1440. |
| QA-07 | `product.description` demoted `<h2>→<h4>`, `<h3>→<h5>` before printing, and the scoped CSS restyles both. | heading census: the description's four headings are now `H4`/`H5`; no `H2` outside the eight sections. |
| QA-09 | `<ol role="radiogroup">` + `role="radio" aria-checked` on the six row buttons, kept in sync by `paint()`. | `[{'true/radio'},{'false/radio'}×5]`, container `role=radiogroup`. Behaviour unchanged and re-verified. |
| SHOPPER-12 | the per-unit column is suppressed on a quantity ledger, where it printed `≈ 169.90 ₪ ליחידה` six times. | B's ledger rows carry no `__pm`; the space goes to graft C's meanings. |
| SHOPPER-13 | a `dl` row whose whole value equals the giant numeral is skipped. | A and C no longer print `IP65` twice in the same block. |
| SHOPPER-09 | partial: the mobile rail's fade mask moved 84 % → 90 %, so the fourth stop is no longer half under it. The peek/hint the critic asked for is not built. | mask `linear-gradient(to left,#000 90%,transparent)`. |
| CREATIVE-13 | partial: on a two-axis rail the caption (the part that actually differs) now carries the numeral's weight — 14 px, full ink. | `.env2-pdp-stage__track--pair` present on C only. |

### Deliberately left

| id | why, and which round |
|---|---|
| QA-05 (minor) | 25 nodes under 13 px is a **spec-internal conflict**: §6.18 forbids anything under 13 px and §4.8 specifies an 11.5 px card kicker, §3.2 an 11 px kicker. The fixer must not pick. Everything that is a *caption* was raised (TYPOGRAPHER-04); what remains is the tracked kicker/eyebrow role the design system itself defines. **The lead rules; round 2 applies it, and it changes the homepage too.** |
| TYPOGRAPHER-11 (minor) | Hebrew letterspaced at `.16em`/`.18em` is prescribed by `brief/WINNING-SPEC.md` §3.2 and is used on every page in the store. Halving it is a design-system change, not a PDP fix. **Lead, then a system-wide pass.** |
| TYPOGRAPHER-12 (nit) | the guillemet pair prints mirrored (`»…«`). It is symmetric, consistent and correct bidi behaviour; which pair is *intended* is a copy decision. **Lead: record it in the spec so a later copy edit does not "fix" one side.** |
| TYPOGRAPHER-13 (nit) | `.env2-h{line-height:.98}` is a shared core class on every display heading in the store; the computed overlap is 0.44 px on one mobile h3 and no heading on any of the 27 products currently puts a ל under a descender. **Core change → lead.** |
| QA-08 (minor) | the three header chrome tab stops with no focus ring are Kalles' own, on every template. **Core change → lead.** |
| CREATIVE-11 (minor) | the ledger's mini-string. It is now the row's only visual scale cue beside a populated `__use` caption, and re-drawing it as a labelled length bar is a design decision, not a fix. **Round 2 with the catalogue card.** |
| CREATIVE-12 (minor) | section 02's length. With the switch restored the section carries the device, the refusal and the solar question; the "meta lead" the critic objected to only renders in *choose* mode (product C). Re-cutting the choose-mode copy is a copy pass. |
| CREATIVE-03 (the section-order half) | impossible this round: one shared template, and `templateSuffix` is a product property (§8.1). **Owner + lead, when per-product templates are on the table.** |
| the `redirect_html` line of §4.2 | "לאור חזק… יש אצלנו מקום אחר — תאורת קיר" is per-place copy with a per-place link; the template is shared. Not a critic finding; recorded so it is not lost. |

---

## 4. The three archetypes, final measurements

Real Frank Ruhl Libre and Heebo; `brief/shot-http.js`; 1440×900 and 390×844.

| | pdp-multi (24 variants) | pdp-single (1 variant) | pdp-wall (8 variants, mains) |
|---|---|---|---|
| document height desktop / mobile | **8,492 / 8,988 px** | **8,171 / 8,750 px** | **8,137 / 8,527 px** |
| Liquid errors | **0** | **0** | **0** |
| horizontal overflow (390 / 360 / 320) | none | none | none |
| console errors | the two known mirror errors only | same | same |
| buy action inside the 390 fold | `הוספה לסל` bottom edge **555 px** (§4.1 asks < 700) | **555 px** | **534 px** |
| primary ATC height | 52.0 px both viewports | 52.0 | 52.0 |
| section anchors present | all eight | all eight | all eight |
| section tops at 390 | 0 · 843 · 1950 · 2996 · 4264 · 5355 · 6545 · 7279 | 0 · 843 · 1901 · 2953 · 4103 · 5133 · 6323 · 7057 | 0 · 843 · 1707 · 2759 · 3759 · 4826 · 6015 · 6750 |
| spine #2 device | switch + approved negative + solar question | switch + approved negative + solar question | choose mode, no negative (§4.2 C) |
| ledger `__use` captions | 6 / 6 | 6 / 6 | 4 / 4 |
| ledger price decimals aligned | yes, x = 335.3 on all six | yes | yes |
| kicker contrast over the photo (1440) | 10.95 : 1 | 11.10 : 1 | 10.52 : 1 |

## 5. Buy flow

* **With JavaScript, healthy theme.** Rail stop → stage price counts, mirror, sticky bar, hidden `id` and
  the **ledger** all move together (SHOPPER-01). `הוספה לסל` POSTs to `/cart/add.js`; the Kalles drawer opens
  and is night (`brief/side-pages/pdp/build-preview/buyflow-mobile.png`, unchanged by this pass).
* **With JavaScript, degraded theme** (the drawer element present, its module not upgraded — the mirror's
  own state): the POST succeeds and **the page now says so** — the button reads `נוסף לסל` and stays
  disabled 1.6 s, so a second tap cannot land in that window.
* **Keyboard.** 1–2 `Tab`s from a body click reach the stage ATC at 390; `Enter` posts.
* **Reduced motion.** `movingCount = 0` inside the eight sections on all three; every lamp `--lit:1`,
  including the new closing photograph.

## 6. What degrades without JavaScript

Nothing that decides or completes a purchase.

* Every ledger row is a real `<form method="post" action="/cart/add">` and **every one is visible**: 6 / 6 / 4
  forms, six prices on A (`89.90 … 179.90`), six running totals on B (`169.90 … 1,359.20`), four on C.
* The fold's add-to-cart posts through the `form=` binding; the quiet axis is a native `<select>`/radio line.
* The sticky bar renders un-transformed with its own hidden `id`; `body` keeps its 78 px end padding.
* Section 02's switch is two native radios plus CSS `:checked ~`, so the light really goes out, the refusal
  really prints and the solar question really answers **with JS off**.
* The closing photograph is lit (`--lit` defaults to 1), the body ground is `rgb(2,3,6)`.
* What is *not* rendered: the drawn string/halo/path over the hero (decoration on a photograph that already
  shows the lit product), the price count-up, the row→stage binding, and the single collapsed buy line — the
  six row forms are the whole path instead. Two nodes sit at `opacity:0` on A and B: the refusal line and the
  solar answer, which are **responses to a switch the visitor has not flipped yet** and appear on flip
  without a script.

## 7. Open items

**For the lead**

1. **QA-05 — the 13 px floor conflicts with the spec's own kicker.** §6.18 says nothing under 13 px; §3.2
   specifies an 11 px kicker and §4.8 an 11.5 px card kicker. Rule one way; both the PDP and the homepage
   change with it.
2. **TYPOGRAPHER-11 — Hebrew letterspacing.** `.16em`/`.18em` at 11–12 px is a system decision (§3.2), not a
   PDP one.
3. **TYPOGRAPHER-13 — `.env2-h{line-height:.98}`** is a core class on every display heading in the store.
4. **QA-08 — the header's three focus rings** are Kalles chrome, core-level.
5. **TYPOGRAPHER-01, second half — the `FRL Fallback` metrics.** The critic called `size-adjust:94% /
   ascent-override:102% / descent-override:36%` "untuned guesses". Two of the three are not: Frank Ruhl
   Libre's real metrics are ascent .957 / descent .334, and against the size-adjusted em they are
   .957/.94 = 101.8 % ≈ **102 %** and .334/.94 = 35.5 % ≈ **36 %** — exactly what is written, and the file's
   own comment says so. Only `size-adjust:94%` is a judgement about David/Times, and it cannot be tuned on
   this box because neither face is installed. **Decide: tune it on a machine that has them, or drop the
   fake fallback and let `Noto Serif Hebrew` carry the swap.**
6. **CREATIVE-13 / SHOPPER-09** — whether C's two price axes should be one rail or two, and whether the
   mobile rail needs a partial-peek affordance. Both are compositions, not bugs.
7. **CREATIVE-03's remaining half** — a different section order per archetype needs per-product templates,
   which needs `templateSuffix` changes, which this round may not make.

**For the owner**

1. **Write `custom.not_fit_for` and `custom.power_source`** for the 27 products from
   `brief/side-pages/pdp/metafields.json`. The page no longer *depends* on them — it derives both from the
   place pair and from the product's own description — but a written metafield is the first source in both
   sections and is what lets a product say something the description does not. It is also the only way to
   give a product a negative its category does not imply.
2. **The wall product's photography.** `waterproof-led-wall-light-ip65-6w-12w` owns four usable frames, two
   of which are the same lamp on the same wall; index 0 is a slogan slide and index 2 a supplier contact
   sheet. Its night gallery and its closing screen therefore repeat. One real night photograph of that lamp
   on a house front would fix three sections at once.
3. **`templates/product.elmsnest.json` still carries "בוואטסאפ"?** No — that string left with the old
   template in round 1; recorded here because core REPORT §9.6 flagged it.

---

## 8. Does this page sell, and does it belong to the same store as the homepage?

**Does it sell — yes, and it now sells honestly.**

On a phone the first screen does the whole job: a night photograph of the product itself, the place and the
approved promise, the product's name, a resolved `89.90 ₪` with the honest range beside it, a 52 px
`הוספה לסל` whose bottom edge is at 555 px, the four consumer numbers in one strip, the photo-check step,
and a rail with six lengths and six prices — before a single scroll. That was true before this pass. What
was not true is that the page agreed with itself: choosing 11 metres on the fold left the ledger selling the
5-metre variant, on all three products. It agrees now, and the id that reaches the cart is the id the buyer
chose. And section 02, which existed as an empty frame around the store's one differentiator, now actually
does the thing: the switch flips, the light goes out, and the page says `לא נדלק. זו הנקודה.` next to
`צריך אור חזק — זו אינה מטרתה`. On the mains wall light it says nothing of the kind, because nothing of the
kind is true — which is the same promise kept in the other direction. A shopper who reads this page knows
what the lamp will not do before she knows how to pay for it. That is the only reason a narrow specialist
beats a marketplace, and it is on the page.

**Does it belong to the same store as the homepage — yes, and it is the same store's better half.**

Same ground, same night, same palette, same two faces, the same hairline vocabulary and the same refusal to
show a badge, a star or a countdown. The page is still *quieter* than the homepage in the strict sense —
8 % of its pixels are lit against the homepage's 24 % — but that difference is not a failure of belonging:
the homepage's job is four collection photographs at full bleed, and the PDP's job below the fold is a price
table, a spec ledger and consumer law, which are text. Where the critic was right is that the page used to
*stop* being photographic after the ledger and never started again; it now closes on a full-bleed
photograph of the product's own light with the quote over it, so the last screen is an event and not a
footer. The two pages read as one shop with two jobs — and the PDP is the one you could give a card to.
