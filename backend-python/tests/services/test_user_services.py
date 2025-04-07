import unittest
from services.user_service import UserService
from models.user import User
from utils.exceptions import UserNotFoundException

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'password123'
        }

    def test_create_user(self):
        user = UserService.create_user(self.user_data)
        self.assertIsNotNone(user.id)

    def test_get_user_by_email(self):
        UserService.create_user(self.user_data)
        user = UserService.get_user_by_email('john.doe@example.com')
        self.assertEqual(user.email, 'john.doe@example.com')

    def test_get_user_by_id(self):
        user = UserService.create_user(self.user_data)
        found_user = UserService.get_user_by_id(user.id)
        self.assertEqual(found_user.id, user.id)

    def test_delete_user(self):
        user = UserService.create_user(self.user_data)
        UserService.delete_user(user.id)
        with self.assertRaises(UserNotFoundException):
            UserService.get_user_by_id(user.id)

if __name__ == '__main__':
    unittest.main()