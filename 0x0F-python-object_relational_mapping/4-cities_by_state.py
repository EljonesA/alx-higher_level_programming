#!/usr/bin/python3
"""
Script to list al cities from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py username password database
"""

# import required modules
import MySQLdb
import sys  # capture command line args


def display_cities_by_state(username, password, database):
    """
    Connects to the MySQL server and retrieves and prints all cities
    from the 'cities' table with their corrsponding state names
    sorted by states.id.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

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
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

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
    username, password, database = sys.argv[1:]

    # call display_state function
    display_cities_by_state(username, password, database)