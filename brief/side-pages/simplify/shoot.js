const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const OUT = __dirname;
const T = '154726400174';
const PAGES = [
  ['home', '/'],
  ['collection-all', '/collections/all'],
  ['pdp-rope', '/products/solar-rope-string-lights'],
  ['pdp-path', '/products/stainless-steel-solar-path-light-ip65'],
  ['cart', '/cart'],
  ['search', '/search?q=solar'],
  ['notfound', '/products/does-not-exist-404'],
];
const VIEWS = [['m', 390, 844], ['d', 1366, 900]];
(async () => {
  const browser = await chromium.launch();
  const report = {};
  for (const [vk, w, h] of VIEWS) {
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1, locale: 'he-IL' });
    const page = await ctx.newPage();
    for (const [name, p] of PAGES) {
      const url = `https://elmsnest.com${p}${p.includes('?') ? '&' : '?'}preview_theme_id=${T}`;
      try {
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
        await page.waitForTimeout(3500);
        // hide shopify preview bar if any
        await page.addStyleTag({ content: '#preview-bar-iframe,[id*="preview-bar"]{display:none!important}' }).catch(() => {});
        await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } window.scrollTo(0, 0); });
        await page.waitForTimeout(800);
        const info = await page.evaluate(() => {
          const secs = [...document.querySelectorAll('[id^="shopify-section"]')].map(s => {
            const r = s.getBoundingClientRect();
            const hd = s.querySelector('h1,h2,h3');
            const inner = s.firstElementChild;
            return { id: s.id, type: inner ? (inner.className || inner.tagName).toString().slice(0, 80) : '', heading: hd ? hd.textContent.trim().slice(0, 80) : '', top: Math.round(r.top + window.scrollY), height: Math.round(r.height), visible: r.height > 0 };
          });
          const btns = [...document.querySelectorAll('button,[role=button],input[type=submit]')].filter(b => b.getBoundingClientRect().height > 0).length;
          const links = [...document.querySelectorAll('a[href]')].filter(a => a.getBoundingClientRect().height > 0).length;
          const inputs = [...document.querySelectorAll('input:not([type=hidden]),select,textarea')].filter(i => i.getBoundingClientRect().height > 0).length;
          const imgs = [...document.querySelectorAll('img')].filter(i => i.getBoundingClientRect().height > 0).map(i => ({ src: (i.currentSrc || i.src).split('?')[0].slice(-70), w: Math.round(i.getBoundingClientRect().width), h: Math.round(i.getBoundingClientRect().height), alt: (i.alt || '').slice(0, 40) })).slice(0, 60);
          const svgs = [...document.querySelectorAll('svg')].filter(s => s.getBoundingClientRect().height > 60).length;
          return { title: document.title, docH: document.documentElement.scrollHeight, bodyBg: getComputedStyle(document.body).backgroundColor, secs, btns, links, inputs, imgs, bigSvgs: svgs, h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim().slice(0, 80)), h2: [...document.querySelectorAll('h2')].map(h => h.textContent.trim().slice(0, 80)) };
        });
        info.viewportH = h; info.screens = +(info.docH / h).toFixed(1);
        report[`${name}-${vk}`] = info;
        await page.screenshot({ path: path.join(OUT, `${name}-${vk}-full.png`), fullPage: true });
        await page.screenshot({ path: path.join(OUT, `${name}-${vk}-fold.png`), fullPage: false });
        console.log(`${name}-${vk}: ${info.screens} screens, ${info.secs.length} sections, ${info.btns} btns, ${info.links} links, ${info.inputs} inputs`);
      } catch (e) { console.log(`${name}-${vk}: ERROR ${e.message.slice(0, 120)}`); report[`${name}-${vk}`] = { error: e.message }; }
    }
    await ctx.close();
  }
  fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(report, null, 2));
  await browser.close();
})();
