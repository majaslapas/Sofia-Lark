# Product text before the SEO pass (22 October 2026)

What the store's products looked like before they were changed, so any of it can be put back.

- `all.json` – every published product as `/products.json` showed it (titles, descriptions, images).
- `english.json` – the 55 products whose titles and descriptions were in English: the originals.
- `media.jsonl` – every product photo with the alt text it had (most had none).
- `latvian.py` → `latvian.json` – the Latvian titles and descriptions written for those 55.
- `alts.py` → `alts.json` – the alt text given to the 393 photos that had none, made from the
  product's (Latvian) title, its type and, for a variant's own photo, the variant name.
- `*-bulk.jsonl` – exactly what was sent to Shopify in the two bulk updates.

Product handles (and so the product URLs), variants, prices and stock were not changed.
