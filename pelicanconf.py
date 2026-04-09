from __future__ import annotations

import re

from markupsafe import Markup

AUTHOR = "EdelConnect"
SITENAME = "The AI Agents Book"
SITEURL = ""

# Author headshot: place the file in content/images/ (same filename as below).
AUTHOR_PHOTO = "/images/yorgo_petsas_aiagentsbook.jpg"

PATH = "content"
TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "en"

# GA4 Measurement ID
GA4_MEASUREMENT_ID = "G-7FZ2XTFXJB"

# Optional lead capture API endpoint (e.g. Cloudflare Worker URL).
# Leave empty to keep download-only behavior.
LEAD_API_URL = "https://aiagents-leads-api.yorgopecas.workers.dev/lead"

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
STATIC_PATHS = ["es", "downloads", "images"]

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


_H2_SPLIT = re.compile(r"(?=<h2\b)", re.IGNORECASE)
_H3_STEP_SPLIT = re.compile(r'(?=<h3\s[^>]*\bid="step-\d+")', re.IGNORECASE)


def _is_build_track_h2_block(fragment: str) -> bool:
    return bool(re.search(r'\bid=["\']build-track["\']', fragment[:4000], re.IGNORECASE))


def _wrap_build_track(fragment: str) -> str:
    """Split build track into intro + one panel per Step 0–10."""
    chunks = _H3_STEP_SPLIT.split(fragment)
    out: list[str] = []
    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue
        if i == 0:
            out.append(
                '<div class="content-section content-section-build-intro">'
                f"{chunk}"
                "</div>"
            )
        else:
            out.append(
                '<div class="content-section content-section-step">'
                f"{chunk}"
                "</div>"
            )
    return "".join(out)


def sectionize_book_content(html):
    """
    Wrap major h2 regions and each build-track step in visible panels so the page
    reads as sections instead of one continuous column.
    """
    if not html:
        return html
    s = str(html).strip()
    parts = _H2_SPLIT.split(s)
    blocks: list[str] = []
    for i, part in enumerate(parts):
        if not part.strip():
            continue
        if i == 0 and not re.match(r"^\s*<h2\b", part, re.IGNORECASE):
            blocks.append(
                '<div class="content-section content-section-lead">' f"{part}" "</div>"
            )
        elif _is_build_track_h2_block(part):
            blocks.append(_wrap_build_track(part))
        else:
            blocks.append(
                '<div class="content-section content-section-block">' f"{part}" "</div>"
            )
    return Markup("".join(blocks))


JINJA_FILTERS = {
    "add_nofollow_howaiagentswork": add_nofollow_howaiagentswork,
    "sectionize_book_content": sectionize_book_content,
}

