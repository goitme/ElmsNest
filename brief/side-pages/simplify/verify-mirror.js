// ElmsNest SIMPLIFY round — the §11 verification, run through MIRRORS served on 127.0.0.1.
// Why a port: the other session's verify.js drives https://elmsnest.com directly, and Chromium cannot reach it
// through this sandbox's proxy (ERR_CONNECTION_RESET, ws_closed_mid_exchange — measured 2026-09-05). curl can. So
// every page is mirrored with brief/mirror.py (which fetches Kalles' importmap so theme JS runs) and rendered from
// a local server, exactly as every screenshot in this repo has been taken. The audit() below is the other
// session's, kept verbatim, then EXTENDED with the §11 checks it did not cover. Two §11 checks need the live
// store (add-to-cart → drawer line; the drawer opening after the main button) and are done in the hybrid at the
// end: DOM state read from the mirror, the POST made with curl, the drawer section fetched with curl.
// Usage: node brief/side-pages/simplify/verify-mirror.js <outDir> [featured.json] [--no-mirror]
const path = require('path'), fs = require('fs'), http = require('http'), { execFileSync } = require('child_process');
function loadPlaywright() {
  const roots = [process.env.ENV2_PW_ROOT].filter(Boolean);
  try { for (const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest')) roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`); } catch (e) {}
  for (const r of roots) { try { return require(`${r}/node_modules/playwright`); } catch (e) {} }
  return require('playwright');
}
const { chromium } = loadPlaywright();
const REPO = '/home/user/ElmsNest';
const OUT = process.argv[2] || path.join(__dirname, 'verify-out');
const FEAT = process.argv[3] && !process.argv[3].startsWith('--') ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : null;
const NO_MIRROR = process.argv.includes('--no-mirror');
fs.mkdirSync(OUT, { recursive: true });
const T = '154726400174', BASE = 'https://elmsnest.com';
const PAGES = [
  { name: 'home', path: '/', target: 6 },
  { name: 'collection-all', path: '/collections/all', target: 8 },
  { name: 'collection-path', path: '/collections/%D7%AA%D7%90%D7%95%D7%A8%D7%AA-%D7%A9%D7%91%D7%99%D7%9C-%D7%A1%D7%95%D7%9C%D7%90%D7%A8%D7%99%D7%AA', target: 8 },
  { name: 'pdp-rope', path: '/products/solar-rope-string-lights', target: 6 },
  { name: 'pdp-path', path: '/products/stainless-steel-solar-path-light-ip65', target: 6 },
  { name: 'pdp-deck', path: '/products/waterproof-solar-deck-step-lights', target: 6 },
];
const VIEWS = [['m', 390, 844], ['s', 360, 640], ['d', 1366, 900]];
const url = p => `${BASE}${p}${p.includes('?') ? '&' : '?'}preview_theme_id=${T}`;
const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.woff': 'font/woff', '.gif': 'image/gif', '.ico': 'image/x-icon', '.json': 'application/json' };
const FONT_DIR = `${REPO}/brief/assets/fonts`;
function fontFaceCss(port) {
  let css = ''; let files = []; try { files = fs.readdirSync(FONT_DIR); } catch (e) { return ''; }
  for (const f of files) { const m = /^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f); if (!m) continue; const fam = m[1] === 'FrankRuhlLibre' ? 'Frank Ruhl Libre' : 'Heebo'; css += `@font-face{font-family:'${fam}';font-style:normal;font-weight:${m[3]};font-display:swap;src:url(http://127.0.0.1:${port}/__fonts/${f}) format('woff2')}`; }
  return css;
}
function mirror(name, p) {
  const dir = path.join(OUT, 'mirrors', name);
  if (NO_MIRROR && fs.existsSync(path.join(dir, 'index.html'))) return dir;
  fs.mkdirSync(dir, { recursive: true });
  execFileSync('python3', [`${REPO}/brief/mirror.py`, url(p), dir], { stdio: 'ignore', timeout: 300000 });
  return dir;
}
function serve(root) {
  const srv = http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split('?')[0]);
    if (p.startsWith('/__fonts/')) { const f = path.join(FONT_DIR, p.slice(9)); if (fs.existsSync(f)) { res.writeHead(200, { 'Content-Type': 'font/woff2', 'Access-Control-Allow-Origin': '*' }); return fs.createReadStream(f).pipe(res); } res.writeHead(404); return res.end(); }
    let f = path.join(root, p === '/' ? 'index.html' : p.slice(1));
    if (!fs.existsSync(f)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(f).toLowerCase()] || 'application/octet-stream', 'Access-Control-Allow-Origin': '*' });
    if (f === path.join(root, 'index.html')) return res.end(fs.readFileSync(f, 'utf8').replace(/(["'])a\//g, '$1/a/'));
    fs.createReadStream(f).pipe(res);
  });
  return new Promise(r => srv.listen(0, '127.0.0.1', () => r({ srv, port: srv.address().port })));
}
async function audit(page, name, vw, vh) {
  return page.evaluate(({ name, vh, FEAT }) => {
    const q = s => [...document.querySelectorAll(s)];
    const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
    const main = document.querySelector('main') || document.body;
    const html = document.documentElement.outerHTML;
    const res = {};
    res.docH = document.documentElement.scrollHeight; res.screens = +(res.docH / vh).toFixed(2);
    res.overflowX = document.documentElement.scrollWidth > document.documentElement.clientWidth + 1;
    res.liquidErrors = (html.match(/Liquid error/g) || []).length;
    res.glyphPlates = q('.env2-coll-glyph, svg.env2-glyph').filter(vis).length;
    res.glyphCaption = (main.innerText.match(/איור/g) || []).length;
    res.whatsapp = (main.innerText.match(/וואטסאפ|ווטסאפ|WhatsApp/gi) || []).length + (html.match(/wa\.me/g) || []).length;
    res.enWa = q('.en-wa').length;
    res.bestSelling = (main.innerText.match(/הנמכרים ביותר/g) || []).length;
    res.mailtoInMain = q('main a[href^="mailto:"]').filter(vis).length;
    res.mailtoInFooter = q('footer a[href^="mailto:"], .shopify-section-group-footer-group a[href^="mailto:"]').length;
    res.photoLineInMain = (main.innerText.match(/תמונה של המקום/g) || []).length;
    res.termsStrips = q('[data-env2-terms], .ens-terms, #env2-terms').filter(vis).length;
    res.termsLine = q('.ens-terms-line').length;
    res.cartForms = q('form[action*="/cart/add"]').length;
    res.mainProductForms = q('form.hdt-main-product-form').length;
    res.stickyForms = q('form.hdt-sticky-atc__form').length;
    res.noscriptSelect = /<noscript>[\s\S]*?<select[^>]*name="id"/i.test(html);
    res.qtyInputs = q('input[name="quantity"]').filter(vis).length;
    res.atcButtons = q('form[action*="/cart/add"] button[type="submit"], form[action*="/cart/add"] [name="add"]').filter(vis).length;
    res.sections = q('[id^="shopify-section"]').map(s => ({ id: s.id.replace('shopify-section-', ''), h: Math.round(s.getBoundingClientRect().height) }));
    const cards = q('.hdt-card-product').filter(vis);
    res.cards = cards.length;
    res.cardForms = q('.hdt-card-product form').length;
    res.cardBigSvgs = q('.hdt-card-product__media svg').filter(s => { const r = s.getBoundingClientRect(); return r.width >= 100 && r.height >= 100; }).length;
    res.cardButtons = q('.hdt-card-product button, .hdt-card-product [role="button"]').filter(vis).length;
    res.cardImgs = cards.map(c => { const a = c.querySelector('a[href*="/products/"]'); const img = c.querySelector('img.hdt-card-product__media--main') || c.querySelector('img'); const handle = a ? (a.getAttribute('href').split('/products/')[1] || '').split(/[?#]/)[0] : ''; const src = img ? (img.currentSrc || img.src || img.getAttribute('data-src') || img.getAttribute('srcset') || '') : ''; return { handle, file: src.split(',')[0].trim().split(' ')[0].split('?')[0].split('/').pop(), w: img ? Math.round(img.getBoundingClientRect().width) : 0 }; });
    if (FEAT) res.cardsNotFeatured = res.cardImgs.filter(c => c.handle && FEAT[c.handle] && !decodeURIComponent(c.file).startsWith(FEAT[c.handle].replace(/\.[a-z]+$/i, ''))).map(c => c.handle + ':' + c.file);
    const atc = q('form[action*="/cart/add"] [name="add"], form[action*="/cart/add"] button[type="submit"]').filter(vis)[0];
    if (atc) { const r = atc.getBoundingClientRect(); res.atcTop = Math.round(r.top + window.scrollY); res.atcInFold = (r.top + window.scrollY + r.height) <= vh; }
    res.smallTaps = q('main a, main button, main input, main select').filter(vis).filter(el => { const r = el.getBoundingClientRect(); return r.height < 40 && r.width < 40; }).length;
    res.pillsUnder44 = q('.hdt-variant-option button, .hdt-variant-option label, [class*="variant"] label, [class*="pill"]').filter(vis).filter(el => el.getBoundingClientRect().height < 44).length;
    res.h1 = q('h1').map(h => h.textContent.trim()).filter(Boolean);
    res.placeOrder = q('[data-ens-place]').filter(vis).map(e => e.getAttribute('data-ens-place'));
    res.headerMenuOrder = q('header a[href*="/collections/"], .shopify-section-group-header-group a[href*="/collections/"]').map(a => decodeURIComponent(a.getAttribute('href')).split('/collections/')[1].split(/[?#/]/)[0]).filter((h, i, arr) => h && h !== 'all' && arr.indexOf(h) === i);
    res.footerOrder = q('.shopify-section-group-footer-group a[href*="/collections/"]').map(a => decodeURIComponent(a.getAttribute('href')).split('/collections/')[1].split(/[?#/]/)[0]).filter((h, i, arr) => h && h !== 'all' && arr.indexOf(h) === i);
    // every en-dash range in <main> text must sit inside a <bdi>
    const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT); const bare = []; let n;
    while ((n = walker.nextNode())) { if (/\d\s?–\s?\d/.test(n.nodeValue) && !n.parentElement.closest('bdi') && !n.parentElement.closest('script,style,noscript')) bare.push(n.nodeValue.trim().slice(0, 40)); }
    res.rangesOutsideBdi = bare.slice(0, 8); res.rangesOutsideBdiCount = bare.length;
    res.cardTransition = cards[0] ? getComputedStyle(cards[0]).transitionDuration : null;
    return res;
  }, { name, vh, FEAT });
}
(async () => {
  const report = {};
  const dirs = {};
  for (const p of PAGES) { process.stdout.write(`mirror ${p.name} … `); dirs[p.name] = mirror(p.name, p.path); console.log('ok'); }
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  for (const js of [true, false]) for (const [vk, w, h] of VIEWS) for (const p of PAGES) {
    const key = `${p.name}-${vk}-${js ? 'js' : 'nojs'}`;
    const { srv, port } = await serve(dirs[p.name]);
    const ctx = await b.newContext({ viewport: { width: w, height: h }, javaScriptEnabled: js, locale: 'he-IL', deviceScaleFactor: 1, isMobile: w < 500, hasTouch: w < 500 });
    const faces = fontFaceCss(port);
    await ctx.route(/^https?:\/\//, r => { const u = r.request().url(); if (/^https?:\/\/127\.0\.0\.1:/.test(u)) return r.continue(); if (/fonts\.googleapis\.com/.test(u)) return r.fulfill({ status: 200, contentType: 'text/css', body: faces }); return r.abort(); });
    const page = await ctx.newPage();
    try {
      await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: js ? 'load' : 'domcontentloaded', timeout: 60000 });
      await page.waitForTimeout(js ? 2500 : 600);
      if (js) { await page.evaluate(async () => { document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager'); for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 90)); } window.scrollTo(0, 0); }); await page.waitForTimeout(900); }
      const r = await audit(page, p.name, w, h);
      r.target = p.target; r.overTarget = r.screens > p.target;
      report[key] = r;
      if (js && vk !== 's') await page.screenshot({ path: path.join(OUT, `${key}-full.png`), fullPage: true }).catch(() => {});
      await page.screenshot({ path: path.join(OUT, `${key}-fold.png`) }).catch(() => {});
      console.log(key, `screens=${r.screens}/${p.target}`, `forms=${r.cartForms}`, `main=${r.mainProductForms} sticky=${r.stickyForms}`, `mailto=${r.mailtoInMain}`, `photo=${r.photoLineInMain}`, `terms=${r.termsStrips}/${r.termsLine}`, `glyph=${r.glyphPlates}/${r.glyphCaption}`, `wa=${r.whatsapp}`, `cards=${r.cards} cardForms=${r.cardForms} svg=${r.cardBigSvgs}`, `liquidErr=${r.liquidErrors}`, `ovX=${r.overflowX}`, `bdi!=${r.rangesOutsideBdiCount}`, r.cardsNotFeatured ? `notFeatured=${r.cardsNotFeatured.length}` : '');
    } catch (e) { report[key] = { error: e.message.slice(0, 200) }; console.log(key, 'ERROR', e.message.slice(0, 120)); }
    await ctx.close(); srv.close();
  }
  // reduced motion: no transitions on cards (collection-all, mobile, JS on)
  { const { srv, port } = await serve(dirs['collection-all']);
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, locale: 'he-IL', reducedMotion: 'reduce' });
    await ctx.route(/^https?:\/\//, r => /127\.0\.0\.1:/.test(r.request().url()) ? r.continue() : r.abort());
    const page = await ctx.newPage(); await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'load', timeout: 60000 }); await page.waitForTimeout(1500);
    report['reduced-motion'] = await page.evaluate(() => { const c = document.querySelector('.hdt-card-product'); if (!c) return { card: false }; const all = [c, ...c.querySelectorAll('*')].map(e => getComputedStyle(e).transitionDuration).filter(d => d && d !== '0s'); return { card: true, elementsWithTransition: all.length }; });
    console.log('reduced-motion', JSON.stringify(report['reduced-motion'])); await ctx.close(); srv.close(); }
  // hybrid: variant pill → price + sticky id on the MIRROR; then the POST and the drawer section through curl
  try { const { srv, port } = await serve(dirs['pdp-rope']);
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, locale: 'he-IL' });
    await ctx.route(/^https?:\/\//, r => /127\.0\.0\.1:/.test(r.request().url()) ? r.continue() : r.abort());
    const page = await ctx.newPage(); await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'load', timeout: 60000 }); await page.waitForTimeout(2500);
    const before = await page.evaluate(() => ({ mainId: (document.querySelector('form.hdt-main-product-form input[name="id"], form.hdt-main-product-form select[name="id"]') || {}).value, stickyId: (document.querySelector('form.hdt-sticky-atc__form input[name="id"]') || {}).value, price: ((document.querySelector('.hdt-price .hdt-money, .hdt-product-price .hdt-money, [class*="price"] .hdt-money') || {}).textContent || '').trim() }));
    // click the second value of the first option (a pill/radio/label)
    const clicked = await page.evaluate(() => { const opts = [...document.querySelectorAll('form.hdt-main-product-form input[type="radio"], .hdt-variant-option input[type="radio"]')]; if (opts.length < 2) return null; const target = opts.find(o => !o.checked) || opts[1]; const lab = document.querySelector(`label[for="${target.id}"]`) || target; lab.click(); return target.value; });
    await page.waitForTimeout(1200);
    const after = await page.evaluate(() => ({ mainId: (document.querySelector('form.hdt-main-product-form input[name="id"], form.hdt-main-product-form select[name="id"]') || {}).value, stickyId: (document.querySelector('form.hdt-sticky-atc__form input[name="id"]') || {}).value, price: ((document.querySelector('.hdt-price .hdt-money, .hdt-product-price .hdt-money, [class*="price"] .hdt-money') || {}).textContent || '').trim() }));
    let live = null;
    try {
      const jar = path.join(OUT, 'jar.txt'); try { fs.unlinkSync(jar); } catch (e) {}
      execFileSync('curl', ['-sS', '-c', jar, '-b', jar, '-L', '-o', '/dev/null', url('/')]);
      const id = after.mainId || after.stickyId;
      const add = JSON.parse(execFileSync('curl', ['-sS', '-c', jar, '-b', jar, '-X', 'POST', `${BASE}/cart/add.js`, '-H', 'Content-Type: application/json', '-d', JSON.stringify({ items: [{ id: Number(id), quantity: 1 }] })]).toString());
      const drawerHtml = execFileSync('curl', ['-sS', '-c', jar, '-b', jar, '-L', `${BASE}/collections/all?section_id=sections--21567608946862__cart-drawer`]).toString();
      live = { postedId: id, addStatus: add.status || 'ok', lineTitle: add.items && add.items[0] && add.items[0].title, drawerHasVariant: drawerHtml.includes(`variant=${id}`) || drawerHtml.includes(String(id)), drawerHasLineItem: /<hdt-line-item/.test(drawerHtml) };
    } catch (e) { live = { error: String(e.message).slice(0, 160) }; }
    report['pdp-variant-sync'] = { before, clicked, after, idsAgree: after.mainId && after.mainId === after.stickyId, priceChanged: before.price !== after.price, live };
    console.log('pdp-variant-sync', JSON.stringify(report['pdp-variant-sync']).slice(0, 400)); await ctx.close(); srv.close(); } catch (e) { report['pdp-variant-sync'] = { error: String(e.message).slice(0, 200) }; console.log('pdp-variant-sync ERROR', String(e.message).slice(0, 160)); }
  fs.writeFileSync(path.join(OUT, 'verify.json'), JSON.stringify(report, null, 2));
  await b.close();
  console.log('wrote', path.join(OUT, 'verify.json'));
})();
