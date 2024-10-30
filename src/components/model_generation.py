import pandas as pd
from datetime import datetime
from src.entity.config_entity import ModelGenerationConfig

class ModelGeneration:
    def __init__(self, config: ModelGenerationConfig, df: pd.DataFrame) -> None:
        self.config = config
        self.df = df

    def segments_customers(self):
        labels = self.config.labels
        # Segment the customers
        self.df["SEGMENT"] = pd.qcut(self.df["PRICE_MEAN"], len(labels), labels=labels)
        
        today = datetime.today().strftime("%Y-%m-%d")
        self.df.to_csv(self.config.root_dir + "/" + f"segmentation_model_{today}.csv", index=False)