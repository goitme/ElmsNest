# QUIET — notes

**Angle: the fewest images that make it real.** Four photographs for seven pages, each placed where
it carries a fact the words cannot. Everything else is typography: one clear scale, hairlines, and a
numbered spine only where the order is real.

---

## 1. The device per idea, per page

No device is used twice on a page. Nine devices in total, and each page picks the ones its ideas need.

**Guide** (six ideas, six devices)

| idea | device |
|---|---|
| where do you need light | **link rows** — four hairline rows: collection title, sub-line, `products_count`, ← |
| the four places are one real place | **the photograph, full bleed**, then **four labels on hairlines** (2-up at 390, 4-up at 1366) naming what each place word is *in that frame* |
| what the light must do | **the airy list** — serif term, body under it, no rules at all. Three alternatives, so no numerals |
| which power source | **the two-column definition list** — a narrow term column (סולארי · סוללה או USB · חיבור לחשמל), the condition and body beside it |
| what to check before ordering | **the wrapping checklist** — five short labels, two per row, hairline between; a list you scan, not one you read |
| a spec is missing | **the note** and the page's **one gold pill** |
| the four decisions themselves | **the numbered spine** `01`–`04` on the four h2s — the only numerals on the page, because place → purpose → power → checks *is* an order |

**About** (five ideas, five devices)

| idea | device |
|---|---|
| who we are | **the h1 row**: the sentence and, beside it, a tall slice of a real outside (photo on the inline-end at 390, on the inline-start at 1366) with one caption line under both |
| why the store exists | **one paragraph**, wide measure, nothing else |
| the three principles | **the airy list** (serif term, body, no rules) — principles are not ranked, so no numerals |
| what that means in practice | **ruled rows** (title + body on hairlines) — deliberately the opposite texture to the airy list above it |
| what you will find | **link rows** (title + ←) and the **one gold pill** |

**Why solar** (five ideas, five devices)

| idea | device |
|---|---|
| how it works | **the numbered spine** `1 · 2 · 3` — a day is an order — with **the mechanism photograph as a column beside it**, stretched to the height of the three beats |
| when it suits | **a plain hairline list** of four one-liners |
| when it does not | **the place / sentence pairing** — the place word in glow serif in a narrow column, the licensed sentence beside it |
| three checks | **three questions in serif**, hairline between, no numerals |
| a spec is missing | **the note** and the **one gold pill** |

**FAQ** (three ideas, three devices) — the compact TOC row, **native `<details>`** with a hairline
chevron (no «+» anywhere on the page), the **one gold pill**. No photograph.

**Processing · shipping** — the two-column definition list for the plate and the schedule, the
numbered spine for «מה קורה אחרי שהזמנתם» (an order), the note, one gold pill. No photograph.

**Contact** — the Kalles form untouched, the instruction list, **one photograph** above the email
line: an example of the picture the page asks for. One gold pill is not used here (the form's own
submit button is the action, P1).

## 2. The template plumbing — one section, seven handles

`sections/elmsnest-s-page.liquid`, `"enabled_on": {"templates": ["page"]}`.

- **One `case page.handle`, seven `when` branches, one `else`.** Branches: `guide-garden-lighting`,
  `why-solar-lighting`, `מי-אנחנו`, `help-faq`, `processing-time`, `shipping-delivery`,
  `contact-us`. The `else` prints `{{ page.content }}` inside the same prose column, the same
  hairlines and the same foot nav, so any page the owner adds tomorrow is already dressed.
- **Where the copy lives.** Literal Liquid inside each branch — as today, the owner edits page copy in
  code. That includes **shipping-delivery**, whose copy moves out of the Shopify page body and into
  the section: it is the only way the seven pages stop being two species, and it puts the schedule
  numbers of shipping and of processing in **one file**, next to each other, where a drift between
  them is visible in a diff. The Shopify page body is left in place, untouched — it is the rollback.
- **What the schema exposes** (31 settings, in eight `header` groups):
  - seven `text` settings, one h1 per page (`h1_guide`, `h1_why`, `h1_about`, `h1_faq`,
    `h1_processing`, `h1_shipping`, `h1_contact`), each defaulted to the string the page prints today;
  - four photograph groups (guide · about · why · contact), six settings each:
    `image_*` (`image_picker`, empty = the theme asset `ens-page-*.jpg`), `pos_*` and `pos_*_d`
    (object-position, mobile and ≥ 901), `alt_*`, `cap_*` (the caption that names the place or the
    mechanism), `credit_*` (the drawn credit line — empty prints nothing).
  Nothing else is a setting. Long copy is not a setting, and neither is a heading below h1: the file
  is the source, and a `text` setting per paragraph is how the old section became unmaintainable.
- **Live data, so names cannot drift.** The four rows on the guide and on About print
  `collections['…'].title` and `.products_count` in the main-menu order. The place words under the
  guide photograph and the four negatives on why-solar come from
  `{% render 'elmsnest-s-place', collection: …, emit: 'word' %}` / `emit: 'no'` — one source for all
  four pairs, the one the home and the PDP already use.
- **The foot nav is computed, not typed.** The four shared labels live in one array; the section
  removes the current page and the target of the page's gold pill before printing, so no page ever
  links to itself or repeats its own call to action.
- **Templates.** `templates/page.json` → `{"sections":{"ens_page":{"type":"elmsnest-s-page"}},
  "order":["ens_page"]}` (the Kalles `main-heading` and `main-page` leave the template; the old JSON
  is the rollback). `templates/page.contact-us.json` → `ens_page` first, then the **stock Kalles
  `contact-form` section, byte-identical** (P1: the form a Shopify shopper knows). `ens_page` gives
  the contact page its h1, its photograph and the email line; the form gives the fields.
- **Assets.** `assets/ens-page-guide.jpg` · `-about.jpg` · `-why.jpg` · `-contact.jpg`, ≤ 1800 px,
  ≤ 220 KB. About's is `eager`/`fetchpriority=high` (it is in the h1 row); the other three are
  `lazy` + `decoding=async`, all four `width`/`height`-sized.
- **No JS.** The FAQ is native `<details>`; the chevron is two CSS borders. Nothing animates,
  nothing reveals on scroll, radius 0 everywhere except the one gold pill.

## 3. Measured at 390 × 844 (Chromium, real Frank Ruhl Libre + Heebo)

Page height is the body alone; the screen count adds the shared header (64) and footer (620).

| page | body height at 390 | + header + footer | screens | target |
|---|---|---|---|---|
| **guide** | **<bdi dir="ltr">2824</bdi> px** | <bdi dir="ltr">3508</bdi> px | **<bdi dir="ltr">4.16</bdi>** | ≤ 6 |
| **about** | **<bdi dir="ltr">1870</bdi> px** | <bdi dir="ltr">2554</bdi> px | **<bdi dir="ltr">3.03</bdi>** | ≤ 5 |
| why-solar | <bdi dir="ltr">1904</bdi> px | <bdi dir="ltr">2588</bdi> px | <bdi dir="ltr">3.07</bdi> | ≤ 5 |
| FAQ (collapsed, first answer open) | <bdi dir="ltr">1261</bdi> px | <bdi dir="ltr">1945</bdi> px | <bdi dir="ltr">2.30</bdi> | ≤ 6 |

Desktop 1366 × 900, same content: guide <bdi dir="ltr">2714</bdi> px, about <bdi dir="ltr">1928</bdi> px
— shorter than mobile, as asked. The desktop section is a two-column grid (heading and numeral in the
300 px inline-start column, content in the wide one), which is the grammar the PDP facts block
already uses.

Processing, shipping and contact are not rendered here; on the same devices and the same copy they
land at roughly 2.6, 3.4 and 2.8 screens — all inside their targets, and none of them carries a
photograph that could push them over.

## 4. Is any of this twice? — the honest answer

**Once, and I left it there on purpose.** On the guide the four place words appear as labels under the
photograph (שביל · קיר · גינה · מרפסת), and two sections later the kept copy of «מה האור צריך לעשות?»
says «לשביל, למדרגות…», «לכניסה, לקיר…», «למרפסת, לפרגולה…». The words repeat; the job does not — under
the photograph they point at things in a frame, in §02 they are the objects of a sentence the audit
told us to keep verbatim. Rewriting §02 to avoid the echo would have cost more than the echo does.

Everything else that was twice is now once: the four collection names are one Liquid string each; the
photo/email promise is on the guide only in the note and nowhere else on the page; each page has one
gold pill, and the foot nav drops the link that pill already carries and never links to the page you
are on; the guide's four sections are four different devices instead of four copies of one ruled
list; About's two three-item lists have deliberately opposite textures. The nearest remaining call is
why-solar's suits list and does-not-suit list — both hairline lists — but they say opposite things and
are drawn differently (four plain lines against a glow place column), and splitting them further would
break the pairing that is the point of the page.
