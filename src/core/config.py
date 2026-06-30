import yaml
from src.core.paths import CONFIG_DIR


SETTINGS_FILE = CONFIG_DIR/"settings.yaml"


def load_settings():
    with open(
        SETTINGS_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return yaml.safe_load(f)