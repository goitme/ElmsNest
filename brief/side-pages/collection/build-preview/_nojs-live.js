// No-JS narrowing proof on the DEPLOYED render (mirror served over http, javaScriptEnabled:false).
const path=require('path'),fs=require('fs'),http=require('http');
function lp(){const r=[];try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))r.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const x of r){try{return require(`${x}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=lp();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
 const [,,key,stopId,outPng]=process.argv;
 const root=`/home/user/ElmsNest/brief/inventory/${key}`;
 const srv=http.createServer((q,s)=>{let p=decodeURIComponent(q.url.split('?')[0]);if(p==='/')p='/index.html';
  const f=path.join(root,p);fs.readFile(f,(e,d)=>{if(e){s.writeHead(404);s.end();return;}
  s.writeHead(200,{'Content-Type':MIME[path.extname(f)]||'application/octet-stream'});s.end(d);});});
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 const ctx=await b.newContext({viewport:{width:1440,height:1000},javaScriptEnabled:false});
 const page=await ctx.newPage();
 await page.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'load'});
 await page.waitForTimeout(600);
 // page.evaluate still works in an isolated world, so the honest probe is whether the PAGE's own
 // scripts ran: elmsnest-v2-core adds html.env2-js from an inline script on first paint.
 const cls=await page.evaluate(()=>document.documentElement.className);
 console.log('javaScriptEnabled:false -> html class =', JSON.stringify(cls),
   cls.includes('env2-js')?'  *** PAGE SCRIPTS RAN (bad) ***':'  (no env2-js: the page ran no script)');
 // click the label, not the input: this is exactly what a visitor does
 const lab=page.locator(`label[for="env2-stop-${stopId}"]`);
 console.log('label count:', await lab.count(), 'text:', (await lab.first().textContent()||'').trim());
 await lab.first().click();
 await page.waitForTimeout(500);
 const rows=await page.$$eval('.env2-coll-ruler__row',(els,sid)=>els.map(r=>{
   const t=r.querySelector('.env2-coll-ruler__title');
   const vis=[...r.querySelectorAll('.env2-coll-rail__v')].filter(v=>getComputedStyle(v).display!=='none');
   return {title:(t?t.textContent:'').trim().replace(/\s+/g,' ').slice(0,44),
     opacity:getComputedStyle(r).opacity,
     shown:vis.map(v=>({stop:v.dataset.stop,state:v.dataset.state,txt:v.textContent.trim().replace(/\s+/g,' ')}))};
 }),stopId);
 rows.forEach(r=>console.log(` ${r.opacity.padEnd(5)} ${r.title}\n        ${JSON.stringify(r.shown)}`));
 const cur=await page.$eval('.env2-coll-ruler__cursor',e=>getComputedStyle(e).insetInlineStart||getComputedStyle(e).left).catch(()=>'?');
 const pill=await page.$eval(`label[for="env2-stop-${stopId}"]`,e=>getComputedStyle(e).backgroundColor);
 console.log('cursor inset-inline-start:',cur,' chosen pill bg:',pill);
 const sec=await page.$('#env2-coll-ruler');
 if(outPng) await sec.screenshot({path:outPng});
 await b.close();srv.close();
})();
