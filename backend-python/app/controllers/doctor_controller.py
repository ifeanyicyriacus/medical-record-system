from flask import Blueprint, request, jsonify
from app.models.doctor import Doctor
from app.repositories.appointment_repository import AppointmentRepository
from bson import ObjectId

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctors')

@doctor_bp.route('/appointments', methods=['GET'])
def view_appointments():
    doctor_id = request.args.get('doctor_id')
    appointments = AppointmentRepository.get_appointments_by_doctor({"doctor_id": ObjectId(doctor_id)})
    return jsonify([appointment for appointment in appointments]), 200

@doctor_bp.route('/appointments/<appointment_id>', methods=['PUT'])
def reschedule_appointment(appointment_id):
    data = request.get_json()
    AppointmentRepository.get_appointment_by_id({"_id": ObjectId(appointment_id)}, {"$set": data})
    return jsonify({"message": "Appointment rescheduled successfully"}), 200

@doctor_bp.route('/appointments/<appointment_id>/note', methods=['PUT'])
def edit_appointment_note(appointment_id):
    note = request.get_json().get('note')
    AppointmentRepository.get_appointment_by_id({"_id": ObjectId(appointment_id)}, {"$set": {"note": note}})
    return jsonify({"message": "Appointment note updated successfully"}), 200