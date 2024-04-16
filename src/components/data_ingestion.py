import pandas as pd
import numpy as np
from dataclasses import dataclass
import os
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
import sys
from data_transformation import *
from mode_trainer import * 


@dataclass
class data_inegestionconfig:
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")

class data_ingestion:
    def __init__(self):
        self.data_ingestion=data_inegestionconfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Data ingestion started")
            df=pd.read_csv("src/notebooks/data/stud.csv")
            logging.info("Data loaded as Dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion.raw_data_path,header=True,index=False)

            logging.info("train test split started")

            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)

            train_data.to_csv(self.data_ingestion.train_data_path,header=True,index=False)
            test_data.to_csv(self.data_ingestion.test_data_path,header=True,index=False)

            return(self.data_ingestion.train_data_path,self.data_ingestion.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)
        
    


if __name__=="__main__":
    data_ingestion_object=data_ingestion()
    train_deta,test_deta=data_ingestion_object.initiate_data_ingestion()
    data_transformation_obj=data_transformation()
    train_arr,test_arr,_=data_transformation_obj.initiate_data_transformation(train_deta,test_deta)
    model_trainer_obj=model_trainer()
    model_trainer_obj.initiate_model_training(train_arr,test_arr)
