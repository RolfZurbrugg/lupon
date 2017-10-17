# __init__.py
from flask import Flask
from flask_babel import Babel, gettext
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel
from flask_wtf.csrf import CSRFProtect
from flask_cache import Cache

app = Flask(__name__)
app.config.from_object('config')

# INIT EXTENSIONS
db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
babel = Babel(app)
csrf = CSRFProtect(app)
cache = Cache(app)

# LOAD VIEWS
from lupon import views, models
