"""configuration file for the questions app"""


class Config():
    """The base class for configs"""
    DEBUG = True



class DevelopmentConfig(Config):
    """Defines the development environment configuration"""
    DEBUG = True


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
