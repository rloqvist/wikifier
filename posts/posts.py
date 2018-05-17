from database.database import db, Post

def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        return False
    return post

def create_post(title, content):
    post = Post(title, content)

    db.session.add(post)
    db.session.commit()

    return post.id
