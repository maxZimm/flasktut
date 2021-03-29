from os import environ, path
from dotenv import load_dotenv
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config():
    DEBUG=False
    TETING=False
    CSRF=False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')    

class ProductionConfig(Config):
    DEBUG=False

class StagingConfig(Config):
    DEBUG=True
    DEVELOPMENT=True

class DevConfig(Config):
    DEBUG=True
    DEVELOPMENT=True

class TestingConfig(Config):
    TESTING=True
