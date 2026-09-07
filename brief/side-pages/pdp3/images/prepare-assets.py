#!/usr/bin/env python3
"""Turn chosen photographs into DEV-THEME assets — PDP round 3 and the content pages.
  prepare-assets.py <id>=<slug>[:x,y,w,h] [...] [--prefix ens-pdp|ens-page] [--max-width 1800] [--kb 220] [--chosen <md>]
Ids are looked up in THIS round's manifest (pdp3/images/manifest.jsonl) first, then in the home round's pool
(home2/images/manifest.jsonl — internet photographs and the store's own frames). For each: open, EXIF-orient, optional
pre-crop (pixels in the source), resize to ≤ max-width on the long side, save as progressive JPEG stepping the quality
down from 82 until ≤ kb, write theme/assets/<prefix>-<slug>.jpg and append one row (id, size, weight, source, licence,
author, page, the credit line the section must carry) to the CHOSEN.md of this folder (or --chosen)."""
import sys, os, json, io, hashlib
from PIL import Image, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); SP = os.path.dirname(os.path.dirname(HERE))
THEME = '/home/user/ElmsNest/theme'; os.makedirs(os.path.join(THEME, 'assets'), exist_ok=True)
FLAGS = ('--prefix', '--max-width', '--kb', '--chosen')
argv = sys.argv[1:]
opt = {'--prefix': 'ens-pdp', '--max-width': '1800', '--kb': '220', '--chosen': os.path.join(HERE, 'CHOSEN.md')}
args = []
i = 0
while i < len(argv):
    if argv[i] in FLAGS: opt[argv[i]] = argv[i + 1]; i += 2
    else: args.append(argv[i]); i += 1
prefix, maxw, kb, chosen = opt['--prefix'], int(opt['--max-width']), int(opt['--kb']), opt['--chosen']
POOLS = [HERE, os.path.join(SP, 'home2', 'images')]
man = {}
for d in POOLS:
    p = os.path.join(d, 'manifest.jsonl')
    if os.path.exists(p):
        for l in open(p, encoding='utf-8'):
            r = json.loads(l); r['_dir'] = d; man.setdefault(r['id'], r)
NOCREDIT = ('CC0', 'CC PDM 1.0', 'Public domain', 'PDM', 'CC0 1.0', 'Public domain mark')
n = 0
for spec in args:
    pid, slug = spec.split('=', 1)
    crop = None
    if ':' in slug:
        slug, box = slug.split(':', 1); crop = tuple(int(v) for v in box.split(','))
    rec = man[pid]
    im = ImageOps.exif_transpose(Image.open(os.path.join(rec['_dir'], rec['file']))).convert('RGB')
    if crop:
        x, y, cw, ch = crop; im = im.crop((x, y, x + cw, y + ch))
    w, h = im.size
    if max(w, h) > maxw:
        s = maxw / max(w, h); im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    q = 82; data = None
    while q >= 55:
        b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True, progressive=True); data = b.getvalue()
        if len(data) <= kb * 1024: break
        q -= 4
    name = f'{prefix}-{slug}.jpg'
    open(os.path.join(THEME, 'assets', name), 'wb').write(data)
    n += 1
    lic = rec.get('license') or '?'
    credit = 'none (store-owned)' if lic == 'store-owned' else ('none' if lic in NOCREDIT else f"צילום: {rec.get('author') or '?'} ({lic})")
    new = not os.path.exists(chosen)
    with open(chosen, 'a', encoding='utf-8') as f:
        if new: f.write('| asset | id (crop) | px | weight | source | licence | author | page | credit line |\n|---|---|---|---|---|---|---|---|---|\n')
        f.write(f"| `{name}` | {pid}{' crop ' + ','.join(map(str, crop)) if crop else ''} | {im.width}×{im.height} | {len(data)//1024} KB q{q} | {rec['source']} | {lic} | {rec.get('author') or ''} | {rec.get('page') or rec.get('url')} | {credit} |\n")
    print(f'{name}: {im.width}x{im.height} {len(data)//1024} KB (q{q}) md5 {hashlib.md5(data).hexdigest()} — {lic} {rec.get("author") or ""}')
print(f'{n} assets written to theme/assets; rows appended to {chosen}')
