from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.doctor import Doctor
from app.models.specialization import Specialization

class IDoctorService(ABC):
    @abstractmethod
    def register(self, doctor_data: dict) -> Optional[Doctor]:
        """Register a new doctor"""
        pass
    
    @abstractmethod
    def login(self, email: str, password: str) -> Optional[dict]:
        """Login a doctor"""
        pass
    
    @abstractmethod
    def view_appointments(self, doctor_id: str) -> List[dict]:
        """View all appointments for a doctor"""
        pass
    
    @abstractmethod
    def update_appointment_status(self, doctor_id: str, appointment_id: str, status: str) -> bool:
        """Update the status of an appointment"""
        pass
    
    @abstractmethod
    def add_appointment_notes(self, doctor_id: str, appointment_id: str, notes: str) -> bool:
        """Add notes to an appointment"""
        pass
    
    @abstractmethod
    def find_by_specialization(self, specialization: Specialization) -> List[Doctor]:
        """Find doctors by specialization"""
        pass
