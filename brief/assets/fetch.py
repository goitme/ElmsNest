"""Regenerates the local asset pack (fonts + images) used by offline mockups.
Run from brief/assets:  python3 fetch.py
Binaries are gitignored; this script is the source of truth."""
import subprocess,re,os,json
from PIL import Image
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
os.makedirs("fonts",exist_ok=True); os.makedirs("img",exist_ok=True)
fams={"Heebo":"wght@300;400;500;700;800;900","Rubik":"wght@300;400;500;700;900","Frank+Ruhl+Libre":"wght@300;400;500;700;900","Suez+One":"","Secular+One":"","Karantina":"wght@300;400;700","Bellefair":"","Assistant":"wght@300;400;600;700;800","Miriam+Libre":"wght@400;700","Noto+Serif+Hebrew":"wght@300;400;600;800","David+Libre":"wght@400;500;700","Alef":"wght@400;700"}
css_out=[]
for fam,axis in fams.items():
    url=f"https://fonts.googleapis.com/css2?family={fam}"+(f":{axis}" if axis else "")+"&display=swap"
    css=subprocess.run(["curl","-sS","-A",UA,url],capture_output=True,text=True).stdout
    for subset,body in re.findall(r'/\* (\w+) \*/\s*@font-face \{(.*?)\}',css,re.S):
        if subset not in ("hebrew","latin"): continue
        m=re.search(r'url\((https://[^)]+)\)',body)
        if not m: continue
        src=m.group(1); fname=fam.replace('+','')+"-"+subset+"-"+re.search(r'font-weight: (\d+)',body).group(1)+("-i" if "italic" in body else "")+".woff2"
        if not os.path.exists("fonts/"+fname): subprocess.run(["curl","-sS","-o","fonts/"+fname,src])
        css_out.append(f"/* {fam} {subset} */\n@font-face {{{body.replace(src,'fonts/'+fname)}}}")
open("fonts.css","w").write("\n".join(css_out))
cat=json.load(open("../catalog.json"))
jobs=[(f"img/{p['handle']}-{i}.jpg",u) for p in cat["products"] for i,u in enumerate(p["images"])]
cols={"path":"https://cdn.shopify.com/s/files/1/0689/4927/8894/collections/u1879343312_a_single_real_solar_pathway_stake_light_installed_41768c9e-1393-483f-bbb8-d4a432cdb5f5_0.png?v=1781370749","wall":"https://cdn.shopify.com/s/files/1/0689/4927/8894/collections/u1879343312_solar_wall_light_on_a_modern_exterior_wall_warm_g_892144ba-5c87-4d2d-b58d-60e168b0cbb9_3.png?v=1781369741","decor":"https://cdn.shopify.com/s/files/1/0689/4927/8894/collections/u1879343312_real_outdoor_decorative_string_lights_in_a_home_g_b1972f25-2ec8-4e4d-b253-015693b651da_3.png?v=1781371196","spot":"https://cdn.shopify.com/s/files/1/0689/4927/8894/collections/u1879343312_real_solar_spotlights_illuminating_a_home_garden__fda15a86-c920-4892-a6a6-3c55edb4c411_0.png?v=1781371445"}
jobs+= [(f"img/collection-{k}.jpg",u) for k,u in cols.items()]
# Frames the PDP image ledger (snippets/elmsnest-v2-pdp-image.liquid) needs beyond catalog.json's
# first four. modern-led-wall-light-indoor-outdoor carries baked-in Hebrew marketing text on images
# 0-3; index 4 is its only text-free frame, so the card/close slots point at it.
jobs+= [("img/modern-led-wall-light-indoor-outdoor-4.jpg","https://cdn.shopify.com/s/files/1/0689/4927/8894/files/ChatGPTImageAug1_2026_09_49_48PM_1.png?v=1785610205")]
jobs+= [("img/logo.png","https://cdn.shopify.com/s/files/1/0689/4927/8894/files/ElmsNest_Logo_Night.png?v=1786651424"),("img/hero-desktop.webp","https://elmsnest.com/cdn/shop/t/21/assets/elmsnest-hero-desktop-performance.webp"),("img/hero-mobile.webp","https://elmsnest.com/cdn/shop/t/21/assets/elmsnest-hero-mobile-performance.webp")]
for out,u in jobs:
    if os.path.exists(out): continue
    tmp=out+".tmp"; subprocess.run(["curl","-sSL","--max-time","60","-o",tmp,u])
    if out.endswith(".jpg"):
        im=Image.open(tmp).convert("RGB"); im.thumbnail((1000,1000)); im.save(out,quality=86,optimize=True); os.remove(tmp)
    else: os.rename(tmp,out)
print("done")
