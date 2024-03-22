#!/usr/bin/python3

"""
Connects to MySQL, searches for specified state name
in states table.

Usage:
    ./script.py <username> <password> <database> <name>

Arguments:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database containing the states table.
    state_name (str): Name of the state to search for.
"""

import MySQLdb
import sys


def search_states(username, password, database, state_name):
    """
    Connects to MySQL, searches for specified state name in states table.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the states table.
        state_name (str): Name of the state to search for.

    Returns:
        None. Prints the matching states to the console.
    """
    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()

        query = ("SELECT * FROM states "
                 "WHERE name = '{}' "
                 "ORDER BY id ASC").format(state_name)

        cursor.execute(query)

        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, database, state_name)
