from datetime import datetime
from tests.base_test import BaseTest
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.repositories.doctor_repository import DoctorRepository
from app.models.gender import Gender
from app.models.specialization import Specialization
from app.models.appointment_status import AppointmentStatus

class TestDoctorRepository(BaseTest):
    def setUp(self):
        super().setUp()
        self.repository = DoctorRepository()
        self.test_doctor = Doctor(
            first_name="Jane",
            last_name="Smith",
            email_address="jane@example.com",
            phone_number="1234567890",
            date_of_birth=datetime(1985, 1, 1),
            gender=Gender.FEMALE,
            doctor_id="D123",
            specialization=Specialization.GENERAL_PRACTICE,
            hash_password="hashed_password"
        ).save()
        
        self.test_appointment = Appointment(
            appointment_id="A123",
            date=datetime.now(),
            doctor=self.test_doctor,
            appointment_status=AppointmentStatus.SCHEDULED
        ).save()
    
    def test_update_appointment_notes(self):
        result = self.repository.update_appointment_notes(
            self.test_appointment.appointment_id,
            "Test notes"
        )
        self.assertTrue(result)
        
        appointment = Appointment.objects.get(appointment_id=self.test_appointment.appointment_id)
        self.assertEqual(appointment.doctor_notes, "Test notes")
    
    def test_update_appointment_status(self):
        result = self.repository.update_appointment_status(
            self.test_appointment.appointment_id,
            "COMPLETED"
        )
        self.assertTrue(result)
        
        appointment = Appointment.objects.get(appointment_id=self.test_appointment.appointment_id)
        self.assertEqual(appointment.appointment_status, AppointmentStatus.COMPLETED)
    
    def test_find_by_email(self):
        doctor = self.repository.find_by_email("jane@example.com")
        self.assertIsNotNone(doctor)
        self.assertEqual(doctor.email_address, "jane@example.com")
    
    def test_find_by_specialization(self):
        doctors = self.repository.find_by_specialization(Specialization.GENERAL_PRACTICE)
        self.assertEqual(len(doctors), 1)
        self.assertEqual(doctors[0].doctor_id, "D123")
    
    def test_update_profile(self):
        update_data = {
            "phone_number": "0987654321",
            "email_address": "jane.new@example.com"
        }
        
        result = self.repository.update_profile(
            self.test_doctor.doctor_id,
            update_data
        )
        self.assertTrue(result)
        
        updated_doctor = Doctor.objects.get(doctor_id=self.test_doctor.doctor_id)
        self.assertEqual(updated_doctor.phone_number, "0987654321")
        self.assertEqual(updated_doctor.email_address, "jane.new@example.com")
    
    def test_change_password(self):
        result = self.repository.change_password(
            self.test_doctor.doctor_id,
            "new_password"
        )
        self.assertTrue(result)
        
        updated_doctor = Doctor.objects.get(doctor_id=self.test_doctor.doctor_id)
        self.assertNotEqual(updated_doctor.hash_password, "hashed_password")