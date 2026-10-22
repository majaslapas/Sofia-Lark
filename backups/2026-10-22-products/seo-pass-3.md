# SEO pass 3 (22 October 2026)

Checks taken from the twelve "Shopify SEO" skills in get-ryze.ai's article (collection pages,
product template, faceted URLs, product schema, variant duplicates, alt text, internal links,
titles and meta), applied by hand.

Store data changed:
- **44 product SEO overrides deleted** (`global.title_tag` / `global.description_tag`), listed with
  their old values in `seo-tags-before.jsonl`. They belonged to other products (three rings called
  "Earrings "Marie Antoinette"", nine brooches called "Zvaigznītes…", Bezdelīga and Lapiņas called
  "Spāre…", four necklaces called "Libera ZAMAK…", Moonlit Arch Ring described as the Golden Ball Bar
  Ring) or were the English texts replaced earlier. Google now uses each product's own title and
  description. The "| Laviyen Rotas" titles were left: those pieces are by Laviyen.
- **Gredzeni** got the 7 rings that were only in "ALL RINGS" (wave rings, Afrodītes gredzens,
  Zelta viļņa / lodītes / Mēnessgaismas arkas / Četrlapu āboliņa gredzens): 38 → 45.
- **Search descriptions** for Auskari, Kaklarotas, Aproces and Gredzeni (they had none) and for Rotu
  kopšanas līdzekļi, whose description was English text about a silver cleaner:
  "Keep the precious sterling silver clean, shiny and sparkling with this handy two-step silver
  jewellery cleaner …".
- **Contacts page**: the link to the old domain (http://www.sofialarkshop.com, now 404) points to
  https://sofialark.com.

Theme (copy "Impulse – SEO labojumi (priekšskatījums)"):
- `/collections/all` ("vissas rotas", the same list as Visas rotas) names Visas rotas as canonical.
- Titles lose a stray trailing "." or ":" ("Gredzeni.", "Kontakti:").
- Thank-you / event / live-shopping / empty sign-up pages are `noindex`.
- Product structured data names the maker (Kalliope, Laviyen) as brand and carries the 30-day
  return policy.
- Each category header has an opening line naming what it holds.
