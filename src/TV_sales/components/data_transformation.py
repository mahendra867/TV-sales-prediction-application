import os
from TV_sales import logger
from sklearn.model_selection import train_test_split
from TV_sales.entity.config_entity import DataTransformationConfig
import pandas as pd



# here i defined the component of DataTransformationConfig below
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def feature_scalling(self):
        data = pd.read_csv(self.config.data_path)
        data.drop('Newspaper',axis=1,inplace=True)
        standardized_radio=((data['Radio']-data['Radio'].mean())/data['Radio'].std())
        standardized_tv =((data['TV']-data['TV'].mean())/data['TV'].std())
        data['Radio'] = standardized_radio # replaced those scalled values in the columns of tv and radio
        data['TV'] = standardized_tv

        print(data.head)
        return data # here iam returning my scaled data to save in the object of this Data_transformation class



    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


# here i have defined the tarin_test_split below for performing the train_test_split
    def train_test_spliting(self,scaled_data):
        

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(scaled_data) # this line splits the data into train_test_split

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False) # here it saves the train and test data in csv format inisde the artifacts-> transformation folder
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape) # this logs the information about that how many training and testing samples i have 
        logger.info(test.shape)

        print(train.head())
        print(train.shape)
        print(test.shape)