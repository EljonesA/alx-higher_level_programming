#!/usr/bin/python3
"""
Script to list all State objects containing the letter a from the database
hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_states_by_letter_a(username, password, database):
    """
    that lists all State objects that contain the letter a from the database
    hbtn_0e_6_usa
    """
    # connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, database),
                           pool_pre_ping=True)

    # create a configured session class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # Query State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%'))
    .order_by(State.id).all()

    # display results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()


if __name__ == "__main__":
    """ Entry of the program """

    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Capture the command line arguments
    username, password, database = sys.argv[1:]

    # Call the function
    filter_states_by_letter_a(username, password, database)
