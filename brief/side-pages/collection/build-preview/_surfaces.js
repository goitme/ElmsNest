const path=require('path'),fs=require('fs'),http=require('http');
function lp(){const r=[];try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))r.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const x of r){try{return require(`${x}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=lp();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 for(const k of process.argv.slice(2)){
  const root=`/home/user/ElmsNest/brief/inventory/${k}`;
  const srv=http.createServer((q,s)=>{let p=decodeURIComponent(q.url.split('?')[0]);if(p==='/')p='/index.html';
   const f=path.join(root,p);fs.readFile(f,(e,d)=>{if(e){s.writeHead(404);s.end();return;}
   s.writeHead(200,{'Content-Type':MIME[path.extname(f)]||'application/octet-stream'});s.end(d);});});
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;
  const ctx=await b.newContext({viewport:{width:1440,height:900}});
  const page=await ctx.newPage();
  await page.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'load'});
  await page.waitForTimeout(1200);
  const out=await page.evaluate(()=>{
   const bad=[];
   for(const s of document.querySelectorAll('section[id^="env2-coll-"]'))
    for(const e of s.querySelectorAll('*')){
     const cs=getComputedStyle(e), bg=cs.backgroundColor;
     const m=bg.match(/rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)/); if(!m) continue;
     const [r,g,bl]=[+m[1],+m[2],+m[3]], al=m[4]===undefined?1:+m[4];
     if(al<0.5) continue;
     const L=(Math.max(r,g,bl)+Math.min(r,g,bl))/2;
     if(L>140 && r>=g && g>=bl && (r-bl)>8){
       const bx=e.getBoundingClientRect();
       if(bx.width*bx.height>2000) bad.push({sec:s.id,cls:e.className.toString().slice(0,44),bg,area:Math.round(bx.width*bx.height)});
     }
    }
   const seen=new Set(),o=[];for(const x of bad){const k=x.sec+x.cls+x.bg;if(!seen.has(k)){seen.add(k);o.push(x);}}
   return o;
  });
  console.log(k, 'warm-light surfaces >2000px2:', out.length);
  out.slice(0,10).forEach(x=>console.log('   ',x.sec,x.bg,x.area,x.cls));
  await ctx.close(); srv.close();
 }
 await b.close();
})();
