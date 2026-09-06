#!/usr/bin/env python3
"""Worst-case contrast of text painted over a photograph, from the real section shots (PDP round 2; generalised from
home2/verify/contrast.py — sizes.json keys are <section short name>-<viewport>, written by pdp2/shoot-sections.js).
  contrast.py [dir]      — every text box in <dir>/sizes.json (default: this folder)
For a box: text pixels = pixels within tol of the CSS colour; background = the rest of the box; the reported ratio is
text luminance vs the 90th-percentile background luminance (the brightest tenth of what sits behind the glyphs), i.e.
the local worst case WCAG would look at, not the average. ≥ 4.5 passes; 3–4.5 is the band to look at by eye.
When <dir>-bg/ exists (the same shots taken with --hide-text) the background is read from there — exact, no edge-pixel guess."""
import json, os, re, sys
from PIL import Image
HERE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
def lum(rgb):
    def c(v):
        v = v / 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb; return 0.2126 * c(r) + 0.7152 * c(g) + 0.0722 * c(b)
def ratio(a, b): a, b = sorted([a, b], reverse=True); return (a + 0.05) / (b + 0.05)
S = json.load(open(os.path.join(HERE, 'sizes.json')))
worst = None
for key, v in S.items():
    if v.get('missing') or not v.get('texts'): continue
    png = os.path.join(HERE, f'{key}.png')
    if not os.path.exists(png): continue
    im = Image.open(png).convert('RGB'); px = im.load()
    bgpng = os.path.join(HERE.rstrip('/') + '-bg', f'{key}.png')  # the same shot with the text hidden: the true background
    bgim = Image.open(bgpng).convert('RGB').load() if os.path.exists(bgpng) else None
    for t in v['texts']:
        m = re.findall(r'\d+', t['color']); col = tuple(int(x) for x in m[:3]); Lt = lum(col)
        bg = []
        x0, y0, x1, y1 = max(0, t['x']), max(0, t['y']), min(im.width, t['x'] + t['w']), min(im.height, t['y'] + t['h'])
        for y in range(y0, y1):
            for x in range(x0, x1):
                if bgim is not None:
                    bg.append(lum(bgim[x, y])); continue
                p = px[x, y]
                if sum(abs(p[i] - col[i]) for i in range(3)) < 90: continue  # glyph (or anti-aliased edge) pixel — approximate when no -bg shot exists
                bg.append(lum(p))
        if not bg: continue
        bg.sort(); p90 = bg[int(len(bg) * 0.9)]; p50 = bg[len(bg) // 2]
        r90 = ratio(Lt, p90)
        if worst is None or r90 < worst[0]: worst = (r90, key, t['cls'].split()[-1])
        print(f"{key:22s} {t['cls'].split()[-1]:26s} {t['text'][:18]:18s} rgb{col} {t.get('size','')} vs bg p50 {ratio(Lt, p50):5.2f}:1  p90 {r90:5.2f}:1  box {t['w']}x{t['h']}{'  (bg shot)' if bgim is not None else ''}")
if worst: print(f"worst p90: {worst[0]:.2f}:1 at {worst[1]} {worst[2]}")
