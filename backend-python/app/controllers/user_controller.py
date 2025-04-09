from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.exceptions.custom_exception import (
    EmailAlreadyExistsException,
    IncorrectLoginCredentialsException,
    MedicalRecordSystemException,
    PatientNotFoundException
)
from app.repositories.user_repository import UserRepository

user_bp = Blueprint("user", __name__)
user_repository = UserRepository()
user_service = UserService(user_repository)

@user_bp.route('/register', methods=['POST'])
@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    try:
        user = user_service.register_user(data)

        user['_id'] = str(user['_id'])

        return jsonify(user), 201
    except EmailAlreadyExistsException as e:
        return jsonify({"error": str(e)}), 400
    except MedicalRecordSystemException as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    try:
        user = user_service.login_user(email, password)
        if not user:
            raise IncorrectLoginCredentialsException()
        return jsonify(user), 200
    except IncorrectLoginCredentialsException:
        return jsonify({"error": "Invalid email or password"}), 401

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_service.get_user_by_id(user_id)
        return jsonify(user), 200
    except PatientNotFoundException as e:
        return jsonify({"error": str(e)}), 404

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    try:
        user_service.update_user(user_id, data)
        return jsonify({"message": "User updated successfully"}), 200
    except MedicalRecordSystemException as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return jsonify({"message": "User deleted successfully"}), 200
    except MedicalRecordSystemException as e:
        return jsonify({"error": str(e)}), 500