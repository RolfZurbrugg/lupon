# Installation
```shell
virtualenv -p python3 flask
cd flask
scource bin/activate
```

```shell
git clone https://github.com/RolfZurbrugg/lupon.git
cd lupon
pip install --editable .
```

```shell
## run Luopn
export FLASK_APP=lupon
flask run
```

# Configuration
```shell
cp config-example.py config.py
```

```python
# DATABASE Connection
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database'
```

```python
# Security
SECRET_KEY = 'real_secret_key'
# GOOGLE API KEY
# https://developers.google.com/maps/documentation/javascript/get-api-key?hl=de
GOOGLE_API_KEY = 'this-is-my-google-api-key'
```

```python
# Mail
MAIL_FROM_EMAIL = "no@addre.ss" # For use in application emails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'MAIL_USERNAME'
MAIL_PASSWORD = 'MAIL_PASSWORD'
```