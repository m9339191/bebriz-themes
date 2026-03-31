---
title: Kids & Baby Features
id: kids-features
---

### Shop by Age

LittleJoy organizes products into visual emoji-based age group cards, making it easy for parents to find age-appropriate items quickly.

**Setup:**

1. In the theme editor, click **Add section > Shop by Age**.
2. Click **Add block** to create age group cards.
3. For each age group, set:
   - **Emoji** — e.g., "👶", "🧒", "🎒"
   - **Label** — e.g., "Newborn (0-3m)", "Infant (3-12m)", "Toddler (1-3y)", "Preschool (3-5y)", "Big Kids (5+)"
   - **Collection Link** — Link to a collection filtered for that age group
4. Cards display in a horizontal scrollable row on mobile.

**Default age groups:**
- **Newborn** — 0-3 months
- **Infant** — 3-12 months
- **Toddler** — 1-3 years
- **Preschool** — 3-5 years
- **Big Kids** — 5+ years

> **Tip:** Create dedicated collections for each age group and use automated collection rules based on product tags like `age-newborn`, `age-infant`, `age-toddler`, etc.

### Milestone Cards

Milestone cards display growth milestones (First Steps, First Words, Starting School, etc.) with links to relevant product collections, helping parents shop by developmental stage.

**Setup:**

1. In the theme editor, click **Add section > Milestone Cards**.
2. Click **Add block** to add milestones.
3. For each milestone, set:
   - **Emoji** — e.g., "👣", "🗣️", "🎓"
   - **Title** — e.g., "First Steps"
   - **Description** — e.g., "Walking shoes and safety gear for new walkers"
   - **Collection Link** — Link to a relevant product collection
4. Cards display in a grid with pastel backgrounds.

> **Tip:** Milestone cards are great for gift guides and seasonal campaigns. Update them for holidays and back-to-school seasons.

### Safety Badges

Safety certification badges appear automatically on product pages when products are tagged with safety-related tags, building trust with safety-conscious parents.

**How to enable:**

1. Add any of the following tags to products in **Shopify Admin > Products**:
   - `bpa-free` — Displays BPA-Free badge
   - `non-toxic` — Displays Non-Toxic badge
   - `cpsc-certified` — Displays CPSC Certified badge
   - `organic` — Displays Organic badge
   - `eco-friendly` — Displays Eco-Friendly badge
2. Badges appear below the Add to Cart button with colored icons.
3. Multiple badges can be displayed on a single product.

> **Tip:** Use safety badges on all qualifying products. Parents actively look for these certifications and they significantly improve conversion rates.

### Size Recommender

The size recommender widget helps parents choose the right clothing size based on their child's age, reducing returns and improving customer satisfaction.

**Setup:**

1. The size recommender appears automatically on products with a `Size` variant option.
2. To customize the age-to-size mapping, create a **shop metafield** `custom.kids_size_chart` (JSON) with the format:
   ```json
   {
     "Newborn": "NB / 0-3M",
     "3-6 months": "3-6M",
     "6-12 months": "6-12M",
     "12-18 months": "12-18M",
     "18-24 months": "18-24M",
     "2-3 years": "2T-3T",
     "4-5 years": "4T-5T",
     "6-7 years": "6-7"
   }
   ```
3. Parents select the child's age from a dropdown and the recommended size is highlighted.

> **Tip:** Keep the size chart updated for each brand you carry, as sizing can vary between manufacturers.

### Age Filter Bar

The age filter bar displays emoji-based filter buttons on collection pages, allowing customers to quickly filter products by age group.

**Setup:**

1. Go to **Theme settings > Collection Page**.
2. Check **Show Age Filter Bar**.
3. The filter reads product tags prefixed with `age-` (e.g., `age-newborn`, `age-toddler`).
4. Each age group displays as a rounded pill button with its emoji.

> **Tip:** Ensure all products have appropriate age tags for the filter to work effectively across your catalog.

### Bouncy Animations

LittleJoy includes playful CSS animations that give the theme a fun, kid-friendly feel without impacting performance.

**Available animations:**

- **Bounce** — Elements gently bounce on hover (product cards, buttons)
- **Wiggle** — Subtle wiggle animation on emoji and icon elements
- **Float** — Gentle floating motion on hero section bubbles
- **Pop** — Scale-up effect when elements enter the viewport

**To disable animations:**

1. Go to **Theme settings > Animations**.
2. Uncheck **Enable Playful Animations**.
3. Individual animation types can also be toggled independently.

> **Note:** All animations respect the user's `prefers-reduced-motion` system setting for accessibility compliance.

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
