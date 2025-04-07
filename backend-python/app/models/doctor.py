from dataclasses import dataclass, field
from typing import List
from user import User
from app.models.enums import Specialization

@dataclass
class Doctor(User):
    doctor_id: int
    specialization: Specialization
    medical_license: str
    appointments: List[int] = field(default_factory=list)