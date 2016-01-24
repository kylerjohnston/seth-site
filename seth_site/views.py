from manage import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/issues/')
def platform():
    return render_template('issues.html')
