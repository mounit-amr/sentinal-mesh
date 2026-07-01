from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

DATABASE_URL = ""

engine = create_engine(DATABASE_URL)

Sessionlocal = sessionmaker (
    autocommit = False
    autoflush = False
    bind = engine
)


class Base(DeclarativeBase):
    pass

def get_db():
    db = Sessionlocal()
    try:
        yield db         #why not return db because it willnot automatically close the session but try: and yeild: would automatically close the db session
    finally:
        db.close
        
