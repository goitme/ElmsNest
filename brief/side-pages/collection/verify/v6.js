const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
const {p,ctx,srv}=await open(b,'coll-decor',{width:1440,height:900});
const r=await p.evaluate(()=>{
 const out={sheets:[],matched:[]};
 let idx=0;
 for(const sh of document.styleSheets){let rules;try{rules=sh.cssRules}catch(e){out.sheets.push('BLOCKED');continue}
  const id=(sh.ownerNode&&(sh.ownerNode.id||sh.ownerNode.href||sh.ownerNode.tagName))||'?';
  out.sheets.push(idx+':'+id);
  for(const r of rules){ if(!r.selectorText)continue;
   if(/focus-visible/.test(r.selectorText)&&/outline/.test(r.style.cssText)&&(/env2-section|coll-scene__pin|coll-bands__pin/.test(r.selectorText)))
     out.matched.push({sheet:idx+':'+id, sel:r.selectorText, css:r.style.cssText});}
  idx++;}
 return out;});
console.log(JSON.stringify(r,null,1));
// visual: keyboard-focus the scene pin and screenshot the tag region
await p.keyboard.press('Tab');
const shot=await p.evaluate(()=>{const a=document.querySelector('.env2-coll-scene__pin');a.focus();
  const t=a.querySelector('.env2-coll-scene__tag').getBoundingClientRect();const ar=a.getBoundingClientRect();
  return {tag:{x:t.x,y:t.y,w:t.width,h:t.height},anchor:{x:ar.x,y:ar.y,w:ar.width,h:ar.height}};});
console.log('rects',JSON.stringify(shot));
await p.screenshot({path:'/home/user/ElmsNest/brief/side-pages/collection/verify/focus-scene.png',
  clip:{x:Math.max(0,shot.tag.x-40),y:Math.max(0,shot.tag.y-20),width:shot.tag.w+120,height:shot.tag.h+40}});
await ctx.close(); srv.close(); await b.close();})();
