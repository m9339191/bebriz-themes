# Volt — Shopify OS 2.0 Coffee Theme (Design Spec)

Date: 2026-07-06
Status: Approved
Design reference: `Gemini_Generated_Image_ni9xcsni9xcsni9x.png` (Electric Bean Roasters mockup)

## Goal

Build a complete, sellable Shopify Online Store 2.0 theme named **Volt**, implementing the
"Electric Bean Roasters" mockup: a brutalist / neon coffee-brand aesthetic. The theme is
built from scratch (no Dawn fork), works without third-party apps, and ships as an
upload-ready zip. Source lives at `themes/volt/` in the bebriz-themes repo.

## Design System

Extracted from the mockup; every color/font is exposed as a theme setting.

- **Colors** (defaults):
  - Background dark charcoal `#1A2321`
  - Neon mint `#00E0A8` (primary accent, left rail, buttons)
  - Orange-red `#FF4B33` (secondary accent, header bar, color-block cards)
  - Electric blue `#2E5BFF` (tertiary accent, color-block cards)
  - Off-white `#F4F1EA` (text on dark, light sections)
- **Typography**: bold condensed uppercase headings (Archivo Black-style via Shopify font
  picker, default `assistant_n4`-class fallback chain), plain sans-serif body. Headings
  render uppercase with tight letter-spacing.
- **Signature elements**:
  - Desktop-only fixed left vertical icon rail (mint background, category icon links,
    brand mark top) — configurable, hidden on mobile/tablet.
  - Color-blocked product cards: card background cycles mint / orange-red / blue
    (or reads per-product metafield/tag override).
  - Roast-level indicator: 5-step flame icons from metafield
    `custom.roast_level` (integer 1–5), falling back to product tags `roast-1`…`roast-5`.
  - Thick borders, hard corners (no border-radius), high-contrast blocks.

## Theme Structure (OS 2.0)

```
themes/volt/
  layout/        theme.liquid, password.liquid
  templates/     index.json, product.json, collection.json, list-collections.json,
                 cart.json, page.json, page.contact.json, blog.json, article.json,
                 search.json, 404.json, password.json,
                 customers/ login, register, account, order, addresses,
                            activate_account, reset_password
  sections/      announcement-bar, header, footer, left-rail,
                 hero-collage, featured-grid (color-block), bestsellers,
                 community-grid (Instagram-style), cafe-finder, story, newsletter,
                 main-product, main-collection, main-cart, main-search, main-404,
                 main-page, main-blog, main-article, main-list-collections,
                 main-password, customers main-* sections, cart-drawer
  snippets/      product-card, price, variant-picker, roast-level, quantity-input,
                 icon (sprite), cart-drawer-item, pagination, meta-tags
  assets/        base.css, theme.js (vanilla, no libs), section CSS where large
  config/        settings_schema.json, settings_data.json
  locales/       en.default.json, en.default.schema.json
```

## Homepage Sections (per mockup)

1. **Hero collage** — photo strip collage with oversized two-line headline overlay
   ("FUEL YOUR ELECTRIC LIFE."), image blocks configurable (up to 5).
2. **Featured color-block grid** — 2×2-ish mosaic of featured products, each tile a solid
   accent color with product image, name, roast-level flames; one tile can be double-size.
3. **Bestsellers** — light background, centered uppercase heading, 4-up product card row
   from a chosen collection, horizontal scroll on mobile.
4. **Community grid** — dark section, "JOIN THE COMMUNITY" heading with Instagram link,
   2×4 image grid (image picker blocks).
5. **Cafe finder** — banner with background image, big heading, CTA button linking to a
   page.
6. Also available: story/rich-text, newsletter signup (Shopify customer form).

## Built-in Features

- AJAX cart drawer (add/update/remove via Cart API, free-shipping progress bar optional)
- Quick-add from product cards (default variant; goes to product page if multi-variant)
- Sticky header + slide-in mobile menu
- Product page: media gallery with thumbnails, variant picker (swatch-style buttons),
  quantity, buy buttons (dynamic checkout), roast-level display, collapsible detail tabs
- Collection page: sort, tag filtering via Shopify's storefront filtering, paginated grid
- Predictive-search-free basic search page (standard `search` object)
- SEO: meta-tags snippet, JSON-LD product/organization structured data
- Accessibility: skip link, focus states, 44px touch targets, reduced-motion respect

## Non-Goals

- No wishlist/compare/quick-view modals in v1 (not in mockup; can be added later)
- No app integrations, no external JS/CSS libraries
- No demo-store content creation (products/images) — theme ships with placeholder-safe
  sections that render gracefully when content is missing (`placeholder_svg_tag`)

## Verification

- `shopify theme check` (if Shopify CLI available locally) must pass with no errors
- All JSON templates/config valid JSON; all Liquid balanced (spot check via build)
- Package `volt-theme.zip` with correct top-level folder layout for upload

## Risks / Notes

- `themes/volt/` also hosts the (future) sales page `index.html` generated by
  build_themes.py; theme source subfolders and a sales index.html can coexist, but the
  theme zip must be built from the theme folders only.
