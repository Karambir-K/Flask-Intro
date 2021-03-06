import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xa6(\xf7;j\x01Sv\xbc9\xac/|\x93\xa2\x03\xa4\x02,\xa82\x80\x83\xd5'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #export DATABASE_URL="postgresql://localhost/discover_flask_dev" --- to set our environment variable
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print SQLALCHEMY_DATABASE_URI


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False