# Home round 2 — deploy log (dev theme `gid://shopify/OnlineStoreTheme/154726400174` only)

## Assets, 2026-09-06 ~08:06 UTC — `themeFilesUpsert` with `body: {type: URL}`

The four photographs are theme assets, fetched by Shopify from the repository (the branch is publicly readable
on raw.githubusercontent.com — which also means everything committed to this repo is public; the Mapbox token file
stays gitignored). A URL upsert returns an empty `upsertedThemeFiles` and no error: Shopify fetches asynchronously;
the file query a few seconds later shows the result. Every checksum equals the local file's md5 byte for byte.

| asset | bytes | md5 | source frame (store-owned) |
|---|---|---|---|
| `assets/ens-home-day.jpg` | 294319 | `1fa13f5252888ec0884faf21a1bd055b` | powerful-solar-garden-light image 3 |
| `assets/ens-home-night.jpg` | 290687 | `6491723bbb6e109908003f8c114178ce` | powerful-solar-garden-light image 2, top 1090 px |
| `assets/ens-home-winter.jpg` | 164984 | `36457edab3d82f958a7ba51a33f8cb63` | modern-solar-path-lights-set image 6, crop 150,450 → 1100×580 |
| `assets/ens-home-fence.jpg` | 249301 | `693a408d7cd280613a9780e32de8efaf` | solar-crystal-ball-string-lights image 5 |

Also on the theme: `assets/ens-test.png` (75 B, the upload-path probe of 06:34) — `themeFilesDelete` is refused by
the tool's safety policy, so it stays until the owner removes it in the theme editor; it is referenced nowhere.
