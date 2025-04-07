from repositories.user_repository import UserRepository
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
from exceptions import PatientNotFoundException, ValidationError, DatabaseError, EmailAlreadyExistsException
from models.user import User

load_dotenv()

class PatientRepository(UserRepository):
    def __init__(self):
        super().__init__()
        self.collection = self.db[os.getenv('PATIENTS_COLLECTION')]

    def create_patient(self, data):
        return self.create_user(data)

    def get_patient_by_id(self, patient_id):
        patient = self.get_user_by_id(patient_id)
        if not patient:
            raise PatientNotFoundException(patient_id)
        return patient

    def get_all_patients(self):
        try:
            return self.get_users_by_role('patient')
        except Exception as e:
            raise DatabaseError(f"Error fetching patients: {str(e)}")

    def update_patient_profile(self, patient_id, profile_data):
        if not profile_data:
            raise ValidationError("Profile data cannot be empty")
        if not self.get_patient_by_id(patient_id):
            raise PatientNotFoundException(patient_id)
        self.collection.update_one({'_id': ObjectId(patient_id)}, {'$set': profile_data})

    def get_patient_medical_history(self, patient_id):
        if not self.get_patient_by_id(patient_id):
            raise PatientNotFoundException(patient_id)

        appointments_collection = self.db[os.getenv('APPOINTMENTS_COLLECTION')]
        try:
            return list(appointments_collection.find({'patient_id': patient_id}))
        except Exception as e:
            raise DatabaseError(f"Error fetching medical history for patient {patient_id}: {str(e)}")