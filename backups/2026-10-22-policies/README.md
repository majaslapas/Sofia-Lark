# Policies: the old domain (22 October 2026)

The texts named the old shop address https://sofialarkshop.com/, which no longer works.

- **Privacy policy page** (`/pages/privacy-policy`): fixed. The three links now go to
  https://sofialark.com/. The Word formatting was removed; every word of the text is the same.
  `before.json` has the original.
- **Shopify's own policies** (Settings → Policies) could not be changed from here: the connection
  has no permission to edit them. Each needs the same small change in the admin:
  - Privacy policy: 3 links, https://sofialarkshop.com/ → https://sofialark.com/
  - Refund policy: 1 link, same change
  - Terms of service: 2 links, same change
  - Contact information: the link http://www.sofialarkshop.com/ → https://sofialark.com/, and the
    e-mail **info@lauralark.com → info@lauralark.lv** (the address everywhere else).
  The finished texts are in `policy-*.html` (paste into the editor's HTML view, `<>`) if that is
  easier than editing the links one by one.
