# specify the paths of the config files and params file [yaml files]
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

print(CONFIG_FILE_PATH)

__all__ = ["CONFIG_FILE_PATH", "PARAMS_FILE_PATH"]