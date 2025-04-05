from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from app.models.patient import Patient

class IPatientService(ABC):
    @abstractmethod
    def register(self, patient_data: dict) -> Optional[Patient]:
        """Register a new patient"""
        pass
    
    @abstractmethod
    def login(self, email: str, password: str) -> Optional[dict]:
        """Login a patient"""
        pass
    
    @abstractmethod
    def create_appointment(self, patient_id: str, doctor_id: str, date: datetime) -> bool:
        """Create an appointment for a patient"""
        pass
    
    @abstractmethod
    def reschedule_appointment(self, patient_id: str, appointment_id: str, new_date: datetime) -> bool:
        """Reschedule an existing appointment"""
        pass
    
    @abstractmethod
    def view_appointments(self, patient_id: str) -> List[dict]:
        """View all appointments for a patient"""
        pass
