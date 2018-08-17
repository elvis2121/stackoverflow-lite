import os
from flask import Flask,  abort
from flask_restful import Api, Resource, reqparse, fields, marshal

from instance.config import APP_CONFIG
from app.models.model import questions


def create_app(config_name):
    """app initialization"""

    app = Flask(__name__, instance_relative_config=True,
                instance_path=os.environ.get('INSTANCE_PATH'))
    app.config.from_object(APP_CONFIG[config_name])
    api = Api(app)

    question_fields = {
        'title': fields.String,
        'description': fields.String,
        'answered': fields.Boolean,
        'myanswer': fields.String,
        'uri': fields.Url('question')
    }

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
            return {'questions': [marshal(question, question_fields)
                                  for question in questions]}

        def post(self):
            """Defines the POST a question route"""

            args = self.reqparse.parse_args()
            question = {
                'id': questions[-1]['id'] + 1,
                'title': args['title'],
                'description': args['description'],
                'answered': False
            }
            questions.append(question)
            return {'question': marshal(question, question_fields)}, 201

    class QuestionAPI(Resource):
        """Defines the GET,PUT,DELETE questions by ID routes"""

        def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument('id', type=int, location='json')
            self.reqparse.add_argument('title', type=str, location='json')
            self.reqparse.add_argument('description',
                                       type=str, location='json')
            self.reqparse.add_argument('answered', type=bool, location='json')
            super(QuestionAPI, self).__init__()

        def get(self, id):
            """Defines the GET question by ID route"""
            question = [question for question in questions
                        if question['id'] == id]
            if not question:
                abort(404)
            return {'question': marshal(question[0], question_fields)}

        def put(self, id):
            """Defines the PUT question route"""
            question = [question for question in questions
                        if question['id'] == id]
            if not question:
                abort(404)
            question = question[0]
            args = self.reqparse.parse_args()
            for key, value in args.items():
                if value is not None:
                    question[key] = value
            return {'question': marshal(question, question_fields)}

        def delete(self, id):
            """Defines a method to DELETE a route"""
            question = [question for question in questions
                        if question['id'] == id]
            if not question:
                abort(404)
            questions.remove(question[0])
            return {'result': "you have successfully deleted the question"}

    class AnswerAPI(Resource):
        """Defines the answer a question route"""

        def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument('title', type=str, location='json')
            self.reqparse.add_argument('description',
                                       type=str, location='json')
            self.reqparse.add_argument('answered', type=bool, location='json')
            self.reqparse.add_argument('myanswer', type=str, location='json')
            super(AnswerAPI, self).__init__()

        def put(self, id):
            """Defines the route for answering a question"""
            question = [question for question in questions
                        if question['id'] == id]
            if not question:
                abort(404)
            question = question[0]
            args = self.reqparse.parse_args()
            for key, value in args.items():
                if value is not None:
                    question[key] = value
            return{'answer': marshal(questions, question_fields)}

    api.add_resource(QuestionListAPI, '/api/v1/questions',
                     endpoint='questions')
    api.add_resource(QuestionAPI, '/api/v1/questions/<int:id>',
                     endpoint='question')
    api.add_resource(AnswerAPI, '/api/v1/questions/<int:id>/answers',
                     endpoint='answers')
    return app
