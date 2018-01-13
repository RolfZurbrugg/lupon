import datetime
from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .constants import STRING_SIZE

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('workpackage.id')),
    Column('right_id', Integer, ForeignKey('task.id'))
)

class CustomBase(object):
    ''' Define base atribuetes for all table '''
    
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime(timezone=False), default=datetime.datetime.utcnow)
    modify_date = Column(DateTime(timezone=False))
    create_by = Column(String(STRING_SIZE), default="system")
    modify_by = Column(String(STRING_SIZE))
