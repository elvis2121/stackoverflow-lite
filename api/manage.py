import os
from psycopg2 import connect


class Database(object):

    def __init__(self, app_config):
        self.dbname = os.getenv('APP_DATABASE')
        self.user = os.getenv('APP_USER')
        self.password = os.getenv('APP_PASSWORD')
        self.host = os.getenv('APP_HOST')
        print("...Establishing connection to database server...")
        self.connection = connect(database=self.dbname, user=self.user,
                                  host=self.host, password=self.password)
        self.connection.autocommit = True
        print("Connected.")

    def create_all(self):
        print("... starting creation of tables and relationship")
        commands = (
            'CREATE TABLE IF NOT EXISTS users (user_id serial PRIMARY KEY, \
                        username varchar(255), \
                        email varchar(50) NOT NULL, \
                        password varchar(255) NOT NULL, \
                        user_type varchar(255) NOT NULL,\
                        UNIQUE(email))',

            'CREATE TABLE IF NOT EXISTS questions (question_id serial PRIMARY KEY, \
                       owner_id serial, \
                       title varchar(255), \
                       description varchar(255), \
                       FOREIGN KEY (owner_id) REFERENCES users(user_id) on delete cascade)',

            'CREATE TABLE IF NOT EXISTS answers (answer_id serial PRIMARY KEY,\
                       question_id serial,\
                       user_id serial,\
                       description varchar(255) NOT NULL, \
                       FOREIGN KEY (question_id) REFERENCES questions(question_id) on delete cascade, \
                       FOREIGN KEY (user_id) REFERENCES users(user_id) on delete cascade)')

        try:
            cursor = self.connection.cursor()
            # create table one by one
            print("Creating relations")
            for command in commands:
                cursor.execute(command)
            # close communication with the PostgreSQL database server
            cursor.close()
            print("connection closed successfully.")
        except (Exception) as error:
            print(error)

    def drop_all(self):
        commands = (
            'DROP TABLE "users" CASCADE',
            'DROP TABLE "questions" CASCADE')
        try:
            cursor = self.connection.cursor()
            # drop table one by one
            print("Deleting relations")
            for command in commands:
                cursor.execute(command)
            # close communication with the PostgreSQL database server
            cursor.close()
            print("Done.")
        except (Exception) as error:
            print(error)

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor

    def __del__(self):
        # close connectin to the database
        self.connection.close()


if __name__ == '__main__':
    print("This file needs to be imported and linked with app configuration file.")
