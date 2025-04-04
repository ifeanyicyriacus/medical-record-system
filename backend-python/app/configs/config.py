import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # MongoDB Configuration
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB', 'medical_records'),
        'host': os.getenv('MONGODB_HOST', 'localhost'),
        'port': int(os.getenv('MONGODB_PORT', 27017)),
        'username': os.getenv('MONGODB_USERNAME'),
        'password': os.getenv('MONGODB_PASSWORD')
    }
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    
    # CORS Configuration
    CORS_HEADERS = ['Content-Type', 'Authorization']
    CORS_ORIGINS = "*"  # Allow all origins
    CORS_SUPPORTS_CREDENTIALS = True  # Allow credentials
    
    @staticmethod
    def init_app(app):
        pass
