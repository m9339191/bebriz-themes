---
title: Pet & Wellness Features
id: pet-features
---

### Subscription Badge

The subscription badge displays a "Subscribe & Save" label on product cards to visually indicate which products are eligible for recurring purchases.

**How to enable:**

1. Add the tag `subscription` or `auto-refill` to any product in **Shopify Admin > Products**.
2. The badge text can be customized in **Theme settings > Product Card > Subscription Badge Text** (default: "Subscribe & Save 15%").

> **Important:** The badge is a visual indicator only. To enable actual subscription checkout functionality, you need to install a Shopify subscription app:

| App | Cost | Best For |
|-----|------|----------|
| **Shopify Subscriptions** | Free | Basic subscription needs |
| **Recharge** | $99/mo | Advanced features, analytics |
| **Loop Subscriptions** | $99/mo | Growing brands |
| **Seal Subscriptions** | Free tier | Small stores getting started |

After installing a subscription app, its checkout widget will appear on product pages automatically. The theme's badge works independently to attract attention on collection and homepage grids.

### Age Verification Gate

The age verification gate displays a full-screen modal requiring visitors to confirm they are 21 years or older before accessing the store. This is required for stores selling CBD, hemp, or other age-restricted pet wellness products.

**Setup:**

1. Go to **Theme settings > Age Verification**.
2. Check **Enable Age Verification**.
3. Customize the heading, description text, and button labels.
4. Optionally upload a logo to display in the modal.
5. Set a **Deny Redirect URL** — visitors who click "I am under 21" will be redirected to this URL (e.g., Google).

> **Note:** Once a visitor confirms their age, a cookie is stored for 24 hours so they won't see the popup again during that session.

### Feeding Guide Tab

Food and treat products automatically display a "Feeding Guide" tab on the product detail page. This tab shows a weight-based feeding recommendation table.

**How it works:**

- Products with the type `Food`, `Treats`, or the tag `food` will show the feeding guide tab.
- The default table displays recommended daily amounts based on pet weight (up to 10 lbs, 10-25 lbs, 25-50 lbs, 50-75 lbs, 75+ lbs).
- To customize the feeding guide for a specific product, create a **product metafield** named `custom.feeding_guide` with your custom HTML content. This will replace the default table.

### Vet Approved Badge

A trust badge displaying "Vet Approved — Recommended by veterinarians" appears on the product detail page for verified products.

**How to enable:**

1. Add the tag `vet-approved` to any product in **Shopify Admin > Products**.
2. The badge will appear below the Add to Cart button with a green checkmark icon.

> **Tip:** Use this badge for products that have been formulated or reviewed by veterinary professionals. It builds customer trust and can improve conversion rates.

### Pet Profile Cards

A dedicated section for showcasing popular pet breeds with circular photo cards, breed names, temperament info, and links to relevant product collections.

**Setup:**

1. In the theme editor, click **Add section > Pet Profiles**.
2. Click **Add block** to add breed profiles.
3. For each profile, set:
   - **Photo** — Upload a breed photo (square format recommended)
   - **Breed Name** — e.g., "Golden Retriever"
   - **Size** — e.g., "Large"
   - **Temperament** — e.g., "Friendly, Loyal"
   - **Collection Link** — Link to a collection filtered for this breed

### Pet Type Filter

A breed/species filter in the collection sidebar allows customers to filter products by pet type.

**Setup:**

1. Go to **Theme settings > Product Card**.
2. Check **Show Pet Type Filter**.
3. The filter shows checkboxes for: Dogs, Cats, Birds, Fish.
4. Products must have matching tags (`dog`, `cat`, `bird`, `fish`) to appear in filtered results.

> **Tip:** When creating products, add both the pet type tag and breed-specific tags (e.g., `dog`, `golden-retriever`) for the most effective filtering experience.

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
