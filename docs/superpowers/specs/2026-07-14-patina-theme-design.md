# Patina — Shopify OS 2.0 Handcrafted-Scrapbook Jewelry Theme (Design Spec)

Date: 2026-07-14
Status: Approved (established fork pipeline)
Design reference: `Gemini_Generated_Image_y17hahy17hahy17h.png` (AURORA FINE craft variant)

## Goal

Build "Patina" by forking Aurora (themes/aurora @ HEAD): same accessories-shop
section structure and ALL commerce boosters, re-skinned to a distressed-paper /
scrapbook craft aesthetic. Ships as `patina-theme-1.0.0.zip`.

## Design System (from mockup swatches + art)

- Colors: Distressed Paper `#F0E8D8` (bg), Worn Ink `#2B2925` (text), Raw
  Silver/Tan kraft `#C9B08D` (accent 1), deep kraft `#A98F68` (accent 2),
  turquoise accent `#4E9A8E` (accent 3 — from the jewelry stones), light card
  paper `#F7F2E7`, dark text `#2B2925`.
- Typography: TYPEWRITER headlines — Shopify library lacks one, so BUNDLE OFL/
  Apache web fonts in assets: Special Elite (headlines) + Caveat (handwritten
  accents), loaded via @font-face; checkbox setting `use_craft_fonts`
  (default true) switches headings to the bundled stack, otherwise the font
  picker value applies. Eyebrows/accents use `.hand` (Caveat) class.
- Craft utilities (CSS-only where possible):
  - `.torn` — torn-paper edges (SVG mask data-URI, top/bottom variants)
  - `.paper` — subtle paper-grain background (tiny tiled data-URI texture)
  - `.tape` — washi-tape strip pseudo-elements (rotated, semi-transparent)
  - `.polaroid` — white frame + bottom chin + soft shadow; tilt variants
    `.tilt-1/-2/-3` (±1.5–3deg)
  - doodle accents (stars/moon/arrow inline SVGs) sprinkled sparsely
- Buttons: "stamped label" style — worn-ink block with slightly rough edge
  (tiny irregular clip-path), paper-tone label, typewriter font.

## Structural deltas vs Aurora

- All Aurora sections + boosters retained (spotlight, origin-story,
  direct-purchase, trust-badges, lookbook, countdown, upsell, pairs-well-with,
  hero video/photo modes).
- Reskins: hero (handwritten eyebrow + doodles + torn label CTA), spotlight
  (torn-paper card, callouts in typewriter), origin-story (torn photos +
  tape label), lookbook (polaroid collage w/ tape + tilts), bestsellers =
  "High-volume D2C grid" (torn paper cards, visible prices), testimonials in
  direct-purchase become polaroid-styled.
- NEW `sections/social-proof.liquid`: horizontal strip of polaroid quote
  cards (image + handwritten quote + author), ≤6 blocks, tilts.
- Bundled media: 5 hero photos (boho silver/turquoise jewelry) + Remotion
  loop variant (kraft paper bg, drifting hand-drawn star/moon doodles, subtle
  grain — 8s seamless, ≤4MB) + poster.
- Branding: Aurora strings → Patina; brand mark icon 'star' doodle style.

## Non-Goals

Same as Aurora (no pricing logic, no review apps). No parallax/scroll-jack.

## Verification

Aurora-T5-style sweep + theme check 0 errors + bundled font files present +
zip layout; harness render check for fonts/torn edges/video.
