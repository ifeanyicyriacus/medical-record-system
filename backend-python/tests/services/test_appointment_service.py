from datetime import datetime, timedelta
from unittest.mock import Mock, patch
from tests.base_test import BaseTest
from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.gender import Gender
from app.models.specialization import Specialization
from app.models.appointment_status import AppointmentStatus
from app.services.appointment_service import AppointmentService

class TestAppointmentService(BaseTest):
    def setUp(self):
        super().setUp()
        self.appointment_repository = Mock()
        self.service = AppointmentService(self.appointment_repository)
        
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
    
    def test_schedule_appointment_success(self):
        self.appointment_repository.schedule_appointment.return_value = True
        
        appointment = self.service.schedule_appointment(
            "D123",
            "P123",
            datetime.now() + timedelta(days=1)
        )
        
        self.assertIsNotNone(appointment)
        self.appointment_repository.schedule_appointment.assert_called_once()
    
    def test_schedule_appointment_slot_not_available(self):
        # Create an existing appointment in the same slot
        existing_appointment = Appointment(
            appointment_id="A123",
            date=datetime.now(),
            doctor=self.test_doctor,
            patient=self.test_patient,
            appointment_status=AppointmentStatus.SCHEDULED
        ).save()
        
        appointment = self.service.schedule_appointment(
            "D123",
            "P123",
            existing_appointment.date
        )
        
        self.assertIsNone(appointment)
        self.appointment_repository.schedule_appointment.assert_not_called()
    
    def test_reschedule_appointment_success(self):
        self.appointment_repository.update_appointment.return_value = True
        new_date = datetime.now() + timedelta(days=2)
        
        result = self.service.reschedule_appointment(
            "A123",
            new_date
        )
        
        self.assertTrue(result)
        self.appointment_repository.update_appointment.assert_called_once()
    
    def test_cancel_appointment(self):
        self.appointment_repository.update_appointment.return_value = True
        
        result = self.service.cancel_appointment("A123")
        
        self.assertTrue(result)
        self.appointment_repository.update_appointment.assert_called_once()
    
    def test_get_appointment_details(self):
        expected_details = {
            "id": "A123",
            "date": datetime.now(),
            "doctor": str(self.test_doctor.id),
            "patient": str(self.test_patient.id),
            "status": AppointmentStatus.SCHEDULED.value
        }
        self.appointment_repository.get_details.return_value = expected_details
        
        details = self.service.get_appointment_details("A123")
        
        self.assertEqual(details, expected_details)
        self.appointment_repository.get_details.assert_called_once_with("A123")
    
    def test_find_available_slots(self):
        # Mock an existing appointment
        existing_date = datetime.now().replace(hour=10, minute=0)
        Appointment(
            appointment_id="A123",
            date=existing_date,
            doctor=self.test_doctor,
            patient=self.test_patient,
            appointment_status=AppointmentStatus.SCHEDULED
        ).save()
        
        slots = self.service.find_available_slots(
            "D123",
            existing_date.date()
        )
        
        # Should return all slots except the booked one
        self.assertNotIn(existing_date, slots)
        # Should return slots between 9 AM and 5 PM
        for slot in slots:
            self.assertTrue(9 <= slot.hour < 17)
