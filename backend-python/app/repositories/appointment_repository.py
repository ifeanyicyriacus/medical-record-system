from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

class AppointmentRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('APPOINTMENTS_COLLECTION')]

    def create_appointment(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_appointment_by_id(self, appointment_id):
        return self.collection.find_one({'_id': ObjectId(appointment_id)})

    def get_all_appointments(self):
        return list(self.collection.find({}))

    def update_appointment(self, appointment_id, data):
        self.collection.update_one({'_id': ObjectId(appointment_id)}, {'$set': data})

    def delete_appointment(self, appointment_id):
        self.collection.delete_one({'_id': ObjectId(appointment_id)})