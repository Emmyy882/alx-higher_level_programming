#!/usr/bin/python3
"""
A script that lists all the data in the state field starting with N
...from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        db_conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cursor = db_conn.cursor()
        cursor.execute(
            'SELECT * FROM states WHERE name IS NOT NULL AND' +
            ' LEFT(CAST(name AS BINARY), 1) = "N" ORDER BY states.id ASC;'
        )
        results = cursor.fetchall()
        for result in results:
            print(result)
        db_conn.close()
