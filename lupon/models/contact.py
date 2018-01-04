from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, JSON, Boolean, Unicode, DateTime, Table
from sqlalchemy.orm import relationship
from lupon import db
import json
from flask import jsonify

from .base import CustomBase
from .location import Location
from .constants import STRING_SIZE

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
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'firstname': self.firstname, 
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone,
            'mobile': self.mobile,
            'fax': self.fax,
            'title': self.title,
            'sex': self.sex,
            'homepage': self.hompage,
            'company': self.company,
            'discount': self.discount,
        }

    @classmethod
    def tojson(self, user_id):
        return jsonify(json_list=[i.serialize for i in Contact.get_all(user_id)])
    
    @classmethod
    def get_all(cls, user_id):
        return Contact.query.filter_by(user_id=user_id).all()