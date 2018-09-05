"""This is models.py file"""
#from . import DB


class Questions():
    '''class to represent question and answer model'''

    def get_all(self):
        '''return all questions from ALL_QUESTIONS dictionary'''
        query = "SELECT * from questions"
        result = DB.execute(query)

        return "all questions in db are {}".format(result)

    def post_question(self, title, description):
        """ insert new record"""
        query = "INSERT INTO questions(title,description) \
                 VALUES ('{}','{}')" . format(title, description)
        DB.execute(query)

        return "question created successfully"
