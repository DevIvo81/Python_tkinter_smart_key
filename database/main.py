from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

engine = create_engine("sqlite:///PinStore_db.sqlite", echo=True)

Session = sessionmaker(bind=engine)

class Osoba(Base):
    __tablename__ = 'osobe'
    
    id = Column(Integer(), primary_key=True)
    ime = Column(String(25), nullable=False, unique=True)
    prezime = Column(String(25), nullable=False, unique=True)
    pin = Column(String(4), nullable=False, unique=True)
    
    def __repr__(self) -> str:
        return f'''{self.ime} {self.prezime}'''
    

