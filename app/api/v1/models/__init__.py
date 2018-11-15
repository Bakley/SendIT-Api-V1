"""The mock database setup."""


class MockDatabase():
    """Class for mock database."""

    def __init__(self):
        """Initialize the parameters."""
        self.users = {}
        self.user_number = 0
        self.parcel_number = 0

    def drop(self):
        """Destroy the mock db."""
        self.__init__()
