from dataclasses import dataclass
from datetime import datetime
from enums import AppointmentStatus

@dataclass
class Appointment:
    appointment_id: int
    date: datetime
    patient_id: int
    doctor_id: int
    appointment_status: AppointmentStatus
    student_notes: str = ""
    doctor_notes: str = ""