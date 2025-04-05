from mongoengine import Document, StringField, DateTimeField, EnumField
from .gender import Gender

class User(Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }
    
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    hash_password = StringField(required=True)
    phone_number = StringField()
    email_address = StringField(required=True, unique=True)
    dob = DateTimeField()
    gender = EnumField(Gender)
