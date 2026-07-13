# Meowhaus Shopify Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fork Volt (themes/volt @ 9c8f8c0) into `themes/meowhaus/`, re-skin to the MEOWHAUS mockup (warm cream/sage/oak, serif, rounded), replace/add home sections, strip coffee-specific features, ship `meowhaus-theme-1.0.0.zip` with `shopify theme check` clean.

**Architecture:** Same as Volt (JSON templates + sections + one base.css + one theme.js). All JS behavior inherited; changes are Liquid/CSS/schema/branding plus three new-or-replaced home sections.

**Tech Stack:** Liquid, vanilla JS/CSS, Shopify CLI theme check, Python (integrity sweep + zip).

## Global Constraints

- Source at `C:\Users\DJMOON\bebriz-themes\themes\meowhaus\`, standalone nested git repo (git init at fork; commit per task). Parent repo `.gitignore` gains `themes/meowhaus/*` + `!themes/meowhaus/index.html` (same pattern as volt). NEVER commit theme source to the parent repo.
- Verify every task: `shopify theme check --path "C:/Users/DJMOON/bebriz-themes/themes/meowhaus"` → 0 errors (the 2 form-after-capture info warnings in main-login.liquid are pre-existing and acceptable); `node --check assets/theme.js` when JS touched.
- Design tokens (settings defaults): bg `#F6F1E6`, text `#2F2A23`, accent_1 sage `#A9BFA0`, accent_2 oak `#C6976B`, accent_3 clay `#B77E5C`, light `#FFFDF7`, dark text `#2F2A23`.
- Shape: `--radius: 14px`; `.button` = pill (border-radius 999px), 1px borders replace 3px; headings serif via font_picker (default a Playfair-class handle, e.g. `playfair_display_n4` — verify handle passes theme check, fallback `lora_n4`), sentence case (remove global uppercase on h1–h6; keep uppercase only for small labels/eyebrows/buttons via utility class).
- Known Liquid landmines (already fixed in Volt — do NOT reintroduce): no filters inside `{% form %}` tag arguments; no filters inside bracket indices `arr[i | minus: 1]`; `alt: x | default: y` never inline inside image_tag args (hoist to assign).
- Snippet contracts inherited from Volt stay identical EXCEPT: `roast-level` snippet is deleted and every render call removed.
- Icon snippet gains: paw, leaf, star, star-outline, tag (keep all existing names too; brand mark = paw).

---

### Task 1: Fork, tokens, typography, shape reskin

**Files:** copy themes/volt → themes/meowhaus (exclude .git, .superpowers); fresh `git init`; edit config/settings_schema.json (theme_info Meowhaus/bebriz/1.0.0, color defaults, serif heading font default, enable_left_rail default false), config/settings_data.json (match), assets/base.css (–radius 14px, pill buttons, 1px borders, serif heading rules, drop global h1–h6 uppercase → add `.text-upper` utility used by labels/buttons, palette-sensitive rules audit: anything assuming dark bg must read tokens not hardcode), layout/theme.liquid (brand strings), snippets/icon.liquid (+paw, leaf, star, star-outline, tag; brand mark paw), locales (Volt→Meowhaus strings), parent .gitignore.
**Steps:** fork → token/typography/shape edits → grep sweep `volt|bolt|electric` in liquid/json (allow icon name 'bolt' to remain as a generic icon) → theme check 0 errors → commit.

### Task 2: Strip coffee features; global reskin of components

**Files:** delete snippets/roast-level.liquid; edit snippets/product-card.liquid (remove roast render; default card = light rounded card `.product-card--plain`-style on cream; color-block variant now uses soft palette), sections/main-product.liquid (remove roast_level block type + render; default product.json blocks updated), sections/featured-grid.liquid (soft palette, stays out of default homepage), sections/bestsellers.liquid (light rounded "fan favorites" card look, optional star rating from `product.metafields.reviews.rating.value` — render only when present, star/star-outline icons, one decimal), cart drawer + header + footer + announcement recolor (cream header, logo_position setting left|center default left, "Join the Club" newsletter heading default, paw brand mark), templates/product.json.
**Steps:** edits → grep `roast` = 0 hits → theme check → commit.

### Task 3: New home sections + index.json

**Files:** create sections/hero-banner.liquid (image_picker bg, eyebrow, 2-line serif heading, pill CTA label+link, height range 360–720 default 560, overlay opacity range, placeholder-safe), sections/explore-categories.liquid (heading default "Explore Categories"; up to 8 blocks: collection picker + optional image override + label; circular medallion cards 4/2 cols; placeholder circles), sections/lookbook.liquid (heading default "The Lookbook: Inspiring Homes"; up to 8 image blocks + optional product link; staggered grid 4/2 cols, rounded tiles, tag-icon badge on linked tiles, whole-tile link); rewrite templates/index.json (hero-banner, explore-categories, lookbook, bestsellers preset titled "Fan Favorites", newsletter "Join the Club"); subtle paw/leaf motif utility (low-opacity inline SVG backgrounds via CSS class used by explore/lookbook sections).
**Steps:** build 3 sections w/ schemas+presets → index.json → theme check → commit.

### Task 4: Final validation + packaging

**Steps:** full theme check review; Python integrity sweep (all JSON parses; every render/section/locale/icon ref resolves; settings_data ids ⊆ schema ids; grep bans: `roast`, `Volt`, filters-in-brackets pattern, form-arg pipes, image_tag alt|default inline); responsive breakpoint audit unchanged from Volt (spot check); build `C:\Users\DJMOON\bebriz-themes\meowhaus-theme-1.0.0.zip` (7 folders at zip root; parent .gitignore covers `meowhaus-theme-*.zip`); commit; report.

## Verification checklist (every task)

```
shopify theme check --path "C:/Users/DJMOON/bebriz-themes/themes/meowhaus"
```
0 errors (+2 known info warnings). Commit in nested repo per task.
