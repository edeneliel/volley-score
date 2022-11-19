from pymongo import MongoClient
from utilities.config import Constants
from utilities.singleton import Singleton


class MongoConnector(metaclass=Singleton):
    def __init__(self):
        host = Constants.MONGO_HOST
        user = Constants.MONGO_USER
        password = Constants.MONGO_PASSWORD

        self.client = MongoClient(f'mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority')
        self.db = self.client.volleyscore
