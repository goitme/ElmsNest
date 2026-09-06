# PDP round 2 — the lead's rulings on the critique of the deployed render (2026-09-06, written BEFORE the fixes)

Five lenses on the real dev-theme renders (`workflows/pdp2-critique.js`, `critique/RESULT.json`): shopper 6 · owner 6 ·
honesty 4 · designer 6 · engineer 7 — 30 findings, one skeptic each (evidence + scope). Skeptic votes: 15 confirmed,
15 refuted. The lead's rulings below decide what is fixed in pass 2, what is kept with a reason, and what goes to the owner.

## Fixed in pass 2

| # | finding (lens/id, skeptic) | ruling |
|---|---|---|
| 1 | **The rope photograph carries the baked «עמידות IP65 / מתאימות לשימוש חוץ» badge** (S1, O1, H1, D1, E1 — all five lenses; skeptics confirmed 0.95–0.96) | **Confirmed, blocker, mine.** My pre-crop (y 210) was read off a 455 px thumbnail; the badge spans y ≈ 185–355 in the source. Re-cut at y 380 → 1254×874 (the panel, the lantern, the sofa and the wrapped trunk stay; ≥ 600 px band). Map `ens_h` 874. Re-uploaded, re-verified at 390/360. |
| 2 | Legs of a person at the top-right of the powerful bollard frame (H2, confirmed 0.7) | Confirmed by eye on the re-cut sheet. Re-cut 0,90,1254,1040; map `ens_h` 1040. |
| 3 | A stroke of the headline on the top edge of the step-light frame (H4, confirmed 0.85) | Confirmed. Re-cut 400,345,854,909; map `ens_h` 909. |
| 4 | Three assets over the 220 KB budget; the 900w CDN derivative of the path page 281 KB (E2, confirmed 0.92) | Confirmed. Stainless and the path scene re-encoded at 1100 px / q70 (205 and 216 KB; the band renders ≤ 1366 wide, 1100 upscales ×1.24 at desktop like every 1254 source ×1.09 — accepted); powerful at q70 (205 KB). Map sizes updated. |
| 5 | «בלילה» four times in 290 px on the flood page (S4, confirmed 0.6) | Confirmed on the text-only pages, where the words are all there is. The spot line loses its «בלילה» (the heading already says when): «אור מכוון אל מה שרוצים לראות.» — a copy change, listed for the owner. The decor line keeps its two sentences. |
| 6 | The two dusk sentences wrap as one paragraph, an orphan «בלילה.» at 1366 (D2, confirmed 0.8) | Confirmed. Each sentence on its own line (`display:block` spans). |
| 7 | The dusk row is glued to the scene text (28 px) and floats above the facts (78–130 px) with no closing rule (D3, confirmed 0.82) | Confirmed. The row gets a closing hairline and 16 px of air above it; the gap to the facts is the facts' own top padding (that file is out of scope) and reads as the section break once the row is closed. Measured after the redeploy. |
| 8 | At 1366 the dusk hairline runs the full 1240 px wrap while the facts' rows are half-width (O6, confirmed 0.7) | Confirmed. At ≥ 901 the row takes the facts' `<dl>` column: `inline-size:calc((100% - 64px) * .55)` at the inline-end, the hairlines aligned with the rows under it. |
| 9 | Three crops cut the product (D5, confirmed 0.6): lantern 9 head and panel pressed against the edge at 390/360; edison's first bulb beheaded at 1366 | Confirmed for lantern 9 (`--ens-op` 0% 50%) and edison (`--ens-op-lg` 50% 30%). Stainless at 1366: every head intact on `verify/scene-d.png` — no change. |
| 10 | `scene_fallback` with a blank pictured product shows an uncredited photograph (E3, confirmed 0.7) | Confirmed (a dormant path, off by default). Guard: no pictured product → no photograph. |
| 11 | The 930 px dual-head file never offers its own width (E4, confirmed 0.6) | Confirmed. Any file narrower than 1254 offers its own width as the last candidate (the 1000 px wall-6w file included). |
| 12 | The camping lantern is headed «בלילה, בגינה» (H3, refuted 0.7 on scope) | The skeptic is right that the SPEC put it in the spot family; the honesty judge is right that the listing never mentions a garden («בשטח… סביב אוהל, רכב או אזור עבודה»). A one-line map override like the birch one costs nothing: «בלילה, בשטח» (`heading_portable`), listed for the owner. |
| 13 | The text-only state (12 products) reads as a stub with a caption-scale heading (S3 refuted 0.72, D4 refuted 0.7, O2 refuted 0.8 — all on scope: «the SPEC decided no photograph») | The rule (no photograph rather than another product's) stands. The *form* of the text-only state is mine to improve: without a photograph the block renders as a hairline row in the dusk row's grammar (20/22 px serif heading, the line and the link beside it at ≥ 901), so the two rows before the facts read as one designed list, not as a picture that failed to load. The cure the owner lens names (clean frames for the twelve) goes to the owner list. |

## Kept, with the reason (refuted by the skeptic, or a decision the SPEC records)

| finding | ruling |
|---|---|
| The deck/stair light is headed «בלילה, על השביל» (S2, refuted 0.68) | The deck lights sit in the path collection; the heading uses the licensed place word. «מדרגות» is not in the licensed vocabulary (P4) — a new word needs the owner. Listed for him as a possible per-product heading. |
| Dusk line 2 «יותר שמש ביום, יותר אור בלילה.» is the not-for line's positive (S5 refuted 0.72, O3 refuted 0.7) | The shopper judge of the concept round called it the single most useful solar sentence; the not-for line warns, this one explains. Kept; `line_2` is a setting the owner can clear. Listed. |
| The family line repeats the kicker's yes-line in other words (O4 refuted 0.72, H5 refuted 0.72) | The kicker says what the light is *for*; the line says what the light *is* (its form at night). Kept; listed. |
| At 1366 the scene photograph is also a visible gallery thumbnail (O5, refuted 0.6) | The known cost of «my own photos only»; the phone shopper never swipes to frame 4–6. Noted for the owner. |
| The guide link is drawn like the contact link (S6, refuted 0.85) | One link form on the page (P4's ל־ infinitive links share one form). Kept. |
| Two wall frames are studio product shots under «בלילה, על הקיר» (H6, refuted 0.7) | They are the product on a wall, the store's own frames; the honest state until the owner has night frames of them (his open item). Noted. |
| 1366 two-column baseline (D6, refuted 0.82) | The facts grid uses `start`; the scene mirrors it. Kept. |
| 360×640 over the tool's 6-screen line on three pages (E5, refuted 0.82) | P5 binds at 390×844 (every page ≤ 5.01); 360 is recorded for information (path 6.54, rope 6.30, wall 6.31; before the round 5.40, 5.12, 5.4). Written in the log. |
| `scroll-margin-top` is physical (E6, refuted 0.9) | The house pattern on every ens section; no visible effect. Kept. |

## To the owner (on his page)

The twelve products without a clean frame (the cure is a night frame per product, added through a `frame` block); the
«scene_fallback» option and why it is off; the seven copy lines plus the two new headings («בערב, בבית», «בלילה, בשטח») and
the changed spot line; line 2 of the dusk row as a setting; the deck lights' heading word; the desktop thumbnail overlap;
the two studio wall frames; the 854 px step-light source.
