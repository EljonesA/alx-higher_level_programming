#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

# import required modules
import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL server and retrieves and prints all states
    from the 'states' table where the name matches the provided state_name,
    sorted by states.id.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): State name to search for.

    Returns:
        None
    """

    # create connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # create cursor obect
    cursor = db.cursor()

    # execute SELECT query with WHERE clause
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # fetch all rows
    rows = cursor.fetchall()

    # display the results
    for row in rows:
        print(row)

    # close connection/cursor
    cursor.close()
    db.close()


if __name__ == "__main__":
    """ Script entry point """
    # ensure correct number of args
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format
              (sys.argv[0]))
        sys.exit(1)

    # capture coomand line args
    username, password, database, state_name = sys.argv[1:]

    # call filter states function
    filter_states_by_name(username, password, database, state_name)
