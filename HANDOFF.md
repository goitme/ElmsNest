# ElmsNest — handoff for the next session (written 2026-09-02)

Read this file first, in full. Then read the files it points to before touching anything.
It exists so a fresh session starts with everything the previous one learned, including what failed.

## 0. Where things stand

- Store: **elmsnest.com**, Shopify, Hebrew-only RTL, ₪, Israel, 27 outdoor-lighting products, 4 collections, plan "Pause and Build".
- **MAIN (published) theme:** `ElmsNest - PDP Design v2` (`gid://shopify/OnlineStoreTheme/154315063470`). Untouched.
- **Dev theme with the new homepage:** `ElmsNest - Homepage Rebuild 2026-09-01` (`gid://shopify/OnlineStoreTheme/154726400174`), UNPUBLISHED. It is a full copy of MAIN plus the v2 homepage. Preview: `https://elmsnest.com/?preview_theme_id=154726400174` (works without login; the sandbox can fetch it with curl but NOT with Chromium — see §4).
- Git: branch `claude/homepage-rebuild-709jc6` on `goitme/ElmsNest`. `theme/` mirrors the theme files we own; `brief/` holds the brief, spec, concepts, harness.
- **Homepage status:** built, deployed to the dev theme, passed one adversarial critique round (41/47 → residuals closed). **Not yet approved by the owner, not published.** The owner has been shown the real render and asked for (a) verdict, (b) WhatsApp number, (c) a ≥2000px hero photo. Do not publish anything without an explicit "publish" from the owner.
- Open admin-side items nobody can do from code: `settings.whatsapp_number` is empty (every "שלחו תמונה" CTA falls back to `/pages/contact-us`, honestly labelled); main-menu should point קולקציות → `/#env2-places` and drop שאלות נפוצות; the `solar-wall-lights` collection image needs a focal point set in admin (landscape image, lamp at the crop edge).

## 1. What the owner rejected, and why (never repeat)

First attempt (commit 489e149, files `theme/sections/elmsnest-{hero,products,collections,places,terms}.liquid`, still in the repo as a record) was rejected verbatim as: *"very bad, from the nineties, everything repeated, trivial text, no creativity, no innovation, no creative visual design."*
Diagnosis (accepted by the owner): same layout four times (heading + four equal boxes), text shortened instead of replaced with visual ideas, colour mistaken for identity, default typography, same container every section, zero motion, and — the root cause — one version built straight through with no alternatives and no visual judging.

**Rule for every page from now on: never build one version and ship it.**

## 2. The process that produced the accepted-so-far homepage (replicate it per page)

1. **Brief** (`brief/BRIEF.md`): store facts, brand non-negotiables, assets, hard constraints, the bar, a do-not list. Written before any design.
2. **Concept panel**: 5 designers, each forced to a *radically different* creative seed, each producing a complete offline HTML mockup with real copy, real products/prices, real fonts and images, and screenshotting it (`brief/shot.js`) and self-critiquing from the PNGs. Text specs are not judged — renders are.
3. **Judges**: 3 lenses (creative director / Israeli mobile conversion / brand + Liquid feasibility) score all mockups from the screenshots. Then one lead synthesizes a build spec that grafts the best devices from non-winners (`brief/WINNING-SPEC.md` is the model of what "build-ready" means: palette, type scale, motion rules, image ledger per slot, per-section copy/layout/schema, do-not list).
4. **Build**: shared plumbing first, then one engineer per section in parallel, each proving its section with an offline preview and `brief/lint.py`, then an integrator reconciles schemas ↔ template, deploys (`brief/DEPLOY.md`), mirrors the real render (`brief/mirror.py`) and screenshots it.
5. **Adversarial critique**: 4 critics whose job is to refute "this is world-class" (creative director, Hebrew mobile shopper, Hebrew typographer, front-end QA who *tests* touch/keyboard/reduced-motion/no-JS), triaged into per-file fix packages, fixed, redeployed, verified on a fresh mirror.
6. **The lead looks at the real render personally** before showing the owner, and the owner is the final judge before anything is published.

Workflow scripts from this session are persisted under `/root/.claude/projects/-home-user-ElmsNest*/…/workflows/scripts/` (may not survive a new container) — the prompts inside them are worth lifting. They used the Workflow tool with `parallel()` for judges/builders and one agent for triage/synthesis.

## 3. The design system (source of truth: `brief/WINNING-SPEC.md` §3)

- **Idea:** dusk turning to night. One page-long sky gradient (`#4a6a9c → #1f3357 → #0f1a2f → #070b15 → #020306`), sections transparent, every lamp dim until it enters view then lights once. Stars increase toward the footer.
- **Ink** `#f4eee3`, ink-2 `#c9c4b8`, mute `#8f95a3` (only on sky-2 or darker), **gold** `#e9b96e` (kickers, rules, active), **glow** `#ffd394` (prices, lit numerals, primary button), ember `#f7a24a` (halo cores only). Hairline `rgba(244,238,227,.12)`. The only "card" surface is a scrim `rgba(5,8,14,.55)` + blur. **No brown / beige / cream anywhere.**
- **Type:** Frank Ruhl Libre (500/700/900) for display, Heebo (300/400/500) for text; loaded once by `snippets/elmsnest-v2-fonts.liquid` with size-adjust fallbacks. Display headlines line-height .98, second line in glow. Product titles never in the serif. Latin tokens in `<bdi>`; prices `<bdi>n</bdi> ₪`.
- **Radius:** 0 on everything except pill buttons and the divider knob (999px). No boxes; hairlines separate.
- **Motion:** lamps light on arrival (IntersectionObserver, never re-dim); the sun-rail dot tracks scroll progress; exactly one thing switches on per section; reduced-motion = everything lit, no transitions; no-JS = everything lit (`html.env2-js` guard). No fade-in-on-scroll for text, no parallax, no autoplay.
- **Layout:** `.env2-wrap` = min(1240px, 100% − 2×gutter); full-bleed for hero-scale moments; logical properties only (Sense RTL app flips physical ones).
- **Shared code:** `theme/snippets/elmsnest-v2-{fonts,base,price,buy}.liquid`; contract in `brief/build-preview/CONTRACT.md` (class names, `[data-lamp]`, `window.env2.observe(el)`).
  ⚠ `elmsnest-v2-base` is rendered by the homepage hero and its gradient targets `body.hdt-page-type-index`. For other templates you will need a page-agnostic core: split the base into a global part (tokens, type, buttons, lamps, `window.env2`) rendered from `layout/theme.liquid`, and a per-template ground (the index gradient stays index-only; decide the ground for collection/product/page templates deliberately — probably sky-3/sky-4 with the same hairline/scrim vocabulary).

## 4. Tooling and mechanics that took hours to learn

- **Chromium cannot reach the internet from this sandbox** (proxy relay closes the tunnel); curl can. So: `python3 brief/mirror.py <url> <dir>` mirrors a Shopify page with all assets to disk, then `node brief/shot.js <dir>/index.html <prefix>` screenshots it at 1440 and 390 (full page + first fold) from `file://`. Kalles' cross-origin module scripts do not run on `file://`; for interaction tests serve the mirror over `python3 -m http.server` on localhost.
- **Offline asset pack** for mockups: `brief/assets/` (12 Hebrew font families as local woff2 + `fonts.css`, 115 product/collection/hero images ≤1000px). Binaries are gitignored — regenerate with `cd brief/assets && python3 fetch.py`. Playwright is installed in the scratchpad `node_modules`; chromium binary `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
- **Deploy** = Shopify MCP `graphql_mutation` → `themeFilesUpsert`, one file per call, body as a GraphQL block string `"""…"""` (so no escaping; files must not contain `"""`). Writes to MAIN are blocked by the tool; writes to unpublished themes work. Sections must exist before a template referencing them is uploaded. Shopify validates Liquid + schema on upload. **Schema `name` max 25 chars.** `settings_data.json` must be fetched and minimally edited, never rewritten (and backslashes pass through block strings literally).
- **`brief/lint.py`** checks tag balance, no Liquid inside `{% stylesheet %}`/`{% javascript %}`, `.env2-` selector prefixing, schema JSON, presets, anchors, and index.json ↔ schema id drift. It globs `elmsnest-v2-*` and `templates/index.json` only — extend it for other templates.
- **Kalles facts:** header is `header-inline-blocks` (transparent over the first section only when that section's schema `class` includes `section-allow-transparent hdt-section`); sticky on scroll-up; body class `hdt-page-type-<type>`; Kalles styles bare `blockquote` with a cream panel (reset it); `<back-to-top>` is hidden on index via the base snippet; Liquid trims literal text between `{%-` tags (build separators with `append`). Theme radii are 0. Colour schemes live in `settings_data.json` (`scheme-env2-night` added: ink on `#020306`).
- **Image ledger:** many product featured images (index 0) carry baked-in Hebrew marketing text. `brief/WINNING-SPEC.md` §3.6 lists per-product usable indexes and a never-use list. Reuse it for collection/product pages.
- **Honesty rules (from «מי אנחנו»):** no best-sellers, no review counts, no customer quotes, no "trusted by", no countdowns. The four approved suits/doesn't-suit pairs are in `brief/BRIEF.md` §3 — shorten published lines, never write new negatives. Consumer-protection terms (shipping/delivery/cancellation) must stay findable.

## 5. The side pages to design next (inventory)

Check what the dev theme already renders for each before designing — the theme is a copy of "PDP Design v2", so the product page already had a design pass (unreviewed by this session).
- Collection template (4 collections + `/collections/all`): the browse experience, filters/sort, product cards, empty state.
- Product template (PDP): gallery, variants (many products have 8–30 variants), price rule, buy, the suits/doesn't-suit pair as a product-level device, spec sheet (IP65, W, K), shipping/cancellation terms.
- Cart + cart drawer; search results; 404.
- Pages: `guide-garden-lighting`, `why-solar-lighting`, `מי-אנחנו`, `shipping-delivery`, `help-faq`, `contact-us`, `processing-time`, `accessibility-statement`; policy pages.
- Header and footer are Kalles groups, configured (dark, gold mark) in `theme/sections/{header,footer}-group.json` — they now appear on every page, so they are the first thing to check on each template.

Same bar as the homepage: one idea per template that only a lighting store could have, every screen composed differently, editorial Hebrew type, motion that means something, and it must sell. Same process: brief → divergent concepts as rendered mockups → judged → spec → build → adversarial critique → owner's verdict.

## 6. Prompt to paste into the new chat

اقرأ أولاً `/home/user/ElmsNest/HANDOFF.md` بالكامل، ثم الملفات التي يشير إليها (`brief/BRIEF.md`, `brief/WINNING-SPEC.md` §3 و§7, `brief/THEME-NOTES.md`, `brief/DEPLOY.md`, `brief/build-preview/CONTRACT.md`). الصفحة الرئيسية الجديدة منشورة على ثيم التطوير `154726400174` (غير المنشور) وتنتظر حكم المالك؛ لا تنشر شيئاً على المتجر الحي. المطلوب الآن: تصميم كل الصفحات الجانبية (الكولكشن، صفحة المنتج، السلة، البحث، 404، وصفحات المحتوى) بنفس مستوى الصفحة الرئيسية ونفس نظام التصميم، وبنفس العملية: موجز ← 5 مفاهيم متباعدة كنماذج مُصوَّرة ← تحكيم من اللقطات ← مواصفة ← بناء ← نقد عدائي ← حكم المالك. ابدأ بجرد ما يعرضه ثيم التطوير حالياً لكل قالب (لقطات حقيقية عبر mirror.py + shot.js) وقدّم لي خطة ترتيب الصفحات وأسئلتك قبل البناء.
