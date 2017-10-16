from sqlalchemy import Column, Integer, String
from lupon2.database import Base

class User(Base):
    __tablename__ = 'users'
    userId = Column(Integer, primary_key=True)
    userName = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name = None, email = None):
        self.naem = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)