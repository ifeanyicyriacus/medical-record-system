import unittest
from unittest.mock import patch, MagicMock
from repositories.doctor_repository import DoctorRepository
from exceptions import DoctorNotFoundException, DatabaseError, EmailAlreadyExistsException
from models.user import User


class TestDoctorRepository(unittest.TestCase):
    def setUp(self):
        self.doctor_repo = DoctorRepository()
        self.doctor_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'securepassword',
            'phone_number': '1234567890',
            'email_address': 'john.doe@example.com',
            'dob': '1980-01-01',
            'gender': 'male',
            'role': 'doctor'
        }

    @patch('repositories.doctor_repository.MongoClient')
    def test_create_doctor(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_mongo_client().db.collection = mock_collection
        mock_collection.find_one.return_value = None

        result = self.doctor_repo.create_doctor(self.doctor_data)

        self.assertIsNotNone(result)
        mock_collection.insert_one.assert_called_once()

    @patch('repositories.doctor_repository.MongoClient')
    def test_create_doctor_email_already_exists(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_mongo_client().db.collection = mock_collection
        mock_collection.find_one.return_value = self.doctor_data

        with self.assertRaises(EmailAlreadyExistsException):
            self.doctor_repo.create_doctor(self.doctor_data)

    @patch('repositories.doctor_repository.MongoClient')
    def test_get_doctor_by_id(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_mongo_client().db.collection = mock_collection
        mock_collection.find_one.return_value = self.doctor_data

        doctor = self.doctor_repo.get_doctor_by_id('some_doctor_id')

        self.assertIsNotNone(doctor)

    @patch('repositories.doctor_repository.MongoClient')
    def test_get_doctor_by_id_not_found(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_mongo_client().db.collection = mock_collection
        mock_collection.find_one.return_value = None

        with self.assertRaises(DoctorNotFoundException):
            self.doctor_repo.get_doctor_by_id('some_doctor_id')


if __name__ == '__main__':
    unittest.main()