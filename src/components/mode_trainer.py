from src.exception import CustomException
from src.logger import logging
import os,sys
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor)
from sklearn.svm import SVR
from src.utils import evaluate_model
from sklearn.metrics import r2_score
from src.utils import saveobject

@dataclass
class model_trainerconfig:
    best_model_pickle_file=os.path.join("artifacts","model.pkl")

class model_trainer:
    def __init__(self):
        self.model_trainer=model_trainerconfig()

    def initiate_model_training(self,train_ar,test_ar):
        try:
            logging.info("Model_training_started")
            X_train,Y_train,X_test,Y_test=[train_ar[:,:-1],train_ar[:,-1],test_ar[:,:-1],test_ar[:,-1]]

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Ride_regressor":Ridge(),
                "Lasso reg":Lasso()
            }

            best_model=evaluate_model(x_train=X_train,y_train=Y_train,x_test=X_test,y_test=Y_test,models=models)

            max_score=(max(best_model.values()))
            best_score_model=[i[0] for i in best_model.items() if i[1]==max_score]

            best_model=models[best_score_model[0]]

            y_pred=best_model.predict(X_test)

      

            saveobject(file_path=self.model_trainer.best_model_pickle_file,obj=best_model)


            return r2_score(Y_test,y_pred)

        except Exception as e:
            raise CustomException(e,sys)   