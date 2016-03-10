import os
from env import *

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Defined in env.py
    SECRET_KEY = SECRET_KEY
    DB_USERNAME = DB_USERNAME
    DB_PASSWORD = DB_PASSWORD

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testing.db')
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + Config.DB_USERNAME + ':' + Config.DB_PASSWORD + '@localhost/' + config.DB_USERNAME
    DEBUG = False
    TESTING = False

config = {
    'dev': DevelopmentConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
}
