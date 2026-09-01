# ElmsNest v2 — shared plumbing CONTRACT (for section builders)

Source: `theme/snippets/elmsnest-v2-{fonts,base,price,buy}.liquid`. Proof render: `brief/build-preview/_base.html` (+ `_base-*.png`).
Only **elmsnest-v2-hero** renders the first two, at the very top of its markup, in this order:
`{% render 'elmsnest-v2-fonts' %}{% render 'elmsnest-v2-base' %}`. Every other section assumes they exist and still degrades (see JS).

## Section root (every section)
```html
<section id="env2-<name>" data-env2-<name> class="env2-section" dir="rtl" style="scroll-margin-top:90px;--env2-stars:.3">
  <div class="env2-stars" aria-hidden="true"></div>   <!-- only places/switch/atmosphere/terms/goodnight; opacity .18/.30/.45/.55/.70 -->
  <div class="env2-wrap">…</div>                        <!-- min(1240px, 100% - 2*gut); .env2-wrap--wide = 1500px -->
</section>
```
`.env2-section` = transparent background, ink colour, Heebo 300 15px/1.55, RTL, `overflow-x:clip`, resets `img/a/bdi/:focus-visible` inside it. Never paint a section background (only night-wall paints its photo). The Kalles header is transparent over the hero: the hero is the first `.shopify-section` child, starts at top 0, and clears the bar with its own `padding-top` (≥120px desktop / 96px mobile).

## CSS custom properties (on `:root`)
`--env2-sky-0..4` (#4a6a9c #1f3357 #0f1a2f #070b15 #020306) · `--env2-ink` #f4eee3 · `--env2-ink-2` #c9c4b8 · `--env2-mute` #8f95a3 (only on sky-2 or darker) · `--env2-gold` #e9b96e · `--env2-glow` #ffd394 · `--env2-ember` #f7a24a (halos only) · `--env2-btn-ink` #1a1206 · `--env2-hair` rgba(244,238,227,.12) · `--env2-hair-btn` .25 · `--env2-hair-num` .45 · `--env2-scrim` rgba(5,8,14,.55) (+ your own `backdrop-filter:blur(10px)`) · `--env2-gut` clamp(20px,4vw,64px) · `--env2-w` 1240px · `--env2-serif` / `--env2-sans` (from fonts) · `--env2-p` 0…1 scroll progress, written by JS on `<html>` (alias `--p`); use it as `filter:brightness(max(.45, calc(1 - 2.2*var(--env2-p))))`.

## Shared classes (do not restyle; size/position from your own `.env2-<section>__…` selectors)
| Class | What it is | Example |
|---|---|---|
| `.env2-h` | display heading: FRL 700, lh .98, ls −.01em, balance; `<em>` or `.env2-glow` inside = glow colour | `<h2 class="env2-h env2-first__h2">מה שנדלק ראשון</h2>` (you set font-size) |
| `.env2-lead` | Heebo 300 clamp(17,1.4vw,21), 38ch, ink-2 | `<p class="env2-lead">…</p>` |
| `.env2-eyebrow` | gold 34px rule + tracked 12px label (flex); `.env2-eyebrow--ink` = ink text (hero) | `<p class="env2-eyebrow">01 · נדלקים עכשיו</p>` |
| `.env2-kicker` | 11px tracked gold label, no rule | `<span class="env2-kicker">קיר · להאיר נקודה מסוימת</span>` |
| `.env2-price` | FRL 500 tabular glow, nowrap; size via `--env2-price-size` (default 24px) | `.env2-wall__price .env2-price{--env2-price-size:34px}` |
| `.env2-btn` / `.env2-btn--ghost` / `.env2-btn--sm` | pill (999px) glow / outlined ghost / 10×16 small; works on `<a>` and `<button>` | `<a class="env2-btn env2-btn--ghost" href="…">לשלוח תמונה</a>` |
| `.env2-link` | 14px ink-2 hairline-underlined link, hover glow; optional 14px svg arrow | `<a class="env2-link" href="/collections/all">לכל 27 המוצרים ←</a>` |
| `.env2-hair` | `<hr class="env2-hair">` hairline rule | |
| `.env2-serif` | just the serif face | |
| `.env2-stars` | absolute star layer, `opacity:var(--env2-stars,.25)` set on the section root | see above |

## The lamp device — `[data-lamp]`
```html
<div class="env2-first__item" data-lamp>
  <div class="env2-ph env2-first__ph"><div class="env2-halo"></div><img …></div>   <!-- .env2-halo / .env2-pool optional -->
</div>
```
States: no JS → `--lit:1` (lit). `html.env2-js` (added by base line 1) → `--lit:0` (photo 22 % brightness, halo off) until `.lit` is added → `--lit:1`, 1.6 s filter curve. Never removed. `[data-lamp="manual"]` is skipped by the observer — the section lights it itself with `env2.light(el)` (e.g. the "לא." h2, 40 % threshold). Your own effects read `var(--lit,1)` (e.g. numeral stroke → fill, word drop-shadow, garden opacity). Keyframes provided: `env2-lamp-on` (.55 s flicker-on), `env2-flick` (.24 s). Reduced motion: every lamp lit (also manual), transitions off, `--env2-p` stays 0.

## JS API — `window.env2` (defined by base, runs before your `{% javascript %}` bundle)
`env2.observe(root)` — idempotent; registers every `[data-lamp]` under `root` (or `root` itself) with one shared IntersectionObserver (threshold .25, rootMargin `0 0 -6%`) + a scroll sweep; safe to call per section and again after `shopify:section:load`. Base already calls `observe(document)` on DOMContentLoaded and on section load.
`env2.light(el)` · `env2.sweep()` · `env2.rm` (boolean, prefers-reduced-motion) · anchors `a[href^="#env2-"]` scroll smoothly (instant under rm).
**Every section's JS ends with:**
```js
document.querySelectorAll('[data-env2-<name>]').forEach(function(el){ /* init */
  window.env2 ? env2.observe(el) : el.querySelectorAll('[data-lamp]').forEach(function(l){ l.classList.add('lit'); });
});
```

## Snippet call signatures
`{% render 'elmsnest-v2-price', product: product %}` → `<span class="env2-price"><bdi>169.90</bdi> ₪</span>` · narrow range (max ≤ min×1.25) `<bdi>219.90–252.90</bdi> ₪` · else `מ־<bdi>89.90</bdi> ₪`. Nothing if product blank.
`{% render 'elmsnest-v2-buy', product: product, label: 'לבחירת גוון', small: true %}` → one available variant: `<form class="env2-buy" method="post" action="{{ routes.cart_add_url }}">` (hidden id, quantity=1, `<button class="env2-btn">הוספה לסל</button>`; `add_label:` overrides); several variants: `<a class="env2-btn env2-btn--ghost" href="product.url">label | default 'לבחירת דגם'</a>`; sold out: same link, default `לעמוד המוצר`. `small: true` → `.env2-btn--sm` (hero card).

## Rules that the base enforces or expects
Prefix everything `.env2-<section>__…`; no Liquid inside `{% stylesheet %}`/`{% javascript %}`; Latin/numbers in `<bdi>`; radius 0 except pills; logical properties; product titles in `var(--env2-sans)` never the serif; WhatsApp: `{%- assign wa = settings.whatsapp_number | default: '' | remove: ' ' | remove: '-' | remove: '+' -%}` → `https://wa.me/{{ wa }}?text={{ 'שלום, אשמח לבדוק התאמה — מצרף/ת תמונה של המקום.' | url_encode }}`, else `/pages/contact-us`.
Lead to verify on the live preview: the body class Kalles stamps on the index (`template-index` and `hdt-page-type-index` are both targeted) and that no other Kalles wrapper paints cream between sections.
