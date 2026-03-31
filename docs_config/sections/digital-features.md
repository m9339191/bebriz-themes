---
title: Digital Products Features
id: digital-features
---

### Dark Mode

Pixelmart is a full dark mode theme. Every element — header, footer, product cards, cart drawer, modals, popups, and all UI components — is styled with a dark background palette, glassmorphism card effects, and neon accent colors.

**Setup:**

1. Dark mode is the default and only mode for Pixelmart. No toggle is needed.
2. To customize dark colors, go to **Theme settings > Colors**.
3. Adjustable settings include:
   - **Background** — Main page background (default: `#0a0a0f`)
   - **Surface** — Card and section backgrounds (default: `#14141f`)
   - **Border** — Subtle borders and dividers
   - **Text** — Primary and secondary text colors
   - **Accent** — Neon highlight color used for buttons, links, and badges

> **Tip:** Keep contrast ratios above 4.5:1 for accessibility. The default palette is WCAG AA compliant.

### File Info Display

The file info display shows format, file size, version number, and last update date on product pages, giving buyers essential details about the digital product before purchasing.

**Setup:**

1. Create the following **product metafields** in Shopify Admin:
   - `custom.file_format` (Single line text) — e.g., "PSD", "AI", "FIGMA", "ZIP"
   - `custom.file_size` (Single line text) — e.g., "245 MB"
   - `custom.file_version` (Single line text) — e.g., "2.1.0"
   - `custom.last_updated` (Date) — The date of the last file update
2. The info box renders automatically on any product page where at least one metafield has a value.
3. To reorder or hide specific fields, go to **Theme settings > Product Page > File Info**.

> **Tip:** Keep file size and version up to date whenever you release a new version. Customers value transparency about what they are downloading.

### File Tree Preview

The file tree preview displays a terminal-style representation of the ZIP file structure, so buyers can see exactly what files are included before purchasing.

**Setup:**

1. Create a **product metafield** with the namespace and key `custom.file_tree`.
2. Set the metafield type to **Multi-line text**.
3. Enter the file structure using indented plain text, for example:
   ```
   ui-kit-v2.zip
   ├── Components/
   │   ├── Buttons.psd
   │   ├── Cards.psd
   │   └── Forms.psd
   ├── Icons/
   │   ├── icon-set-outlined.svg
   │   └── icon-set-filled.svg
   ├── README.md
   └── License.txt
   ```
4. If no metafield is set, a default placeholder tree is displayed showing a generic file structure.

> **Tip:** Use tree-drawing characters (├── │ └──) for an authentic terminal look. The theme renders them in a monospace font with dark terminal styling.

### Compatibility Checker

The compatibility checker displays checkmark badges for supported software (Photoshop, Figma, Sketch, Illustrator, etc.) on the product page, helping buyers confirm the file works with their tools.

**Setup:**

1. Create a **product metafield** with the namespace and key `custom.compatibility`.
2. Set the metafield type to **Single line text (List)**.
3. Add entries for each supported application, e.g., `Photoshop`, `Figma`, `Sketch`, `Illustrator`, `XD`.
4. The theme renders each entry as a checkmark badge with the application icon.

> **Tip:** Use consistent application names across products so customers can filter by compatibility.

### License Selector

The license selector displays product variants as styled radio cards instead of a standard dropdown, ideal for Personal, Commercial, and Extended license tiers.

**Setup:**

1. In **Shopify Admin > Products**, create a product option named `License` (or your preferred name).
2. Add variants such as:
   - **Personal** — $29
   - **Commercial** — $59
   - **Extended** — $99
3. The theme automatically detects the variant option and renders radio cards with the variant name and price.
4. To add descriptions to each license tier, create a **product metafield** `custom.license_descriptions` (JSON) with the format:
   ```json
   {
     "Personal": "For personal, non-commercial projects",
     "Commercial": "For client work and commercial projects",
     "Extended": "Unlimited usage including SaaS and resale"
   }
   ```

> **Tip:** Keep license tier names short (1-2 words) for the cleanest card layout.

### License Table

The license table section displays a side-by-side comparison of license tiers with feature checkmarks, helping buyers choose the right license.

**Setup:**

1. In the theme editor, click **Add section > License Table** on the product page template.
2. Configure the table columns (one per license tier).
3. For each tier, set:
   - **Tier Name** — e.g., "Personal", "Commercial", "Extended"
   - **Price** — e.g., "$29", "$59", "$99"
   - **Features** — Toggle checkmarks for each feature row
4. Feature rows are shared across all tiers and configured in the section settings.

**Default feature rows include:**
- Use in personal projects
- Use in commercial projects
- Use in client projects
- Modify and edit
- Remove attribution
- Use in SaaS products
- Resale/redistribution rights

> **Tip:** Highlight the most popular tier with the "Recommended" badge option in the tier settings.

### Bundle Builder

The bundle builder section lets customers select multiple digital products and add them all to cart with a bundle discount.

**Setup:**

1. In the theme editor, click **Add section > Bundle Builder** on any page template.
2. Configure the section settings:
   - **Title** — e.g., "Build Your Bundle"
   - **Collection** — Select the collection of products to display
   - **Minimum items** — Minimum products to qualify for discount (default: 2)
   - **Discount percentage** — Bundle discount amount (default: 20%)
3. Customers check products they want, the section calculates the total with discount, and clicking "Add Bundle to Cart" adds all selected products.

> **Tip:** Create a dedicated "Bundle Eligible" collection for curated bundle offerings rather than using your entire catalog.

### Format Badge

Format badges display file type indicators (PSD, AI, FIGMA, SVG, etc.) on product cards in collection pages and grids, helping buyers identify file formats at a glance.

**Setup:**

1. Add product tags using the format `format:PSD`, `format:AI`, `format:FIGMA`, etc.
2. The theme automatically reads tags prefixed with `format:` and renders them as small colored badges on the product card.
3. To customize badge colors per format, go to **Theme settings > Product Card > Format Badges**.

**Default format colors:**
- **PSD** — Blue
- **AI** — Orange
- **FIGMA** — Purple
- **SKETCH** — Yellow
- **SVG** — Green
- **ZIP** — Gray

> **Tip:** Use consistent format tag names across your catalog. A product can have multiple format badges if it includes several file types.

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

### Subscription Products (App Required)

The theme displays "Subscribe & Save" badges on product cards for products tagged with `subscription`. However, **actual subscription checkout requires a Shopify subscription app**.

| App | Cost | Best For |
|-----|------|----------|
| **Shopify Subscriptions** | Free | Basic subscription needs |
| **Recharge** | $99/mo | Advanced features, analytics |
| **Loop Subscriptions** | $99/mo | Growing brands |
| **Seal Subscriptions** | Free tier | Small stores getting started |

**What the theme provides:**
- Visual "Subscribe & Save" badge on product cards (tag-based)
- Badge text customizable in Theme Settings > Product Card

**What the app provides:**
- Subscription checkout widget on product pages
- Recurring billing and order management
- Customer subscription portal

After installing a subscription app, its widget will appear on product pages automatically alongside the theme's visual badges.
