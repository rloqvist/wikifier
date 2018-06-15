from database.database import db, Comment
from difflib import SequenceMatcher

def search(term):
    comments = Comment.query.all()

    found = list()

    for comment in comments:
        if not comment.content:
            continue
        elif term in comment.content.lower():
            found.append(comment)
        elif SequenceMatcher(None, term, comment.content).ratio() >= 0.6:
            found.append(comment)

    return found
