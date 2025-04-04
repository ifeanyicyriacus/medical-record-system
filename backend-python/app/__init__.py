from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.configs import Config

# Initialize extensions
db = MongoEngine()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions with app
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)
    
    # Register blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.patient_controller import patient_bp
    from app.controllers.doctor_controller import doctor_bp
    from app.controllers.appointment_controller import appointment_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(patient_bp, url_prefix='/api/patients')
    app.register_blueprint(doctor_bp, url_prefix='/api/doctors')
    app.register_blueprint(appointment_bp, url_prefix='/api/appointments')
    
    return app