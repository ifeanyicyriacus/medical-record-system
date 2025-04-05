from mongoengine import Document, StringField, DateTimeField, ReferenceField
from datetime import datetime, timedelta

class Token(Document):
    meta = {'collection': 'tokens'}
    
    token = StringField(required=True, unique=True)
    user_id = StringField(required=True)
    expires_at = DateTimeField(required=True)
    refresh_token = StringField(required=True, unique=True)
    
    @classmethod
    def create_token(cls, user_id: str, token: str, refresh_token: str, expires_in: int = 3600):
        expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
        return cls(
            user_id=user_id,
            token=token,
            refresh_token=refresh_token,
            expires_at=expires_at
        ).save()
    
    def is_valid(self) -> bool:
        return datetime.utcnow() < self.expires_at
