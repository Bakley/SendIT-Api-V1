"""Parcel view file."""
from flask_restful import Resource, reqparse

# imports from model file and validator
from app.api.v1.models.parcel_models import ParcelModel
from app.api.v1.validators import check_for_blanks, check_for_intergers


class ParcelResource(Resource):
    """Resource for the parcel orders."""

    # Enables adding and parsing of multiple arguments in the context of a
    # single request
    parser = reqparse.RequestParser()
    parser.add_argument('sender_location', type=str, required=True,
                        help='The present location cannot be blank')
    parser.add_argument('destination', type=str, required=True,
                        help='The destination cannot be blank')
    parser.add_argument('weight', type=int, required=True,
                        help='The weight can only be an interger')
    parser.add_argument('parcel_name', type=str, required=True,
                        help='The parcel_name cannot be blank')

    def post(self):
        """Method for creating a parcel delivery order POST http method."""
        args = ParcelResource.parser.parse_args()
        sender_location = args.get('sender_location')
        parcel_name = args.get('parcel_name')
        destination = args.get('destination')
        weight = args.get('weight')
        userid = args.get('userid')

        if check_for_blanks(sender_location) or check_for_blanks(parcel_name) \
                or check_for_blanks(destination):
            return {'message': 'All fields are required'}, 400

        if check_for_intergers(weight):
            return {'message': 'The value need to be an interger'}, 400

        parcel = ParcelModel(sender_location=sender_location,
                             weight=weight,
                             parcel_name=parcel_name,
                             destination=destination,
                             userid=userid
                             )

        parcel = parcel.save()

        return {'message':
                'Parcel delivery order has been saved', 'parcel': parcel}, 201

    def get(self):
        """Method for gettting single parcel delivery order GET http method."""
        product_order = ParcelModel.get_all_parcels()
        if not product_order:
            return{'message': 'No product yet found'}, 404

        return {'message':
                'Parcel delivery order found', 'Parcel': product_order}, 200


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

    def delete(self, id):
        """Method for deleting a parcel delivery order DELETE http method."""
        product_order = ParcelModel.delete(id)
        if isinstance(product_order, ParcelModel):
            product_order.delete()
            return {'message':
                    'The product delivery order has been deleted'}, 200

        return {'message': 'No product delivery order found'}


class GetUserParcels(Resource):
    """Class for getting user parcels."""

    def get(self, id):
        """Get a user parcel orders."""
        product_order = ParcelModel.get_one_parcel_by_user(id)
        if not product_order:
            return{'message':
                   'No product Exist with that ID'}, 404
        return {'message':
                'Parcel delivery order found', 'Parcel': product_order}, 200
