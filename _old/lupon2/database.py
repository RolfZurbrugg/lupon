from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declaretive import declarative_base


engine = create_engine('mariadb:////Users//Rolf//gitHub//semester5//Lupon//lupon//lubon.db', convert_unicoe=True)
db_session = scoped_session(sessionmaker(autocommit=false,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.qyery_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import yourapplication.models
    Base.metadata.create_all(bind=engine)