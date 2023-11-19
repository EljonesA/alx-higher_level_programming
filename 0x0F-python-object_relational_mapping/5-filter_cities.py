#!/usr/bin/python3
"""
Script to list al cities of a specified state from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py username password database
"""

# import required modules
import MySQLdb
import sys  # capture command line args


def filter_cities_by_state(username, password, database, state_name):
    """
    Connects to the MySQL server and retrieves and prints all cities
    from the 'cities' table of the specifiwd state.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to filter cities.

    Returns:
        None
    """

    # create a connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # create a cursor object
    cursor = db.cursor()

    # execute, fetch and print the database records
    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC)
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))  # must be a tuple
    result = cursor.fetchone()
    if result and result[0]:
        print(result[0])
    else:
        print("No cities found for the specified state.")

    # close the cursor & connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Entry point of the script
    """
    # ensure correct number of args provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # capture the command line arguments
    username, password, database, state_name = sys.argv[1:]

    # call display_state function
    filter_cities_by_state(username, password, database, state_name)
