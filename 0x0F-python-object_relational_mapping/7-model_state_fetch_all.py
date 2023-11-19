#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # create a configured session class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # Query all State objects, orde by id
    states = session.query(State).order_by(State.id).all()

    # display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

        # close the session
        session.close()
