from mongoengine import ReferenceField, ListField, EnumField
from app.models.user import User
from app.models.user_type import UserType
from app.models.specialization import Specialization

class Doctor(User):
    meta = {
        'collection': 'doctors'
    }
    
    specialization = EnumField(Specialization, required=True)
    appointments = ListField(ReferenceField('Appointment'))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = UserType.DOCTOR
