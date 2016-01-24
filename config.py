class Config:
    FREEZER_RELATIVE_URLS = True
    FREEZER_DESTINATION_IGNORE = [
        '.gitignore',
        '.git/',
        '.htaccess'
    ]
    FREEZER_IGNORE_404_NOT_FOUND = True

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
