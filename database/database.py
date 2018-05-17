from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from factory.app_creator import init_app

app = init_app(__name__)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    pw_hash = db.Column(db.String(160))
    posts = db.relationship("Post", backref="user")

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def set_admin(self, admin):
        self.admin = admin

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(200), unique=True)
    content = db.Column(db.String(10000))
    comments = db.relationship("Comment", backref="post")
    votes = db.relationship("Vote", backref="post")
    tags = db.relationship("Tag", backref="post")

    def __init__(self, user_id, title, content):
        self.user_id = user_id
        self.title = title
        self.content = content

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    content = db.Column(db.String(1000))

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    name = db.Column(db.String(30), unique=True)

db.create_all()
