#!/usr/bin/python3
"""
Script to change the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state_name(username, password, database):
    """
    Changes the name of the State where id = 2 to New Mexico.
    """
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

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
    update_state_name(username, password, database)
