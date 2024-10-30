
import pandas as pd
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self) -> pd.DataFrame:
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data = data_ingestion.read_data(data_ingestion_config.local_data_file)
            return data
        except Exception as e:
            raise e