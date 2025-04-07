from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

class UserRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('USERS_COLLECTION')]

    def create_user(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_user_by_id(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})

    def get_user_by_email(self, email):
        return self.collection.find_one({'email_address': email})

    def update_user(self, user_id, data):
        self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})

    def delete_user(self, user_id):
        self.collection.delete_one({'_id': ObjectId(user_id)})

    def get_users_by_role(self, role):
        return list(self.collection.find({'role': role}))