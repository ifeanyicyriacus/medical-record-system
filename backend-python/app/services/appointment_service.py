from typing import List, Optional
from datetime import datetime, timedelta
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment_status import AppointmentStatus
from app.repositories.appointment_repository import AppointmentRepository
from .interfaces.appointment_service import IAppointmentService

class AppointmentService(IAppointmentService):
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository
    
    def schedule_appointment(self, doctor_id: str, patient_id: str, date: datetime) -> Optional[Appointment]:
        try:
            # Check if doctor and patient exist
            doctor = Doctor.objects.get(doctor_id=doctor_id)
            patient = Patient.objects.get(patient_id=patient_id)
            
            # Check if slot is available
            if not self._is_slot_available(doctor_id, date):
                return None
            
            # Create appointment
            appointment = Appointment(
                doctor=doctor,
                patient=patient,
                date=date,
                appointment_status=AppointmentStatus.SCHEDULED
            )
            
            if self.appointment_repository.schedule_appointment(appointment):
                return appointment
            return None
        except Exception as e:
            return None
    
    def reschedule_appointment(self, appointment_id: str, new_date: datetime) -> bool:
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            if not self._is_slot_available(appointment.doctor.doctor_id, new_date):
                return False
            
            appointment.date = new_date
            return self.appointment_repository.update_appointment(appointment_id)
        except Exception as e:
            return False
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        try:
            appointment = Appointment.objects.get(appointment_id=appointment_id)
            appointment.appointment_status = AppointmentStatus.CANCELLED
            return self.appointment_repository.update_appointment(appointment_id)
        except Exception as e:
            return False
    
    def get_appointment_details(self, appointment_id: str) -> Optional[dict]:
        return self.appointment_repository.get_details(appointment_id)
    
    def find_available_slots(self, doctor_id: str, date: datetime) -> List[datetime]:
        try:
            # Get all appointments for the doctor on that date
            start_of_day = date.replace(hour=9, minute=0)  # Clinic opens at 9 AM
            end_of_day = date.replace(hour=17, minute=0)   # Clinic closes at 5 PM
            
            booked_slots = set()
            appointments = Appointment.objects(
                doctor__doctor_id=doctor_id,
                date__gte=start_of_day,
                date__lt=end_of_day
            )
            
            for appointment in appointments:
                booked_slots.add(appointment.date)
            
            # Generate all possible slots (30-minute intervals)
            available_slots = []
            current_slot = start_of_day
            while current_slot < end_of_day:
                if current_slot not in booked_slots:
                    available_slots.append(current_slot)
                current_slot += timedelta(minutes=30)
            
            return available_slots
        except Exception as e:
            return []
    
    def _is_slot_available(self, doctor_id: str, date: datetime) -> bool:
        """Check if a time slot is available for booking"""
        try:
            existing_appointment = Appointment.objects(
                doctor__doctor_id=doctor_id,
                date=date,
                appointment_status__ne=AppointmentStatus.CANCELLED
            ).first()
            return existing_appointment is None
        except Exception as e:
            return False
