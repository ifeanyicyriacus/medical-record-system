from typing import List, Optional
from datetime import datetime
from app.models.patient import Patient
from app.models.appointment import Appointment
from models.user import User
from repositories.appointment_repository import AppointmentRepository
from repositories.patient_repository import PatientRepository
from repositories.user_repository import UserRepository
from user_service import UserService


class PatientService(UserService):
    def __init__(self, user_repository: UserRepository, appointment_repository: AppointmentRepository):
        super().__init__(user_repository)
        self.appointment_repository = appointment_repository

    def create_patient(self, data: dict) -> dict:
        return self.create_user(data)

    def update_patient(self, patient: User) -> None:
        self.update_user(patient)

    def delete_patient(self, patient_id: str) -> None:
        self.delete_user(patient_id)

    def get_patient_history(self, patient_id: str) -> dict:

        pass

    def book_appointment(self, appointment: Appointment) -> Appointment:
        return self.appointment_repository.create_appointment(appointment)

    def reschedule_appointment(self, appointment_id: str, date: str) -> None:
        self.appointment_repository.reschedule_appointment(appointment_id, date)

    def view_appointments(self, patient_id: str) -> List[Appointment]:
        return self.appointment_repository.get_appointments_by_patient(patient_id)

    def update_student_notes(self, appointment_id: str, notes: str) -> None:
        self.appointment_repository.update_patient_notes(appointment_id, notes)


    def get_appointments_report(self, start_date: datetime, end_date: datetime) -> Dict:
        appointments = self.appointment_repository.get_by_date_range(start_date, end_date)
        return {
            'total_appointments': len(appointments),
            'scheduled': len([a for a in appointments if a.status == 'scheduled']),
            'completed': len([a for a in appointments if a.status == 'completed']),
            'cancelled': len([a for a in appointments if a.status == 'cancelled']),
            'appointments': appointments
        }