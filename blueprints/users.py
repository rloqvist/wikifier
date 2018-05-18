from flask import Blueprint, jsonify, request, redirect, url_for
from flask import render_template as render
from flask_login import login_required, current_user
from markdown import markdown
import json

from users.users import create_user, change_password, make_admin

user_pages = Blueprint('user_pages', __name__, template_folder='templates')

@user_pages.route("/user_settings")
def onUserSettings():
    return render("user_settings.html")

@user_pages.route("/user/create", methods=['POST'])
def onCreateUser():
    username = request.form.get('username')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')

    if not pass1 == pass2 or not username:
        return redirect(url_for('user_pages.onUserSettings'))

    password = pass1

    user_id = create_user(username, password)

    assert user_id

    return redirect(url_for('user_pages.onUserSettings'))


@user_pages.route("/user/password", methods=['POST'])
@login_required
def onUserPassword():
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')

    if not pass1 == pass2:
        return redirect(url_for('user_pages.onUserSettings'))

    password = pass1

    user_id = change_password(current_user.id, password)

    assert user_id == current_user.id

    return redirect(url_for('user_pages.onUserSettings'))


@user_pages.route("/user/admin", methods=['POST'])
@login_required
def onUserAdmin():
    username = request.form.get('username')

    if not username:
        return redirect(url_for('user_pages.onUserSettings'))

    user_id = make_admin(username)

    assert user_id

    return redirect(url_for('user_pages.onUserSettings'))
