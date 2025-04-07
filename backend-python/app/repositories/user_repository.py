from pymongo import MongoClient
from bson.objectid import ObjectId
from models.user import User
from custom_exception import MedicalRecordSystemException

class UserRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('USERS_COLLECTION')]

    def create_user(self, data):
        if self.get_user_by_email(data['email_address']):
            raise EmailAlreadyExistsException(data['email_address'])

        user = User(**data)
        user.set_password(data['password'])

        result = self.collection.insert_one(user.__dict__)
        inserted_document = self.collection.find_one({"_id": result.inserted_id})

        return inserted_document

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

    def login_user(self, email, password):
        user_data = self.get_user_by_email(email)
        if not user_data:
            raise IncorrectLoginCredentialsException()

        user = User(**user_data)
        if not user.check_password(password):
            raise IncorrectLoginCredentialsException()

        return user
