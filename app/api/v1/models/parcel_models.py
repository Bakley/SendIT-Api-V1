"""
app/api/v1/models/parcel_models.py.
contains user models for the app
"""
# from .import MockDatabase

# Initialize the mock database
# database = MockDatabase()
parcel = []


class ParcelModel():
    """Class Parcel models."""

    def __init__(self, present_location, price, weight, destination, status):
        """Initialize users information."""
        self.present_location = present_location
        self.price = price
        self.weight = weight
        self.destination = destination
        self.status = status
        self.id = None

    def save(self):
        """Create the Parcel information in the mock database and save."""
        parcels = {}
        parcels['id'] = str(len(parcel) + 1)
        parcels['present_location'] = self.present_location
        parcels['price'] = self.price
        parcels['weight'] = self.weight
        parcels['destination'] = self.destination
        parcels['status'] = self.status
        parcel.append(parcels)
        return parcel

    def delete(self):
        """Method for deleting a user."""
        del parcel

    def get_all_parcels(self):
        """Method for getting all parcels available in the database."""
        return parcel

    def get_one_parcel(self, id):
        """Method for getting a specific parcel available in the database."""
        new_parcel = [new_parcel for new_parcel in parcels if new_parcel[
            'id'] == id]  # list comprehension
