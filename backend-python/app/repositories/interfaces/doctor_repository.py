from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.doctor import Doctor
from app.models.specialization import Specialization

class IDoctorRepository(ABC):
    @abstractmethod
    def view_appointments(self) -> List[dict]:
        pass
    
    @abstractmethod
    def update_appointment_notes(self, appointment_id: str, notes: str) -> bool:
        pass
    
    @abstractmethod
    def update_appointment_status(self, appointment_id: str, status: str) -> bool:
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Doctor]:
        pass
    
    @abstractmethod
    def find_by_specialization(self, specialization: Specialization) -> List[Doctor]:
        pass
    
    @abstractmethod
    def update_profile(self, doctor_id: str, data: dict) -> bool:
        pass
    
    @abstractmethod
    def change_password(self, doctor_id: str, new_password: str) -> bool:
        pass
