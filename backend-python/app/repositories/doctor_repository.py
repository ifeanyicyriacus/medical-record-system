from typing import List, Optional
from werkzeug.security import generate_password_hash
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.models.appointment_status import AppointmentStatus
from app.models.specialization import Specialization
from .interfaces.doctor_repository import IDoctorRepository

class DoctorRepository(IDoctorRepository):
    def view_appointments(self) -> List[dict]:
        try:
            appointments = Appointment.objects.all()
            return [{
                "id": str(appointment.id),
                "date": appointment.date,
                "patient": str(appointment.patient.id),
                "status": appointment.appointment_status.value,
                "notes": appointment.doctor_notes
            } for appointment in appointments]
        except Exception as e:
            return []
    
    def update_appointment_notes(self, appointment_id: str, notes: str) -> bool:
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            appointment.doctor_notes = notes
            appointment.save()
            return True
        except Exception as e:
            return False
    
    def update_appointment_status(self, appointment_id: str, status: str) -> bool:
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            appointment.appointment_status = AppointmentStatus[status]
            appointment.save()
            return True
        except Exception as e:
            return False
    
    def find_by_email(self, email: str) -> Optional[Doctor]:
        try:
            return Doctor.objects.get(email_address=email)
        except Exception as e:
            return None
    
    def find_by_specialization(self, specialization: Specialization) -> List[Doctor]:
        try:
            return Doctor.objects(specialization=specialization)
        except Exception as e:
            return []
    
    def update_profile(self, doctor_id: str, data: dict) -> bool:
        try:
            doctor = Doctor.objects.get(doctor_id=doctor_id)
            for key, value in data.items():
                if hasattr(doctor, key):
                    setattr(doctor, key, value)
            doctor.save()
            return True
        except Exception as e:
            return False
    
    def change_password(self, doctor_id: str, new_password: str) -> bool:
        try:
            doctor = Doctor.objects.get(doctor_id=doctor_id)
            doctor.hash_password = generate_password_hash(new_password)
            doctor.save()
            return True
        except Exception as e:
            return False
