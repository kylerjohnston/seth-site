#!/usr/bin/env python

from seth_site import app
from flask.ext.script import Manager
import os
from config import config

manager = Manager(app)
basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    manager.run()

