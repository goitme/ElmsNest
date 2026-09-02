export const meta = {
  name: 'pdp-build-round-1',
  description: 'Build the eight ElmsNest PDP sections from WINNING-SPEC, deploy to the dev theme, adversarially critique the real render and the buy flow, fix, re-verify',
  phases: [
    { title: 'Plumbing', detail: 'shared snippets: ground, image ledger, variant model, buybar, card, photo CTA' },
    { title: 'Sections', detail: 'one engineer per section, each proved with an offline preview' },
    { title: 'Integrate', detail: 'template, deploy, mirror, screenshot the three archetypes' },
    { title: 'Critique', detail: 'four adversarial critics, one executes the buy flow' },
    { title: 'Fix', detail: 'triage, fix, redeploy, verify' },
  ],
}
const ROOT = '/home/user/ElmsNest'
const DIR = `${ROOT}/brief/side-pages/pdp`
const THEME = 'gid://shopify/OnlineStoreTheme/154726400174'
const COMMON = `Repo ${ROOT} (branch claude/design-sidebar-pages-3991tn). Shopify DEV theme ${THEME} — UNPUBLISHED; writes allowed; the MAIN theme is blocked and must never be targeted; NEVER publish; never change any product, collection, page or metafield (products' templateSuffix in particular — it is shared with the live theme).
Read before doing anything: ${DIR}/WINNING-SPEC.md (binding — INCLUDING §8, the lead's addendum, which overrides §5 on the template filename), ${DIR}/BRIEF.md (§3 honesty rules, §4 the persuasion spine, §11 do-not list), ${ROOT}/brief/WINNING-SPEC.md §3 (the homepage design system), ${ROOT}/brief/build-preview/CONTRACT.md (class names, [data-lamp], window.env2), ${ROOT}/brief/side-pages/core/REPORT.md §9 (known core bugs you must not inherit), ${ROOT}/brief/side-pages/OWNER-NOTES.md, ${ROOT}/brief/THEME-NOTES.md and ${ROOT}/brief/DEPLOY.md (upsert mechanics).
Data: ${DIR}/products.json (27 products: description_text, variants with prices, options, images) and ${DIR}/metafields.json (extracted facts — NOT yet written to Shopify, so treat every metafield as EMPTY at render time and make each section degrade to the description bullets).
Facts that constrain everything: the shared core (snippets/elmsnest-v2-core.liquid) is already rendered from layout/theme.liquid on every page and provides the tokens, Frank Ruhl Libre + Heebo, .env2-* helpers, [data-lamp], window.env2 and the night ground — do not re-render it and do not redefine its tokens. settings.whatsapp_number is EMPTY: the photo CTA is a mailto and no label may say בוואטסאפ. There are no sales: no badge, no strikethrough, no compare-at. Latin tokens and prices go in <bdi>. Logical CSS properties only (an RTL app flips physical ones). No Liquid inside {% stylesheet %} / {% javascript %} blocks. No file may contain three double-quotes in a row (it breaks the GraphQL upload). Radius 0 except pills.
Tooling: Shopify tools via ToolSearch "select:mcp__Shopify__graphql_query,mcp__Shopify__graphql_mutation". Chromium cannot reach the internet: mirror with python3 ${ROOT}/brief/mirror.py "<url>?preview_theme_id=154726400174" <dir> then screenshot with node ${ROOT}/brief/shot-http.js <dir>/index.html <dir>/http (serves the mirror so the theme JS runs). node ${ROOT}/brief/shot.js is for offline static previews only. Playwright: /tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/node_modules/playwright, chromium /opt/pw-browsers/chromium-1194/chrome-linux/chrome, args --no-sandbox. Do not commit with git; the lead commits. Do not use gh.`

const SECTIONS = [
  { id: 'stage', spec: '4.1', title: 'screen 1 + the buy box', note: 'Renders snippets/elmsnest-v2-ground-product (§5/§8.2) — it is the only section that does. Must fit the whole buy decision inside 1440x900 AND 390x844: lamp lit in its place, place word + approved suits phrase, title, price, add-to-cart, the four numbers in one line (graft F), the small step, and a preview of the ledger. Per §8.3 the primary CTA must be a <button> in a form or set its own colour.' },
  { id: 'fit', spec: '4.2', title: 'the not-for device', note: 'The approved pair as a physical switch that puts the product light out, plus graft B (the sun question) on solar products only — see §3.7 power-source branch. The four pairs are verbatim from BRIEF §3; never write a new negative.' },
  { id: 'night', spec: '4.3', title: 'the night gallery', note: 'Two distances plus a scale cue; obeys the image ledger (§3.5) — never index 0 of the never-use list.' },
  { id: 'ledger', spec: '4.4', title: 'the variant / price ledger', note: 'The technical heart. Every variant row with its own price, per-unit price, use-meaning caption (graft A) and its own no-JS <form method="post" action="{{ routes.cart_add_url }}">. JS enhances to a selector and syncs ?variant= via history.replaceState. Uses snippets/elmsnest-v2-pdp-variants.' },
  { id: 'facts', spec: '4.5', title: 'what could go wrong', note: 'Only facts from the product description bullets, plus an explicit row for what is NOT known. Metafields are empty today, so the fallback path is the one that renders.' },
  { id: 'terms', spec: '4.6', title: 'the four numbers', note: 'The licensed consumer wording verbatim; graft H headings. No new claim.' },
  { id: 'ask', spec: '4.7', title: 'the specialist line + the small step', note: 'No comparison table, no competitor. The photo CTA uses snippets/elmsnest-v2-pdp-photo-cta (mailto today).' },
  { id: 'related', spec: '4.8', title: 'related products + THE product card', note: 'snippets/elmsnest-v2-pdp-card.liquid is designed here and becomes the catalogue card in round 2 — build it as a standalone, reusable snippet taking a product and options. Deck copy is graft G (no stars, no best-seller).' },
]
const FILE_SCHEMA = { type: 'object', required: ['files', 'preview', 'lint', 'notes'], properties: { files: { type: 'array', items: { type: 'string' } }, preview: { type: 'array', items: { type: 'string' } }, lint: { type: 'string' }, schemaIds: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' }, risks: { type: 'array', items: { type: 'string' } } } }

phase('Plumbing')
const plumbing = await agent(`${COMMON}

You are the plumbing engineer for the PDP build. Build ONLY the shared pieces every section depends on, in ${ROOT}/theme/ (repo paths mirror theme paths). Do NOT build any section. Do NOT deploy — the integrator does that.
Files (all per WINNING-SPEC §5, §3.1, §3.5, §3.6, §3.7, §4.9):
1. snippets/elmsnest-v2-ground-product.liquid — the PDP ground per §3.1, mirroring how snippets/elmsnest-v2-ground-index.liquid works for the homepage (read that file first). Scoped to body.hdt-page-type-product so it cannot touch other templates.
2. snippets/elmsnest-v2-pdp-image.liquid — the §3.5 index resolver: input product + a slot name (hero / context / close / card / wall-pair); returns the chosen image object honouring the per-product ledger and the never-use list from ${ROOT}/brief/WINNING-SPEC.md §3.6 (15 products whose index 0 carries baked-in text). Must never return index 0 for those, must fall back safely, and must accept a per-section override setting.
3. snippets/elmsnest-v2-pdp-variants.liquid — builds the ledger model ONCE from product.variants: for each row, the option value that carries the price axis (§3.6 option-axis rule), its price, its per-unit or per-metre price where the option name states a count or a length (parse the Hebrew option values in products.json: "5 מ׳ / 20 נורות", "2 יחידות", "6W"), availability, variant id, and the secondary axes. Emit it both as Liquid variables for the no-JS markup and as one JSON script tag for the JS enhancement.
4. snippets/elmsnest-v2-pdp-buybar.liquid — §4.9, the sticky mobile buy bar mirroring the selected row.
5. snippets/elmsnest-v2-pdp-photo-cta.liquid — mailto today, wa.me when settings.whatsapp_number fills (one place, both branches correct and url-encoded; never the label בוואטסאפ while the number is empty).
6. snippets/elmsnest-v2-pdp-card.liquid — the product card of §4.8, standalone and reusable (round 2's catalogue card): image via the resolver, place kicker, title in Heebo (never the serif), price by the elmsnest-v2-price rule, single-variant → add-to-cart form, multi → link. No badge, no swatch dots, no quick-add icon, no stars.
Also: extend ${ROOT}/brief/lint.py so it globs sections/elmsnest-v2-pdp-* and snippets/elmsnest-v2-pdp-* and validates templates/product.elmsnest.json against the new section schemas; keep its existing checks working.
Prove your work offline: build ${DIR}/build-preview/_plumbing.html that renders the card, the buybar and a ledger model for the three archetypes (crystal 24 variants, path 1 variant, wall 8 variants) with hand-substituted Liquid output and local assets (${ROOT}/brief/assets/img/<handle>-<i>.jpg, ${ROOT}/brief/assets/fonts.css), screenshot it with node ${ROOT}/brief/shot.js, and READ the PNG. Run python3 ${ROOT}/brief/lint.py until it passes.
Write ${DIR}/build-preview/CONTRACT-PDP.md: for each snippet, its exact call signature, its inputs, what it returns/prints, the class names it emits, and the JSON shape of the variant model — the eight section engineers build against this document, so it must be precise and final.
Return files, preview paths, lint result, and the risks a section engineer must know.`, { label: 'plumbing', phase: 'Plumbing', schema: FILE_SCHEMA, effort: 'high' })
if (!plumbing) return { error: 'plumbing failed' }
log(`plumbing: ${plumbing.files.length} files, lint ${plumbing.lint}`)

phase('Sections')
const built = await parallel(SECTIONS.map(s => () => agent(`${COMMON}

You are the engineer for ONE PDP section: **sections/elmsnest-v2-pdp-${s.id}.liquid** (WINNING-SPEC §${s.spec} — ${s.title}).
The plumbing is built and its contract is ${DIR}/build-preview/CONTRACT-PDP.md — READ IT FIRST and build against it; the snippets exist in ${ROOT}/theme/snippets/. Plumbing notes: ${plumbing.notes} ${(plumbing.risks || []).join(' · ')}
Section-specific: ${s.note}
Write ${ROOT}/theme/sections/elmsnest-v2-pdp-${s.id}.liquid: markup + {% stylesheet %} (every selector prefixed .env2-pdp-${s.id}__…) + {% javascript %} (init via document.querySelectorAll('[data-env2-pdp-${s.id}]'), and end with the CONTRACT's env2.observe fallback line) + {% schema %} with settings, blocks and ONE preset. Section root: <section id="env2-pdp-${s.id}" data-env2-pdp-${s.id} class="env2-section" dir="rtl" style="scroll-margin-top:90px">. Schema name max 25 chars. Every block root carries {{ block.shopify_attributes }}. Copy is exactly what §${s.spec} specifies (Hebrew); product facts come only from the product object or its description — never typed.
It must render correctly for all three archetypes: solar-crystal-ball-string-lights (24 variants), stainless-steel-solar-path-light-ip65 (1 variant — no one-value picker anywhere), waterproof-led-wall-light-ip65-6w-12w (8 variants, MAINS: no solar sentence, per §3.7). And it must not break on the other 24 products (guard every image index, every option, every empty metafield).
Prove it offline before returning: build ${DIR}/build-preview/${s.id}.html — the section's rendered markup for the crystal-ball product (hand-substitute the Liquid you wrote), on the page ground, with local assets and fonts; screenshot at 1440 and 390 with node ${ROOT}/brief/shot.js ${DIR}/build-preview/${s.id}.html ${DIR}/build-preview/${s.id}; READ both PNGs and fix what they show (overflow, clipped text, contrast, mobile tap targets ≥44px) until they are right. Run python3 ${ROOT}/brief/lint.py and fix anything it reports about your file.
No-JS and reduced-motion: the section must render fully and buyably with JS disabled (lamps lit, prices visible, forms working) — state in your notes exactly what degrades.
Return: the file, the preview paths, lint result, your schema setting ids, notes, and the risks the integrator must check on the real render.`, { label: `section:${s.id}`, phase: 'Sections', schema: FILE_SCHEMA, effort: 'high' })))
const sok = built.filter(Boolean)
log(`sections built: ${sok.length}/8`)

phase('Integrate')
const INTEG = { type: 'object', required: ['deployed', 'pages', 'issues'], properties: { deployed: { type: 'array', items: { type: 'string' } }, pages: { type: 'array', items: { type: 'object', required: ['key', 'url', 'pngs', 'heightDesktop', 'heightMobile', 'liquidErrors'], properties: { key: { type: 'string' }, url: { type: 'string' }, pngs: { type: 'array', items: { type: 'string' } }, heightDesktop: { type: 'integer' }, heightMobile: { type: 'integer' }, liquidErrors: { type: 'integer' }, foldHasBuy: { type: 'boolean' }, note: { type: 'string' } } } }, buyFlow: { type: 'string' }, issues: { type: 'array', items: { type: 'string' } } } }
const integ = await agent(`${COMMON}

You are the integrator. The eight sections and the plumbing are written in ${ROOT}/theme/. Section engineer notes: ${JSON.stringify(sok.map(b => ({ files: b.files, schemaIds: b.schemaIds, risks: b.risks })))}
Do this:
1. Reconcile: read every section's {% schema %} and write ${ROOT}/theme/templates/product.elmsnest.json — the eight sections in the §5 order with ids pdp_stage … pdp_related and the default settings/blocks each section's spec calls for. **Per §8.1 the file is product.elmsnest.json (all 27 products carry templateSuffix "elmsnest"); do NOT create templates/product.json and do NOT touch any product.** Every setting key you write must exist in that section's schema — run python3 ${ROOT}/brief/lint.py until it passes.
2. Deploy to the dev theme with themeFilesUpsert, ONE file per call, GraphQL block string, in this order: snippets (ground-product, pdp-image, pdp-variants, pdp-photo-cta, pdp-card, pdp-buybar) → the eight sections → templates/product.elmsnest.json. A userErrors entry means the file was NOT written: fix and retry. Log filename → size.
3. Verify the real render for all three archetypes: /products/solar-crystal-ball-string-lights (pdp-multi), /products/stainless-steel-solar-path-light-ip65 (pdp-single), /products/waterproof-led-wall-light-ip65-6w-12w (pdp-wall). Mirror each into ${ROOT}/brief/inventory/<key>/ and shoot with shot-http.js. Then READ the PNGs (folds and cropped slices of the full page) and check: 0 'Liquid error' in the mirrored HTML; the buy action inside the 390×844 fold; every section present (grep each anchor id); no horizontal overflow; no cream/brown surface; the wall product carries no solar sentence; the single-variant product shows no one-value picker; heights.
4. Execute the buy flow on the http-served mirror with Playwright (as brief/side-pages/core did for the drawer): click a ledger row's add-to-cart, confirm the drawer opens or the documented fallback fires, screenshot it to ${DIR}/build-preview/buyflow-{desktop,mobile}.png. Stub /cart/add.js and /cart.js with page.route since the mirror is offline; what you are judging is that our JS reaches the right call and the right event, and that the no-JS form posts to routes.cart_add_url.
5. Fix anything broken (edit the repo file, redeploy that one file, re-mirror, re-shoot) and record it.
Return deployed files, the three pages with their measurements, what the buy flow did, and every issue you could not fix.`, { label: 'integrator', phase: 'Integrate', schema: INTEG, effort: 'high' })
if (!integ) return { plumbing, sections: sok, error: 'integration failed' }
log(`deployed ${integ.deployed.length} files; pages ${integ.pages.map(p => `${p.key} ${p.heightDesktop}/${p.heightMobile}`).join(' · ')}`)

phase('Critique')
const CRIT = { type: 'object', required: ['lens', 'verdict', 'findings'], properties: { lens: { type: 'string' }, verdict: { type: 'string' }, wouldOwnerSayNineties: { type: 'boolean' }, findings: { type: 'array', items: { type: 'object', required: ['id', 'severity', 'where', 'what', 'evidence', 'fix'], properties: { id: { type: 'string' }, severity: { type: 'string', enum: ['blocker', 'major', 'minor', 'nit'] }, where: { type: 'string' }, what: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } } } } } }
const CRITICS = [
  ['creative-director', 'You are the creative director who rejected the first attempt as "from the nineties, everything repeated, trivial text, no creativity". Your job is to REFUTE the claim that this page is world-class. Judge from the renders: is every screen composed differently, is there scale contrast, is there one idea only a lighting store could have, is the typography editorial, does anything read as a template, a box grid, or filler? Compare against the homepage renders (brief/inventory/home/http-*.png) — is it unmistakably the same store?'],
  ['mobile-shopper', 'You are an Israeli shopper on a phone with a real intention to buy string lights for a terrace. EXECUTE the purchase on the http-served mirror with Playwright at 390×844 (serve brief/inventory/pdp-multi over python3 -m http.server, stub /cart/add.js and /cart.js): find the price, pick 11 metres, add to cart, see what happens; then try the single-variant path (pdp-single) and the wall light (pdp-wall). Report everything that made you hesitate, everything you could not find without scrolling twice, every tap target under 44px, and whether you learned that it might NOT suit you before you were asked to pay. Screenshot each step.'],
  ['hebrew-typographer', 'You are a Hebrew typographer. Judge the type from the renders at both viewports: hierarchy, line length, leading on display Hebrew, RTL correctness, <bdi> discipline on Latin tokens and prices (IP65, 6W, USB, 89.90 ₪), the maqaf and geresh, ragged edges on justified/end-aligned paragraphs, product titles never in the serif, mixed-direction strings in variant names ("5 מ׳ / 20 נורות"), and anything that reads as a translation rather than Hebrew written for this store.'],
  ['frontend-qa', 'You are a front-end QA engineer. TEST, do not read: with Playwright on the http-served mirror — keyboard-only path to buying (tab order, focus visibility, the ledger as a real control), prefers-reduced-motion: reduce (every lamp lit, no transitions), JS disabled (context with javaScriptEnabled:false — every price visible, every form posts to /cart/add, no black page), 320px width, 390×664 (iPhone small viewport), and the sticky bar not covering the last row. Also check the schemas: every setting the template writes exists, presets present, block.shopify_attributes on block roots, no Liquid inside stylesheet/javascript blocks, and no console errors beyond the two known mirror ones.'],
]
const crits = await parallel(CRITICS.map(([lens, role]) => () => agent(`${COMMON}

${role}
The page is deployed. Renders: ${JSON.stringify(integ.pages)}. Buy flow as the integrator left it: ${integ.buyFlow || 'not reported'}. Open issues the integrator could not fix: ${JSON.stringify(integ.issues)}.
Read the spec you are auditing against: ${DIR}/WINNING-SPEC.md §4 (what each section must be) and §6 (the do-not list), ${DIR}/BRIEF.md §4 (the persuasion spine — the page must answer all eight, in order) and §11.
Your job is to find what is WRONG. Every finding needs evidence you produced yourself: a PNG you read (give the path and what you saw), a measured number, a Playwright observation, or a file:line. Severity: blocker = the owner would reject the page or a buyer cannot buy; major = a spine answer fails or a rule in §11/§6 is broken; minor; nit. Do not pad with praise. Also answer: would the owner still say "nineties"?`, { label: `critic:${lens}`, phase: 'Critique', schema: CRIT, effort: 'high' })))
const cok = crits.filter(Boolean)
const findings = cok.flatMap(c => c.findings.map(f => ({ ...f, lens: c.lens })))
const must = findings.filter(f => f.severity === 'blocker' || f.severity === 'major')
log(`critique: ${findings.filter(f => f.severity === 'blocker').length} blockers, ${findings.filter(f => f.severity === 'major').length} majors, ${findings.length} total`)

phase('Fix')
const fix = await agent(`${COMMON}

You are the integrator, fix pass. Four critics audited the deployed PDP. Their verdicts: ${JSON.stringify(cok.map(c => ({ lens: c.lens, verdict: c.verdict, nineties: c.wouldOwnerSayNineties })))}
Fix EVERY blocker and EVERY major; fix minors that are one-line; leave the rest recorded:
${JSON.stringify(must, null, 1)}
Minors and nits for the record: ${JSON.stringify(findings.filter(f => f.severity === 'minor' || f.severity === 'nit').map(f => ({ id: f.id, what: f.what, fix: f.fix })))}
For each: reproduce it first, fix it in ${ROOT}/theme/, redeploy only the changed files, re-mirror and re-shoot the affected product pages, and verify the fix with the same method the critic used (read the PNG, re-run the Playwright check). Then write ${DIR}/BUILD-REPORT.md: the deploy log, a finding-by-finding table (id → what → what changed → evidence it is closed → or why it is deliberately left), the three archetypes' final measurements (heights, fold has buy, Liquid errors, section anchors present), the buy-flow result, what degrades without JS, and the open items for the lead and the owner.
Finally re-read the three folds and the full pages yourself and say plainly whether this page sells and whether it belongs to the same store as the homepage.
Return the structured result.`, { label: 'fixer', phase: 'Fix', schema: INTEG, effort: 'high' })
return { plumbing: plumbing.files, sections: sok.map(s => s.files).flat(), integ, critics: cok.map(c => ({ lens: c.lens, verdict: c.verdict, nineties: c.wouldOwnerSayNineties })), findings, fix }
