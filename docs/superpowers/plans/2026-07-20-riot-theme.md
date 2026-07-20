# Riot Shopify Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:subagent-driven-development task-by-task. Checkbox steps.

**Goal:** Fork Patina (themes/patina @ HEAD) into `themes/riot/`, re-skin to the ARCHIVE UNKNOWN street/protest mockup (`972be0ba-3d52-4162-9fd9-03c50896a5e5.jpg`), bundle Permanent Marker font + concrete/tape textures + 5 street hero photos + a glitch Remotion loop, ship `riot-theme-1.0.0.zip` + bonus `riot-canva-banner-templates.zip`.

**Architecture:** identical to Patina; changes are CSS/Liquid skin + bundled assets + one bonus-zip deliverable. All commerce boosters AND Patina's product-image fallbacks inherited untouched.

## Global Constraints

- Source `C:\Users\DJMOON\bebriz-themes\themes\riot\`, standalone nested git (fork commit from Patina HEAD, then per-task commits; user m9339191 / 12160564+m9339191@users.noreply.github.com). Parent .gitignore: add `themes/riot/*`, `!themes/riot/index.html`, `riot-theme-*.zip`, `riot-canva-*.zip`, `riot-demo-products.csv`, `riot-theme/`.
- Verify per task: `shopify theme check --path "C:/Users/DJMOON/bebriz-themes/themes/riot"` → 0 errors; `node --check assets/theme.js` when touched.
- Tokens: bg `#C9C7C2`, text `#171715`, accent_1 `#878785`, accent_2 `#696967`, accent_3 `#BBFB35`, light `#E4E2DC`, dark `#171715`.
- Fonts: KEEP Special Elite woff2; REPLACE Caveat with Permanent Marker (Apache-2.0) woff2 → `.hand` = marker. Setting stays `use_craft_fonts`.
- Landmines banned (form-arg filters, bracket-index filters, inline alt|default, non-fieldset option selectors, utility classes demoting flex — keep compound display:flex restores). NEVER touch other themes. NEVER full-push to stores.

### Task 1: Fork, tokens, fonts, street utilities
Fork copy (exclude .git/.superpowers/.gstack/index.html) + git init/fork commit; settings_schema theme_info Riot/1.0.0 + color defaults + settings_data sync; download Permanent Marker woff2 (verify loads in browse harness), drop Caveat files/refs; PIL textures: concrete grain tile (replaces texture-cardboard.png usage) + scrap-fabric tape tile; CSS utilities: retune `.tape` (gray fabric, frayed mask), add `.frame-hard` (black photo frame) + `.sticker-neon` (glitch chip) + bracket-button style + neon ATC block style; doodle icons in icon.liquid (circled-A, scribble star, marker arrow); brand strings Patina→Riot; delete hero-craft/hero-patina media refs (replaced T3; hero preset guard — check index.json doesn't pin missing assets). Grep `patina` → 0 user-facing hits. Theme check + commit.

### Task 2: Section reskins + index.json
hero-banner (torn-label eyebrow chip, typewriter headline, bracket CTA, NEW optional marker note card top-right `note_text`), origin-story (marker headline, manifesto copy), product-spotlight (typewriter callouts + 360° doodle badge accent), lookbook (black hard frames + neon `#SHOP THE LOOK` sticker replaces tag badge on product tiles), social-proof (black frames + marker captions), bestsellers "High-Volume D2C Grid" (black-frame cards, neon sticker prices), direct-purchase (neon ADD TO CART / SYSTEM CHECK block), trust-badges, cart drawer (label-cream panel on concrete). index.json demo copy in ARCHIVE UNKNOWN voice (English, brandable). Flex-restore compound rules re-checked for every reused utility. Theme check + commit.

### Task 3: Bundled media + Canva bonus zip
5 hero photos (Pexels verified: streetwear/techwear/urban graffiti, 2200×1200) → assets/hero-street-1..5.jpg + preset labels; Remotion loop in scratch project (concrete bg + drifting white marker doodles + neon glitch scanline flickers, 8s seamless 1920×1080 ≤4MB, NO text) → assets/hero-riot.mp4 + poster; hero-banner asset refs renamed; harness verify (fonts render, video non-black). Canva bonus: 5 banner designs 2200×1200 (PIL compositing hero photos + tape/label/neon motifs) each as sample PNG + text-free background PNG + CANVA-GUIDE.txt → `riot-canva-banner-templates.zip` at repo root (gitignored). Theme check + commit.

### Task 4: Final validation + packaging
Patina-T4 sweep (+ banned `patina` grep; fonts/textures/media present + referenced; flex-restore rules present) + `riot-theme-1.0.0.zip` (7 std dirs only, report size) + verify canva zip contents + commit.

### Post-store (when user provides demo store): product CSV (streetwear demo products), scoped deploy, product connections via pull-edit-push, THEN the per-section overlay fidelity loop vs mockup until 100% — treat as design rounds, not optional QA.

## Verification checklist (every task)
theme check 0 errors; commit nested repo.
