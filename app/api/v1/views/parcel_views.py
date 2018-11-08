from flask import Flask, request
from flask_restful import Resource, reqparse

# imports from model file and validator
from app.api.v1.models.parcel_models import ParcelModel
from app.api.v1.validators import check_for_blanks

class ParcelResource(Resource):
    """Resource for the parcel orders"""

    # Enables adding and parsing of multiple arguments in the context of a single request
    parser = reqparse.RequestParser()
    parser.add_argument('present_location', type=str, help='The present location cannot be blank')
    parser.add_argument('status', type=str, help='The status cannot be blank')
    parser.add_argument('destination', type=str, help='The destination cannot be blank')
    parser.add_argument('price', type=str, help='The price cannot be blank')
    parser.add_argument('weight', type=str, help='The weight cannot be blank')

    def post(self):
        """
        Method for creating a parcel delivery order
        POST http method
        """
        args = ParcelResource.parser.parse_args()
        present_location = args.get('present_location', '')
        price = args.get('price', '')
        weight = args.get('weight', '')
        destination = args.get('destination', '')
        status = args.get('status', '')

        if check_for_blanks(present_location) or check_for_blanks(status) or check_for_blanks(price) or check_for_blanks(destination) or check_for_blanks(status):
            return {'message': 'All fields are required'}, 400

        parcel = ParcelModel(present_location=present_location, price=price, weight=weight, destination=destination, status=status)
        parcel = parcel.save()
        return {'message': 'Parcel delivery order has been saved', 'parcel': parcel}, 201

    def get(self, parcel_id):
        """
        Method for gettting both single and multiple parcel delivery order
        GET http method
        """
        product_order = ParcelModel(id=parcel_id)
        if isinstance(product_order, ParcelModel):
            # https://python-reference.readthedocs.io/en/latest/docs/functions/isinstance.html
            return {'message': 'Parcel delivery order found', 'Parcel':product_order.view()}, 200

        if product_order.get('message'):
            return product_order, 404
        return {'message': 'Parcel delivery order', 'parcel': [product_order[parcel].view() for parcel in product_order]}, 200

    def put(self, parcel_id):
        """
        Method for Updating a parcel delivery order
        PUT http method
        """
        parcel = ParcelModel.get(id=parcel_id)

        if isinstance(parcel, dict):
            return parcel, 404
        post_data = request.get_json()
        destination = post_data.get('destination', None)
        status = post_data.get('status', None)

        new_data = {}

        if destination and check_for_blanks(destination) != '':
            new_data.update({'destination': destination})

        if status and check_for_blanks(status) != '':
            new_data.update({'status': status})

        parcel = parcel.update(new_data=new_data)
        return {'message': 'Parcel delivery order succesfully updated', 'new parcel order': parcel}, 200

    def delete(self, parcel_id):
        """
        Method for deleting a parcel delivery order
        DELETE http method
        """
        product_order = ParcelModel.get(id=parcel_id)
        if isinstance(product_order, ParcelModel):
            product_order.delete()
            return {'message': 'The product delivery order has been deleted'}, 200
        return {'message': 'No product delivery order found'}
