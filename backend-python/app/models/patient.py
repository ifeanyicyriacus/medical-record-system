from mongoengine import ReferenceField, ListField, EmbeddedDocumentField
from app.models.user import User
from app.models.user_type import UserType

class Patient(User):
    meta = {
        'collection': 'patients'
    }
    
    appointments = ListField(ReferenceField('Appointment'))
    medical_record = EmbeddedDocumentField('MedicalRecord')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = UserType.PATIENT
