#!/usr/bin/env python3
"""
beBriz Documentation Site Generator
====================================
Reads theme definitions from docs_config/themes.yaml and markdown section
templates from docs_config/sections/*.md, then generates:
  - docs/{theme-handle}/index.html  (individual theme doc pages)
  - docs/index.html                 (docs index with theme cards)

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
CONFIG_DIR = os.path.join(SCRIPT_DIR, "docs_config")
THEMES_YAML = os.path.join(CONFIG_DIR, "themes.yaml")
SECTIONS_DIR = os.path.join(CONFIG_DIR, "sections")
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")

# ---------------------------------------------------------------------------
# Simple YAML parser (fallback when PyYAML is not installed)
# ---------------------------------------------------------------------------

def _simple_yaml_parse(text):
    """Minimal YAML parser that handles the themes.yaml structure."""
    themes = []
    current_theme = None
    current_list_key = None

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
            current_theme = {
                "handle": stripped.split(":", 1)[1].strip().strip('"'),
                "features": [],
                "sections": [],
            }
            themes.append(current_theme)
            current_list_key = None
            continue

        if current_theme is None:
            continue

        # Scalar fields
        if indent == 4 and ":" in stripped and not stripped.startswith("- "):
            key, val = stripped.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"')
            if val:
                current_theme[key] = val
                current_list_key = None
            else:
                current_list_key = key
            continue

        # List items
        if indent == 6 and stripped.startswith("- "):
            item = stripped[2:].strip().strip('"')
            if current_list_key and current_list_key in current_theme:
                current_theme[current_list_key].append(item)
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
# Markdown-to-HTML converter
# ---------------------------------------------------------------------------

def md_to_html(md_text):
    """Convert markdown text to HTML.

    Supported syntax:
      ## / ### headings
      **bold**
      `inline code`
      ```code blocks```
      - unordered lists
      1. ordered lists
      [text](url) links
      > **Tip:** / > **Note:** callout blocks
      Paragraphs separated by blank lines
    """
    lines = md_text.split("\n")
    html_parts = []
    i = 0

    def inline(text):
        """Process inline markdown."""
        # Escape HTML entities first (but preserve already-safe chars)
        text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        # Code spans (before bold to avoid conflicts)
        text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
        # Bold
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        # Links
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
        # Em dash
        text = text.replace(" --- ", " &mdash; ")
        text = text.replace(" -- ", " &mdash; ")
        # The mdash pattern from original: —
        text = text.replace("—", "&mdash;")
        return text

    while i < len(lines):
        line = lines[i]

        # Skip blank lines
        if not line.strip():
            i += 1
            continue

        # Fenced code block
        if line.strip().startswith("```"):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(html_module.escape(lines[i]))
                i += 1
            i += 1  # skip closing ```
            html_parts.append(
                "<pre><code>" + "\n".join(code_lines) + "</code></pre>"
            )
            continue

        # Headings
        if line.startswith("### "):
            html_parts.append("<h3>" + inline(line[4:].strip()) + "</h3>")
            i += 1
            continue
        if line.startswith("## "):
            html_parts.append("<h2>" + inline(line[3:].strip()) + "</h2>")
            i += 1
            continue

        # Callout / blockquote block
        if line.startswith("> "):
            callout_lines = []
            while i < len(lines) and lines[i].startswith("> "):
                callout_lines.append(lines[i][2:])
                i += 1
            callout_text = " ".join(callout_lines)
            # Determine callout type
            css_class = "callout"
            if "**Tip:**" in callout_text or "**Pro tip:**" in callout_text:
                css_class = "callout callout-tip"
            html_parts.append(
                '<div class="' + css_class + '">\n  <p>' + inline(callout_text) + "</p>\n</div>"
            )
            continue

        # Ordered list
        if re.match(r"^\d+\.\s", line.strip()):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                item_text = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                items.append("  <li>" + inline(item_text) + "</li>")
                i += 1
            html_parts.append("<ol>\n" + "\n".join(items) + "\n</ol>")
            continue

        # Unordered list
        if line.strip().startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                item_text = lines[i].strip()[2:]
                items.append("  <li>" + inline(item_text) + "</li>")
                i += 1
            html_parts.append("<ul>\n" + "\n".join(items) + "\n</ul>")
            continue

        # Paragraph — collect consecutive non-empty, non-special lines
        para_lines = []
        while i < len(lines) and lines[i].strip() and \
              not lines[i].startswith("### ") and \
              not lines[i].startswith("## ") and \
              not lines[i].startswith("> ") and \
              not lines[i].strip().startswith("- ") and \
              not re.match(r"^\d+\.\s", lines[i].strip()) and \
              not lines[i].strip().startswith("```"):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            html_parts.append("<p>" + inline(" ".join(para_lines)) + "</p>")

    return "\n\n".join(html_parts)


def parse_section_file(path):
    """Parse a section markdown file, returning (frontmatter_dict, html_content)."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Parse front matter
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
            body = parts[2].strip()

    return meta, md_to_html(body)


# ---------------------------------------------------------------------------
# HTML Templates
# ---------------------------------------------------------------------------

def theme_doc_page(theme, sidebar_links, content_html, root_prefix="../../"):
    """Generate a complete theme documentation page."""
    title = f'{theme["name"]} Documentation &mdash; beBriz'
    description = f'Complete documentation for the {theme["name"]} Shopify theme by beBriz. Installation, setup, features, customization, and troubleshooting.'

    sidebar_html = ""
    for sid, stitle in sidebar_links:
        sidebar_html += f'        <a href="#{sid}">{html_module.escape(stitle)}</a>\n'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{html_module.escape(description)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root_prefix}css/style.css">
</head>
<body>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="{root_prefix}index.html" class="logo"><span>be</span>Briz</a>
      <nav class="nav-links">
        <a href="{root_prefix}index.html">Home</a>
        <a href="{root_prefix}themes/index.html">Themes</a>
        <a href="{root_prefix}docs/index.html" class="active">Documentation</a>
        <a href="{root_prefix}support/index.html">Support</a>
      </nav>
      <button class="mobile-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Mobile sidebar toggle -->
  <button class="docs-sidebar-toggle">Show Navigation</button>

  <!-- Docs Layout -->
  <div class="docs-layout">

    <!-- Sidebar -->
    <aside class="docs-sidebar">
      <div class="sidebar-logo">
        <a href="{root_prefix}index.html" class="logo" style="font-size: 1.2rem;"><span>be</span>Briz</a>
      </div>
      <nav>
        <h3>Documentation</h3>
{sidebar_html}      </nav>
    </aside>

    <!-- Main Content -->
    <main class="docs-main">
      <div class="docs-breadcrumb">
        <a href="{root_prefix}index.html">Home</a>
        <span>/</span>
        <a href="{root_prefix}docs/index.html">Docs</a>
        <span>/</span>
        {html_module.escape(theme["name"])}
      </div>

      <div class="docs-content">
        <h1>{html_module.escape(theme["name"])} Documentation</h1>
        <p>This comprehensive guide covers everything you need to install, configure, and customize the {html_module.escape(theme["name"])} Shopify theme. Use the sidebar navigation to jump to a specific section, or scroll through for the complete reference.</p>

{content_html}

      </div>
    </main>
  </div>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="{root_prefix}index.html" class="logo"><span>be</span>Briz</a>
          <p>Premium Shopify themes for modern e-commerce. Designed and developed with an obsession for quality, performance, and detail.</p>
          <div class="footer-tagline">Powered by beBriz</div>
        </div>
        <div class="footer-col">
          <h4>Themes</h4>
          <a href="{root_prefix}themes/luxe-fashion/index.html">Luxe Fashion</a>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <a href="{root_prefix}docs/index.html">Documentation</a>
          <a href="{root_prefix}support/index.html">Support</a>
        </div>
        <div class="footer-col">
          <h4>Connect</h4>
          <div class="footer-social">
            <a href="#" aria-label="Twitter">X</a>
            <a href="#" aria-label="GitHub">GH</a>
            <a href="#" aria-label="Dribbble">Dr</a>
          </div>
          <a href="{root_prefix}support/index.html#contact" style="margin-top: 12px;">Contact Us</a>
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

  <script src="{root_prefix}js/main.js"></script>
</body>
</html>
'''


def docs_index_page(themes):
    """Generate the docs index page with theme cards."""
    cards_html = ""
    for theme in themes:
        feature_count = len(theme.get("features", []))
        cards_html += f'''        <a href="{theme["handle"]}/index.html" class="docs-theme-card glass-card">
          <div class="docs-theme-card-body">
            <h3>{html_module.escape(theme["name"])}</h3>
            <p>{html_module.escape(theme.get("description", ""))}</p>
            <div class="docs-theme-card-meta">
              <span class="docs-theme-badge">{feature_count} Features</span>
              <span class="docs-theme-price">{html_module.escape(theme.get("price", ""))}</span>
            </div>
          </div>
          <span class="docs-theme-card-link">View Docs &rarr;</span>
        </a>
'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Documentation &mdash; beBriz</title>
  <meta name="description" content="Browse documentation for all beBriz premium Shopify themes. Installation guides, feature references, and customization instructions.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="../index.html" class="logo"><span>be</span>Briz</a>
      <nav class="nav-links">
        <a href="../index.html">Home</a>
        <a href="../themes/index.html">Themes</a>
        <a href="index.html" class="active">Documentation</a>
        <a href="../support/index.html">Support</a>
      </nav>
      <button class="mobile-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Hero -->
  <section class="hero" style="padding: 120px 0 60px;">
    <div class="container">
      <div class="hero-content">
        <h1>
          <span class="gradient-text">Documentation</span>
        </h1>
        <p>Select a theme to view its documentation</p>
      </div>
    </div>
  </section>

  <!-- Theme Cards -->
  <section class="section" style="padding-top: 20px;">
    <div class="container">
      <div class="docs-theme-grid">
{cards_html}      </div>
    </div>
  </section>

  <!-- Footer -->
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
          <a href="../themes/luxe-fashion/index.html">Luxe Fashion</a>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <a href="index.html">Documentation</a>
          <a href="../support/index.html">Support</a>
          <a href="../support/index.html#faq">FAQ</a>
        </div>
        <div class="footer-col">
          <h4>Connect</h4>
          <div class="footer-social">
            <a href="#" aria-label="Twitter">X</a>
            <a href="#" aria-label="GitHub">GH</a>
            <a href="#" aria-label="Dribbble">Dr</a>
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
</html>
'''


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build():
    print("beBriz Documentation Builder")
    print("=" * 40)

    # Load config
    config = load_yaml(THEMES_YAML)
    themes = config.get("themes", [])
    print(f"Found {len(themes)} theme(s) in config\n")

    for theme in themes:
        handle = theme["handle"]
        name = theme["name"]
        sections = theme.get("sections", [])
        print(f"Building: {name} ({handle})")
        print(f"  Sections: {len(sections)}")

        # Process sections
        sidebar_links = []
        all_content = []

        for section_id in sections:
            md_path = os.path.join(SECTIONS_DIR, f"{section_id}.md")
            if not os.path.exists(md_path):
                print(f"  WARNING: Section file not found: {md_path}")
                continue

            meta, section_html = parse_section_file(md_path)
            section_title = meta.get("title", section_id.replace("-", " ").title())
            sid = meta.get("id", section_id)

            sidebar_links.append((sid, section_title))

            # Wrap section content with id anchor on the h2
            section_block = f'        <!-- {section_title} -->\n'
            section_block += f'        <h2 id="{sid}">{html_module.escape(section_title)}</h2>\n\n'
            # Indent content
            for line in section_html.split("\n"):
                section_block += f'        {line}\n'

            all_content.append(section_block)

        content_html = "\n".join(all_content)

        # Generate page
        page_html = theme_doc_page(theme, sidebar_links, content_html)

        # Write output
        out_dir = os.path.join(DOCS_DIR, handle)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"  Output: docs/{handle}/index.html")

    # Generate docs index
    index_html = docs_index_page(themes)
    index_path = os.path.join(DOCS_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"\nGenerated: docs/index.html")

    print(f"\nBuild complete! Generated {len(themes)} theme doc(s) + index page.")


if __name__ == "__main__":
    build()
