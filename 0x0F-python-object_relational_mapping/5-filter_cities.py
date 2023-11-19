#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of a specified state from the database hbtn_0e_4_usa
    """

    # Create a connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the results as a tuple
    results = cursor.fetchall()

    # Check if any results were found
    if results:
        # Extract city names and join them into a comma-separated string
        cities = ', '.join(result[0] for result in results)
        print(cities)
    else:
        print("No cities found for the specified state.")

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Entry point of the script
    """

    # Ensure the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    # Capture the command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Call the function
    filter_cities_by_state(username, password, database, state_name)
