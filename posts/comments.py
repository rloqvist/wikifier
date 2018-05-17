from database.database import db, Comment
from time import time

def create_comment(post_id, user_id, content):
    comment = Comment(post_id=post_id, user_id=user_id, content=content)

    comment.updated = int(time())

    db.session.add(comment)
    db.session.commit()

    return comment.id

def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if not comment:
        return False

    print(comment)

    db.session.delete(comment)
    db.session.commit()

    return comment.id

def list_comments_for_post(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return comments
