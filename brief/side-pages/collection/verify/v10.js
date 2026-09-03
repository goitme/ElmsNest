const {chromium,open}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
const {p,ctx,srv}=await open(b,'coll-decor',{width:1440,height:900});
const m=await p.evaluate(()=>{
 const qa=s=>[...document.querySelectorAll(s)],cs=e=>getComputedStyle(e);
 const ks=qa('.env2-coll-ledger__k');
 const num=qa('.env2-coll-ledger__k > *').map(e=>{const r=e.getBoundingClientRect();return{cls:e.className,txt:e.textContent.trim(),l:+r.left.toFixed(1),r:+r.right.toFixed(1),ta:cs(e).textAlign}});
 const rows=qa('[class*=env2-coll-ledger__row]').map(e=>{const r=e.getBoundingClientRect();return{w:+r.width.toFixed(0),l:+r.left.toFixed(0),rr:+r.right.toFixed(0)}});
 // name end vs price start inside one row
 const pairs=qa('[class*=env2-coll-ledger__row]').slice(0,4).map(e=>{
   const n=e.querySelector('[class*=name],[class*=title],a'); const pr=e.querySelector('.env2-price');
   const R=x=>x?(()=>{const r=x.getBoundingClientRect();return{l:+r.left.toFixed(0),r:+r.right.toFixed(0)}})():null;
   return {name:R(n),price:R(pr), gap: (n&&pr)?+(n.getBoundingClientRect().left-pr.getBoundingClientRect().right).toFixed(0):null};});
 const sec=document.querySelector('#env2-coll-ledger');
 return {nK:ks.length, num:num.slice(0,10), rows:rows.slice(0,4), pairs, secTop: sec?Math.round(sec.getBoundingClientRect().top+window.scrollY):null};});
console.log(JSON.stringify(m,null,1));
if(m.secTop){await p.evaluate(y=>window.scrollTo(0,y),m.secTop); await p.waitForTimeout(500);
 await p.screenshot({path:'/home/user/ElmsNest/brief/side-pages/collection/verify/ledger.png',clip:{x:0,y:0,width:1440,height:900}});}
await ctx.close(); srv.close(); await b.close();})();
