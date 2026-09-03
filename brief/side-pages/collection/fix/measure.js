// QA-01 + fold measurement harness. Serves a mirror over http and measures the scene at 4 phone sizes.
// usage: node measure.js <key1,key2,...> [--out file.json]
const path=require('path'), fs=require('fs'), http=require('http');
function loadPlaywright(){const roots=[process.env.ENV2_PW_ROOT].filter(Boolean);
 try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}} return require('playwright');}
const {chromium}=loadPlaywright();
const FONT_DIR='/home/user/ElmsNest/brief/assets/fonts';
const FF={FrankRuhlLibre:'Frank Ruhl Libre',Heebo:'Heebo'};
const FR={hebrew:'U+0590-05FF,U+200C-2010,U+20AA,U+25CC,U+FB1D-FB4F',latin:'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215'};
function faceCss(port){let css='';let files=[];try{files=fs.readdirSync(FONT_DIR);}catch(e){return '';}
 for(const f of files){const m=/^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f);if(!m)continue;
 css+=`@font-face{font-family:"${FF[m[1]]}";font-style:normal;font-weight:${m[3]};font-display:block;src:url(http://127.0.0.1:${port}/__fonts/${f}) format("woff2");unicode-range:${FR[m[2]]}}\n`;}return css;}
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
function serve(root,file){const srv=http.createServer((req,res)=>{const p=decodeURIComponent(req.url.split('?')[0]);
 if(p.startsWith('/__fonts/')){const g=path.join(FONT_DIR,path.basename(p));if(fs.existsSync(g)){res.writeHead(200,{'Content-Type':'font/woff2','Access-Control-Allow-Origin':'*'});return fs.createReadStream(g).pipe(res);}res.writeHead(404);return res.end();}
 let f=path.join(root,p==='/'?file:p);let g=f;
 if(!g.startsWith(root)||!fs.existsSync(g)||fs.statSync(g).isDirectory()){const base=path.basename(g);g=null;
  for(const dir of ['/home/user/ElmsNest/brief/inventory','/home/user/ElmsNest/brief/build-preview']){try{for(const sub of fs.readdirSync(dir)){const c=path.join(dir,sub,'a',base);if(fs.existsSync(c)&&fs.statSync(c).size>0){g=c;break;}}}catch(e){}if(g)break;}
  if(!g){res.writeHead(404);return res.end();}}
 f=g;res.writeHead(200,{'Content-Type':MIME[path.extname(f).toLowerCase()]||'application/octet-stream','Access-Control-Allow-Origin':'*'});
 if(f===path.join(root,file)){return res.end(fs.readFileSync(f,'utf8').replace(/(["'])a\//g,'$1/a/'));}
 fs.createReadStream(f).pipe(res);});return srv;}
const VPS=[[390,844],[390,664],[360,640],[320,568]];
const KEYS=(process.argv[2]||'coll-decor,coll-path,coll-wall,coll-spot,coll-all').split(',');
const OUT=process.argv.includes('--out')?process.argv[process.argv.indexOf('--out')+1]:null;
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
 const all={};
 for(const key of KEYS){
  const root=`/home/user/ElmsNest/brief/inventory/${key}`;const srv=serve(root,'index.html');
  await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
  all[key]={};
  for(const [w,h] of VPS){
   const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:1,locale:'he-IL',hasTouch:true,isMobile:true});
   await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
    if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
   const p=await ctx.newPage();
   await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
   await p.waitForTimeout(1500);
   const m=await p.evaluate(()=>{
    const R=s=>{const e=document.querySelector(s);if(!e)return null;const r=e.getBoundingClientRect();
      return {t:+r.top.toFixed(1),b:+r.bottom.toFixed(1),l:+r.left.toFixed(1),r:+r.right.toFixed(1),w:+r.width.toFixed(1),h:+r.height.toFixed(1)};};
    const tag=R('#env2-coll-scene .env2-coll-scene__tag');
    const h1=R('#env2-coll-scene .env2-coll-scene__h1');
    const eb=R('#env2-coll-scene .env2-eyebrow');
    const nl=R('.env2-coll-scene__narrowlink');
    const ov=(a,x)=>!!(a&&x)&&a.t<x.b&&a.b>x.t;
    // buy control: first button/anchor inside the scene card
    let buy=null;const card=document.querySelector('#env2-coll-scene .env2-coll-scene__card');
    if(card){const el=card.querySelector('.env2-btn');if(el){const r=el.getBoundingClientRect();buy={t:+r.top.toFixed(1),b:+r.bottom.toFixed(1)};}}
    const ruler=document.querySelector('#env2-coll-ruler');
    const rt=ruler?+(ruler.getBoundingClientRect().top+window.scrollY).toFixed(1):null;
    return {tag,h1,eb,nl,buy,tagOverH1:ov(tag,h1),tagOverEyebrow:ov(tag,eb),
      gap:(tag&&h1)?+(h1.t-tag.b).toFixed(1):null,
      gapEb:(tag&&eb)?+(eb.t-tag.b).toFixed(1):null,
      narrowInFold:nl?nl.b<=window.innerHeight:null,
      buyInFold:buy?buy.b<=window.innerHeight:null,
      rulerTop:rt,
      overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,
      pageH:document.body.scrollHeight,
      h1lines:(()=>{const e=document.querySelector('#env2-coll-scene .env2-coll-scene__h1');if(!e)return null;
        const r=document.createRange();r.selectNodeContents(e);return r.getClientRects().length;})(),
      h1b:(()=>{const e=document.querySelector('.env2-coll-scene__h1b');return e?getComputedStyle(e).display:'none'})()};
   });
   all[key][`${w}x${h}`]=m;
   await ctx.close();
  }
  srv.close();
  const d=all[key];
  console.log(key.padEnd(10),VPS.map(([w,h])=>{const m=d[`${w}x${h}`];
   return `${w}x${h}: gap=${m.gap} eb=${m.gapEb} overH1=${m.tagOverH1?'YES':'no'} overEb=${m.tagOverEyebrow?'YES':'no'} buy=${m.buy?m.buy.b:'-'}/${m.buyInFold} nl=${m.nl?m.nl.t+'+'+m.nl.h:'-'}/${m.narrowInFold} ovf=${m.overflow}`;}).join('\n           '));
 }
 if(OUT)fs.writeFileSync(OUT,JSON.stringify(all,null,1));
 await b.close();
})();
