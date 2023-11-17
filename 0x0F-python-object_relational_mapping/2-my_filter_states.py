#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all..
values in the states table of hbtn_0e_0_usa where name matches..
the argument
"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        # connecting to MySQL Database by passing the arguments
        db_conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                )
        cursor = db_conn.cursor()

        # Assigning the value argument passed to state_name
        state_name = sys.argv[4]

        # Executing the SQL query
        cursor.execute(
            'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(state_name)
        )

        # fetching all the data
        results = cursor.fetchall()
        # Displaying the result
        for result in results:
            print(result)

        # closing the database
        db_conn.close()
