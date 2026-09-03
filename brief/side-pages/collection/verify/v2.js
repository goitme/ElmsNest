const {chromium,open,VROOT}=require('/home/user/ElmsNest/brief/side-pages/collection/verify/srv.js');
const KEYS=['coll-decor','coll-path','coll-wall','coll-spot','coll-all'];
(async()=>{
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of KEYS){
 for(const [w,h] of [[1440,900],[390,844]]){
  const {p,ctx,srv}=await open(b,key,{width:w,height:h});
  const m=await p.evaluate(()=>{
   const q=s=>document.querySelector(s);
   const h1=q('#env2-coll-scene .env2-coll-scene__h1'); if(!h1) return null;
   const glow=q('.env2-coll-scene__h1b');
   // build word-level line map by wrapping each word in a temp span
   const walker=document.createTreeWalker(h1,NodeFilter.SHOW_TEXT);
   const nodes=[];let n;while(n=walker.nextNode())nodes.push(n);
   const marks=[];
   for(const tn of nodes){
     const parts=tn.textContent.split(/(\s+)/).filter(s=>s.length);
     const frag=document.createDocumentFragment();
     for(const part of parts){
       if(/^\s+$/.test(part)){frag.appendChild(document.createTextNode(part));continue;}
       const s=document.createElement('span'); s.setAttribute('data-vw','1'); s.textContent=part;
       s.dataset.inGlow = (glow && glow.contains(tn)) ? '1':'0';
       frag.appendChild(s); marks.push(s);
     }
     tn.parentNode.replaceChild(frag,tn);
   }
   const info=marks.map(s=>{const r=s.getBoundingClientRect();return{t:Math.round(r.top),l:+r.left.toFixed(1),r:+r.right.toFixed(1),w:+r.width.toFixed(1),txt:s.textContent,glow:s.dataset.inGlow==='1'};});
   // group by line top
   const linesMap={};for(const i of info){(linesMap[i.t]=linesMap[i.t]||[]).push(i);}
   const lines=Object.keys(linesMap).sort((a,b)=>a-b).map(t=>{const ws=linesMap[t];
     return {top:+t, words:ws.map(x=>x.txt), n:ws.length, allGlow:ws.every(x=>x.glow), anyGlow:ws.some(x=>x.glow),
       width:+(Math.max(...ws.map(x=>x.r))-Math.min(...ws.map(x=>x.l))).toFixed(0)};});
   const h1r=h1.getBoundingClientRect();
   const cs=getComputedStyle(h1);
   // desc chars per line
   let desc=null;const d=q('.env2-coll-scene__p');
   if(d){const r=document.createRange();r.selectNodeContents(d);const rects=[...r.getClientRects()].map(x=>+x.width.toFixed(0));
     const txt=d.textContent.trim();
     desc={rects, w:+d.getBoundingClientRect().width.toFixed(0), max:getComputedStyle(d).maxInlineSize, fs:getComputedStyle(d).fontSize,
       chars:txt.length, approxPerLine: rects.length?Math.round(txt.length/rects.length):null, txt:txt.slice(0,60)};}
   return {lines, h1w:+h1r.width.toFixed(0), h1max:cs.maxInlineSize||cs.maxWidth, wrap:cs.textWrap||cs.textWrapStyle, glowTxt:glow?glow.textContent:null, desc};
  });
  console.log('=== '+key+' '+w+'x'+h+'  h1 box '+(m?m.h1w:'-')+' max '+(m?m.h1max:'-')+' wrap '+(m?m.wrap:'-')+' glow="'+(m?m.glowTxt:'-')+'"');
  if(m) for(const L of m.lines) console.log('   line w='+String(L.width).padStart(4)+' allGlow='+(L.allGlow?'YES':'no ')+' anyGlow='+(L.anyGlow?'y':'n')+'  '+L.words.join(' '));
  if(m&&m.desc) console.log('   DESC w='+m.desc.w+' max='+m.desc.max+' fs='+m.desc.fs+' lineRects='+JSON.stringify(m.desc.rects)+' chars='+m.desc.chars+' ~perLine='+m.desc.approxPerLine);
  await ctx.close(); srv.close();
 }}
await b.close();})();
