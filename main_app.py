from flask import Flask
from flask import request, redirect, url_for, jsonify
from flask import render_template as render
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from factory.app_creator import init_app
from users.users import get_user, get_user_with_username, create_user, should_login
from posts.posts import list_posts
from posts.timing_helper import calculate_time_ago
from posts.tags import list_tags

from blueprints.posts import post_pages

app = init_app(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)

@app.route('/login', methods=['GET', 'POST'])
@login_manager.unauthorized_handler
def onLogin():
    if request.method == "GET":
        return render("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    status = should_login(username, password)

    if status:
        user = get_user_with_username(username)
        login_user(user)

    return redirect("/")

@app.route("/logout")
@login_required
def onLogout():
    logout_user()
    return redirect("/")

@app.route('/')
@login_required
def onHome():
    posts = list_posts()

    data = {
        'posts': posts,
        'time_ago': calculate_time_ago,
    }

    return render('index.html', **data)

@app.route('/tags/list')
def onListTags():
    results = list()
    for tag in list_tags():
        result = {
            'name': tag.name,
            'value': tag.name,
            'text': tag.name,
        }
        results.append(result)

    data = {
        'success': True,
        'results': results,
    }

    return jsonify(data)


app.register_blueprint(post_pages)

if __name__ == '__main__':
    admin_user = create_user('admin', 'admin', admin=True)
    app.run()
