from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.doctor import Doctor
from app.models.specialization import Specialization

class IDoctorRepository(ABC):
    @abstractmethod
    def view_appointments(self) -> List[dict]:
        pass
    
    @abstractmethod
    def update_appointment_notes(self, appointment_id: str, patient: str) -> bool:
        pass
    
    @abstractmethod
    def update_appointment_status(self, appointment_id: str, patient: str, status: str) -> bool:
        pass
