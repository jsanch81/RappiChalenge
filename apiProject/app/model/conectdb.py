import json
import pandas as pd
from pymongo import MongoClient

class MongoConnection:
    
    __instance__ = None

    def __init__(self):
        self.client = MongoClient('mongo:27017',
                                    username='root',
                                    password='example',
                                    authSource='admin',
                                    authMechanism='SCRAM-SHA-256')
        print(self.client)
        self.db = self.client["admin"]
        print(self.db)
        self.col = self.db["estimators"]
        print(self.col)
        if MongoConnection.__instance__ is None:
            MongoConnection.__instance__ = self

    @staticmethod
    def get_instance():
        if not MongoConnection.__instance__:
            MongoConnection()
        return MongoConnection.__instance__      

    def save_data(self, data):
        return self.__instance__.col.insert_many(data, ordered=False)

    def get_data(self):
        return self.__instance__.col.find({},{'_id': 0})
