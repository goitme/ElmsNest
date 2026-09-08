# Shopify content backup — 2026-09-08

Verbatim, read-only capture of every Shopify-hosted text that may be edited next, so any change can be reverted exactly.

- **Captured:** 2026-09-08
- **Shop:** ElmsNest — `vcw4sm-r3.myshopify.com` / https://elmsnest.com (Shop id `68949278894`)
- **Method:** Shopify Admin GraphQL reads only. No mutation was issued.
- **Format:** each file is the unmodified GraphQL response object (`{"data": …}`), pretty-printed with `json.dump(..., ensure_ascii=False, indent=1)` so Hebrew and Arabic stay readable in git diffs.

## Files

| File | Bytes | Holds | Objects |
| --- | ---: | --- | ---: |
| `policies.json` | 20,833 | All five shop policies (`id`, `type`, `title`, `body`, `url`) — contact info, privacy, refund, shipping, terms | 5 |
| `pages.json` | 9,982 | Every Shopify page (`id`, `handle`, `title`, `body`, `bodySummary`, `templateSuffix`) | 8 |
| `products.json` | 249,461 | Every product with customer-readable fields: `descriptionHtml`, `productType`, `vendor`, `tags`, `status`, `seo`, up to 40 metafields each, up to 15 media each (with `alt` and image URL/size) | 27 |
| `collections.json` | 3,980 | Every collection (`id`, `handle`, `title`, `descriptionHtml`, `seo`) | 5 |
| `shop.json` | 488 | Shop identity: name, emails, myshopify domain, primary domain, billing address | 1 |

Every product carries a `custom.faq` JSON metafield; product-page shipping copy lives there, not in `descriptionHtml`.

## Where the watched strings occur

30 occurrences across the five files. `Count` is the number of times the string appears inside that one field.

| String | File | Object (handle / type + id) | Field | Count |
| --- | --- | --- | --- | ---: |
| «מחוץ לישראל» | `pages.json` | shipping-delivery (104093417646) | `body` | 1 |
| «מחוץ לישראל» | `policies.json` | PRIVACY_POLICY (32294797486) | `body` | 2 |
| «מחוץ לישראל» | `policies.json` | SHIPPING_POLICY (34732933294) | `body` | 1 |
| «חבילות נפרדות» | `pages.json` | shipping-delivery (104093417646) | `body` | 1 |
| «חבילות נפרדות» | `policies.json` | SHIPPING_POLICY (34732933294) | `body` | 2 |
| «7–14» | `pages.json` | processing-time (104095449262) | `body` | 1 |
| «7–14» | `pages.json` | processing-time (104095449262) | `bodySummary` | 1 |
| «7–14» | `pages.json` | shipping-delivery (104093417646) | `body` | 1 |
| «7–14» | `policies.json` | SHIPPING_POLICY (34732933294) | `body` | 1 |
| «7–14» | `policies.json` | TERMS_OF_SERVICE (34732671150) | `body` | 1 |
| «7–14» | `products.json` | solar-wall-light-motion-sensor-ip65 (9196178604206) | metafield `custom.faq` (json) | 1 |
| «8–17» | `pages.json` | processing-time (104095449262) | `body` | 1 |
| «8–17» | `pages.json` | processing-time (104095449262) | `bodySummary` | 1 |
| «8–17» | `pages.json` | shipping-delivery (104093417646) | `body` | 1 |
| «8–17» | `policies.json` | SHIPPING_POLICY (34732933294) | `body` | 1 |
| «8–17» | `policies.json` | TERMS_OF_SERVICE (34732671150) | `body` | 1 |
| «8–17» | `products.json` | solar-wall-light-motion-sensor-ip65 (9196178604206) | metafield `custom.faq` (json) | 1 |
| «1–3» | `pages.json` | processing-time (104095449262) | `body` | 1 |
| «1–3» | `pages.json` | processing-time (104095449262) | `bodySummary` | 1 |
| «1–3» | `pages.json` | shipping-delivery (104093417646) | `body` | 1 |
| «1–3» | `policies.json` | SHIPPING_POLICY (34732933294) | `body` | 1 |
| «1–3» | `policies.json` | TERMS_OF_SERVICE (34732671150) | `body` | 1 |
| «1–3» | `products.json` | solar-wall-light-motion-sensor-ip65 (9196178604206) | metafield `custom.faq` (json) | 1 |
| «17 ימי עסקים» | `policies.json` | SHIPPING_POLICY (34732933294) | `body` | 2 |
| «17 ימי עסקים» | `policies.json` | TERMS_OF_SERVICE (34732671150) | `body` | 1 |
| «17 ימי עסקים» | `products.json` | solar-wall-light-motion-sensor-ip65 (9196178604206) | metafield `custom.faq` (json) | 1 |
| «United Kingdom» | `policies.json` | CONTACT_INFORMATION (34732998830) | `body` | 1 |
| «(أو ضع» | `policies.json` | CONTACT_INFORMATION (34732998830) | `body` | 1 |
| «(إضافة» | `policies.json` | CONTACT_INFORMATION (34732998830) | `body` | 1 |
| «(إن وجد» | `policies.json` | CONTACT_INFORMATION (34732998830) | `body` | 1 |

### Strings with no occurrence

- **«ממחסן»** — 0 hits in all five files. The shipping copy uses the plural **ממחסנים** (regular nun), which does not contain the singular form ending in final nun (ן). It occurs once in `policies.json` (SHIPPING_POLICY `body`) and once in `pages.json` (`shipping-delivery` `body`) as `ממחסנים מחוץ לישראל` — search for `ממחסנ` (no final nun) to catch both.

### Notes for any future edit

- The delivery numbers **1–3 / 7–14 / 8–17 / 17 ימי עסקים** are stated in five places that must stay consistent: SHIPPING_POLICY, TERMS_OF_SERVICE, the `shipping-delivery` page, the `processing-time` page (in both `body` and `bodySummary`), and the `custom.faq` metafield of `solar-wall-light-motion-sensor-ip65`.
- All en-dashes above are U+2013 (–), not hyphens. `pages.json` also wraps them in `<bdi dir="ltr">` tags.
- The four Arabic placeholders and `United Kingdom` are all in one object: the CONTACT_INFORMATION policy `body` (id `34732998830`).
- `pages.json` `bodySummary` is Shopify-generated and truncated with `...`; it is stored as returned and is not independently editable.
- `accessibility-statement` also carries unfilled `[[...]]` placeholders (coordinator name, phone, response days, date), outside the watched string list.
