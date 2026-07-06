# Volt Shopify Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete Volt Shopify OS 2.0 coffee theme (Electric Bean Roasters mockup) at `themes/volt/`, passing `shopify theme check` and packaged as an upload-ready zip.

**Architecture:** From-scratch OS 2.0 theme: JSON templates composed of Liquid sections, one shared `base.css` (design tokens as CSS custom properties), one vanilla `theme.js` (custom elements for cart drawer, variant picker, mobile menu). No external libraries, no apps.

**Tech Stack:** Liquid, JSON templates, vanilla JS/CSS, Shopify CLI 3.93.1 (`shopify theme check`), Python 3.13 (JSON validation + zip packaging).

## Global Constraints

- Theme source lives at `C:\Users\DJMOON\bebriz-themes\themes\volt\` and is **git-ignored in the parent repo** (public repo — sellable product must not be published). Version control: standalone `git init` inside `themes/volt/`; commit there after each task.
- Verify after every task: `shopify theme check --path themes/volt` → 0 errors (warnings acceptable, note them).
- Design tokens (settings defaults): bg `#1A2321`, text `#F4F1EA`, mint `#00E0A8`, red `#FF4B33`, blue `#2E5BFF`, light bg `#F4F1EA`, dark text `#121917`.
- CSS custom properties (defined in theme.liquid from settings, consumed everywhere):
  `--color-bg, --color-text, --color-accent-1 (mint), --color-accent-2 (red), --color-accent-3 (blue), --color-light, --color-dark-text, --font-heading-family, --font-body-family, --page-width (default 1440px)`.
- Style rules: `border-radius: 0` everywhere; headings uppercase, `letter-spacing: -0.01em`, weight 900; thick `3px solid` borders; buttons are solid accent blocks with dark text.
- All user-facing strings via `{{ 'key' | t }}` from `locales/en.default.json`. All section/settings labels via `locales/en.default.schema.json` or inline literals (inline literals acceptable — theme check allows; prefer `t:` keys for section names only if time permits: **decision = inline English literals for schema labels** to keep scope down).
- Accessibility: skip-to-content link, `:focus-visible` outlines (2px mint), min 44px touch targets, `prefers-reduced-motion` disables transitions.
- Snippet contracts (exact signatures — every task must match):
  - `{% render 'product-card', product: product, accent_index: forloop.index, show_quick_add: true %}` — accent_index cycles card bg mint/red/blue via `accent_index modulo 3`; tag override `card-mint|card-red|card-blue`.
  - `{% render 'price', product: product %}` — renders `.price` span, sale price + compare-at strikethrough.
  - `{% render 'roast-level', product: product %}` — reads `product.metafields.custom.roast_level.value` (1–5 integer), falls back to tag `roast-N`; renders 5 flame SVGs, filled = level; renders nothing if neither present.
  - `{% render 'icon', name: 'cart' %}` — inline SVG, `aria-hidden="true"`, `stroke="currentColor"`, 24×24. Names: cart, search, account, menu, close, chevron-down, chevron-left, chevron-right, plus, minus, flame, flame-outline, instagram, bolt, bag, cup, mug, shirt, store, trash.
  - `{% render 'quantity-input', id: some_id, value: 1, min: 1 %}`.
- JS custom elements (defined once in `assets/theme.js`, used by name in sections):
  `cart-drawer`, `cart-drawer-item`, `quantity-input`, `variant-picker`, `product-form`, `quick-add-button`, `mobile-menu`, `media-gallery`, `details-collapsible`.
- Cart API: `POST /cart/add.js`, `POST /cart/change.js`, re-render drawer via Section Rendering API (`?sections=cart-drawer`), dispatch `cart:updated` CustomEvent on `document` with `{detail: {cart}}`.
- Every section ends with `{% schema %}` including `"name"`, settings, and (where meaningful) `"presets"` so it appears in the theme editor.
- Sections must render gracefully with zero content: use `placeholder_svg_tag` ('product-1', 'image', 'collection-1') when product/image blank.

## File Structure (complete inventory)

```
themes/volt/
├── layout/theme.liquid              # HTML shell, CSS vars from settings, header/footer groups
├── layout/password.liquid
├── config/settings_schema.json      # theme_info + colors, typography, layout, cart, social
├── config/settings_data.json        # defaults matching Global Constraints tokens
├── locales/en.default.json
├── templates/index.json  product.json  collection.json  list-collections.json
│   cart.json  page.json  page.contact.json  blog.json  article.json
│   search.json  404.json  gift_card.liquid
│   customers/login.json  register.json  account.json  order.json
│   customers/addresses.json  activate_account.json  reset_password.json
├── sections/
│   announcement-bar.liquid  header.liquid  footer.liquid  left-rail.liquid
│   hero-collage.liquid  featured-grid.liquid  bestsellers.liquid
│   community-grid.liquid  cafe-finder.liquid  story.liquid  newsletter.liquid
│   cart-drawer.liquid
│   main-product.liquid  main-collection.liquid  main-list-collections.liquid
│   main-cart.liquid  main-search.liquid  main-404.liquid  main-page.liquid
│   main-contact.liquid  main-blog.liquid  main-article.liquid  main-password.liquid
│   main-login.liquid  main-register.liquid  main-account.liquid  main-order.liquid
│   main-addresses.liquid  main-activate-account.liquid  main-reset-password.liquid
├── snippets/ product-card.liquid  price.liquid  roast-level.liquid  icon.liquid
│   quantity-input.liquid  pagination.liquid  meta-tags.liquid
│   cart-drawer-items.liquid  variant-picker.liquid
└── assets/ base.css  theme.js
```

---

### Task 1: Scaffold, config, locales, layout, base.css

**Files:** Create `layout/theme.liquid`, `layout/password.liquid`, `config/settings_schema.json`, `config/settings_data.json`, `locales/en.default.json`, `assets/base.css`, `snippets/meta-tags.liquid`, `snippets/icon.liquid`, plus minimal `templates/index.json` + `sections/hero-collage.liquid` stub (theme check requires valid refs).

**Produces:** CSS custom properties per Global Constraints; `.button`, `.button--secondary`, `.section-heading`, `.page-width`, `.grid` utility classes; icon snippet with all names listed above.

- [ ] Step 1: `git init` in themes/volt, create folder tree.
- [ ] Step 2: settings_schema.json — theme_info (Volt, bebriz, 1.0.0) + panels: Colors (background, text, accent_1, accent_2, accent_3, light_background, dark_text), Typography (heading font_picker default `archivo_n7`? → use `assistant_n4` body / heading picker default `archivo_black_n4` if unavailable fall back to `oswald_n6`; verify with theme check — font handles must be valid Shopify font library handles: use `oswald_n6` heading, `assistant_n4` body as safe defaults), Layout (page_width range 1200–1600 default 1440, left rail enable checkbox), Cart (drawer/page select, free shipping threshold), Social (instagram_url, twitter_url, facebook_url).
- [ ] Step 3: theme.liquid — doctype shell: meta-tags render, CSS vars in `:root` from settings (color settings via `.red`, `.green`, `.blue` channels for rgba use), font_face filters, preload base.css, skip link, sections group render: announcement-bar/header via `{% sections 'header-group' %}`… **decision: render sections directly** (`{% section 'announcement-bar' %}`, `{% section 'header' %}`, `{% section 'left-rail' %}`, `{{ content_for_layout }}`, `{% section 'footer' %}`, `{% section 'cart-drawer' %}`) — simpler than section groups, valid OS 2.0.
- [ ] Step 4: base.css — reset, tokens usage, typography (uppercase 900 headings, clamp() sizes), buttons, forms, grid/page-width utilities, focus-visible, reduced-motion block, `.color-block--1/2/3` card background classes.
- [ ] Step 5: en.default.json — general/header/cart/products/search/blogs/customer/forms/404 key groups (standard Dawn-like key naming, hand-written).
- [ ] Step 6: Verify `shopify theme check --path themes/volt` → 0 errors. Commit (nested repo).

### Task 2: Core snippets

**Files:** Create `snippets/price.liquid`, `roast-level.liquid`, `product-card.liquid`, `quantity-input.liquid`, `pagination.liquid`.

**Consumes:** icon snippet, `.color-block--N` classes. **Produces:** contracts in Global Constraints.

- [ ] price.liquid: `price`, `price--on-sale`, compare_at with `<s>`, money filter, unit price support.
- [ ] roast-level.liquid: metafield → tag fallback → nothing; 5 flames with `aria-label="Roast level N of 5"`.
- [ ] product-card.liquid: `<article class="product-card color-block--{N}">` — accent from tag override else `accent_index` cycle; image (or placeholder_svg_tag), title uppercase, price render, roast-level render, quick-add button (`quick-add-button` element, only when single variant & available; else link), whole-card link overlay.
- [ ] pagination.liquid: paginate object → prev/next + numbered, mint current.
- [ ] Verify: theme check 0 errors; commit.

### Task 3: Header, footer, announcement bar, left rail, mobile menu

**Files:** Create `sections/announcement-bar.liquid`, `header.liquid`, `footer.liquid`, `left-rail.liquid`; extend `assets/theme.js` (`mobile-menu` element).

**Design:** header = red (`--color-accent-2`) bar per mockup: left nav links, centered uppercase shop name/logo, right search/account/cart icons with cart count bubble; sticky. Left rail = fixed mint 68px column, brand bolt mark top, vertical icon links (linklist `left-rail` menu fallback to main-menu, icon per link via handleized title match: beans→bag, merch→shirt, cafe/locations→store, else cup), desktop ≥1200px only; body gets left padding via CSS when enabled. Footer = dark, 3 columns (menu, newsletter form `customer_form`, social icons) + payment icons.

- [ ] Build 4 sections with schemas (announcement text/link/colors; header menu picker + sticky checkbox; footer menu picker + newsletter toggle; left-rail menu picker).
- [ ] theme.js: `mobile-menu` custom element — hamburger toggles full-viewport overlay panel (solid bg, per past bugfix learnings), focus trap, Escape closes, `aria-expanded`.
- [ ] Verify: theme check 0 errors; commit.

### Task 4: Cart drawer + Cart API JS + quick add

**Files:** Create `sections/cart-drawer.liquid`, `snippets/cart-drawer-items.liquid`; extend `theme.js` (`cart-drawer`, `cart-drawer-item`, `quantity-input`, `quick-add-button`).

**Produces:** `window` behavior: any `quick-add-button` posts `/cart/add.js` then fetches `?sections=cart-drawer`, swaps drawer innerHTML, opens drawer, dispatches `cart:updated`. Header cart icon opens drawer (or links to /cart when setting = page).

- [ ] cart-drawer.liquid: `<cart-drawer>` overlay right panel — free shipping progress bar (threshold setting × 100 vs cart.total_price), line items via snippet (image, title, options, quantity-input, remove trash icon, line price), subtotal, checkout button (mint), continue-shopping close.
- [ ] JS: change.js on quantity/remove with line index; optimistic disable during fetch; error message region `role="status"`.
- [ ] Verify: theme check 0 errors; commit.

### Task 5: Homepage sections + index.json

**Files:** Create `sections/hero-collage.liquid` (replace stub), `featured-grid.liquid`, `bestsellers.liquid`, `community-grid.liquid`, `cafe-finder.liquid`, `story.liquid`, `newsletter.liquid`; finalize `templates/index.json` with all six in mockup order.

- [ ] hero-collage: up to 5 image blocks in CSS grid strip (differing column spans), overlay headline 2 lines (settings heading_1/heading_2, white uppercase clamp(2.5rem,6vw,5.5rem)), optional CTA; placeholder images when blank.
- [ ] featured-grid: block type "product" (product picker + accent color select + size select normal/wide); mosaic grid `grid-template-columns: repeat(12, 1fr)`, wide = span 8, normal = span 4; tile = color block w/ big product image, uppercase name bottom-left, roast-level; section footer giant outline text heading setting ("ELECTRIC BEAN ROASTERY" style, first word mint).
- [ ] bestsellers: light bg (`--color-light`), centered heading, collection picker, products_to_show range 2–8 default 4, grid → horizontal scroll-snap on mobile, uses product-card.
- [ ] community-grid: dark bg, heading + instagram icon link, 8 image blocks 4-col grid (2-col mobile).
- [ ] cafe-finder: full-width image bg w/ dark overlay, huge heading, CTA button (mint) to page/url.
- [ ] story: rich text, eyebrow + heading + text + link, light/dark scheme select. newsletter: heading + customer form (email, submit mint button, success/error states).
- [ ] index.json ordering: hero-collage, featured-grid, bestsellers, community-grid, cafe-finder, newsletter.
- [ ] Verify: theme check 0 errors; commit.

### Task 6: Product template

**Files:** Create `sections/main-product.liquid`, `snippets/variant-picker.liquid`; extend `theme.js` (`variant-picker`, `product-form`, `media-gallery`, `details-collapsible`); `templates/product.json`.

- [ ] Layout: 2-col (gallery left sticky, info right). Gallery: main media + thumbnail row, `media-gallery` element swaps on click, supports video/model fallback via `media` object.
- [ ] Info: vendor eyebrow, H1, price, roast-level, variant-picker (button swatches per option, `input[type=radio]` visually-hidden pattern), quantity, `product-form` (add to cart → drawer flow, uses `/cart/add.js`), `{{ form | payment_button }}` dynamic checkout, description, collapsible blocks (@app? no — block types: collapsible_tab title+richtext, shipping default), share.
- [ ] variant-picker JS: on change → match variant from `product.variants` JSON script tag, update price/availability/media/url (`replaceState`), disable sold-out combos.
- [ ] product.json: main-product + bestsellers preset as "You may also like" (collection = blank → uses recommendations? **decision: add `related-products` capability into bestsellers section via optional `use_recommendations` checkbox using `recommendations.products`**; product.json includes bestsellers with that flag).
- [ ] Verify: theme check 0 errors; commit.

### Task 7: Collection, search, static pages, blog

**Files:** Create `sections/main-collection.liquid`, `main-list-collections.liquid`, `main-search.liquid`, `main-404.liquid`, `main-page.liquid`, `main-contact.liquid`, `main-blog.liquid`, `main-article.liquid`; templates collection.json, list-collections.json, search.json, 404.json, page.json, page.contact.json, blog.json, article.json.

- [ ] main-collection: banner (title + description + collection image bg option), toolbar (sort_by select form + product count; storefront filtering via `collection.filters` checkboxes in `<details>` dropdowns), paginate 12/24 setting, product-card grid, empty state.
- [ ] main-search: search form + results grid (product cards; article/page results as simple list), paginate.
- [ ] main-404: giant "404" outline text + mint CTA home. main-page: narrow prose column. main-contact: contact form (name/email/phone/message) + shop info column.
- [ ] main-blog: article card grid (image, date, title, excerpt). main-article: hero image, meta, prose, comments form when enabled.
- [ ] Verify: theme check 0 errors; commit.

### Task 8: Cart page, password, customers, gift card

**Files:** Create `sections/main-cart.liquid`, `main-password.liquid`, all 7 customer main-* sections; templates cart.json, customers/*.json, `templates/gift_card.liquid`; `layout/password.liquid` finalize.

- [ ] main-cart: full-width table (item/qty/total), same JS as drawer (`cart-items` reuse cart-drawer-item element), note field, subtotal + checkout.
- [ ] customers: standard forms (`form 'customer_login'`, `'create_customer'`, `'recover_customer'`, `'customer_address'` CRUD w/ country selects + `Shopify.CountryProvinceSelector`? **decision: plain `all_country_option_tags` + small inline script**, `'activate_customer_account'`, `'reset_customer_password'`), account = order table + addresses link, order = line items detail. Volt styling: centered 480px dark cards, mint submits.
- [ ] password layout+section: centered logo, headline, password form + newsletter. gift_card.liquid: standard printable card w/ code + QR (`gift_card.qr_identifier` via Shopify's qrcode.js asset? **decision: skip QR script, show code text + apply URL** — acceptable).
- [ ] Verify: theme check 0 errors; commit.

### Task 9: Polish pass + final validation + packaging

- [ ] Run `shopify theme check --path themes/volt` full output review; fix ALL errors, fix warnings where cheap (missing alt, img width/height, remote asset, etc.).
- [ ] Python sweep: validate every `.json` parses; grep every `{% render '...' %}` target exists; grep every `"type": "..."` in templates has matching section file.
- [ ] Responsive audit of base.css breakpoints (750px, 990px, 1200px rail).
- [ ] Package: python zipfile → `volt-theme-1.0.0.zip` containing assets/config/layout/locales/sections/snippets/templates at zip root (Shopify upload format). Place zip in repo root (gitignored).
- [ ] Final nested-repo commit + report summary to user.

## Verification checklist (every task)

```
shopify theme check --path "C:/Users/DJMOON/bebriz-themes/themes/volt"
```
Expected: `0 errors`. Then `git -C themes/volt add -A && git -C themes/volt commit -m "..."`.
