import os
import sqlite3
from flask import Flask, render_template, request, session, g

app = Flask(__name__)
app.config.from_object(__name__)

# Configuration
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'lupon.db'),
    SECRET_KEY=('lupon'),
    USERNAME='admin',
    PASSWORD='lupon'
))

## FROM ENVIRONEMNT
app.config.from_envvar('LUPON_SETTINGS', silent=True)

# DB Functions
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
<<<<<<< HEAD
        g.sqlite_db connect_db()
=======
        g.sqlite_db = connect_db()
>>>>>>> caee197599a3f54600c6dbc90ea48d5d736e11ad
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.jinja')

@app.route('/customers')
def customers():
    return render_template('customers.jinja')

if __name__ == '__main__':
    app.run(debug=True)
