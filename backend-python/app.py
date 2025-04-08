from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)
CORS(app, origins=["http://localhost:63342"], supports_credentials=True)


client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('DB_NAME')]

# Register blueprints
from app.controllers.patient_controller import patient_bp
from app.controllers.doctor_controller import doctor_bp
from app.controllers.user_controller import user_bp

#from app.controllers.appointment_controller import appointment_bp
#from app.controllers.admin_controller import admin_bp

app.register_blueprint(patient_bp)
app.register_blueprint(doctor_bp)
#app.register_blueprint(appointment_bp)
#app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp)


print(app.url_map)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Medical Record System API"}), 200

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST'),
        port=int(os.getenv('FLASK_PORT')),
        debug=os.getenv('FLASK_DEBUG') == 'True'
    )