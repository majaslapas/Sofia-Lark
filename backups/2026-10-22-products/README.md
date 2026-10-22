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

## Second pass (same day)

- **Calypso was put back exactly as it was** (title `Earrings "Calypso"`, its English description,
  `custom.stone` and photos without alt text): its names belong to the design and are not translated.
  Its colour names (Pearl gray, Lagoon blue …) are left as they are too.
- **Variant names in Latvian** (`variants.py` → `variants.json`, before: `options-before.jsonl`,
  after: `options-after.jsonl`). Option names are now `Krāsa` (was Color / KRĀSA / krāsa) and
  `Variants` (was Style). Eight products had their own values renamed; the other colour options are
  linked to Shopify's shared colour entries, which were renamed instead (`color-entries.json`).
  Not changed: the Kalliope `Izpildījums` finishes (Montana Crystal, Creamrose Light Pearl … are the
  crystal maker's names), the Habaha stone names (already Latvian) and Pērļu aitiņa (Pelēks/Balts).
- **Title typos:** `TĪRĀMO LIDZEKĻU KOMPLEKTS` → `TĪRĀMO LĪDZEKĻU KOMPLEKTS`,
  `Eleganvces vainags` → `Elegances vainags`, `Bambus Ii` → `Bambus II`.
- **Alt text** that quoted an old variant name or title was updated to match (`alts-variant-fix.json`).
