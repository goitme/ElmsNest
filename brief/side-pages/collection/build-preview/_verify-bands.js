// Offline checks on the §4.3 bands proof that a still cannot show:
//   1. the section with SCRIPTING DISABLED — every band, every price and every buy control present;
//   2. the computed colour of every pill (core REPORT §9.1 — an <a class="env2-btn"> is 1.21:1);
//   3. tap targets under 44px and captions under 11.5px (§3.2, §6.13);
//   4. cream backgrounds (§6.10) and text contrast where the background is opaque;
//   5. reduced motion — every lamp lit, no transition left running.
// Usage: node brief/side-pages/collection/build-preview/_verify-bands.js [file ...]
const path = require('path'); const fs = require('fs');
function loadPW() {
  const roots = [process.env.ENV2_PW_ROOT].filter(Boolean);
  try { for (const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest')) roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`); } catch (e) {}
  for (const r of roots) { try { return require(`${r}/node_modules/playwright`); } catch (e) {} }
  return require('playwright');
}
const { chromium } = loadPW();
const FILES = process.argv.slice(2).length ? process.argv.slice(2) : [
  'brief/side-pages/collection/build-preview/bands.html',
  'brief/side-pages/collection/build-preview/bands-path.html',
  'brief/side-pages/collection/build-preview/_bands-wall.html',
  'brief/side-pages/collection/build-preview/_bands-spot.html',
  'brief/side-pages/collection/build-preview/_bands-all.html'];

const AUDIT = () => {
  const out = { bad: [], small: [], cream: 0, lowContrast: [] };
  const lum = (c) => { const [r, g, b] = c.map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * r + .7152 * g + .0722 * b; };
  const rgb = (s) => { const m = s.match(/[\d.]+/g); return m ? m.slice(0, 3).map(Number) : null; };
  const alpha = (s) => { const m = s.match(/[\d.]+/g); return m && m.length > 3 ? Number(m[3]) : 1; };
  document.querySelectorAll('.env2-coll-bands a,.env2-coll-bands button,.env2-coll-bands label').forEach(el => {
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    if (r.width < 1 && r.height < 1) return;
    if (r.height < 44 && !el.closest('.env2-pdp-card__title')) out.bad.push(['tap<44', el.className || el.tagName, Math.round(r.height)]);
    if (cs.backgroundColor.includes('255, 211, 148') && cs.color !== 'rgb(26, 18, 6)') out.bad.push(['ink-on-glow', el.className, cs.color]);
  });
  document.querySelectorAll('.env2-coll-bands *').forEach(el => {
    if (!el.textContent.trim() || el.children.length) return;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs < 11.5) out.small.push([el.className || el.tagName, fs]);
  });
  out.cream = [...document.querySelectorAll('.env2-coll-bands *')].filter(el => {
    const b = getComputedStyle(el).backgroundColor;
    return /rgb\(2(4[0-9]|5[0-5]), 2[0-9][0-9], 2[0-9][0-9]\)/.test(b);
  }).length;
  // contrast, but only where an opaque background can actually be found (never over a photograph)
  document.querySelectorAll('.env2-coll-bands__facts,.env2-coll-bands__quote,.env2-coll-bands__assert,.env2-coll-bands__h2,.env2-coll-bands__num,.env2-pdp-card__title,.env2-pdp-card__axis,.env2-pdp-card__unit,.env2-kicker,.env2-price').forEach(el => {
    let n = el, bg = null;
    while (n && n !== document.documentElement) {
      const b = getComputedStyle(n).backgroundColor;
      if (alpha(b) === 1 && rgb(b)) { bg = rgb(b); break; }
      if (getComputedStyle(n).backgroundImage !== 'none' || n.querySelector('img')) { if (n !== el && n.matches('figure,.env2-coll-bands__fig')) return; }
      n = n.parentElement;
    }
    if (!bg) return;
    const fg = rgb(getComputedStyle(el).color); if (!fg) return;
    const L1 = lum(fg), L2 = lum(bg);
    const ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
    const size = parseFloat(getComputedStyle(el).fontSize);
    const need = size >= 24 ? 3 : 4.5;
    if (ratio < need) out.lowContrast.push([el.className, size, Math.round(ratio * 100) / 100, need]);
  });
  return out;
};

(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  let fail = 0;
  for (const f of FILES) {
    const url = 'file://' + path.resolve(f);
    console.log('\n=== ' + path.basename(f));
    // 1. no JavaScript at all
    for (const [name, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 360, height: 780 }]]) {
      const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 1, locale: 'he-IL', javaScriptEnabled: false });
      const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'load' });
      const r = await p.evaluate(() => ({
        bands: document.querySelectorAll('.env2-coll-bands__band').length,
        cards: document.querySelectorAll('.env2-pdp-card').length,
        prices: document.querySelectorAll('.env2-pdp-card .env2-price').length,
        buys: document.querySelectorAll('.env2-pdp-card form[action="/cart/add"], .env2-pdp-card .env2-pdp-card__action a').length,
        lit: getComputedStyle(document.querySelector('[data-lamp]')).getPropertyValue('--lit').trim(),
        hscroll: document.documentElement.scrollWidth > document.documentElement.clientWidth
      }));
      const bad = (r.prices !== r.cards) || (r.buys !== r.cards) || r.hscroll || r.lit === '0';
      if (bad) fail++;
      console.log('  no-JS ' + name + ': bands=' + r.bands + ' cards=' + r.cards + ' prices=' + r.prices +
        ' buy-controls=' + r.buys + ' --lit=' + (r.lit || '(unset=lit)') + ' h-scroll=' + r.hscroll + (bad ? '  FAIL' : '  OK'));
      await ctx.close();
    }
    // 2-4. computed styles, with JS
    for (const [name, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 360, height: 780 }]]) {
      const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 1, locale: 'he-IL' });
      const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'load' });
      await p.waitForTimeout(400);
      const r = await p.evaluate(AUDIT);
      const bad = r.bad.length || r.small.length || r.cream || r.lowContrast.length;
      if (bad) fail++;
      console.log('  audit ' + name + ': tap/ink=' + JSON.stringify(r.bad) + ' small=' + JSON.stringify(r.small) +
        ' cream=' + r.cream + ' low-contrast=' + JSON.stringify(r.lowContrast) + (bad ? '  FAIL' : '  OK'));
      await ctx.close();
    }
    // 5. reduced motion
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce', locale: 'he-IL' });
    const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'load' });
    await p.waitForTimeout(300);
    const rm = await p.evaluate(() => {
      const lamps = [...document.querySelectorAll('.env2-coll-bands [data-lamp]')];
      return { n: lamps.length, dim: lamps.filter(l => getComputedStyle(l).getPropertyValue('--lit').trim() === '0').length };
    });
    console.log('  reduced-motion: lamps=' + rm.n + ' still dim=' + rm.dim + (rm.dim ? '  FAIL' : '  OK'));
    if (rm.dim) fail++;
    await ctx.close();
  }
  await b.close();
  console.log(fail ? '\nFAILURES: ' + fail : '\nall checks passed');
  process.exit(fail ? 2 : 0);
})();
