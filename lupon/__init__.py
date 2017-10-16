# __init__.py
from flask import Flask
from flask_babel import Babel, gettext
from .extensions import db, babel, mail

app = Flask(__name__)
app.config.from_object('config')

# INIT EXTENSIONS
babel.init_app(app)
db.init_app(app)
mail.init_app(app)

# LOAD VIEWS
from lupon import views, models
