# Patina Shopify Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:subagent-driven-development task-by-task. Checkbox steps.

**Goal:** Fork Aurora (themes/aurora @ HEAD) into `themes/patina/`, re-skin to the distressed-paper scrapbook mockup, add the polaroid social-proof section, bundle craft fonts + 5 hero photos + a doodle Remotion loop, ship `patina-theme-1.0.0.zip`.

**Architecture:** identical to Aurora; changes are CSS/Liquid skin + one new section + bundled assets. All commerce boosters inherited untouched.

## Global Constraints

- Source `C:\Users\DJMOON\bebriz-themes\themes\patina\`, standalone nested git (fork commit from Aurora HEAD, then per-task commits; user m9339191 / 12160564+m9339191@users.noreply.github.com). Parent .gitignore: `themes/patina/*`, `!themes/patina/index.html`, `patina-theme-*.zip`.
- Verify per task: `shopify theme check --path "C:/Users/DJMOON/bebriz-themes/themes/patina"` → 0 errors (2 known main-login infos OK); `node --check assets/theme.js` when touched.
- Tokens: bg `#F0E8D8`, text `#2B2925`, accent_1 `#C9B08D`, accent_2 `#A98F68`, accent_3 `#4E9A8E`, light `#F7F2E7`, dark `#2B2925`.
- Fonts: bundle woff2 in assets — Special Elite (Apache-2.0) + Caveat (OFL); @font-face in base.css; setting `use_craft_fonts` checkbox default true → headings use `'Special Elite', var(--font-heading-family)` stack via a `--font-craft` variable pattern; `.hand` class = Caveat. License files NOT required in zip but note licenses in a CSS comment.
- Landmines banned (form-arg filters, bracket-index filters, inline alt|default, non-fieldset option selectors). NEVER touch other themes. NEVER full-push to stores.

### Task 1: Fork, tokens, fonts, craft utilities
Fork copy (exclude .git/.superpowers) + git init/fork commit; settings_schema theme_info Patina/1.0.0 + color defaults + `use_craft_fonts` checkbox + settings_data sync; download Special Elite + Caveat woff2 (google/fonts github raw or gstatic; verify files load in a browse harness) into assets; @font-face + heading/craft stacks; craft utility CSS: `.torn`/`.torn--top`/`.torn--bottom` (SVG mask data-URI), `.paper` grain bg, `.tape` (+ variants), `.polaroid` + `.tilt-1/2/3`, doodle SVG icons added to icon.liquid (doodle-star, doodle-moon, doodle-arrow — hand-drawn stroke style); button "stamped label" restyle; brand strings Aurora→Patina; delete hero-jewels + hero-aurora media (replaced in T3); hero preset default 'none' temporarily (Aurora T1 lesson: check index.json doesn't pin it). Grep `aurora` → 0 user-facing hits. Theme check + commit.

### Task 2: Section reskins + social-proof + index.json
Reskin w/ craft utilities: hero-banner (Caveat eyebrow + doodle star/arrow accents, torn-label CTA), product-spotlight (torn paper card + typewriter callouts), origin-story (torn photos + tape + handwritten label), lookbook (polaroid + tape + tilts, Caveat captions), bestsellers → "High-volume D2C grid" look (torn paper product cards, prices prominent), direct-purchase testimonials → polaroid style, trust-badges (stamped icons), countdown (stamped digits look), cart drawer (paper panel). NEW sections/social-proof.liquid (≤6 polaroid quote blocks: image/quote(.hand)/author, tilt cycle, preset 3). index.json rewrite: hero-banner, trust-badges, product-spotlight, origin-story, lookbook, social-proof, direct-purchase, bestsellers("High-volume favorites"). Copy defaults keep AURORA FINE voice per mockup but neutral-brandable. Theme check + commit.

### Task 3: Bundled media
5 hero photos (Pexels: boho/turquoise/silver jewelry, landscape 2200×1200, verified) → assets/hero-craft-1..5.jpg + preset labels + default "1"; Remotion loop variant in scratch project (kraft paper tone bg w/ grain, ~12 drifting hand-drawn white-ink doodle stars/moons at low opacity, subtle vignette; 8s seamless 1920×1080 ≤4MB) → assets/hero-patina.mp4 + poster jpg; hero-banner video branch asset refs renamed accordingly; harness verify (fonts render, video non-black). Theme check + commit.

### Task 4: Final validation + packaging
Aurora-T5 sweep (+ banned `aurora` grep; font files present + referenced; media present) + `patina-theme-1.0.0.zip` (includes woff2+mp4; report size) + commit.

## Verification checklist (every task)
theme check 0 errors; commit nested repo.
