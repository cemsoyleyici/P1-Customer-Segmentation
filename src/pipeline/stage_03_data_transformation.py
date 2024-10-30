import pandas as pd
from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self, df) -> pd.DataFrame:
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config, df)
            df = data_transformation.transform()
            
            return df
        except Exception as e:
            raise e  