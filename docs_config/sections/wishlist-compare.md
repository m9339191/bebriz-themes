---
title: Wishlist & Compare
id: wishlist-compare
---

Luxe Fashion includes a built-in wishlist and product comparison feature that requires no third-party apps or external services.

### How They Work

Both features use the browser's `localStorage` API to save product selections on the client side. This means data persists across browser sessions on the same device without requiring customer accounts, logins, or any server-side storage.

- **Wishlist** — Customers click the heart icon on any product card or product page to add it to their wishlist. A dedicated wishlist page (automatically created at `/pages/wishlist`) displays all saved products in a grid layout. Products can be added to cart directly from the wishlist or removed individually.
- **Compare** — Customers can add up to 4 products to a comparison list using the compare icon on product cards. A floating compare bar appears at the bottom of the screen showing selected products. Clicking "Compare" opens a modal with a side-by-side table of product attributes including price, availability, variant options, and description.

### Data Storage

Wishlist and compare data is stored under the keys `bebriz_wishlist` and `bebriz_compare` in localStorage. Each entry stores the product handle, title, image URL, price, and availability status. The data is automatically cleaned up if a product is no longer available when the wishlist page loads.

> **Note:** Since localStorage is browser-specific, wishlist and compare data will not sync across different devices or browsers. If a customer clears their browser data, saved items will be removed. For cross-device persistence, consider integrating a Shopify customer metafield-based solution.
