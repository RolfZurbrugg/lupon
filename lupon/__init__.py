# __init__.py

import os

from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse, Api
from flask_mail import Mail
from flask_babel import Babel, gettext
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    babel.init_app(app)
    mail.init_app(app)
    api = restful.Api(app)
    return app

# Flsk-SQLAlchemy
db = SQLAlchemy()

# flask-restful
api = restful.Api()
 
# flask-httpauth
auth = HTTPBasicAuth()

# Flask-Babel
babel = Babel()

# Flask-Mail
mail = Mail()

# Init lupon
app = create_app()
app.app_context().push()

# flask-bcrypt
flask_bcrypt = Bcrypt(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


from lupon import views
