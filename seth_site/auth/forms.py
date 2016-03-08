from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class LoginForm(Form):
    username = StringField('Username', validators = [
        InputRequired(),
        Length(1, 64)
    ])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Log in')

class SettingsForm(Form):
    username = StringField('Username', validators = [
        InputRequired(),
        Length(1, 64)])
    name = StringField('Name', validators = [InputRequired()])
    email = StringField('Email', validators = [InputRequired(), Email()])
    new_password = PasswordField('New password',
                                 validators = [
                                     EqualTo('password_verification',
                                             message = 'Passwords must match.')])
    password_verification = PasswordField('Verify new password')
    password = PasswordField('Current password', validators = [InputRequired()])
    submit = SubmitField("Apply changes")
