#!/usr/bin/python3

"""
Connects to MySQL, lists all cities of the specified
state from the database.

Returns:
    None. Prints the list of cities for the specified
    state to the console.
"""


import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    """
    Connects to MySQL, lists all cities of the specified
    state from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing
        the cities and states tables.
        state_name (str): Name of the state to list cities for.

    Returns:
        None. Prints the list of cities for the specified
        state to the console.
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
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """

        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()

        city_names = [city[0] for city in cities]
        print(", ".join(city_names))

        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database, state_name)
