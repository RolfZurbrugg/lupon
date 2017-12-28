'''
THIS MODULE IS STILL UNTESTED
putting some crypto toools in this utils class
'''
from .decorators import async
import hashlib
import uuid
from lupon import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import MetaData, ForeignKeyConstraint, Table, DropConstraint, DropTable
from sqlalchemy.engine import reflection

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

def initDB():
    from lupon import app, db
    from lupon import models
    #db.drop_all()
    db_DropEverything(db)
    db.create_all()

def initdb():
    initDB()
    
def create_salt():
    return uuid.uuid4().hex

def create_password_hash(password, salt):
    return hashlib.sha512(password + salt).hexdigest()

''' FROM  https://www.mbeckler.org/blog/?p=218 '''
def db_DropEverything(db):
    # From http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything

    conn=db.engine.connect()

    # the transaction only applies if the DB supports
    # transactional DDL, i.e. Postgresql, MS SQL Server
    trans = conn.begin()

    inspector = reflection.Inspector.from_engine(db.engine)

    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in 
    # a transaction.
    metadata = MetaData()

    tbs = []
    all_fks = []

    for table_name in inspector.get_table_names():
        fks = []
        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(
                ForeignKeyConstraint((),(),name=fk['name'])
                )
        t = Table(table_name,metadata,*fks)
        tbs.append(t)
        all_fks.extend(fks)

    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))

    for table in tbs:
        conn.execute(DropTable(table))

    trans.commit()
    