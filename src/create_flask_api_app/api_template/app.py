from flask import Flask
from flask_restful import Api
from api_template.resources.example import Example

app = Flask(__name__)
api = Api(app)

api.add_resource(Example, "/Example", "/Example/<string:id>")
