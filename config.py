import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testing.db')
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config = {
    'dev': DevelopmentConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
}
