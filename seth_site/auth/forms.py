from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class LoginForm(Form):
    username = StringField('Username', validators = [
        InputRequired(),
        Length(1, 64)
    ])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Log in')
