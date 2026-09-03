const {chromium,open,VROOT}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
const fs=require('fs');
const KEYS=['coll-decor','coll-path','coll-wall','coll-spot','coll-all'];
const VPS=[[1440,900],[390,844],[390,664],[360,640],[320,568]];
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
const all={};
for(const key of KEYS){all[key]={};
 for(const [w,h] of VPS){
  const {p,ctx,srv}=await open(b,key,{width:w,height:h});
  const m=await p.evaluate(()=>{
   const q=s=>document.querySelector(s), qa=s=>[...document.querySelectorAll(s)];
   const cs=e=>e?getComputedStyle(e):null;
   const R=e=>{if(!e)return null;const r=e.getBoundingClientRect();return{t:+r.top.toFixed(1),b:+r.bottom.toFixed(1),l:+r.left.toFixed(1),r:+r.right.toFixed(1),w:+r.width.toFixed(1),h:+r.height.toFixed(1)};};
   const Rq=s=>R(q(s));
   const tag=Rq('#env2-coll-scene .env2-coll-scene__tag');
   const h1=Rq('#env2-coll-scene .env2-coll-scene__h1');
   const eb=Rq('#env2-coll-scene .env2-eyebrow');
   const vov=(a,x)=>!!(a&&x)&&a.t<x.b&&a.b>x.t;            // vertical band overlap (critic's method)
   const box=(a,x)=>!!(a&&x)&&a.t<x.b&&a.b>x.t&&a.l<x.r&&a.r>x.l; // true rect intersection
   // buy control inside the scene card
   let buy=null;const card=q('#env2-coll-scene .env2-coll-scene__card');
   if(card){const el=card.querySelector('.env2-btn')||card.querySelector('button,a.env2-btn');if(el)buy=R(el);}
   // h1 line boxes
   const lines=(()=>{const e=q('#env2-coll-scene .env2-coll-scene__h1');if(!e)return null;const r=document.createRange();r.selectNodeContents(e);
     return [...r.getClientRects()].map(x=>+x.width.toFixed(0));})();
   const glowAlone=(()=>{const g=q('.env2-coll-scene__h1b');const e=q('#env2-coll-scene .env2-coll-scene__h1');if(!g||!e)return null;
     const gr=g.getBoundingClientRect();const r=document.createRange();r.selectNodeContents(e);const rects=[...r.getClientRects()];
     // the line box containing the glow span's vertical centre
     const cy=(gr.top+gr.bottom)/2;const line=rects.find(x=>cy>=x.top-1&&cy<=x.bottom+1);
     if(!line)return null;return Math.abs(line.width-gr.width)<2;})();
   const pinnames=qa('.env2-coll-bands__pinname').map(e=>({fs:cs(e).fontSize,ls:cs(e).letterSpacing,tt:cs(e).textTransform,
     clipped:e.scrollWidth>e.clientWidth+1||e.scrollHeight>e.clientHeight+1, ell:cs(e).textOverflow, ws:cs(e).whiteSpace,
     txt:e.textContent.trim(), cls:e.className}));
   const st=q('.env2-coll-scene__tagname');
   const gc=q('.env2-coll-glyph__cap');
   const grp=q('#env2-coll-ruler [role=group]');
   const dsc=q('.env2-coll-scene__p')||q('.env2-coll-scene__desc');
   const hs=qa('[id^=env2-coll] h1,[id^=env2-coll] h2,[id^=env2-coll] h3,[id^=env2-coll] h4,[id^=env2-coll] h5,[id^=env2-coll] h6').map(e=>+e.tagName[1]);
   const jumps=[];for(let i=1;i<hs.length;i++) if(hs[i]-hs[i-1]>1) jumps.push(hs[i-1]+'->'+hs[i]);
   // overflow: page + elements crossing viewport edge inside our sections
   const de=document.documentElement;
   const crossing=qa('[id^=env2-coll] *').filter(e=>{const r=e.getBoundingClientRect();
     if(r.width===0||r.height===0)return false;const c=cs(e);if(c.position==='fixed')return false;
     return r.right>de.clientWidth+1||r.left<-1;}).filter(e=>{ // ignore ones inside an overflow-x container
     let n=e.parentElement;while(n&&n!==document.body){const c=cs(n);if(c.overflowX==='auto'||c.overflowX==='scroll'||c.overflowX==='hidden')return false;n=n.parentElement;}return true;})
     .map(e=>e.className+'|'+Math.round(e.getBoundingClientRect().right));
   const lampImgs=qa('[id^=env2-coll] [data-lamp] .env2-ph img');
   const filters={};for(const e of lampImgs){const f=cs(e).filter;filters[f]=(filters[f]||0)+1;}
   const quotes=qa('.env2-coll-bands__quote');
   const bands=qa('[data-kind]').map(e=>e.getAttribute('data-kind'));
   const bandComp=qa('.env2-coll-bands__band').map(e=>e.getAttribute('data-comp')||e.getAttribute('data-kind')||e.className);
   const perEntry=qa('.env2-coll-rail__per--entry').length;
   const perAll=qa('[class*=env2-coll-rail__per]').length;
   const railRows=qa('#env2-coll-ruler .env2-coll-rail__row, #env2-coll-ruler [class*=rail__row]').length;
   const prices=qa('#env2-coll-ruler .env2-price').map(e=>{const r=e.getBoundingClientRect();return{l:+r.left.toFixed(0),r:+r.right.toFixed(0)};});
   const placenames=qa('.env2-coll-ruler__placename');
   return {
    tag,h1,eb,buy,
    tagOverH1_vert:vov(tag,h1), tagOverH1_box:box(tag,h1),
    tagOverEb_vert:vov(tag,eb), tagOverEb_box:box(tag,eb),
    gapH1:(tag&&h1)?+(h1.t-tag.b).toFixed(1):null,
    gapEb:(tag&&eb)?+(eb.t-tag.b).toFixed(1):null,
    buyInFold: buy?buy.b<=window.innerHeight:null,
    narrowlinkN: qa('.env2-coll-scene__narrowlink').length,
    narrowlink: Rq('.env2-coll-scene__narrowlink'),
    narrowInFold:(()=>{const n=Rq('.env2-coll-scene__narrowlink');return n?n.b<=window.innerHeight:null})(),
    rulerLinksInScene: qa('#env2-coll-scene a[href="#env2-coll-ruler"]').length,
    h1count: document.querySelectorAll('h1').length,
    h1text: q('h1')?q('h1').textContent.trim():null,
    headings:hs, jumps,
    h1bDisplay:(()=>{const e=q('.env2-coll-scene__h1b');return e?cs(e).display:'NOSPAN'})(),
    h1lines:lines, glowAlone,
    descMax: dsc?(cs(dsc).maxInlineSize||cs(dsc).maxWidth):null,
    descW: dsc?+dsc.getBoundingClientRect().width.toFixed(0):null,
    descCls: dsc?dsc.className:null,
    sceneTag: st?{fs:cs(st).fontSize,ls:cs(st).letterSpacing,tt:cs(st).textTransform,txt:st.textContent.trim()}:null,
    sceneTagBg:(()=>{const e=q('.env2-coll-scene__tag');return e?{bg:cs(e).backgroundColor,bd:cs(e).backdropFilter}:null})(),
    pinnames,
    glyphcap: gc?{fs:cs(gc).fontSize,ah:gc.getAttribute('aria-hidden'),txt:gc.textContent.trim()}:null,
    glyphcapN: qa('.env2-coll-glyph__cap').length,
    glyphcapAllHidden: qa('.env2-coll-glyph__cap').every(e=>e.getAttribute('aria-hidden')==='true'),
    groupAria: grp?grp.getAttribute('aria-label'):null,
    rulerEyebrow:(()=>{const e=q('.env2-coll-ruler__eyebrow');return e?e.textContent.trim():null})(),
    rulerH2:(()=>{const e=q('.env2-coll-ruler__h2');return e?e.textContent.trim():null})(),
    numcap:(()=>{const e=q('.env2-coll-ruler__numcap');return e?e.textContent.trim():null})(),
    quoteN: quotes.length,
    quoteBg: quotes[0]?cs(quotes[0]).backgroundColor:null,
    quoteFs: quotes[0]?cs(quotes[0]).fontSize:null,
    quoteTxt: quotes[0]?quotes[0].textContent.trim().slice(0,90):null,
    quoteBefore: quotes[0]?getComputedStyle(quotes[0],'::before').content:null,
    bandKinds: bands, bandComp,
    perEntry, perAll, railRows,
    railPrices: prices,
    placenameDisp: placenames[0]?cs(placenames[0]).display:null, placenameN:placenames.length,
    bodyBg: cs(document.body).backgroundImage.slice(0,220),
    groundEl:(()=>{const e=q('.env2-ground')||q('[class*=ground]');return e?{cls:e.className,bi:cs(e).backgroundImage.slice(0,260),bs:cs(e).backgroundSize}:null})(),
    lampFilters: filters,
    overflowPage: de.scrollWidth>de.clientWidth,
    scrollW:de.scrollWidth, clientW:de.clientWidth,
    crossing: crossing.slice(0,6), crossingN:crossing.length,
    pageH: document.body.scrollHeight,
    ledgerK:(()=>{const e=q('.env2-coll-ledger__k');return e?{d:cs(e).display,gtc:cs(e).gridTemplateColumns}:null})(),
    ledgerRowMax:(()=>{const e=q('.env2-coll-ledger__row')||q('[class*=coll-ledger__row]');return e?{mw:cs(e).maxInlineSize||cs(e).maxWidth,w:+e.getBoundingClientRect().width.toFixed(0)}:null})(),
    termsRowMax:(()=>{const e=q('[class*=coll-terms__row]');return e?{mw:cs(e).maxInlineSize||cs(e).maxWidth,w:+e.getBoundingClientRect().width.toFixed(0)}:null})(),
   };
  });
  all[key][`${w}x${h}`]=m;
  await ctx.close(); srv.close();
 }
 console.log('done '+key);
}
fs.writeFileSync(VROOT+'/v1.json',JSON.stringify(all,null,1));
await b.close();})();
