# QUIET — the photographs

Four photographs for seven pages. Three of them are drawn in `index.html`; the fourth belongs to the
contact page, which the deliverable does not render. Every crop is CSS `object-fit: cover` +
`object-position` on the untouched original file — no editing, no filter, no text baked in.
Sources and licences: `../../../pdp3/images/SHORTLIST.md` and `manifest.jsonl`.

---

## 1. Guide — `ov_b59b37d7-b683-414d-ab57-8aa936fd6833`

| field | value |
|---|---|
| file | `../../../pdp3/images/candidates/ov_b59b37d7-b683-414d-ab57-8aa936fd6833.jpg` — <bdi dir="ltr">2048×1362</bdi> |
| author | Jeremy Levine Design |
| licence | CC BY 2.0 (Flickr) — source `https://www.flickr.com/photos/25186605@N04/3640914366` |
| credit as drawn | «צילום: Jeremy Levine Design (CC BY <bdi dir="ltr">2.0</bdi>)» — 11.5 px, muted, under the caption |
| crop | full bleed. 390×320 at mobile (`object-position: 50% 62%`, horizontal crop only, 81 % of the width kept); 1366×460 at desktop (vertical crop, the same 62 % keeps gravel, table, doorway and the potted tree, drops the top sky) |
| role | «content: guide» — the place, after the four collections |
| page | guide, between `01 · איפה צריך אור?` and `02 · מה האור צריך לעשות?` |
| why it cannot read as the store's product | there is no lamp in the frame. The only light is a window and a doorway of the house. The caption names it as a place («חצר אחת בשעת בין ערביים») and the four labels under it point at gravel, wall, a potted tree and furniture — never at a light fitting. The credit names a photographer, so it reads as someone's yard, not a catalogue frame. |

## 2. About — `ov_7379ba54-775e-4044-b839-56ce83f7deb1`

| field | value |
|---|---|
| file | `../../../pdp3/images/candidates/ov_7379ba54-775e-4044-b839-56ce83f7deb1.jpg` — <bdi dir="ltr">3840×2881</bdi> (the shortlist's 1024 px note is stale, the file on disk is the large original) |
| author | Carol M Highsmith |
| licence | CC0 1.0 — source `https://www.rawpixel.com/image/582428/carol-highsmiths-arizona-photograph` |
| credit as drawn | «צילום: Carol M Highsmith (CC0 <bdi dir="ltr">1.0</bdi>)» — **the licence needs none**; drawn anyway, on the same caption line, because a page that says «כאשר מידע אינו מאומת, איננו צריכים להציג אותו כעובדה» should name its sources |
| crop | a tall slice beside the h1. 128×296 at mobile (`--op: 5% 62%` → the white wall, the bougainvillea and the gravel; the yellow wall stays out); 300×400 at desktop (`--op-d: 0% 55%`, a wider slice that lets the yellow corner in) |
| role | «content: about» — the outside itself, beside «רק תאורת חוץ. וזה בכוונה.» |
| page | about, in the h1 row |
| why it cannot read as the store's product | a wall, a shrub and gravel at noon. Nothing manufactured is in the frame, and the caption names the three things that are («קיר, שיח וחצץ באור צהריים»). It is the only warm colour on the page, which is the job: the store sells light for places like this one. |

## 3. Why solar — `wm_701ca719a2`

| field | value |
|---|---|
| file | `../../../pdp3/images/candidates/wm_701ca719a2.jpg` — <bdi dir="ltr">3840×2560</bdi> |
| author | Bastique |
| licence | CC BY 4.0 (Wikimedia Commons) — source `https://commons.wikimedia.org/wiki/File:Solar_Panels_on_Church_Roof.jpg` |
| credit as drawn | «צילום: Bastique (CC BY <bdi dir="ltr">4.0</bdi>)» — 11 px, muted, under the caption in the photo column |
| crop | a column beside the three beats, stretched to their height. 126 px wide at mobile, 300 px at desktop, `object-position: 62% 55%` — glass, busbars and the sun, the pines and the sky left at the top edge |
| role | «solar cell in sun» / «content: why solar» — the mechanism |
| page | why-solar, beside «איך זה עובד בפועל» |
| why it cannot read as the store's product | it is a roof array, not a garden light: no lamp head, no stake, no housing. The caption calls it what it is — «תאים סולאריים באור יום» — and it sits beside the sentence «הפאנל הסולארי נטען מאור היום», so it illustrates the mechanism the page explains, not an item for sale. |

## 4. Contact — `wm_241425af37` *(planned; the contact page is not in this render)*

| field | value |
|---|---|
| file | `../../../pdp3/images/candidates/wm_241425af37.jpg` — <bdi dir="ltr">3840×2560</bdi> |
| author | Swphotouk |
| licence | CC BY 4.0 (Wikimedia Commons) — source `https://commons.wikimedia.org/wiki/File:Kew_Gardens_Mediterranean_Garden_03.jpg` |
| credit as drawn | «צילום: Swphotouk (CC BY <bdi dir="ltr">4.0</bdi>)» |
| crop | a <bdi dir="ltr">16:9</bdi> band above the email line, `object-position: 50% 60%` — flagstone path and grasses, the grey sky excluded |
| role | «content: contact» — an example of the photograph the page asks the visitor to send |
| page | contact, above «דוא״ל: info@elmsnest.com» |
| why it cannot read as the store's product | a path with no lamp on it, captioned «גינה ים־תיכונית באור יום — תמונה כזאת מספיקה לנו». It is a picture of the *kind of picture we want*, which is the one thing the contact page is for. |

---

## Pages with no photograph, and why

- **FAQ**, **processing-time**, **shipping-delivery**. These pages answer with numbers and rules. A
  garden beside «<bdi dir="ltr">1–3</bdi> ימי עסקים» decorates, it does not inform, and the concept's
  whole claim is the fewest images that make it real. They keep the same typography, the same
  hairlines and the same one gold pill, so they still read as the same family.

## Weight and delivery (as shipped)

Every photograph becomes a theme asset (`assets/ens-page-guide.jpg`, `-about.jpg`, `-why.jpg`,
`-contact.jpg`), re-encoded to ≤ <bdi dir="ltr">1800</bdi> px on the long side and ≤ <bdi dir="ltr">220</bdi> KB,
with an `image_picker` override per page. One photograph per page, so nothing needs a second request:
the About frame is `loading="eager" fetchpriority="high"` (it is in the h1 row, above the fold at
390); the guide, why-solar and contact frames are `loading="lazy" decoding="async"` and sized with
`width`/`height`, so nothing shifts.

No faces (the two distant figures that the shortlist flagged in other frames are not in any of these
four), no brand marks, no baked text, no heavy filters, no store product in any frame.
