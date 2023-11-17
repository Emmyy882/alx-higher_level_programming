#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and \
        lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        # Connecting to MySQL Database
        db_conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cursor = db_conn.cursor()
        state_name = sys.argv[4]

        # Executing the SQL query
        cursor.execute(
            'SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE CAST(states.name AS BINARY) = %s \
            ORDER BY cities.id ASC;',
            [state_name]
        )

        # Fetching the result
        results = cursor.fetchall()

        # Displaying the result
        for result in results:
            print(result)
        db_conn.close()
