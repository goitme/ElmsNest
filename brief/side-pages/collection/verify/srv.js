const path=require('path'), fs=require('fs'), http=require('http');
const PW='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/node_modules/playwright';
const {chromium}=require(PW);
const FONT_DIR='/home/user/ElmsNest/brief/assets/fonts';
const FF={FrankRuhlLibre:'Frank Ruhl Libre',Heebo:'Heebo'};
const FR={hebrew:'U+0590-05FF,U+200C-2010,U+20AA,U+25CC,U+FB1D-FB4F',latin:'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215'};
function faceCss(port){let css='';let files=[];try{files=fs.readdirSync(FONT_DIR);}catch(e){return '';}
 for(const f of files){const m=/^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f);if(!m)continue;
 css+=`@font-face{font-family:"${FF[m[1]]}";font-style:normal;font-weight:${m[3]};font-display:block;src:url(http://127.0.0.1:${port}/__fonts/${f}) format("woff2");unicode-range:${FR[m[2]]}}\n`;}return css;}
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
const VROOT='/home/user/ElmsNest/brief/side-pages/collection/verify';
function serve(root,file){const srv=http.createServer((req,res)=>{const p=decodeURIComponent(req.url.split('?')[0]);
 if(p.startsWith('/__fonts/')){const g=path.join(FONT_DIR,path.basename(p));if(fs.existsSync(g)){res.writeHead(200,{'Content-Type':'font/woff2','Access-Control-Allow-Origin':'*'});return fs.createReadStream(g).pipe(res);}res.writeHead(404);return res.end();}
 let f=path.join(root,p==='/'?file:p);let g=f;
 if(!g.startsWith(root)||!fs.existsSync(g)||fs.statSync(g).isDirectory()){const base=path.basename(g);g=null;
  try{for(const sub of fs.readdirSync(VROOT)){const c=path.join(VROOT,sub,'a',base);if(fs.existsSync(c)&&fs.statSync(c).size>0){g=c;break;}}}catch(e){}
  if(!g){res.writeHead(404);return res.end();}}
 f=g;res.writeHead(200,{'Content-Type':MIME[path.extname(f).toLowerCase()]||'application/octet-stream','Access-Control-Allow-Origin':'*'});
 if(f===path.join(root,file)){return res.end(fs.readFileSync(f,'utf8').replace(/(["'])a\//g,'$1/a/'));}
 fs.createReadStream(f).pipe(res);});return srv;}
async function open(b,key,vp,opts={}){
 const root=`${VROOT}/${key}`;const srv=serve(root,'index.html');
 await new Promise(r=>srv.listen(0,'127.0.0.1',r));const port=srv.address().port;const faces=faceCss(port);
 const ctx=await b.newContext(Object.assign({viewport:vp,deviceScaleFactor:1,locale:'he-IL',isMobile:vp.width<1000,hasTouch:vp.width<1000},opts));
 await ctx.route(/^https?:\/\//,r=>{const u=r.request().url();if(/^https?:\/\/127\.0\.0\.1:/.test(u))return r.continue();
  if(/fonts\.googleapis\.com/.test(u))return r.fulfill({status:200,contentType:'text/css',body:faces});return r.abort();});
 const p=await ctx.newPage();
 await p.goto(`http://127.0.0.1:${port}/index.html`,{waitUntil:'domcontentloaded',timeout:90000});
 await p.waitForTimeout(1600);
 return {p,ctx,srv};
}
module.exports={chromium,serve,faceCss,open,VROOT};
