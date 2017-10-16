import os """tests"""
import sqlite3
from flask import Flask, render_template, request, session, g

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)


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
    """ DOC String
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
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
    return render_template('customers.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.jinja')

@app.route('/customers')
def customers():
    return render_template('customers.jinja')

@app.route('/add', methods=['POST'])
def add_user():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into users (username, password) values (?, ?)'
                [request.form['username'], request.form['text']])
    db.commit
    flash('New User  successfully registered')
    return redirect(url_for('login.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('flaskr.show_entries'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
