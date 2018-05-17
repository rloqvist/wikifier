from flask import Flask
from flask import request, redirect, url_for
from flask import render_template as render
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from markdown import markdown

from factory.app_creator import init_app
from users.users import get_user, get_user_with_username, create_user, should_login

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
def index():
    return render('index.html')

if __name__ == '__main__':
    admin_user = create_user('admin', 'admin', admin=True)
    app.run()