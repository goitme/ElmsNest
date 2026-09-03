const {chromium,faceCss,serve}=require('/home/user/ElmsNest/brief/side-pages/collection/fix/probe.js');
const fs=require('fs');
const KEYS=(process.argv[2]).split(',');const OUT=process.argv[3];
const VPS=(process.argv[4]||'390x844,390x664,320x568').split(',').map(s=>s.split('x').map(Number));
fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){const srv=serve(`/home/user/ElmsNest/brief/inventory/${key}`,'index.html');
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
 for(const [w,h] of VPS){const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2,locale:'he-IL',hasTouch:true,isMobile:true});
  await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
   if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
  const p=await ctx.newPage();await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
  await p.waitForTimeout(2000);
  await p.screenshot({path:`${OUT}/${key}-${w}x${h}.png`});
  await ctx.close();}
 srv.close();}
await b.close();})();
