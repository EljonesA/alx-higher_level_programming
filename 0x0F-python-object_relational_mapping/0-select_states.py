#!/usr/bin
# import required modules
import MySQLdb
import sys  # capture command line args

if __name__ == "__main__":
    # ensure correct number of args provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # capture the command line arguments
    username, password, database = sys.argv[1:]

    # create a connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # create a cursor object
    cursor = db.cursor()

    # execute, fetch and print the database records
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close the cursor & connection
    cursor.close()
    db.close()
