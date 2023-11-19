#!/usr/bin/python3
"""
Script to print the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_id_by_name(username, password, database, state_name):
    """
    Prints the State object's id with the specified name from the database
    hbtn_0e_6_usa.
    """
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query State object's id by name
    result = session.query(State.id).filter(State.name == state_name).first()

    # Display results
    if result:
        print(result[0])
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    """ Entry of the program """

    # Ensure correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)

    # Capture the command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Call the function
    get_state_id_by_name(username, password, database, state_name)
