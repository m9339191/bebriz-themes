---
title: Coffee & Specialty Food Features
id: coffee-features
---

### Flavor Profile

Flavor profile tags are displayed on product cards and detail pages, giving customers a quick overview of tasting notes for each coffee or food product.

**Setup:**

1. In **Shopify Admin > Products**, add tags to your products using the format `flavor:Chocolate`, `flavor:Nutty`, `flavor:Fruity`, etc.
2. The theme automatically reads tags prefixed with `flavor:` and renders them as styled badges on the product card and product page.
3. To customize badge colors, go to **Theme settings > Coffee Features > Flavor Profile Colors**.

> **Tip:** Use consistent flavor names across your catalog so customers can filter and compare products by tasting notes.

### Roast Level Gauge

The roast level gauge displays a visual Light-to-Dark indicator bar on the product page, helping customers quickly understand the roast intensity.

**Setup:**

1. Create a **product metafield** with the namespace and key `custom.roast_level`.
2. Set the metafield type to **Integer** with a value from 1 (lightest) to 5 (darkest).
3. The gauge renders automatically on any product page where this metafield is present.

| Value | Label |
|-------|-------|
| 1 | Light |
| 2 | Medium-Light |
| 3 | Medium |
| 4 | Medium-Dark |
| 5 | Dark |

> **Tip:** You can customize the gauge colors and labels in **Theme settings > Coffee Features > Roast Gauge**.

### Origin Card

The origin card is a kraft-style card displayed on the product page showing the coffee's region, altitude, process, and variety information sourced from metafields.

**Setup:**

1. Create the following **product metafields** in Shopify Admin:
   - `custom.origin_region` (Single line text) — e.g., "Huila, Colombia"
   - `custom.origin_altitude` (Single line text) — e.g., "1,800 - 2,000 masl"
   - `custom.origin_process` (Single line text) — e.g., "Washed"
   - `custom.origin_variety` (Single line text) — e.g., "Caturra, Castillo"
2. Fill in the metafield values for each product.
3. The origin card automatically appears on the product page when at least one origin metafield has a value.

> **Tip:** The origin card uses a warm kraft-paper aesthetic that matches the BrewHaus design language. No additional styling is needed.

### Brewing Guide

The brewing guide section displays step-by-step method cards with specifications for grind size, coffee-to-water ratio, water temperature, and brew time.

**Setup:**

1. In the theme editor, click **Add section > Brewing Guide**.
2. Click **Add block** to add a brewing method card.
3. For each method, configure:
   - **Method Name** — e.g., "Pour Over", "French Press", "AeroPress"
   - **Grind Size** — e.g., "Medium-Fine"
   - **Ratio** — e.g., "1:16"
   - **Temperature** — e.g., "200°F / 93°C"
   - **Brew Time** — e.g., "3:30"
   - **Steps** — Add numbered steps for the brewing process
4. Each method renders as a card with an icon, specs grid, and step list.

> **Tip:** Add 3-4 brewing methods to give customers useful guidance without overwhelming the page.

### Freshness Counter

The freshness counter displays the number of days since the coffee was roasted, helping customers gauge freshness at a glance.

**Setup:**

1. Create a **product metafield** with the namespace and key `custom.roast_date`.
2. Set the metafield type to **Date**.
3. Enter the roast date for each product.
4. The counter calculates the days since roasting in real time and displays it on the product page.

**Display logic:**

- **0-7 days:** "Freshly Roasted" with a green badge
- **8-21 days:** Shows the day count with a neutral badge
- **22+ days:** Shows the day count with a subtle warning style

> **Tip:** Update the roast date whenever you roast a new batch. Customers value freshness transparency and it builds trust.

### Flavor Wheel

The flavor wheel section displays visual intensity bars for flavor categories like chocolate, nutty, fruity, floral, spicy, and more.

**Setup:**

1. In the theme editor, click **Add section > Flavor Wheel** on the product page template.
2. Click **Add block** for each flavor category.
3. For each flavor, set:
   - **Flavor Name** — e.g., "Chocolate", "Nutty", "Fruity"
   - **Intensity** — A value from 1 to 5
   - **Color** — Choose a color for the intensity bar
4. Bars render horizontally with filled segments matching the intensity value.

> **Tip:** Keep flavor entries to 5-6 categories for the cleanest visual. Use metafields if you want to set values per-product instead of per-template.

### Magazine Grid Collection Layout

The magazine grid is a masonry-style collection layout that features a large hero product, wide feature items, and standard cards in an editorial arrangement.

**Setup:**

1. Go to **Theme settings > Collection Page > Layout**.
2. Select **Magazine Grid** as the collection layout.
3. The first product in the collection becomes the hero card (large, spanning two columns).
4. Every 5th product is displayed as a wide card for visual variety.

**Layout pattern:**

- **Hero card** — First product, full-width with large image and overlay text
- **Standard cards** — 3-column grid with hover effects
- **Wide cards** — Every 5th item spans two columns for editorial rhythm

> **Tip:** Curate your collection sort order so that your most photogenic products land in the hero and wide positions.

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
