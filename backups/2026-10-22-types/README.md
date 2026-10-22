# Jewellery type tags (2026-10-22)

Every collection can be narrowed to one kind of jewellery (the "Veids" filter in
`theme/snippets/sl-filters.liquid`). It works from product tags and Shopify's tag
URLs, `/collections/<handle>/<tag>`, so nothing needs setting up in Search & Discovery.

Tags added (one per product, 281 products; `plan.json` lists each one):

| Tag | Products | URL handle |
|---|---|---|
| Auskari | 112 | auskari |
| Kaklarotas | 50 | kaklarotas |
| Piespraudes | 47 | piespraudes |
| Aproces | 36 | aproces |
| Gredzeni | 34 | gredzeni |
| Rotu kopšana | 2 | rotu-kopsana |

The packaging product (mk-1, "Iepakošana") got no tag.

How each product's tag was chosen: membership of a category collection (all-earrings,
necklaces, all-bracletes, gredzeni, all-rings, piespraudes-1, cleaning-chemicals),
otherwise its product type. No product matched two kinds.

Other store changes made at the same time:
- product type set to "Auskari" on naudinas, earrings-olympic-palm and
  modernist-auskari-24-19, and to "Rokassprādzes" on aproce-24-3, so they appear in the
  smart Visi auskari / Visas aproces categories;
- Daudzķēžu kaklarota, Dore kaklarota and Vox added to the Kaklarotas collection
  (`missing-from-category.json`).

**New products need one of these tags** (written exactly as above), or they won't show
under any kind. Products with none of the tags still appear on the plain collection page.

Files:
- `products-before.jsonl`: bulk export before the change (tags, type, collections);
- `plan-raw.json`, `plan.json`: the tag each product was given.

To undo: `tagsRemove` the tag listed in `plan.json` for each product.
