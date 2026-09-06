# Concept «dusk» — two frames

## The idea

One idea, twice: day and night. Section A puts the same place at two hours side by side — the store's own bollards by day (panel on the head, lamp off) and by night (lit) — and lets the headline live on the frames themselves: «ביום נטען.» on the day frame, «בלילה נדלק.» on the night frame. Three plain steps under the frames say the rest in one line each. Section B is the honest footnote to A: the cold-blue dusk photograph with «ובחורף?» and three lines — shorter sun, less light, better to know before ordering. Big serif on the image, nothing else.

Cinematic and quiet: no eyebrow, no button, no link, no card chrome. Numbers in gold serif as in the terms strip, hairlines from the fit block, so the sections sit in the page's existing rhythm: photo → tiles → cards → [A: photos + three lines] → fit (text) → [B: one photo] → terms (text).

## Where the sections go (`templates/index.json`)

- **[A] `elmsnest-s-home-dusk`** — after «מה שנדלק ראשון» (cards), before «מתי כן, ומתי לא» (fit). The buyer has seen where and what; A says how, in the time it takes to scroll one frame.
- **[B] `elmsnest-s-home-winter`** — after the fit block, before the terms strip. Fit ends on «which spot gets no sun»; B is the seasonal version of the same honesty, and it gives the page one breath of photograph between two text sections.

## Measured heights (playwright, `getBoundingClientRect`, fonts loaded)

| section | 390 × 844 | 1366 × 900 |
|---|---|---|
| [A] ens-home-dusk | **481 px** | 582 px |
| [B] ens-home-winter | **520 px** | 560 px |

Both ≤ 675 (0.8 screen). Page in the mockup at 390: 5342 px = 6.33 screens (was 5.12; the two sections add 1009 px incl. an 8 px margin) — under the 7.5 cap. Horizontal scroll width = 390, nothing bleeds.

## What it refuses

- A third section. Two frames is the concept; a «before you buy» trio or a light-kinds row would dilute it and repeat the tiles.
- Any product claim: no hours, no lumen, no IP, no «all our lights». Sentences 3–7 and 9–11 are category facts (COPY.md lists the source of each).
- A second guide link, a second contact line, a second product grid — none of the existing sections' questions is answered again.
- Editing images: crops are CSS only; the baked caption on the night frame is cropped out by the box, not retouched.
- Motion: none. No carousel, no parallax, no scroll-lamps, no hover reveal. Reduced-motion has nothing to switch off.
- A daylight photograph anywhere except inside the day/night pair.

## Engineering notes

- Stock patterns: a `<figure>` grid and an `<ol>`; one `<img>` per frame with `object-position` per breakpoint. Works with JS off.
- Night frame at 390 uses `height:116%` on the image (top-aligned) so the baked caption at y > 92 % is outside the box; at ≥ 901 px the 16:10 box drops it by itself.
- Text on images sits on a bottom scrim (`rgba(5,8,14,.72–.86)`); the day frame gets a slightly stronger scrim because the photo is bright. Cream on the scrim ≥ 7:1; the glow headline on the night scrim ≥ 8:1.
- Winter band is full-bleed (edge to edge) on both breakpoints; the copy is inside `.env2-wrap` on desktop and inside the gutter on phone.
- Liquid: every text and both images become section settings; `image_picker` empty → theme asset (`assets/ens-home-day.jpg`, `-night.jpg`, `-winter.jpg`), rendered with `asset_img_url` sizes and `loading="lazy"`.
- Weight: three JPEGs ≤ 220 KB each, below the hero, lazy.

## Risk the judges may raise

The day frame is the only bright image on a night page. That is the point of the pair — but if the owner finds it too bright, the scrim on the day frame can go up to `.85` at the bottom without losing the panel on the lamp head, or the day frame can be sized 4:5 → 1:1 at 390 to shrink its share of the screen.
