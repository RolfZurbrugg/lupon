'''
--> RENAME AS config.py
'''
# -*- coding: utf-8 -*-
# available languages
LANGUAGES = {
    'en': 'English',
    'de': 'German',
    'ko': 'Korean'
}
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'

# DEGUB
DEBUG = True

# WTForms
SECRET_KEY = 'real_secret_key' #WTF Form require secret key -> TO BE CHANGES PLZ

# GOOGLE API KEY
GOOGLE_API_KEY = 'AIzaSyCuubDZxrnuw5KQPXrv0uleU32pFKye-7Y'

# Flask-Bcrypt
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension

# DATABASE Connection
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://lupon:lupon@localhost/lupon2'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# Mail
MAIL_FROM_EMAIL = "[email protected]" # For use in application emails

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'MAIL_USERNAME'
MAIL_PASSWORD = 'MAIL_PASSWORD'
