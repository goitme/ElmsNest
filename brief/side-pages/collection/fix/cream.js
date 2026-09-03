// CREATIVE-03: mean RGB + cream fraction over every band card photo box and every band figure.
const {chromium,faceCss,serve}=require('/home/user/ElmsNest/brief/side-pages/collection/fix/probe.js');
const fs=require('fs');
const KEYS=(process.argv[2]||'coll-wall,coll-all,coll-decor').split(',');
const OUT=process.argv[3]||'/tmp/cream';fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){const srv=serve(`/home/user/ElmsNest/brief/inventory/${key}`,'index.html');
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
 const ctx=await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1,locale:'he-IL'});
 await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
  if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
 const p=await ctx.newPage();await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
 await p.waitForTimeout(1200);
 await p.evaluate(async()=>{document.querySelectorAll('img[loading="lazy"]').forEach(i=>i.loading='eager');
  document.documentElement.style.scrollBehavior='auto';
  for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,60));}
  window.scrollTo({top:0,behavior:'instant'});});
 await p.waitForTimeout(2500);
 const boxes=await p.evaluate(()=>{const out=[];
  document.querySelectorAll('#env2-coll-bands .env2-pdp-card__ph, #env2-coll-bands .env2-coll-bands__fig').forEach((e,i)=>{
   const r=e.getBoundingClientRect(); if(r.width<40||r.height<40) return;
   const img=e.querySelector('img'); if(!img) return;
   const band=e.closest('.env2-coll-bands__band');
   out.push({i,x:Math.round(r.left+scrollX),y:Math.round(r.top+scrollY),w:Math.round(r.width),h:Math.round(r.height),
     kind:band?band.getAttribute('data-kind'):'',id:band?band.id:'',cls:e.className.split(' ')[1]||e.className.split(' ')[0],
     src:(img.currentSrc||img.src).split('/').pop().split('?')[0].slice(0,20)});});
  return out;});
 for(const bx of boxes){
   await p.evaluate(y=>window.scrollTo({top:y,behavior:'instant'}),Math.max(0,bx.y-100));
   await p.waitForTimeout(150);
   const vy=await p.evaluate(()=>window.scrollY);
   const clip={x:bx.x,y:bx.y-vy,width:Math.min(bx.w,1440-bx.x),height:Math.min(bx.h,900-(bx.y-vy))};
   if(clip.height<40||clip.y<0){continue;}
   await p.screenshot({path:`${OUT}/${key}-${bx.id}-${bx.i}.png`,clip});
 }
 console.log(key,JSON.stringify(boxes.map(b=>[b.id,b.kind,b.cls,b.w+'x'+b.h,b.src])));
 await ctx.close();srv.close();}
await b.close();})();
