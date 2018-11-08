"""
app/api/v1/models/parcel_models.py
contains user models for the app
"""

from .import MockDatabase

# Initialize the mock database
database = MockDatabase()

class ParcelModel():
    """
    Class Parcel models
    Initialize users information
    """

    def __init__(self, present_location, price, weight, destination, status):
        self.present_location = present_location
        self.price = price
        self.weight = weight
        self.destination = destination
        self.status = status
        self.id = None


    def save(self):
        """
        Create the Parcel information in the mock database and save
        """
        setattr(self, 'id', database.parcel_number + 1) # Increment the Parcel number 
        # self is the object to be set
        database.parcel_number += 1 # Increment the Parcel 
        database.parcels.update({self.id: self})
        return self.view()
        
    def view(self):
        """
        Jsonify the Parcel object
        """
        database_keys = ['id', 'present_location', 'price', 'weight', 'destination', 'status']
        return {key: getattr(self, key)for key in database_keys}


    def delete(self):
        '''Method for deleting a user'''
        del database.parcels[self.id]

    @classmethod
    def get_all_user(cls, id):
        """Method for getting all parcels available in the database"""
        for id_ in database.parcels:
            parcel = database.parcels.get(id_)
            if parcel.id == id:
                return parcel
            return None