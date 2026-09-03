const {chromium,open,VROOT}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
const KEYS=['coll-decor','coll-path','coll-wall','coll-spot','coll-all'];
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){
  const {p,ctx,srv}=await open(b,key,{width:1440,height:900});
  const m=await p.evaluate(()=>{
   const q=s=>document.querySelector(s), qa=s=>[...document.querySelectorAll(s)];
   const cs=e=>getComputedStyle(e);
   // band composition
   const bands=qa('.env2-coll-bands__band, [class*=env2-coll-bands__band]');
   const comp=bands.map(e=>{const mm=/env2-coll-bands__band--([a-z0-9]+)/.exec(e.className);
     return {mod:mm?mm[1]:null, kind:e.getAttribute('data-kind'), cls:e.className, comp:e.getAttribute('data-composition')||e.getAttribute('data-comp')};});
   // rail default state
   const checked=q('#env2-coll-ruler input[type=radio]:checked');
   const rows=qa('#env2-coll-ruler [class*=env2-coll-rail__row]');
   const rowTxt=qa('#env2-coll-ruler [class*=env2-coll-rail__row]').slice(0,6).map(e=>e.innerText.replace(/\n+/g,' | ').trim().slice(0,140));
   const perTxt=qa('.env2-coll-rail__per--entry').map(e=>e.textContent.trim());
   // cursor
   const cur=q('[class*=env2-coll-rail__cursor],[class*=cursor]');
   const curInfo=cur?{cls:cur.className,op:cs(cur).opacity,left:+cur.getBoundingClientRect().left.toFixed(1),w:+cur.getBoundingClientRect().width.toFixed(1)}:null;
   // ground
   const bodyBI=cs(document.body).backgroundImage;
   const bodyBS=cs(document.body).backgroundSize;
   let groundEls=[];
   for(const e of qa('body > *, #env2-coll-scene, [class*=ground]')){const c=cs(e);
     if(c.backgroundImage&&c.backgroundImage.includes('gradient')) groundEls.push({tag:e.tagName,cls:(e.className||'').toString().slice(0,60),bi:c.backgroundImage.slice(0,300),bs:c.backgroundSize});}
   // html bg
   const htmlBI=cs(document.documentElement).backgroundImage;
   // terms rows
   const tr=qa('[class*=terms]').filter(e=>/row|item|li/i.test(e.className)).slice(0,3).map(e=>({cls:e.className,mw:cs(e).maxInlineSize||cs(e).maxWidth,w:+e.getBoundingClientRect().width.toFixed(0)}));
   const termsNum=qa('[class*=coll-terms] [class*=num]').slice(0,2).map(e=>({cls:e.className,fs:cs(e).fontSize}));
   const ledgerRows=qa('[class*=coll-ledger__row]').slice(0,3).map(e=>({w:+e.getBoundingClientRect().width.toFixed(0),mw:cs(e).maxInlineSize}));
   // alt=""
   const imgs=qa('img');
   const noAlt=imgs.filter(e=>!e.hasAttribute('alt')).length;
   const emptyAlt=imgs.filter(e=>e.getAttribute('alt')==='').map(e=>e.className||e.src.split('/').pop());
   return {comp, checkedId:checked?checked.id:null, checkedLabel:checked?(document.querySelector(`label[for="${checked.id}"]`)||{}).textContent:null,
     nRows:rows.length, rowTxt, perTxt, curInfo, bodyBI:bodyBI.slice(0,400), bodyBS, htmlBI:htmlBI.slice(0,200), groundEls:groundEls.slice(0,4), tr, termsNum, ledgerRows, noAlt, emptyAlt:emptyAlt.slice(0,5), nImgs:imgs.length};
  });
  console.log('=== '+key);
  console.log(JSON.stringify(m,null,1));
  await ctx.close(); srv.close();
}
await b.close();})();
