import os
from datetime import timedelta

class Config:
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    
    # MongoDB
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/mrs',
        'db': os.environ.get('MONGODB_DB') or 'mrs'
    }
    
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # App Settings
    APPOINTMENT_SLOT_DURATION = timedelta(minutes=30)
    CLINIC_OPENING_HOUR = 9  # 9 AM
    CLINIC_CLOSING_HOUR = 17  # 5 PM
