// Home round 2 — per-section shots of the REAL render (the re-mirrored dev-theme home, served locally like every
// screenshot in this repo). Element screenshots, so a section that sits deep in the page is captured whole; a
// viewport shot of the band is added because the sentence's contrast is judged against the photo under it.
// Usage: node brief/side-pages/home2/shoot-sections.js [mirrorDir] [outDir]
const path = require('path'), fs = require('fs'), http = require('http');
const PW = fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest').map(d => `/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad/node_modules/playwright`).find(p => fs.existsSync(p));
const { chromium } = require(PW);
const DIR = process.argv[2] || '/home/user/ElmsNest/brief/side-pages/simplify/verify-after/mirrors/home';
const OUT = process.argv[3] || '/home/user/ElmsNest/brief/side-pages/home2/verify';
const FONT_DIR = '/home/user/ElmsNest/brief/assets/fonts';
const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff': 'font/woff', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.json': 'application/json' };
fs.mkdirSync(OUT, { recursive: true });
function fontFaceCss(port) { let css = ''; for (const f of fs.readdirSync(FONT_DIR)) { const m = /^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f); if (!m) continue; css += `@font-face{font-family:'${m[1] === 'FrankRuhlLibre' ? 'Frank Ruhl Libre' : 'Heebo'}';font-style:normal;font-weight:${m[3]};font-display:swap;src:url(http://127.0.0.1:${port}/__fonts/${f}) format('woff2')}`; } return css; }
(async () => {
  const srv = http.createServer((req, res) => { let p = decodeURIComponent(req.url.split('?')[0]); if (p === '/') p = '/index.html'; const f = p.startsWith('/__fonts/') ? path.join(FONT_DIR, p.slice(9)) : path.join(DIR, p); if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); } res.writeHead(200, { 'content-type': MIME[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(res); });
  await new Promise(r => srv.listen(0, '127.0.0.1', r)); const port = srv.address().port;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const out = {};
  for (const [vk, w, h] of [['s', 360, 640], ['m', 390, 844], ['d', 1366, 900]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, locale: 'he-IL', deviceScaleFactor: 1, isMobile: w < 500, hasTouch: w < 500 });
    const faces = fontFaceCss(port);
    await ctx.route(/^https?:\/\//, r => { const u = r.request().url(); if (/127\.0\.0\.1/.test(u)) return r.continue(); if (/fonts\.googleapis\.com/.test(u)) return r.fulfill({ status: 200, contentType: 'text/css', body: faces }); return r.abort(); });
    const page = await ctx.newPage();
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'load', timeout: 60000 });
    await page.waitForTimeout(2000);
    await page.evaluate(async () => { document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager'); for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 80)); } window.scrollTo(0, 0); });
    await page.waitForTimeout(800);
    await page.addStyleTag({ content: '.hdt-sticky-btn-atc,.hdt-back-top,[class*="back_top"]{display:none!important}' }).catch(() => {});
    for (const sec of ['ens-home-solar', 'ens-home-winter', 'ens-home-band']) {
      const el = await page.$(`.${sec}`); if (!el) { console.log(vk, sec, 'MISSING'); continue; }
      await el.scrollIntoViewIfNeeded(); await page.waitForTimeout(400);
      await el.screenshot({ path: path.join(OUT, `${sec.replace('ens-home-', '')}-${vk}.png`) });
      const box = await el.boundingBox();
      // text boxes relative to the section shot, for verify/contrast.py (the headline on the day scrim, the band sentence)
      const texts = await el.evaluate((node) => { const r0 = node.getBoundingClientRect(); return [...node.querySelectorAll('.ens-home-solar__word, .ens-home-solar__tag, .ens-home-solar__eyebrow, .ens-home-band__h, .ens-hw__h2, .ens-hw__line, .ens-home-solar__txt')].map(t => { const r = t.getBoundingClientRect(); return { cls: t.className, text: t.textContent.trim().slice(0, 30), color: getComputedStyle(t).color, x: Math.round(r.left - r0.left), y: Math.round(r.top - r0.top), w: Math.round(r.width), h: Math.round(r.height) }; }); });
      out[`${sec}-${vk}`] = { w: Math.round(box.width), h: Math.round(box.height), texts };
    }
    // the band and the diptych in the viewport, as a phone shows them (scroll so the section top sits at y=0)
    for (const sec of ['ens-home-solar', 'ens-home-band']) {
      await page.evaluate(s => { const el = document.querySelector('.' + s); window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - (s === 'ens-home-solar' ? 0 : Math.max(0, window.innerHeight - el.getBoundingClientRect().height))); }, sec);
      await page.waitForTimeout(400);
      await page.screenshot({ path: path.join(OUT, `${sec.replace('ens-home-', '')}-${vk}-viewport.png`) });
    }
    await ctx.close();
  }
  fs.writeFileSync(path.join(OUT, 'sizes.json'), JSON.stringify(out, null, 1));
  console.log(JSON.stringify(out));
  await b.close(); srv.close();
})();
