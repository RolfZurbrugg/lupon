from sqlalchemy import Column, String, ForeignKey, Integer, Text, Float, JSON, Boolean, Unicode, DateTime, Table
from sqlalchemy.orm import relationship
from lupon import db

from .base import CustomBase
from .constants import STRING_SIZE

association_table = Table('workpackage_task', db.Model.metadata,
    Column('workpackage_id', Integer, ForeignKey('workpackage.id')),
    Column('task_id', Integer, ForeignKey('task.id'))
)

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