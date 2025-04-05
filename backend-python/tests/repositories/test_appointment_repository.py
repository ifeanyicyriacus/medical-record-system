from datetime import datetime, timedelta
from tests.base_test import BaseTest
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.repositories.appointment_repository import AppointmentRepository
from app.models.gender import Gender
from app.models.specialization import Specialization
from app.models.appointment_status import AppointmentStatus

class TestAppointmentRepository(BaseTest):
    def setUp(self):
        super().setUp()
        self.repository = AppointmentRepository()
        
        # Create test doctor
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
        
        # Create test patient
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
        
        # Create test appointment
        self.test_appointment = Appointment(
            appointment_id="A123",
            date=datetime.now(),
            doctor=self.test_doctor,
            patient=self.test_patient,
            appointment_status=AppointmentStatus.SCHEDULED
        ).save()
    
    def test_schedule_appointment(self):
        new_appointment = Appointment(
            appointment_id="A124",
            date=datetime.now() + timedelta(days=1),
            doctor=self.test_doctor,
            patient=self.test_patient,
            appointment_status=AppointmentStatus.SCHEDULED
        )
        
        result = self.repository.schedule_appointment(new_appointment)
        self.assertTrue(result)
        
        saved_appointment = Appointment.objects.get(appointment_id="A124")
        self.assertIsNotNone(saved_appointment)
    
    def test_update_appointment(self):
        self.test_appointment.appointment_status = AppointmentStatus.COMPLETED
        result = self.repository.update_appointment(self.test_appointment.appointment_id)
        self.assertTrue(result)
        
        updated_appointment = Appointment.objects.get(appointment_id=self.test_appointment.appointment_id)
        self.assertEqual(updated_appointment.appointment_status, AppointmentStatus.COMPLETED)
    
    def test_get_details(self):
        details = self.repository.get_details(self.test_appointment.appointment_id)
        self.assertEqual(details["id"], str(self.test_appointment.id))
        self.assertEqual(details["doctor"], str(self.test_doctor.id))
        self.assertEqual(details["patient"], str(self.test_patient.id))
        self.assertEqual(details["status"], self.test_appointment.appointment_status.value)
    
    def test_find_by_date_range(self):
        now = datetime.now()
        start_date = now - timedelta(days=1)
        end_date = now + timedelta(days=1)
        
        appointments = self.repository.find_by_date_range(start_date, end_date)
        self.assertEqual(len(appointments), 1)
        self.assertEqual(appointments[0].appointment_id, "A123")