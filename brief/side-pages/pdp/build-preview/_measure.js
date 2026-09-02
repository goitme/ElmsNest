// node brief/side-pages/pdp/build-preview/_measure.js <html> [width] [height]
const path = require('path'); const fs = require('fs');
function loadPlaywright() {
  const roots = [process.env.ENV2_PW_ROOT].filter(Boolean);
  try { for (const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest')) roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`); } catch (e) {}
  for (const r of roots) { try { return require(`${r}/node_modules/playwright`); } catch (e) {} }
  return require('playwright');
}
const { chromium } = loadPlaywright();
(async () => {
  const [, , htmlPath, W, H] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  for (const [name, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: +(W || 390), height: +(H || 844) }]]) {
    const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 1, locale: 'he-IL' });
    await ctx.route(/^https?:\/\//, r => r.abort());
    const p = await ctx.newPage();
    await p.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load' });
    await p.waitForTimeout(1200);
    const out = await p.evaluate(() => {
      const sel = ['#env2-pdp-stage', '.env2-pdp-stage__body', '.env2-pdp-stage__txt', '.env2-pdp-stage__h1',
        '.env2-pdp-stage__buy', '.env2-pdp-stage__atc', '.env2-pdp-stage__terms', '.env2-pdp-stage__rail',
        '.env2-pdp-stage__track', '.env2-pdp-stage__small', '.env2-pdp-stage__fit', '.env2-pdp-bar'];
      const rows = sel.map(s => {
        const e = document.querySelector(s); if (!e) return [s, 'MISSING'];
        const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
        return [s, `x=${Math.round(r.left)}..${Math.round(r.right)} w=${Math.round(r.width)} y=${Math.round(r.top + scrollY)}..${Math.round(r.bottom + scrollY)} h=${Math.round(r.height)} color=${cs.color} bg=${cs.backgroundColor}`];
      });
      // widest element that exceeds the viewport
      const wide = [];
      document.querySelectorAll('#env2-pdp-stage *').forEach(e => {
        const r = e.getBoundingClientRect();
        if (r.width > innerWidth + 1 || r.left < -1 || r.right > innerWidth + 1) wide.push((e.className.baseVal !== undefined ? e.tagName : (e.className || e.tagName)) + ' w=' + Math.round(r.width) + ' l=' + Math.round(r.left) + ' r=' + Math.round(r.right));
      });
      // smallest font sizes and tap targets
      const fonts = new Set(); const small = [];
      document.querySelectorAll('#env2-pdp-stage *').forEach(e => {
        if (!e.textContent || !e.textContent.trim()) return;
        const cs = getComputedStyle(e); fonts.add(cs.fontSize);
      });
      document.querySelectorAll('#env2-pdp-stage a,#env2-pdp-stage button,#env2-pdp-stage select,#env2-pdp-stage label').forEach(e => {
        const r = e.getBoundingClientRect();
        if (r.height && r.height < 44) small.push((e.className || e.tagName) + ' h=' + Math.round(r.height));
      });
      return { rows, wide: wide.slice(0, 12), fonts: [...fonts].sort((a, b) => parseFloat(a) - parseFloat(b)).slice(0, 6), small: small.slice(0, 10), docH: document.body.scrollHeight };
    });
    console.log('=== ' + name + ' ' + vp.width + 'x' + vp.height + ' docH=' + out.docH);
    out.rows.forEach(r => console.log('  ' + r[0].padEnd(32) + r[1]));
    console.log('  OVERFLOW: ' + (out.wide.join(' | ') || 'none'));
    console.log('  FONTS: ' + out.fonts.join(' '));
    console.log('  TAP<44: ' + (out.small.join(' | ') || 'none'));
    await ctx.close();
  }
  await b.close();
})();
