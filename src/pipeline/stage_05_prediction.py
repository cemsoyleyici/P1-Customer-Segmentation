from src.config.configuration import ConfigurationManager
from src.components.prediction import Prediction

class PredictionPipeline:
    
    def __init__(self):
        pass
    
    def main(self, country: str, os: str, sex: str, age: int):
        try:
            config = ConfigurationManager()
            pediction_config = config.get_prediction_config()
            prediction = Prediction(pediction_config)
            return prediction.predict(country, os, sex, age)
        
        except Exception as e:
            raise e  
    
    