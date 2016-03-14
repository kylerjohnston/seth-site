from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.assets import Environment
from .bundles import css_all, js_all

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
assets = Environment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    assets.init_app(app)
    assets.register('css_all', css_all)
    assets.register('js_all', js_all)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth
    app.register_blueprint(auth, url_prefix = '/auth')

    from .blog import blog
    app.register_blueprint(blog, url_prefix = '/blog')

    return app
