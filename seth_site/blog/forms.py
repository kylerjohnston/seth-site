from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import InputRequired
from ..models import Post
import re

class PostForm(Form):
    title = StringField('Title', validators = [InputRequired()])
    content = TextAreaField('Post', validators = [InputRequired()])
    submit = SubmitField('Submit')

    def validate_title(self, field):
        slugify = re.sub(r'[^\w\s]', '', field.data)
        slug = '-'.join(slugify.lower().split())
        if Post.query.filter_by(slug = slug).first():
            raise ValidationError('Title already exists.')
