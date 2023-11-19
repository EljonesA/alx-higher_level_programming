#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state(username, password, database):
    # connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, database),
                           pool_pre_ping=True)

    # create a configured session class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # close the session
    session.close()


if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Capture the command line arguments
    username, password, database = sys.argv[1:]

    # Call the function
    print_first_state(username, password, database)
