# Meowhaus — Shopify OS 2.0 Cat Furniture & Toys Theme (Design Spec)

Date: 2026-07-13
Status: Approved (same pipeline as Volt per owner request)
Design reference: `Gemini_Generated_Image_e48i0ee48i0ee48i.png` (MEOWHAUS mockup)

## Goal

Build "Meowhaus", a sellable Shopify OS 2.0 theme for cat furniture / toy stores
(cat towers, scratchers, interactive toys, beds), by FORKING the completed Volt
theme (themes/volt @ 9c8f8c0) and re-skinning + adapting it to the Meowhaus
mockup. Source lives at `themes/meowhaus/` (standalone nested git repo,
git-ignored in the public parent repo). Ships as `meowhaus-theme-1.0.0.zip`.

## Why fork Volt

Volt carries battle-tested infrastructure this theme reuses unchanged in
behavior: AJAX cart drawer (queued refresh, note preservation, focus restore),
quick add, variant picker (bracket-index and form-tag Liquid fixes), media
gallery incl. 3D, storefront filters, customer accounts, gift card, no-JS
fallbacks, a11y. Only the skin and several home sections change.

## Design System (from mockup — all exposed as settings)

- Colors (defaults):
  - Background cream `#F6F1E6`
  - Text warm dark brown `#2F2A23`
  - Accent 1 sage green `#A9BFA0` (buttons, highlights)
  - Accent 2 warm oak/tan `#C6976B`
  - Accent 3 soft clay `#B77E5C`
  - Light surface `#FFFDF7` (cards)
  - Dark text `#2F2A23`
- Typography: serif display headings (Shopify font picker default a Playfair
  Display-class serif handle), sentence-case headlines (NOT uppercase), clean
  sans body. Buttons: small caps/uppercase allowed on pills.
- Shape language: ROUNDED — `--radius: 14px` base, pill buttons
  (border-radius 999px), circular category medallions, rounded cards; thin
  1px warm borders (not thick 3px).
- Decorative motifs: subtle paw-print / leaf accents (inline SVG, low
  opacity) on section backgrounds — tasteful, sparse.
- Left rail: EXISTS but default OFF (mockup has none).

## Structural deltas vs Volt

Same file inventory as Volt, plus/minus:

- REPLACE hero-collage with **hero-banner**: full-width image, eyebrow text,
  serif 2-line headline, pill CTA, optional light overlay, adjustable height.
  (hero-collage file may remain for variety but index.json uses hero-banner.)
- NEW **explore-categories**: heading + up to 8 blocks (collection picker +
  circular image/illustration + label), 4-across desktop / 2 mobile.
- NEW **lookbook**: heading ("The Lookbook: Inspiring Homes") + image blocks
  (image + optional product link) in a staggered grid, tag-icon badge on
  linked tiles.
- ADAPT bestsellers → **fan-favorites** styling: light rounded cards, price,
  optional star rating (product.metafields.reviews.rating when present,
  hidden otherwise), pill "Add to Cart" quick-add.
- REMOVE roast-level from cards/product page (coffee-specific). Keep snippet
  file deleted; no tag/metafield coupling remains.
- Featured-grid (color-block mosaic) retires from the default homepage but the
  section stays available (soft palette variant) for merchant use.
- Newsletter copy: "Join the Club".
- index.json order: hero-banner, explore-categories, lookbook, fan-favorites
  (bestsellers), newsletter.
- Header: cream bar, logo/monogram left, nav inline (Shop All, Cat Towers,
  Toys, Scratchers, Lookbook, Blog via menu), icons right — reuse Volt header
  with recolor + layout tweak (logo left instead of center; keep center as a
  section setting option `logo_position`).
- All Volt-brand strings (Volt, bolt icon defaults, electric copy) replaced
  with Meowhaus equivalents (paw icon brand mark, cat copy). settings_schema
  theme_info: Meowhaus / bebriz / 1.0.0.

## Non-Goals

- No review-app integration (stars only via optional metafield).
- No new JS features; JS is inherited from Volt unchanged except selectors/
  branding.
- No demo-store content creation in this project (products/images separate).

## Verification

- `shopify theme check` 0 errors (2 known form-after-capture info warnings OK)
- Volt's Task-9-style integrity sweep (JSON parse, render/section/locale/icon
  reference resolution, settings_data↔schema id match)
- No remaining "volt"/"roast" strings in user-facing output (grep sweep)
- Package `meowhaus-theme-1.0.0.zip` (zip root = 7 folders)
