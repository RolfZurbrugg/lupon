# __init__.py
from flask import Flask
from flask_babel import Babel, gettext
from .extensions import babel, mail
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push() # CONTEXT
app.config.from_object('config') # CONFIG
db = SQLAlchemy()

# INIT EXTENSIONS
babel.init_app(app)
db.init_app(app)
mail.init_app(app)

# LOAD VIEWS
from lupon import views, models
