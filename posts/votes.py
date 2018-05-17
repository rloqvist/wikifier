from database.database import db, Vote

def vote(post_id, user_id):
    vote = Vote.query.filter_by(post_id=post_id, user_id=user_id).first()
    if vote:
        db.session.delete(vote)
    else:
        vote = Vote(post_id=post_id, user_id=user_id)
        db.session.add(vote)
    db.session.commit()
    return vote.id

def has_voted(post_id, user_id):
    vote = Vote.query.filter_by(post_id=post_id, user_id=user_id).first()
    if vote:
        return True
    return False
