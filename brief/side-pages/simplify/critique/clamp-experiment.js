// Serve the /all mirror and measure docH at 390x844 with the card-title clamp at 2 vs 3 lines (and a 16px variant).
const path=require('path'),fs=require('fs'),http=require('http');
function loadPw(){const roots=[];try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`)}catch(e){}for(const r of roots){try{return require(`${r}/node_modules/playwright`)}catch(e){}}return require('playwright')}
const {chromium}=loadPw();
const MIME={'.html':'text/html','.css':'text/css','.js':'text/javascript','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.woff2':'font/woff2','.woff':'font/woff','.json':'application/json'};
const dir=process.argv[2];
const srv=http.createServer((req,res)=>{let p=decodeURIComponent(req.url.split('?')[0]);if(p==='/')p='/index.html';const f=path.join(dir,p);fs.readFile(f,(e,b)=>{if(e){res.statusCode=404;return res.end()}res.setHeader('content-type',MIME[path.extname(f)]||'application/octet-stream');res.end(b)})});
(async()=>{await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;
const br=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const variants={'square only':'.hdt-ratio--portrait{--ratio-percent:100%!important}','square+clamp3+16px':'.hdt-ratio--portrait{--ratio-percent:100%!important}.hdt-card-product h3 .hdt-card-product__title{--line-clamp-count:3!important;font-size:16px!important}','square+clamp3+17px':'.hdt-ratio--portrait{--ratio-percent:100%!important}.hdt-card-product h3 .hdt-card-product__title{--line-clamp-count:3!important}','clamp2 (now)':'', 'clamp3':'.hdt-card-product h3 .hdt-card-product__title{--line-clamp-count:3!important}', 'clamp3+16px':'.hdt-card-product h3 .hdt-card-product__title{--line-clamp-count:3!important;font-size:16px!important}', 'clamp2+15px':'.hdt-card-product h3 .hdt-card-product__title{font-size:15px!important}'};
for(const [name,css] of Object.entries(variants)){
  const ctx=await br.newContext({viewport:{width:390,height:844},deviceScaleFactor:1,locale:'he-IL'});const page=await ctx.newPage();
  await page.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'load'});await page.waitForTimeout(800);
  if(css)await page.addStyleTag({content:css});await page.waitForTimeout(300);
  const r=await page.evaluate(()=>{const t=[...document.querySelectorAll('.hdt-card-product__title')];const three=t.filter(e=>e.getBoundingClientRect().height>50).length;const ell=t.filter(e=>e.scrollHeight>e.clientHeight+2).length;return {docH:document.documentElement.scrollHeight,titles:t.length,threeLine:three,stillClipped:ell}});
  console.log(name.padEnd(14),'docH',r.docH,'screens',(r.docH/844).toFixed(2),'titles',r.titles,'3-line',r.threeLine,'stillClipped',r.stillClipped);
  await ctx.close();}
await br.close();srv.close();})();
