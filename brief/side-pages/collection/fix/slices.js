// viewport-by-viewport capture (no 16384 ceiling) + per-screen ink density, at 1440x900.
const {chromium,faceCss,serve}=require('/home/user/ElmsNest/brief/side-pages/collection/fix/probe.js');
const fs=require('fs');
const KEYS=(process.argv[2]||'coll-decor,coll-path,coll-wall,coll-spot,coll-all').split(',');
const OUT=process.argv[3];const W=+(process.argv[4]||1440),H=+(process.argv[5]||900);
const SRC=process.argv[6]||'/home/user/ElmsNest/brief/inventory';
fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){const root=`${SRC}/${key}`;const srv=serve(root,'index.html');
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
 const ctx=await b.newContext({viewport:{width:W,height:H},deviceScaleFactor:1,locale:'he-IL',isMobile:W<900,hasTouch:W<900});
 await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
  if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
 const p=await ctx.newPage();await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
 await p.waitForTimeout(1200);
 await p.evaluate(async()=>{document.querySelectorAll('img[loading="lazy"]').forEach(i=>i.loading='eager');
  document.documentElement.style.scrollBehavior='auto';
  for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,60));}});
 await p.waitForTimeout(2000);
 const h=await p.evaluate(()=>document.body.scrollHeight);
 const n=Math.ceil(h/H);
 for(let i=0;i<n;i++){await p.evaluate(y=>window.scrollTo({top:y,behavior:'instant'}),i*H);await p.waitForTimeout(220);
  await p.screenshot({path:`${OUT}/${key}-${String(i+1).padStart(2,'0')}.png`});}
 console.log(key,'h='+h,'slices='+n);
 await ctx.close();srv.close();}
await b.close();})();
