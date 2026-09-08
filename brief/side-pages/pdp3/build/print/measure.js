// Measures the rendered ens_pdp_print section for the three archetypes and writes sizes.json + PNGs.
// sizes.json is in the pdp2/verify/contrast.py shape: key = "<name>-<viewport>", texts[] = box + CSS colour.
const fs = require('fs');
const path = require('path');
const scratch = '/tmp/claude-0/-home-user-ElmsNest';
const dir = fs.readdirSync(scratch).map(d => path.join(scratch, d, 'scratchpad', 'node_modules'))
  .find(p => fs.existsSync(path.join(p, 'playwright')));
const { chromium } = require(path.join(dir, 'playwright'));
const HERE = __dirname;
const SEL = ['.ens-pdp-print__line', '.ens-pdp-print__cap', '.ens-pdp-print__credit'];

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const out = {};
  for (const vp of [{ w: 390, h: 844 }, { w: 1366, h: 900 }]) {
    for (const k of ['A', 'B', 'C']) {
      const ctx = await browser.newContext({ viewport: { width: vp.w, height: vp.h }, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      await page.goto('file://' + path.join(HERE, `archetype-${k}.html`));
      await page.waitForLoadState('networkidle');
      await page.evaluate(() => document.fonts.ready);
      await page.evaluate(async () => {
        // the section is lazy-loaded below the fold on a real page; here force the decode before measuring
        await Promise.all([...document.images].map(i => i.complete ? null : i.decode().catch(() => {})));
      });
      await page.waitForTimeout(250);
      const data = await page.evaluate((SEL) => {
        const sec = document.querySelector('.ens-pdp-print');
        const r = sec.getBoundingClientRect();
        const img = document.querySelector('.ens-pdp-print__fig img');
        const ir = img.getBoundingClientRect();
        const texts = [];
        for (const s of SEL) {
          document.querySelectorAll(s).forEach(el => {
            const b = el.getBoundingClientRect(); const cs = getComputedStyle(el);
            texts.push({ cls: el.className, text: el.textContent.trim(), color: cs.color, size: cs.fontSize,
              x: Math.round(b.x + scrollX), y: Math.round(b.y + scrollY), w: Math.round(b.width), h: Math.round(b.height) });
          });
        }
        return { height: Math.round(r.height), width: Math.round(r.width),
          img: { w: Math.round(ir.width), h: Math.round(ir.height), natural: img.naturalWidth + 'x' + img.naturalHeight,
                 currentSrc: img.currentSrc.split('/').pop() },
          doc: Math.round(document.documentElement.scrollHeight), texts };
      }, SEL);
      const key = `print-${k}-${vp.w}`;
      out[key] = data;
      await page.screenshot({ path: path.join(HERE, `${key}.png`), fullPage: true });
      console.log(key, 'section height', data.height, 'img', data.img.w + 'x' + data.img.h, data.img.currentSrc);
      await ctx.close();
    }
  }
  fs.writeFileSync(path.join(HERE, 'sizes.json'), JSON.stringify(out, null, 1));
  await browser.close();
})();
