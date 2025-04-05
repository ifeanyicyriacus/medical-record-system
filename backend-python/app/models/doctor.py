from mongoengine import ReferenceField, ListField, EnumField
from .user import User
from .specialization import Specialization
from .appointment import Appointment

class Doctor(User):
    meta = {'collection': 'doctors'}
    
    doctor_id = StringField(required=True, unique=True)
    specialization = EnumField(Specialization, required=True)
    appointments = ListField(ReferenceField(Appointment))
