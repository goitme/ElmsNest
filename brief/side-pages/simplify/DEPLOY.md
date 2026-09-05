# Deploying the SIMPLIFY round to the dev theme

Theme: `gid://shopify/OnlineStoreTheme/154726400174` (UNPUBLISHED). The MAIN theme is blocked by the
tool and must never be targeted. Tool: `mcp__claude_ai_Shopify__graphql_mutation` (load with
ToolSearch `select:mcp__claude_ai_Shopify__graphql_mutation`). One file per call, GraphQL block string:

```
mutation { themeFilesUpsert(themeId: "gid://shopify/OnlineStoreTheme/154726400174", files: [{filename: "<path>", body: {type: TEXT, value: """
<file contents verbatim>
"""}}]) { upsertedThemeFiles { filename size checksumMd5 } userErrors { filename code message } } }
```

Rules: the file must not contain `"""`; send the file byte-for-byte (read it with the Read tool from
`theme/` and paste — do not retype, do not "fix" anything while pasting); a non-empty `userErrors`
means the file was NOT written — fix the file in the repo, then retry; never upsert a template before
every section/snippet it references exists on the theme.

Order (each group after the previous one has 0 userErrors):
1. snippets: elmsnest-s-skin, elmsnest-s-place, elmsnest-s-contact, elmsnest-s-terms,
   elmsnest-s-pdp-kicker, elmsnest-s-pdp-unit, elmsnest-s-pdp-terms-line, elmsnest-s-pdp-notfor
2. sections: elmsnest-s-collections, elmsnest-s-products, elmsnest-s-fit, elmsnest-s-terms,
   elmsnest-s-coll-header, elmsnest-s-guide-strip, elmsnest-s-pdp-facts, elmsnest-v2-hero (edited)
3. layout/theme.liquid (edited), config/settings_data.json (edited), sections/footer-group.json (edited)
4. templates: index.json, collection.json, product.elmsnest.json

After each group, record filename + size + checksumMd5 from the response. Finish with a table of all
files and their remote checksums, and the local size of each (they must match the size Shopify reports
for text files, ± CRLF differences).
