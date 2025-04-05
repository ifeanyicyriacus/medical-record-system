from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from app.models.appointment import Appointment

class IAppointmentService(ABC):
    @abstractmethod
    def schedule_appointment(self, doctor_id: str, patient_id: str, date: datetime) -> Optional[Appointment]:
    
        pass
    
    @abstractmethod
    def reschedule_appointment(self, appointment_id: str, new_date: datetime) -> bool:
        """Reschedule an existing appointment"""
        pass
    
    @abstractmethod
    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an appointment"""
        pass
    
    @abstractmethod
    def get_appointment_details(self, appointment_id: str) -> Optional[dict]:
        """Get details of a specific appointment"""
        pass
    
    @abstractmethod
    def find_available_slots(self, doctor_id: str, date: datetime) -> List[datetime]:
        """Find available appointment slots for a doctor on a specific date"""
        pass
