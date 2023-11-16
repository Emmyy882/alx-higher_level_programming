#!/usr/bin/python3
"""A script that lists all rows of the states field in a database"""
import sys
import MySQLdb


if __name__ == '__main__':
    if sys.argv >= 4:
        db_conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cursor = db.cursor()
        cursor.execute('SELECT * FROM states ORDER BY id ASC;')
        results = cursor.fetchall()
        for result in results:
            print(result)
        db_conn.close()
