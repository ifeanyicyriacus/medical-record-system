from dataclasses import dataclass
from datetime import datetime
from app.models.enums import AppointmentStatus

@dataclass
class Appointment:
    appointment_id: int
    date: datetime
    patient_id: int
    doctor_id: int
    appointment_status: AppointmentStatus
    patient_notes: str = ""
    doctor_notes: str = ""