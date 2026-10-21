# Product metafields: what was written to the store

On sofialark.com, eight product metafields were created (namespace `custom`, pinned on the product form in admin). They were then filled with **491 values on 263 of the 278 published products**, taken only from what each product's own description already states.

Every value is listed per product in [`values.csv`](values.csv) (with [`values.json`](values.json) for scripts). Nothing that existed before was changed: all eight fields were new, and the older `custom.material`, `custom.color`, `custom.design` and `custom.earring_closure` were left as they were.

| Field (admin name) | Key | Type | Products | Taken from |
| --- | --- | --- | --- | --- |
| Īss apraksts | `custom.subtitle` | single line text | 49 | The description's first plain line, when it reads as a summary. Lines that only repeat the name, contain a colon ("Dizains: …", "Kulons: 12 cm") or make a claim are skipped. |
| Garums (mm) | `custom.length_mm` | decimal | 104 | Size lines ("Izmērs: 5 × 3 cm", "Length 61 mm", "Garums: 19 cm"), converted to millimetres. When a line gives two numbers without saying which is which, the longer side is the length. Lengths with a "+" (a bracelet's "16 cm + 3 cm" extension) and sizes without a unit (ring "18") were left empty. |
| Platums (mm) | `custom.width_mm` | decimal | 91 | As above. |
| Pārklājums | `custom.plating` | single line text | 12 | Descriptions that say "14 carats", "14Carats" or "14 karāti", written as "14 karātu zeltījums". |
| Akmens | `custom.stone` | single line text | 55 | "Akmens:" lines, "saldūdens pērles" (freshwater pearls) in the text, and short first lines naming the stones ("Natural pearls"). |
| Kopšana | `custom.care` | multi-line text | 59 | The Kalliope products' own "Rotas kopšana" paragraph. |
| Nemaina krāsu ūdenī | `custom.water_resistant` | true/false | 68 | Only explicit phrases: "nemaina krāsu saskarē ar ūdeni", "pret ūdeni", "ūdensdroši", "ūdensizturīgi", "pret mitrumu", "does not change color in contact with water", "water-resistant". Only "yes" was written; a product that says nothing has no value, not "no". |
| Hipoalerģiska | `custom.hypoallergenic` | true/false | 53 | "hipoalerģiska", "neizraisa alerģijas", "hypoallergenic", "anti-allergic". Only "yes" was written. |

## Not filled

- **The 58 draft or unpublished products.** The values came from the public catalogue. The page still reads their descriptions if they're published later.
- **What descriptions don't state.** About 140 products give no size, and most give no stone or care text. Those fields stay empty and the page leaves them out.
- **Claims that weren't explicit.** For example, "saldūdens pērles" (freshwater pearls) contains "ūden" (water) but is not a water promise.

## How the product page uses them

For each fact, the page uses the first that exists:
1. the filled metafield;
2. what the description says;
3. for material and closure only, the older metafields.

An empty field is simply not shown, so a product with any mix of these filled, or none, still has a complete page. Shopify returns decimals as "61.0"; the page shows "61 mm", and sizes from 100 mm as "19 cm".

## Adding a new product

Nothing extra is required. Write the description as usual, ideally with lines such as "Izmērs: 4 × 3 cm" and "Materiāls: zeltīta bronza", and the page reads them.

The eight fields appear under **Metafields** on the product form. Fill one only to show a value the description doesn't have, or to override it. Whatever is filled wins over the description.

## Undoing it

In admin, go to *Settings → Custom data → Products*, open a field, and choose *Delete definition*. Shopify offers to delete its values along with it. The theme keeps working without them; it falls back to reading the descriptions.

## Why these fields help beyond the page

The Search & Discovery app can turn metafields into collection filters, for example "Nemaina krāsu ūdenī", "Hipoalerģiska" or "Akmens". Descriptions alone can't do that.
