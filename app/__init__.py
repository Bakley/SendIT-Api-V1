from flask import Flask, Blueprint

import os
from config import app_config


def create_app(config_name):
    """ Creates the app with the desired environment """
    # instantiate the flask app
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    # app setting config
    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    # app.config['JWT_SECRET_KEY'] = "your-secret"

    #import the blueprint from the V1 folder __init__.py file and register the blueprint
    from app.api.v1 import version1  
    app.register_blueprint(version1) 

    return app