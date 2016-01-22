from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from config import config

flatpages = Flatpages()
freezer = Freezer()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init(app)
    flatpages.init(app)
    freezer.init(app)

    import seth-site.views
    import seth-site.errors
