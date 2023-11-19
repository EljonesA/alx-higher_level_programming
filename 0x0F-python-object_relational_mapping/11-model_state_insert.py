#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_louisiana(username, password, database):
    """
    Adds the State object "Louisiana" to the database hbtn_0e_6_usa
    and prints the new states.id after creation.
    """
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Add the State object "Louisiana" to the session
    new_state = State(name="Louisiana")
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Print the new states.id
    print(new_state.id)

    # Close the session
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
    add_louisiana(username, password, database)
