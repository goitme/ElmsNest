#!/usr/bin/env python3
"""Image sourcing helper for the home round 2 (image-led sections).
  fetch.py openverse "<query>" [n]      -> commercial-safe CC results (cc0, pdm, by, by-sa) downloaded to candidates/
  fetch.py commons "<query>" [n]        -> Wikimedia Commons results (license recorded; NC/ND excluded) to candidates/
  fetch.py own                          -> every product image of the store (products.json) to own/
Every download appends a record to images/manifest.jsonl: {id, file, source, url, page, author, license, title, w, h, query}.
Skips files already present. Never overwrites."""
import sys, os, json, re, hashlib, subprocess, urllib.parse, time
HERE = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(HERE, 'manifest.jsonl')
UA = 'ElmsNest-image-sourcing/1.0 (contact: info@elmsnest.com)'
OK_LIC = {'cc0', 'pdm', 'by', 'by-sa', 'CC0', 'Public domain', 'CC BY 2.0', 'CC BY 3.0', 'CC BY 4.0', 'CC BY-SA 2.0', 'CC BY-SA 3.0', 'CC BY-SA 4.0', 'CC BY 2.5', 'CC BY-SA 2.5', 'CC BY 1.0'}
def curl(url, out=None, extra=()):
    cmd = ['curl', '-sS', '-L', '--max-time', '60', '-A', UA, *extra]
    cmd += ['-o', out, url] if out else [url]
    r = subprocess.run(cmd, capture_output=True, text=not out)
    return r.stdout if not out else (r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 5000)
def seen():
    s = set()
    if os.path.exists(MAN):
        for l in open(MAN, encoding='utf-8'):
            try: s.add(json.loads(l)['id'])
            except Exception: pass
    return s
def record(rec):
    with open(MAN, 'a', encoding='utf-8') as f: f.write(json.dumps(rec, ensure_ascii=False) + '\n')
def dims(p):
    try:
        from PIL import Image; im = Image.open(p); return im.width, im.height
    except Exception: return None, None
def openverse(q, n=20):
    url = f'https://api.openverse.org/v1/images/?q={urllib.parse.quote(q)}&license=cc0,pdm,by,by-sa&page_size={n}&size=large,medium'
    txt = curl(url)
    try: d = json.loads(txt)
    except Exception: print('openverse: bad response', txt[:120]); return
    have = seen(); got = 0
    for r in d.get('results', []):
        lic = r.get('license'); rid = 'ov_' + r['id']
        if lic not in ('cc0', 'pdm', 'by', 'by-sa') or rid in have: continue
        if (r.get('width') or 0) < 1000 and (r.get('height') or 0) < 1000: continue
        ext = 'jpg'; out = os.path.join(HERE, 'candidates', rid + '.' + ext)
        if curl(r['url'], out):
            w, h = dims(out)
            if not w: os.remove(out); continue
            record({'id': rid, 'file': os.path.relpath(out, HERE), 'source': 'openverse:' + r.get('source', ''), 'url': r['url'], 'page': r.get('foreign_landing_url'), 'author': r.get('creator'), 'license': f"CC {lic.upper()} {r.get('license_version', '')}".strip(), 'title': r.get('title'), 'w': w, 'h': h, 'query': q})
            got += 1; time.sleep(0.4)
    print(f'openverse {q!r}: {d.get("result_count")} results, {got} downloaded')
def commons(q, n=12):
    url = ('https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=' + urllib.parse.quote(q) +
           f'&gsrnamespace=6&gsrlimit={n}&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=2000&format=json')
    txt = curl(url)
    try: d = json.loads(txt)
    except Exception: print('commons: bad response', txt[:120]); return
    have = seen(); got = 0
    for p in d.get('query', {}).get('pages', {}).values():
        ii = (p.get('imageinfo') or [{}])[0]; em = ii.get('extmetadata', {})
        lic = em.get('LicenseShortName', {}).get('value', '')
        if lic not in OK_LIC or not ii.get('thumburl'): continue
        if not p['title'].lower().endswith(('.jpg', '.jpeg', '.png')): continue
        rid = 'wm_' + hashlib.md5(p['title'].encode()).hexdigest()[:10]
        if rid in have: continue
        out = os.path.join(HERE, 'candidates', rid + '.jpg')
        if curl(ii['thumburl'], out):
            w, h = dims(out)
            if not w: os.remove(out); continue
            record({'id': rid, 'file': os.path.relpath(out, HERE), 'source': 'wikimedia-commons', 'url': ii.get('url'), 'page': ii.get('descriptionurl'), 'author': re.sub('<[^>]+>', '', em.get('Artist', {}).get('value', ''))[:80], 'license': lic, 'title': p['title'], 'w': w, 'h': h, 'query': q})
            got += 1; time.sleep(0.4)
    print(f'commons {q!r}: {len(d.get("query", {}).get("pages", {}))} results, {got} downloaded')
def own():
    txt = curl('https://elmsnest.com/products.json?limit=50')
    d = json.loads(txt); have = seen(); got = 0
    for p in d['products']:
        for i, im in enumerate(p['images']):
            rid = f"own_{p['handle'][:40]}_{i+1}"
            if rid in have: continue
            src = im['src'].split('?')[0]
            out = os.path.join(HERE, 'own', rid + '.jpg')
            if curl(src + '?width=1600', out):
                w, h = dims(out)
                record({'id': rid, 'file': os.path.relpath(out, HERE), 'source': 'store-product-image', 'url': src, 'page': f"https://elmsnest.com/products/{p['handle']}", 'author': 'ElmsNest', 'license': 'store-owned', 'title': f"{p['title']} — image {i+1}", 'w': w, 'h': h, 'query': 'own'})
                got += 1; time.sleep(0.2)
    print(f'own: {got} downloaded')
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'openverse': openverse(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 20)
    elif cmd == 'commons': commons(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 12)
    elif cmd == 'own': own()
