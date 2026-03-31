---
title: Product Page
id: product-page
---

### Variant Picker

The product page supports multiple variant picker styles. In the product section settings, choose between:

- **Dropdown** — Standard dropdown selectors for each option (Size, Color, Material, etc.).
- **Buttons** — Inline pill-style buttons that let customers select variants without opening a dropdown.
- **Color swatches** — Visual color circles for color-type options that swap the product image on selection.

### Color Swatches

Color swatches display a visual circle representing each color option. When a customer selects a different color, the product image gallery automatically scrolls to the corresponding variant image. To set up color swatches:

1. Ensure your product has a variant option named `Color` (or the localized equivalent for your store language).
1. Assign a unique image to each color variant in the Shopify product editor. The swatch will pull the image for that variant.
1. In the theme editor, navigate to the product section and enable **Show color swatches**.
1. Swatch colors are automatically derived from the variant option value name (e.g., "Black" renders a black circle). For custom colors that don't match a standard color name, add a product metafield `product.color_hex` with the hex value.

### Image Gallery

The product page image gallery supports multiple layouts: stacked, carousel, or thumbnail grid. Images support pinch-to-zoom on mobile and click-to-zoom on desktop. The gallery automatically groups images by variant when variant-specific images are assigned.

### Product Tabs

Product tabs appear below the main product details and organize supplementary content into collapsible sections:

- **Description** — Automatically populated from the product description field in Shopify.
- **Shipping & Returns** — Static content configured in **Theme settings > Product tabs**. Write once, display on all products.
- **Size Guide** — Displays a size chart table or links to a custom page with detailed sizing information.
- **Reviews** — Integrates with the Shopify Product Reviews app or compatible third-party review apps like Judge.me and Loox.

You can add custom tabs by creating pages in Shopify and assigning them in the product section settings. Each custom tab displays the full page content inline.
