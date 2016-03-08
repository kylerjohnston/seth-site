from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, ValidationError
from wtforms.validators import InputRequired, DataRequired
from ..models import Post
import re

class PostForm(Form):
    title = StringField('Title', validators = [InputRequired()])
    content = TextAreaField('Post', validators = [InputRequired()])
    submit = SubmitField('Submit')

class DeleteForm(Form):
    checkbox = BooleanField('Definitely delete this post.',
                            validators = [DataRequired()])
    submit = SubmitField('Delete')
