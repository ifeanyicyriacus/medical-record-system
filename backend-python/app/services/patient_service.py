from typing import List, Optional
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.repositories.patient_repository import PatientRepository
from .interfaces.patient_service import IPatientService

class PatientService(IPatientService):
    def __init__(self, patient_repository: PatientRepository):
        self.patient_repository = patient_repository
    
    def register(self, patient_data: dict) -> Optional[Patient]:
        try:
            # Hash the password
            patient_data['hash_password'] = generate_password_hash(patient_data.pop('password'))
            
            # Create and save patient
            patient = Patient(**patient_data)
            patient.save()
            return patient
        except Exception as e:
            return None
    
    def login(self, email: str, password: str) -> Optional[dict]:
        try:
            patient = Patient.objects.get(email_address=email)
            if check_password_hash(patient.hash_password, password):
                return {
                    "id": str(patient.id),
                    "patient_id": patient.patient_id,
                    "name": f"{patient.first_name} {patient.last_name}",
                    "email": patient.email_address
                }
            return None
        except Exception as e:
            return None
    
    def create_appointment(self, patient_id: str, doctor_id: str, date: datetime) -> bool:
        appointment_data = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date
        }
        return self.patient_repository.create_appointment(patient_id, appointment_data)
    
    def reschedule_appointment(self, patient_id: str, appointment_id: str, new_date: datetime) -> bool:
        return self.patient_repository.reschedule_appointment(appointment_id, new_date.isoformat())
    
    def view_appointments(self, patient_id: str) -> List[dict]:
        return self.patient_repository.view_appointments()
