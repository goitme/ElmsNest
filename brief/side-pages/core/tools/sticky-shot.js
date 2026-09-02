// V-3: re-shoot the PDP sticky add-to-cart bar from the CURRENT mirror (the old PNGs predated the deploy).
// Usage: node sticky-shot.js <mirror-dir> <out-dir> <prefix>
const path=require('path'),fs=require('fs'),http=require('http');
function pw(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}} return require('playwright');}
const {chromium}=pw();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
const [,,dir,outDir,prefix]=process.argv;
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
 await p.waitForTimeout(1500);
 await p.evaluate(async()=>{document.querySelectorAll('img[loading="lazy"]').forEach(i=>i.loading='eager');
   for(let y=0;y<3000;y+=400){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,70));}
   window.scrollTo({top:2600,behavior:'instant'});});
 await p.evaluate(()=>{const e=document.querySelector('.hdt-sticky-btn-atc');if(e){document.body.classList.add('sticky-shown');e.style.setProperty('transform','translateZ(0)','important');}});
 await p.waitForTimeout(1500);
 const info=await p.evaluate(()=>{
  const el=document.querySelector('.hdt-sticky-btn-atc'); if(!el)return null;
  const cs=e=>getComputedStyle(e),R=e=>e.getBoundingClientRect();
  const r=R(el);
  const one=s=>{const e=el.querySelector(s);if(!e)return null;const q=R(e);
   return {sel:s,text:(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,26),color:cs(e).color,bg:cs(e).backgroundColor,w:Math.round(q.width),h:Math.round(q.height)};};
  return {bg:cs(el).backgroundColor,color:cs(el).color,vis:cs(el).visibility,op:cs(el).opacity,
   rect:{x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)},
   parts:[one('.hdt-sticky-atc__submit'),one('.hdt-sticky-atc__product-infos'),one('.hdt-sticky-atc__qty-selector'),one('.hdt-sticky-atc__infos')].filter(Boolean)};
 });
 const clip = info && info.rect.h>0 ? {x:0,y:Math.max(0,info.rect.y),width:vp.width,height:Math.min(vp.height-Math.max(0,info.rect.y),info.rect.h+8)} : null;
 await p.screenshot({path:path.join(outDir,`${prefix}-${name}.png`),clip:clip||undefined,fullPage:false});
 out[name]={info};
 await ctx.close();
}
await b.close();srv.close();
console.log(JSON.stringify(out,null,1));
})();
