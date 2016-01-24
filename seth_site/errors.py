from seth_site import app
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error = '404'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error = '500'), 500
