"""API version 2 views file."""
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
parser.add_argument()
args = parser.parse_args()
