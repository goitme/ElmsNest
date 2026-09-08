# Concept «install» — the photographs

Six internet photographs in the concept, at most three on any one page (A: soil · rain-panel · cells; B: plug · drops · wall; C: plug · rain-panel · cells). None is presented as the product: every frame carries a naming caption inside the section, and none shows a lamp of any brand. No faces, no brand marks, no baked text, no watermark, no colour filter. Crops are CSS only (`object-fit`/`object-position`; the soil frame a CSS zoom inside an `overflow:hidden` frame) — the files are untouched.

Note on the pool files: the `candidates/` files are now larger than their `manifest.jsonl` rows say (the originals were re-fetched after the shortlist was written): soil 1276×1276, rain-on-panel 1365×2048, drops 2047×1365, bougainvillea 3840×2881. The sizes below are the files as they are on disk today.

| # | id | file | author | licence | credit line as drawn | crop (390 / ≥ 901) | role | the sentence that says what it is |
|---|---|---|---|---|---|---|---|---|
| 1 | `ov_f726110a-04f8-4546-861e-5eb0af61a54b` (pdp3) | `../../images/candidates/ov_f726110a-….jpg` 1276×1276 | mypubliclands (BLM Idaho, Flickr) | CC BY 2.0 | צילום: mypubliclands (CC BY 2.0) | CSS zoom 189.6 % / 190 %, window x 15.6–68.4 % · y 34.2–79.4 % (phone 7:6) / x 21–73.6 % · y 34.2–100 % (desktop 4:5): both hands and the seedling, the boot at the top-right out of the window | install «stake» — hands pressing soil: the gesture of a stake going into the ground, no lamp | ידיים מהדקות אדמה |
| 2 | `d5cfca29-ca46-454e-bd51-5ead417396b5` (Openverse, NEW this concept) | `images/fetched/d5cfca29.jpg` 1024×680 ⚠ | anka.albrecht (Flickr) | CC BY 2.0 | צילום: anka.albrecht (CC BY 2.0) | `object-position` 58 % 55 % (phone: plug and screw, the plug's fluted tip cut) / 82 % 55 % (desktop 4:5: the whole screw, the plug's end) | install «wall» / «panel» / «screws» — a wall plug and a screw on a white ground: what fixing to a wall looks like, no lamp, no bracket of any brand | בורג ודיבל, מקרוב |
| 3 | `ov_dbe4a3f1-c6e9-4900-84ef-34a5c41e30b1` (pdp3) | `../../images/candidates/ov_dbe4a3f1-….jpg` 1365×2048 | h080 (Flickr) | CC BY-SA 2.0 | צילום: h080 (CC BY-SA 2.0) | 1:1 at 390 / 3:2 at ≥ 901, `object-position` 50 % 62 % (the lower cells with the larger drops) | weather, solar — rain on a solar panel: a material in weather, not a product | טיפות על פאנל סולארי |
| 4 | `wm_5869e6ea3a` (pdp3) | `../../images/candidates/wm_5869e6ea3a.jpg` 3840×2560 | Guilhem Vellut (Wikimedia Commons) | CC BY 2.0 | צילום: Guilhem Vellut (CC BY 2.0) | 1:1 / 3:2 centred | weather, solar — polycrystalline cells in hard sun, macro: reads as material; the blue is the «different colour» on the night page | תאים סולאריים בשמש, מקרוב |
| 5 | `ov_5795ed8a-cd8b-4588-9ae7-110f9a3ed0e4` (pdp3) | `../../images/candidates/ov_5795ed8a-….jpg` 2047×1365 | jenny downing (Flickr) | CC BY 2.0 | צילום: jenny downing (CC BY 2.0) | 1:1 / 3:2, `object-position` 38 % 50 % (the hanging drop) | weather, not solar — drops on a plant stem: «wet» without a lamp or a panel | טיפות על גבעול |
| 6 | `ov_7379ba54-775e-4044-b839-56ce83f7deb1` (pdp3) | `../../images/candidates/ov_7379ba54-….jpg` 3840×2881 | Carol M. Highsmith (Library of Congress via rawpixel) | CC0 1.0 | none (CC0) | 1:1 / 3:2, `object-position` 22 % 45 % (the white wall and the bougainvillea; the yellow house and the barred window stay out at 390, a strip of yellow enters at 3:2) | weather, not solar — a white wall in noon sun: Israeli to the eye, warm, no lamp | בוגנוויליה על קיר לבן, בשמש |

⚠ #2 is 1024 px as downloaded (the Flickr `_b`); the same photograph is on Wikimedia Commons at 4288×2848 as `File:Dübel Rawlplug (24097520989).jpg` (Openverse id `e7517c35-9faf-4aa8-a2c5-f07376fe918e`, page https://commons.wikimedia.org/w/index.php?curid=75147346) — Commons rate-limited this session (HTTP 429 on the original and on the API); `fetch.py` should take that file before `prepare-assets.py`. At 1024×680 it already exceeds the 900 px the theme would serve for the 440 px frame.

## The new photograph and the manifest

#2 is not in `../../images/manifest.jsonl` (the shortlist listed «wall bracket and two screws» as a gap and asked for a new search). It was found on Openverse this round with `license_type=commercial`, downloaded to this concept folder only (`images/fetched/d5cfca29.jpg`, plus the Openverse record in `images/fetched/records.json`), and its manifest row is written in `images/manifest.install.jsonl` for the lead to merge:

```
{"id": "ov_d5cfca29-ca46-454e-bd51-5ead417396b5", "file": "candidates/ov_d5cfca29-ca46-454e-bd51-5ead417396b5.jpg", "source": "openverse:flickr", "url": "https://live.staticflickr.com/1606/24097520989_e6b57f3e68_b.jpg", "page": "https://www.flickr.com/photos/134465805@N06/24097520989", "author": "anka.albrecht", "license": "CC BY 2.0", "title": "Dübel / Rawlplug", "w": 1024, "h": 680, "query": "wall plug screw", "commons_original": "https://commons.wikimedia.org/w/index.php?curid=75147346 (4288x2848, same photograph, CC BY 2.0, author credited as Anka Albrecht)"}
```

Rejected while searching the same gap (all seen): `efc46abc` «Red Rawl Plugs» (DaGoaty, CC BY 2.0) — a strip of plugs backlit, abstract, a shopper would not read it; `eb8c30a7` «Rawlplug» (Stewart Black, CC BY 2.0) — a single plug in a white wall, 1024², too empty at 4:5; `da5d960f` «Know the drill» (Keith Williamson, CC BY 2.0) — a drill chuck with brand lettering on the collar; `6c872ceb` «Tarugos» (Canopus49, CC BY-SA 4.0, 1600×1200) — not downloadable this session (429); IKEA shop shelf of screws (`4b1951d1`) — brand; `a88915eb`/`3208962b` (Yutaka Tsutano) — a guitar hanger and a speaker mount, other objects.

## Gaps kept honest

- «String on a hook» (decor): no licensed frame that is not another brand's string light — the «hook» variant is text-only by default; its `image_picker` takes an own frame of a plain hook on a pergola beam when the owner shoots one.
- «Rain on a lamp head»: none in the pool (the icy lantern is a lookalike); rain on a panel and drops on a stem carry the role.
- Dust: dropped from the copy.
- The «stake» gesture is hands on soil, not a stake — the caption says so; the store's own stake in soil (hands only) can replace it through the `image_picker` when shot.

## Slots in the theme (per BRIEF §4)

`elmsnest-s-pdp-install`: five `image_picker` settings (stake, wall, panel, screws, hook), each with a theme-asset default (`ens-pdp-install-soil.jpg` 900×900 ≈ 182 KB q80; `ens-pdp-install-plug.jpg` 1024×680 ≈ 28 KB) and a `text` credit setting pre-filled with the credit line above (the owner clears it when he picks his own frame). `elmsnest-s-pdp-weather`: four `image_picker` settings (rain-solar, sun-solar, rain-other, sun-other) with defaults `ens-pdp-weather-rain-panel.jpg` (800×1200 ≈ 159 KB), `ens-pdp-weather-cells.jpg` (1000×667 ≈ 175 KB), `ens-pdp-weather-drops.jpg` (1000×667 ≈ 68 KB), `ens-pdp-weather-wall.jpg` (1000×750 ≈ 186 KB), plus a credit text per slot. Every file ≤ 220 KB; `asset_img_url` candidates capped at the file's width (600/900 for the frame, 600/1000 for the tiles).
