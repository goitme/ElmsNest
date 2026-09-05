# Fix log — SIMPLIFY round (fixer, 2026-09-05)

Running log; each applied finding gets a line when its edit is done and re-read.

## home group
- [x] skin header trim: theme/snippets/elmsnest-s-skin.liquid lines 5-7 of the comment deleted → 11,958 bytes (was 12,254).
- [x] collections: `assign img = col.image` (featured_image fallback dropped).
- [x] collections: `alt` no longer `| escape`d (image_tag escapes).
- [x] collections + fit: fixed ids dropped; h2 id / aria-labelledby suffixed `-{{ section.id }}`; aria-labelledby only when heading != blank, else aria-label = the schema heading default.
## pdp group
- [x] pdp-facts: whole-token `<bdi dir="ltr">` wrap (Latin/digit-initial tokens + bare `& &amp; + /` connectors, adjacent isolates merged) → range isolator → dir attribute, for both the `<dd>` values and the numeral caption; per-code replace loop and `replace: giant, giant_bdi` dropped; `latin` list kept for the IP giant pick; `latin_chars` constant added at line 42.
- [x] pdp-facts: `{{ heading | escape }}`, `{{ more_label | escape }}`; schema default of `heading` → "".
- [x] pdp-unit: `ens_any` pre-computed over product.variants; container gated on it (nothing renders for «יחידה אחת»).
- [x] pdp-kicker: `collections[handle]` → loop over product.collections; header comment; 44px hit area (`position:relative` + `::before inset-block:-15px`); elmsnest-s-place comment line 9 updated.
- [x] pdp-terms-line: `position:relative` + `::before inset-block:-11px`.
## collection group
- [x] coll-header: `data-ens-place="all"` dropped from the «כל המוצרים» pill; comment line 6 updated.
- [x] products: `collections.all.products` fallback deleted; aria-labelledby now conditional on heading.
- [x] guide-strip: `.ens-gs{background:#020306;…}`.
## templates / edited / interfaces
- [x] product.elmsnest.json: ens_pdp_facts.heading → "" (JSON parses).
- [x] index.json «הגינה נדלקת.»: NOT changed (LEAD-DECISIONS: keep the period); exemption written into SPEC.md P4 (line 64-65) and §6.1 (line 194).
- [x] hero: the two editor labels edited per LEAD-DECISIONS (line 245 «כפתור משני — טקסט», line 246 «קישור חיצוני לכפתור המשני (ריק = קישור הדוא״ל לשליחת תמונה)»); id `whatsapp_url` and the `wa.me` code path untouched; SPEC §10 hero note amended.
- [x] layout/theme.liquid: the simplify comment line deleted; diff vs baseline = the single skin render line.
- [x] footer-group.json: `data-ens-place="<handle>"` on the four «קולקציות» anchors (JSON parses).
## verification
- liquidjs 10 simulation of the pdp-facts loop (13 sample bullets incl. 800mAh, 54 LED, 12×2, AC 85–265V, Up &amp; Down, 5–22) and a full render of the section with a mocked product: every Latin/number token sits in one `<bdi dir="ltr">`, ranges keep their isolate, blank heading renders nothing.
- `python3 brief/lint.py theme` → LINT OK (0 issues) after all edits.
- deploy mirrors regenerated with deploy-prep.py (22 files) so brief/side-pages/simplify/deploy/* match theme/.
## deliberately not applied
- index.json:23 terminal period (two findings): kept per LEAD-DECISIONS; SPEC exemption added instead.
- hero `whatsapp_url` id / `wa.me` code path: left untouched per both findings' own advice (renaming breaks saved values, exceeds §10).
- "verify on the preview after upsert" for the footer richtext attributes: cannot be done here (no deploy from this container).
