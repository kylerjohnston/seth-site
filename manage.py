#!/usr/bin/env python

from seth_site import app, freezer
from flask.ext.script import Manager
import os
from config import config

manager = Manager(app)
basedir = os.path.abspath(os.path.dirname(__file__))

@manager.command
def build():
    app.config.from_object(config['production'])
    freezer.freeze()

if __name__ == '__main__':
    manager.run()

