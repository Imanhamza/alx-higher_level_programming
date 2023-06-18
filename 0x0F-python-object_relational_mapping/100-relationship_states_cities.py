#!/usr/bin/python3
''' A script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa '''

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

    # Add new state  and city object and commit changes
    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()
