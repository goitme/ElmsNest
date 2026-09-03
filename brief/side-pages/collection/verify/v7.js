// No-JS: does the CSS-only ruler still narrow? Click a stop label with javaScriptEnabled:false and
// compare the rail region before/after.
const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
const fs=require('fs');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of ['coll-decor','coll-path','coll-wall','coll-spot']){
 const {p,ctx,srv}=await open(b,key,{width:1440,height:900},{javaScriptEnabled:false});
 const ruler=await p.$('#env2-coll-ruler');
 const A=`/home/user/ElmsNest/brief/side-pages/collection/verify/nojs-${key}-all.png`;
 const B=`/home/user/ElmsNest/brief/side-pages/collection/verify/nojs-${key}-stop.png`;
 await ruler.screenshot({path:A});
 const labels=await p.$$('#env2-coll-ruler label');
 // count radios & labels via HTML (no JS available)
 const html=await p.content();
 const nRadios=(html.match(/type="radio"/g)||[]).length;
 // click the 3rd stop label
 let clicked=null;
 if(labels.length>2){ await labels[2].click({force:true}); await p.waitForTimeout(400); clicked=await labels[2].innerText(); }
 await ruler.screenshot({path:B});
 const a=fs.readFileSync(A), bb=fs.readFileSync(B);
 console.log(`${key}: labels=${labels.length} radiosInHTML=${nRadios} clicked='${(clicked||'').trim()}' pngA=${a.length} pngB=${bb.length} differ=${!a.equals(bb)}`);
 await ctx.close(); srv.close();
}
await b.close();})();
