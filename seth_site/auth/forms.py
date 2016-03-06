from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class LoginForm(Form):
    username = StringField('Username', validators = [
        InputRequired(),
        Length(1, 64),
        Email()
    ])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Log in')
