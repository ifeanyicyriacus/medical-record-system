from mongoengine import Document, DateTimeField, ReferenceField
from datetime import datetime

class Appointment(Document):
    meta = {
        'collection': 'appointments'
    }
    
    date = DateTimeField(required=True)
    doctor = ReferenceField('Doctor', required=True)
    patient = ReferenceField('Patient', required=True)
    
    def __str__(self):
        return f"Appointment on {self.date} with Dr. {self.doctor.last_name}"
