"""Run this file to start the application"""
import os

from app.routes.route import create_app


config_name = os.environ.get('FLASK_ENV')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()