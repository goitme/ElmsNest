export const meta = {
  name: 'owner-feedback-audit',
  description: 'Audit the dev theme against the owner\'s three complaints (complexity, duplication, images) from real screenshots, then critique the lead\'s draft questions',
  phases: [
    { title: 'Audit', detail: 'four independent lenses on the screenshots' },
    { title: 'Critique', detail: 'completeness critic on the draft owner questions' },
  ],
}

const CTX = 'C:\\Users\\covid\\AppData\\Local\\Temp\\claude\\c--Users-covid-Desktop-claude\\bfa8f647-4fec-44c7-8dd1-7c6bb6aaaf08\\scratchpad\\shots\\context.md'
const SLICES = 'C:\\Users\\covid\\AppData\\Local\\Temp\\claude\\c--Users-covid-Desktop-claude\\bfa8f647-4fec-44c7-8dd1-7c6bb6aaaf08\\scratchpad\\shots\\slices'
const REPORT = 'C:\\Users\\covid\\AppData\\Local\\Temp\\claude\\c--Users-covid-Desktop-claude\\bfa8f647-4fec-44c7-8dd1-7c6bb6aaaf08\\scratchpad\\shots\\report.json'
const REPO = 'C:\\Users\\covid\\AppData\\Local\\Temp\\claude\\c--Users-covid-Desktop-claude\\bfa8f647-4fec-44c7-8dd1-7c6bb6aaaf08\\scratchpad\\repo'

const COMMON = `First Read ${CTX} in full. Screenshots are in ${SLICES} (Read them with the Read tool — they are PNG images; read the MOBILE slices in order for home, collection-all, pdp-rope and pdp-path; open desktop slices only where you need to confirm something). The DOM report is ${REPORT}. Theme source (Liquid) is under ${REPO}\\theme if you need to confirm what a section does. Do not modify any file. Be concrete: cite slice filenames for every finding. Do not flatter the design; your job is evidence for the owner's verdict, and equally to say where the owner's verdict is NOT supported by the screenshots.`

const FINDINGS = {
  type: 'object',
  properties: {
    summary: { type: 'string', description: '3-5 sentences, the verdict in plain words' },
    findings: { type: 'array', items: { type: 'object', properties: {
      title: { type: 'string' },
      page: { type: 'string', description: 'home | collection | pdp | cross-page | cart | search | 404' },
      evidence: { type: 'string', description: 'what is visible and in which slice files' },
      severity: { type: 'string', description: 'high | medium | low' },
      recommendation: { type: 'string', description: 'the simplest fix' },
    }, required: ['title', 'page', 'evidence', 'severity', 'recommendation'] } },
    numbers: { type: 'array', items: { type: 'object', properties: { metric: { type: 'string' }, value: { type: 'string' } }, required: ['metric', 'value'] } },
  },
  required: ['summary', 'findings', 'numbers'],
}

phase('Audit')
const LENSES = [
  { key: 'shopper', prompt: `${COMMON}

You are a first-time Israeli shopper on a phone. You want to light a 6-metre pergola and you have never seen this store. You know normal Shopify stores (Dawn / Kalles / Amazon / AliExpress): a grid of product photos with prices, a product page with photos, a variant dropdown, quantity, add-to-cart, a cart drawer.
Walk the screenshots as that shopper: home (home-m-s01..s11) -> collection (collection-all-m-s01..s26) -> product (pdp-rope-m-s01..s11). At every screen ask: do I know what this is, what it wants me to do, and where the buy button is?
Deliverables in findings: (1) every UI pattern that is NEW relative to a standard store, with the slice where it first appears and how many seconds/steps it costs to understand; (2) the number of distinct decisions or controls the shopper meets before add-to-cart on each page; (3) the exact points where you would get lost or give up; (4) what a standard store shows at that point instead. In numbers: screens to reach the first product grid on the collection page, screens to the add-to-cart on the PDP, number of add-to-cart buttons on one PDP, count of novel patterns per page.` },
  { key: 'duplication', prompt: `${COMMON}

You are auditing DUPLICATION. The owner says every page has things repeated twice, "once one way and once another way". For every section on the three pages (the inventory in context.md, verify against the slices) write the single buyer question that section answers (e.g. "what does it cost per metre?", "does it suit my place?", "what are the return terms?", "which products exist?"). Then list every pair or group of sections/elements that answer the SAME question — within one page AND across pages — and say whether they repeat "the same way" or "a different way". Include the compact terms strip under the PDP add-to-cart vs the PDP terms ledger vs the homepage terms ledger vs the goodnight hairline; the PDP stage variant picker vs the PDP ledger rows with their own add-to-cart; the collection ruler vs bands vs ledger vs span (how many times does the same product appear on the collection page? count one product, e.g. the rope lights, across the 26 slices). In numbers: times the four consumer terms appear per page; times each product appears on the collection page; number of sections per page and how many could be deleted with no buyer question left unanswered. In recommendation: the minimal section list per page that still answers every question once.` },
  { key: 'images', prompt: `${COMMON}

You are auditing PRODUCT IMAGES. The owner says the collection shows different images than the products' own photos. Read the collection slices (collection-all-m-s01..s26 and a few desktop ones) and the PDP slices, plus report.json (the img list per page with src tails, and bigSvgs counts). Determine: (1) how many product cards on the collection page show an illustrated glyph/SVG plate instead of a product photograph, and which products (by the Hebrew title on the card); (2) whether any card shows a photo that is not the product's featured image; (3) on the two PDPs, whether the first image shown is the product's featured image (report.json lists img src tails; the Shopify featured images are named like ChatGPTImage...png — compare with the src tails in the pdp pages); (4) how the glyph plates look to a shopper — do they read as "this product has no photo" or as a broken/placeholder card? Also check ${REPO}\\theme\\snippets\\elmsnest-v2-pdp-card.liquid and elmsnest-v2-pdp-image.liquid to confirm the mechanism. In numbers: cards with glyph vs photo on /collections/all; products whose PDP first image != featured image (from the resolver's banned-index logic, list handles). Recommendation: the exact code change that restores "always the store's featured image" everywhere, and what else in the theme depends on the resolver.` },
  { key: 'simplify', prompt: `${COMMON}

You are a senior e-commerce designer asked: keep this store's visual identity (night photography, gold, the serif, the restrained motion) but make every page as SIMPLE to shop as a standard Shopify store. Study the slices for home, collection and pdp. For each of the three pages propose the minimal structure: an ordered list of 3-6 sections, each with one sentence of what it shows, using STANDARD shopping patterns for every action (one product grid with photos + prices on the collection, ONE variant selector + ONE add-to-cart on the PDP, a normal cart drawer) and keeping creativity only in the non-action layers (hero photo, typography, one signature device per page at most). For every existing device in the dev theme (ruler, bands, span, ledger, fit switch, night gallery, facts numeral, ask, atmosphere, switch, night-wall, first-lit, places, terms ledger, goodnight) say KEEP / MERGE INTO x / CUT and why in one line. Target mobile page heights: home <= 6 screens, collection <= 8 screens for 27 products, PDP <= 6 screens. Put the three proposed structures in findings (one finding per page, the structure in recommendation) and the KEEP/MERGE/CUT list as further findings.` },
]

const audits = await parallel(LENSES.map(l => () =>
  agent(l.prompt, { label: `audit:${l.key}`, phase: 'Audit', schema: FINDINGS }).then(r => ({ key: l.key, r }))))
const ok = audits.filter(Boolean)
log(`audits done: ${ok.map(a => a.key).join(', ')}`)

phase('Critique')
const DRAFT = `Q1 direction: keep the night visual language of the dev theme and strip it down to standard shopping patterns, OR start from the live Homepage v3 (light paper page with a night hero) and extend that language to all pages? Default: keep the night look, rebuild structure to be standard-simple.
Q2 images: rule = always the store's own featured image on every card and as the first PDP image, no glyphs, no index-skipping resolver, even where a photo carries baked-in supplier text? Default: yes, real images everywhere.
Q3 the simplicity bar: for every ACTION (browse, choose variant, add to cart, cart) use exactly the patterns a Shopify shopper already knows; creativity only in hero/photography/typography/motion; page height targets home <= 6, collection <= 8, PDP <= 6 screens. Is that the bar, or does the owner want to keep one signature device per page (e.g. price per metre on the PDP)?
Q4 scope and order: fix the three built pages (home, collection, PDP) first, then continue to cart/search/404/content pages in the same simplified language? And the homepage: does the dev theme's homepage replace the live v3, or should v3 stay and only the side pages be built?
Q5 process: the 5-concept -> judges -> adversarial-critique process produced this complexity. Proposal: 3 concepts max, a first-time-shopper judge with veto power, and the owner sees mobile screenshots of the whole flow BEFORE deploy. Agree, or build directly from one simplified spec?`

const CRIT_SCHEMA = { type: 'object', properties: {
  keep: { type: 'array', items: { type: 'string' }, description: 'draft question ids that must stay, with a one-line reason each' },
  drop_or_answer_yourself: { type: 'array', items: { type: 'string' }, description: 'draft question ids the lead should NOT ask because the evidence already answers them, with the answer' },
  missing: { type: 'array', items: { type: 'object', properties: { question: { type: 'string' }, why: { type: 'string' }, default: { type: 'string' } }, required: ['question', 'why', 'default'] }, description: 'questions the owner must answer that the draft omits, ordered by impact' },
  evidence_for_owner: { type: 'array', items: { type: 'string' }, description: 'the 5-8 hardest facts from the audits the lead should put in front of the owner, each with its number and slice reference' },
}, required: ['keep', 'drop_or_answer_yourself', 'missing', 'evidence_for_owner'] }

const critique = await agent(`${COMMON}

You are the completeness critic. The lead is about to ask the store owner the questions needed before fixing the dev theme. Here are the four audits (JSON) and the lead's draft questions.

AUDITS:
${JSON.stringify(ok, null, 1)}

DRAFT QUESTIONS:
${DRAFT}

Rules: the owner is a non-technical business owner who answers briefly in Arabic and often says "do your recommendation". A question is worth asking only if different answers lead to materially different work AND the evidence cannot settle it. Find what the draft misses (e.g. what to do with the 16 "no clean photo" products, whether the products' Hebrew titles/prices are fine, whether the WhatsApp/email CTA, the cookie banner covering the fold, the collection navigation model — 4 places vs one catalogue —, the cart drawer, the live-vs-dev homepage conflict need a decision). Keep the final list to at most 6 questions in total including kept draft ones.`, { label: 'critic:completeness', phase: 'Critique', schema: CRIT_SCHEMA })

return { audits: ok, critique }