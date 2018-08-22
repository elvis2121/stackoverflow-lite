
"""This is models.py file"""
ALL_QUESTIONS = {1: {"title": "how do i use ORMs?",
                     "description": "i want to connect to database..."},
                 2: {"title": "android apps",
                     "description": "how do i build android apps?"}}
ANSWERS = {1: {"description": "first instantiate the class and use methods"}}


class Questions():
    '''class to represent question and answer model'''

    def get_all(self):
        '''return all questions from ALL_QUESTIONS dictionary'''

        return ALL_QUESTIONS


    def get_single_question(self, question_id):
        '''get single question from ALL_QUESTIONS using id'''
        if question_id in ALL_QUESTIONS:
            return ALL_QUESTIONS[question_id]
        return {"message": "question requested not available"}


    def update_a_question(self, question_id, title, description):
        '''update an existing question'''
        if question_id not in ALL_QUESTIONS:
            return {"message": "cannot update a non existing question"}
        ALL_QUESTIONS[question_id]["title"] = title
        ALL_QUESTIONS[question_id]["description"] = description
        return ALL_QUESTIONS



    def post_question(self, title, description):
        '''add a question to ALL_QUESTIONS'''
        new_id = len(ALL_QUESTIONS) + 1
        ALL_QUESTIONS[new_id] = {"title": title, "description": description}
        return ALL_QUESTIONS


    def delete(self, question_id):
        '''delete a question by its id'''
        if question_id in ALL_QUESTIONS:
            del ALL_QUESTIONS[question_id]
            return {"message": "Question deleted"}

        return {"message": "Question you are trying to delete doesn't exist"}


class Answers():
    """ class to represent answer model"""

    def post_answer(self, answer_id, description):
        '''add a question to ALL_QUESTIONS'''
        if answer_id in ANSWERS:
            ANSWERS["description"] = description
            return ANSWERS
        return {"message": "cannot update a non existing answer"}
