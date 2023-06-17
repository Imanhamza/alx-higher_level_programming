#!/usr/bin/python3
''' A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. '''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect the database
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2],
            database=argv[3], host="localhost", port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # create the query and execute
    query = 'SELECT * FROM states WHERE name LIKE BINARY %s\
            ORDER BY id', (argv[4])
    cursor.execute(query)

    # fetch all rows in the result and print them all
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
