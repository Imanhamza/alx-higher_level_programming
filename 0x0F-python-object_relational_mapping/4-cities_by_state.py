#!/usr/bin/python3
''' A script that lists all cities from the database hbtn_0e_4_usa'''

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
    query = '''SELECT c.id, c.name, s.name
    FROM states AS s
    JOIN cities AS c
    ON s.id = c.state_id
    ORDER BY c.id'''
    cursor.execute(query)

    # fetch all rows in the result and print them all
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
