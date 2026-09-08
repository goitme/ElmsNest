const fs = require('fs');
const glob = '/tmp/claude-0/-home-user-ElmsNest';
const dir = fs.readdirSync(glob).map(d => `${glob}/${d}/scratchpad/node_modules/playwright`)
              .find(p => fs.existsSync(p));
const { chromium } = require(dir);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const out = {};
  for (const k of ['A','B','C']) {
    for (const [tag, w, h] of [['390', 390, 844], ['1366', 1366, 900]]) {
      const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
      await p.goto('file://' + __dirname + `/harness-${k}.html`, { waitUntil: 'load' });
      await p.evaluate(() => document.fonts.ready);
      await p.evaluate(async () => { for (const i of document.images) if (!i.complete) await i.decode().catch(()=>{}); });
      await p.waitForTimeout(400);
      const m = await p.evaluate(() => {
        const s = document.querySelector('.ens-pdp-weather');
        const r = s.getBoundingClientRect();
        const texts = [];
        for (const el of document.querySelectorAll('.ens-pdp-weather__cap, .ens-pdp-weather__credit, .ens-pdp-weather__line, .ens-pdp-weather__h')) {
          const b = el.getBoundingClientRect(); const cs = getComputedStyle(el);
          texts.push({ cls: el.className, text: el.textContent.trim(), color: cs.color, size: cs.fontSize,
                       x: Math.round(b.x + scrollX), y: Math.round(b.y + scrollY), w: Math.round(b.width), h: Math.round(b.height) });
        }
        const tile = document.querySelector('.ens-pdp-weather__frame').getBoundingClientRect();
        const img = document.querySelector('.ens-pdp-weather__frame img');
        return { height: Math.round(r.height), tile: [Math.round(tile.width), Math.round(tile.height)],
                 currentSrc: img.currentSrc.split('/').pop(), texts };
      });
      out[`weather-${k}-${tag}`] = m;
      await p.screenshot({ path: `${__dirname}/weather-${k}-${tag}.png`, fullPage: true });
      // the same shot with the text hidden: the exact background for contrast.py
      await p.addStyleTag({ content: '.ens-pdp-weather__cap,.ens-pdp-weather__credit,.ens-pdp-weather__line,.ens-pdp-weather__h{color:transparent!important}' });
      fs.mkdirSync(`${__dirname}-bg`, { recursive: true });
      await p.screenshot({ path: `${__dirname}-bg/weather-${k}-${tag}.png`, fullPage: true });
      await p.close();
    }
  }
  fs.writeFileSync(`${__dirname}/sizes.json`, JSON.stringify(out, null, 1));
  for (const k of Object.keys(out)) console.log(k, out[k].height + 'px', 'tile', out[k].tile.join('x'), out[k].currentSrc);
  await b.close();
})();
