import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from app.models.user import User
from app.exceptions.custom_exception import (
    EmailAlreadyExistsException,
    IncorrectLoginCredentialsException,
    MedicalRecordSystemException,
    PatientNotFoundException
)

class UserRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('USERS_COLLECTION')]

    def create_user(self, data: dict) -> dict:
        if self.get_user_by_email(data['email_address']):
            raise EmailAlreadyExistsException(data['email_address'])

        password = data.pop('password', None)
        if not password:
            raise MedicalRecordSystemException("Password is required.")

        user = User(**data, hash_password="")
        user.set_password(password)

        try:
            result = self.collection.insert_one(user.__dict__)
            user_dict = self.get_user_by_id(result.inserted_id)

            user_dict['_id'] = str(user_dict['_id'])

            return user_dict
        except Exception:
            raise MedicalRecordSystemException("Failed to create user.")


    def get_user_by_id(self, user_id: str) -> dict:
        user = self.collection.find_one({'_id': ObjectId(user_id)})
        if not user:
            raise PatientNotFoundException(user_id)
        return user

    def get_user_by_email(self, email: str) -> dict:
        return self.collection.find_one({'email_address': email})

    def update_user(self, user_id: str, data: dict) -> None:
        try:
            self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
        except Exception:
            raise MedicalRecordSystemException("Failed to update user.")

    def delete_user(self, user_id: str) -> None:
        try:
            self.collection.delete_one({'_id': ObjectId(user_id)})
        except Exception:
            raise MedicalRecordSystemException("Failed to delete user.")

    def get_users_by_role(self, role: str) -> list:
        return list(self.collection.find({'role': role}))

    def login_user(self, email: str, password: str) -> User:
        user_data = self.get_user_by_email(email)
        if not user_data:
            raise IncorrectLoginCredentialsException()

        user = User(**user_data)
        if not user.check_password(password):
            raise IncorrectLoginCredentialsException()

        return user
