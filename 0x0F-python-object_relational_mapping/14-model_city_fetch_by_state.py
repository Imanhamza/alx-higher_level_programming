#!/usr/bin/python3
''' A script that lists all State objects from the database hbtn_0e_6_usa '''

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    # Craete a connection sring
    connection_string = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # create engine and session
    engine = create_engine(connection_string)
    _session = sessionmaker(bind=engine)
    session = _session()

    # Query all cities and join states object and sort by city id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f'{state.name}: {city.id} {city.name}')

    session.close()
