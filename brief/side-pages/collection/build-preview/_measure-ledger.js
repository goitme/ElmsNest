// Measures §4.5's non-negotiables on a rendered ledger page, at 1440, 390 and 360, with JS on and OFF.
// Usage: node _measure-ledger.js <file...>
const path = require('path');
const fs = require('fs');
function loadPlaywright(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
  try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
  for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const { chromium } = loadPlaywright();

const PROBE = () => {
  const px = n => Math.round(n);
  const sec = document.querySelector('#env2-coll-ledger');
  if (!sec) return { none: true };
  const box = el => el ? (r => ({ t: px(r.top + scrollY), b: px(r.bottom + scrollY), l: px(r.left), r: px(r.right), w: px(r.width), h: px(r.height) }))(el.getBoundingClientRect()) : null;
  const out = { pageH: px(document.body.scrollHeight), horiz: document.documentElement.scrollWidth > document.documentElement.clientWidth };
  out.rows = [];
  sec.querySelectorAll('.env2-coll-ledger__row').forEach(r => {
    const k = r.querySelector('.env2-coll-ledger__k');
    const num = k.querySelector('bdi'), u = k.querySelector('.env2-coll-ledger__u');
    const kb = box(k), nb = box(num), ub = box(u);
    out.rows.push({ n: num.textContent, kh: kb.h, kw: kb.w,
      unitOnOwnLine: ub.t >= nb.b - 2,
      prices: [...r.querySelectorAll('.env2-coll-ledger__price')].map(p => box(p).l),
      pers: [...r.querySelectorAll('.env2-coll-ledger__per')].filter(p => p.textContent.trim()).map(p => box(p).l),
      rowH: box(r).h });
  });
  out.small = [];
  sec.querySelectorAll('a,button,input,label').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width < 1 && r.height < 1) return;
    if (el.getAttribute('aria-hidden') === 'true') return;
    if (r.height < 44 || r.width < 44) out.small.push({ cls: el.className.toString().slice(0, 40), w: px(r.width), h: px(r.height), txt: el.textContent.trim().slice(0, 22) });
  });
  out.tiny = [];
  sec.querySelectorAll('*').forEach(el => {
    let hasText = false; el.childNodes.forEach(n => { if (n.nodeType === 3 && n.textContent.trim()) hasText = true; });
    if (!hasText) return;
    const fs2 = parseFloat(getComputedStyle(el).fontSize);
    if (fs2 < 13) out.tiny.push({ cls: el.className.toString().slice(0, 36), fs: fs2, txt: el.textContent.trim().slice(0, 18) });
  });
  out.cream = [];
  sec.querySelectorAll('*').forEach(el => {
    const bg = getComputedStyle(el).backgroundColor;
    const m = bg.match(/rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)/); if (!m) return;
    const [r, g, b] = [+m[1], +m[2], +m[3]]; const a = m[4] === undefined ? 1 : +m[4];
    const rb = el.getBoundingClientRect(); if (rb.width < 24 || rb.height < 24) return;
    const glow = (r > 240 && g > 190 && b > 130);
    if (a > .5 && !glow && r > 150 && g > 130 && b > 100 && r >= g && g >= b) out.cream.push({ cls: el.className.toString().slice(0, 36), bg });
  });
  // contrast of every text run against the page ground
  const lum = c => { const s = c / 255; return s <= .03928 ? s / 12.92 : Math.pow((s + .055) / 1.055, 2.4); };
  const L = (r, g, b) => .2126 * lum(r) + .7152 * lum(g) + .0722 * lum(b);
  const parse = s => { const m = s.match(/rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)/); return m ? [+m[1], +m[2], +m[3], m[4] === undefined ? 1 : +m[4]] : null; };
  const ground = [2, 3, 6];
  out.low = [];
  sec.querySelectorAll('*').forEach(el => {
    let hasText = false; el.childNodes.forEach(n => { if (n.nodeType === 3 && n.textContent.trim()) hasText = true; });
    if (!hasText) return;
    const cs = getComputedStyle(el); const fg = parse(cs.color); if (!fg) return;
    let bgc = ground; let p = el;
    while (p && p !== document.body) { const b2 = parse(getComputedStyle(p).backgroundColor); if (b2 && b2[3] > .5) { bgc = b2; break; } p = p.parentElement; }
    const l1 = L(fg[0], fg[1], fg[2]), l2 = L(bgc[0], bgc[1], bgc[2]);
    const ratio = (Math.max(l1, l2) + .05) / (Math.min(l1, l2) + .05);
    const size = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight, 10) >= 700;
    const need = (size >= 24 || (size >= 18.66 && bold)) ? 3 : 4.5;
    if (ratio < need) out.low.push({ cls: el.className.toString().slice(0, 36), ratio: Math.round(ratio * 100) / 100, need, fs: size, txt: el.textContent.trim().slice(0, 20) });
  });
  // the foot, and the row-link hrefs
  const rest = sec.querySelector('.env2-coll-ledger__rest');
  out.foot = rest ? rest.textContent.replace(/\s+/g, ' ').trim() : null;
  out.links = [...sec.querySelectorAll('.env2-coll-ledger__k')].map(a => a.getAttribute('href') + '|' + (a.getAttribute('data-stop') || ''));
  return out;
};

(async () => {
  const files = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  for (const f of files) {
    console.log('\n=== ' + path.basename(f));
    for (const [name, vp, js, rm] of [['desktop', { width: 1440, height: 900 }, true, 'no-preference'],
                                      ['mobile', { width: 390, height: 844 }, true, 'no-preference'],
                                      ['mobile-nojs', { width: 390, height: 844 }, false, 'no-preference'],
                                      ['360-reduced', { width: 360, height: 800 }, true, 'reduce']]) {
      const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 1, locale: 'he-IL', javaScriptEnabled: js, reducedMotion: rm });
      await ctx.route(/^https?:\/\//, r => r.abort());
      const p = await ctx.newPage();
      await p.goto('file://' + path.resolve(f), { waitUntil: 'load' });
      await p.waitForTimeout(js ? 1500 : 500);
      const o = await p.evaluate(PROBE);
      if (o.none) { console.log('  ' + name + ': the section prints nothing'); await ctx.close(); continue; }
      const priceL = [...new Set(o.rows.flatMap(r => r.prices))];
      const perL = [...new Set(o.rows.flatMap(r => r.pers))];
      const wrapped = o.rows.filter(r => r.unitOnOwnLine).map(r => r.n);
      console.log(`  ${name}: page=${o.pageH} horiz=${o.horiz} rows=${o.rows.length} rowH=${[...new Set(o.rows.map(r => r.rowH))].join(',')}`);
      console.log(`    numeral box ${[...new Set(o.rows.map(r => r.kw + 'x' + r.kh))].join(' ')} · unit on its own line: ${wrapped.length ? '!! ' + wrapped.join(',') : 'no'}`);
      console.log(`    price inline-start x: ${priceL.length} distinct ${JSON.stringify(priceL.slice(0, 6))} · per x: ${perL.length} distinct ${JSON.stringify(perL.slice(0, 4))}`);
      if (o.small.length) console.log('    !! tap targets <44px: ' + JSON.stringify(o.small));
      if (o.tiny.length) console.log('    !! font-size <13px: ' + JSON.stringify(o.tiny));
      if (o.cream.length) console.log('    !! cream surface: ' + JSON.stringify(o.cream));
      if (o.low.length) console.log('    !! contrast: ' + JSON.stringify(o.low));
      if (name === 'desktop') { console.log('    links: ' + o.links.slice(0, 4).join(' ')); console.log('    foot: ' + (o.foot || '').slice(0, 220)); }
      await ctx.close();
    }
  }
  await b.close();
})();
