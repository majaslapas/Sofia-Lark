# Sofia Lark product page: theme sections

The product page layout from [`../product-page/`](../product-page/), built for the store's Impulse 9 theme as its **default product template**. Every product uses it as it is, with no setup per product, collection or metafield. Each part fills itself from data the store already has, and any part with nothing to show is left out.

![four products, no setup](screenshots/four-products.jpg)

These are renders of real products (photos, prices, stock and descriptions as they are today) inside the live header and footer: a brooch with one photo, a bracelet, an adjustable ring and a Kalliope earring.

## What every product gets, and where it comes from

The catalogue was measured first: 278 published products, 246 of them single-variant and 151 with one photo. The layout was then built and tested against all 278 (see *How it was checked*).

| Part of the page | Source | Products that get it today |
| --- | --- | --- |
| Photographs | The product's media. With fewer than four photos of its own, its variant photos fill in. A last photo that would sit alone in a half-width slot takes the full width. | all (151 show one photo) |
| One line under the title | The description's first plain line, when it reads like a summary ("Zeltītas bronzas auskari ar dabīgām saldūdens pērlēm"). The `custom.subtitle` metafield wins when filled. | 65 |
| Key facts under the price | The description, read by `snippets/sl-product-facts.liquid`, which picks up four things:<ul><li>`Label: value` lines (Izmērs, Garums, Materiāls, Size, Material, …).</li><li>The Kalliope headings: Materiāli, Roku darbs, Rotas kopšana.</li><li>A short first line naming the metal.</li><li>The description's claims: does not change colour in water, hypoallergenic, handmade in Greece.</li></ul> | 275 |
| Colour or variant picker | Photo tiles when every value of an option has its own photo, otherwise words. No option names need setting. | 25 tiles, 7 words |
| Stock line | The variant's inventory: "Palicis pēdējais" (one left), "Palikuši tikai 2" (only two left), or sold out with a "tell me when it's back" link. | all |
| Rating | Shopify's standard review metafields, which Judge.me fills. | the 5 with reviews |
| Size and materials tab | The same facts in full, under Latvian labels. | 275 |
| Care tab | The description's own care text (Kalliope), otherwise the section's text and the care cloth. | all |
| "Sader kopā" (goes well together) | The Search & Discovery app's complementary products. If there are none, Shopify's own recommendations for the product, fetched after the page loads. The care cloth always comes last. | all |
| Review letter, shop in Rīga | The same real review and shop details on every product. | all |

## Files

| File | What it does |
| --- | --- |
| `templates/product.json` | The default product template: the sections below plus the theme's existing `sl-store`. |
| `sections/sl-product.liquid` | The product itself. The photos scroll while the buy box stays in place. The buy box holds the title, the one-line summary, app blocks (for example Judge.me stars), the price, key facts, the variant picker with stock, the button, the free-delivery meter, the three promises and the tabs. On phones there's a swipe gallery and a sticky add-to-cart bar. |
| `sections/sl-product-pair.liquid` | "Sader kopā": complementary products, or Shopify's recommendations, then the care product. Rows can be added to the cart in place. |
| `sections/sl-quote.liquid` | One real review set as a letter, plus up to three short ones. |
| `snippets/sl-product-facts.liquid` | Reads size, material, claims and care from a product. It uses only plain string operations, so each rule can be read and changed. |
| `snippets/sl-product-media.liquid`, `snippets/sl-pair-row.liquid` | One gallery square; one "Sader kopā" row. |
| `assets/sl-product.css`, `assets/sl-product.js` | Styles and behaviour. Without the script, the form still adds the chosen variant to the cart. |

## Install

Because `product.json` is the default template, **installing it changes every product page at once**. Do it on a copy first.

1. Duplicate the live theme ("Impulse – fiksētā kartīte (draft)") under *Online Store → Themes*.
2. On the copy, choose *Edit code* and add the files above, replacing `templates/product.json`. Everything else is a new file.
3. Preview the copy on a few very different products: one with many colours, a one-photo brooch, a bracelet, a ring and a sold-out piece.
4. Publish the copy. The live theme stays untouched as the way back.

Products that use another template (`product.gift-card`, `product.high-variant`, `product.preorder`, …) keep it.

## The cart

- The theme's cart type is currently **page**. With a page cart, adding a piece shows a short confirmation under the button and the visitor stays on the page.
- If the theme is switched to **drawer**, the theme's own drawer opens instead. The section sends the same `ajaxProduct:added` event the theme listens for.
- The header cart badge updates either way.

## Product metafields

Eight product metafields exist in the store and were filled from the descriptions for 263 products: `custom.subtitle`, `length_mm`, `width_mm`, `plating`, `stone`, `care`, `water_resistant` and `hypoallergenic`. What was written, by which rule, and how to undo it is in [`../metafields/README.md`](../metafields/README.md).

For each fact, the page uses the first that exists:
1. the filled metafield;
2. what the description says;
3. for material and closure only, the older `custom.material` and `custom.earring_closure`.

Anything empty is left out, so every product looks complete whatever is filled. Some older metafields hold wrong values (Calypso's `custom.material` says "Juveliertērauds"), but they're only used where a description says nothing.

"Sader kopā" also reads the Search & Discovery app's **complementary products**. Filling those replaces Shopify's automatic recommendations with hand-picked ones.

## How it was checked

- **Theme Check** (`shopify theme check`): 0 offenses.
- **The whole template with and without metafields.** All 278 products rendered twice: once with the values now stored, once with none. Both give complete pages.
- **The facts parser, on all 278 published products.** The rules were first written as a Python prototype limited to what Liquid can do. The Liquid snippet gives identical results on **278 of 278** products.
- **The whole template, on all 278 products.** Each was rendered with LiquidJS and Shopify-style filters from the store's public `products.json`, and all 278 rendered without an error.
- **In a browser**, inside a saved copy of the live product page with the real `theme.css`, `theme.js`, header and footer, and with the cart and recommendations endpoints mocked.
  - **Products:** Calypso (12 colours, 5 sold out), a brooch, a bracelet, an adjustable ring, a Kalliope earring, and a sold-out necklace.
  - **Behaviour checked:**
    - Price, stock line, photo and `?variant=` follow the chosen colour.
    - Sold-out variants offer the notify link.
    - Adding to the cart updates the badge and the delivery meter.
    - "Sader kopā" swaps in Shopify's recommendations when there are any and keeps the care cloth when there are none.
    - Arrow keys move through the colours.
    - The phone bar appears after the button and steps aside at the footer.
    - No sideways scroll at 1440px or 390px, and no script errors.
- **Not yet checked on Shopify itself.** That needs the files on an unpublished copy of the theme.
