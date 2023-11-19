#!/usr/bin/python3
"""
Script to list al states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py username password database
"""

# import required modules
import MySQLdb
import sys  # capture command line args


def display_states_filter_by_name(username, password, database):
    """
    Connects to the MySQL server and retrieves and prints all states
    where name starts with N from the 'states' table sorted by states.id.

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

    # execute (with condition), fetch and print the database records
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
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
    display_states_filter_by_name(username, password, database)
