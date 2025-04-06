from dataclasses import dataclass, field
from typing import List
from .user import User

@dataclass
class Patient(User):
    patient_id: int
    appointments: List[int] = field(default_factory=list)