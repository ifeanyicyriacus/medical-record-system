from typing import List
from datetime import datetime
from app.models.appointment import Appointment
from .interfaces.appointment_repository import IAppointmentRepository

class AppointmentRepository(IAppointmentRepository):
    def schedule_appointment(self, appointment: Appointment) -> bool:
        try:
            appointment.save()
            return True
        except Exception as e:
            return False
    
    def update_appointment(self, appointment_id: str) -> bool:
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            appointment.save()
            return True
        except Exception as e:
            return False
    
    def get_details(self, appointment_id: str) -> dict:
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            return {
                "id": str(appointment.id),
                "date": appointment.date,
                "doctor": str(appointment.doctor.id),
                "patient": str(appointment.patient.id),
                "status": appointment.appointment_status.value
            }
        except Exception as e:
            return {}
    
    def view_appointments(self) -> List[dict]:
        try:
            appointments = Appointment.objects.all()
            return [{
                "id": str(appointment.id),
                "date": appointment.date,
                "doctor": str(appointment.doctor.id),
                "patient": str(appointment.patient.id),
                "status": appointment.appointment_status.value
            } for appointment in appointments]
        except Exception as e:
            return []
    
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Appointment]:
        try:
            return Appointment.objects(date__gte=start_date, date__lte=end_date)
        except Exception as e:
            return []
