'''
This module contains all classes requeried for Database Model

'''
from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, JSON, Boolean, Unicode, DateTime, Table
import requests
import datetime
from flask import g
from flask_login import UserMixin
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr, has_inherited_table, declarative_base
from lupon import app, flask_bcrypt, db


association_table = Table('workpackage_task',db.Model.metadata,
    Column('workpackage_id', Integer, ForeignKey('workpackage.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
 )


class CustomBase(object):
    ''' Define base atribuetes for all table '''
    
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime(timezone=False), default=datetime.datetime.utcnow)
    modify_date = Column(DateTime(timezone=False))
    create_by = Column(String(256), default="system")
    modify_by = Column(String(256))

    def get_id(self):
        return self.id

    def add(self):
        try:
            self.create_date(datetime.datetime.utcnow)
            db.session.add(self)
            db.session.commit()

        except Exception as e:
            return e

        return
    
    def update(self):
        try:
            self.modify_date(datetime.datetime.utcnow)
            db.session.commit()

        except Exception as e:
            return e

        return

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

        except Exception as e:
            return e

        return self



class User(db.Model, UserMixin):
   
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    email = Column(
            String(100), 
            unique=True, 
            nullable=False
    )
    password = Column(
            String(100),
            nullable=False                              
    )

    username = Column(
            String(100),
            nullable=False
    )

    firstname = Column(String(100))
    lastname= Column(String(100))
    street = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    number = Column(String(100))
    zip_code = Column(String(100))
    workpakages = relationship('Workpackage', backref='user', lazy=True)
    contacts = relationship('Contact', backref='user', lazy=True)



    '''
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
    '''
    def __repr__(self):
        return '<User %r>' % self.email

    def email_exists(self):
        if db.session.query(User.id).filter_by(email=self.email).scalar() is not None:
            return False
        else:
            return True

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(db.or_(
            User.username == login, User.email == login)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def get_name(self):
        return str(self.username)


class Contact(db.Model, CustomBase):
    ''' Contact Contact Datatable '''
    __tablename__ = 'contact'
    is_active = Column(Boolean)
    firstname = Column(String(256), nullable=False)
    lastname = Column(String(256), nullable=False)
    email = Column(String(256))
    phone = Column(String(256))
    mobile = Column(String(256))
    fax = Column(String(256))
    title = Column(String(256))
    sex = Column(String(256))
    hompage = Column(String(256))
    company = Column(String(256))
    discount = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    adresses = relationship('Location', backref='contact', lazy=True)

    def __repr__(self):
        ''' DEBUG PRINT OUTPUT'''
        return '<Contact %r>' % (self.firstname+" "+self.lastname)
    
    @classmethod
    def get_all(cls, user_id):
        return Contact.query.filter_by(user_id=user_id).all() 

class Location(db.Model, CustomBase):
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
    street = Column(String(256))
    streetNumber = Column(Integer)
    city = Column(String(256))
    state = Column(String(256))
    zip_code = Column(String(256))
    #coordinates = Column(JSON)
    #customer_id = Column(Integer, ForeignKey('customer.id'))
    #user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact.id'), nullable=False)

    def __repr__(self):
        pass

    def __init__(self, street, city, plz, contact_id):
        self.street = street
        self.city = city
        self.plz = plz
        self.coordinates = self.get_cordiantes()


class Workpackage(db.Model, CustomBase):
    
    __tablename__ = 'workpackage'
    name = Column(String(256))
    description = Column(Text)
    due_date = Column(DateTime())
    start_date = Column(DateTime())
    status = Column(String(256))
    location_id = Column(Integer, ForeignKey('location.id'))
    discoutn = Column(Float)
    priority = Column(String(256))
    comment = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    contact_id = Column(Integer, ForeignKey('contact.id'))
    tasks = relationship('Workpackage', secondary=association_table)
    

    def total_houres(self):
        pass

    def total_value(self):
        pass

    def get_work_packages(self):
        #load all workpakages linked to this task
        pass

class Task(db.Model, CustomBase):

    __tablename__ = 'task'
    name = Column(String(256)) #Name of the shit
    amount = Column(Float)  #How much shit
    unit = Column(String(256))  #Unit of shit
    description = Column(Text) # Shiti descripion
    value = Column(Float) #Cost of shit
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    @classmethod
    # get all task filtered by user_id
    def get_all(cls, user_id):
        return Task.query.filter_by(user_id=user_id).all()