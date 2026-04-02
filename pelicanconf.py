from __future__ import annotations

AUTHOR = "EdelConnect"
SITENAME = "The AI Agents Book"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "en"

# GA4 Measurement ID is intentionally disabled until you provide it.
GA4_MEASUREMENT_ID = ""

THEME = "simple"
EXTRA_TEMPLATES_PATHS = ["themes/aiagents_theme/templates"]

# Home page should live at /en/ and /es/.
PAGE_URL = "{lang}/"
PAGE_SAVE_AS = "{lang}/index.html"

# No chapter posts in the book site yet (only pages + later articles).
ARTICLE_URL = "{lang}/{slug}/"
ARTICLE_SAVE_AS = "{lang}/{slug}/index.html"

PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["posts"]

# Copy Spanish placeholder to /es/.
STATIC_PATHS = ["es"]

RELATIVE_URLS = True

DEFAULT_METADATA = {
    "lang": DEFAULT_LANG,
}

