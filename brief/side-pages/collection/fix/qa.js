const {chromium,faceCss,serve}=require('/home/user/ElmsNest/brief/side-pages/collection/fix/probe.js');
const KEYS=(process.argv[2]||'coll-decor,coll-path,coll-wall,coll-spot,coll-all').split(',');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){const srv=serve(`/home/user/ElmsNest/brief/inventory/${key}`,'index.html');
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
 const out={};
 for(const [name,vp,rm] of [['d',{width:1440,height:900},'no-preference'],['m',{width:390,height:844},'no-preference'],['rm',{width:390,height:844},'reduce']]){
  const ctx=await b.newContext({viewport:vp,deviceScaleFactor:1,locale:'he-IL',reducedMotion:rm,isMobile:name!=='d',hasTouch:name!=='d'});
  await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
   if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
  const p=await ctx.newPage();await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
  await p.waitForTimeout(1400);
  out[name]=await p.evaluate(()=>{
   const cs=e=>e?getComputedStyle(e):null;
   const q=s=>document.querySelector(s), qa=s=>[...document.querySelectorAll(s)];
   const sub=r=>({w:+r.width.toFixed(1),h:+r.height.toFixed(1)});
   // headings inside our sections
   const hs=qa('[id^=env2-coll] h1,[id^=env2-coll] h2,[id^=env2-coll] h3,[id^=env2-coll] h4').map(e=>+e.tagName[1]);
   const jumps=[];for(let i=1;i<hs.length;i++) if(hs[i]-hs[i-1]>1) jumps.push(hs[i-1]+'->'+hs[i]);
   // pin names
   const pn=qa('.env2-coll-bands__pinname').map(e=>({fs:cs(e).fontSize,w:+e.getBoundingClientRect().width.toFixed(0),
     clipped:e.scrollWidth>e.clientWidth+1||e.scrollHeight>e.clientHeight+1,txt:e.textContent.slice(0,18)}));
   const st=q('.env2-coll-scene__tagname');
   const gc=q('.env2-coll-glyph__cap');
   const grp=q('#env2-coll-ruler [role=group]');
   // sub-13px information text inside our sections
   const small=qa('[id^=env2-coll] *').filter(e=>e.children.length===0&&e.textContent.trim()&&parseFloat(cs(e).fontSize)<13)
     .map(e=>e.className+'@'+cs(e).fontSize);
   const lamps=qa('[id^=env2-coll] [data-lamp]');
   const moving=qa('[id^=env2-coll] *').filter(e=>{const c=cs(e);return parseFloat(c.transitionDuration)>0||c.animationName!=='none'}).length;
   return {
    headings:hs.slice(0,12), jumps,
    h1b:(()=>{const e=q('.env2-coll-scene__h1b');return e?cs(e).display:'none'})(),
    h1lines:(()=>{const e=q('.env2-coll-scene__h1');if(!e)return null;const r=document.createRange();r.selectNodeContents(e);return r.getClientRects().length})(),
    descMax:(()=>{const e=q('.env2-coll-scene__p');return e?cs(e).maxInlineSize||cs(e).maxWidth:null})(),
    descW:(()=>{const e=q('.env2-coll-scene__p');return e?+e.getBoundingClientRect().width.toFixed(0):null})(),
    sceneTag:st?{fs:cs(st).fontSize,ls:cs(st).letterSpacing,tt:cs(st).textTransform}:null,
    pinnames:pn,
    glyphcap:gc?{fs:cs(gc).fontSize,hidden:gc.getAttribute('aria-hidden')}:null,
    groupAria:grp?grp.getAttribute('aria-label'):null,
    eyebrow:(()=>{const e=q('.env2-coll-ruler__eyebrow');return e?e.textContent.trim():null})(),
    rulerH2:(()=>{const e=q('.env2-coll-ruler__h2');return e?e.textContent.trim():null})(),
    numcap:(()=>{const e=q('.env2-coll-ruler__numcap');return e?e.textContent.trim().slice(0,50):null})(),
    rulerLinks:qa('#env2-coll-scene a[href="#env2-coll-ruler"]').length,
    small:small.slice(0,8), nSmall:small.length,
    lamps:lamps.length, notLit:lamps.filter(e=>parseFloat(cs(e).getPropertyValue('--lit')||'1')<1).length,
    moving,
    overflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,
    pageH:document.body.scrollHeight,
    quoteBg:(()=>{const e=q('.env2-coll-bands__quote');return e?cs(e).backgroundColor:null})(),
    ledgerK:(()=>{const e=q('.env2-coll-ledger__k');return e?cs(e).display:null})(),
   };});
  await ctx.close();
 }
 console.log('=== '+key);console.log(JSON.stringify(out,null,0).slice(0,2400));
 srv.close();}
await b.close();})();
