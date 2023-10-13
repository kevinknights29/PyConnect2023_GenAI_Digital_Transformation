from __future__ import annotations

import os

# Directories
MODULE_FOLDER = os.path.dirname(os.path.abspath(__file__))
APP_FOLDER = os.path.dirname(os.path.dirname(MODULE_FOLDER))
STYLES_FOLDER = os.path.join(APP_FOLDER, "styles")
ASSETS_FOLDER = os.path.join(APP_FOLDER, "assets")

# Files
CONFIG_FILE = os.path.join(APP_FOLDER, "config.yml")
