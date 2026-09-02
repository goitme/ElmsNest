#!/usr/bin/env python3
"""Contact sheet of the header band + first heading of the 14 side pages, from the current fold PNGs."""
from PIL import Image, ImageDraw
import sys
KEYS=["coll-all","coll-wall","pdp-single","pdp-multi","cart-full","cart-empty","search-hits",
      "search-none","p404","page-guide","page-shipping","page-contact","policy-shipping","coll-list"]
for view,W,H in (("desktop",2880,560),("mobile",780,560)):
    tiles=[]
    for k in KEYS:
        im=Image.open(f"brief/inventory/{k}/http-{view}-fold.png").convert("RGB")
        crop=im.crop((0,0,im.width,min(H,im.height)))
        scale=900/crop.width
        crop=crop.resize((900,int(crop.height*scale)))
        d=ImageDraw.Draw(crop); d.rectangle([0,0,190,20],fill=(0,0,0)); d.text((6,5),k,fill=(255,211,148))
        tiles.append(crop)
    cols=2; rows=(len(tiles)+cols-1)//cols
    tw,th=tiles[0].width,max(t.height for t in tiles)
    sheet=Image.new("RGB",(cols*tw+ (cols-1)*8, rows*th + (rows-1)*8),(40,40,40))
    for i,t in enumerate(tiles):
        sheet.paste(t,((i%cols)*(tw+8),(i//cols)*(th+8)))
    out=f"brief/side-pages/core/headers-{view}-sheet.png"
    sheet.save(out); print(out, sheet.size)
