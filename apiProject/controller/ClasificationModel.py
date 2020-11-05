import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from model.conectdb import MongoConnection
import pickle

class ClasificationModel:

    def __init__(self, data):
        self.mongoConnection = MongoConnection().get_instance()
        script_dir = os.path.dirname(__file__)
        rel_path = "modelpkl/scaler.sav"
        rel_path2 = "modelpkl/rforest.sav"
        abs_file_path = os.path.join(script_dir, rel_path)
        abs_file_path2 = os.path.join(script_dir, rel_path2)
        self.scaler = pickle.load(open(abs_file_path, 'rb'))
        self.model = pickle.load(open(abs_file_path2, 'rb'))
        if isinstance(data, dict):
            self.data = pd.DataFrame([data])
        else:
            self.data = pd.DataFrame(data)

    def to_datetime(self,date_str):
        return datetime.strptime(date_str,'%Y-%m-%dT%H:%M:%SZ')

    def predict(self):
        self.transforData()
        data = self.model.predict(self.data.values)
        data = pd.DataFrame(data.reshape(-1,1), columns=["taken_prediction"])
        result = pd.concat([self.inverseTransform(), data], axis=1)
        self.mongoConnection.save_data(result.to_dict("records"))
        return result
    
    def getEstimators(self):
        return list(self.mongoConnection.get_data())

    def inverseTransform(self):
        return pd.DataFrame(
                            self.scaler.inverse_transform(self.data),
                            columns=['store_id','to_user_distance','to_user_elevation','total_earning','hour','weekday','month']
               )

    def transforData(self):
        df = self.data
        df["created_at"] = df["created_at"].map(lambda x: self.to_datetime(x))
        df["hour"] = df["created_at"].map(lambda x: x.hour)
        df["weekday"] = df["created_at"].map(lambda x: x.weekday())
        df["month"] = df["created_at"].map(lambda x: x.month)
        df["year"] = df["created_at"].map(lambda x: x.year)

        df = df[['store_id','to_user_distance','to_user_elevation','total_earning','hour','weekday','month']]
        df = pd.DataFrame(
                        self.scaler.transform(df),
                        columns=['store_id','to_user_distance','to_user_elevation','total_earning','hour','weekday','month']
        )
        self.data = df
