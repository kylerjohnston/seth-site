from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='user')

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
    title = db.Column(db.String)
    date = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)
    tags = db.Column(db.String)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>>'.format(self.title)
