# `config/settings_data.json` — patch note (do not rewrite the file)

Target: theme `gid://shopify/OnlineStoreTheme/154726400174`, file `config/settings_data.json`
(fetched 2026-09-01; 8 834 bytes, 11 existing schemes under `current.color_schemes`).

Apply as a **minimal edit** to the live file: one new key inside `current.color_schemes`, nothing else is
required. The scheme id `scheme-env2-night` is referenced by `sections/header-group.json`
(`header_colors`, `header_transparent_colors`, `header_sticky_colors`, `header_menu_colors`,
`_menu_mobile.header_mobile_colors`) and by `sections/footer-group.json` (both footer sections and every
`_footer-column`). **Upsert `settings_data.json` before the two group files** — a group JSON that
references an unknown scheme id is rejected or falls back to `scheme-1` (cream).

## 1. Add under `current.color_schemes` (after the last existing scheme, `scheme-deb451b2-…`)

The key set mirrors the 17 keys every existing scheme carries (Kalles `color_scheme_group` definition), so
the theme editor renders the scheme without "missing setting" fallbacks.

```json
"scheme-env2-night": {
  "settings": {
    "text": "#f4eee3",
    "text2": "#c9c4b8",
    "background": "#020306",
    "background_gradient": "",
    "background2": "#070b15",
    "button": "#ffd394",
    "button_label": "#1a1206",
    "button_border": "#ffd394",
    "secondary_button_label": "#f4eee3",
    "accent_color": "#ffd394",
    "line_border": "#1f1e1d",
    "overlay": "#020306",
    "pr_text": "#f4eee3",
    "price": "#ffd394",
    "sale_price": "#ffd394",
    "input_primary": "#f4eee3",
    "input_secondary": "#c9c4b8"
  }
}
```

Remember the comma after the previous scheme's closing `}`.

Mapping to SPEC §5 / §3.1: text `--env2-ink` · text2 `--env2-ink-2` · background `--env2-sky-4` (the
`html` ground, so the footer continues `goodnight` with no seam) · background2 `--env2-sky-3` (Kalles uses
it for inputs/secondary surfaces inside the scheme) · button / accent / price `--env2-glow` · button_label
`--env2-btn-ink` · `line_border` is the §3.1 hairline `rgba(244,238,227,.12)` flattened onto `#020306`
(0.12 × 244 + 0.88 × 2 ≈ 31 → `#1f1e1d`) because the scheme field is an opaque hex.

## 2. How the header glass gets its tint (no extra setting needed)

`header-inline-blocks.liquid` paints the stuck bar as
`rgb(<sticky scheme background rgb> / <background_opacity_sticky>)`. With this scheme and
`background_opacity_sticky: 0.7` in `header-group.json` that is `rgba(2,3,6,.7)` — the closest the range
(step 0.1) gets to the spec's `.72`. The blur amount is theme CSS (`.hdt-header-sticky--glass`), not a
setting; if the lead wants exactly `blur(14px)` add to `snippets/elmsnest-v2-base.liquid`:

```css
.template-index .hdt-header-sticky--glass.is-sticky,
.hdt-page-type-index .hdt-header-sticky--glass.is-sticky{backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
```

## 3. Top-level settings — no change required

Nothing under `current` needs to move for the homepage: `color_scheme_body` stays `scheme-1` (the index
template paints its own gradient on `body.template-index` / `.hdt-page-type-index` per §3.1, and
`elmsnest-v2-base` makes `#wrapper/.main-content/main` transparent). Optional, only if the lead wants the
whole store to read as night rather than just the homepage:

| key | now | optional |
|---|---|---|
| `color_scheme_body` | `scheme-1` | `scheme-env2-night` (affects every page — not asked for by §5) |
| `color_scheme_dialog` | `scheme-1` | `scheme-env2-night` (cart drawer / dialogs opened from the black header) |
| `color_focus` | `#2b2118` | `#ffd394` (focus ring visible on the dark header; §3.4 uses glow for `:focus-visible`) |
| `checkout_accent_color` / `checkout_button_color` | `#2B2118` | leave — checkout is outside this brief |

Recommendation: apply only `color_scheme_dialog` and `color_focus` if anything; leave `color_scheme_body`.

## 4. Things this file cannot do (lead / admin actions)

- **Menu `main-menu`** (Navigation, not theme files). §5 wants: `דף הבית` `/` · `קולקציות` `#env2-places`
  · `מדריך לבחירה` `/pages/guide-garden-lighting` · `מי אנחנו` `/pages/מי-אנחנו` · `יצירת קשר`
  `/pages/contact-us`. The live menu currently has `קולקציות → /collections` (with four children) and an
  extra `שאלות נפוצות`. Edit in Admin → Online Store → Navigation; use `/#env2-places` so the link also
  works from other pages.
- **WhatsApp number.** `https://wa.me/` placeholders (index.json switch/goodnight, footer contact column)
  need the number, or the sections fall back to `settings.whatsapp_number` → `/pages/contact-us`. The
  footer `text` block is rich text, so its `wa.me` link must be typed by hand.
- **Gold column headings in the footer** (`#e9b96e`, "if the scheme allows"): Kalles sets the footer
  heading colour from the scheme's `text`, so headings will be ink, not gold. If gold is wanted, add
  `.hdt-footer .hdt-footer__heading, .hdt-footer h2, .hdt-footer h3, .hdt-footer .hdt-heading{color:#e9b96e}`
  to `elmsnest-v2-base.liquid` (index-scoped) — verify the real class name on the preview first.
