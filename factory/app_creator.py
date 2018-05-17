from server_config import debug, sqlite_uri
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def init_app(name):

    app = Flask(name)

    app.config['DEBUG'] = debug
    app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = "secret"
    
    db = SQLAlchemy(app)

    return app
