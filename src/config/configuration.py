
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import (DataIngestionConfig,
                                      DataValidationConfig,
                                      DataTransformationConfig,
                                      ModelGenerationConfig,
                                      PredictionConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
        
    # Data Ingestion Configuration       
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # config\config.yaml 
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_file = config.local_data_file,
        )
        
        return data_ingestion_config
    
    # Data Validation Configuration  
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation # config\config.yaml 
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema,
        )
        
        return data_validation_config
    
    # Data Transformation Configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir
            )
        
        return data_transformation_config
    
    # Model Generation Configuration
    def get_model_generation_config(self) -> ModelGenerationConfig:
        config = self.config.model_generation
        params = self.params.PARAMETERS
        create_directories([config.root_dir])
        
        model_generation_config = ModelGenerationConfig(
            root_dir=config.root_dir,
            labels=params.labels
            )
        return model_generation_config
    
    # Prediction Configuration
    def get_prediction_config(self) -> PredictionConfig:
        config = self.config.prediction
        
        create_directories([config.root_dir])
        
        prediction_config = PredictionConfig(
            root_dir=config.root_dir,
            )
        return prediction_config