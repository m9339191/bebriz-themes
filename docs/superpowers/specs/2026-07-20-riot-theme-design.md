# Riot — Shopify OS 2.0 Street/Protest Fashion Theme (Design Spec)

Date: 2026-07-20
Status: Approved (established fork pipeline)
Design reference: `972be0ba-3d52-4162-9fd9-03c50896a5e5.jpg` (ARCHIVE UNKNOWN street mockup)

## Goal

Build "Riot" by forking Patina (themes/patina @ HEAD): same accessories-shop
section structure and ALL commerce boosters, re-skinned to a distressed
street/protest collage aesthetic (concrete wall, scrap fabric tape, neon
glitch stickers, typewriter + marker type, black photo frames, anarchy
doodles). Ships as `riot-theme-1.0.0.zip` PLUS a separate bonus
`riot-canva-banner-templates.zip` (5 hero banner template designs + guide)
for the Etsy listing.

**Fidelity gate:** the user requires 100% match to the mockup. Use the Patina
methodology from the START: per-section zoomed mockup crops + ~50% overlay
comparison against live renders, iterating until each section passes.

## Design System (sampled from mockup swatches)

- Colors: Distressed Concrete `#C9C7C2` (bg, under a real concrete grain
  texture; swatch chip `#878785` = accent 1), Ink `#171715` (text/dark),
  Scrap Fabric Tape `#696967` (accent 2), Neon Glitch `#BBFB35` (accent 3 —
  stickers, prices, ATC block), torn label cream `#E4E2DC` (light).
- Typography: keep bundled Special Elite (typewriter headlines — matches
  "UNRAVELING Order. THE CLOTHING IS OUR PROTEST."); REPLACE Caveat with
  Permanent Marker (Apache-2.0) for the `.hand` class — mockup handwriting
  ("THE UNKNOWN ROAD.", photo captions) is thick marker, not cursive.
- Craft utilities (evolve Patina's):
  - concrete grain texture tile (PIL) replaces kraft cardboard on body
  - `.tape` → gray scrap-fabric tape strips (frayed edge masks, slight
    rotation) replacing washi
  - torn label scraps stay (cream), plus BLACK PHOTO FRAME variant
    (`.frame-hard`: thick black border, hard shadow, slight rotate) for
    lookbook/social photos — mockup photos are black-framed, not polaroid
  - `.sticker-neon`: neon glitch sticker chip (skewed rect, ink text,
    tiny offset "glitch" double-layer) for #SHOP THE LOOK / prices / CTAs
  - doodles: white marker scribbles — circled-A, star, arrow, underline
    stroke (inline SVGs in icon.liquid, drawn hand-style)
  - buttons: bracket CTA style `[LABEL]` (typewriter, ink on label cream)
    and solid neon block ("ADD TO CART / SYSTEM CHECK") with glitch offset
    hover; keep inset double focus ring (WCAG 2.4.7, clip-path lesson).
- Landmine (Patina lesson): `.torn-*`/utility classes must NOT demote flex
  layouts — keep the compound `display:flex` restore rules for
  direct-purchase card + spotlight media, and check any new utility.

## Structural deltas vs Patina (sections all retained + boosters)

- hero-banner: full-bleed street photo, typewriter multi-line headline with
  torn-label eyebrow chip, bracket CTA, small marker note card pinned
  top-right ("We don't just sell clothes. We sell the movement.") — new
  optional `note_text` setting.
- origin-story: photo collage feel (big+small torn photos stay) + huge
  marker headline; copy voice = manifesto.
- product-spotlight: torn label card + typewriter callouts (mockup shows
  sketch w/ callout lines — real product photo + callouts is the productized
  equivalent) + small "360°" doodle badge accent.
- lookbook: B/W-leaning street photos in black hard frames + neon
  `#SHOP THE LOOK` sticker on product-linked tiles (replaces tag badge).
- social-proof: WHITE polaroid frames + marker captions (amended 2026-07-20:
  the mockup's social-proof row is white-bordered polaroids, not black frames
  — mockup wins over the original spec draft; direct-purchase testimonials
  match). Lookbook stays black `.frame-hard`.
- bestsellers ("High-Volume D2C Grid"): gray fabric mats (accent-1 + tape
  texture) with taped top edge and cream MARKER price chips (amended
  2026-07-20: the mockup's D2C grid shows gray mats + handwritten price
  scraps, not black frames/neon prices — mockup wins).
- direct-purchase: neon ATC block, label-cream card on concrete.
- trust-badges: stamped icon row (bottom of mockup).
- Branding: Patina strings → Riot; demo shop voice "ARCHIVE UNKNOWN".

## Bundled media

- 5 hero photos (Pexels, verified live: streetwear/techwear, urban/graffiti,
  landscape 2200×1200) → assets/hero-street-1..5.jpg.
- Remotion loop variant: concrete texture bg + drifting white marker doodles
  + occasional neon glitch scanline flickers, 8s seamless, 1920×1080, ≤4MB
  → assets/hero-riot.mp4 + poster. NO baked wordmark text (Aurora lesson).

## Canva banner bonus (NEW deliverable, separate zip)

`riot-canva-banner-templates.zip`: 5 hero-banner template designs
(2200×1200) in the Riot visual language, each shipped as (a) full sample PNG
with placeholder text, (b) text-free background PNG for Canva editing, plus
`CANVA-GUIDE.txt` (upload background → add text with free Canva fonts
"Special Elite" / "Permanent Marker" → export). Not part of the theme zip
(Shopify upload rejects stray root files); uploaded to Etsy as an extra
digital file.

## Non-Goals

Same as Patina/Aurora. No literal offensive imagery; anarchy-A/pentagram
doodles from the mockup are rendered as generic scribble-star/circled-A
marker doodles.

## Verification

Patina-T4-style sweep + theme check 0 errors + fonts/media/textures present
+ zip layouts (theme zip = 7 std dirs only) + per-section overlay fidelity
loop once the demo store exists.
