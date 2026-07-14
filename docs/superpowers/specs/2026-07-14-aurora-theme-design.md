# Aurora — Shopify OS 2.0 Luxury Jewelry Theme (Design Spec)

Date: 2026-07-14
Status: Approved (established fork pipeline)
Design reference: `Gemini_Generated_Image_pz4depz4depz4dep.png` ("AURORA FINE" mockup)

## Goal

Build "Aurora", a sellable Shopify OS 2.0 theme for fine jewelry / luxury
single-hero-product brands, by forking Meowhaus (themes/meowhaus @ e4676eb —
carries all shared-infra fixes). Ships as `aurora-theme-1.0.0.zip` with:
- The mockup's editorial sections (product spotlight w/ material callouts,
  origin story, editorial lookbook, direct-purchase card, trust badges)
- NEW app-replacing commerce boosters (portable, to be backported later):
  cart upsell, cross-sell ("pairs well with"), countdown timers
- 5 bundled hero images + 1 bundled Remotion-rendered hero video, with
  hero-banner video-background support

## Design System (from mockup)

- Colors: ivory `#F7F4EF` bg, warm charcoal `#26221C` text, champagne gold
  `#C4A265` accent 1, soft taupe `#A9967C` accent 2, deep bronze `#8A6D3F`
  accent 3, light `#FFFFFF` cards, dark text `#26221C`.
- Typography: refined display serif headings (Cormorant Garamond-class picker
  default; fallback Playfair), sentence/Title case, wide letter-spaced
  small-caps eyebrows; body clean sans.
- Shape: elegant minimal — radius 2px (near-square, hairline 1px borders),
  buttons slim rectangles (NOT pills), generous whitespace, editorial grids.

## Structural deltas vs Meowhaus

- hero-banner: + video mode (bundled `hero-aurora.mp4` muted loop autoplay
  playsinline + poster; select image|video; 5 bundled jewelry hero images
  hero-jewels-1..5.jpg replacing cat photos).
- NEW product-spotlight: featured product image center, up to 6 annotated
  callout lines (text blocks positioned left/right with hairline connectors),
  per mockup "18k Reclaimed Gold / Ethical Diamond / Custom Engraving".
- NEW origin-story: editorial split — large image + small image pair, eyebrow
  "Our Origin Story", heading, prose, optional link.
- NEW direct-purchase: full product buy card inline on homepage (featured
  product w/ variant selects, qty, ATC via existing product-form JS) + side
  testimonial blocks (quote + author + avatar image).
- NEW trust-badges: horizontal row of icon+label items ("Socially Conscious",
  "Handcrafted Luxury", "Forever Warranty").
- NEW countdown-timer: banner section (headline + end datetime setting +
  live JS countdown, auto-hide or swap message on expiry) AND a product-page
  collapsing block variant (offer ends at X).
- NEW cart upsell: drawer + cart page row "Complete the look" — manual
  product picks (settings) else Shopify recommendations; one-click quick-add.
- NEW cross-sell section: "Pairs well with" — complementary-intent
  recommendations (Search & Discovery) w/ manual fallback list.
- lookbook: reuse (editorial styling pass, "Shop the Look" labels per tile).
- explore-categories → keep file, off homepage.
- index.json: hero-banner(video), trust-badges, product-spotlight,
  origin-story, lookbook, direct-purchase, bestsellers("Signature pieces"),
  cross-sell optional.
- Branding: Meowhaus/cat strings → Aurora/jewelry; icon 'sparkle' brand mark.

## Bundled media

- 5 hero images (Pexels jewelry lifestyle, 2200×1200, verified URLs).
- 1 Remotion video: ~8s 1920×1080 30fps seamless-loop luxury motion piece
  (champagne gradient, drifting gold bokeh particles, subtle serif wordmark
  shimmer), H.264 mp4 ≤ ~4MB, plus a poster jpg. Built from a scratch
  Remotion project (not committed to theme); mp4+poster land in assets/.

## Non-Goals

- No discount/bundle pricing logic (Shopify Functions/app territory — upsell
  is presentation + one-click add). Listing copy must stay accurate.
- No review-app integration (testimonials are section settings; ratings stay
  metafield-based).

## Verification

Same as Meowhaus T4 sweep + theme check 0 errors + zip layout check; video
plays muted-loop in hero via local harness render check.
