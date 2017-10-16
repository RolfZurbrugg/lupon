from sqlalchemy import Column, String, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .app import db

Base = declarative_base()

class Person(Base):
    """
    Defines persons class
    """
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(256), nullable=False)
    lastname = Column(String(256), nullable=False)
    email = Column(String(256))
    phone = Column(String(256))
    location_id = Column(ForeignKey('location.id'))
    location = relationship("Location", backref="location")

    def name(self):
        """
        returns surname + lastname
        """
        return self.surename +" "+ self.lastname

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(256))
    city = Column(String(256))
    plz = Column(String(256))

class Customer(Person):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    person = Column(ForeignKey('person.id'))
    location = Column(ForeignKey('location.id'))
    history = relationship("History")

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    person = Column(ForeignKey('person.id'))
    person_id = 
    entry = Column(Text())