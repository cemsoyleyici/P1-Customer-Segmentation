import pandas as pd
from datetime import datetime
from src.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self, df) -> bool:    
        try:
            validation_status = None
            
            all_cols = list(df.columns)
            
            all_schema = self.config.all_schema.keys()
                
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status},\nColumn: {col}")
                        
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status} - {datetime.now()}")
                
            return validation_status     
            
        except Exception as e:
            raise e