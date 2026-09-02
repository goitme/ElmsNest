#!/usr/bin/env python3
"""Slice a tall full-page screenshot into readable pieces. Usage: crops.py <key> <desktop|mobile> <n> [scale=0.5] [prefix=shot]
→ <scratchpad>/crops/<key>-<vp>-<i>.jpg"""
import sys,os
from PIL import Image
key,vp,n=sys.argv[1],sys.argv[2],int(sys.argv[3]); scale=float(sys.argv[4]) if len(sys.argv)>4 else 0.5; prefix=sys.argv[5] if len(sys.argv)>5 else 'shot'
out='/tmp/claude-0/-home-user-ElmsNest/1c2132db-077d-58e0-b54a-35f2ebea6b2c/scratchpad/crops'; os.makedirs(out,exist_ok=True)
im=Image.open(f'/home/user/ElmsNest/brief/inventory/{key}/{prefix}-{vp}.png').convert('RGB')
im=im.resize((round(im.width*scale),round(im.height*scale)),Image.LANCZOS)
h=im.height//n
for i in range(n):
    c=im.crop((0,i*h,im.width,(i+1)*h if i<n-1 else im.height)); p=f'{out}/{key}-{vp}-{i+1}.jpg'; c.save(p,quality=80); print(p,c.size)
