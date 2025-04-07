from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

class AdminRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('ADMINS_COLLECTION')]

    def create_admin(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_admin_by_id(self, admin_id):
        return self.collection.find_one({'_id': ObjectId(admin_id)})

    def get_all_admins(self):
        return list(self.collection.find({}))

    def update_admin(self, admin_id, data):
        self.collection.update_one({'_id': ObjectId(admin_id)}, {'$set': data})

    def delete_admin(self, admin_id):
        self.collection.delete_one({'_id': ObjectId(admin_id)})