
import pandas as pd
from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self, df) -> pd.DataFrame:
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns(df)
            
        except Exception as e:
            raise e