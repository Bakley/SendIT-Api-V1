"""Test base class."""
import unittest
import json

from app import create_app
from app.api.v1.models.parcel_models import ParcelModel
from app.api.v1.models.user_models import UserModel, database


SIGNUP_URL = '/api/v1/user/register'
LOGIN_URL = '/api/v1/user/login'


class BaseClass(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.user_data = {
            "username": "Barclay",
            "email": "koin@gmail.com",
            "password": "mypassword",
            "role": "User"
        }

        self.parcel_data = [
            {
                "sender_location": "Nanyuki",
                "weight": "9",
                "destination": "udsfb",
                "parcel_name": "Bucket",
                "userid": "1"
            }
        ]

        self.user1 = UserModel(
            username='testuser',
            email='testuser@email.com',
            password='password',
            role='Admin')

        self.parcel_order1 = ParcelModel(
            sender_location="Nanyuki",
            weight="9",
            destination="udsfb",
            parcel_name="Bucket",
            userid="1"
        )

        self.test_user = UserModel(
            username='Koin',
            email='koin@email.com',
            password='password',
            role='User')

    def logged_in_user(self):
        """First create user, then log in user."""
        self.client.post(SIGNUP_URL, data=json.dumps(
            self.user_data), content_type='application/json')

        response = self.client.post(LOGIN_URL,
                                    data=json.dumps({'username': 'Barclay',
                                                     'password': 'mypassword'}), content_type='application/json')

        return response

    def tearDown(self):
        """Clear the database."""
        database.drop()
