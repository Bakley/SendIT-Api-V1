"""User views contains Signup and login."""
from flask_restful import Resource, reqparse
import re

from app.api.v1.models.user_models import UserModel
from app.api.v1.validators import check_for_blanks


class SignupResource(Resource):
    """Resource for user registration."""

    # <RequestParser> Enables adding and parsing of multiple arguments
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,
                        help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True,
                        help='Email cannot be blank', type=str)
    parser.add_argument('password', required=True,
                        help='Password cannot be blank', type=str)
    parser.add_argument('role', required=True,
                        help='Role cannot be blank', type=str)

    def post(self):
        """Method for signing up a user."""
        # <parse_args>
        # Parse all arguments from the provided request
        # and return the results as a Namespace
        args = SignupResource.parser.parse_args()
        password = args.get('password')
        username = args.get('username')
        email = args.get('email')
        role = args.get('role')

        email_format = re.compile(
            r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$)")
        username_format = re.compile(r"(^[A-Za-z]+$)")

        if not (re.match(username_format, username)):
            return {'message':
                    'Invalid username, only characters allowed no intergs allowed'}, 400

        elif not (re.match(email_format, email)):
            return {'message':
                    'Invalid email. Ensure email is of the form example@mail.com'}, 400

        if len(username) < 4:
            return {'message':
                    'Username should be atleast 4 characters'}, 400
        if check_for_blanks(password) or check_for_blanks(username) or check_for_blanks(email):
            return {'message':
                    'All fields are required'}, 400

        if len(password) < 8:
            return {'message':
                    'Password should be atleast 8 characters'}, 400

        username_exists = UserModel.get_user_by_username(
            username=args['username'])
        email_exists = UserModel.get_user_by_email(email=args['email'])

        if username_exists or email_exists:
            return {'message': 'User already exists'}, 203

        user = UserModel(username=args.get('username'), email=args.get(
            'email'), role=args.get('role'), password=password)
        user = user.save()

        return {'message': 'Successfully registered', 'user': user}, 201


class LoginResource(Resource):
    """Resource for user login."""

    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,
                        help='Username cannot be blank', type=str)
    parser.add_argument('password', required=True,
                        help='Password cannot be blank')

    def post(self):
        """Method for logging in a signed up user."""
        args = LoginResource.parser.parse_args()
        username = args["username"]
        password = args["password"]

        if check_for_blanks(username) or check_for_blanks(password) == '':
            return {'message': 'All fields are required'}, 400

        user = UserModel.get_user_by_username(username)
        if not user:
            return {'message':
                    'User has not yet been registered.'}, 404

        if user.validate_user_password(password):
            return {"message": "You are successfully logged in",
                    'user': user.view()}, 200
        return {"message": "Username or password is wrong."}, 401
