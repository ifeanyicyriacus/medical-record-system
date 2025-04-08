from app.repositories.user_repository import UserRepository
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
from app.exceptions.custom_exception import DoctorNotFoundException, ValidationError, DatabaseError, EmailAlreadyExistsException
from app.models.user import User

load_dotenv()

class DoctorRepository(UserRepository):
    def __init__(self):
        super().__init__()
        self.collection = self.db[os.getenv('DOCTORS_COLLECTION')]

    def create_doctor(self, data):
        return self.create_user(data)

    def get_doctor_by_id(self, doctor_id):
        doctor = self.get_user_by_id(doctor_id)
        if not doctor:
            raise DoctorNotFoundException(doctor_id)
        return doctor

    def get_all_doctors(self):
        try:
            return self.get_users_by_role('doctor')
        except Exception as e:
            raise DatabaseError(f"Error fetching doctors: {str(e)}")

    def get_scheduled_appointments(self, doctor_id):
        if not self.get_doctor_by_id(doctor_id):
            raise DoctorNotFoundException(doctor_id)
        appointments_collection = self.db[os.getenv('APPOINTMENTS_COLLECTION')]
        try:
            return list(appointments_collection.find({'doctor_id': doctor_id}))
        except Exception as e:
            raise DatabaseError(f"Error fetching scheduled appointments for doctor {doctor_id}: {str(e)}")

    def get_patient_medical_history(self, doctor_id, patient_id):
        if not self.get_doctor_by_id(doctor_id):
            raise DoctorNotFoundException(doctor_id)
        appointments_collection = self.db[os.getenv('APPOINTMENTS_COLLECTION')]
        try:
            return list(appointments_collection.find({'doctor_id': doctor_id, 'patient_id': patient_id}))
        except Exception as e:
            raise DatabaseError(f"Error fetching medical history for patient {patient_id} by doctor {doctor_id}: {str(e)}")

    def update_doctor_profile(self, doctor_id, profile_data):
        if not profile_data:
            raise ValidationError("Profile data cannot be empty")
        if not self.get_doctor_by_id(doctor_id):
            raise DoctorNotFoundException(doctor_id)
        self.collection.update_one({'_id': ObjectId(doctor_id)}, {'$set': profile_data})