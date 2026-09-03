// Usage: node brief/shot-http.js <path/to/index.html> <out-prefix> [--rm]
// Like shot.js, but serves the mirror directory over http://127.0.0.1 so Kalles' module scripts
// (importmap + cross-origin modules, which never run from file://) execute. Same viewports/outputs.
const path = require('path'); const fs = require('fs'); const http = require('http');
function loadPlaywright() {
  const roots = [process.env.ENV2_PW_ROOT].filter(Boolean);
  try { for (const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest')) roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`); } catch (e) {}
  for (const r of roots) { try { return require(`${r}/node_modules/playwright`); } catch (e) {} }
  return require('playwright');
}
const { chromium } = loadPlaywright();
// TYPOGRAPHER-01: the two brand faces come from fonts.googleapis.com, which this box cannot reach,
// and the "FRL Fallback" chain (David / Times New Roman / Noto Serif Hebrew) resolves to nothing that
// is installed here — so every render before this was shot in a generic serif and a generic sans, and
// every type verdict taken from one was a verdict on DejaVu. The .woff2 files are already in the repo;
// they are served locally and the Google stylesheet request is fulfilled with @font-face rules for
// them, so the mirror renders in real Frank Ruhl Libre and real Heebo.
const FONT_DIR = '/home/user/ElmsNest/brief/assets/fonts';
const FONT_FAMILY = { FrankRuhlLibre: 'Frank Ruhl Libre', Heebo: 'Heebo' };
const FONT_RANGE = {
  hebrew: 'U+0590-05FF,U+200C-2010,U+20AA,U+25CC,U+FB1D-FB4F',
  latin: 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215'
};
function fontFaceCss(port) {
  let css = '';
  let files = [];
  try { files = fs.readdirSync(FONT_DIR); } catch (e) { return ''; }
  for (const f of files) {
    const m = /^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f);
    if (!m) continue;
    css += `@font-face{font-family:"${FONT_FAMILY[m[1]]}";font-style:normal;font-weight:${m[3]};font-display:swap;` +
           `src:url(http://127.0.0.1:${port}/__fonts/${f}) format("woff2");unicode-range:${FONT_RANGE[m[2]]}}\n`;
  }
  return css;
}
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.gif': 'image/gif', '.woff': 'font/woff', '.woff2': 'font/woff2', '.ico': 'image/x-icon', '.json': 'application/json' };
(async () => {
  const [,, htmlPath, outPrefix, flag] = process.argv;
  if (!htmlPath || !outPrefix) { console.error('usage: node shot-http.js <html> <out-prefix> [--rm]'); process.exit(2); }
  const root = path.dirname(path.resolve(htmlPath)); const file = path.basename(htmlPath);
  const srv = http.createServer((req, res) => {
    const p = decodeURIComponent(req.url.split('?')[0]);
    if (p.startsWith('/__fonts/')) {
      const g = path.join(FONT_DIR, path.basename(p));
      if (fs.existsSync(g)) { res.writeHead(200, { 'Content-Type': 'font/woff2', 'Access-Control-Allow-Origin': '*' }); return fs.createReadStream(g).pipe(res); }
      res.writeHead(404); return res.end();
    }
    let f = path.join(root, p === '/' ? file : p);
    let g = f;
    if (!g.startsWith(root) || !fs.existsSync(g) || fs.statSync(g).isDirectory()) {
      // an asset this mirror did not fetch (dynamic import): borrow the same-hash file from any other mirror
      const base = path.basename(g); g = null;
      for (const dir of ['/home/user/ElmsNest/brief/inventory', '/home/user/ElmsNest/brief/build-preview']) {
        try { for (const sub of fs.readdirSync(dir)) { const c = path.join(dir, sub, 'a', base); if (fs.existsSync(c) && fs.statSync(c).size > 0) { g = c; break; } } } catch (e) {}
        if (g) break;
      }
      if (!g) { res.writeHead(404); return res.end(); }
    }
    f = g;
    res.writeHead(200, { 'Content-Type': MIME[path.extname(f).toLowerCase()] || 'application/octet-stream', 'Access-Control-Allow-Origin': '*' });
    if (f === path.join(root, file)) {
      // mirror.py rewrote asset URLs to bare "a/…" paths; import maps and dynamic import() need a root-relative URL
      const html = fs.readFileSync(f, 'utf8').replace(/(["'])a\//g, '$1/a/');
      return res.end(html);
    }
    fs.createReadStream(f).pipe(res);
  });
  await new Promise(r => srv.listen(0, '127.0.0.1', r)); const port = srv.address().port;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  for (const [name, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844 }]]) {
    const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 2, locale: 'he-IL', reducedMotion: flag === '--rm' ? 'reduce' : 'no-preference', hasTouch: name === 'mobile', isMobile: name === 'mobile' });
    const faces = fontFaceCss(port);
    await ctx.route(/^https?:\/\//, r => {
      const u = r.request().url();
      if (/^https?:\/\/127\.0\.0\.1:/.test(u)) return r.continue();
      if (/fonts\.googleapis\.com/.test(u)) return r.fulfill({ status: 200, contentType: 'text/css', body: faces });
      return r.abort();
    });
    const p = await ctx.newPage(); const errors = [];
    p.on('pageerror', e => errors.push(String(e).slice(0, 120)));
    await p.goto(`http://127.0.0.1:${port}/${file}`, { waitUntil: 'load', timeout: 60000 });
    await p.waitForTimeout(1200);
    await p.evaluate(async () => {
      document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager');
      document.documentElement.style.scrollBehavior = 'auto';
      for (let y = 0; y < document.body.scrollHeight; y += 400) { window.scrollTo({ top: y, behavior: 'instant' }); await new Promise(r => setTimeout(r, 70)); }
      window.scrollTo({ top: 0, behavior: 'instant' });
    });
    await p.waitForTimeout(2800);
    await p.screenshot({ path: `${outPrefix}-${name}.png`, fullPage: true });
    await p.screenshot({ path: `${outPrefix}-${name}-fold.png`, fullPage: false });
    const h = await p.evaluate(() => document.body.scrollHeight);
    const horiz = await p.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
    console.log(`${name}: height=${h}px horizontal-overflow=${horiz} js-errors=${errors.length}${errors.length ? ' ' + errors.slice(0, 3).join(' | ') : ''}`);
    await ctx.close();
  }
  await b.close(); srv.close();
})();
