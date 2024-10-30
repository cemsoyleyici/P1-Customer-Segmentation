from src.config.configuration import ConfigurationManager
from src.components.model_generation import ModelGeneration

class ModelGenerationPipeline:
    def __init__(self):
        pass
    
    def main(self, df):
        try:
            config = ConfigurationManager()
            model_generation_config = config.get_model_generation_config()
            model_generation = ModelGeneration(model_generation_config, df)
            model_generation.segments_customers()
        except Exception as e:
            raise e   