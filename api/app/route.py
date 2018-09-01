"""app routes"""
from flask_restful import Api, response, reqparse

from app.model import Questions, Answers


question = Questions()
answer = Answers()


class QuestionListAPI(responseource):

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
        response = question.get_all()
        return (response), 200

    def post(self):
        """Defines the POST a question route"""
        args = self.reqparse.parse_args()
        title = args["title"]
        description = args["description"]

        response = question.post_question(title, description)
        return (response), 201


class QuestionAPI(responseource):
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

        response = question.get_single_question(question_id=question_id)
        return (response), 200

    def put(self, question_id):
        """Defines the edit a question route"""
        args = self.reqparse.parse_args()
        title = args["title"]
        description = args["description"]
        response = question.update_a_question(question_id, title, description)
        return (response), 200

    def delete(self, question_id):
        """Defines the delete a question route"""
        response = question.delete(question_id)
        return (response), 200


class AnswerAPI(responseource):
    """Defines the answer a question route"""

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('description', required=True,
                                   type=str, location='json')
        super(AnswerAPI, self).__init__()

    def put(self, answer_id):
        """Defines providing an answer route"""
        args = self.reqparse.parse_args()
        description = args["description"]
        response = answer.post_answer(answer_id, description)
        return response
