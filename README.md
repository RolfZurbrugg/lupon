# LuponCRM

## Requirements

- python3
- virtualenv
- git
- PostgreSQL or MySQL

## Installation

```bash
sudo useradd lupon
su lupon
```

```Bash
virtualenv -p python3 venv
cd venv
scource bin/activate
```

```Bash
git clone https://github.com/RolfZurbrugg/lupon.git
cd lupon
pip install --editable .
```

### Run Application

```shell
export FLASK_APP=lupon
flask run
```

### Run in Developer mode

````shell
python run.py
````

## Configuration

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

### Database

```Bash
sudo yum -y install mysql
mysql -u root -p
```

```sql
CREATE DATABASE lupon;
CREATE USER lupon@localhost IDENTIFIED BY 'lupon';
GRANT ALL PRIVILEGES ON  lupon to 'lupon'@'localhost'
```

```Python
from lupon import app, db

db.create_all()
```

```bash
pacuar -S postgresql
sudo useradd lupon
su lupon
```

#### PostgreSQL

Create Database and Database User

```bash
## ARCHLinux spesific??
initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'
sudo -u postgres -i
# add user to psql
createuser --interactive lupon
# create database lupon
createdb lupon
# drop database lupon
dropdb lupon
```

Verify:

```bash
psql -U lupon -d lupon -h 127.0.0.1 -W
```

## Dependencies

* Flask
* Flask-Babel
* Flask-Mail
* Flask-Cache
* Flask-WTF
* Flask-Login
* requests
* ...
## Database
* Psycopg2
* Flask-MySQLdb
* Flask-SQLAlchemy
* Flask-Migrate


## Documentation References

### Plugins
* Flask: http://flask.pocoo.org/docs/0.12/
* Flask-SQLAlchemy: http://flask-sqlalchemy.pocoo.org/2.3/
* WTForms: https://wtforms.readthedocs.io/en/latest/index.html
* Flask-WTF: https://flask-wtf.readthedocs.io/en/stable/index.html
* Flask-Babel: https://pythonhosted.org/Flask-Babel/
* SQLAlchemy: http://docs.sqlalchemy.org/en/latest/orm/index.html
* Twitter Bootstrap: https://getbootstrap.com/docs/4.0/getting-started/introduction/
* Jinja2 (Templateing): http://jinja.pocoo.org/docs/2.9/templates/#
* Flask-Login: http://flask-login.readthedocs.io/en/latest/

### HowTos & Tutorials
* Example Flask Project(Template): https://github.com/xen/flask-project-template
* Flask Example Projekct: https://github.com/imwilsonxu/fbone
* Flask by Example: https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
* Flask Mega Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* GoogleMaps API: https://developers.google.com/maps/documentation/javascript/tutorial
* Explore Flask: http://exploreflask.com/en/latest/index.html

### Snippets
* Flask-WTF Tricks: https://goonan.io/flask-wtf-tricks/

### Product Backlog
Florian
* Send eMail on user registration
* Administrator Interface
* Customer management

Rolf
* Offer creation page
    * AJAX
* Search functionaliy
    * Tasks
    * Customers
