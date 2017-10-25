import requests
# from flask import jsonify
from sqlalchemy import Column, ForeignKey, Integer, JSON, Boolean, Unicode, relationship
from sqlalchemy_utils import EmailType, PasswordType

class User(db.Model):
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    email = Column(
        EmailType, 
        unique=True, 
        nullable=False, 
        info={
            'label': 'eMail'  
        }
    )
    
    password = Column(
        PasswordType(
            schemes=['pbkdf2_sha512']
            ),
        info={ 'label': 'Password' },
        nullable=False
    )

    username = Column(String(80),
                      unique=True,
                      nullable=False,
                      info={'lable': 'Username'})

    locations = relationship('Location', backref='user', lazy='dynamic')

    company

    create_date
    last_login
    is_active = Boolean()
    subscription

    session_token
    
    locale

    def __init__(self, email, password):
        self.email = email
        self.password = password
 
    def __repr__(self):
        return '<User %r>' % self.email

    def __unicode__(self):
        pass

    def update(self):

        db.session.commit() 
        return 

    def serialize(self):
        return {
                'username': self.username, 
                'password': self.password,
                'email': self.email,
            }

    def is_active(self):
        return self.isActive

    def is_authenticated(self):
        pass
    
    def is_anonymus(self):
        pass

    def get_id(self):
        pass

    # classmethod example, src: http://blog.sampingchuang.com/setup-user-authentication-in-flask/
    @classmethod
    def exists(cls, user ):
       return db.session.query(db.exists().where(_or(User.email==user| User.user)).scalar()
    
    @classmethod 
    def authenticate(cls, user):
        pass