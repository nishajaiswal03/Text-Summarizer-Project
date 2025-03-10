from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    source_URL: str
    root_dir: str
    local_data_file: str
    unzip_dir: str
