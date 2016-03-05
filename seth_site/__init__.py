from flask import Flask
from flask_frozen import Freezer
from config import config
from .main import main as main_blueprint

freezer = Freezer()

app = Flask(__name__)
app.config.from_object(config['dev'])
config['dev'].init_app(app)
freezer.init_app(app)
app.register_blueprint(main_blueprint)
