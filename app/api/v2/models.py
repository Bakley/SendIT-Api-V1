"""The API version 2 model file."""

from ...db_config import init_db


class ParcelModel(object):
    """docstring for ParcelModel."""

    def __init__(self):
        self.db = init_db()

    def save(self):
        """Method to save values in database."""
        pass
