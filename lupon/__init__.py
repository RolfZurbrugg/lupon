# __init__.py
from flask import Flask
from flask_babel import Babel
from flask_babel import gettext
from .extensions import babel
from .extensions import mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    babel.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    return app


app = create_app()
app.app_context().push()
# INIT EXTENSIONS

login_manager = LoginManager()
login_manager.init_app(app)

#@login_manager.user_loader
#def load_user(user_id):
#    return User.get(user_id)

# flask-bcrypt
flask_bcrypt = Bcrypt(app)

# LOAD VIEWS
from lupon import views, models
