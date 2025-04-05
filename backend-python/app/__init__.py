from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from .config import Config

db = MongoEngine()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # Register blueprints
    from .routes import patient_bp, doctor_bp, appointment_bp
    app.register_blueprint(patient_bp, url_prefix='/api/patients')
    app.register_blueprint(doctor_bp, url_prefix='/api/doctors')
    app.register_blueprint(appointment_bp, url_prefix='/api/appointments')
    
    return app