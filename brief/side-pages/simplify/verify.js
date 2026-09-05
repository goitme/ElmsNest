// ElmsNest simplify round — verification against the REAL preview render (no mirror).
// Usage: NODE_PATH=$(npm root -g) node verify.js <outDir> [featured.json]
//   featured.json: { "<handle>": "<featured image filename without query>" } from the Admin API.
// Checks per page × viewport, JS on and off, and writes <outDir>/verify.json + screenshots.
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const OUT = process.argv[2] || path.join(__dirname, 'verify-out');
const FEAT = process.argv[3] ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : null;
fs.mkdirSync(OUT, { recursive: true });
const T = '154726400174';
const BASE = 'https://elmsnest.com';
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
    res.whatsapp = (main.innerText.match(/וואטסאפ|WhatsApp/gi) || []).length;
    res.mailtoInMain = q('main a[href^="mailto:"]').filter(vis).length;
    res.termsStrips = q('[data-env2-terms], .ens-terms').filter(vis).length;
    res.cartForms = q('form[action*="/cart/add"]').length;
    res.qtyInputs = q('input[name="quantity"]').filter(vis).length;
    res.atcButtons = q('form[action*="/cart/add"] button[type="submit"], form[action*="/cart/add"] [name="add"]').filter(vis).length;
    res.sections = q('[id^="shopify-section"]').map(s => ({ id: s.id.replace('shopify-section-', ''), h: Math.round(s.getBoundingClientRect().height) }));
    // cards
    const cards = q('.hdt-card-product').filter(vis);
    res.cards = cards.length;
    res.cardImgs = cards.map(c => { const a = c.querySelector('a[href*="/products/"]'); const img = c.querySelector('img'); const handle = a ? (a.getAttribute('href').split('/products/')[1] || '').split(/[?#]/)[0] : ''; const src = img ? (img.currentSrc || img.src || img.getAttribute('data-src') || '') : ''; return { handle, file: src.split('?')[0].split('/').pop(), w: img ? Math.round(img.getBoundingClientRect().width) : 0 }; });
    if (FEAT) res.cardsNotFeatured = res.cardImgs.filter(c => c.handle && FEAT[c.handle] && !c.file.startsWith(FEAT[c.handle].replace(/\.[a-z]+$/, ''))).map(c => c.handle + ':' + c.file);
    // fold: first buy button top
    const atc = q('form[action*="/cart/add"] [name="add"], form[action*="/cart/add"] button[type="submit"]').filter(vis)[0];
    if (atc) { const r = atc.getBoundingClientRect(); res.atcTop = Math.round(r.top + window.scrollY); res.atcInFold = (r.top + window.scrollY + r.height) <= vh; }
    // small tap targets
    res.smallTaps = q('main a, main button, main input, main select').filter(vis).filter(el => { const r = el.getBoundingClientRect(); return r.height < 40 && r.width < 40; }).length;
    res.h1 = q('h1').map(h => h.textContent.trim()).filter(Boolean);
    // order of place names on the page (home tiles / filter row)
    res.placeOrder = q('[data-ens-place]').filter(vis).map(e => e.getAttribute('data-ens-place'));
    return res;
  }, { name, vh, FEAT });
}

(async () => {
  const browser = await chromium.launch();
  const report = {};
  for (const js of [true, false]) {
    for (const [vk, w, h] of VIEWS) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, javaScriptEnabled: js, locale: 'he-IL' });
      const page = await ctx.newPage();
      for (const p of PAGES) {
        const key = `${p.name}-${vk}-${js ? 'js' : 'nojs'}`;
        try {
          await page.goto(url(p.path), { waitUntil: 'domcontentloaded', timeout: 60000 });
          await page.waitForTimeout(js ? 3000 : 800);
          if (js) { await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 90)); } window.scrollTo(0, 0); }); await page.waitForTimeout(600); }
          const r = await audit(page, p.name, w, h);
          r.target = p.target; r.overTarget = r.screens > p.target;
          report[key] = r;
          if (js && vk !== 's') { await page.screenshot({ path: path.join(OUT, `${key}-full.png`), fullPage: true }).catch(() => {}); }
          await page.screenshot({ path: path.join(OUT, `${key}-fold.png`) }).catch(() => {});
          console.log(key, `screens=${r.screens}/${p.target}`, `forms=${r.cartForms}`, `mailto=${r.mailtoInMain}`, `terms=${r.termsStrips}`, `glyph=${r.glyphPlates}`, `liquidErr=${r.liquidErrors}`, `ovX=${r.overflowX}`, r.cardsNotFeatured ? `notFeatured=${r.cardsNotFeatured.length}` : '');
        } catch (e) { report[key] = { error: e.message.slice(0, 200) }; console.log(key, 'ERROR', e.message.slice(0, 120)); }
      }
      // drawer test: add to cart on the rope PDP (JS on, mobile only)
      if (js && vk === 'm') {
        try {
          await page.goto(url('/products/stainless-steel-solar-path-light-ip65'), { waitUntil: 'domcontentloaded', timeout: 60000 });
          await page.waitForTimeout(3000);
          const btn = page.locator('form[action*="/cart/add"] [name="add"], form[action*="/cart/add"] button[type="submit"]').first();
          await btn.scrollIntoViewIfNeeded(); await btn.click();
          await page.waitForTimeout(3500);
          const drawer = await page.evaluate(() => { const d = document.querySelector('cart-drawer, #cart-drawer, .hdt-cart-drawer, [id*="cart-drawer"], hdt-cart-drawer'); if (!d) return { found: false }; const r = d.getBoundingClientRect(); const cs = getComputedStyle(d); return { found: true, visible: r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none', open: d.hasAttribute('open') || d.classList.contains('open') || d.classList.contains('active') || d.classList.contains('hdt-active') || cs.transform === 'none', text: (d.innerText || '').slice(0, 200) }; });
          report['drawer-m-js'] = drawer;
          await page.screenshot({ path: path.join(OUT, 'drawer-m-js.png') }).catch(() => {});
          console.log('drawer', JSON.stringify(drawer).slice(0, 200));
        } catch (e) { report['drawer-m-js'] = { error: e.message.slice(0, 200) }; console.log('drawer ERROR', e.message.slice(0, 120)); }
      }
      await ctx.close();
    }
  }
  fs.writeFileSync(path.join(OUT, 'verify.json'), JSON.stringify(report, null, 2));
  await browser.close();
})();
