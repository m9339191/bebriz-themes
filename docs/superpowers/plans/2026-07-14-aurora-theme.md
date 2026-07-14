# Aurora Shopify Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development task-by-task. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Fork Meowhaus (@ e4676eb) into `themes/aurora/`, re-skin to the AURORA FINE mockup (ivory/champagne editorial serif, near-square minimal), add jewelry sections + app-replacing commerce boosters (upsell/cross-sell/countdown), bundle 5 hero images + 1 Remotion video, ship `aurora-theme-1.0.0.zip`.

**Architecture:** Same as Volt/Meowhaus. New JS kept in theme.js (countdown element, upsell quick-add reuses existing quick-add-button; video needs no JS beyond autoplay attrs).

**Tech Stack:** Liquid, vanilla JS/CSS, Shopify CLI theme check, Python (sweep+zip), Node+Remotion (video build, scratch project outside theme).

## Global Constraints

- Source `C:\Users\DJMOON\bebriz-themes\themes\aurora\`, standalone nested git (init at fork, commit per task; user m9339191 / 12160564+m9339191@users.noreply.github.com). Parent .gitignore: `themes/aurora/*`, `!themes/aurora/index.html`, `aurora-theme-*.zip`. Never commit theme source to parent.
- Verify per task: `shopify theme check --path "C:/Users/DJMOON/bebriz-themes/themes/aurora"` → 0 errors (2 known main-login info warnings OK); `node --check assets/theme.js` when touched.
- Tokens: bg `#F7F4EF`, text `#26221C`, accent_1 `#C4A265` champagne, accent_2 `#A9967C` taupe, accent_3 `#8A6D3F` bronze, light `#FFFFFF`, dark text `#26221C`. `--radius: 2px`; buttons slim rectangles (radius 2px, NOT pills), 1px hairline borders; heading font picker default a Cormorant Garamond-class serif handle (verify with theme check; fallback playfair_display_n5/n7); eyebrows letter-spacing .14em small caps.
- Liquid landmines (never reintroduce): no filters in {% form %} args; no filters in bracket indices; hoist alt|default out of image_tag args; fieldset-scoped [data-option-position] selectors in JS.
- Icon additions: sparkle, shield, hand-heart, infinity, clock (keep existing set; brand mark = sparkle).
- Commerce boosters must be PORTABLE (self-contained sections/snippets + one JS element) for later backport to Volt/Meowhaus.

---

### Task 1: Fork, tokens, typography, shape, branding
Copy themes/meowhaus → themes/aurora (exclude .git/.superpowers); fresh git init + fork commit; settings_schema/theme_info Aurora/bebriz/1.0.0 + color/font defaults (serif handle verified) + settings_data match; base.css: radius 2px, UN-pill buttons (Meowhaus made .button 999px — revert to 2px slim rectangles w/ letter-spaced uppercase label), hairline borders, eyebrow utility letter-spacing, palette audit (sage/oak assumptions → champagne/taupe); icon.liquid + sparkle/shield/hand-heart/infinity/clock, brand mark paw→sparkle render sites; locales Meowhaus→Aurora strings; delete assets/hero-cats-*.jpg; hero-banner preset options relabeled (files replaced in T4 — temporarily point options at hero-jewels-1..5.jpg names); accent labels Sage/Oak/Clay→Champagne/Taupe/Bronze (labels only); parent .gitignore. Grep `meowhaus|cat-` copy defaults → neutralize obvious ones (deep copy rewrite in T3). Theme check + commit.

### Task 2: Commerce boosters (portable)
- NEW sections/countdown-banner.liquid: heading, subtext, end datetime (text setting ISO "YYYY-MM-DDTHH:MM", timezone note), scheme, on-expiry select (hide|swap message + message text); `<countdown-timer>` element in theme.js (data-end attr, renders DD:HH:MM:SS boxes, 1s tick, expiry behavior, no layout shift).
- main-product.liquid: new block type "countdown" (label + end datetime + expired text) reusing the same element inline.
- NEW snippets/upsell-row.liquid: params heading, products (array), context ('drawer'|'page') — compact cards (img, title, price, quick-add single-variant else link).
- cart-drawer.liquid + main-cart.liquid: "Complete the look" upsell — section settings: enable, heading, up to 4 manual product picks; else fallback to cart-item recommendations (first line item, intent related, via existing product-recommendations element pattern fetching section render — keep simple: manual picks render server-side; recommendations mode uses `routes.product_recommendations_url` fetch wrapper already in theme.js). Drawer refresh must not duplicate listeners (delegation).
- NEW sections/pairs-well-with.liquid: product-page-oriented cross-sell ("Pairs well with") — uses recommendations w/ intent=complementary (falls back to related, then manual picks); added to product.json below main-product.
- Verify: theme check, node --check, no landmines; commit.

### Task 3: Jewelry sections + index.json
- NEW product-spotlight (annotated callouts: up to 6 text blocks side select left|right + vertical offset range; hairline connector lines CSS; center product image from featured product; eyebrow+heading).
- NEW origin-story (eyebrow "Our Origin Story", heading, prose, big+small image pair, link).
- NEW direct-purchase (featured product: media, variant selects via existing variant-picker snippet? product-form full reuse — simplest correct: render buy card with form 'product' + variant-picker + qty + ATC using existing elements; plus up to 3 testimonial blocks: quote/author/avatar).
- NEW trust-badges (up to 5 icon+label blocks, icon select from set).
- lookbook editorial pass ("Shop the Look" tile label option). hero-banner: text_position + light scrim tuned for portrait model shots.
- index.json rewrite: hero-banner, trust-badges, product-spotlight, origin-story, lookbook, direct-purchase, bestsellers("Signature Pieces"); product.json += pairs-well-with + countdown block available. Copy defaults: Aurora Fine voice ("Worn by Stars, Defined by You." etc.).
- Verify + commit.

### Task 4: Bundled media (5 hero images + Remotion video)
- 5 Pexels jewelry lifestyle images (verified 200) → assets/hero-jewels-1..5.jpg (2200×1200); hero-banner preset select labels match.
- Remotion scratch project (scratchpad, Node): 8s 1920×1080 30fps seamless loop — ivory→champagne gradient, ~40 drifting soft gold bokeh particles (deterministic seeded), faint serif "AURORA" shimmer sweep; render H.264 CRF high-compression target ≤4MB → assets/hero-aurora.mp4 + poster frame → assets/hero-aurora-poster.jpg.
- hero-banner.liquid: media_type select image|video (video = bundled mp4: `<video muted loop autoplay playsinline preload="metadata" poster>`; reduced-motion: pause via CSS/JS courtesy + poster fallback; image mode unchanged incl. picker/preset).
- Verify video loads in local harness (browse) + theme check + commit.

### Task 5: Final validation + packaging
Meowhaus-T4-style sweep (JSON/render/section/locale/icon refs; settings_data⊆schema; banned patterns incl. `meowhaus|cat-tower|roast`; breakpoints) + fix cheap findings; zip build (7 folders at root, INCLUDES mp4 — confirm size sane) → `aurora-theme-1.0.0.zip`; commit; report.

## Verification checklist (every task)
`shopify theme check --path "C:/Users/DJMOON/bebriz-themes/themes/aurora"` → 0 errors; commit nested repo per task.
