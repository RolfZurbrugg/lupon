from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, JSON, Boolean, Unicode, DateTime, Table
from sqlalchemy.orm import relationship
from lupon import db

from .base import CustomBase
from .constants import STRING_SIZE

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


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'amount': self.amount,
            'unit': self.unit,
            'description': self.description,
            'value': self.value,
            'create_date': self.create_date,
            'modify_date': self.modify_date,
            'created_by': self.create_by,
            'modify_by': self.modify_by,
            'id': self.id
        }
