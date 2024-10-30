from dataclasses import dataclass
from pathlib import Path

# Data Ingestion Config
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path

# Data Validation Config    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    all_schema: dict    
    
# Data Transformation Config    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path   
    
# Model Generation Config    
@dataclass(frozen=True)
class ModelGenerationConfig:
    root_dir: Path
    labels: list      

# Model Generation Config    
@dataclass(frozen=True)
class PredictionConfig:
    root_dir: Path