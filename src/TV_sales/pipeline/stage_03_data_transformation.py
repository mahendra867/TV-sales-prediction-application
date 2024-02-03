# then import the neccessary  libraries
from TV_sales.config.configuration import ConfigurationManager
from TV_sales.components.data_transformation import DataTransformation
from TV_sales import logger

# here iam defined one class w.r.t name of the stage
STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline: # inside this DataValidationTrainingPipeline iam creating one main method
    def __init__(self):
        pass

    def main(self): # this the main method
        config = ConfigurationManager() # here iam initlizing my ConfigurationManager
        data_transformation_config = config.get_data_transformation_config() # and here iam getting my get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config) # here iam passing my data_transformation_config it means iam calling this data_transformation_config
        scaled_data=data_transformation.feature_scalling()
        data_transformation.train_test_spliting(scaled_data) # here performing the train_test_split()



# now iam calling the above code inside the below main fucntion

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline() # logging is started calling the class DataValidationTrainingPipeline
        obj.main() # here calling this main method from this class
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:  # if anything error in this code then we are telling this part of code to raise exception
        logger.exception(e)
        raise e
    
