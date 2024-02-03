# these are libraries i need for to update the components 
import os
import urllib.request as request # so i use the request to download the data from the URL
import zipfile # here iam using the Zipfile to transform the data 
from TV_sales import logger # here logger is used to logger the data 
from TV_sales.utils.common import get_size # here i used the getsize is used to get to know the file size 
from pathlib import Path
from TV_sales.entity.config_entity import DataValidationConfig 
import pandas as pd

class DataValiadtion: # this is components name 
    def __init__(self, config: DataValidationConfig): # it will take my DataValidationConfig
        self.config = config


    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            # Check if all columns in the schema are present in the dataset
            validation_status = all(col in all_cols for col in all_schema)

            # Write the validation status to the status file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
