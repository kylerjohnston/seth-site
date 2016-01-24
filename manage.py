#!/usr/bin/env python

from seth_site import app, freezer
from flask.ext.script import Manager
import os
from config import config
import subprocess

manager = Manager(app)
basedir = os.path.abspath(os.path.dirname(__file__))

@manager.command
def build():
    app.config.from_object(config['production'])
    freezer.freeze()
    subprocess.run(['/usr/bin/tar', '-zcvf',
                    '{}/seth_site.tar.gz'.format(basedir),
                    '-C',
                    '{}/seth_site/build/'.format(basedir)])

if __name__ == '__main__':
    manager.run()

