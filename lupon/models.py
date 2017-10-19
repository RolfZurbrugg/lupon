'''
This module contains all classes requeried for Database Model

'''
from sqlalchemy import Column, String, ForeignKey, Integer, JSON, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import requests


from lupon import app, db

''' DEV
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
END DEV '''
# Base = declarative_base()

class Contact(db.Model):
    ''' Contact Contact Datatable '''
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean)
    firstname = Column(String(256), nullable=False)
    lastname = Column(String(256), nullable=False)
    email = Column(String(256))
    phone = Column(String(256))
    # locations = relationship('Location', backref='contact', lazy='dynamic')
    
    def __repr__(self):
        ''' DEBUG PRINT OUTPUT'''
        return '<Contact %r>' % (self.firstname+" "+self.lastname)

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
    coordinates = Column(JSON)
    #contact_id = Column(Integer, ForeignKey('contact.id'))
    #company = relationship('Company', uselist=False, back_populates="location")

    def __repr__(self):
        pass

    def __init__(self, street, city, plz, contact_id):
        self.street = street
        self.city = city
        self.plz = plz
        self.coordinates = self.get_cordiantes()

    def get_cordiantes(self):
       
        address = self.street+'+'+self.streeNumber+',+'+self.city+'+'+self.plz+',+'+self.state
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?'+address+'&'+app.config['GOOGE_API_KEY'])
        return response.json()

class Company(db.Model):
    ''' Add Company attributes if contact is a company '''
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    #employees = relationship('Contact', backref='employee', lazy='dynamic')
    #location_id = Column(Integer, ForeignKey('location.id'))
    #location = relationship('Location', back_populates="company")
    
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
