import os
from pathlib import Path

OGX_CLIENT_CONFIG_DIR = Path(os.path.expanduser("~/.ogx/client"))


def get_config_file_path():
    return OGX_CLIENT_CONFIG_DIR / "config.yaml"
