#!/usr/bin/python3

"""
Connects to MySQL, lists all cities from the specified
database with their respective states.

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the MySQL database containing
    the cities and states tables.

Returns:
    None. Prints the list of cities with their respective
    states to the console.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Connects to MySQL, lists all cities from the specified
    database with their respective states.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing
        the cities and states tables.

    Returns:
        None. Prints the list of cities with their respective
        states to the console.
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

        query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """

        cursor.execute(query)
        cities = cursor.fetchall()

        for city in cities:
            print(city)

        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
