#!/usr/bin/python3
''' A script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa '''

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

    # Add new state object and commit changes
    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    print(state.id)

    session.close()
