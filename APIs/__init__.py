from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint('api', __name__)
api = Api(blueprint, version='1.0', title='RESTful API with Flask, Flask-RESTx and SQLAlchemy', contact='Gil Tober',
          contact_email='giltober@gmail.com', doc='/docs')

from .CustomersApi import ns as ns1, CustomersApi

api.add_namespace(ns1, path='/api')
ns1.add_resource(CustomersApi, '/Customers')