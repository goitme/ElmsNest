#!/usr/bin/env python3
"""Turn chosen photographs into DEV-THEME assets.
  prepare-assets.py <id>=<slug> [<id>=<slug> ...] [--max-width 1800] [--kb 220]
For each manifest id: open the file, EXIF-orient, resize to ≤ max-width on the long side, save as JPEG (progressive,
quality stepping down from 82 until ≤ kb), write theme/assets/ens-home-<slug>.jpg, a BASE64 themeFilesUpsert
mutation to brief/side-pages/home2/deploy/NN-assets__ens-home-<slug>.jpg.graphql, and append the choice with its
source/license/author to images/CHOSEN.md (the credit line the section or footer must carry)."""
import sys, os, json, base64, io, hashlib
from PIL import Image, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); H = os.path.dirname(HERE)
THEME = '/home/user/ElmsNest/theme'; OUT = os.path.join(H, 'deploy'); os.makedirs(OUT, exist_ok=True); os.makedirs(os.path.join(THEME, 'assets'), exist_ok=True)
TID = 'gid://shopify/OnlineStoreTheme/154726400174'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
maxw = int(next((a.split()[0] for a in sys.argv if a.startswith('--max-width')), '--max-width 1800').split()[-1]) if False else 1800
kb = 220
for i, a in enumerate(sys.argv):
    if a == '--max-width': maxw = int(sys.argv[i + 1])
    if a == '--kb': kb = int(sys.argv[i + 1])
man = {json.loads(l)['id']: json.loads(l) for l in open(os.path.join(HERE, 'manifest.jsonl'), encoding='utf-8')}
n = 0
for spec in args:
    pid, slug = spec.split('=', 1)
    rec = man[pid]
    im = ImageOps.exif_transpose(Image.open(os.path.join(HERE, rec['file']))).convert('RGB')
    w, h = im.size
    if max(w, h) > maxw:
        s = maxw / max(w, h); im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    q = 82; data = None
    while q >= 55:
        b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True, progressive=True); data = b.getvalue()
        if len(data) <= kb * 1024: break
        q -= 4
    name = f'ens-home-{slug}.jpg'
    open(os.path.join(THEME, 'assets', name), 'wb').write(data)
    n += 1
    gq = ('mutation { themeFilesUpsert(themeId: "%s", files: [{filename: "assets/%s", body: {type: BASE64, value: "%s"}}]) '
          '{ upsertedThemeFiles { filename size checksumMd5 } userErrors { filename code message } } }') % (TID, name, base64.b64encode(data).decode())
    open(os.path.join(OUT, f'{n:02d}-assets__{name}.graphql'), 'w').write(gq)
    credit = 'none (store-owned)' if rec['license'] == 'store-owned' else ('none' if rec['license'] in ('CC0', 'CC PDM 1.0', 'Public domain') else f"צילום: {rec.get('author') or '?'} ({rec['license']})")
    with open(os.path.join(HERE, 'CHOSEN.md'), 'a', encoding='utf-8') as f:
        f.write(f"| `{name}` | {pid} | {im.width}×{im.height} | {len(data)//1024} KB q{q} | {rec['source']} | {rec['license']} | {rec.get('author') or ''} | {rec.get('page') or rec.get('url')} | {credit} |\n")
    print(f'{name}: {im.width}x{im.height} {len(data)//1024} KB (q{q}) md5 {hashlib.md5(data).hexdigest()} — {rec["license"]} {rec.get("author") or ""}')
print(f'{n} assets written to theme/assets and {OUT}')
