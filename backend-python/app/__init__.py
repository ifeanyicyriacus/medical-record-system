from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

db = MongoEngine()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # Configure CORS
    CORS(app, 
         resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}},
         headers=app.config['CORS_HEADERS'],
         supports_credentials=app.config['CORS_SUPPORTS_CREDENTIALS'])
    
    # Register blueprints
    from .routes import patient_bp, doctor_bp, appointment_bp
    app.register_blueprint(patient_bp, url_prefix='/api/patients')
    app.register_blueprint(doctor_bp, url_prefix='/api/doctors')
    app.register_blueprint(appointment_bp, url_prefix='/api/appointments')
    
    # Initialize app specific configurations
    config_class.init_app(app)
    
    return app