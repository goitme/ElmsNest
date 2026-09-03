// Real contrast over the photograph: for every text element in §4.1 that is read straight off the
// scene image, hide the text, screenshot the exact box it occupies, and measure the worst pixel behind
// it. Nothing here guesses a background colour — the ground is a photograph and only the pixels know.
// Usage: node _contrast-scene.js <file...>
const path = require('path'), fs = require('fs');
function loadPW(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const { chromium } = loadPW();
const lum = (r,g,b) => { const f=c=>{c/=255;return c<=.03928?c/12.92:Math.pow((c+.055)/1.055,2.4);}; return .2126*f(r)+.7152*f(g)+.0722*f(b); };
const ratio = (l1,l2) => (Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);

const TARGETS = [
  ['.env2-coll-scene__eyebrow', 'eyebrow'],
  ['.env2-coll-scene__h1', 'h1'],
  ['.env2-coll-scene__deck', 'deck'],
  ['.env2-coll-scene__suits', 'suits'],
  ['.env2-coll-scene__counts', 'counts'],
  ['.env2-coll-scene__tagname', 'pin name'],
  ['.env2-coll-scene__tagval', 'pin value'],
  ['.env2-pdp-card__title', 'card title'],
  ['.env2-pdp-card__axis', 'card axis'],
  ['.env2-pdp-card__price .env2-price', 'card price'],
  ['.env2-pdp-card__unit', 'card unit line'],
  ['.env2-coll-scene__p', 'description'],
];

(async () => {
  const files = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const reader = await (await b.newContext()).newPage();
  await reader.setContent('<canvas id=c></canvas>');
  for (const f of files) {
    console.log('\n=== ' + path.basename(f));
    for (const [vname, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844 }]]) {
      const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: 1, locale: 'he-IL' });
      await ctx.route(/^https?:\/\//, r => r.abort());
      const p = await ctx.newPage();
      await p.goto('file://' + path.resolve(f), { waitUntil: 'load' });
      await p.waitForTimeout(2200);
      const rows = [];
      for (const [sel, label] of TARGETS) {
        const info = await p.evaluate(s => { const el = document.querySelector(s); if (!el) return null;
          const r = el.getBoundingClientRect(); if (!r.width || !r.height) return null;
          el.style.visibility = 'hidden';
          return { x: Math.max(0, Math.round(r.left)), y: Math.max(0, Math.round(r.top + scrollY)), w: Math.round(r.width), h: Math.round(r.height), color: getComputedStyle(el).color }; }, sel);
        if (!info) continue;
        const buf = await p.screenshot({ clip: { x: info.x, y: info.y, width: info.w, height: info.h }, fullPage: true });
        await p.evaluate(s => { const el = document.querySelector(s); if (el) el.style.visibility = ''; }, sel);
        const px = await reader.evaluate(async (d) => {
          const img = new Image(); img.src = d; await img.decode();
          const c = document.getElementById('c'); c.width = img.width; c.height = img.height;
          const g = c.getContext('2d'); g.drawImage(img, 0, 0);
          const data = g.getImageData(0, 0, c.width, c.height).data; const out = [];
          for (let i = 0; i < data.length; i += 4) out.push([data[i], data[i+1], data[i+2]]);
          return out;
        }, 'data:image/png;base64,' + buf.toString('base64'));
        const m = info.color.match(/(\d+), (\d+), (\d+)/); const fg = lum(+m[1], +m[2], +m[3]);
        const ls = px.map(c => lum(c[0], c[1], c[2])).sort((a, z) => a - z);
        // worst case = the 95th-percentile brightest background pixel behind the glyphs
        const worst = ls[Math.floor(ls.length * .95)];
        const med = ls[Math.floor(ls.length * .5)];
        rows.push([label, ratio(fg, worst).toFixed(2), ratio(fg, med).toFixed(2), info.color]);
      }
      console.log('  ' + vname + '  (worst / median contrast against the real pixels behind the text)');
      rows.forEach(r => console.log('    ' + (parseFloat(r[1]) < 4.5 ? '!! ' : '   ') + r[0].padEnd(15) + ' worst ' + r[1] + '  median ' + r[2] + '  ' + r[3]));
      await ctx.close();
    }
  }
  await b.close();
})();
