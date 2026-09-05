// Usage: node brief/side-pages/cart/verify.js <mirror-dir>/index.html <label> [--drawer]
// The round-3 acceptance harness. Serves a mirror on 127.0.0.1 (so theme JS runs), optionally opens the
// cart drawer through the theme's own hdt-cart-drawer.open(), and prints one JSON line per viewport with
// every number this round is judged on. Nothing here is a screenshot opinion; every field is measured.
//
// Checks, in the order the BRIEF's constraints are numbered:
//   fold        checkout button top/bottom vs the viewport — CONTRACT: inside the fold at 360x640 (cart page)
//   dominance   checkout area / largest competing control area (a twin button scores ~1.0 and fails)
//   touch       every control's height; anything under 44 is listed
//   removes     remove controls per line item — CONTRACT: exactly 1 (Kalles renders 2 at quantity 1)
//   truncated   line titles whose scrollWidth exceeds clientWidth
//   lineTotal   whether each line prints its own total (qty x unit) or makes the buyer multiply
//   tracking    any Hebrew run with letter-spacing != normal
//   void        px between the last line item and the subtotal
//   terms       whether any of the four approved numbers is present
//   overflow    document horizontal overflow
//   liquid      "Liquid error" occurrences in the served HTML
const path = require('path'), fs = require('fs'), http = require('http');
function loadPlaywright() {
  const roots = [process.env.ENV2_PW_ROOT].filter(Boolean);
  try { for (const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest')) roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`); } catch (e) {}
  for (const r of roots) { try { return require(`${r}/node_modules/playwright`); } catch (e) {} }
  return require('playwright');
}
const { chromium } = loadPlaywright();
const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.woff': 'font/woff', '.gif': 'image/gif', '.ico': 'image/x-icon', '.json': 'application/json' };
const FONT_DIR = '/home/user/ElmsNest/brief/assets/fonts';
function fontFaceCss(port) {
  let css = '';
  let files = []; try { files = fs.readdirSync(FONT_DIR); } catch (e) { return ''; }
  for (const f of files) {
    const m = /^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f); if (!m) continue;
    const fam = m[1] === 'FrankRuhlLibre' ? 'Frank Ruhl Libre' : 'Heebo';
    css += `@font-face{font-family:'${fam}';font-style:normal;font-weight:${m[3]};font-display:swap;src:url(http://127.0.0.1:${port}/__fonts/${f}) format('woff2')}`;
  }
  return css;
}
const VIEWPORTS = [[390, 844], [360, 640], [320, 568], [1440, 900]];

(async () => {
  const target = process.argv[2], label = process.argv[3] || path.basename(path.dirname(process.argv[2]));
  const openDrawer = process.argv.includes('--drawer');
  const root = path.resolve(path.dirname(target)), file = path.basename(target);
  const raw = fs.readFileSync(target, 'utf8');
  const liquidErrors = (raw.match(/Liquid error/g) || []).length;

  const srv = http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split('?')[0]);
    if (p.startsWith('/__fonts/')) {
      const f = path.join(FONT_DIR, p.slice(9));
      if (fs.existsSync(f)) { res.writeHead(200, { 'Content-Type': 'font/woff2', 'Access-Control-Allow-Origin': '*' }); return fs.createReadStream(f).pipe(res); }
      res.writeHead(404); return res.end();
    }
    let f = path.join(root, p === '/' ? file : p.slice(1));
    if (!fs.existsSync(f)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(f).toLowerCase()] || 'application/octet-stream', 'Access-Control-Allow-Origin': '*' });
    if (f === path.join(root, file)) return res.end(raw.replace(/(["'])a\//g, '$1/a/'));
    fs.createReadStream(f).pipe(res);
  });
  await new Promise(r => srv.listen(0, '127.0.0.1', r));
  const port = srv.address().port;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const faces = fontFaceCss(port);

  for (const [w, h] of VIEWPORTS) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, locale: 'he-IL', isMobile: w < 500, hasTouch: w < 500 });
    await ctx.route(/^https?:\/\//, r => {
      const u = r.request().url();
      if (/^https?:\/\/127\.0\.0\.1:/.test(u)) return r.continue();
      if (/fonts\.googleapis\.com/.test(u)) return r.fulfill({ status: 200, contentType: 'text/css', body: faces });
      return r.abort();
    });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push(String(e).slice(0, 90)));
    await p.goto(`http://127.0.0.1:${port}/${file}`, { waitUntil: 'load', timeout: 60000 });
    await p.waitForTimeout(1400);
    let drawerState = null;
    if (openDrawer) {
      drawerState = await p.evaluate(async () => {
        const host = document.querySelector('hdt-cart-drawer'), dlg = document.getElementById('CartDrawer');
        if (!dlg) return 'no-dialog';
        try { if (host && typeof host.open === 'function') host.open(); else dlg.showModal(); } catch (e) { try { dlg.showModal(); } catch (e2) { return 'failed' } }
        dlg.setAttribute('open', ''); await new Promise(r => setTimeout(r, 500));
        return dlg.open ? 'open' : 'not-open';
      });
      await p.waitForTimeout(600);
    }
    const out = await p.evaluate((vh) => {
      const box = el => { if (!el) return null; const r = el.getBoundingClientRect(); return { t: Math.round(r.top), b: Math.round(r.bottom), w: Math.round(r.width), h: Math.round(r.height) }; };
      const scope = document.getElementById('CartDrawer') && document.getElementById('CartDrawer').open ? document.getElementById('CartDrawer') : document;
      const chk = scope.querySelector('button[name="checkout"], [data-env2-checkout]');
      const chkBox = box(chk);
      // dominance: the checkout's area against the biggest other interactive control in the same scope
      let rival = 0, rivalTxt = '', exits = 0;
      for (const el of scope.querySelectorAll('a,button')) {
        if (el === chk || (chk && chk.contains(el))) continue;
        if (el.querySelector('img')) { exits++; continue; }  // a photo link is an exit, not a rival control
        const r = el.getBoundingClientRect(); const a = r.width * r.height;
        if (getComputedStyle(el).visibility === 'hidden' || !el.offsetParent && getComputedStyle(el).position !== 'fixed') continue;
        if (a > rival && r.width > 40 && r.height > 20) { rival = a; rivalTxt = (el.textContent || '').trim().slice(0, 24) || el.className.slice(0, 24); }
      }
      const chkArea = chkBox ? chkBox.w * chkBox.h : 0;
      const small = [];
      for (const el of scope.querySelectorAll('a,button,input[type="number"]')) {
        const r = el.getBoundingClientRect();
        if (r.width === 0 || r.height === 0) continue;
        if (r.height < 44) small.push({ txt: (el.textContent || el.getAttribute('name') || '').trim().slice(0, 18), h: Math.round(r.height) });
      }
      const items = [...scope.querySelectorAll('hdt-line-item,[data-env2-line]')].map(e => {
        // the IMAGE anchor also matches a[href*=/products/] and never overflows — take the title explicitly
        const t = e.querySelector('[data-env2-line-title], .hdt-mini-cart__title, .hdt-page-cart__title') || [...e.querySelectorAll('a[href*="/products/"]')].filter(a => !a.querySelector('img')).pop();
        const removes = e.querySelectorAll('wrapp-remove-item-oncart,[data-env2-remove]').length;
        const txt = e.textContent.replace(/\s+/g, ' ');
        return {
          removes,
          truncated: t ? (t.scrollWidth > t.clientWidth + 1 || t.scrollHeight > t.clientHeight + 1) : null,
          title: t ? t.textContent.trim().slice(0, 30) : null,
          lineTotal: /339\.80|89\.90\s*₪/.test(txt) && /339\.80/.test(txt) ? true : /339\.80/.test(txt),
        };
      });
      // any Hebrew run carrying letter-spacing
      const tracked = [];
      for (const el of scope.querySelectorAll('*')) {
        if (el.children.length) continue;
        const t = (el.textContent || '').trim(); if (!/[֐-׿]/.test(t)) continue;
        const ls = getComputedStyle(el).letterSpacing;
        if (ls && ls !== 'normal' && parseFloat(ls) > 0.2) tracked.push({ txt: t.slice(0, 20), ls });
      }
      const sub = [...scope.querySelectorAll('*')].find(e => !e.children.length && /סכום ביניים|סה"כ|לתשלום/.test(e.textContent));
      const last = [...scope.querySelectorAll('hdt-line-item,[data-env2-line]')].pop();
      const gap = (sub && last) ? Math.round(sub.getBoundingClientRect().top - last.getBoundingClientRect().bottom) : null;
      const body = scope === document ? document.body.textContent : scope.textContent;
      return {
        checkout: chkBox,
        checkoutLabel: chk ? chk.textContent.trim().slice(0, 28) : null,
        insideFold: chkBox ? chkBox.b <= vh : null,
        belowFoldBy: chkBox ? Math.max(0, chkBox.b - vh) : null,
        dominance: rival ? +(chkArea / rival).toFixed(2) : null,
        rival: rivalTxt,
        exitLinks: exits,
        under44: small,
        items,
        tracked: tracked.slice(0, 4),
        voidAboveSubtotal: gap,
        terms: { pickup: body.includes('נקודת איסוף'), days: body.includes('8–17') || body.includes('ימי עסקים'), cancel: body.includes('14') && body.includes('ביטול'), photo: body.includes('תמונה של המקום') },
        overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
        docH: document.body.scrollHeight,
      };
    }, h);
    out.viewport = `${w}x${h}`; out.label = label; out.drawer = drawerState; out.jsErrors = errs.length; out.liquidErrors = liquidErrors;
    console.log(JSON.stringify(out));
    await ctx.close();
  }
  await b.close(); srv.close();
})();
