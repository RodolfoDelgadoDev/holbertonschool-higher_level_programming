#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys

'''Open database conection'''
if __name__ == "__main__":
    database = MySQLdb.connect("localhost", sys.argv[1],
                            sys.argv[2], sys.argv[3], port=3306)

    cuar = sys.argv[4]
    '''Cursor object with cursor() method'''
    cursor = database.cursor()

    '''Consulte the table and execute commands with execute() method'''
    cursor.execute("SELECT * FROM states WHERE name = %(n)s ORDER BY id ASC",
                {'n': sys.argv[4]})

    '''Get the results with method fetchall()'''

    results = cursor.fetchall()

    '''Print the results'''
    for raw in results:
        print(raw)

    '''Disconect'''
    database.close()
