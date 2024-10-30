import pandas as pd
from datetime import datetime
from src.utils.eda import *
from src.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig, df: pd.DataFrame) -> None:
        self.config = config
        self.df = df
    
    def target_analysis(self) -> pd.DataFrame:
        # Analysis of Target Variable
        self.df = target_summary_with_cat(self.df, "PRICE", ["COUNTRY", "SOURCE", "SEX", "AGE"]).reset_index()
    
    def determine_age_groups(self) -> pd.DataFrame:
        # Determine the age groups
        # bins = [0, 18, 23, 30, 40, self.df["AGE"].max()]
        bins = [0, 18, 23, 30, 40, 65, 100]
        # Create labels for these bins
        # mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(self.df["AGE"].max())]
        mylabels = ['0_18', '19_23', '24_30', '31_40', '41_65', '66_100']
        self.df["age_cat"] = pd.cut(self.df["AGE"], bins, labels=mylabels)
    
    def create_customer_definition(self) -> pd.DataFrame:
        # Create level based customer definition
        self.df['customers_level_based'] = self.df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].agg(lambda x: '_'.join(x).upper(), axis=1)
        
        # Select the columns of interest
        self.df = self.df[["customers_level_based", "PRICE_MEAN"]]
        
    def singularize_customers(self) -> pd.DataFrame:
    
        # Check the number of customer definition
        num_df = self.df["customers_level_based"].value_counts().reset_index()    
        
        # Singularize the customer definition
        if len(num_df) != sum(num_df["count"]):
            
            self.df = self.df.groupby("customers_level_based").agg({"PRICE_MEAN": "mean"}).reset_index()
        else:
            pass
        
        today = datetime.today().strftime("%Y-%m-%d")
        self.df.to_csv(self.config.root_dir + "/" + f"customer_definition_{today}.csv", index=False)
    
    def transform(self) -> pd.DataFrame:
        self.target_analysis()
        self.determine_age_groups()
        self.create_customer_definition()
        self.singularize_customers()
        
        return self.df