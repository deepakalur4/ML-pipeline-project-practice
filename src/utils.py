import os
import sys
import pickle
from src.exception import CustomException
from sklearn.metrics import r2_score

def saveobject(file_path,obj):
    try:
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        score=dict()
        for i in models.items():
            model=i[1]
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            score[i[0]]=r2_score(y_test,y_pred)
        return score
    
    except Exception as e:
        raise CustomException(e,sys)   
            