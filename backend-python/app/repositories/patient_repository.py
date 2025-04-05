from datetime import datetime
from typing import List
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
            appointment.date = datetime.fromisoformat(date)
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
                "notes": appointment.student_notes
            } for appointment in appointments]
        except Exception as e:
            return []
