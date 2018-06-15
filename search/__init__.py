from search.posts import search as search_posts
from search.users import search as search_users
from search.comments import search as search_comments

def search(term):
    results = {
        'posts': search_posts(term),
        'users': search_users(term),
        'comments': search_comments(term),
    }
    return results
