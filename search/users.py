from database.database import db, User
from difflib import SequenceMatcher

def search(term):
    users = User.query.all()

    found = list()

    for user in users:
        if SequenceMatcher(None, term, user.username).ratio() >= 0.6:
            found.append(user)

    return found
