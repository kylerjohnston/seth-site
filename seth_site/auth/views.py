from . import auth
from .forms import LoginForm, SettingsForm
from ..models import User
from flask_login import login_user, login_required, logout_user
from flask import redirect, url_for, render_template, flash
from .. import db

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('blog.root'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form = form)

@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/settings/<userid>', methods = ['GET', 'POST'])
@login_required
def settings(userid):
    user = User.query.get_or_404(int(userid))
    form = SettingsForm()
    if form.validate_on_submit():
        if user.verify_password(form.password.data):
            user.username = form.username.data
            user.name = form.name.data
            user.email = form.email.data
            if form.new_password.data != '':
                user.password = form.new_password.data
            db.session.add(user)
            db.session.commit()
            flash('Your user settings have been updated.')
            return redirect(url_for('main.index'))
        flash('Invalid username or password.')
    form.username.data = user.username
    form.name.data = user.name
    form.email.data = user.email
    return render_template('auth/settings.html',
                           form = form)

