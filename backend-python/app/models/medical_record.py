from mongoengine import EmbeddedDocument, StringField, ListField, DateTimeField
from datetime import datetime

class MedicalRecord(EmbeddedDocument):
    meta = {
        'collection': 'medical_records'
    }
    
    conditions = ListField(StringField())
    allergies = ListField(StringField())
    medications = ListField(StringField())
    notes = ListField(StringField())
    last_updated = DateTimeField(default=datetime.utcnow)
