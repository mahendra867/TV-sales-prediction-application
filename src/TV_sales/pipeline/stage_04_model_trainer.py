from TV_sales.config.configuration import ConfigurationManager
from TV_sales.components.model_trainer import ModelTrainer
from TV_sales import logger


 # here i have named a stage name w.r.t below 1 class created 
STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline: # here i have created a class
    def __init__(self):
        pass

    def main(self): # here i have created a main methode 
        config = ConfigurationManager()  # here i taken created pipeline of model trainer  in sequence one by one step
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()





# Now here i will initilized the pipeline of model trainer inside my main methode

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e