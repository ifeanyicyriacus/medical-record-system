from typing import List
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.models.appointment_status import AppointmentStatus
from .interfaces.doctor_repository import IDoctorRepository

class DoctorRepository(IDoctorRepository):
    def view_appointments(self, doctor_id: str) -> List[dict]:
        try:
            doctor = Doctor.objects.get(doctor_id=doctor_id)
            appointments = Appointment.objects(doctor=doctor)
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
