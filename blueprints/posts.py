from flask import Blueprint, jsonify, request, redirect, url_for
from flask import render_template as render
from flask_login import login_required, current_user
from markdown import markdown

from posts.posts import create_post, get_post, delete_post, update_post

post_pages = Blueprint('post_pages', __name__, template_folder='templates')

@post_pages.route('/post', methods=['GET', 'POST'])
def onCreatePost():
    if request.method == 'POST':

        title = request.form.get('title')
        content = request.form.get('content')

        user_id = current_user.id

        post_id = create_post(user_id, title, content)

        return redirect(url_for('post_pages.onViewPost', post_id=post_id))
    else:
        return render('create_post.html')

@post_pages.route('/post/<int:post_id>')
def onViewPost(post_id):

    post = get_post(post_id)

    if not post:
        return redirect('/post')

    data = {
        'title': post.title,
        'content': markdown(post.content),
        'post_id': post_id,
    }

    return render('view_post.html', **data)

@post_pages.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def onEditPost(post_id):
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        update_post(post_id, title, content)

        return redirect(url_for('post_pages.onViewPost', post_id=post_id))
    else:
        post = get_post(post_id)

        if not post:
            return redirect('/post')

        data = {
            'title': post.title,
            'content': post.content,
            'post_id': post_id,
        }

        return render('edit_post.html', **data)

@post_pages.route('/post/<int:post_id>/remove')
def onRemovePost(post_id):
    assert delete_post(post_id) == post_id
    return redirect('/')
