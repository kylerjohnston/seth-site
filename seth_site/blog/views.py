from . import blog
from flask import render_template

@blog.route('/admin')
def admin():
    return render_template('blog/admin.html')
