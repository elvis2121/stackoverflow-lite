"""configuration file for the questions app"""
import os


class Config():
    """The base class for configs"""
    DEBUG = True
    CSRF_ENABLED = True
    DATABASE_NAME = os.getenv('APP_DATABASE')
    PASSWORD = os.getenv('APP_PASSWORD')
    HOST = os.getenv('APP_HOST')
    USER = os.getenv('APP_USER')


class DevelopmentConfig(Config):
    """Defines the development environment configs"""
    DEBUG = True
    DATABASE_NAME = os.getenv('APP_DATABASE')


class TestingConfig(Config):
    """Defines the testing environment configs"""

    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Defines the production environment configs"""
    DEBUG = False
    TESTING = False


APP_CONFIG = {'development': DevelopmentConfig, 'testing': TestingConfig,
              'production': ProductionConfig}
