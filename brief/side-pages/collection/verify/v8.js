const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of ['coll-decor','coll-wall']){
 const {p,ctx,srv}=await open(b,key,{width:1440,height:900},{javaScriptEnabled:false});
 const rows=async()=>{const h=await p.$$('#env2-coll-ruler [class*=rail__r], #env2-coll-ruler li, #env2-coll-ruler [class*=__row]');
   const o=[];for(const e of h.slice(0,10)){const t=(await e.innerText()).replace(/\s*\n\s*/g,' | ').trim();if(t)o.push(t.slice(0,120));}return o;};
 console.log('=== '+key+' BEFORE (הכול)');(await rows()).forEach(t=>console.log('  '+t));
 const labels=await p.$$('#env2-coll-ruler label');
 await labels[2].click({force:true}); await p.waitForTimeout(400);
 console.log('--- AFTER clicking "'+(await labels[2].innerText()).trim()+'" (JS DISABLED)');
 (await rows()).forEach(t=>console.log('  '+t));
 // prices present, cart form present
 const html=await p.content();
 console.log('  prices=',(html.match(/env2-price/g)||[]).length,' cartForms=',(html.match(/action="\/cart\/add"/g)||[]).length,
   ' sortAnchors=',(html.match(/sort_by=/g)||[]).length);
 await ctx.close(); srv.close();
}
await b.close();})();
