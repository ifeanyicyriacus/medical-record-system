from mongoengine import Document, StringField, DateTimeField, ReferenceField, EnumField
from .appointment_status import AppointmentStatus

class Appointment(Document):
    meta = {'collection': 'appointments'}
    
    appointment_id = StringField(required=True, unique=True)
    date = DateTimeField(required=True)
    patient = ReferenceField('Patient', required=True)
    doctor = ReferenceField('Doctor', required=True)
    appointment_status = EnumField(AppointmentStatus, default=AppointmentStatus.SCHEDULED)
    student_notes = StringField()
    doctor_notes = StringField()
