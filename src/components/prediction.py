import os
import pandas as pd
from src.utils.common import *
from src.entity.config_entity import PredictionConfig

class Prediction:
    def __init__(self, config: PredictionConfig) -> None:
        self.config = config
        
        current_file_name = read_file(self.config.root_dir)
        # Read the current CSV file
        self.model = pd.read_csv(os.path.join(self.config.root_dir, current_file_name))
    
    def predict(self, country: str, os: str, sex: str, age: int):
        
        bins = [0, 18, 23, 30, 40, 65, 100]
        
        for i, j in enumerate(bins):
            if age <= j:
                age_range = f"{bins[i-1] + 1}_{j}"
                break
            
        new_customer = country + "_" + os + "_" + sex + "_" + age_range 
        # Return the prediction
        pred = self.model[self.model["customers_level_based"] == new_customer]
        
        if not pred.empty:
            print(pred)
            pred_income = pred["PRICE_MEAN"].values[0]
            pred_segment = pred["SEGMENT"].values[0]
            return pred_income, pred_segment
        
        else:
            print("The prediction is not available for the given input.")
            return None