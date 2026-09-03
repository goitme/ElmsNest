// Offline checks on the ruler section that a still cannot show: the radio narrowing in a context with
// JAVASCRIPT DISABLED, the computed colour of every pill and CTA (core REPORT §9.1), tap targets, the
// caption floor, cream surfaces, and the stills at a chosen stop.
//   node brief/side-pages/collection/build-preview/_verify-ruler.js
const path=require('path');const fs=require('fs');
function loadPW(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=loadPW();
const DIR='brief/side-pages/collection/build-preview/';
const PAGES=[['ruler.html','10','decor'],['ruler-path.html','4','path'],
             ['_ruler-wall.html','129_90','wall'],['_ruler-spot.html','169_90','spot'],
             ['_ruler-all.html',null,'all'],['_ruler-sorted.html','10','decor?sort_by=price-ascending']];

const AUDIT=()=>{
  const out={bad:[],small:[],cream:0,overflow:{}};
  document.querySelectorAll('.env2-btn,.env2-coll-ruler__pill,.env2-coll-ruler__sortlink,.env2-link,.env2-coll-ruler__title a,.env2-coll-ruler__placelink,.env2-coll-ruler__unit a').forEach(el=>{
    const cs=getComputedStyle(el);
    const box=el.closest('.env2-coll-ruler__rowhead')||el;
    const r=box.getBoundingClientRect();
    if(r.width&&r.height&&r.height<44) out.bad.push(['tap<44',(el.className||el.tagName)+'/'+(box.className||''),Math.round(r.height)]);
    if(cs.backgroundColor.includes('255, 211, 148')&&cs.color!=='rgb(26, 18, 6)') out.bad.push(['ink-on-glow',el.className,cs.color]);
  });
  document.querySelectorAll('.env2-coll-ruler__axis,.env2-coll-ruler__numcap,.env2-coll-ruler__footnote,.env2-coll-ruler__stopq,.env2-coll-rail__per,.env2-coll-rail__miss,.env2-coll-ruler__end,.env2-coll-ruler__placenames,.env2-coll-ruler__unitk,.env2-coll-ruler__sortnote').forEach(el=>{
    const fs=parseFloat(getComputedStyle(el).fontSize); if(fs<13) out.small.push([el.className,fs]);});
  out.cream=[...document.querySelectorAll('*')].filter(el=>{const b=getComputedStyle(el).backgroundColor;
    return /rgb\(2(4[0-9]|5[0-5]), 2[0-9][0-9], 2[0-9][0-9]\)/.test(b);}).length;
  const de=document.documentElement;
  out.overflow.page=de.scrollWidth>de.clientWidth;
  out.overflow.widest=Math.max(0,de.scrollWidth-de.clientWidth);
  const sec=document.getElementById('env2-coll-ruler');
  out.sectionH=sec?Math.round(sec.getBoundingClientRect().height):0;
  const foot=document.querySelector('.env2-coll-ruler__foot');
  out.footBottom=foot?Math.round(foot.getBoundingClientRect().bottom+window.scrollY):0;
  const sort=document.querySelector('.env2-coll-ruler__sort');
  out.sortTop=sort?Math.round(sort.getBoundingClientRect().top+window.scrollY):0;
  const pills=document.querySelector('.env2-coll-ruler__pills');
  out.pillsTop=pills?Math.round(pills.getBoundingClientRect().top+window.scrollY):0;
  return out;
};

const READ=()=>{const rows=[];document.querySelectorAll('.env2-coll-ruler__row').forEach(r=>{
  const t=r.querySelector('.env2-coll-ruler__title').textContent.trim().slice(0,26);
  const vis=[...r.querySelectorAll('.env2-coll-rail__v')].filter(v=>getComputedStyle(v).display!=='none');
  rows.push({t,op:getComputedStyle(r).opacity,
    shown:vis.map(v=>v.dataset.state+': '+v.textContent.replace(/\s+/g,' ').trim())});});
  return rows;};

(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 for(const [file,stop,label] of PAGES){
  const url='file://'+path.resolve(DIR+file);
  for(const [vname,vp] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}],['narrow',{width:360,height:800}]]){
   // JAVASCRIPT DISABLED — this is the §3.4 no-JS contract, measured, not asserted.
   const ctx=await b.newContext({viewport:vp,deviceScaleFactor:1,locale:'he-IL',javaScriptEnabled:false});
   const p=await ctx.newPage(); await p.goto(url,{waitUntil:'load'});
   const a=await p.evaluate('('+AUDIT.toString()+')()');
   console.log(`${label.padEnd(30)} ${vname.padEnd(8)} noJS  h=${String(a.sectionH).padStart(5)} overflow=${a.overflow.page}(${a.overflow.widest}) tap/ink=${JSON.stringify(a.bad)} small=${JSON.stringify(a.small)} cream=${a.cream} pillsTop=${a.pillsTop} sortTop=${a.sortTop} footBottom=${a.footBottom}`);
   if(stop&&vname==='desktop'){
     const rows=await p.evaluate('('+READ.toString()+')()');
     console.log('   at הכול (no JS, nothing clicked):');
     rows.forEach(r=>console.log('     '+(r.op!=='1'?'[DIM '+r.op+'] ':'          ')+r.t+'  ->  '+r.shown.join(' | ')));
   }
   await ctx.close();
  }
  if(!stop) continue;
  // narrowing, still with no script on the page: only the radio's checked state changes
  const ctx=await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:2,locale:'he-IL',reducedMotion:'reduce'});
  const p=await ctx.newPage(); await p.goto(url,{waitUntil:'load'});
  await p.evaluate(k=>{document.getElementById('env2-stop-'+k).checked=true;},stop);
  const rows=await p.evaluate('('+READ.toString()+')()');
  console.log('   at stop '+stop+':');
  rows.forEach(r=>console.log('     '+(r.op!=='1'?'[DIM '+r.op+'] ':'          ')+r.t+'  ->  '+r.shown.join(' | ')));
  const lit=await p.evaluate(()=>[...document.querySelectorAll('.env2-coll-rail__dot')]
     .filter(d=>{const t=getComputedStyle(d).transform;return t!=='none'&&t!=='matrix(1, 0, 0, 1, 0, 0)';}).length);
  const cur=await p.evaluate(()=>getComputedStyle(document.querySelector('.env2-coll-ruler__cursor')).insetInlineStart);
  console.log('   lit dots='+lit+'  cursor inset-inline-start='+cur);
  const el=await p.$('.env2-coll-ruler__body');
  await el.screenshot({path:DIR+'_ruler-'+label.replace(/[^a-z]/g,'')+'-at-'+stop+'.png'});
  await ctx.close();
 }
 await b.close();})();
