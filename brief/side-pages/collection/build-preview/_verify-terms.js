// Offline checks on the terms previews that a still cannot show: the whole section with JAVASCRIPT
// DISABLED and under reduced motion (every numeral must be LIT, every licensed sentence present),
// tap targets, the caption floor, text contrast against the night ground, ink-on-glow anchors,
// cream grounds and horizontal scroll at 360.
//     node brief/side-pages/collection/build-preview/_verify-terms.js
const path=require('path');const fs=require('fs');
function loadPW(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=loadPW();
const FILES=['terms.html','terms-path.html','_terms-wall.html','_terms-spot.html','_terms-all.html'];
const probe=()=>{
  const out={rows:0,dim:0,bad:[],small:[],low:[],cream:0,words:0};
  // worst case ground: the LIGHTEST stop of the 3.1 pixel gradient, #0b1526
  const BG=[11,21,38];
  const lum=c=>{const f=c.map(v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);});
    return 0.2126*f[0]+0.7152*f[1]+0.0722*f[2];};
  const ratio=(a,b)=>{const l1=lum(a),l2=lum(b);return (Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05);};
  const rgb=s=>{const m=s.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
    if(!m)return null;const a=m[4]===undefined?1:parseFloat(m[4]);
    return [0,1,2].map(i=>Math.round(parseFloat(m[i+1])*a+BG[i]*(1-a)));};
  const rows=[...document.querySelectorAll('.env2-coll-terms__line')];
  out.rows=rows.length;
  rows.forEach(li=>{
    const n=li.querySelector('.env2-coll-terms__n');
    if(!n) return;
    if(parseFloat(getComputedStyle(n).opacity)<0.9) out.dim++;
  });
  document.querySelectorAll('.env2-coll-terms a').forEach(el=>{
    const r=el.getBoundingClientRect();
    if(r.height&&r.height<44) out.bad.push(['tap<44',el.className,Math.round(r.height)]);
    const cs=getComputedStyle(el);
    if(cs.backgroundColor.includes('255, 211, 148')&&cs.color!=='rgb(26, 18, 6)') out.bad.push(['ink-on-glow',el.className,cs.color]);
  });
  document.querySelectorAll('.env2-coll-terms__b,.env2-coll-terms__p,.env2-coll-terms__note,.env2-coll-terms__deck,.env2-coll-terms__foot a,.env2-coll-terms__unit').forEach(el=>{
    const f=parseFloat(getComputedStyle(el).fontSize); if(f<13) out.small.push([el.className||el.tagName,f]);});
  document.querySelectorAll('.env2-coll-terms__eyebrow').forEach(el=>{
    const f=parseFloat(getComputedStyle(el).fontSize); if(f<11.5) out.small.push(['label '+el.className,f]);});
  document.querySelectorAll('.env2-coll-terms__b,.env2-coll-terms__p,.env2-coll-terms__note,.env2-coll-terms__deck,.env2-coll-terms__foot a,.env2-coll-terms__unit,.env2-coll-terms__num,.env2-coll-terms__h2,.env2-coll-terms__eyebrow,.env2-coll-terms .env2-btn').forEach(el=>{
    const cs=getComputedStyle(el);const c=rgb(cs.color);if(!c)return;
    const px=parseFloat(cs.fontSize);const bold=parseInt(cs.fontWeight,10)>=700;
    const large=px>=24||(px>=18.66&&bold);
    const r=ratio(c,BG);const need=large?3:4.5;
    if(r<need) out.low.push([el.className||el.tagName,Math.round(px),r.toFixed(2),need]);});
  out.cream=[...document.querySelectorAll('.env2-coll-terms,.env2-coll-terms *')].filter(el=>{
    const b=getComputedStyle(el).backgroundColor;
    return /rgb\(2(4[0-9]|5[0-5]), 2[0-9][0-9], 2[0-9][0-9]\)/.test(b);}).length;
  out.words=(document.querySelector('.env2-coll-terms')||{textContent:''}).textContent.replace(/\s+/g,' ').trim().length;
  out.doc=document.documentElement.scrollWidth>document.documentElement.clientWidth;
  return out;};
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 let fail=0;
 for(const f of FILES){
  const url='file://'+path.resolve('brief/side-pages/collection/build-preview/'+f);
  for(const [mode,opts] of [['NO-JS  ',{javaScriptEnabled:false}],['reduced',{reducedMotion:'reduce'}],['normal ',{}]]){
   for(const [vpn,vp] of [['1440',{width:1440,height:900}],['360 ',{width:360,height:780}]]){
    const ctx=await b.newContext(Object.assign({viewport:vp,locale:'he-IL'},opts));
    const p=await ctx.newPage(); await p.goto(url,{waitUntil:'load'});
    let r;
    if(opts.javaScriptEnabled===false){
      const html=await p.content(); await ctx.close();
      const c2=await b.newContext({viewport:vp,locale:'he-IL'});
      const p2=await c2.newPage();
      await p2.setContent(html.replace(/<script[\s\S]*?<\/script>/g,''),{waitUntil:'load'});
      await p2.waitForTimeout(300); r=await p2.evaluate(probe); await c2.close();
    } else { await p.waitForTimeout(opts.reducedMotion?400:2400); r=await p.evaluate(probe); await ctx.close(); }
    const ok=(r.rows===4&&r.dim===0&&r.bad.length===0&&r.small.length===0&&r.low.length===0&&r.cream===0&&!r.doc&&r.words>400);
    if(!ok) fail++;
    console.log([f.padEnd(17),mode,vpn,'rows='+r.rows,'dim-numerals='+r.dim,'chars='+r.words,
      'taps/ink='+(r.bad.length?JSON.stringify(r.bad.slice(0,3)):'0'),
      'text<13='+(r.small.length?JSON.stringify(r.small.slice(0,3)):'0'),
      'contrast<AA='+(r.low.length?JSON.stringify(r.low.slice(0,3)):'0'),
      'cream='+r.cream,'h-scroll='+r.doc,ok?'OK':'FAIL'].join(' '));
   }
  }
 }
 await b.close();
 console.log(fail?('VERIFY FAIL ('+fail+')'):'VERIFY OK');
 process.exit(fail?2:0);
})();
