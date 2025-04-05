from typing import List, Optional
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.doctor import Doctor
from app.models.specialization import Specialization
from app.repositories.doctor_repository import DoctorRepository
from .interfaces.doctor_service import IDoctorService

class DoctorService(IDoctorService):
    def __init__(self, doctor_repository: DoctorRepository):
        self.doctor_repository = doctor_repository
    
    def register(self, doctor_data: dict) -> Optional[Doctor]:
        try:
            # Hash the password
            doctor_data['hash_password'] = generate_password_hash(doctor_data.pop('password'))
            
            # Create and save doctor
            doctor = Doctor(**doctor_data)
            doctor.save()
            return doctor
        except Exception as e:
            return None
    
    def login(self, email: str, password: str) -> Optional[dict]:
        try:
            doctor = Doctor.objects.get(email_address=email)
            if check_password_hash(doctor.hash_password, password):
                return {
                    "id": str(doctor.id),
                    "doctor_id": doctor.doctor_id,
                    "name": f"{doctor.first_name} {doctor.last_name}",
                    "email": doctor.email_address,
                    "specialization": doctor.specialization.value
                }
            return None
        except Exception as e:
            return None
    
    def view_appointments(self, doctor_id: str) -> List[dict]:
        return self.doctor_repository.view_appointments()
    
    def update_appointment_status(self, doctor_id: str, appointment_id: str, status: str) -> bool:
        return self.doctor_repository.update_appointment_status(appointment_id, status)
    
    def add_appointment_notes(self, doctor_id: str, appointment_id: str, notes: str) -> bool:
        return self.doctor_repository.update_appointment_notes(appointment_id, notes)
    
    def find_by_specialization(self, specialization: Specialization) -> List[Doctor]:
        return Doctor.objects(specialization=specialization)
