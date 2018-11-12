"""The API version 2 model file."""

from ...db_config import init_db


class ParcelModel(object):
    """docstring for ParcelModel."""

    def __init__(self):
        """Initialize the user db."""
        self.db = init_db()

    def save(self, present_location, price, weight, destination, status='Active'):
        """Method to save parcel orders values in database."""
        payload = {
            'present_location': present_location,
            'price': price,
            'weight': weight,
            'destination': destination,
            'status': status
        }

        query = """INSERT INTO orders(present_location, price, weight, destination)
        VALUES(%s,%s,%s,%s,%s) RETURNING orderid;"""

        curr = self.db.cursor()
        curr.execute(query, payload)
        response = curr.fetchone()[0]
        self.db.commit()
        return {'response': response}

    def getparcelorder(self):
        """Get all parcels."""
        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT""")
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            pass
