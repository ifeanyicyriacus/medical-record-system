from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, EnumField
from app.models.gender import Gender
from app.models.user_type import UserType

class User(Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }
    
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    phone = StringField()
    date_of_birth = DateTimeField()
    gender = EnumField(Gender)
    type = EnumField(UserType, required=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
