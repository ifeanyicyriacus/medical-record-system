from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)
CORS(app)


client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('DB_NAME')]

# Register blueprints
from app.controllers.patient_controller import patient_bp
from app.controllers.doctor_controller import doctor_bp
#from app.controllers.appointment_controller import appointment_bp
#from app.controllers.admin_controller import admin_bp

app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST'),
        port=int(os.getenv('FLASK_PORT')),
        debug=os.getenv('FLASK_DEBUG') == 'True'
    )