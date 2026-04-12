#!/usr/bin/env python3
"""
beBriz Theme Sales Page Generator
===================================
Reads theme definitions from themes_config/themes.yaml and optional markdown
descriptions from themes_config/descriptions/{handle}.md, then generates:
  - themes/{handle}/index.html  (individual theme sales pages)
  - Updates index.html homepage catalog grid section

Dependencies: PyYAML (pip install pyyaml)
              Falls back to a simple YAML parser if PyYAML is not installed.
"""

import os
import re
import sys
import html as html_module

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(SCRIPT_DIR, "themes_config")
THEMES_YAML = os.path.join(CONFIG_DIR, "themes.yaml")
DESCRIPTIONS_DIR = os.path.join(CONFIG_DIR, "descriptions")
THEMES_DIR = os.path.join(SCRIPT_DIR, "themes")
INDEX_PATH = os.path.join(SCRIPT_DIR, "index.html")

# ---------------------------------------------------------------------------
# Simple YAML parser (fallback when PyYAML is not installed)
# ---------------------------------------------------------------------------

def _simple_yaml_parse(text):
    """Minimal YAML parser that handles the themes.yaml structure.

    Supports:
      - Top-level 'themes:' list
      - Scalar fields at indent 4
      - Simple string lists at indent 6 (e.g. badges)
      - List of dicts at indent 6-8 (e.g. features, screenshots, whats_included, faq)
    """
    themes = []
    current_theme = None
    current_list_key = None
    current_dict_item = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        # Top-level key
        if indent == 0 and stripped == "themes:":
            continue

        # New theme item
        if indent == 2 and stripped.startswith("- handle:"):
            current_theme = {"handle": stripped.split(":", 1)[1].strip().strip('"')}
            themes.append(current_theme)
            current_list_key = None
            current_dict_item = None
            continue

        if current_theme is None:
            continue

        # Scalar fields at theme level
        if indent == 4 and ":" in stripped and not stripped.startswith("- "):
            key, val = stripped.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"')
            if val:
                current_theme[key] = val
                current_list_key = None
                current_dict_item = None
            else:
                current_list_key = key
                if current_list_key not in current_theme:
                    current_theme[current_list_key] = []
                current_dict_item = None
            continue

        # List items at indent 6
        if indent == 6 and stripped.startswith("- "):
            content = stripped[2:].strip()
            if current_list_key is None:
                continue

            # Check if it's a dict item (has key: value)
            if ":" in content:
                key, val = content.split(":", 1)
                key = key.strip()
                val = val.strip().strip('"')
                current_dict_item = {key: val}
                current_theme[current_list_key].append(current_dict_item)
            else:
                # Simple string list item
                current_theme[current_list_key].append(content.strip('"'))
                current_dict_item = None
            continue

        # Dict continuation at indent 8
        if indent == 8 and ":" in stripped and not stripped.startswith("- "):
            if current_dict_item is not None:
                key, val = stripped.split(":", 1)
                key = key.strip()
                val = val.strip().strip('"')
                current_dict_item[key] = val
            continue

    return {"themes": themes}


def load_yaml(path):
    """Load YAML file, trying PyYAML first, falling back to simple parser."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    try:
        import yaml
        return yaml.safe_load(text)
    except ImportError:
        return _simple_yaml_parse(text)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def esc(text):
    """HTML-escape a string."""
    return html_module.escape(str(text))


def make_icon_letters(name):
    """Generate 2-letter icon abbreviation from a feature name."""
    words = name.split()
    if len(words) >= 2:
        return (words[0][0] + words[1][0]).upper()
    return name[:2].upper()


def load_description_md(handle):
    """Load optional markdown description for a theme."""
    md_path = os.path.join(DESCRIPTIONS_DIR, f"{handle}.md")
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            return f.read()
    return None


CATEGORY_LABELS = {
    "fashion": "Fashion",
    "furniture": "Furniture",
    "electronics": "Electronics",
    "food": "Food & Drink",
    "pet": "Pet & Wellness",
    "supplements": "Supplements & Health",
    "coffee": "Coffee & Food",
    "digital": "Digital Products",
    "kids": "Kids & Baby",
    "jewelry": "Jewelry & Luxury",
}


# ---------------------------------------------------------------------------
# Coming-soon placeholder themes for homepage catalog
# ---------------------------------------------------------------------------

COMING_SOON_THEMES = [
    {
        "handle": None,
        "name": "Luxe Interior",
        "category": "furniture",
        "description": "Modern furniture & home decor theme with room visualizer, material swatches, and curated collection layouts.",
    },
    {
        "handle": None,
        "name": "Luxe Tech",
        "category": "electronics",
        "description": "High-performance electronics & gadgets theme with spec comparison tables, video galleries, and tech-focused layouts.",
    },
    {
        "handle": None,
        "name": "Luxe Gourmet",
        "category": "food",
        "description": "Artisan food & beverage theme with subscription support, recipe pages, and farm-to-table storytelling sections.",
    },
]


# ---------------------------------------------------------------------------
# Theme Sales Page Generator
# ---------------------------------------------------------------------------

def generate_theme_page(theme):
    """Generate the full HTML for a theme sales page."""
    handle = theme["handle"]
    name = theme.get("name", handle)
    tagline = theme.get("tagline", "")
    description = theme.get("description", "")
    price = theme.get("price", "$59")
    price_note = theme.get("price_note", "One-time payment")
    category = theme.get("category", "")
    demo_url = theme.get("demo_url", "#")
    demo_password = theme.get("demo_password", "")
    badges = theme.get("badges", [])
    features = theme.get("features", [])
    screenshots = theme.get("screenshots", [])
    whats_included = theme.get("whats_included", [])
    faq = theme.get("faq", [])

    root = "../../"

    # Split name for accent styling (last word gets accent)
    name_parts = name.rsplit(" ", 1)
    if len(name_parts) == 2:
        name_html = f'{esc(name_parts[0])} <span class="accent">{esc(name_parts[1])}</span>'
    else:
        name_html = esc(name)

    # --- Badges ---
    badges_html = ""
    for i, badge in enumerate(badges):
        if i == 0:
            badges_html += f'          <span class="badge-item"><span class="badge-dot"></span> {esc(badge)}</span>\n'
        else:
            badges_html += f'          <span class="badge-item">{esc(badge)}</span>\n'

    # --- Screenshots ---
    screenshots_html = ""
    if screenshots:
        screenshots_html = '  <!-- Large Preview Section -->\n'
        screenshots_html += '  <section class="preview-section">\n'
        screenshots_html += '    <div class="container">\n'
        screenshots_html += '      <div class="preview-grid preview-screenshots">\n'
        for ss in screenshots:
            file = ss.get("file", "")
            label = ss.get("label", "")
            screenshots_html += f'        <div class="preview-card">\n'
            screenshots_html += f'          <img src="{root}images/{esc(file)}" alt="{esc(label)} Preview">\n'
            screenshots_html += f'          <div class="preview-label">{esc(label)}</div>\n'
            screenshots_html += f'        </div>\n'
        screenshots_html += '      </div>\n'
        screenshots_html += '    </div>\n'
        screenshots_html += '  </section>\n'

    # --- Features ---
    features_html = ""
    if features:
        features_html += '  <!-- Features Grid -->\n'
        features_html += '  <section class="section feature-grid-section">\n'
        features_html += '    <div class="container">\n'
        features_html += '      <span class="section-label">Features</span>\n'
        features_html += '      <h2 class="section-title">Packed with Features</h2>\n'
        features_html += '      <p class="section-subtitle">Everything you need to run a successful store, built right into the theme. No apps required.</p>\n'
        features_html += '\n'
        features_html += '      <div class="feature-items-grid">\n'
        for feat in features:
            fname = feat.get("name", "")
            fdesc = feat.get("desc", "")
            icon = make_icon_letters(fname)
            features_html += f'        <div class="feature-item">\n'
            features_html += f'          <div class="feature-icon-circle">{esc(icon)}</div>\n'
            features_html += f'          <div class="feature-item-text">\n'
            features_html += f'            <h4>{esc(fname)}</h4>\n'
            features_html += f'            <p>{esc(fdesc)}</p>\n'
            features_html += f'          </div>\n'
            features_html += f'        </div>\n'
        features_html += '      </div>\n'
        features_html += '    </div>\n'
        features_html += '  </section>\n'

    # --- What's Included ---
    included_html = ""
    if whats_included:
        # Icon letters for included items
        inc_icons = ["Z", "D", "S", "U", "P", "T", "G", "B"]
        included_html += '  <!-- What\'s Included -->\n'
        included_html += '  <section class="section">\n'
        included_html += '    <div class="container">\n'
        included_html += '      <span class="section-label">What You Get</span>\n'
        included_html += '      <h2 class="section-title">What\'s Included</h2>\n'
        included_html += '      <p class="section-subtitle">Everything you need to get your store running and growing from day one.</p>\n'
        included_html += '\n'
        included_html += '      <div class="included-grid">\n'
        for idx, item in enumerate(whats_included):
            title = item.get("title", "")
            desc = item.get("desc", "")
            icon = inc_icons[idx] if idx < len(inc_icons) else title[0].upper()
            included_html += f'        <div class="included-card">\n'
            included_html += f'          <div class="inc-icon">{esc(icon)}</div>\n'
            included_html += f'          <h4>{esc(title)}</h4>\n'
            included_html += f'          <p>{esc(desc)}</p>\n'
            included_html += f'        </div>\n'
        included_html += '      </div>\n'
        included_html += '    </div>\n'
        included_html += '  </section>\n'

    # --- FAQ ---
    faq_html = ""
    if faq:
        faq_html += '  <!-- FAQ -->\n'
        faq_html += '  <section class="section bg-elevated">\n'
        faq_html += '    <div class="container">\n'
        faq_html += '      <span class="section-label">FAQ</span>\n'
        faq_html += '      <h2 class="section-title">Frequently Asked Questions</h2>\n'
        faq_html += f'      <p class="section-subtitle">Common questions about the {esc(name)} theme.</p>\n'
        faq_html += '\n'
        faq_html += '      <div class="accordion">\n'
        for item in faq:
            q = item.get("q", "")
            a = item.get("a", "")
            faq_html += f'        <div class="accordion-item">\n'
            faq_html += f'          <button class="accordion-trigger">\n'
            faq_html += f'            {esc(q)}\n'
            faq_html += f'            <span class="accordion-icon">+</span>\n'
            faq_html += f'          </button>\n'
            faq_html += f'          <div class="accordion-content">\n'
            faq_html += f'            <div class="accordion-content-inner">\n'
            faq_html += f'              {esc(a)}\n'
            faq_html += f'            </div>\n'
            faq_html += f'          </div>\n'
            faq_html += f'        </div>\n'
        faq_html += '      </div>\n'
        faq_html += '    </div>\n'
        faq_html += '  </section>\n'

    # --- Footer theme links ---
    footer_theme_links = f'          <a href="index.html">{esc(name)}</a>\n'

    # --- Assemble full page ---
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(name)} &mdash; Premium Shopify Theme | beBriz</title>
  <meta name="description" content="{esc(tagline)}. {esc(description)} {esc(price)} one-time payment.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}css/style.css">
</head>
<body>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="{root}index.html" class="logo"><span>be</span>Briz</a>
      <nav class="nav-links">
        <a href="{root}index.html">Home</a>
        <a href="index.html" class="active">Themes</a>
        <a href="{root}docs/index.html">Documentation</a>
        <a href="{root}support/index.html">Support</a>
      </nav>
      <button class="mobile-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Theme Hero -->
  <section class="theme-hero">
    <div class="container">
      <div class="theme-hero-content">
        <h1>{name_html}</h1>
        <div class="price-tag">{esc(price)}</div>
        <p class="price-note">{esc(price_note)} &middot; Lifetime updates included</p>
        <div class="btn-group">
          <a href="#" class="btn btn-primary btn-lg">Buy Now</a>
          <a href="{f'{root}demo-redirect.html?store={esc(demo_url)}&pw={esc(demo_password)}' if demo_password else esc(demo_url)}" target="_blank" rel="noopener" class="btn btn-outline btn-lg">Live Preview</a>
        </div>
        <div class="badge-row">
{badges_html}        </div>
      </div>
    </div>
  </section>

{screenshots_html}
{features_html}
{included_html}
{faq_html}
  <!-- Bottom CTA -->
  <section class="bottom-cta">
    <div class="container">
      <h2 class="section-title" style="margin-bottom: 24px;">Start Building Your Dream Store</h2>
      <p class="section-subtitle" style="margin-bottom: 40px;">One-time payment. Lifetime updates. No recurring fees.</p>
      <a href="#" class="btn btn-primary btn-lg">{esc(price)} &mdash; Get {esc(name)}</a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="{root}index.html" class="logo"><span>be</span>Briz</a>
          <p>Premium Shopify themes for modern e-commerce. Designed and developed with an obsession for quality, performance, and detail.</p>
          <div class="footer-tagline">Powered by beBriz</div>
        </div>
        <div class="footer-col">
          <h4>Themes</h4>
{footer_theme_links}        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <a href="{root}docs/index.html">Documentation</a>
          <a href="{root}support/index.html">Support</a>
          <a href="{root}support/index.html#faq">FAQ</a>
        </div>
        <div class="footer-col">
          <h4>Connect</h4>
          <div class="footer-social">
            <a href="#" aria-label="Twitter">X</a>
            <a href="#" aria-label="GitHub">GH</a>
            <a href="#" aria-label="Dribbble">Dr</a>
          </div>
          <a href="{root}support/index.html#contact" style="margin-top: 12px;">Contact Us</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 beBriz. All rights reserved.</span>
        <div class="footer-bottom-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="{root}js/main.js"></script>
</body>
</html>
'''
    return page


# ---------------------------------------------------------------------------
# Homepage Catalog Grid Generator
# ---------------------------------------------------------------------------

def generate_catalog_grid(themes):
    """Generate the catalog grid HTML for the homepage."""
    lines = []
    lines.append('      <!-- Theme Grid -->')
    lines.append('      <div class="catalog-grid">')

    # Active themes from YAML
    for theme in themes:
        handle = theme["handle"]
        name = theme.get("name", handle)
        category = theme.get("category", "")
        price = theme.get("price", "")
        description = theme.get("description", "")
        screenshots = theme.get("screenshots", [])
        badges = theme.get("badges", [])
        category_label = CATEGORY_LABELS.get(category, category.title())

        # Determine tags
        tags_html = f'              <span class="catalog-tag">{esc(category_label)}</span>\n'
        if "Shopify 2.0" in badges:
            tags_html += '              <span class="catalog-tag">Shopify 2.0</span>\n'

        # Build card image or coming-soon placeholder
        if screenshots:
            first_img = screenshots[0].get("file", "")
            card_image = f'          <div class="catalog-card-image">\n'
            card_image += f'            <img src="images/{esc(first_img)}" alt="{esc(name)} Theme">\n'
            card_image += f'          </div>'
        else:
            card_image = f'          <div class="catalog-card-image catalog-card-image--placeholder">\n'
            card_image += f'            <span>Coming Soon</span>\n'
            card_image += f'          </div>'

        # Truncate description for card
        short_desc = description
        if len(short_desc) > 140:
            short_desc = short_desc[:137] + "..."

        lines.append(f'        <!-- {esc(name)} -->')
        lines.append(f'        <a href="themes/{esc(handle)}/index.html" class="catalog-card glass-card" data-category="{esc(category)}">')
        lines.append(card_image)
        lines.append(f'          <div class="catalog-card-body">')
        lines.append(f'            <div class="catalog-card-tags">')
        lines.append(tags_html.rstrip())
        lines.append(f'            </div>')
        lines.append(f'            <h3>{esc(name)}</h3>')
        lines.append(f'            <p>{esc(short_desc)}</p>')
        lines.append(f'            <div class="catalog-card-footer">')
        lines.append(f'              <span class="catalog-price">{esc(price)}</span>')
        lines.append(f'              <span class="catalog-link">View Theme &rarr;</span>')
        lines.append(f'            </div>')
        lines.append(f'          </div>')
        lines.append(f'        </a>')

    # Coming-soon cards (only for categories not yet covered by real themes)
    active_categories = {t.get("category", "") for t in themes}
    for cs in COMING_SOON_THEMES:
        if cs["category"] in active_categories:
            continue
        category = cs["category"]
        category_label = CATEGORY_LABELS.get(category, category.title())
        lines.append(f'')
        lines.append(f'        <!-- Coming Soon: {esc(cs["name"])} -->')
        lines.append(f'        <div class="catalog-card glass-card catalog-card--coming-soon" data-category="{esc(category)}">')
        lines.append(f'          <div class="catalog-card-image catalog-card-image--placeholder">')
        lines.append(f'            <span>Coming Soon</span>')
        lines.append(f'          </div>')
        lines.append(f'          <div class="catalog-card-body">')
        lines.append(f'            <div class="catalog-card-tags">')
        lines.append(f'              <span class="catalog-tag">{esc(category_label)}</span>')
        lines.append(f'              <span class="catalog-tag">Shopify 2.0</span>')
        lines.append(f'            </div>')
        lines.append(f'            <h3>{esc(cs["name"])}</h3>')
        lines.append(f'            <p>{esc(cs["description"])}</p>')
        lines.append(f'            <div class="catalog-card-footer">')
        lines.append(f'              <span class="catalog-price">Coming Soon</span>')
        lines.append(f'            </div>')
        lines.append(f'          </div>')
        lines.append(f'        </div>')

    lines.append('      </div>')
    return "\n".join(lines)


def update_homepage(themes):
    """Update the homepage catalog grid between marker comments."""
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the catalog grid section and replace it
    # Pattern: from "<!-- Theme Grid -->" to the closing "</div>" of catalog-grid,
    # which is right before the closing "</div>" of the container and "</section>"
    grid_start = "      <!-- Theme Grid -->"
    grid_end = "    </div>\n  </section>"

    start_idx = content.find(grid_start)
    # Find the closing of the catalog-grid div first, then locate the container/section close
    end_idx = content.find(grid_end, start_idx)

    if start_idx == -1 or end_idx == -1:
        print("  WARNING: Could not find catalog grid markers in index.html")
        print("  Attempting alternative approach...")

        # Alternative: find between catalog-filters and the section closing
        alt_start = content.find('<div class="catalog-grid')
        if alt_start == -1:
            print("  ERROR: Cannot locate catalog grid in index.html. Skipping homepage update.")
            return False

        # Find the line start
        line_start = content.rfind("\n", 0, alt_start) + 1

        # Find the closing </div> for catalog-grid - it's followed by container and section close
        # Count div nesting
        search_from = alt_start
        depth = 0
        pos = search_from
        grid_close_pos = -1
        while pos < len(content):
            open_match = content.find("<div", pos)
            close_match = content.find("</div>", pos)

            if close_match == -1:
                break

            if open_match != -1 and open_match < close_match:
                depth += 1
                pos = open_match + 4
            else:
                depth -= 1
                if depth == 0:
                    grid_close_pos = close_match + len("</div>")
                    break
                pos = close_match + 6

        if grid_close_pos == -1:
            print("  ERROR: Cannot find end of catalog grid. Skipping homepage update.")
            return False

        new_grid = generate_catalog_grid(themes)
        content = content[:line_start] + new_grid + "\n" + content[grid_close_pos:]
    else:
        new_grid = generate_catalog_grid(themes)
        content = content[:start_idx] + new_grid + "\n" + content[end_idx:]

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    return True


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def generate_themes_listing(themes):
    """Generate the themes/index.html listing page with all themes."""
    all_categories = set()
    for t in themes:
        all_categories.add(t.get("category", "other"))
    for cs in COMING_SOON_THEMES:
        all_categories.add(cs.get("category", "other"))

    # Build filter buttons
    filters_html = '        <button class="catalog-filter is-active" data-filter="all">All</button>\n'
    for cat in ["fashion", "furniture", "electronics", "food", "pet", "supplements", "coffee", "digital", "kids", "jewelry"]:
        label = CATEGORY_LABELS.get(cat, cat.title())
        filters_html += f'        <button class="catalog-filter" data-filter="{cat}">{esc(label)}</button>\n'

    # Build theme cards
    cards_html = ""
    for t in themes:
        handle = t["handle"]
        name = esc(t.get("name", handle))
        desc = esc(t.get("description", ""))
        if len(desc) > 120:
            desc = desc[:117] + "..."
        price = esc(t.get("price", "$59"))
        category = t.get("category", "other")
        cat_label = CATEGORY_LABELS.get(category, category.title())
        screenshots = t.get("screenshots", [])
        img_html = ""
        if screenshots:
            img_html = f'<img src="../images/{screenshots[0].get("file", "")}" alt="{name} Theme">'
        else:
            img_html = f'<img src="../images/theme-card-{handle}.svg" alt="{name} Theme">'

        cards_html += f'''
        <a href="{handle}/index.html" class="catalog-card glass-card" data-category="{category}">
          <div class="catalog-card-image">
            {img_html}
          </div>
          <div class="catalog-card-body">
            <div class="catalog-card-tags">
              <span class="catalog-tag">{esc(cat_label)}</span>
              <span class="catalog-tag">Shopify 2.0</span>
            </div>
            <h3>{name}</h3>
            <p>{desc}</p>
            <div class="catalog-card-footer">
              <span class="catalog-price">{price}</span>
              <span class="catalog-link">View Theme &rarr;</span>
            </div>
          </div>
        </a>
'''

    # Coming soon cards
    for cs in COMING_SOON_THEMES:
        cs_name = esc(cs.get("name", ""))
        cs_desc = esc(cs.get("description", ""))
        cs_cat = cs.get("category", "other")
        cs_cat_label = CATEGORY_LABELS.get(cs_cat, cs_cat.title())
        cards_html += f'''
        <div class="catalog-card glass-card catalog-card--coming-soon" data-category="{cs_cat}">
          <div class="catalog-card-image catalog-card-image--placeholder">
            <span>Coming Soon</span>
          </div>
          <div class="catalog-card-body">
            <div class="catalog-card-tags">
              <span class="catalog-tag">{esc(cs_cat_label)}</span>
              <span class="catalog-tag">Shopify 2.0</span>
            </div>
            <h3>{cs_name}</h3>
            <p>{cs_desc}</p>
            <div class="catalog-card-footer">
              <span class="catalog-price">Coming Soon</span>
            </div>
          </div>
        </div>
'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Themes — beBriz</title>
  <meta name="description" content="Browse all premium Shopify themes by beBriz. Pixel-perfect, blazing fast, OS 2.0 ready.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="logo"><span>be</span>Briz</a>
      <nav class="nav-links">
        <a href="../index.html">Home</a>
        <a href="index.html" class="active">Themes</a>
        <a href="../docs/index.html">Documentation</a>
        <a href="../support/index.html">Support</a>
      </nav>
      <button class="mobile-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <section class="section" style="padding-top: 140px;">
    <div class="container">
      <span class="section-label">Our Collection</span>
      <h1 class="section-title" style="font-size: clamp(2rem, 4vw, 3rem);">Premium Shopify Themes</h1>
      <p class="section-subtitle">Pixel-perfect, blazing fast themes built for modern e-commerce. Find the perfect foundation for your store.</p>

      <div class="catalog-filters">
{filters_html}      </div>

      <div class="catalog-grid">
{cards_html}      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner">
        <h2>Can&#39;t find what you need?</h2>
        <p>We&#39;re constantly building new themes. Subscribe to get notified when we launch new products.</p>
        <a href="../support/index.html" class="btn btn-lg">Contact Us</a>
      </div>
    </div>
  </section>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="../index.html" class="logo"><span>be</span>Briz</a>
          <p>Premium Shopify themes for modern e-commerce. Designed and developed with an obsession for quality, performance, and detail.</p>
          <div class="footer-tagline">Powered by beBriz</div>
        </div>
        <div class="footer-col">
          <h4>Themes</h4>
          <a href="index.html">All Themes</a>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <a href="../docs/index.html">Documentation</a>
          <a href="../support/index.html">Support</a>
        </div>
        <div class="footer-col">
          <h4>Connect</h4>
          <div class="footer-social">
            <a href="#" aria-label="Twitter">X</a>
            <a href="#" aria-label="GitHub">GH</a>
          </div>
          <a href="../support/index.html#contact" style="margin-top: 12px;">Contact Us</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 beBriz. All rights reserved.</span>
        <div class="footer-bottom-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="../js/main.js"></script>
</body>
</html>'''


def build():
    print("beBriz Theme Sales Page Generator")
    print("=" * 40)

    # Load config
    if not os.path.exists(THEMES_YAML):
        print(f"ERROR: Config file not found: {THEMES_YAML}")
        sys.exit(1)

    config = load_yaml(THEMES_YAML)
    themes = config.get("themes", [])
    print(f"Found {len(themes)} theme(s) in config\n")

    # Generate theme pages
    for theme in themes:
        handle = theme["handle"]
        name = theme.get("name", handle)
        print(f"Building: {name} ({handle})")

        # Generate page HTML
        page_html = generate_theme_page(theme)

        # Write output
        out_dir = os.path.join(THEMES_DIR, handle)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"  Output: themes/{handle}/index.html")

        features_count = len(theme.get("features", []))
        screenshots_count = len(theme.get("screenshots", []))
        faq_count = len(theme.get("faq", []))
        print(f"  Features: {features_count} | Screenshots: {screenshots_count} | FAQ: {faq_count}")

    # Generate themes listing page
    print(f"\nGenerating themes listing page...")
    listing_html = generate_themes_listing(themes)
    listing_path = os.path.join(THEMES_DIR, "index.html")
    with open(listing_path, "w", encoding="utf-8") as f:
        f.write(listing_html)
    print(f"  Output: themes/index.html")

    # Update homepage catalog
    print(f"\nUpdating homepage catalog grid...")
    if update_homepage(themes):
        print(f"  Updated: index.html")
    else:
        print(f"  WARNING: Homepage update had issues (see above)")

    print(f"\nBuild complete! Generated {len(themes)} theme page(s) + themes listing + updated homepage.")


if __name__ == "__main__":
    build()
