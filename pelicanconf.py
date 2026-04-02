from __future__ import annotations

import re

from markupsafe import Markup

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

MARKDOWN = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.attr_list",
        "markdown.extensions.tables",
    ],
}


def add_nofollow_howaiagentswork(html):
    """Post-process rendered HTML: outbound links to howaiagentswork.com get rel=nofollow."""
    if not html:
        return html
    s = str(html)

    def repl(m: re.Match[str]) -> str:
        tag = m.group(0)
        if "rel=" in tag.lower():
            return tag
        return tag.replace("<a ", '<a rel="nofollow noopener noreferrer" ', 1)

    out = re.sub(
        r"<a\s[^>]*href\s*=\s*[\"']https?://(?:www\.)?howaiagentswork\.com[^\"']*[\"'][^>]*>",
        repl,
        s,
        flags=re.IGNORECASE,
    )
    return Markup(out)


JINJA_FILTERS = {
    "add_nofollow_howaiagentswork": add_nofollow_howaiagentswork,
}

