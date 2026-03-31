---
title: Supplements & Health Features
id: supplements-features
---

### Ingredient Chart

The ingredient chart displays an interactive SVG donut chart on the product page, showing the breakdown of supplement ingredients with percentages, colors, and descriptions.

**Setup:**

1. In the theme editor, navigate to **Product page > Ingredient Chart** section.
2. Click **Add block** to add ingredients.
3. For each ingredient, set:
   - **Name** — e.g., "Vitamin D3"
   - **Percentage** — e.g., "25"
   - **Color** — Choose a color for the chart segment
   - **Description** — e.g., "Supports bone health and immune function"
4. The chart auto-calculates and renders based on the percentages provided.

> **Tip:** Keep ingredient entries to 6 or fewer for the best visual clarity. Use the "Other" label to group minor ingredients together.

### Stack Builder

The stack builder section allows customers to select multiple supplement products and add them all to cart at once, encouraging bundle purchases.

**Setup:**

1. In the theme editor, click **Add section > Stack Builder**.
2. Choose the **Source collection** that contains the products to display.
3. Configure the **Maximum selections** (default: 5).
4. Customize the **Heading**, **Subheading**, and **Add All to Cart** button text.

**How it works:**

- Customers check the boxes next to the supplements they want.
- A floating bar at the bottom shows the selected count and total price.
- Clicking "Add All to Cart" adds every selected product in one action.

### Certification Badges

Trust badges for FDA, GMP, Non-GMO, Vegan, and other certifications are displayed on the product page below the Add to Cart button.

**How to enable:**

1. Add certification tags to any product in **Shopify Admin > Products**.
2. Supported tags and their badges:
   - `fda-approved` — FDA Approved badge
   - `gmp-certified` — GMP Certified badge
   - `non-gmo` — Non-GMO badge
   - `vegan` — Vegan badge
   - `organic` — Organic badge
   - `third-party-tested` — Third-Party Tested badge

> **Tip:** Add multiple tags to a single product to display several certification badges. The badges appear in a horizontal row and wrap on smaller screens.

### Dosage Guide

The dosage guide displays a styled info box on the product page with suggested use instructions and an optional physician warning.

**Setup:**

1. Go to **Product page > Dosage Guide** section in the theme editor.
2. Set the **Suggested Use** text — e.g., "Take 2 capsules daily with food."
3. Enable or disable the **Physician Warning** toggle.
4. Customize the warning text if needed (default: "Consult your healthcare professional before use if you are pregnant, nursing, or taking medication.").

The dosage guide section automatically appears between the product description and the reviews tab on product pages.

### Results Timeline

The results timeline shows a week-by-week visualization of expected results, helping customers understand the supplement journey.

**Setup:**

1. In the theme editor, click **Add section > Results Timeline**.
2. Click **Add block** for each timeline milestone.
3. For each milestone, set:
   - **Week Label** — e.g., "Week 1-2"
   - **Title** — e.g., "Initial Absorption"
   - **Description** — e.g., "Your body begins absorbing key nutrients and building baseline levels."
4. The timeline renders as a vertical progression with connecting lines.

> **Note:** Results timelines are informational only. Always include a disclaimer that individual results may vary.

### Category Tab Bar

The category tab bar auto-generates horizontal tabs from your product types, allowing quick filtering on collection pages.

**Setup:**

1. Go to **Theme settings > Collection Page > Category Tabs**.
2. Check **Enable Category Tabs**.
3. The tabs are automatically generated from the **product types** in the current collection.
4. When a collection has more tabs than fit on screen, scroll arrows appear on both sides.

**How it works:**

- Clicking a tab filters the collection to show only products of that type.
- An "All" tab is always shown first to reset filtering.
- Active tab state is indicated with an underline accent.

### List / Grid View Toggle

The collection page defaults to list view, which shows more product information including ingredient highlights and certification badges. Customers can switch to grid view using the toggle.

**Setup:**

1. Go to **Theme settings > Collection Page > Default View**.
2. Choose **List** or **Grid** as the default layout.
3. The toggle button appears at the top of the collection, next to the sort dropdown.

- **List view** — Shows product image, title, price, short description, and certification badges in a horizontal layout.
- **Grid view** — Shows a traditional card layout with image, title, and price.

> **Tip:** List view works especially well for supplement stores where customers want to compare ingredient details at a glance before clicking into a product.

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
