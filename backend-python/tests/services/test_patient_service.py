from datetime import datetime
from unittest.mock import Mock, patch
from tests.base_test import BaseTest
from app.models.patient import Patient
from app.models.gender import Gender
from app.services.patient_service import PatientService
from werkzeug.security import check_password_hash

class TestPatientService(BaseTest):
    def setUp(self):
        super().setUp()
        self.patient_repository = Mock()
        self.service = PatientService(self.patient_repository)
        
        self.test_patient_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "john@example.com",
            "phone_number": "1234567890",
            "date_of_birth": datetime(1990, 1, 1),
            "gender": Gender.MALE,
            "patient_id": "P123",
            "password": "test_password"
        }
    
    def test_register(self):
        result = self.service.register(self.test_patient_data)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.first_name, "John")
        self.assertEqual(result.email_address, "john@example.com")
        self.assertTrue(check_password_hash(result.hash_password, "test_password"))
    
    def test_login_success(self):
        # Create a patient with known password
        patient = Patient(
            **{k: v for k, v in self.test_patient_data.items() if k != "password"}
        )
        patient.hash_password = self.service._hash_password("test_password")
        patient.save()
        
        self.patient_repository.find_by_email.return_value = patient
        
        result = self.service.login("john@example.com", "test_password")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["email"], "john@example.com")
        self.assertEqual(result["name"], "John Doe")
    
    def test_login_failure(self):
        self.patient_repository.find_by_email.return_value = None
        
        result = self.service.login("wrong@example.com", "wrong_password")
        
        self.assertIsNone(result)
    
    def test_create_appointment(self):
        self.patient_repository.create_appointment.return_value = True
        
        result = self.service.create_appointment(
            "P123",
            "D123",
            datetime.now()
        )
        
        self.assertTrue(result)
        self.patient_repository.create_appointment.assert_called_once()
    
    def test_reschedule_appointment(self):
        self.patient_repository.reschedule_appointment.return_value = True
        new_date = datetime.now()
        
        result = self.service.reschedule_appointment(
            "P123",
            "A123",
            new_date
        )
        
        self.assertTrue(result)
        self.patient_repository.reschedule_appointment.assert_called_once()
