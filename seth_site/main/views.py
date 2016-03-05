from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/issues/')
def platform():
    return render_template('issues.html')

@main.route('/contribute/')
def contribute():
    return render_template('contribute.html')

