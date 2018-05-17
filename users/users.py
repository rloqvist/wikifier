from database.database import db, User

def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return False
    return user

def get_user_with_username(username):
    username = username.lower()
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    return user

def should_login(username, password):
    user = get_user_with_username(username)
    if user:
        return user.check_password(password)
    return False

def list_users():
    users = User.query.filter().all()
    if not users:
        return []
    return users

def create_user(username, password, admin=False):
    username = username.lower()

    if get_user_with_username(username):
        return False

    user = User(username=username, password=password)
    user.set_admin(admin)

    db.session.add(user)
    db.session.commit()

    return user.id

def delete_user(user_id):
    if not user_id:
        return False

    user = User.query.filter_by(id=user_id).first()

    if not user:
        return False

    db.session.delete(user)
    db.session.commit()

    return True
