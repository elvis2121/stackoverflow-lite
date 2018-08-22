import os
from flask import Flask, abort, jsonify,make_response
from flask_restful import Api, Resource, reqparse, fields, marshal

from instance.config import APP_CONFIG
from app.models.model import Questions, Answers

question = Questions()
answer = Answers()




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

    class QuestionListAPI(Resource):
        """defines the POST and GET all question routes"""

        def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument('title', type=str, required=True,
                                       help='No question title provided',
                                       location='json')
            self.reqparse.add_argument('description', type=str, default="",
                                       location='json')
            super(QuestionListAPI, self).__init__()


        def get(self):
            """Defines the GET all questions route"""
            res = question.get_all()
            return (res), 200

        def post(self):
            """Defines the POST a question route"""
            args = self.reqparse.parse_args()
            title = args["title"]
            description = args["description"]

            res = question.post_question(title, description)
            return (res), 201


    class QuestionAPI(Resource):
        """Defines the GET,PUT,DELETE questions by ID routes"""

        def __init__(self):
            self.reqparse = reqparse.RequestParser()
            # self.reqparse.add_argument('id', type=int, location='json')
            self.reqparse.add_argument('title', type=str, location='json')
            self.reqparse.add_argument('description',
                                       type=str, location='json')

            super(QuestionAPI, self).__init__()

        def get(self, question_id):
            """Defines the GET question by ID route"""

            res = question.get_single_question(question_id=question_id)
            return (res), 200

        def put(self, question_id):
            args = self.reqparse.parse_args()
            title = args["title"]
            description = args["description"]
            res = question.update_a_question(question_id, title, description)
            return (res), 200

        def delete(self, question_id):
            res = question.delete(question_id)
            return (res), 200

    class AnswerAPI(Resource):
        """Defines the answer a question route"""

        def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument('description', required=True,
                                       type=str, location='json')
            super(AnswerAPI, self).__init__()

        def put(self, answer_id):
            args = self.reqparse.parse_args()
            description = args["description"]
            res = answer.post_answer(answer_id, description)
            return res

    api.add_resource(QuestionListAPI, '/api/v1/questions',
                     endpoint='questions')
    api.add_resource(QuestionAPI, '/api/v1/questions/<int:question_id>')
    api.add_resource(AnswerAPI, '/api/v1/questions/<int:answer_id>/answers')
    return app
