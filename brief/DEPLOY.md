# Deploying to the dev theme (integration agent)

Theme id: `gid://shopify/OnlineStoreTheme/154726400174` (UNPUBLISHED — writes are allowed; the MAIN theme is blocked).

Use the Shopify MCP tool `mcp__Shopify__graphql_mutation` (load it with ToolSearch `select:mcp__Shopify__graphql_mutation,mcp__Shopify__graphql_query`).
Upsert ONE file per call using a GraphQL block string so no escaping is needed:

```
mutation { themeFilesUpsert(themeId: "gid://shopify/OnlineStoreTheme/154726400174", files: [{filename: "sections/elmsnest-v2-hero.liquid", body: {type: TEXT, value: """
<file contents verbatim>
"""}}]) { upsertedThemeFiles { filename size } userErrors { filename code message } } }
```
Rules:
- Order: snippets → sections → `templates/index.json` → `sections/header-group.json`, `sections/footer-group.json` → `config/settings_data.json` → `layout/theme.liquid`. Shopify rejects a template that references a section file that does not exist yet.
- Shopify validates Liquid + schema on upsert; a `userErrors` entry means the file was NOT written. Fix and retry.
- File contents must not contain the sequence `"""`.
- For `config/settings_data.json` and `layout/theme.liquid`, READ the current file first (graphql_query `theme(id){ files(filenames:[...]) { nodes { body { ... on OnlineStoreThemeFileBodyText { content } } } } }`) and make a minimal edit — never rewrite from memory.

Verify the real render:
```
python3 /home/user/ElmsNest/brief/mirror.py "https://elmsnest.com/?preview_theme_id=154726400174" /home/user/ElmsNest/brief/build-preview/live
node /home/user/ElmsNest/brief/shot.js /home/user/ElmsNest/brief/build-preview/live/index.html /home/user/ElmsNest/brief/build-preview/live/shot
```
Then Read the four PNGs. Also grep the mirrored index.html for `Liquid error` (must be 0) and for each section anchor id.
