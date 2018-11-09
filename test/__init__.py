import unittest
import json

from app import create_app
from app.api.v1.models.parcel_models import ParcelModel, parcel
from app.api.v1.models.user_models import UserModel, database
from app.api.v1.models import MockDatabase

SIGNUP_URL = '/api/v1/user/register'
LOGIN_URL = '/api/v1/user/login'


class BaseClass(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.user_data = {
            "username": "Barclay",
            "email": "koin@gmail.com",
            "password": "mypassword",
            "role": "User"
        }

        self.parcel_data = {
            "present_location": "Nakuru",
            "price": "$12",
            "weight": "21kg",
            "destination": "Nairobi",
            "status": "Delivered"
        }

        self.user1 = UserModel(
            username='testuser',
            email='testuser@email.com',
            password='password',
            role='Admin')

        self.parcel_order1 = ParcelModel(
            present_location="Nyeri",
            price="$21",
            weight="12kg",
            destination="Nairobi",
            status="Delivered"
        )

        self.test_user = UserModel(
            username='Koin',
            email='koin@email.com',
            password='password',
            role='User')

    def logged_in_user(self):
        # first create user
        self.client.post(SIGNUP_URL, data=json.dumps(
            self.user_data), content_type='application/json')

        # then log in user
        response = self.client.post(LOGIN_URL,
                                    data=json.dumps({'username': 'Barclay', 'password': 'mypassword'}), content_type='application/json')

        return response

    def tearDown(self):
        '''Clears the database'''
        database.drop()
