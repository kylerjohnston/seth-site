class Config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
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
