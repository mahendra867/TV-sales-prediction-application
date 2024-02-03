# these are libraries i need for to update the components 
import os
import urllib.request as request # so i use the request to download the data from the URL
import zipfile # here iam using the Zipfile to transform the data 
from TV_sales import logger # here logger is used to logger the data 
from TV_sales.utils.common import get_size # here i used the getsize is used to get to know the file size 
from pathlib import Path
from TV_sales.entity.config_entity import ModelTrainerConfig 
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


# now here iam defining a class called model trainer inside it will take ModelTrainerConfig
class ModelTrainer:
    print("initiated model training")
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    # here iam creating a methode which it will traine the model by using train and test dataset
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path) # here it is taking the paths of train and test dataset
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)  # here iam dropping my target column in train_x
        test_x = test_data.drop([self.config.target_column], axis=1)  # here iam dropping my target column in test_X
        train_y = train_data[[self.config.target_column]]  # here iam keeping the target column in train_y
        test_y = test_data[[self.config.target_column]]  # here iam keeping the target column in test_y


        lr = LinearRegression() # here i have created my Elastic model which it takes the alpha,l1_ratio, random state values 
        lr.fit(train_x, train_y) # here i have initiated the model training

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name)) # here are training my model iam just saving inside the folder Model_trainer which it will get create inside the artifacts