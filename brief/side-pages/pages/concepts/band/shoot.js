// shots + measurements for concept «band». node shoot.js
const fs = require('fs'), path = require('path');
const scratchRoot = '/tmp/claude-0/-home-user-ElmsNest';
const dir = fs.readdirSync(scratchRoot).find(d => fs.existsSync(path.join(scratchRoot, d, 'scratchpad/node_modules/playwright')));
const { chromium } = require(path.join(scratchRoot, dir, 'scratchpad/node_modules/playwright'));
const here = __dirname, url = 'file://' + path.join(here, 'index.html');
const OUT = path.join(here, 'shots'); fs.mkdirSync(OUT, { recursive: true });
const MEAS = path.join(here, 'measure'); fs.mkdirSync(MEAS, { recursive: true });
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const result = {};
  for (const [tag, vw, vh] of [['m', 390, 844], ['d', 1366, 900]]) {
    const ctx = await browser.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    await page.goto(url); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(600);
    // geometry of every article + its chrome bands, the h1 boxes on the bands, overflow check
    const geo = await page.evaluate(() => {
      const r = {}; const sw = document.documentElement.scrollWidth;
      for (const a of document.querySelectorAll('article.ens-page')) {
        const head = a.previousElementSibling, foot = a.nextElementSibling;
        const hb = head.getBoundingClientRect(), ab = a.getBoundingClientRect(), fb = foot.getBoundingClientRect();
        const y = window.scrollY;
        const cap = a.querySelector('.ens-page__band-cap .ens-page__h1');
        const cb = cap ? cap.getBoundingClientRect() : null;
        r[a.id] = { headTop: hb.top + y, top: ab.top + y, height: ab.height, footBottom: fb.bottom + y, h1OnBand: cb ? { x: cb.left, y: cb.top + y, w: cb.width, h: cb.height } : null,
          h1Font: getComputedStyle(a.querySelector('.ens-page__h1')).fontFamily, h1Size: getComputedStyle(a.querySelector('.ens-page__h1')).fontSize };
      }
      let minL = 0, maxR = 0; for (const el of document.querySelectorAll('body *')) { const b = el.getBoundingClientRect(); if (b.width === 0) continue; minL = Math.min(minL, b.left); maxR = Math.max(maxR, b.right); }
      r._scrollWidth = sw; r._clientWidth = document.documentElement.clientWidth; r._minLeft = minL; r._maxRight = maxR; r._scrollLeftRange = [document.documentElement.scrollLeft, (() => { document.documentElement.scrollLeft = -99999; const v = document.documentElement.scrollLeft; document.documentElement.scrollLeft = 0; return v; })()]; return r;
    });
    result[tag] = geo;
    const full = { m: ['guide', 'about'], d: [] }[tag];
    for (const id of ['guide', 'about', 'why', 'faq']) {
      const g = geo[id];
      if (tag === 'd' && (id === 'why' || id === 'faq')) continue;
      await page.evaluate(y => window.scrollTo(0, y), g.headTop); await page.waitForTimeout(150);
      await page.screenshot({ path: path.join(OUT, `${id}-${tag}-fold.png`), fullPage: false });
      await page.evaluate(() => window.scrollTo(0, 0));
      if (full.includes(id)) await page.screenshot({ path: path.join(OUT, `${id}-${tag}-full.png`), clip: { x: 0, y: g.headTop, width: vw, height: g.footBottom - g.headTop }, fullPage: true });
      if (tag === 'm' && (id === 'why' || id === 'faq')) await page.screenshot({ path: path.join(MEAS, `${id}-m-top1000.png`), clip: { x: 0, y: g.headTop, width: vw, height: 1000 }, fullPage: true });
    }
    // contrast pass: the same bands with the h1 hidden
    await page.addStyleTag({ content: '.ens-page__band-cap{visibility:hidden}' });
    for (const id of ['guide', 'faq']) {
      const g = geo[id]; if (!g.h1OnBand) continue;
      const b = g.h1OnBand;
      await page.screenshot({ path: path.join(MEAS, `${id}-${tag}-h1bg.png`), clip: { x: b.x, y: b.y, width: b.w, height: b.h }, fullPage: true });
    }
    await ctx.close();
  }
  fs.writeFileSync(path.join(MEAS, 'geo.json'), JSON.stringify(result, null, 2));
  await browser.close();
  console.log(JSON.stringify(result, null, 1));
})();
