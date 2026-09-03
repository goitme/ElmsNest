const path=require('path'),fs=require('fs'),http=require('http');
function loadPlaywright(){const roots=[];
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=loadPlaywright();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
 const browser=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 for(const k of process.argv.slice(2)){
  const root=`/home/user/ElmsNest/brief/inventory/${k}`;
  const srv=http.createServer((req,res)=>{let p=decodeURIComponent(req.url.split('?')[0]);if(p==='/')p='/index.html';
    const f=path.join(root,p);fs.readFile(f,(e,d)=>{if(e){res.writeHead(404);res.end();return;}
    res.writeHead(200,{'Content-Type':MIME[path.extname(f)]||'application/octet-stream'});res.end(d);});});
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const port=srv.address().port;
  for(const [vp,w,h] of [['desktop',1440,900],['mobile',390,844]]){
   const ctx=await browser.newContext({viewport:{width:w,height:h},deviceScaleFactor:1});
   const page=await ctx.newPage();
   await page.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'load'});
   await page.waitForTimeout(1200);
   const m=await page.evaluate(()=>{
    const secs=[...document.querySelectorAll('section[id^="env2-coll-"]')];
    const bad=[];
    for(const s of secs) for(const e of s.querySelectorAll('a[href],button,label')){
      const b=e.getBoundingClientRect(); if(b.height>0&&b.width>0&&b.height<44)
        bad.push({sec:s.id,t:(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,26),h:Math.round(b.height),cls:e.className.toString().slice(0,40)});
    }
    const seen=new Set(),out=[];
    for(const x of bad){const k=x.sec+'|'+x.cls+'|'+x.h;if(!seen.has(k)){seen.add(k);out.push(x);}}
    return {n:bad.length,uniq:out.slice(0,12),docH:document.documentElement.scrollHeight,
      hOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,
      secs:secs.map(s=>s.id)};
   });
   console.log(k,vp,'badTaps',m.n,'docH',m.docH,'ovf',m.hOverflow);
   console.log('  secs:',m.secs.join(' '));
   for(const x of m.uniq) console.log('   ',x.sec,x.h+'px','"'+x.t+'"',x.cls);
   await ctx.close();
  }
  srv.close();
 }
 await browser.close();
})();
