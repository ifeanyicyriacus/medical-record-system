from flask import Blueprint, request, jsonify
from app.models.doctor import Doctor
from app.repositories.appointment_repository import AppointmentRepository
from bson import ObjectId

from app.models.enums import UserRole
from app.repositories.doctor_repository import DoctorRepository

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctors')


@doctor_bp.route('/', methods=['GET'])
def get_all_doctors():
    return jsonify({"message": "Doctors API is working!"}), 200

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctors')
doctor_repo = DoctorRepository()


@doctor_bp.route('/register', methods=['POST'])
def create_doctor():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ["first_name", "last_name", "email_address", "phone_number", "specialization", "dob", "gender", "medical_license"]
        if any(field not in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Assign missing values
        data["role"] = UserRole.DOCTOR
        data["hash_password"] = ""

        # Create doctor object
        new_doctor = Doctor(
            first_name=data["first_name"],
            last_name=data["last_name"],
            hash_password=data["hash_password"],
            phone_number=data["phone_number"],
            email_address=data["email_address"],
            dob=data["dob"],
            gender=data["gender"],
            role=data["role"],
            doctor_id=data.get("doctor_id", ObjectId()),
            specialization=data["specialization"],
            medical_license=data["medical_license"],
            appointments=data.get("appointments", [])
        )

        # Save doctor to database
        inserted_doctor = doctor_repo.create_doctor(data)
        return jsonify({"message": "Doctor created successfully", "doctor": inserted_doctor}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500



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
