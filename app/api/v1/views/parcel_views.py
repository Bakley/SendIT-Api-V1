from flask import Flask, request
from flask_restful import Resource

# imports from model file
from app.api.v1.models.parcel_models import ParcelModel
from app.api.v1.validators import check_for_blanks

class ParcelResource(Resource):
    """Resource for the parcel orders"""

    def post(self, user_id):
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

        if check_for_blanks(present_location) or check_for_blanks(status) or check_for_blanks(price) or check_for_blanks(destinantion) or check_for_blanks(status):
            return {'message': 'All fields are required'}, 400

        parcel = ParcelModel(present_location, price, weight, destination, status)
        parcel = parcel.save()
        return {'message': 'Parcel delivery order has been saved', 'parcel': parcel}, 201

