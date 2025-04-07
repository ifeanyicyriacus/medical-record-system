from user_repository import UserRepository
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
from exceptions.custom_exception import UnauthorizedAccessException, EmailAlreadyExistsException
from models.user import User

load_dotenv()

class AdminRepository(UserRepository):
    def __init__(self):
        super().__init__()
        self.collection = self.db[os.getenv('ADMINS_COLLECTION')]

    def create_admin(self, data):
        return self.create_user(data)

    def get_admin_by_id(self, admin_id):
        admin = self.get_user_by_id(admin_id)
        if not admin:
            raise UnauthorizedAccessException(f"Admin with ID {admin_id} not found.")
        return admin

    def update_admin(self, admin_id, data):
        if not self.get_admin_by_id(admin_id):
            raise UnauthorizedAccessException(f"Admin with ID {admin_id} not found.")
        self.collection.update_one({'_id': ObjectId(admin_id)}, {'$set': data})

    def delete_admin(self, admin_id):
        if not self.get_admin_by_id(admin_id):
            raise UnauthorizedAccessException(f"Admin with ID {admin_id} not found.")
        self.collection.delete_one({'_id': ObjectId(admin_id)})