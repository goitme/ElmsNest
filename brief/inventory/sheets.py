#!/usr/bin/env python3
"""Contact sheets for the inventory: per page, desktop + mobile full-page shots side by side at reduced scale,
plus a strip with both folds. Usage: python3 brief/inventory/sheets.py [prefix=shot] → <dir>/sheet-<prefix>.jpg"""
import glob,os,sys
from PIL import Image
prefix=sys.argv[1] if len(sys.argv)>1 else 'shot'
for d in sorted(glob.glob('/home/user/ElmsNest/brief/inventory/*/')):
    k=os.path.basename(d.rstrip('/'))
    fs={n:d+f'{prefix}-{n}.png' for n in ('desktop','mobile','desktop-fold','mobile-fold')}
    if not all(os.path.exists(f) for f in fs.values()): continue
    im={n:Image.open(f).convert('RGB') for n,f in fs.items()}
    # scale: desktop full → 720 wide; mobile full → 300 wide; folds → 480 / 200
    def sc(i,w): return i.resize((w,max(1,round(i.height*w/i.width))),Image.LANCZOS)
    D=sc(im['desktop'],720); M=sc(im['mobile'],300); DF=sc(im['desktop-fold'],480); MF=sc(im['mobile-fold'],210)
    H=max(D.height,M.height,DF.height+MF.height+20)
    W=720+300+480+60
    sheet=Image.new('RGB',(W,min(H,14000)),(24,24,24))
    sheet.paste(D,(0,0)); sheet.paste(M,(740,0)); sheet.paste(DF,(1060,0)); sheet.paste(MF,(1060,DF.height+20))
    out=d+f'sheet-{prefix}.jpg'; sheet.save(out,quality=78,optimize=True)
    print(k, sheet.size, os.path.getsize(out)//1024,'KB')
