from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from seth_site import login_manager
from flask_login import UserMixin
from markdown import markdown
import bleach
import re

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='user')
    name = db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, unique = True)
    date = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)
    tags = db.Column(db.String)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content_html = db.Column(db.Text)
    slug = db.Column(db.String)
    link_url = db.Column(db.String)
    link_description = db.Column(db.String)
    link_title = db.Column(db.String)

    @staticmethod
    def on_changed_body(target, value, old_value, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.content_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

    @staticmethod
    def on_changed_title(target, value, oldvalue, initiator):
        stripped = re.sub(r'[^\w\s]', '', value)
        slug = '-'.join(stripped.lower().split())
        target.slug = slug

    def __repr__(self):
        return '<Post {}>>'.format(self.title)

db.event.listen(Post.content, 'set', Post.on_changed_body)
db.event.listen(Post.title, 'set', Post.on_changed_title)
