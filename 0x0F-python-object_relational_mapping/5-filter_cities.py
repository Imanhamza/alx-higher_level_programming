#!/usr/bin/python3
''' A script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect the database
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2],
            database=argv[3], host="localhost", port=3306, charset="utf8")

    # Create a cursor object
    cursor = db.cursor()

    # create the query and execute
    query = 'SELECT c.name\
            FROM states AS s\
            JOIN cities AS c\
            ON s.id = c.state_id\
            WHERE s.name = %s\
            ORDER BY c.id'
    cursor.execute(query, (argv[4],))

    # fetch all rows in the result and print them all
    rows = cursor.fetchall()

    print(", ".join(city[0] for city in rows))
    #for i in range(len(rows)):
     #   if rows[i] != rows[-1]:
      #      print(''.join(rows[i]), end=', ')
       # else:
        #    print(''.join(rows[i]))
            # print(type(rows[i]))

    cursor.close()
    db.close()
