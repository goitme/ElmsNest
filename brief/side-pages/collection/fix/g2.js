const {chromium,faceCss,serve}=require('/home/user/ElmsNest/brief/side-pages/collection/fix/probe.js');
const KEYS=(process.argv[2]||'coll-decor,coll-path,coll-wall,coll-spot,coll-all').split(',');
const VPS=[[390,844],[390,664],[360,640],[320,568]];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){const root=`/home/user/ElmsNest/brief/inventory/${key}`;const srv=serve(root,'index.html');
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
 for(const [w,h] of VPS){const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:1,locale:'he-IL',hasTouch:true,isMobile:true});
  await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
   if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
  const p=await ctx.newPage();await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:60000});
  await p.waitForTimeout(1200);
  const m=await p.evaluate(()=>{const R=s=>{const e=document.querySelector(s);if(!e)return null;const r=e.getBoundingClientRect();return {t:+r.top.toFixed(1),b:+r.bottom.toFixed(1),h:+r.height.toFixed(1)};};
   const ty=R('.env2-coll-scene__type'),md=R('.env2-coll-scene__media'),eb=R('#env2-coll-scene .env2-eyebrow'),
    nl=R('.env2-coll-scene__narrow'),cd=R('.env2-coll-scene__card'),tag=R('.env2-coll-scene__tag'),dot=R('.env2-coll-scene__dot');
   const cs=getComputedStyle(document.querySelector('.env2-coll-scene__type'));
   return {mediaH:md&&md.h,typeT:ty&&ty.t,typeH:ty&&ty.h,padT:cs.paddingBlockStart,minB:cs.minBlockSize,
     ebT:eb&&eb.t,contentH:(eb&&nl)?+(nl.b-eb.t).toFixed(1):null,cardT:cd&&cd.t,cardH:cd&&cd.h,
     tagT:tag&&tag.t,tagH:tag&&tag.h,dotT:dot&&dot.t};});
  console.log(key,`${w}x${h}`,JSON.stringify(m));
  await ctx.close();}
 srv.close();}
await b.close();})();
