### extension include 

from flask_mail import Mail
mail = Mail()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

from flask_babel import Babel
babel = Babel()

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

from flask_cache import Cache
cache = Cache()