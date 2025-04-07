from pymongo import MongoClient
from bson.objectid import ObjectId
from models.user import User
from custom_exceptions import MedicalRecordSystemException

class UserRepository:
    def __init__(self, db, collection_name):
        self.collection = db[collection_name]

    def create_user(self, user: User):
        self.collection.insert_one(user.__dict__)

    def get_user_by_id(self, user_id: str) -> User:
        data = self.collection.find_one({"_id": ObjectId(user_id)})
        if not data:
            raise MedicalRecordSystemException(f"User with ID {user_id} not found.")
        return User(**data)

    def update_user(self, user_id: str, update_data: dict):
        result = self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        if result.matched_count == 0:
            raise MedicalRecordSystemException(f"User with ID {user_id} not found.")

    def delete_user(self, user_id: str):
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            raise MedicalRecordSystemException(f"User with ID {user_id} not found.")