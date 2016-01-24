from flask import render_template, Markup
from flask_flatpages import pygmented_markdown

def prerender_jinja(text):
    """ This function uses Jinja to prerender flatpages.
    Courtesy of
    http://stackoverflow.com/questions/21576520/mix-images-with-markdown-in-a-flask-app
    """
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

class Config:
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ROOT = 'content'
    FREEZER_RELATIVE_URLS = True
    FLATPAGES_HTML_RENDERER = prerender_jinja
    FREEZER_DESTINATION_IGNORE = [
        '.gitignore',
        '.git/'
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
