import os
from pathlib import Path

LLAMA_STACK_CLIENT_CONFIG_DIR = Path(os.path.expanduser("~/.llama/client"))


def get_config_file_path():
    return LLAMA_STACK_CLIENT_CONFIG_DIR / "config.yaml"
