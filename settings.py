
import json
import os

CONFIG_FILE = "config.json"

DEFAULT_SETTINGS = {
    "glow": True,
    "boxes": True,
    "color": "#a855f7"
}

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_SETTINGS.copy()

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return {**DEFAULT_SETTINGS, **data}
    except (json.JSONDecodeError, OSError):
        return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)
