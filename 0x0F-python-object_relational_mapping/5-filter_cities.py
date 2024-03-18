#!/usr/bin/python3

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
        # Connect to MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()

        # Construct SQL query with parameterized query to prevent SQL injection
        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """

        # Execute query with user input as parameter
        cursor.execute(query, (state_name,))

        # Fetch all results
        cities = cursor.fetchall()

        # Display results
        city_names = [city[0] for city in cities]
        print(", ".join(city_names))

        # Close cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the list_cities_by_state function with provided arguments
    list_cities_by_state(username, password, database, state_name)
