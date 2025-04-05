from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.patient import Patient

class IPatientRepository(ABC):
    @abstractmethod
    def create_appointment(self, appointment_id: str, appointment: dict) -> bool:
        pass
    
    @abstractmethod
    def reschedule_appointment(self, appointment_id: str, date: str) -> bool:
        pass
    
    @abstractmethod
    def view_appointments(self) -> List[dict]:
        pass
