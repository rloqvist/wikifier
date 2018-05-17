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

def list_posts():
    posts = Post.query.filter().all()
    print('posts', posts)
    return posts
