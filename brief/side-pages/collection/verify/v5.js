const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
const KEYS=['coll-decor','coll-path','coll-wall','coll-spot','coll-all'];
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
console.log('### QA-04 focus ring + reduced motion');
for(const key of KEYS){
  // focus ring @1440
  {const {p,ctx,srv}=await open(b,key,{width:1440,height:900});
  const r=await p.evaluate(()=>{
   const q=s=>document.querySelector(s),qa=s=>[...document.querySelectorAll(s)],cs=e=>getComputedStyle(e);
   const out={};
   const sp=q('.env2-coll-scene__pin'); const bp=q('.env2-coll-bands__pin');
   for(const [n,anchor,tagSel] of [['scene',sp,'.env2-coll-scene__tag'],['band',bp,'.env2-coll-bands__pintag']]){
     if(!anchor){out[n]=null;continue}
     const tag=anchor.querySelector(tagSel)||anchor.querySelector('[class*=tag]');
     const before=tag?cs(tag).outline:null;
     anchor.focus();
     out[n]={anchorRect:(()=>{const r=anchor.getBoundingClientRect();return{w:+r.width.toFixed(1),h:+r.height.toFixed(1)}})(),
       anchorOutline:cs(anchor).outline,
       tagSel:tag?tag.className:null,
       tagRect:tag?(()=>{const r=tag.getBoundingClientRect();return{w:+r.width.toFixed(1),h:+r.height.toFixed(1)}})():null,
       tagOutlineBefore:before, tagOutlineFocused:tag?cs(tag).outline:null, tagOffset:tag?cs(tag).outlineOffset:null,
       isFocused:document.activeElement===anchor};
     anchor.blur();
   }
   return out;});
  console.log(key,'focus',JSON.stringify(r));
  await ctx.close(); srv.close();}
  // reduced motion vs no-preference @390x844
  for(const rm of ['reduce','no-preference']){
   const {p,ctx,srv}=await open(b,key,{width:390,height:844},{reducedMotion:rm});
   const r=await p.evaluate(()=>{
    const qa=s=>[...document.querySelectorAll(s)],cs=e=>getComputedStyle(e);
    const lamps=qa('[id^=env2-coll] [data-lamp]');
    const notLit=lamps.filter(e=>parseFloat(cs(e).getPropertyValue('--lit')||'1')<1).length;
    const moving=qa('[id^=env2-coll] *').filter(e=>{const c=cs(e);return parseFloat(c.transitionDuration)>0||c.animationName!=='none'}).length;
    return {lamps:lamps.length,notLit,moving};});
   console.log(key,'rm='+rm,JSON.stringify(r));
   await ctx.close(); srv.close();
  }
}
await b.close();})();
