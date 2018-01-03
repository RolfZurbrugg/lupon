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

# DEFAULTS
STRING_SIZE = 254

association_table = Table('workpackage_task', db.Model.metadata,
    Column('workpackage_id', Integer, ForeignKey('workpackage.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
)


class CustomBase(object):
    ''' Define base atribuetes for all table '''
    
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime(timezone=False), default=datetime.datetime.utcnow)
    modify_date = Column(DateTime(timezone=False))
    create_by = Column(String(STRING_SIZE), default="system")
    modify_by = Column(String(STRING_SIZE))

    def get_id(self):
        return self.id

'''     def add(self):
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

        return self '''


class User(db.Model, UserMixin):
   
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    email = Column(
            String(STRING_SIZE), 
            unique=True, 
            nullable=False
    )
    password = Column(
            String(STRING_SIZE),
            nullable=False                              
    )

    username = Column(
            String(STRING_SIZE),
            nullable=False
    )

    firstname = Column(String(STRING_SIZE))
    lastname= Column(String(STRING_SIZE))
    street = Column(String(STRING_SIZE))
    city = Column(String(STRING_SIZE))
    state = Column(String(STRING_SIZE))
    number = Column(String(STRING_SIZE))
    zip_code = Column(String(STRING_SIZE))
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
    firstname = Column(String(STRING_SIZE), nullable=False)
    lastname = Column(String(STRING_SIZE), nullable=False)
    email = Column(String(STRING_SIZE))
    phone = Column(String(STRING_SIZE))
    mobile = Column(String(STRING_SIZE))
    fax = Column(String(STRING_SIZE))
    title = Column(String(STRING_SIZE))
    sex = Column(String(STRING_SIZE))
    hompage = Column(String(STRING_SIZE))
    company = Column(String(STRING_SIZE))
    discount = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    address = relationship('Location', backref='contact', lazy=True)

    def __repr__(self):
        ''' DEBUG PRINT OUTPUT'''
        return '<Contact %r>' % (self.firstname+" "+self.lastname)
    
    def set_location(self, location):
        '''' update or create new location for self '''
        if Location.query.filter_by(contact_id=self.id).first() is None:
            location = Location(contact_id=self.id)
            db.session.add(location)
            db.sesson.commit()

        else:
            loc = Location.query.filter_by(id=location.get_id())
            loc = location
            db.session.commit()
    
    def set_primary_location(self, location):
        for addr in self.address:
            addr.is_primary = False
        location.is_primary = True

    def get_primary_location(self):
        return Location.query.filter_by(contact_id=self.id, is_primary = True).first()

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
    street = Column(String(STRING_SIZE))
    streetNumber = Column(String(STRING_SIZE))
    city = Column(String(STRING_SIZE))
    state = Column(String(STRING_SIZE))
    zip_code = Column(String(STRING_SIZE))
    #coordinates = Column(JSON)
    #customer_id = Column(Integer, ForeignKey('customer.id'))
    #user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact.id'), nullable=False)
    is_primary = Column(Boolean)

    def __repr__(self):
        ''' DEBUG PRINT OUTPUT'''
        return '<Location %r>' % (self.street+" "+self.id)

class Workpackage(db.Model, CustomBase):
    
    __tablename__ = 'workpackage'
    name = Column(String(STRING_SIZE))
    description = Column(Text)
    due_date = Column(DateTime())
    start_date = Column(DateTime())
    status = Column(String(STRING_SIZE))
    location_id = Column(Integer, ForeignKey('location.id'))
    discoutn = Column(Float)
    priority = Column(String(STRING_SIZE))
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
    name = Column(String(STRING_SIZE)) #Name of the shit
    amount = Column(Float)  #How much shit
    unit = Column(String(STRING_SIZE))  #Unit of shit
    description = Column(Text) # Shiti descripion
    value = Column(Float) #Cost of shit
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    @classmethod
    # get all task filtered by user_id
    def get_all(cls, user_id):
        return Task.query.filter_by(user_id=user_id).all()