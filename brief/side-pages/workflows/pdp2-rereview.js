export const meta = {
  name: 'pdp2-rereview',
  description: 'PDP round 2: post-fix re-review of pass 2 on the dev theme — a contract lens over the two files and a render lens over the pass-2 shots, one skeptic per finding',
  phases: [
    { title: 'Re-review', detail: 'contract + render lenses' },
    { title: 'Skeptics', detail: 'one skeptic per finding' },
  ],
}
const REPO = '/home/user/ElmsNest', P = `${REPO}/brief/side-pages/pdp2`, THEME = `${REPO}/theme`
const COMMON = `Repo ${REPO}. The ElmsNest product page round 2 was critiqued on its first deployed render, the lead ruled (${P}/critique/LEAD-DECISIONS.md — read it in full: 13 fixes, the kept items with reasons) and pass 2 is now DEPLOYED on the DEV theme and re-verified (${P}/verify-after-pass2.log, ${P}/verify-after/verify.json — the pdpSections, pdpCopy, guideLinksInMain entries; every page ≤ 5.03 screens at 390, scene 596/621 px with a photograph and 134 without, dusk 152, no copy missing). The contract: ${P}/SPEC.md (with the amendment note at its top). The files: ${THEME}/sections/elmsnest-s-pdp-scene.liquid, ${THEME}/sections/elmsnest-s-pdp-dusk.liquid, ${THEME}/templates/product.elmsnest.json, the assets ${THEME}/assets/ens-pdp-*.jpg with the ledger ${P}/images/CHOSEN.md. The pass-2 renders: ${P}/verify-after/pdp-<name>-<v>-js-full.png (name: path, wall, flood, rope, deck; v: m 390, s 360, d 1366) and the per-section shots ${P}/verify/ (path), ${P}/verify-wall/, ${P}/verify-flood/, ${P}/verify-rope/ — <scene|dusk>-<v>.png and -viewport.png. Do not modify any file. Return findings as JSON: at most 6, most severe first, severity blocker/high/medium/low, each with evidence (a shot and what you see in it, a file line, a number) and a concrete fix; report only what is wrong NOW, not what the first critique found and the rulings fixed — check each of the 13 fixes landed and say so in the verdict.`
const FIND = { type: 'object', required: ['lens', 'verdict', 'fixesLanded', 'findings'], properties: { lens: { type: 'string' }, verdict: { type: 'string' }, fixesLanded: { type: 'string' }, findings: { type: 'array', items: { type: 'object', required: ['id', 'severity', 'where', 'what', 'evidence', 'fix'], properties: { id: { type: 'string' }, severity: { type: 'string' }, where: { type: 'string' }, what: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } } } } } }
const VOTE = { type: 'object', required: ['refuted', 'confidence', 'reason'], properties: { refuted: { type: 'boolean' }, confidence: { type: 'number' }, reason: { type: 'string' } } }
const LENSES = [
  ['contract', 'CONTRACT lens: read the two section files line by line against SPEC §1–§4 as amended and LEAD-DECISIONS rulings 1–13: the map sizes (rope 874, powerful 1040, warm-step 909, stainless 1100, scene-path 1100) vs the real files (read the JPEG headers or CHOSEN.md), the crops (lantern9 0% 50%, edison 50% 30%), the camping-lantern heading override and its setting, the spot line, the fallback guard (no pictured product → no photograph), the own-width srcset rule (never a candidate wider than the file; 854/930/1000/1100 offered), the text-only modifier class and its CSS, the dusk row (two block spans, closing hairline, 16 px above, the facts column at ≥ 901), valid Liquid, schema (no empty text default, no url default, names ≤ 25), bdi isolation, logical properties, reduced motion, no JS.'],
  ['render', 'RENDER lens: look at the pass-2 shots. Rope at 390/360: is the badge gone, is the photograph well framed (panel, trunk)? Path/wall at 390/360/1366: the photograph, the heading, the line, the link. Flood/deck (text-only): do the two hairline rows read as designed, at 390 and 1366 (the facts column)? The dusk row: two lines, closed row, the gap to the facts, the 1366 column alignment with the facts rows (dusk-d-viewport.png). Any product cut by a crop? Any text over a photograph? Anything that now looks worse than pass 1?'],
]
phase('Re-review')
const results = await pipeline(
  LENSES,
  ([lens, role]) => agent(`${COMMON}\n${role}`, { label: `lens:${lens}`, phase: 'Re-review', schema: FIND, effort: 'high' }),
  (r, [lens]) => r ? parallel(r.findings.map(f => () =>
    agent(`${COMMON}\nYou are the SKEPTIC. A «${lens}» reviewer reported this finding on pass 2:\n${JSON.stringify(f)}\nTry to REFUTE it: (1) evidence — open the shot or file it cites and check whether what it describes is really there now (measure; do not trust the description); (2) scope — inside SPEC §1–§5 as amended, or a decision LEAD-DECISIONS.md records with a reason, or out of scope. Default to refuted=true when the evidence is not there or it is out of scope. confidence 0–1. Do not modify files.`, { label: `skeptic:${lens}:${f.id}`, phase: 'Skeptics', schema: VOTE, effort: 'high' })
      .then(v => ({ lens, finding: f, vote: v })))).then(items => ({ lens, verdict: r.verdict, fixesLanded: r.fixesLanded, items: items.filter(Boolean) })) : null
)
const lensResults = results.filter(Boolean)
const all = lensResults.flatMap(r => r.items)
log(`re-review: ${all.length} findings, ${all.filter(x => x.vote && !x.vote.refuted).length} confirmed`)
return { lenses: lensResults.map(r => ({ lens: r.lens, verdict: r.verdict, fixesLanded: r.fixesLanded })), findings: all }