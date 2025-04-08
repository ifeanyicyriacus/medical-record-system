from dataclasses import dataclass, field
from typing import List
from app.models.user import User
from app.models.enums import Specialization


@dataclass
class Doctor(User):
    doctor_id: int
    specialization: Specialization
    medical_license: str
    appointments: List[int] = field(default_factory=list)

    def __init__(self, first_name, last_name, hash_password, phone_number, email_address, dob, gender, role, doctor_id, specialization, medical_license, appointments=None):
        super().__init__(first_name, last_name, hash_password, phone_number, email_address, dob, gender, role)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.medical_license = medical_license
        self.appointments = appointments or []