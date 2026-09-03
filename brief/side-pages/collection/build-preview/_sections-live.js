// Per-section screenshots: a full-page capture is cut off at Chromium's 16384 device-px texture
// limit (CSS 8192 at DPR2), and every collection page is taller than that.
const path=require('path'),fs=require('fs'),http=require('http');
function lp(){const r=[];try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))r.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
for(const x of r){try{return require(`${x}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=lp();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
 const key=process.argv[2], vp=process.argv[3]||'desktop', out=process.argv[4];
 const [w,h]= vp==='mobile'?[390,844]:[1440,900];
 const root=`/home/user/ElmsNest/brief/inventory/${key}`;
 fs.mkdirSync(out,{recursive:true});
 const srv=http.createServer((q,s)=>{let p=decodeURIComponent(q.url.split('?')[0]);if(p==='/')p='/index.html';
  const f=path.join(root,p);fs.readFile(f,(e,d)=>{if(e){s.writeHead(404);s.end();return;}s.writeHead(200,{'Content-Type':MIME[path.extname(f)]||'application/octet-stream'});s.end(d);});});
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:1});const page=await ctx.newPage();
 await page.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'load'});
 await page.evaluate(async()=>{await new Promise(r=>{let y=0;const t=setInterval(()=>{window.scrollTo(0,y);y+=400;if(y>document.body.scrollHeight){clearInterval(t);r();}},18);});});
 await page.waitForTimeout(1800);
 const ids=await page.$$eval('section[id^="env2-coll-"]',es=>es.map(e=>e.id));
 for(const id of ids){
   const el=await page.$('#'+id);
   const bb=await el.boundingBox();
   try{ await el.screenshot({path:`${out}/${key}-${vp}-${id.replace('env2-coll-','')}.png`}); }
   catch(e){ console.log('  (too tall, tiling)',id,bb&&Math.round(bb.height)); }
   console.log(`  ${id} h=${bb?Math.round(bb.height):'?'}`);
 }
 await b.close();srv.close();
})();
