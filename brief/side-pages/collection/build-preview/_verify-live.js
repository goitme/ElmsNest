// Measures the five deployed collection URLs from their served mirrors.
const path=require('path'),fs=require('fs'),http=require('http');
function loadPlaywright(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}}return require('playwright');}
const {chromium}=loadPlaywright();
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
(async()=>{
 const keys=process.argv.slice(2);
 const browser=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 const out={};
 for(const k of keys){
  const root=`/home/user/ElmsNest/brief/inventory/${k}`;
  const srv=http.createServer((req,res)=>{let p=decodeURIComponent(req.url.split('?')[0]);if(p==='/')p='/index.html';
    const f=path.join(root,p);fs.readFile(f,(e,d)=>{if(e){res.writeHead(404);res.end();return;}
    res.writeHead(200,{'Content-Type':MIME[path.extname(f)]||'application/octet-stream'});res.end(d);});});
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));
  const port=srv.address().port;
  out[k]={};
  for(const [vp,w,h] of [['desktop',1440,900],['mobile',390,844]]){
   const ctx=await browser.newContext({viewport:{width:w,height:h},deviceScaleFactor:1});
   const page=await ctx.newPage();
   await page.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'load'});
   await page.waitForTimeout(1200);
   const m=await page.evaluate(()=>{
    const q=s=>document.querySelector(s);
    const sec=[...document.querySelectorAll('[id^="env2-coll-"]')].map(e=>e.id);
    const card=q('.env2-coll-scene__card');
    const buy=card?card.querySelector('.env2-pdp-card__action .env2-btn, .env2-pdp-card__action a, .env2-pdp-card__action button'):null;
    const price=card?card.querySelector('.env2-pdp-card__price'):null;
    const title=card?card.querySelector('.env2-pdp-card__title'):null;
    const r=e=>e?e.getBoundingClientRect():null;
    const bb=r(buy),pb=r(price),tb=r(title);
    const glyphs=[...document.querySelectorAll('.env2-coll-glyph')].map(g=>{
      const svg=g.querySelector('svg');return (svg&&svg.getAttribute('aria-label'))||g.dataset.glyph;});
    const caps=[...document.querySelectorAll('*')].filter(e=>e.children.length===0&&e.textContent.trim()).map(e=>parseFloat(getComputedStyle(e).fontSize)).filter(x=>x&&x<13);
    const taps=[...document.querySelectorAll('a[href],button,label.env2-coll-ruler__pill')].map(e=>{const b=e.getBoundingClientRect();return {t:(e.textContent||'').trim().slice(0,24),h:Math.round(b.height),w:Math.round(b.width)};}).filter(x=>x.h>0&&x.h<44&&x.w>0);
    const btnColors=[...document.querySelectorAll('a.env2-btn')].map(a=>getComputedStyle(a).color+' on '+getComputedStyle(a).backgroundColor);
    return {sections:sec, docH:document.documentElement.scrollHeight,
      hOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,
      buy: bb?{label:(buy.textContent||'').trim(),bottom:Math.round(bb.bottom),h:Math.round(bb.height),tag:buy.tagName}:null,
      priceTxt: price?price.textContent.trim().replace(/\s+/g,' '):null,
      priceBottom: pb?Math.round(pb.bottom):null,
      titleTxt: title?title.textContent.trim().replace(/\s+/g,' ').slice(0,60):null,
      glyphs, smallFonts:[...new Set(caps)].sort(), badTaps:taps.slice(0,8), btnColors:[...new Set(btnColors)],
      pills:[...document.querySelectorAll('.env2-coll-ruler__pill')].map(p=>p.textContent.trim()),
      rulerH2: q('.env2-coll-ruler__h2')?q('.env2-coll-ruler__h2').textContent.trim():null,
      counts: q('.env2-coll-scene__counts')?q('.env2-coll-scene__counts').textContent.trim().replace(/\s+/g,' '):null};
   });
   out[k][vp]=m; await ctx.close();
  }
  srv.close();
 }
 await browser.close();
 fs.writeFileSync('/home/user/ElmsNest/brief/side-pages/collection/build-preview/_verify-live.json',JSON.stringify(out,null,1));
 for(const k of Object.keys(out)){const d=out[k].desktop,m=out[k].mobile;
  console.log(`\n### ${k}`);
  console.log(' sections:',d.sections.join(' '));
  console.log(' counts  :',d.counts);
  console.log(' rulerH2 :',d.rulerH2);
  console.log(' pills   :',JSON.stringify(d.pills));
  console.log(` desktop : h=${d.docH} hOverflow=${d.hOverflow} card="${d.titleTxt}" price="${d.priceTxt}" buy=${d.buy?d.buy.tag+' "'+d.buy.label+'" bottom='+d.buy.bottom+' h='+d.buy.h:'NONE'}`);
  console.log(` mobile  : h=${m.docH} hOverflow=${m.hOverflow} buyBottom=${m.buy?m.buy.bottom:'NONE'} priceBottom=${m.priceBottom} buyH=${m.buy?m.buy.h:''}`);
  console.log(' glyphs  :',d.glyphs.length, JSON.stringify(d.glyphs.slice(0,20)));
  console.log(' <13px   :',JSON.stringify(d.smallFonts),'| mobile',JSON.stringify(m.smallFonts));
  console.log(' taps<44 :',JSON.stringify(m.badTaps));
  console.log(' a.env2-btn colours:',JSON.stringify(d.btnColors));
 }
})();
