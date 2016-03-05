#!/usr/bin/env python

from seth_site import create_app
from flask.ext.script import Manager
import os
from config import config

app = create_app(os.getenv('SETHSITE_CONFIG') or 'default')
manager = Manager(app)
basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    manager.run()

