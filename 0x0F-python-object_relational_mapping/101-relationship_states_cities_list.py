#!/usr/bin/python3
''' A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa '''

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Craete a connection sring
    con_str = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'

    # create engine and session
    engine = create_engine(con_str)
    Base.metadata.create_all(engine)

    _session = sessionmaker(bind=engine)
    session = _session()

    # Query all states and cities
    states = session.query(State).outerjoin(
            City).order_by(State.id, City.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')

    session.close()
