# Owner directives for the side pages (verbatim, dated)

## 2026-09-02 — product page
> اهم شيء في صفحة المنتج ان يكون هناك تسويق قوي بيع قوي يعني نعرف كيف ندخل راس الزبون و نجعله يشتري ليس صفحة بصرية فقط

Reading: the PDP is judged first as a **selling page** — it must get into the buyer's head and move them to buy —
and only second as a visual page. Consequences for the process:
- The PDP brief gets a **persuasion spine** (the buyer's questions in the order they arise, each answered by a
  concrete device on the page) written BEFORE the concept panel, and every concept must build on it.
- The judging panel for the PDP adds a **conversion strategist / shopper-simulation** judge with a weighted
  "does it sell" score, on top of the creative and feasibility judges.
- Persuasion stays inside the honesty rules (HANDOFF §4): no fabricated proof (reviews, counts, urgency).
  The levers available are specificity, place-fit, objection handling (the approved "לא מתאים" pairs), risk
  reversal (14-day cancellation, free pickup shipping), concreteness (night photos, what's in the box, sizes),
  bundle/quantity anchoring from real variants, and the WhatsApp photo check as a low-commitment step.

## 2026-09-02 — answers to the blocking questions (verbatim, in order of the questions asked)

> لا يوجد رقم واتس اب الى الان
> استبدل
> لا اعرف اختار الاحسن
> افعل توصيتك
> لا يوجد مبيعات
> الدرج

Mapped to the questions:

1. **WhatsApp** — no number exists yet. Decision: keep `settings.whatsapp_number` as the switch; until it is set, every
   "send a photo of the place" CTA goes to an **email path** (`mailto:info@elmsnest.com` with a prefilled subject +
   body asking for the photo) and the contact page says so plainly. No CTA may say "בוואטסאפ" while the number is empty.
2. **PDP v2** — replace. Keep the copy assets (`.elms-sales` description HTML on all 27 products, the licensed terms
   wording in `elmsnest-pdp-facts/-trust`); the composition, palette, sections and the comparison table go.
3. **Baked-text images** — owner delegates ("choose the best"). Decision: lock the image ledger — never render index 0
   of the WINNING-SPEC §3.6 never-use list anywhere (cards, galleries, related, cart lines, search); use the cleanest
   index per product; propose regeneration of index 0 later as a separate content task.
4. **Metafields for 26 products** — owner accepts the recommendation: extract specs / not-fit / direct answer / FAQ
   from the existing description bullets into a sheet the owner approves; only then write them (writing metafields
   changes live product pages, so it waits for explicit approval of the sheet).
5. **Sales** — there are none. Decision: no sale collection, no badges, no strikethrough prices, no "-N%", no
   compare-at rendering anywhere; the one compare-at price (deck-step lights 199.90) should be cleared in admin.
   Remove `/collections/sale` links from any menu we control.
6. **After add-to-cart** — the drawer is the primary experience; the cart page is the no-JS fallback.

Not answered (my recommendations applied, reversible): no toolbar on collections (place links + price order);
canonical names = the homepage set (שביל · קיר · גינה · מרפסת) with the admin collection titles as subtitles;
homepage verdict / hero master / lockup still pending.
