#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_state(username, password, database):
    """
    Prints all City objects from the database hbtn_0e_14_usa
    """
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects, ordered by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Display results
    for city in cities:
        state_name = session.query(State).filter_by(id=city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

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
    fetch_cities_by_state(username, password, database)
