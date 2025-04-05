from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient

class IAppointmentRepository(ABC):
    @abstractmethod
    def schedule_appointment(self, appointment: Appointment) -> bool:
        pass
    
    @abstractmethod
    def update_appointment(self, appointment_id: str) -> bool:
        pass
    
    @abstractmethod
    def get_details(self) -> dict:
        pass
    
    @abstractmethod
    def view_appointments(self) -> List[dict]:
        pass
