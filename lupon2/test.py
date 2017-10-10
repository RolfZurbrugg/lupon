#!/usr/local/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lupon:lupon@localhost/lupon2'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('userId', db.Integer, primary_key=True)
    userName = db.Column('userName', db.Unicode)
    password = db.Column('password', db.Unicode)


class Test(db.Model):
    __tablename__ = 'Test'
    id = db.Column('id', db.Integer, primary_key=True)
    text = db.Column('text', db.Unicode)


test = Test.query.all()

test2 = Test.query.filter_by(id=1).first()
print(test2.text)

test3 = Test.query.first()
print(test3.text)

for t in test:
    print(t.text)

