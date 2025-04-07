from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
from exceptions.custom_exception import AppointmentNotFoundException, ValidationError, DatabaseError

load_dotenv()


class AppointmentRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('APPOINTMENTS_COLLECTION')]

    def create_appointment(self, data):
        if not data.get('patient_id') or not data.get('doctor_id'):
            raise ValidationError("Appointment must have a patient_id and a doctor_id")

        try:
            result = self.collection.insert_one(data)
            inserted_document = self.collection.find_one({"_id": result.inserted_id})
            return inserted_document
        except Exception as e:
            raise DatabaseError(f"Error creating appointment: {str(e)}")

    def get_appointment_by_id(self, appointment_id):
        appointment = self.collection.find_one({'_id': ObjectId(appointment_id)})
        if not appointment:
            raise AppointmentNotFoundException(appointment_id)
        return appointment

    def get_all_appointments(self):
        try:
            return list(self.collection.find({}))
        except Exception as e:
            raise DatabaseError(f"Error fetching appointments: {str(e)}")

    def update_appointment(self, appointment_id, data):
        if not self.get_appointment_by_id(appointment_id):
            raise AppointmentNotFoundException(appointment_id)
        self.collection.update_one({'_id': ObjectId(appointment_id)}, {'$set': data})

    def delete_appointment(self, appointment_id):
        if not self.get_appointment_by_id(appointment_id):
            raise AppointmentNotFoundException(appointment_id)
        self.collection.delete_one({'_id': ObjectId(appointment_id)})