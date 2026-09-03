const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
const fs=require('fs'); const OUT='/home/user/ElmsNest/brief/side-pages/collection/verify/ph';
fs.mkdirSync(OUT,{recursive:true});
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of ['coll-wall','coll-all','coll-decor','coll-spot','coll-path']){
 const {p,ctx,srv}=await open(b,key,{width:1440,height:900});
 // light every lamp so we measure the LIT (brightest) state - worst case for cream
 await p.evaluate(()=>{document.querySelectorAll('[data-lamp]').forEach(e=>{e.classList.add('lit');e.style.setProperty('--lit','1');});});
 await p.waitForTimeout(1200);
 const boxes=await p.evaluate(()=>{
  return [...document.querySelectorAll('#env2-coll-bands .env2-pdp-card__ph, #env2-coll-bands [class*=__ph]')]
   .map((e,i)=>{const r=e.getBoundingClientRect();const sc=window.scrollY;
     return {i, x:Math.round(r.x), y:Math.round(r.y+sc), w:Math.round(r.width), h:Math.round(r.height),
       cls:e.className, img:(e.querySelector('img')||{}).currentSrc||''};})
   .filter(o=>o.w>40&&o.h>40);});
 let n=0;
 for(const bx of boxes){
   await p.evaluate(y=>window.scrollTo(0,y-100), bx.y);
   await p.waitForTimeout(350);
   const el=(await p.$$('#env2-coll-bands .env2-pdp-card__ph, #env2-coll-bands [class*=__ph]'))[bx.i];
   try{ await el.screenshot({path:`${OUT}/${key}-${String(bx.i).padStart(2,'0')}.png`}); n++; }catch(e){}
 }
 console.log(key,'photo boxes',boxes.length,'shot',n, JSON.stringify(boxes.map(b=>b.w+'x'+b.h)));
 await ctx.close(); srv.close();
}
await b.close();})();
