from user_repository import UserRepository
from models.patient import Patient
from exceptions.custom_exceptions import PatientNotFoundException

class PatientRepository(UserRepository):
    def __init__(self, db):
        super().__init__(db, 'patients')

    def add_patient(self, patient: Patient):
        self.create_user(patient)

    def get_patient(self, patient_id: str) -> Patient:
        try:
            return self.get_user_by_id(patient_id)
        except MedicalRecordSystemException:
            raise PatientNotFoundException(patient_id)

    def update_patient(self, patient_id: str, update_data: dict):
        self.update_user(patient_id, update_data)

    def delete_patient(self, patient_id: str):
        self.delete_user(patient_id)

    def search_patients(self, name: str):
        data = self.collection.find({"name": {"$regex": name, "$options": "i"}})
        return [Patient(**item) for item in data]