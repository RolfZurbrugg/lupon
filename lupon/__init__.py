# __init__.py
from flask import Flask
from flask_babel import Babel, gettext
from .extensions import babel, mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

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


# flask-bcrypt
flask_bcrypt = Bcrypt(app)

# LOAD VIEWS
from lupon import views, models
