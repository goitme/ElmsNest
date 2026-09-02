#!/usr/bin/env python3
"""Round-0 acceptance census over the mirrored+shot inventory pages."""
import sys, json, re, os
import numpy as np
from PIL import Image

PAGES = ["home","coll-all","coll-wall","pdp-single","pdp-multi","cart-full","cart-empty",
         "search-hits","search-none","p404","page-guide","page-shipping","page-contact",
         "policy-shipping","coll-list"]
CREAM = {"#f7f0e6":(247,240,230), "#fffdf7":(255,253,247), "#2b2118":(43,33,24)}
BTN   = (13,13,15)   # .hdt-card-product__btn-ultra fill measured at 390

def lum(c):
    def f(v):
        v/=255.0
        return v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4
    return .2126*f(c[0])+.7152*f(c[1])+.0722*f(c[2])
def cr(a,b):
    la,lb=lum(a),lum(b)
    hi,lo=max(la,lb),min(la,lb)
    return (hi+.05)/(lo+.05)

rows=[]
for k in PAGES:
    r={"key":k}
    for v in ("desktop","mobile"):
        f=f"brief/inventory/{k}/http-{v}.png"
        a=np.asarray(Image.open(f).convert("RGB"))
        r[f"{v}_size"]=[a.shape[1],a.shape[0]]
        s=a[::3,::3].reshape(-1,3).astype(np.int16)
        for name,c in CREAM.items():
            r[f"{v}_{name}"]=round(100*float((np.abs(s-np.array(c)).max(axis=1)<=1).mean()),4)
        full=a.reshape(-1,3).astype(np.int16)
        r[f"{v}_btnultra_px"]=int((np.abs(full-np.array(BTN)).max(axis=1)<=2).sum())
        r[f"{v}_btnultra_pct"]=round(100*r[f"{v}_btnultra_px"]/full.shape[0],4)
        # bottom edge colour at six x positions
        bot=a[-1]
        xs=[int(bot.shape[0]*i/7) for i in range(1,7)]
        r[f"{v}_bottom"]=sorted({"#%02x%02x%02x"%tuple(bot[x]) for x in xs})
    # header band on the desktop fold (CSS y 8..64 -> device px 16..128 at dsf 2)
    a=np.asarray(Image.open(f"brief/inventory/{k}/http-desktop-fold.png").convert("RGB"))
    band=a[16:128].reshape(-1,3)
    L=np.array([lum(p) for p in band[::7]])
    px=band[::7]
    glyph=px[L>0.45]; ground=px[L<=0.45]
    if len(ground)==0: ground=px
    gmed=tuple(int(x) for x in np.median(ground,axis=0))
    r["hdr_ground"]="#%02x%02x%02x"%gmed
    r["hdr_glyph_px"]=int(len(glyph))
    if len(glyph):
        gl=tuple(int(x) for x in np.median(glyph,axis=0))
        r["hdr_glyph"]="#%02x%02x%02x"%gl
        r["hdr_cr"]=round(cr(gl,gmed),1)
    else:
        r["hdr_glyph"]=None; r["hdr_cr"]=None
    h=open(f"brief/inventory/{k}/index.html",encoding="utf-8",errors="replace").read()
    r["core_loaded"]=h.count('id="env2-base"')
    r["fonts_loaded"]=h.count('id="env2-fonts"')
    r["ground_index"]=h.count('id="env2-ground-index"')
    r["liquid_errors"]=len(re.findall(r"Liquid error", h))
    r["scheme1_override"]=1 if '[color-scheme="scheme-1"]{\n  --color-background:2 3 6' in h else 0
    log=f"brief/inventory/{k}/shot-http.log"
    r["shot"]=open(log).read().strip().splitlines() if os.path.exists(log) else []
    rows.append(r)
print(json.dumps(rows,indent=1,ensure_ascii=False))
