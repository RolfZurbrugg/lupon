from flask import Flask, render_template
from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://lupon:lupon@localhost/lupon'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('userId', db.Integer, primary_key=True)
    userName = db.Column('userName', db.Unicode)
    password = db.Column('password', db.Unicode)



@app.route("/test")
def test():
    users = User.query.all()
    for u in users:
        print(u.data)
    return test

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/customers')
def about():
    return render_template('/customers.html')

@app.route('/login')
def login():
    return render_template('/login.html')



if __name__ == '__main__':
    app.run(debug=True)