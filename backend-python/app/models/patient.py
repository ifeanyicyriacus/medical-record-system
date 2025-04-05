from mongoengine import ReferenceField, ListField
from .user import User
from .appointment import Appointment

class Patient(User):
    meta = {'collection': 'patients'}
    
    patient_id = StringField(required=True, unique=True)
    appointments = ListField(ReferenceField(Appointment))
