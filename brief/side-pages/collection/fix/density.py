import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
def dens(path,band=900,thr=34):
    im=Image.open(path).convert('L'); w,h=im.size; out=[]
    for y0 in range(0,h,band):
        y1=min(h,y0+band)
        if y1-y0 < band*0.5 and y0>0: break
        c=im.crop((0,y0,w,y1))
        px=c.getdata(); n=len(px); k=sum(1 for v in px if v>thr)
        out.append(round(100.0*k/n,1))
    return h,out
for p in sys.argv[1:]:
    h,d=dens(p)
    s=sorted(d); med=s[len(s)//2] if len(s)%2 else round((s[len(s)//2-1]+s[len(s)//2])/2,1)
    print(f"{p.split('/')[-1]:28s} h={h:6d} median={med:5.1f}  "+" · ".join(f"{x}" for x in d))
