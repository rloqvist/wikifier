from flask import Blueprint, jsonify, request, redirect, url_for
from flask import render_template as render
from flask_login import login_required, current_user

post_pages = Blueprint('post_pages', __name__, template_folder='templates')

@post_pages.route('/post', methods=['GET', 'POST'])
def onCreatePost():
    if request.method == 'POST':
        return redirect('/')
    return render('create_post.html')

@post_pages.route('/post/<int:post_id>')
def onViewPost(post_id):
    return redirect('/')

@post_pages.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def onEditPost(post_id):
    if request.method == 'POST':
        return redirect('/')
    return render('edit_post.html')
