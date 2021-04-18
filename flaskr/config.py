class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "random secret key"
    DEBUG = True

class TestingConfig(DevelopmentConfig):
    SECRET_KEY = "random secret key for test"
    TESTING = True
