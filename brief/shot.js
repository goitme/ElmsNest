// Usage: node brief/shot.js <path/to/index.html> <out-prefix>
// Renders the mockup offline (file://) at desktop 1440 and mobile 390, full page, 2x.
// Writes <out-prefix>-desktop.png, <out-prefix>-mobile.png and prints page heights.
const path = require('path');
const fs = require('fs');
// playwright lives in the session scratchpad (node_modules is gitignored); resolve it from ENV2_PW_ROOT,
// then any scratchpad under /tmp/claude-0, then a plain require.
function loadPlaywright() {
  const roots = [process.env.ENV2_PW_ROOT].filter(Boolean);
  try { for (const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest')) roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`); } catch (e) {}
  for (const r of roots) { try { return require(`${r}/node_modules/playwright`); } catch (e) {} }
  return require('playwright');
}
const { chromium } = loadPlaywright();
(async () => {
  const [,, htmlPath, outPrefix] = process.argv;
  if (!htmlPath || !outPrefix) { console.error('usage: node shot.js <html> <out-prefix>'); process.exit(2); }
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const url = 'file://' + path.resolve(htmlPath);
  for (const [name, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844 }]]) {
    const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 2, locale: 'he-IL', reducedMotion: 'no-preference' });
    await ctx.route(/^https?:\/\//, r => r.abort()); // offline: only file:// assets load
    const p = await ctx.newPage();
    const errors = [];
    p.on('pageerror', e => errors.push(String(e)));
    await p.goto(url, { waitUntil: 'load', timeout: 60000 });
    await p.evaluate(async () => {
      document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager');
      // The theme sets html{scroll-behavior:smooth}; a smooth walk never lands on most offsets, so the
      // IntersectionObserver / sweep in elmsnest-v2-base misses lamps. Force instant jumps for the walk.
      document.documentElement.style.scrollBehavior = 'auto';
      for (let y = 0; y < document.body.scrollHeight; y += 400) { window.scrollTo({ top: y, behavior: 'instant' }); await new Promise(r => setTimeout(r, 70)); }
      window.scrollTo({ top: 0, behavior: 'instant' });
    });
    await p.waitForTimeout(2800); // lamp filter transitions run 1.6-2.4 s; let every lamp finish lighting
    await p.screenshot({ path: `${outPrefix}-${name}.png`, fullPage: true });
    // also a first-screen crop, since above-the-fold is what a visitor judges
    await p.screenshot({ path: `${outPrefix}-${name}-fold.png`, fullPage: false });
    const h = await p.evaluate(() => document.body.scrollHeight);
    const horiz = await p.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
    console.log(`${name}: height=${h}px horizontal-overflow=${horiz} js-errors=${errors.length}${errors.length ? ' ' + errors.slice(0,3).join(' | ') : ''}`);
    await ctx.close();
  }
  await b.close();
})();
