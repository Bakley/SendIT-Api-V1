"""app/api/v1/models/parcel_models.py. contains user models for the app."""

parcel = []


class ParcelModel():
    """Class Parcel models."""

    def __init__(self, sender_location, weight, destination, parcel_name, userid):
        """Initialize users information."""
        self.sender_location = sender_location
        self.weight = weight
        self.destination = destination
        self.parcel_name = parcel_name
        self.price = weight * 250
        self.status = "active"
        self.id = None
        self.userid = userid

    def save(self):
        """Create the Parcel information in the mock database and save."""
        parcels = {}
        parcels['id'] = str(len(parcel) + 1)
        parcels['userid'] = self.userid
        parcels['sender_location'] = self.sender_location
        parcels['weight'] = self.weight
        parcels['destination'] = self.destination
        parcels['parcel_name'] = self.parcel_name
        parcels['status'] = self.status
        parcels['price'] = self.price
        parcel.append(parcels)
        return parcels

    @classmethod
    def delete(cls, id):
        """Method for deleting a user."""
        new_parcel = [new_par for new_par in parcel if new_par[
            'id'] == str(id)]
        return parcel.parcels.pop(new_parcel)

    @classmethod
    def get_all_parcels(cls):
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

    @classmethod
    def get_one_parcel_by_user(cls, id):
        """Method for getting a specific parcel available in the database."""
        new_parcel = [new_par for new_par in parcel if new_par[
            'id'] == str(id)]  # list comprehension
        return new_parcel
