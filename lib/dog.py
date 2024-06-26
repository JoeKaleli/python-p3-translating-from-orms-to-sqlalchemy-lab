from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

def create_table(engine):
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

# Create engine
engine = create_engine('sqlite:///dogs.db')

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create table
create_table(engine)
