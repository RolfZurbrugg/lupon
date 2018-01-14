import datetime
from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey

from .constants import STRING_SIZE


class CustomBase(object):
    ''' Define base atribuetes for all table '''
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_date = Column(DateTime(timezone=False), default=datetime.datetime.utcnow)
    modify_date = Column(DateTime(timezone=False))
    create_by = Column(String(STRING_SIZE), default="system")
    modify_by = Column(String(STRING_SIZE))
