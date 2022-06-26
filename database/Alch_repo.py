from .main import Osoba, engine, Session, Base

local_session = Session()

def create_db():    
    
    Base.metadata.create_all(engine)
    
    osobe = [
        {
            'ime' : 'Ivo',
            'prezime' : 'Ivić',
            "pin" : '1111'
        },
        {
            'ime' : 'Ana',
            'prezime' : 'Anić',
            "pin" : '2222'
        },
        {
            'ime' : 'Mara',
            'prezime' : 'Marić',
            "pin" : '3333'
        },
        {
            'ime' : 'Admin',
            'prezime' : 'Adminić',
            "pin" : '1234'
        }
    ]
    
    for o in osobe:
        nova_osoba = Osoba(
                        ime = o['ime'], 
                        prezime = o['prezime'], 
                        pin = o['pin'])
        local_session.add(nova_osoba)
        local_session.commit()


def add_person(novo_ime, novo_prezime, novi_pin):
    nova_osoba = Osoba(
                        ime = novo_ime, 
                        prezime = novo_prezime, 
                        pin = novi_pin)        
    local_session.add(nova_osoba)    
    local_session.commit()


def all_persons():
    persons_in_db = local_session.query(Osoba).all()
    return persons_in_db


def pin_to_compare(entry_pin):
    pin_from_db = local_session.query(Osoba)\
                                .filter(Osoba.pin == entry_pin).first()
    return pin_from_db
print(pin_to_compare())

def delete_person(name):
    user_to_delete = local_session.query(Osoba)\
                .filter(Osoba.ime == name).first()

    local_session.delete(user_to_delete)
    local_session.commit()




