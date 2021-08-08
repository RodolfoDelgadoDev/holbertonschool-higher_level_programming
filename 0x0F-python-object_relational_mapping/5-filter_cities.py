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
    constable += "FROM states INNER JOIN cities "
    constable += "ON cities.state_id = states.id "
    constable += "WHERE states.name='{}' ".format(sys.argv[4])
    constable += "ORDER BY cities.id ASC"

    cursor.execute(constable)

    '''Get the results with method fetchall()'''

    results = cursor.fetchall()
    '''Print the results'''

    printear = ""
    for raw in results:
        printear += raw[1] + ", "

    print(printear[0:-2])
    '''Disconect'''
    database.close()
