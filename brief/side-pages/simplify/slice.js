const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const DIR = __dirname, OUT = path.join(DIR, 'slices');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent('<canvas id=c></canvas><img id=i>');
  const files = fs.readdirSync(DIR).filter(f => /-(m|d)-full\.png$/.test(f));
  for (const f of files) {
    const vh = /-m-full/.test(f) ? 844 : 900;
    const b64 = fs.readFileSync(path.join(DIR, f)).toString('base64');
    const n = await page.evaluate(async ({ b64, vh }) => {
      const img = document.getElementById('i');
      await new Promise((res, rej) => { img.onload = res; img.onerror = rej; img.src = 'data:image/png;base64,' + b64; });
      const c = document.getElementById('c'); const ctx = c.getContext('2d');
      const out = []; const W = img.naturalWidth, H = img.naturalHeight;
      for (let y = 0, k = 0; y < H; y += vh, k++) {
        const h = Math.min(vh, H - y); c.width = W; c.height = h;
        ctx.drawImage(img, 0, y, W, h, 0, 0, W, h);
        out.push(c.toDataURL('image/png'));
      }
      window.__out = out; return out.length;
    }, { b64, vh });
    for (let k = 0; k < n; k++) {
      const d = await page.evaluate(k => window.__out[k], k);
      fs.writeFileSync(path.join(OUT, f.replace('-full.png', `-s${String(k + 1).padStart(2, '0')}.png`)), Buffer.from(d.split(',')[1], 'base64'));
    }
    console.log(f, '->', n, 'slices');
  }
  await browser.close();
})();
