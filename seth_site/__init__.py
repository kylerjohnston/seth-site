from flask import Flask
from flask_frozen import Freezer
from config import config

freezer = Freezer()

app = Flask(__name__)
app.config.from_object(config['dev'])
config['dev'].init_app(app)
freezer.init_app(app)

import seth_site.views
import seth_site.errors
