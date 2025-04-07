from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from controllers.patient_controller import patient_bp
from controllers.doctor_controller import doctor_bp
from controllers.appointment_controller import appointment_bp
from controllers.admin_controller import admin_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)


mongo_uri = os.getenv('MONGO_URI')
secret_key = os.getenv('SECRET_KEY')

if not mongo_uri or not secret_key:
    raise ValueError("Please set the MONGO_URI and SECRET_KEY environment variables")

client = MongoClient(mongo_uri)
db = client.get_database()

app.config['SECRET_KEY'] = secret_key

app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)