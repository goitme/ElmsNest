const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of ['coll-decor','coll-all']){
  const {p,ctx,srv}=await open(b,key,{width:1440,height:900});
  const m=await p.evaluate(()=>{
   const q=s=>document.querySelector(s),qa=s=>[...document.querySelectorAll(s)],cs=e=>getComputedStyle(e);
   const styleTags=qa('style[id]').map(e=>e.id);
   const gc=q('#env2-ground-collection');
   // which sheet actually wins body background-image
   let winners=[];
   for(const sh of document.styleSheets){let rules;try{rules=sh.cssRules}catch(e){continue}
     if(!rules)continue;
     for(const r of rules){ if(!r.selectorText)continue;
       if(/hdt-page-type/.test(r.selectorText)&&/background-image/.test(r.style&&r.style.cssText||'')){
         winners.push({owner:(sh.ownerNode&&sh.ownerNode.id)||'ext', sel:r.selectorText.slice(0,90), css:r.style.cssText.slice(0,120)});}}}
   return {
    styleTags, groundPresent: !!gc, groundLen: gc?gc.textContent.length:0,
    bodyClass: document.body.className,
    bodyBI: cs(document.body).backgroundImage, bodyBS: cs(document.body).backgroundSize,
    bodyOverflowX: cs(document.body).overflowX, htmlOverflowX: cs(document.documentElement).overflowX,
    btnSm:(()=>{const e=q('.env2-btn--sm');return e?cs(e).minBlockSize:null})(),
    priceFrom:(()=>{const e=q('.env2-price__from');return e?cs(e).fontSize:null})(),
    wrapperBg:(()=>{const e=q('#MainContent')||q('.hdt-main-content');return e?cs(e).backgroundColor:null})(),
    spanPad:(()=>{const e=q('[class*=env2-coll-span]');return e?{cls:e.className,pt:cs(e).paddingBlockStart,pb:cs(e).paddingBlockEnd}:null})(),
    sectionPads: qa('[id^=env2-coll]').map(e=>({id:e.id,pt:cs(e).paddingBlockStart,pb:cs(e).paddingBlockEnd})),
    winners,
   };
  });
  console.log('=== '+key); console.log(JSON.stringify(m,null,1));
  await ctx.close(); srv.close();
}
await b.close();})();
