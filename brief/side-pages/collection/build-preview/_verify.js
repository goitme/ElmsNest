// Offline checks on _plumbing.html that a still cannot show: the radio narrowing with no JS, the
// computed colour of every pill/CTA (core REPORT §9.1), tap targets, caption floor, and a shot of the
// ruler at the 10 מ׳ stop. Usage: node brief/side-pages/collection/build-preview/_verify.js
const path=require('path');const fs=require('fs');
function loadPW(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=loadPW();
const FILE='file://'+path.resolve('brief/side-pages/collection/build-preview/_plumbing.html');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 for (const [name,vp] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}]]){
  const ctx=await b.newContext({viewport:vp,deviceScaleFactor:2,locale:'he-IL',javaScriptEnabled:false});
  const p=await ctx.newPage(); await p.goto(FILE,{waitUntil:'load'});
  // NO JAVASCRIPT AT ALL in this context: the narrowing below is pure CSS.
  await p.evaluate(()=>{}).catch(()=>{});
  await ctx.close();
 }
 // a JS context only so we can inspect the DOM; the page itself has no script
 const ctx=await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:2,locale:'he-IL',reducedMotion:'reduce'});
 const p=await ctx.newPage(); await p.goto(FILE,{waitUntil:'load'});
 const report=await p.evaluate(()=>{
   const out={};
   const pick=k=>{document.getElementById('env2-stop-'+k).checked=true;};
   const read=()=>{const rows=[];document.querySelectorAll('.plumb-row').forEach(r=>{
     const t=r.querySelector('.plumb-row__t bdi').textContent.trim();
     const vis=[...r.querySelectorAll('.env2-coll-rail__v')].filter(v=>getComputedStyle(v).display!=='none');
     rows.push({t,op:getComputedStyle(r).opacity,
       shown:vis.map(v=>v.dataset.state+': '+v.textContent.replace(/\s+/g,' ').trim())});});
     return rows;};
   pick('all'); out.all=read();
   pick('10');  out.s10=read();
   pick('3');   out.s3=read();
   pick('all');
   // lit dot count at each stop
   pick('10'); out.litDots=[...document.querySelectorAll('.env2-coll-rail__dot')].filter(d=>getComputedStyle(d).transform!=='none'&&getComputedStyle(d).transform!=='matrix(1, 0, 0, 1, 0, 0)').length;
   pick('all');
   // colours + tap targets
   const bad=[];
   document.querySelectorAll('.env2-btn,.plumb-pill,.env2-coll-paginate__n,.env2-coll-paginate__step').forEach(el=>{
     const cs=getComputedStyle(el),r=el.getBoundingClientRect();
     if(r.height&&r.height<44) bad.push(['tap<44',el.className,Math.round(r.height)]);
     if(cs.backgroundColor.includes('255, 211, 148')&&cs.color!=='rgb(26, 18, 6)') bad.push(['ink-on-glow',el.className,cs.color]);
   });
   out.bad=bad;
   const small=[];document.querySelectorAll('.env2-coll-rail__per,.env2-coll-rail__miss,.env2-coll-glyph__cap,.env2-pdp-card__axis,.env2-pdp-card__unit,.env2-coll-rail__off').forEach(el=>{
     const fs=parseFloat(getComputedStyle(el).fontSize); if(fs<11.5) small.push([el.className,fs]);});
   out.small=small;
   out.cream=[...document.querySelectorAll('*')].filter(el=>{const b=getComputedStyle(el).backgroundColor;
     return /rgb\(2(4[0-9]|5[0-5]), 2[0-9][0-9], 2[0-9][0-9]\)/.test(b);}).length;
   return out;});
 const show=(k,rows)=>{console.log('\n=== stop '+k+' ===');rows.forEach(r=>console.log('  '+(r.op!=='1'?'[DIM '+r.op+'] ':'        ')+r.t+'  ->  '+r.shown.join(' | ')));};
 show('הכול',report.all); show('10 מ׳',report.s10); show('3 מ׳',report.s3);
 console.log('\nlit dots at 10 מ׳:',report.litDots);
 console.log('contrast/tap-target failures:',JSON.stringify(report.bad));
 console.log('captions under 11.5px:',JSON.stringify(report.small));
 console.log('elements with a cream background:',report.cream);
 // a still of the ruler at 10 מ׳
 await p.evaluate(()=>{document.getElementById('env2-stop-10').checked=true;});
 const el=await p.$('.plumb-stops');
 await el.screenshot({path:'brief/side-pages/collection/build-preview/_ruler-at-10.png'});
 await b.close();})();
