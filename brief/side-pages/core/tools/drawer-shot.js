// Round-0 fix pass, R0-03: open the Kalles cart drawer on a mirror whose cart cookie carried real lines,
// so the line-item row, qty stepper, subtotal and checkout button are actually rendered, then measure+shoot.
// Usage: node drawer-shot.js <mirror-dir> <out-dir> <prefix>
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
 await ctx.route(/\/cart\/(add|update|change|clear)(\.js)?/,r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({items:[],item_count:3,total_price:42970,currency:'ILS'})}));
 await ctx.route(/\/cart\.js/,r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({items:[],item_count:3,total_price:42970,currency:'ILS',sections:{}})}));
 await ctx.route(/^https?:\/\//,r=>/^https?:\/\/127\.0\.0\.1:/.test(r.request().url())?r.continue():r.abort());
 const p=await ctx.newPage();const errors=[];p.on('pageerror',e=>errors.push(String(e).slice(0,120)));
 await p.goto(`http://127.0.0.1:${port}/${file}`,{waitUntil:'load',timeout:60000});
 await p.waitForTimeout(2500);
 let how='click';
 const btn=await p.$('form[action="/cart/add"] [type="submit"], form[action="/cart/add"] button');
 if(btn){try{await btn.click({timeout:4000});}catch(e){how='click-failed';}} else how='no-add-form';
 await p.waitForTimeout(2500);
 let open=await p.evaluate(()=>{const d=document.getElementById('CartDrawer');return !!(d&&d.open);});
 if(!open){how+='+showModal';await p.evaluate(()=>{const d=document.getElementById('CartDrawer');if(d&&!d.open){try{d.showModal();}catch(e){d.setAttribute('open','');}}});await p.waitForTimeout(1200);
   open=await p.evaluate(()=>{const d=document.getElementById('CartDrawer');return !!(d&&d.open);});}
 await p.waitForTimeout(1200);
 const info=await p.evaluate(()=>{
  const d=document.getElementById('CartDrawer'); if(!d)return null;
  const cs=e=>getComputedStyle(e),R=e=>e.getBoundingClientRect();
  const one=(sel)=>{const e=d.querySelector(sel); if(!e)return null; const r=R(e);
    return {sel,text:(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,34),color:cs(e).color,bg:cs(e).backgroundColor,
      border:cs(e).borderColor,w:Math.round(r.width),h:Math.round(r.height)};};
  const c=cs(d),r=R(d);
  return {open:d.open,scheme:d.getAttribute('color-scheme'),bg:c.backgroundColor,color:c.color,
   rect:{x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)},
   lineCount:d.querySelectorAll('.hdt-mini-cart__item').length,
   parts:[one('.hdt-mini-cart__header-title'),one('.hdt-mini-cart__item'),one('.hdt-mini-cart__title'),
     one('.hdt-mini-cart__meta-variant'),one('.hdt-mini-cart__price'),one('.hdt-mini-cart__quantity'),
     one('.hdt-quantity input'),one('.hdt-mini-cart__remove'),one('.hdt-mini-cart__total'),
     one('.hdt-mini-cart__btn-viewcart'),one('.hdt-mini-cart__btn-checkout'),
     one('.hdt-cart-discount input'),one('.hdt-cart-discount')].filter(Boolean)};
 });
 await p.screenshot({path:path.join(outDir,`${prefix}-${name}.png`),fullPage:false});
 out[name]={how,open,errors:errors.slice(0,3),info};
 await ctx.close();
}
await b.close();srv.close();
console.log(JSON.stringify(out,null,1));
})();
