// full-page render at deviceScaleFactor 1 (beats Chromium's 16384 device-px ceiling) + ink density.
const {chromium,faceCss,serve}=require('/home/user/ElmsNest/brief/side-pages/collection/fix/probe.js');
const fs=require('fs');
const KEYS=(process.argv[2]||'coll-decor,coll-path,coll-wall,coll-spot,coll-all').split(',');
const OUT=process.argv[3]||'/home/user/ElmsNest/brief/side-pages/collection/fix/shots';
const W=+(process.argv[4]||1440), H=+(process.argv[5]||900);
fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){const root=`/home/user/ElmsNest/brief/inventory/${key}`;const srv=serve(root,'index.html');
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
 const ctx=await b.newContext({viewport:{width:W,height:H},deviceScaleFactor:1,locale:'he-IL'});
 await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
  if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(String(e).slice(0,80)));
 await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
 await p.waitForTimeout(1200);
 await p.evaluate(async()=>{document.querySelectorAll('img[loading="lazy"]').forEach(i=>i.loading='eager');
  document.documentElement.style.scrollBehavior='auto';
  for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,60));}
  window.scrollTo({top:0,behavior:'instant'});});
 await p.waitForTimeout(2500);
 const h=await p.evaluate(()=>document.body.scrollHeight);
 await p.screenshot({path:`${OUT}/${key}-${W}.png`,fullPage:true});
 console.log(key,'h='+h,'errs='+errs.length);
 await ctx.close();srv.close();}
await b.close();})();
