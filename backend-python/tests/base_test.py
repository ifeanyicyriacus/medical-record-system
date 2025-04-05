import unittest
from mongoengine import connect, disconnect
from app import create_app
from app.config import Config

class TestConfig(Config):
    MONGODB_SETTINGS = {
        'host': 'mongomock://localhost',
        'db': 'mrs_test'
    }
    TESTING = True

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        
    def setUp(self):
        self.db = connect('mrs_test', host='mongomock://localhost')
    
    def tearDown(self):
        disconnect()
    
    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()