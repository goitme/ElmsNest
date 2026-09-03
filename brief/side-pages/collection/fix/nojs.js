// QA suite 3: JS-off vs JS-on, reduced motion, three scroll depths, 390x844.
const {chromium,faceCss,serve}=require('/home/user/ElmsNest/brief/side-pages/collection/fix/probe.js');
const fs=require('fs');const OUT='/tmp/nojs';fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
const key=process.argv[2]||'coll-decor';
const srv=serve(`/home/user/ElmsNest/brief/inventory/${key}`,'index.html');
await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
for(const js of [true,false]){
 const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1,locale:'he-IL',
   javaScriptEnabled:js,reducedMotion:'reduce',isMobile:true,hasTouch:true});
 await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
  if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
 const p=await ctx.newPage();await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
 await p.waitForTimeout(2200);
 for(const [i,y] of [[0,0],[1,900],[2,2200]]){
   await p.evaluate(v=>window.scrollTo(0,v),y);await p.waitForTimeout(600);
   await p.screenshot({path:`${OUT}/${key}-${js?'on':'off'}-${i}.png`});
 }
 if(!js){const st=await p.evaluate(()=>({prices:document.querySelectorAll('[id^=env2-coll] .env2-price').length,
   empty:[...document.querySelectorAll('[id^=env2-coll] .env2-price')].filter(e=>!e.textContent.trim()).length,
   forms:document.querySelectorAll('[id^=env2-coll] form[action*="/cart/add"]').length,
   radios:document.querySelectorAll('#env2-coll-ruler input[type=radio]').length,
   sorts:document.querySelectorAll('#env2-coll-ruler a[href*="sort_by"]').length,
   overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth}));
  console.log('JS-OFF',key,JSON.stringify(st));}
 await ctx.close();}
srv.close();await b.close();})();
