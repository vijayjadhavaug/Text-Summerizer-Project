from dataclasses import dataclass
from pathlib import Path
# when you use this class, you will get the values from config.yaml file
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path