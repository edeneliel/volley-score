from pymongo import MongoClient
from utilities.singleton import Singleton

MONGO_USER = ''
MONGO_PASSWORD = ''
MONGO_HOST = ''


class MongoConnector(metaclass=Singleton):
    def __init__(self):
        self.client = MongoClient(f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/?retryWrites=true&w=majority')
        self.db = self.client.volleyscore
