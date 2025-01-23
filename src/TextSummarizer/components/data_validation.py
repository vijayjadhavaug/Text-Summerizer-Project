import os
from TextSummarizer.entity.data_ingestion_config import DataValidationConfig
from TextSummarizer.logging import logger

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config
    
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status=False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation satus: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation satus: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e