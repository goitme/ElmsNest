# ElmsNest — Homepage rebuild (2026-09-01)

Source of truth for the sections that make up the ElmsNest homepage. These files
are deployed to the Shopify theme **ElmsNest - Homepage Rebuild 2026-09-01**
(theme id `154726400174`, unpublished) via `themeFilesUpsert`.

## What this replaces

The previous homepage ran on five custom sections (`elmsnest-home-hero`,
`-trust`, `-places`, `-shop`, `-growth`) plus two disabled `custom-liquid`
blocks that duplicated the collection and product rows. Three faults were named
against it:

1. **It did not sell.** A visitor could reach the footer without seeing a
   product, a price, or a way to buy. Every path to purchase went through a
   collection page first.
2. **It read flat.** Brown-on-cream throughout, for a store whose product is
   light — which is only visible against dark.
3. **Too much text.** The terms strip printed four full paragraphs directly
   under the hero, and the guidance table spent four sentences per row.

## The five sections

| File | Ground | Job |
|---|---|---|
| `sections/elmsnest-hero.liquid` | night | One heading, one line, two links, three facts. |
| `sections/elmsnest-products.liquid` | paper | The shelf — image, name, price, buy. New. |
| `sections/elmsnest-collections.liquid` | night | Four tiles, one clause each. |
| `sections/elmsnest-places.liquid` | paper | «איפה צריך אור?» condensed to one clause per field. |
| `sections/elmsnest-terms.liquid` | night | Label + value; the legal detail moves into `<details>`. |

`templates/index.json` sets the order and the Hebrew defaults.

The grounds alternate deliberately: night → paper → night → paper → night. The
old page ran hero (night) then three paper sections in a row, which is how a
lighting store ended up looking like a brochure.

## Rules that outlive this rebuild

- **Every «לא מתאים כאשר» line must already be published** on
  `/pages/guide-garden-lighting` or `/pages/why-solar-lighting`. Shorten a
  published line; never write a new one. «מי אנחנו» commits to not presenting
  unverified information as fact, and a negative invented for a homepage tile
  is the easiest kind of claim to be wrong about.
- **No «best seller», «most popular» or review-count claims.** The store has one
  test order in its history. There is nothing to support those numbers.
- **Leave the hero image pickers empty.** `layout/theme.liquid` preloads
  `elmsnest-hero-{desktop,mobile}-performance.webp` for the index template; the
  hero renders those same assets by default. Setting a picker reintroduces the
  double download the old page had (asset preloaded, `shop_images` file
  rendered).
- **Square corners.** `button_radius`, `block_radius` and `pr_card_radius` are
  all `0` theme-wide. Rounding only the homepage would read as a different site.

## Deploying

Upsert each `sections/*.liquid` **before** `templates/index.json` — Shopify
rejects a template that references a section type with no file behind it.

## Known content gaps

Several catalogue featured images are marketing creatives with Hebrew text
baked into them rather than product photographs, so the shelf reads as a row of
banners. Fixed by curating a collection and pointing the products section at it,
or by replacing those featured images.
