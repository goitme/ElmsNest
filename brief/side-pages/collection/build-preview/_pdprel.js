const path=require('path'),fs=require('fs'),http=require('http');
function lp(){const r=[];try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))r.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const x of r){try{return require(`${x}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=lp();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
 const root='/home/user/ElmsNest/brief/inventory/pdp-multi';
 const srv=http.createServer((q,s)=>{let p=decodeURIComponent(q.url.split('?')[0]);if(p==='/')p='/index.html';
  const f=path.join(root,p);fs.readFile(f,(e,d)=>{if(e){s.writeHead(404);s.end();return;}
  s.writeHead(200,{'Content-Type':MIME[path.extname(f)]||'application/octet-stream'});s.end(d);});});
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 for(const [vp,w,h] of [['desktop',1440,900],['mobile',390,844]]){
  const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2});
  const page=await ctx.newPage();
  await page.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'load'});
  await page.waitForTimeout(2500);
  const el=await page.$('#env2-pdp-related, [id*="pdp-related"], .env2-pdp-related');
  if(!el){console.log(vp,'related section NOT FOUND');await ctx.close();continue;}
  const bb=await el.boundingBox();
  console.log(vp,'related box',JSON.stringify(bb));
  await el.scrollIntoViewIfNeeded(); await page.waitForTimeout(1200);
  await el.screenshot({path:`${process.argv[2]}-${vp}.png`});
  await ctx.close();
 }
 await b.close();srv.close();
})();
