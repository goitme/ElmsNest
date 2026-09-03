const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
const fs=require('fs');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const [key,tag] of [['pdp-pre','PRE (mirror 12:49, before pdp-card upsert)'],['pdp','POST (my fresh mirror)']]){
 for(const [w,h] of [[1440,900],[390,844]]){
  const {p,ctx,srv}=await open(b,key,{width:w,height:h},{reducedMotion:'reduce'});
  const info=await p.evaluate(()=>{
   const q=s=>document.querySelector(s),qa=s=>[...document.querySelectorAll(s)],cs=e=>getComputedStyle(e);
   const t=q('.env2-pdp-card__title');
   const lampImg=q('[data-lamp] .env2-ph img');
   return {bodyClass:document.body.className.slice(0,60),
     cardTitleTag:t?t.tagName:null, nCards:qa('.env2-pdp-card').length,
     h1n:document.querySelectorAll('h1').length,
     headings:qa('h1,h2,h3').map(e=>e.tagName).join(','),
     groundColl: !!q('#env2-ground-collection'),
     collCss: qa('style[id*=coll]').map(e=>e.id),
     lampFilter: lampImg?cs(lampImg).filter:null,
     bodyBI: cs(document.body).backgroundImage.slice(0,120),
     phBefore: (()=>{const e=q('.env2-pdp-card__ph');return e?getComputedStyle(e,'::before').backgroundColor+'/'+getComputedStyle(e,'::before').content:null})(),
     pageH: document.body.scrollHeight};});
  console.log(`${key} ${w}x${h} ${tag}`); console.log('  '+JSON.stringify(info));
  await p.evaluate(()=>{document.querySelectorAll('[data-lamp]').forEach(e=>{e.classList.add('lit');e.style.setProperty('--lit','1')});
    document.querySelectorAll('*').forEach(e=>{e.style.transition='none';e.style.animation='none'});});
  await p.waitForTimeout(1200);
  await p.screenshot({path:`/home/user/ElmsNest/brief/side-pages/collection/verify/${key}-${w}.png`,fullPage:true});
  await ctx.close(); srv.close();
 }}
await b.close();})();
