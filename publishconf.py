from __future__ import annotations

import os

PLUGIN_PATHS: list[str] = []

SITEURL = os.environ.get("SITEURL", "https://theaiagentsbook.com")
RELATIVE_URLS = False
OUTPUT_PATH = "output"

