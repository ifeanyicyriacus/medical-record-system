from datetime import datetime
from tests.base_test import BaseTest
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.repositories.patient_repository import PatientRepository
from app.models.gender import Gender

class TestPatientRepository(BaseTest):
    def setUp(self):
        super().setUp()
        self.repository = PatientRepository()
        self.test_patient = Patient(
            first_name="John",
            last_name="Doe",
            email_address="john@example.com",
            phone_number="1234567890",
            date_of_birth=datetime(1990, 1, 1),
            gender=Gender.MALE,
            patient_id="P123",
            hash_password="hashed_password"
        ).save()
    
    def test_create_appointment(self):
        appointment_data = {
            "date": datetime.now(),
            "doctor_id": "D123",
            "patient_id": self.test_patient.patient_id,
            "appointment_id": "A123"
        }
        
        result = self.repository.create_appointment(
            self.test_patient.patient_id, 
            appointment_data
        )
        self.assertTrue(result)
        
        patient = Patient.objects.get(patient_id=self.test_patient.patient_id)
        self.assertEqual(len(patient.appointments), 1)
    
    def test_find_by_email(self):
        patient = self.repository.find_by_email("john@example.com")
        self.assertIsNotNone(patient)
        self.assertEqual(patient.email_address, "john@example.com")
    
    def test_update_profile(self):
        update_data = {
            "phone_number": "0987654321",
            "email_address": "john.new@example.com"
        }
        
        result = self.repository.update_profile(
            self.test_patient.patient_id,
            update_data
        )
        self.assertTrue(result)
        
        updated_patient = Patient.objects.get(patient_id=self.test_patient.patient_id)
        self.assertEqual(updated_patient.phone_number, "0987654321")
        self.assertEqual(updated_patient.email_address, "john.new@example.com")
    
    def test_change_password(self):
        result = self.repository.change_password(
            self.test_patient.patient_id,
            "new_password"
        )
        self.assertTrue(result)
        
        updated_patient = Patient.objects.get(patient_id=self.test_patient.patient_id)
        self.assertNotEqual(updated_patient.hash_password, "hashed_password")