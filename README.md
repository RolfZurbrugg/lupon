
# Installation

```bash
pacuar -S postgresql
sudo useradd lupon
su lupon
```

```bash
git clone https://github.com/RolfZurbrugg/lupon.git
cd lupon
```

```bash
virtualenv -p python3 venv
cd venv
scource bin/activate
```

```bash

cd lupon
pip install --editable .
```

```bash
## run Luopn
export FLASK_APP=lupon
flask run
```

# Configuration
```bash
cp config-example.py config.py
```

```python
# DATABASE Connection
SQLALCHEMY_DATABASE_URI = 'postgresql://127.0.0.1/lupon'
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
#Dependencies
* Flask
* Flask-Babel
* Flask-Mail
* Flask-Cache
* Flask-WTF
* Flask-Login
* requests
## Database
* Psycopg2
* Flask-SQLAlchemy
* Flask-Migrate


# PostgreSQL
```bash
initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'
sudo -u postgres -i
# add current user to psql
createuser --interactive <flask user>
# create database lupon
createdb lupon
# drop database lupon 
dropdb lupon
```

```bash
python 
>>> from lupon import db
>>> db.create_all()
>>> quit()
```
