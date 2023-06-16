#!/usr/bin/python3
import MySQLdb
from sys import argv

''' A script that lists all states from the database hbtn_0e_0_usa '''


if __name__ == "__main__":
    # connect the database
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2],
            database=argv[3], host="localhost", port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # create the query and excute
    query = 'SELECT * FROM states ORDER BY id'
    cursor.execute(query)

    # fetch all rows in the result and print them all
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
