from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from . import Osoba

engine = create_engine('sqlite:///database/Osoba.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

def get_users(session=session):
    return session.query(Osoba).all()


def create_and_update_user(pin_entry):
    pin_entry_from_db = (
        session.query(Osoba)
        .filter(
            and_(
                Osoba.prezime == pin_entry.prezime,
                Osoba.pin == pin_entry.pin,
                Osoba.ime == pin_entry.ime
            )
        ).one_or_none()
    )
    
    if pin_entry_from_db is not None:
        pin_entry_from_db.ime = pin_entry.ime
        pin_entry_from_db.prezime = pin_entry.prezime
        pin_entry_from_db.pin = pin_entry.pin
        
    else:
        pin_entry_from_db = pin_entry
        session.add(pin_entry_from_db)
    
    session.commit()


def delete_pin_entry(pin_entry):
    
    pin_entry_from_db = (
        session.query(Osoba)
        .filter(
            and_(
                Osoba.ime == pin_entry.ime,
                Osoba.prezime == pin_entry.prezime,
                Osoba.pin == pin_entry.pin,
            )
        ).one_or_none()
    )
    
    if pin_entry_from_db is not None:
        session.delete(pin_entry_from_db)
        session.commit()
        
        