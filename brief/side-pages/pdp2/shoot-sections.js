// PDP round 2 — per-section shots of the REAL render (a re-mirrored dev-theme product page, served locally like every
// screenshot in this repo), generalised from home2/shoot-sections.js: the section classes and the text selectors are
// arguments, so the same harness measures any product page and any fix experiment.
// Usage: node brief/side-pages/pdp2/shoot-sections.js <mirrorDir> <outDir> --sections=ens-pdp-scene,ens-pdp-dusk
//          [--text=".ens-pdp-scene__h,.ens-pdp-scene__line"] [--css=candidate.css] [--hide-text] [--views=s,m,d]
//   --sections: root classes of the sections to shoot (element screenshots: <short>-<vk>.png, short = class minus 'ens-pdp-')
//   --text:     selectors of the text painted over photographs (their boxes go to sizes.json for verify/contrast.py)
//   --css:      candidate CSS injected after load (fix experiments; prefix selectors with `html body` to out-rank inline styles)
//   --hide-text: shoot with the glyphs and their shadows transparent (boxes, scrims and backings stay) so contrast.py measures
//                the TRUE background behind the glyphs — write these to <outDir>-bg/ and contrast.py finds them.
const path = require('path'), fs = require('fs'), http = require('http');
const PW = fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest').map(d => `/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad/node_modules/playwright`).find(p => fs.existsSync(p));
const { chromium } = require(PW);
const argv = process.argv.slice(2);
const pos = argv.filter(a => !a.startsWith('--'));
const DIR = pos[0]; const OUT = pos[1];
const opt = k => (argv.find(a => a.startsWith(`--${k}=`)) || '').slice(k.length + 3);
const SECTIONS = opt('sections').split(',').filter(Boolean);
const TEXT = opt('text') || '';
const CSS = opt('css');
const HIDE = argv.includes('--hide-text');
const VIEWS = (opt('views') || 's,m,d').split(',');
if (!DIR || !OUT || !SECTIONS.length) { console.error('usage: shoot-sections.js <mirrorDir> <outDir> --sections=a,b [--text=sel] [--css=f] [--hide-text]'); process.exit(2); }
const FONT_DIR = '/home/user/ElmsNest/brief/assets/fonts';
const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.woff': 'font/woff', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.json': 'application/json' };
fs.mkdirSync(OUT, { recursive: true });
function fontFaceCss(port) { let css = ''; for (const f of fs.readdirSync(FONT_DIR)) { const m = /^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f); if (!m) continue; css += `@font-face{font-family:'${m[1] === 'FrankRuhlLibre' ? 'Frank Ruhl Libre' : 'Heebo'}';font-style:normal;font-weight:${m[3]};font-display:swap;src:url(http://127.0.0.1:${port}/__fonts/${f}) format('woff2');unicode-range:${m[2] === 'hebrew' ? 'U+0590-05FF,U+200C-2010,U+20AA,U+25CC,U+FB1D-FB4F' : 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'};}`; } return css; }
(async () => {
  const srv = http.createServer((req, res) => { let p = decodeURIComponent(req.url.split('?')[0]); if (p === '/') p = '/index.html'; const f = p.startsWith('/__fonts/') ? path.join(FONT_DIR, p.slice(9)) : path.join(DIR, p); if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); } res.writeHead(200, { 'Content-Type': MIME[path.extname(f).toLowerCase()] || 'application/octet-stream', 'Access-Control-Allow-Origin': '*' }); if (f === path.join(DIR, 'index.html')) return res.end(fs.readFileSync(f, 'utf8').replace(/(["'])a\//g, '$1/a/')); fs.createReadStream(f).pipe(res); });
  await new Promise(r => srv.listen(0, '127.0.0.1', r)); const port = srv.address().port;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const out = {};
  const ALL = { s: [360, 640], m: [390, 844], d: [1366, 900] };
  for (const vk of VIEWS) {
    const [w, h] = ALL[vk];
    const ctx = await b.newContext({ viewport: { width: w, height: h }, locale: 'he-IL', deviceScaleFactor: 1, isMobile: w < 500, hasTouch: w < 500 });
    const faces = fontFaceCss(port);
    await ctx.route(/^https?:\/\//, r => { const u = r.request().url(); if (/127\.0\.0\.1/.test(u)) return r.continue(); if (/fonts\.googleapis\.com/.test(u)) return r.fulfill({ status: 200, contentType: 'text/css', body: faces }); return r.abort(); });
    const page = await ctx.newPage();
    await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'load', timeout: 60000 });
    await page.waitForTimeout(2000);
    await page.evaluate(async () => { document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager'); for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 80)); } window.scrollTo(0, 0); });
    await page.waitForTimeout(800);
    await page.addStyleTag({ content: '.hdt-sticky-btn-atc,.hdt-back-top,[class*="back_top"],hdt-sticky-btn-atc{display:none!important}' }).catch(() => {});
    if (CSS) { await page.addStyleTag({ content: fs.readFileSync(CSS, 'utf8') }); await page.waitForTimeout(300); }
    if (HIDE && TEXT) { await page.addStyleTag({ content: `${TEXT}{color:transparent!important;text-shadow:none!important}` }); await page.waitForTimeout(200); }
    for (const sec of SECTIONS) {
      const short = sec.replace(/^ens-pdp-/, '');
      const el = await page.$(`.${sec}`); if (!el) { console.log(vk, sec, 'MISSING'); out[`${short}-${vk}`] = { missing: true }; continue; }
      await el.scrollIntoViewIfNeeded(); await page.waitForTimeout(400);
      await el.screenshot({ path: path.join(OUT, `${short}-${vk}.png`) });
      const box = await el.boundingBox();
      const texts = TEXT ? await el.evaluate((node, sel) => { const r0 = node.getBoundingClientRect(); return [...node.querySelectorAll(sel)].filter(t => t.getClientRects().length).map(t => { const r = t.getBoundingClientRect(); const cs = getComputedStyle(t); return { cls: t.className, text: (t.textContent || '').trim().slice(0, 40), x: Math.round(r.left - r0.left), y: Math.round(r.top - r0.top), w: Math.round(r.width), h: Math.round(r.height), color: cs.color, size: cs.fontSize }; }); }, TEXT) : [];
      out[`${short}-${vk}`] = { w: Math.round(box.width), h: Math.round(box.height), texts };
      // the section as a phone shows it: scrolled so its top sits at y=0 (or its bottom at the fold when it is taller)
      await page.evaluate(s => { const el = document.querySelector('.' + s); const r = el.getBoundingClientRect(); window.scrollTo(0, r.top + window.scrollY - Math.max(0, Math.min(0, window.innerHeight - r.height))); }, sec);
      await page.waitForTimeout(300);
      await page.screenshot({ path: path.join(OUT, `${short}-${vk}-viewport.png`) });
    }
    await ctx.close();
  }
  fs.writeFileSync(path.join(OUT, 'sizes.json'), JSON.stringify(out, null, 1));
  console.log(JSON.stringify(Object.fromEntries(Object.entries(out).map(([k, v]) => [k, v.missing ? 'MISSING' : `${v.w}x${v.h} texts=${v.texts.length}`]))));
  await b.close(); srv.close();
})();
