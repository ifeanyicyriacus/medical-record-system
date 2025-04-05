from datetime import datetime
from unittest.mock import Mock, patch
from tests.base_test import BaseTest
from app.models.doctor import Doctor
from app.models.gender import Gender
from app.models.specialization import Specialization
from app.services.doctor_service import DoctorService
from werkzeug.security import check_password_hash

class TestDoctorService(BaseTest):
    def setUp(self):
        super().setUp()
        self.doctor_repository = Mock()
        self.service = DoctorService(self.doctor_repository)
        
        self.test_doctor_data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email_address": "jane@example.com",
            "phone_number": "1234567890",
            "date_of_birth": datetime(1985, 1, 1),
            "gender": Gender.FEMALE,
            "doctor_id": "D123",
            "specialization": Specialization.GENERAL_PRACTICE,
            "password": "test_password"
        }
    
    def test_register(self):
        result = self.service.register(self.test_doctor_data)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.first_name, "Jane")
        self.assertEqual(result.email_address, "jane@example.com")
        self.assertTrue(check_password_hash(result.hash_password, "test_password"))
    
    def test_login_success(self):
        # Create a doctor with known password
        doctor = Doctor(
            **{k: v for k, v in self.test_doctor_data.items() if k != "password"}
        )
        doctor.hash_password = self.service._hash_password("test_password")
        doctor.save()
        
        self.doctor_repository.find_by_email.return_value = doctor
        
        result = self.service.login("jane@example.com", "test_password")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["email"], "jane@example.com")
        self.assertEqual(result["name"], "Jane Smith")
        self.assertEqual(result["specialization"], Specialization.GENERAL_PRACTICE.value)
    
    def test_login_failure(self):
        self.doctor_repository.find_by_email.return_value = None
        
        result = self.service.login("wrong@example.com", "wrong_password")
        
        self.assertIsNone(result)
    
    def test_update_appointment_status(self):
        self.doctor_repository.update_appointment_status.return_value = True
        
        result = self.service.update_appointment_status(
            "D123",
            "A123",
            "COMPLETED"
        )
        
        self.assertTrue(result)
        self.doctor_repository.update_appointment_status.assert_called_once()
    
    def test_add_appointment_notes(self):
        self.doctor_repository.update_appointment_notes.return_value = True
        
        result = self.service.add_appointment_notes(
            "D123",
            "A123",
            "Test notes"
        )
        
        self.assertTrue(result)
        self.doctor_repository.update_appointment_notes.assert_called_once()
    
    def test_find_by_specialization(self):
        test_doctor = Doctor(**{k: v for k, v in self.test_doctor_data.items() if k != "password"})
        self.doctor_repository.find_by_specialization.return_value = [test_doctor]
        
        result = self.service.find_by_specialization(Specialization.GENERAL_PRACTICE)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].doctor_id, "D123")
        self.doctor_repository.find_by_specialization.assert_called_once_with(Specialization.GENERAL_PRACTICE)
