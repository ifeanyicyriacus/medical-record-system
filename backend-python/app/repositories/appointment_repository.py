from models.appointment import Appointment
from bson.objectid import ObjectId
from exceptions.custom_exceptions import AppointmentNotFoundException

class AppointmentRepository:
    def __init__(self, db):
        self.db = db

    def add_appointment(self, appointment: Appointment):
        self.db.appointments.insert_one(appointment.__dict__)

    def get_appointment(self, appointment_id: str):
        data = self.db.appointments.find_one({"_id": ObjectId(appointment_id)})
        if not data:
            raise AppointmentNotFoundException(appointment_id)
        return Appointment(**data)

    def get_appointments_by_doctor(self, doctor_id: str):
        data = self.db.appointments.find({"doctor_id": doctor_id})
        return [Appointment(**item) for item in data]

    def get_appointments_by_patient(self, patient_id: str):
        data = self.db.appointments.find({"patient_id": patient_id})
        return [Appointment(**item) for item in data]