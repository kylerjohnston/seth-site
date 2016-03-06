#!/usr/bin/env python

from seth_site import create_app, db
from seth_site.models import User, Post
from flask.ext.script import Manager, Shell
import os
from config import config

app = create_app(os.getenv('SETHSITE_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(
        app = app,
        db = db,
        User = User,
        Post = Post)

manager.add_command('shell',
                    Shell(make_context = make_shell_context))

if __name__ == '__main__':
    manager.run()

