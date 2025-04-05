from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from app.models.appointment import Appointment

class IAppointmentRepository(ABC):
    @abstractmethod
    def schedule_appointment(self, appointment: Appointment) -> bool:
        pass
    
    @abstractmethod
    def update_appointment(self, appointment_id: str) -> bool:
        pass
    
    @abstractmethod
    def get_details(self, appointment_id: str) -> dict:
        pass
    
    @abstractmethod
    def view_appointments(self) -> List[dict]:
        pass
    
    @abstractmethod
    def find_by_date_range(self, start_date: datetime, end_date: datetime) -> List[Appointment]:
        pass
