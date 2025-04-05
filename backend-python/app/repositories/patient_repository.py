from typing import List, Optional
from werkzeug.security import generate_password_hash
from app.models.patient import Patient
from app.models.appointment import Appointment
from .interfaces.patient_repository import IPatientRepository

class PatientRepository(IPatientRepository):
    def create_appointment(self, appointment_id: str, appointment: dict) -> bool:
        try:
            patient = Patient.objects.get(patient_id=appointment_id)
            new_appointment = Appointment(**appointment).save()
            patient.appointments.append(new_appointment)
            patient.save()
            return True
        except Exception as e:
            return False
    
    def reschedule_appointment(self, appointment_id: str, date: str) -> bool:
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            appointment.date = date
            appointment.save()
            return True
        except Exception as e:
            return False
    
    def view_appointments(self) -> List[dict]:
        try:
            appointments = Appointment.objects.all()
            return [{
                "id": str(appointment.id),
                "date": appointment.date,
                "doctor": str(appointment.doctor.id),
                "status": appointment.appointment_status.value,
                "notes": appointment.patient_notes
            } for appointment in appointments]
        except Exception as e:
            return []
    
    def find_by_email(self, email: str) -> Optional[Patient]:
        try:
            return Patient.objects.get(email_address=email)
        except Exception as e:
            return None
    
    def update_profile(self, patient_id: str, data: dict) -> bool:
        try:
            patient = Patient.objects.get(patient_id=patient_id)
            for key, value in data.items():
                if hasattr(patient, key):
                    setattr(patient, key, value)
            patient.save()
            return True
        except Exception as e:
            return False
    
    def change_password(self, patient_id: str, new_password: str) -> bool:
        try:
            patient = Patient.objects.get(patient_id=patient_id)
            patient.hash_password = generate_password_hash(new_password)
            patient.save()
            return True
        except Exception as e:
            return False
