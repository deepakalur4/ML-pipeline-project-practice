import pandas as pd
import numpy as np
from dataclasses import dataclass
import sys,os
from src.logger import logging
from src.exception import CustomException
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from src.utils import saveobject

@dataclass
class data_transformationconfig:
    preprocessor_pickle_file_path=os.path.join("artifacts","preprocessor.pkl")

class data_transformation:
    def __init__(self):
        self.data_transformation=data_transformationconfig()

    def get_preprocessor_object(self):
        try:
            logging.info("creation of a preprocessor obejct started")
            num_columns=["writing_score", "reading_score"]
            cat_columns= [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline=Pipeline([("Imputer",SimpleImputer(strategy="median")),("scaling",StandardScaler())])
            cat_pipeline=Pipeline([("Imputer",SimpleImputer(strategy="most_frequent")),("Encoder",OneHotEncoder()),("scaling",StandardScaler(with_mean=False))])

            preprocessor=ColumnTransformer([("Num_pipeline",num_pipeline,num_columns),("cat_pipeline",cat_pipeline,cat_columns)])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)  

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            logging.info("Data transformation_started")
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            preprocessor_object=self.get_preprocessor_object()
        

            target_column="math_score"

            input_feature_train_data=train_data.drop(columns=[target_column],axis=1)
            target_feature_train_data=train_data[target_column]

            input_feature_test_data=test_data.drop(columns=[target_column],axis=1)
            target_feature_test_data=test_data[target_column]

            input_feature_train_arr=preprocessor_object.fit_transform(input_feature_train_data)
            input_feature_test_arr=preprocessor_object.transform(input_feature_test_data)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_data)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_data)]

            saveobject(

                file_path=self.data_transformation.preprocessor_pickle_file_path,
                obj=preprocessor_object

            )

            return (train_arr,test_arr,self.data_transformation.preprocessor_pickle_file_path)
        
        except Exception as e:
            raise CustomException(e,sys)