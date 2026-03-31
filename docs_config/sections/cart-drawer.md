---
title: Cart Drawer
id: cart-drawer
---

### Setup

The AJAX cart drawer slides in from the right side of the screen when a customer adds a product to the cart, updates without a page reload for a seamless shopping experience. To configure:

1. In the theme editor, go to **Theme settings > Cart**.
1. Set **Cart type** to `Drawer`. Alternatively, choose `Page` for a traditional full-page cart, or `Popup` for a brief notification.
1. Enable **Cart recommendations** to show complementary products inside the cart drawer.
1. Enable **Cart note** to let customers add special instructions to their order.
1. Toggle **Trust badges** to display security and payment icons below the checkout button.

### Free Shipping Bar

The free shipping bar displays a progress indicator showing how much more the customer needs to spend to qualify for free shipping. It updates dynamically as items are added or removed.

1. Navigate to **Theme settings > Cart > Free shipping bar**.
1. Enable the free shipping bar toggle.
1. Set the **Free shipping threshold** amount (e.g., $75, $100). This should match your actual shipping policy.
1. Customize the message text. Use the `{amount}` placeholder for the remaining amount. Example: "You're only {amount} away from free shipping!"

### Auto Discount

If you have automatic discounts configured in Shopify (Admin > Discounts), the cart drawer automatically calculates and displays the discount amount. No additional theme configuration is needed. The discounted price, original price, and savings amount are all shown clearly.

### Terms Checkbox

Require customers to agree to your terms and conditions before proceeding to checkout. Enable this under **Theme settings > Cart > Terms checkbox**. Link the checkbox label text to your terms and conditions page. When enabled, the checkout button remains disabled until the checkbox is checked.
