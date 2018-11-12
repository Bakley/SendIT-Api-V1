"""The API version 2 model file."""

from app.db_config import init_db


class UserModel(object):
    """docstring for ParcelModel."""

    def __init__(self):
        """Initialize the user db."""
        self.db = init_db()

    def save(self):
        """Method to save user values in database."""
        payload = {
            'email': self.email,
            'password': self.password,
            'role': self.role
        }

        query = """INSERT INTO users(email, password, role)
                VALUES(%s,%s,%s,%s) RETURNING userid;"""

        curr = self.db.cursor()
        curr.execute(query, payload)
        response = curr.fetchone()[0]
        self.db.commit()
        return {'response': response}
