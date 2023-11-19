#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_letter_a(username, password, database):
    """
    Deletes all State objects with a name containing the letter 'a'
    """
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query State objects with a name containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the queried states
    for state in states_with_a:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    """ Entry of the program """

    # Ensure the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Capture the command line arguments
    username, password, database = sys.argv[1:]

    # Call the function
    delete_states_with_letter_a(username, password, database)
