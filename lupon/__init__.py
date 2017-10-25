# __init__.py
from flask import Flask
from flask_babel import Babel, gettext
from flask_login import LoginManager
from .extensions import babel, mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    babel.init_app(app)
    mail.init_app(app)
    return app


app = create_app()
app.app_context().push()
# INIT EXTENSIONS

# flask-bcrypt
flask_bcrypt = Bcrypt(app)

from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "login"

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()



# LOAD VIEWS
from lupon import views, models
