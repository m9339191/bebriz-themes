---
title: Jewelry & Luxury Features
id: jewelry-features
---

### Ring Size Guide

The ring size guide provides an interactive size finder that helps customers determine their ring size using diameter-to-US-size conversion, reducing returns and improving confidence in purchases.

**Setup:**

1. The ring size guide button appears automatically on products with a `Ring Size` or `Size` variant option.
2. Clicking the button opens a modal with:
   - A diameter measurement guide
   - A conversion table (mm to US size)
   - Tips for measuring at home
3. To customize the size chart, go to **Theme settings > Product Page > Ring Size Guide**.
4. You can upload a custom printable ring sizer PDF in the section settings.

> **Tip:** Include a note encouraging customers to measure at the end of the day when fingers are slightly larger, for the most accurate fit.

### Custom Engraving

The custom engraving feature adds a text input field on the product page where customers can enter personalized engraving text, which is passed to the order as a line item property.

**Setup:**

1. Add the tag `engravable` to any product in **Shopify Admin > Products**.
2. The engraving input field appears automatically below the variant selector.
3. Settings:
   - **Character limit** — Default 20 characters (customizable in Theme settings)
   - **Live counter** — Shows remaining characters as the customer types
   - **Font preview** — Displays the engraving text in a script font preview
4. The engraving text is stored as a **line item property** named "Engraving" and appears in:
   - Cart drawer
   - Checkout page
   - Order confirmation
   - Admin order details

> **Tip:** Consider adding an engraving fee by creating a variant or using a Shopify app for line item pricing adjustments.

### Certification Card

The certification card displays detailed product specifications including metal type, stone, carat weight, clarity, and GIA certification status in an elegant card format on the product page.

**Setup:**

1. Create the following **product metafields** in Shopify Admin:
   - `custom.metal_type` (Single line text) — e.g., "18K White Gold"
   - `custom.stone_type` (Single line text) — e.g., "Diamond"
   - `custom.carat_weight` (Single line text) — e.g., "1.5 ct"
   - `custom.clarity` (Single line text) — e.g., "VS1"
   - `custom.color_grade` (Single line text) — e.g., "F"
   - `custom.certification` (Single line text) — e.g., "GIA"
   - `custom.certificate_number` (Single line text) — e.g., "2215701234"
2. The certification card renders automatically on any product page where at least one metafield has a value.
3. If `custom.certification` is set to "GIA", a GIA badge icon is displayed.

> **Tip:** Include certificate numbers for high-value items. Customers buying luxury jewelry value transparency and third-party certification.

### Luxury Design

Brilliance features a carefully crafted black and gold luxury aesthetic throughout every element of the theme.

**Key design elements:**

- **Color palette** — Deep black backgrounds (#0a0a0a) with gold (#C5A47E) accents
- **Typography** — Cormorant Garamond serif for headings with wide letter-spacing, Inter for body text
- **Sharp edges** — Zero border radius throughout for a clean, architectural feel
- **Generous whitespace** — Maximum breathing room between elements
- **Thin borders** — Subtle 1px borders in muted gold tones

**Customization:**

1. Go to **Theme settings > Colors** to adjust:
   - **Background** — Main page background
   - **Gold Accent** — Primary accent color (default: `#C5A47E`)
   - **Text** — Primary and secondary text colors
   - **Border** — Subtle border color
2. Go to **Theme settings > Typography** to adjust:
   - **Heading Font** — Default: Cormorant Garamond
   - **Body Font** — Default: Inter
   - **Letter Spacing** — Heading letter-spacing amount

> **Tip:** The default gold accent (#C5A47E) works well for most jewelry brands. If your brand uses rose gold or silver, adjust the accent color accordingly.

### Gallery Style Collection

The gallery-style collection page displays products in a clean 3-column grid with generous whitespace, letting the product photography take center stage.

**Setup:**

1. Go to **Theme settings > Collection Page**.
2. Configure the grid settings:
   - **Columns** — Default: 3 (options: 2, 3, 4)
   - **Image Ratio** — Default: Square (options: Portrait, Square, Natural)
   - **Spacing** — Default: Large (options: Small, Medium, Large)
   - **Hover Effect** — Default: Subtle zoom (options: None, Zoom, Second Image)
3. Product cards display with minimal information:
   - Product name in serif font
   - Price
   - Metal color swatches (if available)

> **Tip:** Use consistent product photography with a plain background. The gallery layout works best when all images share a similar style and lighting.

### Reviews (App Required)

The theme provides a "Reviews" tab on product pages and star rating displays on product cards. However, **actual review collection and display requires a Shopify app**.

| App | Cost | Best For |
|-----|------|----------|
| **Shopify Product Reviews** | Free | Basic review needs |
| **Judge.me** | Free tier | Most popular, photo reviews, email requests |
| **Loox** | $9.99/mo | Photo & video reviews |
| **Stamped.io** | Free tier | Reviews + loyalty integration |

After installing a review app, reviews will automatically appear in the Reviews tab. Star ratings on product cards pull from the app's data.

> **Note:** Without a review app installed, the Reviews tab will be empty and star ratings will show as placeholder.
