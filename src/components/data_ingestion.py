import pandas as pd
from src.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config
        
    def read_data(self, path: str) -> pd.DataFrame:
        
        
        if path.endswith("csv") or path.endswith("xlsx") or path.endswith("xls"):
            df = pd.read_csv(path)
            return df
        
        elif path.endswith("xlsx") or path.endswith("xls"):
            df = pd.read_excel(path)
            return df

        else:
            print("The file format is not supported. Supported formats are csv, xlsx, xls")