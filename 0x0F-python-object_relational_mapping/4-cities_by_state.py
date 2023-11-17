#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        # Connecting database with parameters
        db_conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cursor = db_conn.cursor()

        # Executing SQL query
        cursor.execute('SELECT cities.id, cities.name, states.name FROM \
                       cities JOIN states ON cities.state_id = states.id \
                       ORDER BY cities.id ASC;')

        # fetching the results
        results = cursor.fetchall()

        # Displaying results
        for result in results:
            print(result)
        db_conn.close()
