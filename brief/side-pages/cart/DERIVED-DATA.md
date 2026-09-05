# What the cart can actually derive from `variant.title` (measured, 2026-09-05)

Source: `https://elmsnest.com/products.json?limit=250` — 27 products, 172 variants, read live.
This exists because BRIEF §1 offers "the basket is an amount of light" as the strongest idea available, and an
idea that is blank on most baskets is not an idea. **Check this table before specifying any derived number.**

| product | variants | metres | bulbs | units |
|---|---|---|---|---|
| `dual-head-garden-light-10w-ip65` | 1 | — | — | — |
| `powerful-solar-garden-light` | 1 | — | — | **all** |
| `swaying-solar-path-lights-ip65` | 2 | — | — | **all** |
| `rechargeable-telescopic-camping-lantern` | 1 | — | — | — |
| `modern-led-bollard-light-5w-ip65` | 1 | — | — | — |
| `waterproof-solar-deck-step-lights` | 4 | — | — | **all** |
| `solar-garden-lantern-9-led` | 1 | — | — | — |
| `solar-crystal-ball-string-lights` | 24 | **all** | **all** | — |
| `solar-edison-string-lights` | 2 | **all** | **all** | — |
| `solar-rope-string-lights` | 16 | **all** | **all** | — |
| `solar-firefly-garden-lights` | 1 | — | **all** | — |
| `lighted-birch-branches-20-led` | 2 | — | — | — |
| `led-globe-string-lights` | 30 | **all** | **all** | — |
| `decorative-led-net-lights` | 30 | **all** | **all** | — |
| `solar-security-light-100-led` | 1 | — | — | — |
| `solar-floodlight-ip67-remote-timer` | 3 | — | **all** | — |
| `modern-solar-path-lights-set` | 2 | — | — | **all** |
| `solar-garden-spotlight-52-led` | 4 | — | — | **all** |
| `modern-led-wall-light-6w-up-down` | 8 | — | — | 4/8 |
| `modern-led-wall-light-indoor-outdoor` | 8 | — | — | — |
| `waterproof-led-wall-light-ip65-6w-12w` | 8 | — | — | — |
| `outdoor-bidirectional-led-wall-light-ip65` | 4 | — | — | — |
| `magnetic-rechargeable-touch-wall-light` | 2 | — | — | — |
| `retro-solar-path-lights-set` | 3 | — | — | **all** |
| `warm-solar-step-deck-lights` | 8 | — | — | **all** |
| `stainless-steel-solar-path-light-ip65` | 1 | — | — | — |
| `solar-wall-light-motion-sensor-ip65` | 4 | — | — | **all** |
| **total** | **172** | **102 variants / 5 products** | **106 / 7** | **32 / 8** |

## What this means

- **Metres exist on 5 of 27 products.** They are concentrated entirely in the string-light family. A basket of
  a path light and a wall light — the store's two biggest categories — yields **no metres at all**. A drawer whose
  headline is a metre count is blank or wrong on the majority of real baskets.
- **Bulb counts exist on 7 of 27** and cover the same family plus the firefly string and the floodlight.
- **Units exist on 8 of 27**, and `cart.item_count` already counts units without parsing anything. "3 פריטים"
  is always true; "12 מטר" usually is not available.
- `1.5×1.5 מ׳` (the LED net) is an **area**, not a length. Summing it into a metre total would be a false number.
  Any parser must either special-case `×` or exclude it.

## The ruling this forces

A derived light-measure may be used **per line**, where it is true and visible in the variant the buyer chose, and
**never as a basket headline**, because the headline would be empty on most baskets and would silently drop the
wall lights and path lights that make up the bulk of the catalogue. If a concept's whole idea is the basket
headline, the idea does not survive contact with this catalogue.

Liquid, for the per-line case (no metafield needed, no `split` on a regex — Liquid has none):

```liquid
{%- comment -%} metres: the variant title's first token before מ׳, only when it has no × {%- endcomment -%}
{%- assign vt = item.variant.title -%}
{%- unless vt contains '×' -%}
  {%- if vt contains 'מ׳' -%}
    {%- assign env2_m = vt | split: 'מ׳' | first | split: '/' | last | strip -%}
  {%- endif -%}
{%- endunless -%}
{%- if vt contains 'נורות' -%}
  {%- assign env2_b = vt | split: 'נורות' | first | split: '/' | last | strip -%}
{%- endif -%}
```

Both assignments are strings, so they may be **printed** next to their unit but must not be summed unless they are
passed through `| times: 1` and the sum is shown only when every line contributed one.
