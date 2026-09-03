// Offline checks on the span previews that a still cannot show: the bars at full length with
// JAVASCRIPT DISABLED and under reduced motion, tap targets, the caption floor, ink-on-glow, cream
// grounds, and that no rung is ever hidden.  node brief/side-pages/collection/build-preview/_verify-span.js
const path=require('path');const fs=require('fs');
function loadPW(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=loadPW();
const FILES=['span-path.html','_span-all.html','_span-spot.html','span.html'];
const probe=()=>{
  const out={rungs:0,zero:0,hidden:0,bad:[],small:[],cream:0,bars:[]};
  const rungs=[...document.querySelectorAll('.env2-coll-span__rung')];
  out.rungs=rungs.length;
  rungs.forEach(li=>{
    if(getComputedStyle(li).display==='none') out.hidden++;
    const s=li.querySelector('.env2-coll-span__solid');
    if(s){const w=s.getBoundingClientRect().width; if(w<2) out.zero++; out.bars.push(Math.round(w));}
  });
  document.querySelectorAll('a').forEach(el=>{
    const r=el.getBoundingClientRect();
    if(r.height&&r.height<44) out.bad.push(['tap<44',el.className||el.closest('[class]').className,Math.round(r.height)]);
    const cs=getComputedStyle(el);
    if(cs.backgroundColor.includes('255, 211, 148')&&cs.color!=='rgb(26, 18, 6)') out.bad.push(['ink-on-glow',el.className,cs.color]);
  });
  document.querySelectorAll('.env2-coll-span__axis,.env2-coll-span__per,.env2-coll-span__to,.env2-coll-span__note,.env2-coll-span__foot,.env2-coll-span__bandn,.env2-coll-span__cell-per,.env2-coll-span__tbl tbody th,.env2-coll-span__tbl tbody td').forEach(el=>{
    const f=parseFloat(getComputedStyle(el).fontSize); if(f<13) out.small.push([el.className||el.tagName,f]);});
  // a column header is a LABEL (§3.2: labels 11.5px, information-bearing captions 13px)
  document.querySelectorAll('.env2-coll-span__tbl thead th,.env2-coll-span__cap2,.env2-coll-span__scalelabel').forEach(el=>{
    const f=parseFloat(getComputedStyle(el).fontSize); if(f<11.5) out.small.push(['label '+(el.className||el.tagName),f]);});
  out.cream=[...document.querySelectorAll('.env2-coll-span *')].filter(el=>{const b=getComputedStyle(el).backgroundColor;
    return /rgb\(2(4[0-9]|5[0-5]), 2[0-9][0-9], 2[0-9][0-9]\)/.test(b);}).length;
  out.doc=document.documentElement.scrollWidth>document.documentElement.clientWidth;
  return out;};
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 let fail=0;
 for(const f of FILES){
  const url='file://'+path.resolve('brief/side-pages/collection/build-preview/'+f);
  for(const [mode,opts] of [['NO-JS  ',{javaScriptEnabled:false}],['reduced',{reducedMotion:'reduce'}],['normal ',{}]]){
   for(const [vpn,vp] of [['1440',{width:1440,height:900}],['360 ',{width:360,height:780}]]){
    // a second context WITH js is used only to read the DOM of the no-js render
    const ctx=await b.newContext(Object.assign({viewport:vp,locale:'he-IL'},opts));
    const p=await ctx.newPage(); await p.goto(url,{waitUntil:'load'});
    let r;
    if(opts.javaScriptEnabled===false){
      const html=await p.content(); await ctx.close();
      const c2=await b.newContext({viewport:vp,locale:'he-IL'});
      const p2=await c2.newPage();
      // the same bytes, minus every <script>: exactly what a no-JS browser paints
      await p2.setContent(html.replace(/<script[\s\S]*?<\/script>/g,''),{waitUntil:'load'});
      await p2.waitForTimeout(300); r=await p2.evaluate(probe); await c2.close();
    } else { await p.waitForTimeout(opts.reducedMotion?300:2200); r=await p.evaluate(probe); await ctx.close(); }
    const ok=(r.zero===0&&r.hidden===0&&r.bad.length===0&&r.small.length===0&&r.cream===0&&!r.doc);
    if(!ok) fail++;
    console.log([f.padEnd(16),mode,vpn,'rungs='+r.rungs,'zero-bars='+r.zero,'hidden='+r.hidden,
      'taps/contrast='+(r.bad.length?JSON.stringify(r.bad.slice(0,3)):'0'),
      'captions<13='+(r.small.length?JSON.stringify(r.small.slice(0,3)):'0'),
      'cream='+r.cream,'h-scroll='+r.doc,ok?'OK':'FAIL'].join(' '));
   }
  }
 }
 await b.close();
 console.log(fail?('VERIFY FAIL ('+fail+')'):'VERIFY OK');
 process.exit(fail?2:0);
})();
