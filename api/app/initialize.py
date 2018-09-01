"""app initilization"""

import os
from flask import Flask, make_response, jsonify
from flask_restful import Api
from app.route import QuestionListAPI, QuestionAPI, AnswerAPI

from instance.config import APP_CONFIG


def create_app(config_name):
    """app initialization"""

    app = Flask(__name__, instance_relative_config=True,
                instance_path=os.environ.get('INSTANCE_PATH'))
    app.config.from_object(APP_CONFIG[config_name])
    api = Api(app)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify(
            {'error': 'the resource requested was not found'}), 404)

    api.add_resource(QuestionListAPI, '/api/v1/questions',
                     endpoint='questions')
    api.add_resource(QuestionAPI, '/api/v1/questions/<int:question_id>')
    api.add_resource(AnswerAPI, '/api/v1/questions/<int:answer_id>/answers')
    return app
