// Measures the §4.1 non-negotiables on a rendered scene page, at 1440x900 and 390x844, with JS on and
// with JS OFF, plus contrast and tap targets. Usage: node _measure-scene.js <file...>
const path = require('path');
const fs = require('fs');
function loadPlaywright(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
  try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
  for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const { chromium } = loadPlaywright();

const PROBE = () => {
  const px = n => Math.round(n);
  const sec = document.querySelector('#env2-coll-scene');
  const q = s => sec.querySelector(s);
  const box = el => el ? (r => ({ t: px(r.top + scrollY), b: px(r.bottom + scrollY), l: px(r.left), r: px(r.right), w: px(r.width), h: px(r.height) }))(el.getBoundingClientRect()) : null;
  const cta = q('.env2-coll-scene__card .env2-btn');
  const out = {
    stage: box(q('.env2-coll-scene__stage')),
    type: box(q('.env2-coll-scene__type')),
    h1: box(q('h1')),
    counts: box(q('.env2-coll-scene__counts')),
    card: box(q('.env2-coll-scene__card')),
    price: box(q('.env2-pdp-card__price')),
    cta: box(cta),
    ctaText: cta ? cta.textContent.trim() : null,
    pin: box(q('.env2-coll-scene__pin .env2-coll-scene__tag')),
    below: box(q('.env2-coll-scene__below')),
    pageH: px(document.body.scrollHeight),
    horiz: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  };
  // tap targets: every interactive element in the section
  out.small = [];
  sec.querySelectorAll('a,button,input,label,select').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width < 1 && r.height < 1) return;
    if (el.getAttribute("aria-hidden") === "true" || el.getAttribute("tabindex") === "-1") return;
    // a quiet text link extends its hit area with a ::before overlay (the core does this on mobile,
    // this section does it on both) — measure the effective box, not the text box.
    let w = r.width, h = r.height;
    for (const pe of ['::before', '::after']) {
      const cs = getComputedStyle(el, pe);
      if (cs.content && cs.content !== 'none' && cs.position === 'absolute') {
        const t = parseFloat(cs.top) || 0, b = parseFloat(cs.bottom) || 0, l = parseFloat(cs.left) || 0, rr = parseFloat(cs.right) || 0;
        h = Math.max(h, r.height - t - b); w = Math.max(w, r.width - l - rr);
      }
    }
    if (h < 44 || w < 44) out.small.push({ tag: el.tagName, cls: el.className.toString().slice(0, 46), w: px(w), h: px(h), txt: el.textContent.trim().slice(0, 24) });
  });
  // font sizes below the 13px caption floor
  out.tiny = [];
  sec.querySelectorAll('*').forEach(el => {
    if (!el.childNodes.length) return;
    let hasText = false; el.childNodes.forEach(n => { if (n.nodeType === 3 && n.textContent.trim()) hasText = true; });
    if (!hasText) return;
    const fs2 = parseFloat(getComputedStyle(el).fontSize);
    if (fs2 < 13) out.tiny.push({ cls: el.className.toString().slice(0, 40), fs: fs2, txt: el.textContent.trim().slice(0, 20) });
  });
  // cream / beige / brown surfaces painted by the page (not inside a photograph)
  out.cream = [];
  sec.querySelectorAll('*').forEach(el => {
    const bg = getComputedStyle(el).backgroundColor;
    const m = bg.match(/rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)/);
    if (!m) return; const [r, g, b] = [+m[1], +m[2], +m[3]]; const a = m[4] === undefined ? 1 : +m[4];
    const rb=el.getBoundingClientRect(); if (rb.width<24 || rb.height<24) return;
    const glow = (r>240&&g>190&&b>130); if (a > .5 && !glow && r > 150 && g > 130 && b > 100 && r >= g && g >= b) out.cream.push({ cls: el.className.toString().slice(0, 40), bg });
  });
  return out;
};

(async () => {
  const files = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  for (const f of files) {
    console.log('\n=== ' + path.basename(f));
    for (const [name, vp, js] of [['desktop', { width: 1440, height: 900 }, true],
                                  ['mobile', { width: 390, height: 844 }, true],
                                  ['mobile-nojs', { width: 390, height: 844 }, false],
                                  ['mobile-360', { width: 360, height: 800 }, true]]) {
      const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 1, locale: 'he-IL', javaScriptEnabled: js });
      await ctx.route(/^https?:\/\//, r => r.abort());
      const p = await ctx.newPage();
      await p.goto('file://' + path.resolve(f), { waitUntil: 'load' });
      await p.waitForTimeout(js ? 2200 : 600);
      const o = await p.evaluate(PROBE);
      const fold = vp.height;
      const inFold = v => v === null ? 'n/a' : (v <= fold ? 'IN' : 'OUT +' + (v - fold));
      console.log(`  ${name}: page=${o.pageH} stage=${o.stage.h} horiz=${o.horiz}`);
      console.log(`    h1 bottom ${o.h1.b} ${inFold(o.h1.b)} · counts bottom ${o.counts ? o.counts.b : '-'} ${inFold(o.counts && o.counts.b)}`);
      console.log(`    price bottom ${o.price ? o.price.b : '-'} ${inFold(o.price && o.price.b)} · CTA "${o.ctaText}" bottom ${o.cta ? o.cta.b : '-'} ${inFold(o.cta && o.cta.b)}`);
      console.log(`    card ${o.card ? o.card.w + 'x' + o.card.h + ' @' + o.card.t : '-'} · pin ${o.pin ? o.pin.w + 'x' + o.pin.h + ' @' + o.pin.t : 'none'}`);
      if (o.small.length) console.log('    !! tap targets <44px: ' + JSON.stringify(o.small));
      if (o.tiny.length) console.log('    !! font-size <13px: ' + JSON.stringify(o.tiny));
      if (o.cream.length) console.log('    !! cream surface: ' + JSON.stringify(o.cream));
      await ctx.close();
    }
  }
  await b.close();
})();
