# Product text before the SEO pass (22 October 2026)

What the store's products looked like before they were changed, so any of it can be put back.

- `all.json` – every published product as `/products.json` showed it (titles, descriptions, images).
- `english.json` – the 55 products whose titles and descriptions were in English: the originals.
- `media.jsonl` – every product photo with the alt text it had (most had none).
- `latvian.py` → `latvian.json` – the Latvian titles and descriptions written for those 55.
- `alts.py` → `alts.json` – the alt text given to the 393 photos that had none, made from the
  product's (Latvian) title, its type and, for a variant's own photo, the variant name.
- `products-bulk.jsonl`, `alts-bulk.jsonl` – exactly what was sent to Shopify (as batched updates;
  bulk mutations are not available through the connector).
- `stone-metafields.json` – the seven `custom.stone` values that were in English, before and after.
- `products-after.jsonl` – the store after the changes, used to check every title, description and
  alt text came out as intended (all 55 / 55 and 393 / 393 matched; no photo is left without alt).

Product handles (and so the product URLs), variants, prices and stock were not changed.
