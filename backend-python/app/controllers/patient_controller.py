from flask import Blueprint, request, jsonify
from models.patient import Patient
from models.appointment import Appointment
from bson import ObjectId

patient_bp = Blueprint('patient', __name__, url_prefix='/patients')

@patient_bp.route('/appointments', methods=['GET'])
def view_appointments():
    patient_id = request.args.get('patient_id')
    appointments = appointments_collection.find({"patient_id": ObjectId(patient_id)})
    return jsonify([appointment for appointment in appointments]), 200

@patient_bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointments_collection.insert_one(data)
    return jsonify({"message": "Appointment created successfully"}), 201

@patient_bp.route('/appointments/<appointment_id>', methods=['PUT'])
def reschedule_appointment(appointment_id):
    data = request.get_json()
    appointments_collection.update_one({"_id": ObjectId(appointment_id)}, {"$set": data})
    return jsonify({"message": "Appointment rescheduled successfully"}), 200