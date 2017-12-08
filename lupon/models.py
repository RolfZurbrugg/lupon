'''
This module contains all classes requeried for Database Model
'''
from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, Boolean, Unicode, Date, Table
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from . import app, flask_bcrypt, db


''' Associaction table between workpackages and tasks '''
association_table = Table('workpackage_task',db.Model.metadata,
    Column('workpackage_id', Integer, ForeignKey('workpackage.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
)

class CustomBase(object):
    ''' Define base atribuetes for all table '''
    
    id = Column(Integer, primary_key=True)
    create_date = Column(Date(), nullable=False)
    modify_date = Column(Date())
    creat_by = Column(String(256), nullable=False)
    modify_by = Column(String(256), nullable=False)

class User(db.Model, UserMixin):
    '''User Datatable'''

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    email = Column(
            String(120), 
            unique=True, 
            nullable=False, 
            info={'validators': Email(),
                'label': 'Name' 
            }
    )
    password = Column(
            String(80),
            nullable=False,
            info={ 'label': 'Password' }
    )
    
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    
    # locations = relationship('Location', backref='user', lazy='dynamic')
     
    def __init__(self, email, password):
        self.email = email
        self.password = flask_bcrypt.generate_password_hash(password)
 
    def __repr__(self):
        return '<User %r>' % self.email

    def email_exists(self):
        if db.session.query(User.id).filter_by(email=self.email).scalar() is not None:
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


class Location(db.Model, CustomBase):
    '''
     Location Datatable

    '''

    __tablename__ = 'location'

    street = Column(String(256))
    streetNumber = Column(Integer)
    city = Column(String(256))
    state = Column(String(256))
    zip = Column(String(256))
    contact_id = Column(Integer, ForeignKey('contact.id'), nullable=False)

    def __repr__(self):
        pass
    '''
    def __init__(self, street, city, plz, contact_id):
        self.street = street
        self.city = city
        self.plz = plz
        self.coordinates = self.get_cordiantes()
    '''
    
class Task(db.Model, CustomBase):
    ''' Tasks Datatable'''

    __tablename__ = 'task'

    name = Column(String(256))
    description = Column(Text)
    due_date = Column(Date)
    start_date = Column(Date)
    status = Column(String(256))
    discoutn = Column(Float)
    priority = Column(String(256))
    comment = Column(Text)

    location_id = Column(Integer, ForeignKey('location.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    contact_id = Column(Integer, ForeignKey('contact.id'))
    tasks = relationship('Task', secondary=association_table)

    def total_houres(self):
        pass

    def total_value(self):
        pass

    def get_work_packages(self):
        #load all workpakages linked to this task
        pass


class Workpackage(db.Model, CustomBase):
    ''' Work pakcages Datatable'''

    __tablename__ = 'workpackage'
    
    name = Column(String(256)) #Name of the shit
    amount = Column(Float)  #How much shit
    unit = Column(String(256))  #Unit of shit
    description = Column(Text) # Shiti descripion
    value = Column(Float) #Cost of shit

class Task(object):
    pass

'''
@SOURCE http://zqsmm.qiniucdn.com/data/20140904220136/index.html
'''

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
 
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.user_id = g.user.id
 
    def __repr__(self):
        return '<Post %r>' % self.title
