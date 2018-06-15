from flask import Blueprint
from flask import render_template as render
from markdown import markdown

from search import search

search_pages = Blueprint('search_pages', __name__, template_folder='templates')

@search_pages.route('/search/<string:term>')
def onSearch(term):

    results = search(term)

    data = {
        'term': term,
        'results': results,
        'markdown': markdown,
    }

    return render('search.html', **data)
