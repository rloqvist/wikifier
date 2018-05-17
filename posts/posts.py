from database.database import db, Post, Comment, Vote, Tag
from posts.tags import add_tags_to_post
from time import time

def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        return False
    return post

def create_post(user_id, title, content, tags):
    post = Post.query.filter_by(title=title).first()

    if post:
        return False

    post = Post(user_id, title, content)

    post.updated = int(time())

    add_tags_to_post(post, tags)

    db.session.add(post)
    db.session.commit()

    return post.id

def update_post(post_id, content):
    post = Post.query.filter_by(id=post_id).first()

    post.content = content

    post.updated = int(time())

    db.session.commit()

def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if not post:
        return False

    votes = Vote.query.filter_by(post_id=post_id).all()
    comments = Comment.query.filter_by(post_id=post_id).all()

    for vote in votes:
        db.session.delete(vote)

    for comment in comments:
        db.session.delete(comment)

    db.session.delete(post)
    db.session.commit()

    return post_id

def list_posts():
    posts = Post.query.filter().all()
    return posts
