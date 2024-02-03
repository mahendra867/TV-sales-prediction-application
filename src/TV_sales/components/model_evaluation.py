import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score # here i have imported all the evaluation meterics for evaluating our model peformance
import numpy as np
import joblib
from TV_sales.entity.config_entity import ModelEvaluationConfig
from TV_sales.utils.common import save_json
from pathlib import Path


# here i have defined one ModelEvaluation class in which i have defined the ModelEvaluationConfig
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    # here i have defiend the eval_metrics which it evaluates our model performance by calculating the rmse,mae,r2
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    

# here i have defined one fucntion called log_into_mlflow which it will mlflow 
    def predict_the_model(self):

        test_data = pd.read_csv(self.config.test_data_path) # here iam loading the test dataset
        model = joblib.load(self.config.model_path) # here iam loading my trained model 

        test_x = test_data.drop([self.config.target_column], axis=1) # here iam dropping my targetcolumn in test_x
        test_y = test_data[[self.config.target_column]] # here iam keeping my target column


        predicted_qualities = model.predict(test_x) # here iam predicting my testing data

        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities) # here it is calculating my metrics of the predicted model
            
        # Saving metrics as local
        scores = {"rmse": rmse, "mae": mae, "r2": r2} # these scores are saving inside my artifacts of model_evaluation as a jason file
        save_json(path=Path(self.config.metric_file_name), data=scores)

            

