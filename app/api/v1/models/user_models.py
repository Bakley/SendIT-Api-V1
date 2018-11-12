"""app/api/v1/models/user_models.py contains user models for the app."""
from werkzeug.security import check_password_hash, generate_password_hash


from .import MockDatabase


# Initialize the mock database
database = MockDatabase()


class UserModel:
    """Class user models."""

    def __init__(self, username, email, password, role):
        """Initialize users information."""
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
        self.id = None

    def save(self):
        """Create the user information in the mock database."""
        setattr(self, 'id', database.user_number +
                1)  # Increment the user number
        # self is the object to be set // setattr(object, name, value)
        database.users.update({self.id: self})
        database.user_number += 1  # Increment the User list
        # Link the user_id to the Parcel so to query for parcel using user_id

        return self.view()

    def view(self):
        """Jsonify the User object."""
        database_keys = ['username', 'email', 'role', 'id']
        return {key: getattr(self, key)for key in database_keys}

    def delete(self):
        """Method for deleting a user."""
        del database.users[self.id]

    @classmethod
    def get(cls, id):
        """Method to get user by id."""
        user = database.users.get(id)
        if not user:
            return {'message': 'User does not exist'}
        return user

    @classmethod
    def get_all_user(cls, id):
        """Method for getting all users available in the database."""
        for id_ in database.users:
            user = database.users.get(id_)
            if user.id == id:
                return user
            return None

    @classmethod
    def get_user_by_email(cls, email):
        """Method for getting user by email."""
        for id_ in database.users:
            user = database.users.get(id_)
            if user.email == email:
                return user
        return None

    @classmethod
    def get_user_by_username(cls, username):
        """Method for getting user by username."""
        for id_ in database.users:
            user = database.users.get(id_)
            if user.username == username:
                return user
        return None

    def validate_user_password(self, password):
        """Check if user password is right."""
        if check_password_hash(self.password, password):
            return True
        return False
