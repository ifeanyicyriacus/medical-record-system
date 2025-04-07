from datetime import datetime
from typing import Optional, List

from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
from exceptions.custom_exception import AppointmentNotFoundException, ValidationError, DatabaseError
from models.appointment import Appointment

load_dotenv()

class AppointmentRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('APPOINTMENTS_COLLECTION')]

    def create_appointment(self, data: dict) -> dict:
        if not data.get('patient_id') or not data.get('doctor_id'):
            raise ValidationError("Appointment must have a patient_id and a doctor_id")

        try:
            result = self.collection.insert_one(data)
            inserted_document = self.collection.find_one({"_id": result.inserted_id})
            return inserted_document
        except Exception as e:
            raise DatabaseError(f"Error creating appointment: {str(e)}")

    def get_appointment_by_id(self, appointment_id: str) -> dict:
        appointment = self.collection.find_one({'_id': ObjectId(appointment_id)})
        if not appointment:
            raise AppointmentNotFoundException(appointment_id)
        return appointment

    def get_appointments_by_patient(self, patient_id: str) -> list:
        try:
            return list(self.collection.find({'patient_id': patient_id}))
        except Exception as e:
            raise DatabaseError(f"Error fetching appointments by patient: {str(e)}")

    def get_appointments_by_doctor(self, doctor_id: str) -> list:
        try:
            return list(self.collection.find({'doctor_id': doctor_id}))
        except Exception as e:
            raise DatabaseError(f"Error fetching appointments by doctor: {str(e)}")

    def update_appointment(self, appointment_id: str, data: dict) -> None:
        if not self.get_appointment_by_id(appointment_id):
            raise AppointmentNotFoundException(appointment_id)
        self.collection.update_one({'_id': ObjectId(appointment_id)}, {'$set': data})

    def reschedule_appointment(self, appointment_id: str, date: str) -> None:
        if not self.get_appointment_by_id(appointment_id):
            raise AppointmentNotFoundException(appointment_id)
        self.collection.update_one({'_id': ObjectId(appointment_id)}, {'$set': {'date': date}})

    def cancel_appointment(self, appointment_id: str) -> None:
        if not self.get_appointment_by_id(appointment_id):
            raise AppointmentNotFoundException(appointment_id)
        self.collection.delete_one({'_id': ObjectId(appointment_id)})

    def update_patient_notes(self, appointment_id: str, notes: str) -> None:
        if not self.get_appointment_by_id(appointment_id):
            raise AppointmentNotFoundException(appointment_id)
        self.collection.update_one({'_id': ObjectId(appointment_id)}, {'$set': {'patient_notes': notes}})

    def update_doctor_notes(self, appointment_id: str, notes: str) -> None:
        if not self.get_appointment_by_id(appointment_id):
            raise AppointmentNotFoundException(appointment_id)
        self.collection.update_one({'_id': ObjectId(appointment_id)}, {'$set': {'doctor_notes': notes}})


    def get_by_date_range(self, start_date: datetime, end_date: datetime, doctor_id: Optional[str] = None, patient_id: Optional[str] = None) -> List[Appointment]:
        query = {
            'date_time': {
                '$gte': start_date,
                '$lte': end_date
            }
        }

        if doctor_id:
            query['doctor_id'] = doctor_id

        if patient_id:
            query['patient_id'] = patient_id

        appointments_data = self.collection.find(query)

        return [
            Appointment(
                appointment_id=str(app['_id']),
                patient_id=app['patient_id'],
                doctor_id=app['doctor_id'],
                date_time=app['date_time'],
                status=app['status'],
                notes=app.get('notes', '')
            )
            for app in appointments_data
        ]