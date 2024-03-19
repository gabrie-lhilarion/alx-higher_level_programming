#!/usr/bin/python3

"""
Module: list_states

This module provides functionality to connect to a
MySQL database and list all states
from the 'states' table.

Usage:
    This module can be imported and used to retrieve
    and display states from a MySQL database.

Example:
    from list_states import list_states

    # Provide MySQL credentials
    username = "root"
    password = "password"
    database = "my_database"

    # Call the list_states function
    list_states(username, password, database)
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to a MySQL database and lists all states.

    This function connects to a MySQL server using the provided username,
    password, and database name. It executes a SQL query to retrieve all
    states from the 'states' table in the database, orders them by ID
    in ascending order, fetches all results, and prints them to the console.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.

    Returns:
        None
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

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

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

    list_states(username, password, database)
