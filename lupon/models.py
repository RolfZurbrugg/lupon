'''
This module contains all classes requeried for Database Model

'''
from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, JSON, Boolean, Unicode

import requests

from flask import g

from wtforms.validators import Email
from sqlalchemy_utils import EmailType, PasswordType

from lupon import app, flask_bcrypt, db

''' DEV
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
END DEV '''

class User(db.Model):
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    email = Column(
        EmailType, 
        unique=True, 
        nullable=False, 
        info={
            'label': 'Name'  
        }
    )
    # name = Column(Unicode(100), nullable=False)
    password = Column(
        PasswordType(
            schemes=['pbkdf2_sha512']
            ),
        info={ 'label': 'Password' },
        nullable=False
    )
    # locations = relationship('Location', backref='user', lazy='dynamic')
     
    def __init__(self, email, password):
        self.email = email
        self.password = password
 
    def __repr__(self):
        return '<User %r>' % self.email

    def email_exists(self):
        if db.session.query(User.id).filter_by(name=self.email).scalar() is not None:
            return False
        else:
            return True

class Customer(db.Model):
    ''' Customer Contact Datatable '''
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean)
    firstname = Column(String(256), nullable=False)
    lastname = Column(String(256), nullable=False)
    email = Column(String(256))
    phone = Column(String(256))
    
    def __repr__(self):
        ''' DEBUG PRINT OUTPUT'''
        return '<Customer %r>' % (self.firstname+" "+self.lastname)

    def __init__(self, firstname, lastname, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        
class Location(db.Model):
    '''
     Methods defined here:

    __init__(self, firstname, lastname, email, phone, locations):
        initialize class
    
    __repr__(self)
        pass

    get_coordinates(self)
        // in developent
        GoogleMaps API Request to get geolocation data as JSON
         # address=1600+Amphitheatre+Parkway,+Mountain+View,+CA
    '''
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    street = Column(String(256))
    streetNumber = Column(Integer)
    city = Column(String(256))
    state = Column(String(256))
    plz = Column(String(256))
    # coordinates = Column(JSON)
    #customer_id = Column(Integer, ForeignKey('customer.id'))
    #user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        pass

    def __init__(self, street, city, plz, customer_id):
        self.street = street
        self.city = city
        self.plz = plz
        self.coordinates = self.get_cordiantes()

    def get_cordiantes(self):
       
        address = self.street+'+'+self.streeNumber+',+'+self.city+'+'+self.plz+',+'+self.state
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?'+address+'&'+app.config['GOOGE_API_KEY'])
        return response.json()

class Company(db.Model):
    ''' Add Company attributes if customer is a company '''
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    # employees = relationship('Customer', backref='employee')

    
    def __repr__(self):
        pass
    
    def __init__(self, parameter_list):
        pass


class Contract(object):
    pass

class Service(object):
    pass

class Task(object):
    pass
