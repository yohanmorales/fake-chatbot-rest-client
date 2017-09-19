from flask_api import FlaskAPI
from flask_cors import CORS
from flask import request, jsonify, abort
from faker import Faker

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    CORS(app)
    fake = Faker()

    @app.route('/evaluate_messages/', methods=['POST'])

    def evaluate_messages():
        response = jsonify({
          'data':  request.data,
          'response': fake.text()
        })
        response.status_code = 200
        return response
    return app
