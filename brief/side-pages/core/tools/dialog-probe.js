// Open named dialogs on a mirrored page and report computed colours + screenshots.
// Usage: node dialog-probe.js <mirror-dir> <out-dir> <id1,id2,...>
const path=require('path'),fs=require('fs'),http=require('http');
function pw(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}} return require('playwright');}
const {chromium}=pw();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
const [,,dir,outDir,idsArg]=process.argv;
const ids=idsArg.split(',');
const root=path.resolve(dir),file='index.html';
const srv=http.createServer((req,res)=>{const p=decodeURIComponent(req.url.split('?')[0]);let g=path.join(root,p==='/'?file:p);
 if(!g.startsWith(root)||!fs.existsSync(g)||fs.statSync(g).isDirectory()){const base=path.basename(g);g=null;
  for(const d2 of ['/home/user/ElmsNest/brief/inventory','/home/user/ElmsNest/brief/build-preview']){
   try{for(const sub of fs.readdirSync(d2)){const c=path.join(d2,sub,'a',base);if(fs.existsSync(c)&&fs.statSync(c).size>0){g=c;break;}}}catch(e){} if(g)break;}
  if(!g){res.writeHead(404);return res.end();}}
 res.writeHead(200,{'Content-Type':MIME[path.extname(g).toLowerCase()]||'application/octet-stream','Access-Control-Allow-Origin':'*'});
 if(g===path.join(root,file))return res.end(fs.readFileSync(g,'utf8').replace(/(["'])a\//g,'$1/a/'));
 fs.createReadStream(g).pipe(res);});
await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
fs.mkdirSync(outDir,{recursive:true});
const out={};
for(const [name,vp] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}]]){
 const ctx=await b.newContext({viewport:vp,deviceScaleFactor:2,locale:'he-IL',hasTouch:name==='mobile',isMobile:name==='mobile'});
 await ctx.route(/^https?:\/\//,r=>/^https?:\/\/127\.0\.0\.1:/.test(r.request().url())?r.continue():r.abort());
 const p=await ctx.newPage();
 await p.goto(`http://127.0.0.1:${port}/${file}`,{waitUntil:'load',timeout:60000});
 await p.waitForTimeout(2200);
 for(const id of ids){
  const info=await p.evaluate((id)=>{
   const d=document.getElementById(id); if(!d) return {missing:true};
   document.querySelectorAll('dialog[open]').forEach(x=>{if(x.id!==id){try{x.close()}catch(e){x.removeAttribute('open')}}});
   if(!d.open){try{d.showModal()}catch(e){try{d.show()}catch(e2){d.setAttribute('open','')}}}
   const cs=e=>getComputedStyle(e), R=e=>e.getBoundingClientRect();
   const c=cs(d), r=R(d);
   const texts=[...d.querySelectorAll('h1,h2,h3,h4,label,legend,select,option,.hdt-mini-cart__title,button,a')]
     .filter(e=>e.textContent.trim().length>0&&R(e).width>0)
     .slice(0,14)
     .map(e=>({t:e.textContent.trim().slice(0,26),tag:e.tagName.toLowerCase(),cls:String(e.className).slice(0,40),color:cs(e).color,bg:cs(e).backgroundColor}));
   return {open:d.open,scheme:d.getAttribute('color-scheme')||(d.closest('[color-scheme]')&&d.closest('[color-scheme]').getAttribute('color-scheme')),
     bg:c.backgroundColor,color:c.color,rect:{x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)},texts};
  },id);
  out[`${id}-${name}`]=info;
  if(!info.missing){await p.waitForTimeout(500);await p.screenshot({path:path.join(outDir,`dlg-${id}-${name}.png`),fullPage:false});}
  await p.evaluate((id)=>{const d=document.getElementById(id);if(d&&d.open){try{d.close()}catch(e){d.removeAttribute('open')}}},id);
 }
 await ctx.close();
}
await b.close();srv.close();
console.log(JSON.stringify(out,null,1));
})();
