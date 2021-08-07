#!/usr/bin/python3
'''Script that lists all cities from the database hbtn_0e_4_usa'''
import MySQLdb
import sys

'''Open database conection'''

if __name__ == "__main__":
    database = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2],
                               sys.argv[3], port=3306)

    '''Cursor object with cursor() method'''
    cursor = database.cursor()

    '''Take the table and execute commands with execute() method'''
    constable = "SELECT cities.id, cities.name, states.name "
    constable += "FROM cities INNER JOIN states "
    constable += "ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(constable)

    '''Get the results with method fetchall()'''

    results = cursor.fetchall()
    '''Print the results'''

    for raw in results:
        print(raw)

    '''Disconect'''
    database.close()
