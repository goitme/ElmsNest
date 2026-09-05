# SIMPLIFY deploy log — dev theme 154726400174 (2026-09-05, 15:27–15:41 UTC)

All 23 files upserted through `themeFilesUpsert`, `userErrors: []` on the final attempt of each. Shopify normalises the
trailing newline, so a match is reported "as-is" or with one trailing newline added/removed. `snippets/elmsnest-v2-core.liquid`
was NOT part of this round and stays at `420c9994e18ecc64b071ae38b6090ffa` (the anchor-button fix of the morning).

| file | local bytes | remote bytes | remote md5 | local match |
|---|---|---|---|---|
| `config/settings_data.json` | 13575 | 9336 | `0306b35e516bce1e94afe3f95512662b` | content-identical; Shopify's own serialization |
| `layout/theme.liquid` | 11550 | 11550 | `2d26f6a1f210ab572219938c85d383d3` | as-is |
| `sections/elmsnest-s-coll-header.liquid` | 11189 | 11188 | `223d626e6b00b0e2b5135b19685cf78d` | no-trailing-nl |
| `sections/elmsnest-s-collections.liquid` | 5456 | 5455 | `04ec623451d75df624c60b6d60d0ce83` | no-trailing-nl |
| `sections/elmsnest-s-fit.liquid` | 5458 | 5457 | `0fa5cc27786918f408c15f6702911650` | no-trailing-nl |
| `sections/elmsnest-s-guide-strip.liquid` | 2532 | 2531 | `82eee05eab7ef527d084899c5593f8a8` | no-trailing-nl |
| `sections/elmsnest-s-pdp-facts.liquid` | 13307 | 13306 | `3f72e8cd28783dd88460633526053a19` | no-trailing-nl |
| `sections/elmsnest-s-products.liquid` | 4683 | 4682 | `50d52daf82b531a0d46d66ef2664526d` | no-trailing-nl |
| `sections/elmsnest-s-terms.liquid` | 1937 | 1936 | `6859f2e6ffc279bf723d46a8cb1ab631` | no-trailing-nl |
| `sections/elmsnest-v2-hero.liquid` | 16568 | 16568 | `952d8ec0c94379e600efe283969eb365` | as-is |
| `sections/footer-group.json` | 11417 | 11417 | `74c728992c7f18e0bc391b14278ed93b` | as-is |
| `sections/header-group.json` | 2307 | 2306 | `109c19fa36b2c97408313150b64c687c` | no-trailing-nl |
| `snippets/elmsnest-s-contact.liquid` | 2734 | 2733 | `0bb75b12cbd0ebc5a096fb92433e3a59` | no-trailing-nl |
| `snippets/elmsnest-s-pdp-kicker.liquid` | 2263 | 2262 | `50873ad521e42ae9867d17839b221553` | no-trailing-nl |
| `snippets/elmsnest-s-pdp-notfor.liquid` | 1310 | 1309 | `76394460628f55a12f88631fa78ac202` | no-trailing-nl |
| `snippets/elmsnest-s-pdp-terms-line.liquid` | 2961 | 2960 | `60ec158f2785b2cb836754c5a0916675` | no-trailing-nl |
| `snippets/elmsnest-s-pdp-unit.liquid` | 4958 | 4957 | `91af48eb9254f50ce7bdcb5ffdf26e84` | no-trailing-nl |
| `snippets/elmsnest-s-place.liquid` | 4289 | 4288 | `a8136f84015ac7ce3d64dea70cedf623` | no-trailing-nl |
| `snippets/elmsnest-s-skin.liquid` | 11958 | 11957 | `248deb9cd064e899cbc3fe7dc7befb90` | no-trailing-nl |
| `snippets/elmsnest-s-terms.liquid` | 6412 | 6411 | `0958dc359d82f086224cc060f4d56327` | no-trailing-nl |
| `templates/collection.json` | 1784 | 1783 | `1c2f738c4a4b73fe1219dc2848d5dfd7` | no-trailing-nl |
| `templates/index.json` | 3969 | 3968 | `d3e3ca695a54aa37d8fe2ccb18ece84b` | no-trailing-nl |
| `templates/product.elmsnest.json` | 9611 | 9610 | `c05e8d5737988631fad627b932f0b62b` | no-trailing-nl |

Mismatches: **0 in content, 1 in serialization.** `config/settings_data.json` is the one file Shopify re-serialises on
save: it reports 9,336 bytes and a checksum that no standard JSON serialisation of the local file reproduces (2/4-space,
compact, sorted, with and without the header comment — all tried). The stored body was fetched back in full and read:
key for key the same JSON — `show_ultra_btn: false`, `show_secondary_image: false`, the `scheme-env2-night` scheme, the
two sense-rtl app blocks and the `custom_css` are all there. The checksum column is therefore not a proof for this one
file; the fetched body is.

## Four Shopify rules learned on the way (each bounced a file once, fixed, re-sent)

1. A `url` setting may not carry a page path as `default` (fit `guide_link`, guide-strip `link_url`).
2. A `text` setting may not carry an empty `default` (pdp-facts `heading`).
3. A `richtext` setting refuses the `<bdi>` tag (footer_about, footer_bottom).
4. A `richtext` setting refuses `data-*` attributes on `<a>` (the four footer `data-ens-place` markers).
The header group's `note_mobile` is an HTML setting and accepted its `<bdi>`.

## Second pass (after the first verification), 2026-09-05 ~15:55 UTC

| file | remote bytes | remote md5 | why |
|---|---|---|---|
| `templates/collection.json` | 1784 | `3a6e2e1fb8571895df5f1212b8bd3481` | `space_items` "x" → "15": /all measured 8.15 screens against 8; 13 row gaps × 15 px saved |
| `snippets/elmsnest-s-skin.liquid` | 11977 | `8942a1278987878ee57cb92919d2ba18` | reduced-motion block `!important` (three Kalles card children kept a transition; all `display:none`, harmless, now silent) |

First verification, 390×844 JS on (before → after / target): home 10.32 → **5.18** / 6 · /collections/all 25.76 → **8.15** / 8 ·
path collection 17.98 → **3.82** / 8 · rope PDP 10.25 → **4.38** / 6 · path PDP 10.37 → **4.25** / 6 · deck PDP 9.89 → **4.18** / 6.
Zero glyph plates, zero Liquid errors, zero WhatsApp, one main form + one sticky form + one quantity input + a
`<noscript>` select per PDP, terms strip once on the home and none on collections, one terms line per PDP, one photo
line + one mailto per page body + one in the footer, the four collections in the same order in tiles / fit rows /
filter row / header / footer, 27/27 featured images on /all (checked on the live HTML; the mirror renames files), the
live add-to-cart reached the drawer with the chosen variant, and Shopify's own render of the rope light's second
variant carries its own price (99.90) and form id — the server half of the pill switch. Three verify.json readings
were harness artefacts and are recorded as such in SPEC §11.
