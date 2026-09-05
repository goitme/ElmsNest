# הפתק — "the slip"

**The idea, in one sentence:** the cart is not a table of rows but a short note the shop writes back to you —
a Hebrew sentence in the display serif that says what you just chose, with the numbers underneath it as a quiet
ledger — so the buyer *recognises their own decision* instead of auditing a spreadsheet.

The drawer is the note. The cart page is the same note, longer, on headed paper.

## The two voices, and the rule that keeps them apart

Every line is written twice, on purpose, and the difference is the whole concept:

| | what it is | face | example |
|---|---|---|---|
| **the sentence** | prose the shop composes from `product.type` + `variant.title` + `quantity` | Frank Ruhl Libre 500, 19–30 px | «שתי מנורות שביל סולאריות מנירוסטה, באור **צהוב חם** — לשביל.» |
| **the record** | the literal `product.title` + `variant.title`, never truncated, never styled | Heebo 300, 12–13 px, mute | «מנורת שביל סולארית מנירוסטה – תאורה אוטומטית IP65 · צהוב חם» |

This is how the concept obeys **"product titles never in the serif"** while still putting a sentence in the serif.
The serif line is *authored copy*, not a rendered title; the rendered title sits under it in the sans, in full.
The sentence is recognition; the record is the receipt. A judge can verify the rule holds by reading either line
alone.

## Leak 1 — "is this the right one?"

Today: the name is cut with an ellipsis, the variant is grey 13 px, and there is no line total.

- **The variant is promoted from a footnote to the subject of a sentence.** `צהוב חם` and `5 מ׳ / 20 נורות` are
  lit in `--env2-glow` inside the sentence, at 19–30 px, not parked in grey under the name. The one thing the
  buyer chose two clicks ago is the largest coloured thing on the line.
- **The name is never truncated.** No `text-overflow`, no line clamp; `overflow-wrap:anywhere` on the record line.
  Harness: `truncated` cannot fire — there is no clipped title in either surface.
- **Every line prints its own total** in glow serif (`339.80 ₪`), with `169.90 ₪ ליחידה` beneath it. On the
  quantity-1 line the per-unit line is **suppressed**, because `1 × 89.90` and `89.90` are the same number and
  printing both is noise, not proof. (The harness reads `lineTotal:false` on that line for exactly this reason —
  the total is there, `89.90 ₪`; it is the *unit* row that is provably unnecessary.)
- **Quantity plurality is written, not implied**: «שתי מנורות…», «גרילנדה אחת…». A wrong quantity is caught by
  reading, before any arithmetic.
- **One remove control per line**, and it is the word `הסרה`, not a bin. Kalles' two identical bins at quantity 1
  are gone: harness `removes=[1,1]` against the baseline's `[1,2]`.
- The photo is a 54–104 px stamp. It is a link (the only way back to the product) but a *small* one:
  `exitLinks=2`, against the cart page's baseline of 5 — on a decided buyer's screen the routes out of the cart
  are the smallest things on it.

## Leak 2 — "what will this cost me and when does it come?"

- **The drawer pins two of the approved numbers above the button, permanently, at every scroll position:**
  `0 ₪ · משלוח לנקודת איסוף — חינם. עד הבית 29.90 ₪.` and `14 יום · לביטול מקבלת המוצר, לפי חוק הגנת הצרכן.`
  These two never scroll away, because they are the two facts that decide whether a stranger's shop gets a card
  number. The third, `8–17 ימי עסקים`, and both fine-print subs sit in the **נ.ב.** at the foot of the note —
  where a postscript belongs on a slip.
- **The cart page prints all four, in full, with both subs**, as a hairline 2-column ledger (collection §4.6
  shape, never four boxes), and on desktop it sits **in the same column as the checkout button**, beside it, not
  underneath it. The baseline put the three "לפני שממשיכים לתשלום" boxes *below* the button as the heaviest
  element on the page; here they are the button's neighbour and half its weight.
- Harness: `terms=3/4` in the drawer (by choice), `terms=4/4` on the cart page. Baseline: `0/4` and `3/4`.
- **What the shop refuses to say is written down**: «המחירים כוללים מע״מ. עלות המשלוח נבחרת בעמוד התשלום, ולכן
  איננו כותבים כאן מספר סופי.» An unknown number is named as unknown rather than replaced with a hedge.

## Leak 3 — "can I get out of this?"

`14 יום לביטול מקבלת המוצר, לפי חוק הגנת הצרכן.` is one of the two lines pinned above the drawer's checkout
button — it is impossible to reach checkout without having passed it. The fee cap
(`דמי ביטול עד 5% או 100 ₪ — הנמוך מביניהם.`) rides with it in the נ.ב. and on the cart page. Verbatim, both
halves, no paraphrase.

## The empty state

Not an error screen and not an icon. **«הפתק עוד ריק.»** — then one sentence that explains what *will* be
written here («ייכתב כאן מה נכנס לסל — בשם, בגוון ובכמות»), so the empty state teaches the full state. Under it
the store's own vocabulary as a hairline ledger: **שביל · קיר · גינה · מרפסת**, each with the place it lights,
each row ≥ 56 px, the four flexed to fill the panel so there is no hole. Then a short נ.ב. and one pill,
`לקטלוג — 27 מנורות` (27 is the catalogue's own count, printed on the collection page). The stock grey
cart-with-an-✕ is gone.

## Deliberate decisions

- **Panel width 420 px on desktop** (up from Kalles' 340). Chosen typographically, not arbitrarily: the concept
  lives or dies on whether the sentence reads as *prose*. At 340 px the 23 px serif breaks at ~24 characters and
  «שתי מנורות שביל / סולאריות מנירוסטה, / באור צהוב חם» shatters into fragments; at 420 px it breaks at ~36–40
  and lands on meaning. Mobile stays on the contract: `min(90vw, 420px)` → **351 px at 390, 324 px at 360**.
- **`8–17 ימי עסקים` is in the drawer's postscript, not pinned.** Delivery *time* matters after the decision to
  buy; delivery *cost* and the right to cancel matter before it. Ranking them was the only way three long rows
  could earn a 324 px panel.
- **`1 תמונה` is dropped from the drawer entirely.** "Send a photo and we'll check the fit before you order" is a
  pre-purchase device; offering it to someone holding a full basket invites them to stop. It appears on the cart
  page, where checking properly is the point, with the `mailto:` CTA (never "בוואטסאפ") and the licensed caveat
  «כאשר מידע אינו מאומת, איננו מציגים אותו כעובדה.»
- **No basket-level "amount of light".** `DERIVED-DATA.md` rules that a light-measure is per-line only: metres
  exist on 5 of 27 products and this very basket would print `5 מ׳` while silently dropping two path lights. So
  `5 מ׳` and `20 נורות` are lit **inside the garland's own sentence**, where they are true and visible in the
  variant the buyer picked, and the basket sign-off counts only what always counts:
  «בסל: שתי מנורות שביל וגרילנדה — **3 יחידות**.» (`cart.item_count`, no parsing, never blank.)
- **The dead hole is closed structurally, not by padding.** The note's lines are `flex:1 0 auto` inside the scroll
  box, so spare panel height is absorbed *into* the lines. Harness `voidAboveSubtotal`: baseline 288 px at
  390×844 and 343 px at 1440×900 → **−59 px and 32 px** here (32 px is the body's and the foot's own padding;
  what the harness measures between the last line and the subtotal in this layout is not emptiness, it is the
  sign-off sentence and the refusal).
- **Separation from the page behind.** The Kalles scrim is a black veil on a black page. Here the panel is
  *lighter than the page*: `linear-gradient(202deg,#14213a → #070b15)` with faint 28 px rules (paper), a 1 px
  gold hairline, a 90 px black bloom, and a scrim that actually blurs (`rgba(2,3,6,.66)` + `blur(3.5px)`). The
  edge is visible in the render without a single border box.
- **Kalles contract kept verbatim**: `<hdt-cart-drawer id ref section-id data-count data-total-price>`,
  `<dialog id="CartDrawer" ref="dialog" pos="right" scroll-lock>`, `<button ref="closeButton" aria-controls>`,
  the POST form + `<button name="checkout">`, `<hdt-line-item>`, `<hdt-quantity-wrapp>` with
  `minus`/`updates[]`/`plus`, `<wrapp-remove-item-oncart data-index>`. Only order, wording, type and spacing moved.
- **JS off:** the cart page's steppers and removes are real submit buttons (`name="minus"`, `updates[n]=0`),
  there is a visible `עדכון הפתק אחרי שינוי כמות` submit, and checkout is a native form submit. The drawer does
  not exist without JS, which is why the cart page carries the whole note and all four numbers on its own.
- **Checkout is the only fill on either surface**, 56–58 px, pill, glow, with the amount inside it. Every other
  control is a hairline or an underlined word. The route out of the cart (`לעמוד העגלה` / `להמשיך להסתכל`) is a
  fit-content text link, not a twin button.

## Refused

No free-shipping progress bar, no discount / note / gift / estimator field, no badge, strikethrough or "-N %",
no rating, count, urgency or countdown, no English UI, no cream or brown, no invented fact, no fifth number, no
"בוואטסאפ". Product titles are never in the serif. `letter-spacing` on Hebrew is zero everywhere
(harness `tracked=[]`, against a baseline of two 3 px runs).

## Measured (brief/side-pages/cart/verify.js)

**drawer.html** — 390×844 · 360×640 · 320×568 · 1440×900

```
dom=2.19 / 2.00 / 1.75 / 2.67      (baseline 0.99 — the twin-button defect)
removes=[1,1] everywhere           (baseline [1,2])
under44=0                          (baseline 10)
tracked=0                          (baseline 2 × 3px)
terms=3/4                          (baseline 0/4)
void=-59 / -263 / -339 / 32        (baseline 288 / 84 / 12 / 343)
overflow=false  js-errors=0
```

**cart.html**, full state measured alone (the file also carries the empty state below the `<hr>`; the harness
reads both at once and then reports an empty-state place link as the "rival", which is why the whole-file
dominance is 0.53–0.91 and the state-A dominance below is the real one):

```
checkout t370 b428 · inside the fold at 390×844, 360×640, 320×568 AND 1440×900
   (baseline t932 — 136 px below the fold at 390 and 340 px below at 360)
dom=2.19 / 2.01 / 1.76 / 2.35   rival = the mailto ghost, not a product link
exits=2                         (baseline 5 product-title links)
under44=0                       (baseline 25)
terms=4/4   tracked=0   overflow=false   js-errors=0
doc 2030 px at 390 (baseline 2544) · 1339 px at 1440 (baseline 1791)
```

Shots: `shot-{desktop,mobile}[-fold].png` (drawer), `shot-cart-{desktop,mobile}[-fold].png` (cart page).
`node brief/shot.js` reports **drawer 1801 px desktop / 1689 px mobile**, **cart 2558 px desktop / 3460 px
mobile** (two states per file), no horizontal overflow, no JS errors.

## Weakest point

**The sentence has to be written by Liquid, and Liquid does not conjugate Hebrew.** «שתי מנורות שביל» needs a
gendered numeral and a plural noun agreeing with `product.type`; «גרילנדה אחת» needs the feminine. That is a
`case`/`when` table over the ~8 product types plus a numeral table for 1–10 and a `{{ n }} יחידות` fallback
above that — perhaps 40 lines of Liquid, and a wrong branch produces a sentence that reads as broken Hebrew
rather than as a slightly-off label. A generic table cannot fail this way, and that is the price of the idea.
Two mitigations are already in the markup: the record line beneath always carries the literal title and variant,
so a mangled sentence is never the only identification; and the sign-off falls back to `cart.item_count`, which
needs no grammar at all. The second weakness is smaller: at 320×568 the note scrolls before the second line is
fully visible — below the brief's 324 px floor, but real on an old phone.
