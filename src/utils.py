import os
import sys
import pickle
from src.exception import CustomException

def saveobject(file_path,obj):
    try:
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
