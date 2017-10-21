from sqlalchemy import Column, Integer, String
from .extensions import db
from .utils import create_salt, create_password_hash


class User(db):

    def __init__(self, user_name, user_password, user_email):
        """user created salt should be created automaticaly hear at user creation, the password should be hasched"""
        self.user_name = user_name
        self.user_email = user_email
        self.user_salt = create_salt()
        self.user_password = create_password_hash(user_password, self.user_salt)
        self.is_authenticated #https://flask-login.readthedocs.io/en/latest/#localization
        self.is_active
        self.is_anonymous


    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), index=True)
    user_password = Column(String(255))
    user_salt = Column(String(255))
    user_email = Column(String(120))

    def save(self, user):

        db.session.add(user)
        db.session.commit()

    @staticmethod
    def load(user_name):
        print(User.query.all())

    def check_login(self, username, password):
        pass

    def get_id(self):
        """This method must return a unicode that uniquely identifies this user,
         and can be used to load the user from the user_loader callback. Note that
          this must be a unicode - if the ID is natively an int or some other type,
           you will need to convert it to unicode."""
        pass

