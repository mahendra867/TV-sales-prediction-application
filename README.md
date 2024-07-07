# End-to-End Advertising Sales Prediction

#### Working of an Application

https://github.com/mahendra867/TV-sales-prediction-application/assets/95703197/ce1f24ac-4250-4233-b3c5-620ede05f7c5



## Problem Statement
Description:
The advertising dataset captures the sales revenue generated with respect to advertisement costs across multiple channels like radio, tv, and newspapers.

It is required to understand the impact of ad budgets on the overall sales.




## Approach 

### Data Ingestion
- Description: In this stage, the data ingestion process is performed to obtain the advertising dataset required for sales prediction.
- Approach: Utilize the provided DataIngestion class to download the dataset from a specified URL and extract it into the local data directory.
- Techniques Used: Python libraries such as os, urllib, and zipfile are employed for file handling and extraction. Logging is implemented using the logger module.
- Outcome: The advertising dataset is successfully downloaded, and the zip file is extracted into the designated directory.

### Data Validation
- Description: This stage involves validating the dataset to ensure its consistency and adherence to predefined schema.
- Approach: Employ the DataValidation class to check if all the columns in the dataset match those specified in the schema. The validation status is then written to a status file.
- Techniques Used: Data validation is performed using Python's pandas library to compare dataset columns with the schema.
- Outcome: The validation status, indicating whether all columns match the schema, is recorded for further reference.

### Data Transformation
- Description: Data transformation is carried out to prepare the dataset for model training by scaling and preprocessing features.
- Approach: Use the DataTransformation class to perform feature scaling, specifically standardizing the 'Radio' and 'TV' columns.
- Techniques Used: Standardization of numerical features is achieved by computing z-scores.
- Outcome: The dataset is transformed with scaled features, facilitating improved model performance during training.

### Model Training
- Description: This stage involves training a machine learning model to predict sales revenue based on advertising budgets.
- Approach: Utilize the ModelTrainer class to train a Linear Regression model using the preprocessed dataset.
- Techniques Used: Linear Regression algorithm is employed for its simplicity and effectiveness in predicting continuous target variables.
- Outcome: A trained Linear Regression model is saved to the designated directory for future use.

### Model Evaluation
- Description: The trained model's performance is evaluated to assess its accuracy and effectiveness in predicting sales revenue.
- Approach: Employ the ModelEvaluation class to predict sales revenue using the trained model and calculate evaluation metrics such as RMSE, MAE, and R2 score.
- Techniques Used: Evaluation metrics are calculated using functions from the sklearn.metrics library.
- Outcome: Evaluation metrics are saved as JSON files for analysis, providing insights into the model's predictive capabilities.

By following this workflow, the end-to-end process of advertising sales prediction is successfully executed, enabling businesses to make informed decisions based on predicted sales revenue.


## WorkFlows

1. Update config.yam1
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the [main.py](http://main.py/)
9. Update the [app.py](http://app.py/)




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/mahendra867/random_datasets/raw/main/TV_Sales.zip 
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```





