"""version 1 blueprint."""
from flask import Blueprint
from flask_restful import Api

# import from Views
from app.api.v1.views.parcel_views import ParcelResource, ParcelSpecific
from app.api.v1.views.user_views import SignupResource, LoginResource

version1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')

app = Api(version1)

# Resources are the spiecific route we need to pass the endpoint

# Parcel
app.add_resource(ParcelResource, '/parcel')
app.add_resource(ParcelSpecific, '/parcel/<int:id>', '/parcel/<int:id>/cancel')

# Users
app.add_resource(SignupResource, '/user/register')
app.add_resource(LoginResource, '/user/login')
