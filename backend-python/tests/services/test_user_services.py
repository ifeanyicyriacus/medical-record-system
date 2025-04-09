import unittest
from unittest.mock import MagicMock, patch
from models.user import User
from repositories.user_repository import UserRepository
from services.user_service import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_repository = MagicMock(UserRepository)
        self.user_service = UserService(self.user_repository)

    def test_create_user_success(self):
        user_data = {
            'email_address': 'test@example.com',
            'password': 'password123',
            'name': 'Test User'
        }
        self.user_repository.create_user.return_value = user_data

        created_user = self.user_service.create_user(user_data)

        self.user_repository.create_user.assert_called_once_with(user_data)
        self.assertEqual(created_user['email_address'], 'test@example.com')

    def test_create_user_email_exists(self):
        user_data = {
            'email_address': 'test@example.com',
            'password': 'password123',
            'name': 'Test User'
        }
        self.user_repository.get_user_by_email.return_value = user_data

        with self.assertRaises(Exception) as context:
            self.user_service.create_user(user_data)

        self.assertTrue("Email already exists." in str(context.exception))

    def test_get_user_by_id_success(self):
        user_id = '12345'
        user_data = {
            '_id': user_id,
            'email_address': 'test@example.com',
            'name': 'Test User'
        }
        self.user_repository.get_user_by_id.return_value = user_data

        user = self.user_service.get_user_by_id(user_id)

        self.user_repository.get_user_by_id.assert_called_once_with(user_id)
        self.assertEqual(user['_id'], user_id)

    def test_update_user_success(self):
        user = User(email_address='test@example.com', name='Test User')
        user.id = '12345'
        self.user_repository.update.return_value = None

        self.user_service.update_user(user)

        self.user_repository.update.assert_called_once_with(user)

    def test_delete_user_success(self):
        user_id = '12345'
        self.user_repository.delete.return_value = None

        self.user_service.delete_user(user_id)

        self.user_repository.delete.assert_called_once_with(user_id)

    def test_authenticate_user_success(self):
        email = 'test@example.com'
        password = 'password123'
        user_data = User(email_address=email)
        user_data.check_password = MagicMock(return_value=True)
        self.user_repository.get_user_by_email.return_value = user_data

        user = self.user_service.authenticate_user(email, password)

        self.user_repository.get_user_by_email.assert_called_once_with(email)
        self.assertEqual(user.email_address, email)

    def test_authenticate_user_failure(self):
        email = 'test@example.com'
        password = 'wrongpassword'
        user_data = User(email_address=email)
        user_data.check_password = MagicMock(return_value=False)
        self.user_repository.get_user_by_email.return_value = user_data

        user = self.user_service.authenticate_user(email, password)

        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
