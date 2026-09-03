const path=require('path'), fs=require('fs'), http=require('http');
function lp(){const roots=[];try{for(const d of fs.readdirSync('/tmp/claude-0/-home-user-ElmsNest'))roots.push(`/tmp/claude-0/-home-user-ElmsNest/${d}/scratchpad`);}catch(e){}
 for(const r of roots){try{return require(`${r}/node_modules/playwright`);}catch(e){}} return require('playwright');}
const {chromium}=lp();
const FONT_DIR='/home/user/ElmsNest/brief/assets/fonts';
const FF={FrankRuhlLibre:'Frank Ruhl Libre',Heebo:'Heebo'};
const FR={hebrew:'U+0590-05FF,U+200C-2010,U+20AA,U+25CC,U+FB1D-FB4F',latin:'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215'};
function faceCss(port){let css='';for(const f of fs.readdirSync(FONT_DIR)){const m=/^(FrankRuhlLibre|Heebo)-(hebrew|latin)-(\d+)\.woff2$/.exec(f);if(!m)continue;
 css+=`@font-face{font-family:"${FF[m[1]]}";font-style:normal;font-weight:${m[3]};font-display:block;src:url(http://127.0.0.1:${port}/__fonts/${f}) format("woff2");unicode-range:${FR[m[2]]}}\n`;}return css;}
const MIME={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.gif':'image/gif','.woff':'font/woff','.woff2':'font/woff2','.ico':'image/x-icon','.json':'application/json'};
function serve(root,file){return http.createServer((req,res)=>{const p=decodeURIComponent(req.url.split('?')[0]);
 if(p.startsWith('/__fonts/')){const g=path.join(FONT_DIR,path.basename(p));if(fs.existsSync(g)){res.writeHead(200,{'Content-Type':'font/woff2','Access-Control-Allow-Origin':'*'});return fs.createReadStream(g).pipe(res);}res.writeHead(404);return res.end();}
 let f=path.join(root,p==='/'?file:p);let g=f;
 if(!g.startsWith(root)||!fs.existsSync(g)||fs.statSync(g).isDirectory()){const base=path.basename(g);g=null;
  for(const dir of ['/home/user/ElmsNest/brief/inventory','/home/user/ElmsNest/brief/build-preview']){try{for(const sub of fs.readdirSync(dir)){const c=path.join(dir,sub,'a',base);if(fs.existsSync(c)&&fs.statSync(c).size>0){g=c;break;}}}catch(e){}if(g)break;}
  if(!g){res.writeHead(404);return res.end();}}
 f=g;res.writeHead(200,{'Content-Type':MIME[path.extname(f).toLowerCase()]||'application/octet-stream','Access-Control-Allow-Origin':'*'});
 if(f===path.join(root,file))return res.end(fs.readFileSync(f,'utf8').replace(/(["'])a\//g,'$1/a/'));
 fs.createReadStream(f).pipe(res);});}
module.exports={chromium,faceCss,serve};
