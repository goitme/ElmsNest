// What a still cannot show for 4.7: the section with JAVASCRIPT DISABLED and under reduced motion
// (the garden must be at its full 80% and the word at its bright stroke immediately), tap targets,
// the caption floor, ink-on-glow anchors, cream grounds, horizontal scroll at 360 - and, because the
// ground here is a PHOTOGRAPH, the real contrast of every line of text against the pixels actually
// behind it: the text is hidden, its exact box is screenshot, and the 95th-percentile brightest
// pixel behind the glyphs is the background the ratio is computed from. Nothing is guessed.
//     node brief/side-pages/collection/build-preview/_verify-goodnight.js
const path = require('path'), fs = require('fs');
function loadPW(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const { chromium } = loadPW();
const DIR = 'brief/side-pages/collection/build-preview/';
const FILES = ['goodnight.html','goodnight-path.html','_goodnight-wall.html','_goodnight-spot.html',
               '_goodnight-all.html','_goodnight-noblocks.html','_goodnight-noimage.html'];
const TEXT = ['.env2-coll-goodnight__label','.env2-coll-goodnight__name','.env2-coll-goodnight__n',
              '.env2-coll-goodnight__all','.env2-coll-goodnight__line','.env2-coll-goodnight__photo'];
const lum = (r,g,b) => { const f=c=>{c/=255;return c<=.03928?c/12.92:Math.pow((c+.055)/1.055,2.4);}; return .2126*f(r)+.7152*f(g)+.0722*f(b); };
const ratio = (l1,l2) => (Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);

const probe = (TEXT) => {
  const out = { places:0, bad:[], small:[], cream:0, chars:0, gardenOpacity:null, stroke:null, deco:[] };
  const root = document.querySelector('.env2-coll-goodnight');
  if (!root) return out;
  out.places = document.querySelectorAll('.env2-coll-goodnight__a').length;
  const g = document.querySelector('.env2-coll-goodnight__garden');
  if (g) out.gardenOpacity = parseFloat(getComputedStyle(g).opacity).toFixed(3);
  const w = document.querySelector('.env2-coll-goodnight__big');
  if (w) { const cs = getComputedStyle(w);
    out.stroke = cs.webkitTextStrokeColor + ' / fill ' + cs.color;
    if (cs.color !== 'rgba(0, 0, 0, 0)' && cs.color !== 'transparent') out.bad.push(['word-is-filled', cs.color]); }
  root.querySelectorAll('a').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.height && r.height < 44) out.bad.push(['tap<44', el.className, Math.round(r.height)]);
    const cs = getComputedStyle(el);
    if (cs.backgroundColor.includes('255, 211, 148') && cs.color !== 'rgb(26, 18, 6)')
      out.bad.push(['ink-on-glow', el.className, cs.color]);
    // every anchor must carry a visible affordance: its own underline, or one on a child
    const own = cs.textDecorationLine !== 'none';
    const kid = [...el.querySelectorAll('*')].some(k => getComputedStyle(k).textDecorationLine !== 'none');
    if (!own && !kid) out.deco.push(el.className);
  });
  root.querySelectorAll(TEXT.join(',')).forEach(el => {
    const f = parseFloat(getComputedStyle(el).fontSize);
    const floor = el.classList.contains('env2-coll-goodnight__label') ? 11.5 : 13;
    if (f < floor) out.small.push([el.className, f]);
  });
  out.cream = [...root.querySelectorAll('*')].filter(el => {
    const b = getComputedStyle(el).backgroundColor;
    return /rgb\(2(4[0-9]|5[0-5]), 2[0-9][0-9], 2[0-9][0-9]\)/.test(b); }).length;
  out.chars = root.textContent.replace(/\s+/g,' ').trim().length;
  out.doc = document.documentElement.scrollWidth > document.documentElement.clientWidth;
  return out;
};

(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const reader = await (await b.newContext()).newPage();
  await reader.setContent('<canvas id=c></canvas>');
  let fail = 0;

  console.log('== state, tap targets, floors, cream, horizontal scroll');
  for (const f of FILES) {
    const url = 'file://' + path.resolve(DIR + f);
    for (const [mode, opts] of [['NO-JS  ',{javaScriptEnabled:false}],['reduced',{reducedMotion:'reduce'}],['normal ',{}]]) {
      for (const [vpn, vp] of [['1440',{width:1440,height:900}],['360 ',{width:360,height:780}]]) {
        const ctx = await b.newContext(Object.assign({viewport:vp,locale:'he-IL'},opts));
        await ctx.route(/^https?:\/\//, r => r.abort());
        const p = await ctx.newPage(); await p.goto(url,{waitUntil:'load'});
        let r;
        if (opts.javaScriptEnabled === false) {
          const html = await p.content(); await ctx.close();
          const c2 = await b.newContext({viewport:vp,locale:'he-IL'});
          const p2 = await c2.newPage();
          await p2.setContent(html.replace(/<script[\s\S]*?<\/script>/g,''),{waitUntil:'load'});
          await p2.waitForTimeout(400); r = await p2.evaluate(probe, TEXT); await c2.close();
        } else { await p.waitForTimeout(opts.reducedMotion ? 500 : 2600); r = await p.evaluate(probe, TEXT); await ctx.close(); }
        const litOK = r.gardenOpacity === null || parseFloat(r.gardenOpacity) > 0.79;
        const ok = litOK && r.bad.length===0 && r.small.length===0 && r.deco.length===0 && r.cream===0 && !r.doc && r.chars>60;
        if (!ok) fail++;
        console.log(['  '+f.padEnd(26), mode, vpn, 'places='+r.places, 'garden-opacity='+r.gardenOpacity,
          'chars='+r.chars, 'taps/ink='+(r.bad.length?JSON.stringify(r.bad.slice(0,3)):'0'),
          'text<floor='+(r.small.length?JSON.stringify(r.small.slice(0,2)):'0'),
          'links-without-a-rule='+(r.deco.length?JSON.stringify(r.deco.slice(0,2)):'0'),
          'cream='+r.cream, 'h-scroll='+r.doc, ok?'OK':'FAIL'].join(' '));
      }
    }
  }

  console.log('\n== real contrast against the pixels behind the text (worst = 95th-percentile brightest)');
  for (const f of ['goodnight.html','goodnight-path.html','_goodnight-all.html']) {
    console.log('  --- ' + f);
    for (const [vname, vp] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}]]) {
      const ctx = await b.newContext({viewport:vp,deviceScaleFactor:1,locale:'he-IL'});
      await ctx.route(/^https?:\/\//, r => r.abort());
      const p = await ctx.newPage();
      await p.goto('file://' + path.resolve(DIR + f), {waitUntil:'load'});
      await p.waitForTimeout(2400);
      const sels = await p.evaluate(t => { const o=[]; document.querySelectorAll(t.join(',')).forEach((el,i)=>{
        el.setAttribute('data-probe','p'+i); o.push('p'+i); }); return o; }, TEXT);
      const rows = [];
      for (const id of sels) {
        const info = await p.evaluate(s => { const el=document.querySelector('[data-probe="'+s+'"]');
          const r=el.getBoundingClientRect(); if(!r.width||!r.height) return null;
          el.style.visibility='hidden';
          return {x:Math.max(0,Math.round(r.left)),y:Math.max(0,Math.round(r.top+scrollY)),
                  w:Math.round(r.width),h:Math.round(r.height),color:getComputedStyle(el).color,
                  px:parseFloat(getComputedStyle(el).fontSize),
                  bold:parseInt(getComputedStyle(el).fontWeight,10)>=700,
                  label:(el.className||'').replace('env2-coll-goodnight__','')}; }, id);
        if (!info) continue;
        const buf = await p.screenshot({clip:{x:info.x,y:info.y,width:info.w,height:info.h},fullPage:true});
        await p.evaluate(s => { document.querySelector('[data-probe="'+s+'"]').style.visibility=''; }, id);
        const ls = await reader.evaluate(async d => { const img=new Image(); img.src=d; await img.decode();
          const c=document.getElementById('c'); c.width=img.width; c.height=img.height;
          const g=c.getContext('2d'); g.drawImage(img,0,0);
          const data=g.getImageData(0,0,c.width,c.height).data; const out=[];
          for(let i=0;i<data.length;i+=4) out.push([data[i],data[i+1],data[i+2]]); return out;
        }, 'data:image/png;base64,'+buf.toString('base64'));
        const m = info.color.match(/(\d+), (\d+), (\d+)/); const fg = lum(+m[1],+m[2],+m[3]);
        const sorted = ls.map(c=>lum(c[0],c[1],c[2])).sort((a,z)=>a-z);
        const worst = sorted[Math.floor(sorted.length*.95)];
        const large = info.px>=24 || (info.px>=18.66 && info.bold);
        const need = large ? 3 : 4.5;
        const got = ratio(fg,worst);
        if (got < need) fail++;
        rows.push([info.label, info.px, got.toFixed(2), need, got<need]);
      }
      console.log('    ' + vname);
      rows.forEach(r => console.log('      ' + (r[4]?'!! ':'   ') + String(r[0]).padEnd(10) + ' ' + String(r[1]).padStart(5) + 'px  worst ' + r[2] + '  need ' + r[3]));
      await ctx.close();
    }
  }
  // do-not 10: no cream, beige or brown SURFACE anywhere above the Kalles footer, including a
  // photograph whose own ground is cream. Sampled off the rendered pixels of the whole section.
  console.log('\n== the ground, sampled off the rendered pixels (do-not 10)');
  for (const f of ['goodnight.html','goodnight-path.html','_goodnight-wall.html','_goodnight-spot.html','_goodnight-all.html']) {
    for (const [vn, vp] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}]]) {
      const ctx = await b.newContext({viewport:vp,deviceScaleFactor:1,locale:'he-IL'});
      await ctx.route(/^https?:\/\//, r => r.abort());
      const p = await ctx.newPage();
      await p.goto('file://' + path.resolve(DIR + f), {waitUntil:'load'});
      await p.waitForTimeout(2400);
      const r0 = await p.evaluate(() => { const el=document.querySelector('.env2-coll-goodnight');
        const r=el.getBoundingClientRect();
        return {y:Math.max(0,Math.round(r.top+scrollY)),w:Math.round(r.width),h:Math.round(r.height)}; });
      const buf = await p.screenshot({clip:{x:0,y:r0.y,width:r0.w,height:r0.h},fullPage:true});
      const st = await reader.evaluate(async d => { const img=new Image(); img.src=d; await img.decode();
        const c=document.getElementById('c'); c.width=120; c.height=120;
        const g=c.getContext('2d'); g.drawImage(img,0,0,120,120);
        const data=g.getImageData(0,0,120,120).data;
        let cream=0, warm=0, sum=0, n=0;
        for (let i=0;i<data.length;i+=4){ const R=data[i],G=data[i+1],B=data[i+2];
          const L=.2126*R+.7152*G+.0722*B; sum+=L; n++;
          if (L>170 && R>G && G>B && (R-B)<70) cream++;
          if (L>90 && L<170 && R>G && G>B && (R-B)>25 && (R-B)<90) warm++; }
        return {cream:100*cream/n, warm:100*warm/n, mean:sum/n}; },
        'data:image/png;base64,'+buf.toString('base64'));
      // 0.5% of a 120x120 sample is 72 pixels: a lit bulb core or a plant pot in a night photograph,
      // never a surface. Anything above 2% would be a ground and is a breach.
      const bad = st.cream > 2 || st.warm > 2;
      if (bad) fail++;
      console.log('  ' + (bad?'!! ':'   ') + f.padEnd(26) + vn.padEnd(8) +
        'cream%=' + st.cream.toFixed(2) + '  warm-mid%=' + st.warm.toFixed(2) +
        '  mean-luminance=' + st.mean.toFixed(1) + '/255');
      await ctx.close();
    }
  }

  await b.close();
  console.log(fail ? ('VERIFY FAIL (' + fail + ')') : 'VERIFY OK');
  process.exit(fail ? 2 : 0);
})();
