from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    OTHERS = "others"

class Specialization(Enum):
    GENERAL_PRACTICE = "general_practice"
    PEDIATRICS = "pediatrics"
    CARDIOLOGY = "cardiology"
    ONCOLOGY = "oncology"
    NEUROLOGY = "neurology"
    OTHERS = "others"

class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    RESCHEDULED = "rescheduled"

class UserRole(Enum):
    ADMIN = "admin"
    PATIENT = "patient"
    DOCTOR = "doctor"