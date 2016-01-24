from manage import app
from flask import render_template
from seth_site import freezer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/issues/')
def platform():
    return render_template('issues.html')

@freezer.register_generator
def error_handlers():
    yield '/404/'
