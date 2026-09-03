const {chromium,open}=require('./srv.js');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});
for(const key of ['coll-decor','coll-all']){
 const {p,ctx,srv}=await open(b,key,{width:1440,height:900});
 const H=await p.evaluate(()=>document.body.scrollHeight);
 const shots=[];
 for(let i=0;i<10;i++){const y=Math.round(H*i/10);
  await p.evaluate(yy=>window.scrollTo(0,yy),y); await p.waitForTimeout(250);
  const buf=await p.screenshot({clip:{x:4,y:400,width:12,height:12}});
  shots.push({y,buf});}
 const fs=require('fs');
 fs.writeFileSync(`/tmp/${key}-samples.json`,JSON.stringify(shots.map(s=>({y:s.y,b64:s.buf.toString('base64')}))));
 console.log(key,'height',H,'samples written');
 await ctx.close(); srv.close();}
await b.close();})();
