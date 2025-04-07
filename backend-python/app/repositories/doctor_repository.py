from repositories.user_repository import UserRepository
from models.doctor import Doctor
from exceptions.custom_exceptions import DoctorNotFoundException

class DoctorRepository(UserRepository):
    def __init__(self, db):
        super().__init__(db, 'doctors')

    def add_doctor(self, doctor: Doctor):
        self.create_user(doctor)

    def get_doctor(self, doctor_id: str) -> Doctor:
        try:
            return self.get_user_by_id(doctor_id)
        except MedicalRecordSystemException:
            raise DoctorNotFoundException(doctor_id)

    def update_doctor(self, doctor_id: str, update_data: dict):
        self.update_user(doctor_id, update_data)

    def delete_doctor(self, doctor_id: str):
        self.delete_user(doctor_id)

    def search_doctors(self, name: str):
        data = self.collection.find({"name": {"$regex": name, "$options": "i"}})
        return [Doctor(**item) for item in data]