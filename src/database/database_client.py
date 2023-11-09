from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from os import getenv


class DatabaseClient:
    client: MongoClient | None = None
    database: Database | None = None
    users_collection: Collection | None = None

    @classmethod
    def connect(cls):
        cls.client = MongoClient(getenv('MONGO_URI'))
        cls.database = cls.client.get_database('chat_artifico')
        cls.users_collection = cls.database.get_collection('users')
