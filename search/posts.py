from database.database import db, Post
from difflib import SequenceMatcher

def search(term):
    posts = Post.query.all()

    found = list()

    for post in posts:
        if not post.title or not post.content:
            continue
        elif term in post.title.lower():
            found.append(post)
        elif term in post.content.lower():
            found.append(post)
        elif SequenceMatcher(None, term, post.title).ratio() >= 0.6:
            found.append(post)

    return found
