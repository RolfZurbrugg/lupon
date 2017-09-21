#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

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
