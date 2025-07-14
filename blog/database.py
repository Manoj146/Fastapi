from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

sql_db='sqlite:///./blog.db'

engine= create_engine(sql_db,connect_args={"check_same_thread": False}) 

Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base=declarative_base() 


def get_db():
    db=Sessionlocal()
    try:
        yield db 
    finally:
        db.close()