from . import auth
from .forms import LoginForm
from ..models import User
from flask_login import login_user, login_required, logout_user
from flask import redirect, url_for, render_template, flash

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('blog.admin'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
