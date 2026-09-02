export const meta = {
  name: 'core-round-0',
  description: 'Engineer the shared page-agnostic core on the ElmsNest dev theme per CORE-SPEC, deploy, verify from JS-enabled renders, fix, re-verify',
  phases: [{ title: 'Build', detail: 'one engineer implements + deploys + renders' }, { title: 'Verify', detail: 'visual + code verifiers' }, { title: 'Fix', detail: 'engineer closes must-fix findings' }, { title: 'Re-verify' }],
}
const ROOT = '/home/user/ElmsNest'
const COMMON = `Repo ${ROOT} (branch claude/design-sidebar-pages-3991tn). Shopify DEV theme gid://shopify/OnlineStoreTheme/154726400174 (UNPUBLISHED; writes allowed; the MAIN theme is blocked by the tool and must never be targeted; never publish). Load Shopify tools with ToolSearch "select:mcp__Shopify__graphql_query,mcp__Shopify__graphql_mutation". Read ${ROOT}/brief/DEPLOY.md for the exact upsert mutation shape (GraphQL block string """, one file per call, files must not contain """). Read ${ROOT}/HANDOFF.md §3–§4 and ${ROOT}/brief/build-preview/CONTRACT.md for the design system and tooling. Do not commit with git (the lead commits). Do not use gh. Chromium cannot reach the internet: mirror pages with python3 brief/mirror.py and screenshot with node brief/shot-http.js (JS-enabled) — see brief/inventory/mirror-all.sh and shot-all-http.sh; per page: python3 brief/mirror.py "https://elmsnest.com<path>?preview_theme_id=154726400174" brief/inventory/<key> && node brief/shot-http.js brief/inventory/<key>/index.html brief/inventory/<key>/http. Playwright lives at /tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/node_modules/playwright, chromium at /opt/pw-browsers/chromium-1194/chrome-linux/chrome (args --no-sandbox). Before any screenshot comparison, copy the CURRENT brief/inventory/home/http-*.png to brief/side-pages/core/before-home-*.png (baseline) if not already there.`

const BUILD_SCHEMA = { type: 'object', required: ['deployed', 'pages', 'acceptance', 'open'], properties: {
  deployed: { type: 'array', items: { type: 'string' } },
  pages: { type: 'array', items: { type: 'object', required: ['key', 'desktopPng', 'mobilePng', 'headerLegible', 'creamFound', 'coreLoaded', 'liquidErrors'], properties: { key: { type: 'string' }, desktopPng: { type: 'string' }, mobilePng: { type: 'string' }, headerLegible: { type: 'boolean' }, creamFound: { type: 'boolean' }, coreLoaded: { type: 'boolean' }, liquidErrors: { type: 'integer' }, note: { type: 'string' } } } },
  drawerPngs: { type: 'array', items: { type: 'string' } },
  acceptance: { type: 'object', properties: { homeUnchanged: { type: 'boolean' }, drawerNight: { type: 'boolean' }, lintOk: { type: 'boolean' } } },
  open: { type: 'array', items: { type: 'string' } }, report: { type: 'string' } } }

const FINDINGS = { type: 'object', required: ['findings', 'verdict'], properties: { verdict: { type: 'string' }, findings: { type: 'array', items: { type: 'object', required: ['id', 'severity', 'where', 'what', 'evidence', 'fix'], properties: { id: { type: 'string' }, severity: { type: 'string', enum: ['must', 'should', 'nit'] }, where: { type: 'string' }, what: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } } } } } }

phase('Build')
const build = await agent(`${COMMON}

You are the integration engineer for ROUND 0, resuming after an interruption. A previous engineer already IMPLEMENTED and DEPLOYED ${ROOT}/brief/side-pages/core/CORE-SPEC.md sections A–E to the dev theme (verified on the theme: snippets/elmsnest-v2-core.liquid 15.9 KB, elmsnest-v2-ground-index.liquid, elmsnest-v2-photo-url.liquid, elmsnest-v2-base.liquid stub, layout/theme.liquid, config/settings_data.json, sections/system-group.json, snippets/css-variables.liquid, templates 404/blog/cart/collection/list-collections/page/page.contact-us/product.elmsnest/search.json + customers/*). Repo copies are under ${ROOT}/theme/. The baseline PNGs exist at ${ROOT}/brief/side-pages/core/before-home-*.png and some verification artefacts exist (drawer-desktop/mobile.png, pdp-sticky-*.png, cmp-home-*.png) but NO REPORT.md was written and the acceptance was never completed.
Your job: finish §F of the spec.
1. Read CORE-SPEC.md, then diff ${ROOT}/theme/ against the LIVE theme files (fetch each deployed file via graphql theme.files and compare byte-for-byte with the repo copy; list any mismatch and fix it by redeploying the repo copy, or by saving the live version into the repo if the live one is the intended edit). Confirm ${ROOT}/theme/sections/elmsnest-v2-hero.liquid line 7 renders elmsnest-v2-ground-index and that the deployed hero matches.
2. Run python3 brief/lint.py — if it still only globs the old set, extend it per §F.1 first; fix until LINT OK.
3. Re-mirror + re-shoot the §F.3 pages with the JS-enabled harness (bash brief/inventory/mirror-all.sh && bash brief/inventory/shot-all-http.sh, or per page). Then run every §F.4 acceptance check with real measurements (PIL pixel samples at the stated points, grep counts, heights, the PIL mean-abs-diff of the home folds vs the baseline, the Playwright cart-drawer interaction over python3 -m http.server with /cart/add.js stubbed — re-do it so drawer-desktop.png / drawer-mobile.png reflect the current theme). Read every PNG you cite (Read tool) before declaring anything legible.
4. Fix anything that fails (minimal edits in ${ROOT}/theme/, redeploy the changed file, re-shoot the page) and record it.
5. Write ${ROOT}/brief/side-pages/core/REPORT.md per §F.5 (what changed file → lines; deploy log; the acceptance table page → header legible / cream found / core loaded / height; the drawer screenshot paths; what stays interim and which round replaces it).
Rules: minimal and reversible; homepage pixel-identical; no WhatsApp label; do not delete elms-pdp-* sections; do not touch templates/index.json; never publish. Return the structured result (paths relative to the repo).`, { label: 'engineer:core', phase: 'Build', schema: BUILD_SCHEMA, effort: 'high' })

log(`build done: ${build ? build.deployed.length : 0} files deployed, ${build ? build.pages.length : 0} pages rendered, open: ${build ? build.open.length : '?'}`)
if (!build) return { error: 'engineer returned nothing' }

phase('Verify')
const verifyPrompt = (lens) => `${COMMON}

You are an adversarial verifier (${lens} lens) for ROUND 0. The engineer claims: ${JSON.stringify(build).slice(0, 6000)}.
Read ${ROOT}/brief/side-pages/core/CORE-SPEC.md and ${ROOT}/brief/side-pages/core/REPORT.md, then try to REFUTE the acceptance claims with evidence.
${lens === 'visual' ? `Look at the PNGs yourself (Read): brief/inventory/{home,coll-all,coll-wall,pdp-single,pdp-multi,cart-full,cart-empty,search-hits,search-none,p404,page-guide,page-shipping,page-contact,policy-shipping,coll-list}/http-desktop-fold.png and http-mobile-fold.png, the full-page PNGs cropped into readable slices (python3 brief/inventory/crops.py <key> desktop 4 0.5 http), brief/side-pages/core/drawer-*.png and the before/after home folds (brief/side-pages/core/before-home-*.png vs brief/inventory/home/http-*.png). Check: header menu legible on the first screen of every page (not just the logo); no cream/brown surface anywhere (sample pixels with PIL and report hex values); the page ends in near-black before the footer; the drawer is night; the PDP interim sections readable (glow buttons with dark text); the homepage unchanged (PIL mean abs diff of the fold PNGs); mobile 390 too.` : `Check the code and the live theme: fetch the live snippets/elmsnest-v2-core.liquid, elmsnest-v2-ground-index.liquid, elmsnest-v2-photo-url.liquid, layout/theme.liquid, config/settings_data.json, sections/system-group.json, snippets/css-variables.liquid and every edited template JSON from the theme (graphql theme.files with filenames) and diff them against ${ROOT}/theme/ copies (they must match) and against brief/inventory/theme-src/ (the pre-change versions: the diff must be exactly the spec's edits — nothing else lost, no rewrite of settings_data.json, backslashes intact). Verify: the core is rendered once per page from theme.liquid and the hero no longer renders fonts/base; the env2-js script is still the first line of the core; the index gradient is index-only; no-JS behaviour (lamps lit without JS) preserved; logical properties only in new CSS; no """ in any deployed file; lint.py passes and now covers the templates; the photo-url snippet's mailto/wa.me branches url-encode correctly (render the URL for both branches by reasoning through the Liquid) and no label says בוואטסאפ while the number is empty; the four homepage sections still render (grep the mirrored home index.html for each anchor id and 0 'Liquid error'); blog.json no longer has blog-slider; badges hidden; quick-add off.`}
Every finding needs evidence (file:line, pixel hex at coordinates, or a grep count). Severity: must = the spec's acceptance fails or a regression on the homepage; should = spec item done wrong but pages still usable; nit = cosmetic. Default to reporting; do not soften. Verdict: one sentence.`

const verdicts = await parallel([() => agent(verifyPrompt('visual'), { label: 'verify:visual', phase: 'Verify', schema: FINDINGS, effort: 'high' }), () => agent(verifyPrompt('code'), { label: 'verify:code', phase: 'Verify', schema: FINDINGS, effort: 'high' })])
const findings = verdicts.filter(Boolean).flatMap((v, i) => v.findings.map(f => ({ ...f, lens: i === 0 ? 'visual' : 'code' })))
const musts = findings.filter(f => f.severity === 'must'), shoulds = findings.filter(f => f.severity === 'should')
log(`verify: ${musts.length} must, ${shoulds.length} should, ${findings.length - musts.length - shoulds.length} nit`)

let fix = null, recheck = null
if (musts.length + shoulds.length > 0) {
  phase('Fix')
  fix = await agent(`${COMMON}

You are the integration engineer for ROUND 0, second pass. The build report is ${ROOT}/brief/side-pages/core/REPORT.md. Two verifiers found these issues (fix every "must" and every "should"; skip nits unless trivial):
${JSON.stringify(musts.concat(shoulds), null, 1)}
For each: reproduce it first (read the file / the PNG), fix it in ${ROOT}/theme/ (and fetch-edit-save for live-owned files as in the spec), redeploy only the changed files (one per upsert call), re-mirror and re-shoot the affected pages with the JS-enabled harness, re-run the affected acceptance checks with real measurements, and append a "Fix pass" section to REPORT.md (finding id → what changed → evidence it is closed). Keep the homepage pixel-identical. Return the structured result.`, { label: 'engineer:fix', phase: 'Fix', schema: BUILD_SCHEMA, effort: 'high' })
  phase('Re-verify')
  recheck = await agent(`${COMMON}

Final verifier (visual + code, one pass). The engineer's fix pass claims: ${JSON.stringify(fix).slice(0, 5000)}. The original findings were: ${JSON.stringify(musts.concat(shoulds).map(f => ({ id: f.id, what: f.what }))).slice(0, 4000)}.
Read ${ROOT}/brief/side-pages/core/REPORT.md (Fix pass section), look at the fresh PNGs for every page named in the findings (Read them), re-fetch any live file named in the findings and confirm the fix. For each original finding say closed / still open (with evidence). Then do one last sweep of the §F.4 acceptance table on the current renders. Verdict: one sentence, and whether round 0 is DONE (all musts closed, homepage unchanged) or NOT DONE.`, { label: 'verify:final', phase: 'Re-verify', schema: FINDINGS, effort: 'high' })
}
return { build, findings, fix, recheck }