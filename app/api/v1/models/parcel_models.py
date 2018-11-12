
"""app/api/v1/models/parcel_models.py. contains user models for the app."""
# from .import MockDatabase

# Initialize the mock database
# database = MockDatabase()
parcel = []


class ParcelModel():
    """Class Parcel models."""

    def __init__(self, present_location, price, weight, destination):
        """Initialize users information."""
        self.present_location = present_location
        self.price = price
        self.weight = weight
        self.destination = destination
        self.status = "active"
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
        return parcel.pop()

    def get_all_parcels(self):
        """Method for getting all parcels available in the database."""
        return parcel

    @classmethod
    def get_one_parcel(cls, id):
        """Method for getting a specific parcel available in the database."""
        new_parcel = [new_par for new_par in parcel if new_par[
            'id'] == str(id)]  # list comprehension
        return new_parcel

    @classmethod
    def cancel_order(cls, id):
        """Cancel a parcel order."""
        for parcel_order in parcel:
            if str(id) == parcel_order["id"]:
                parcel_order.update({'status': 'Canceled'})
                return parcel_order
            return 404
