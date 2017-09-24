#!/usr/bin/python3

import os
import sqlite3
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'lupon.db'),
    SECRET_KEY=('lupon'),
    USERNAME='admin',
    PASSWORD='lupon'
))

app.config.from_envvar('LUPON_SETTINGS', silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


@app.route('/')
def index():
    return render_template('home.jinja')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.jinja')

@app.route('/customers')
def customers():
    return render_template('customers.jinja')

if __name__ == '__main__':
    app.run(debug=True)
