#!/usr/bin/python3
''' A script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa '''

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Craete a connection sring
    connection_string = f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # create engine and session
    engine = create_engine(connection_string)
    _session = sessionmaker(bind=engine)
    session = _session()

    # find all state object, delete and commit changes
    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)
    session.commit()

    session.close()
