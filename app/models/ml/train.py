import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib 

class LocationModel:
       
    def __init__(self):
        self.df = pd.read_csv('app/datasets/train.csv')
        self.model_fname_ = 'app/models/ml/logistic_regression_v1.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
        

    def _train_model(self):
        X_train = np.array((self.df.iloc[:, :-1])).reshape(len(self.df),2)
        y_train = np.array(self.df.iloc[:, -1:]).reshape(len(self.df))

        # Fit logistic regression
        model = LogisticRegression()
        model.fit(X_train, y_train)     
        return model
    """
    def predict_location(self, x_xoord, y_coord):
        data_in = [[x_xoord, y_coord]]
        prediction = self.model.predict(data_in)[0]
        probability = self.model.predict_proba(data_in)[0].tolist()
        return {'prediction': int(prediction), 'probability': probability}
    """
    
if __name__=="__main__":
    LocationModel()