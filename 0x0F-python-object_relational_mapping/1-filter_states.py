#!/usr/bin/python3

"""
This script connects to a MySQL database and lists states
starting with 'N' from the specified database.

Usage:
    python script.py <username> <password> <database>

Arguments:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database containing
    the states table.
"""

import MySQLdb
import sys


def list_states_starting_with_N(username, password, database):
    """
    Connects to MySQL, lists states starting with 'N' from database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the states table.

    Returns:
        None. Prints the list of states starting with 'N' to the console.
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

        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

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

    list_states_starting_with_N(username, password, database)
