from database.database import db, Post

def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        return False
    return post

def create_post(user_id, title, content):
    post = Post(user_id, title, content)

    db.session.add(post)
    db.session.commit()

    return post.id

def update_post(post_id, title, content):
    post = Post.query.filter_by(id=post_id).first()

    post.title = title
    post.content = content

    db.session.commit()

def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if not post:
        return False

    db.session.delete(post)
    db.session.commit()

    return post_id

def list_posts():
    posts = Post.query.filter().all()
    return posts
