"""Parcel view file."""

from flask_restful import Resource, reqparse

# imports from model file and validator
from app.api.v1.models.parcel_models import ParcelModel, parcel
from app.api.v1.validators import check_for_blanks


class ParcelResource(Resource):
    """Resource for the parcel orders."""

    # Enables adding and parsing of multiple arguments in the context of a
    # single request
    parser = reqparse.RequestParser()
    parser.add_argument('present_location', type=str,
                        help='The present location cannot be blank')
    parser.add_argument('status', type=str, help='The status cannot be blank')
    parser.add_argument('destination', type=str,
                        help='The destination cannot be blank')
    parser.add_argument('price', type=str, help='The price cannot be blank')
    parser.add_argument('weight', type=str, help='The weight cannot be blank')

    def post(self):
        """Method for creating a parcel delivery order POST http method."""
        args = ParcelResource.parser.parse_args()
        present_location = args.get('present_location', '')
        price = args.get('price', '')
        weight = args.get('weight', '')
        destination = args.get('destination', '')
        # status = args.get('status', '')

        if check_for_blanks(present_location) or check_for_blanks(price) or check_for_blanks(destination):
            return {'message': 'All fields are required'}, 400

        parcel = ParcelModel(present_location=present_location, price=price,
                             weight=weight, destination=destination)
        parcel = parcel.save()
        return {'message':
                'Parcel delivery order has been saved', 'parcel': parcel}, 201

    def get(self):
        """Method for gettting single parcel delivery order GET http method."""
        product_order = ParcelModel.get_all_parcels(id)
        print("product_order", product_order)
        if not product_order:
            return{'message': 'No product yet found'}, 404

        return {'message':
                'Parcel delivery order found', 'Parcel': product_order}, 200

    def delete(self, parcel_id):
        """Method for deleting a parcel delivery order DELETE http method."""
        product_order = ParcelModel.get(id=parcel_id)
        if isinstance(product_order, ParcelModel):
            product_order.delete()
            return {'message':
                    'The product delivery order has been deleted'}, 200
        return {'message': 'No product delivery order found'}


class ParcelSpecific(Resource):
    """Class for specific ids."""

    def get(self, id):
        """Method for gettting single parcel delivery order."""
        product_order = ParcelModel.get_one_parcel(id)
        if not product_order:
            return{'message':
                   'No product Exist with that ID'}, 404
        return {'message':
                'Parcel delivery order found', 'Parcel': product_order}, 200

    def put(self, id):
        """Method for updating parcel info."""
        parcel_orders = ParcelModel.cancel_order(id)
        if parcel_orders:
            return {'new parcel': parcel_orders}
        return {'new parcel': "No parcel order updated"}
