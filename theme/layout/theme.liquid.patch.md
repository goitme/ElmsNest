# `layout/theme.liquid` — index preload patch

Target: theme `gid://shopify/OnlineStoreTheme/154726400174`, file `layout/theme.liquid` (fetched
2026-09-01, 8 701 bytes). One hunk inside `<head>`, in the `{%- if request.page_type == 'index' -%}`
branch. Everything else (the `product` branch with the K4 preload) stays as is.

## Why

The v1 hero assets `elmsnest-hero-{desktop,mobile}-performance.webp` are still preloaded for the index
template. SPEC §4.1 makes the hero background a **section setting** (`product` + `bg_image_index` /
`bg_image_index_mobile`, with `bg_image` / `bg_image_mobile` picker overrides) and §7 #6 bans the v1 webps
anywhere on the page — so with the current head every homepage visit downloads two photos nobody renders.

The layout cannot read `section.settings` of a section in `templates/index.json`, so the preload has to
re-derive the image the same way the hero does, from the same defaults that `templates/index.json` ships:
`stainless-steel-solar-path-light-ip65` `images[0]` for both viewports (§3.6). It is guarded with
`| default: product.featured_image` exactly like the section.

## BEFORE (the index branch right after the `settings.library_font == 'google'` block in `<head>`)

```liquid
    {%- if request.page_type == 'index' -%}
      <link rel="preload" as="image" href="{{ 'elmsnest-hero-mobile-performance.webp' | asset_url }}" media="(max-width: 749px)" fetchpriority="high">
      <link rel="preload" as="image" href="{{ 'elmsnest-hero-desktop-performance.webp' | asset_url }}" media="(min-width: 750px)" fetchpriority="high">
    {%- elsif request.page_type == 'product' -%}
```

## AFTER

```liquid
    {%- if request.page_type == 'index' -%}
      {%- comment -%}
        ElmsNest v2 (2026-09-01): preload the hero photo the elmsnest-v2-hero section renders.
        Keep the handle + index in sync with templates/index.json → env2_hero.settings
        (product / bg_image_index / bg_image_index_mobile). If the merchant sets the
        bg_image / bg_image_mobile picker overrides, delete this block — a mismatched preload
        is a double download, a missing one is harmless. Breakpoint 900px = the hero's <picture>.
      {%- endcomment -%}
      {%- liquid
        assign en_hero_pr = all_products['stainless-steel-solar-path-light-ip65']
        assign en_hero_desk = en_hero_pr.images[0] | default: en_hero_pr.featured_image
        assign en_hero_mob = en_hero_pr.images[0] | default: en_hero_pr.featured_image
      -%}
      {%- if en_hero_mob != blank -%}
        <link rel="preload" as="image" media="(max-width: 900px)" fetchpriority="high"
          href="{{ en_hero_mob | image_url: width: 1000 }}"
          imagesrcset="{{ en_hero_mob | image_url: width: 1000 }} 1000w, {{ en_hero_mob | image_url: width: 1400 }} 1400w"
          imagesizes="100vw">
      {%- endif -%}
      {%- if en_hero_desk != blank -%}
        {%- assign en_hero_widths = '900,1400,1800,2400' | split: ',' -%}
        {%- assign en_hero_sep = '' -%}
        {%- capture en_hero_srcset -%}
          {%- for en_w in en_hero_widths -%}
            {%- assign en_wn = en_w | plus: 0 -%}
            {%- if en_wn <= en_hero_desk.width -%}
              {{- en_hero_sep -}}{{ en_hero_desk | image_url: width: en_wn }} {{ en_wn }}w
              {%- assign en_hero_sep = ', ' -%}
            {%- endif -%}
          {%- endfor -%}
        {%- endcapture -%}
        <link rel="preload" as="image" media="(min-width: 901px)" fetchpriority="high"
          href="{{ en_hero_desk | image_url: width: 1800 }}"
          imagesrcset="{{ en_hero_srcset | strip }}"
          imagesizes="100vw">
      {%- endif -%}
    {%- elsif request.page_type == 'product' -%}
```

## How this matches the hero's own markup (so the browser reuses the preload)

`sections/elmsnest-v2-hero.liquid` renders:

```liquid
<picture>
  <source media="(max-width:900px)" srcset="{{ bg_mobile | image_url: width: 1000 }} 1000w, {{ bg_mobile | image_url: width: 1400 }} 1400w" sizes="100vw">
  {{ bg_desktop | image_url: width: 1800 | image_tag: loading: 'eager', fetchpriority: 'high', widths: '900,1400,1800,2400', sizes: '100vw', … }}
</picture>
```

A preload is only reused when the browser resolves `imagesrcset`/`imagesizes` to the **same candidate
URL** it picks for the `<img>`/`<source>`:

- **Mobile** — the `<source>` srcset is typed literally, so the preload repeats the same two candidates
  verbatim (`width=1000`, `width=1400`) and the same `sizes`.
- **Desktop** — `image_tag` with `widths:` silently drops any width larger than the image (the catalogue
  photos are 1254 px), so its srcset is *not* `900,1400,1800,2400` but only the widths ≤ 1254. The loop
  above reproduces that rule (same technique as the existing product-page preload), so the candidate list
  is identical. The `href` matches `image_url: width: 1800` (Shopify caps it to the native width, same
  URL as the `<img src>`).
- Both `<link>`s carry `media`, so only one photo is fetched per viewport. `(max-width: 900px)` /
  `(min-width: 901px)` follow the hero's `<source media>`; the old 749/750 split belonged to the v1 assets.

**Verify once on the preview:** Chrome DevTools → Console must not print
"The resource … was preloaded using link preload but not used within a few seconds", and Network must show
the hero photo requested once with priority *Highest*. If a warning appears, the hero's srcset and this
preload have drifted — diff the two `imagesrcset`/`srcset` strings.

## Alternative if the lead prefers zero coupling to `templates/index.json`

Delete the whole index branch (keep `{%- if request.page_type == 'product' -%}` as the first condition) and
let the hero's `loading:'eager'` + `fetchpriority:'high'` `<img>` — the first element in `<main>` — carry
the request. Cost: the photo is discovered by the preload scanner a few hundred bytes later than a head
preload, roughly one round-trip on a slow connection; benefit: nothing to keep in sync when the merchant
swaps the product or picks an override in the editor. The section could also emit its own
`<link rel="preload">` at the top of its markup (browsers honour preloads in `<body>`), which keeps the
URL in sync automatically — but it fires at the same time as the `<img>` and adds nothing.

## Optional one-liner in the same file

`<meta name="theme-color" content="#2B2118">` (in `<head>`, just before the canonical link) → `#020306` so mobile browser chrome matches the
night header on the homepage. Not required by §5; global to all pages.
